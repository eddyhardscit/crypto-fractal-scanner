"""Read-only projection of authoritative SOL cone artifacts; no model imports."""
from __future__ import annotations

import csv
import io
import json
import math
import re
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from statistics import median
from zoneinfo import ZoneInfo

LOCAL_ZONE = ZoneInfo('Europe/Madrid')
HORIZONS = (90, 180, 365, 730)
QUANTILES = (10, 25, 50, 75, 90)
THRESHOLDS = (150, 200, 250, 300, 400, 500, 600, 800, 1000)
FIELDS = ['date_local', 'generated_at', 'cohort_sha256', 'spot_sol',
          'canonical_cohort_count', 'distinct_assets', 'raw_episode_count']
for _h in HORIZONS:
    FIELDS += [f'h{_h}_p{q}' for q in QUANTILES]
    FIELDS += [f'h{_h}_p_ge_{v}' for v in THRESHOLDS]
    FIELDS += [f'h{_h}_distinct_assets', f'h{_h}_raw_episode_count']
FIELDS += ['h365_stability', 'source_kind']
VINTAGE_FIELDS = ['forecast_date', 'target_horizon_days', 'target_date',
                  'spot_at_forecast', 'p10', 'p25', 'p50', 'p75', 'p90',
                  'p_ge_200', 'p_ge_300', 'p_ge_500', 'p_ge_800', 'cohort_sha256']
TEXT_FIELDS = {'date_local', 'generated_at', 'cohort_sha256', 'h365_stability', 'source_kind'}


class HistoryError(ValueError):
    pass


def number(value):
    if isinstance(value, bool):
        return None
    try:
        result = float(value)
    except (TypeError, ValueError):
        return None
    return result if math.isfinite(result) else None


def timestamp(value):
    try:
        result = datetime.fromisoformat(str(value).replace('Z', '+00:00'))
        if result.tzinfo is None:
            raise ValueError('timezone missing')
        return result.astimezone(timezone.utc)
    except (ValueError, TypeError) as exc:
        raise HistoryError('invalid snapshot timestamp') from exc


def one_year_stability(report):
    """Same diagnostic classification already used by the deployed summary."""
    try:
        h = report['horizons']['365']
        b = h['bootstrap_ci90']['LOG_ROBUST_TAIL']
        y = h['leave_one_year_out']['LOG_ROBUST_TAIL']
        vals = [number(v['LOG_ROBUST_TAIL']['p50']) for v in report['similarity_sensitivity']['365'].values()]
        bounds = [number(b['p50_ci90_low']), number(b['p50_ci90_high']), number(y['p50_min']), number(y['p50_max'])]
        if not vals or None in vals + bounds:
            return 'N/D'
        count = sum([bounds[0] < 0 < bounds[1], bounds[2] < 0 < bounds[3], max(vals)-min(vals) >= 25])
        return 'UNSTABLE' if count >= 2 else 'CAUTION' if count else 'STABLE'
    except (KeyError, TypeError, AttributeError):
        return 'N/D'


def normalize_snapshot(record, report=None):
    generated = str(record.get('generated_at', ''))
    instant = timestamp(generated)
    sha = str(record.get('cohort_sha256', ''))
    if not re.fullmatch(r'[0-9a-f]{64}', sha):
        raise HistoryError('missing authoritative cohort hash')
    spot = number(record.get('current_sol_price'))
    count = number(record.get('canonical_cohort_count'))
    if spot is None or spot <= 0 or count is None or not 0 < count <= 40:
        raise HistoryError('invalid spot or cohort size')
    row = dict.fromkeys(FIELDS)
    row.update(date_local=instant.astimezone(LOCAL_ZONE).date().isoformat(), generated_at=generated,
               cohort_sha256=sha, spot_sol=spot, canonical_cohort_count=int(count),
               h365_stability='N/D', source_kind='history_jsonl')
    if report is not None:
        if report.get('role') != 'DIAGNOSTIC_ONLY' or report.get('target') != 'SOL-USD':
            raise HistoryError('invalid report role or target')
        if timestamp(report.get('generated_at_utc')) != instant:
            raise HistoryError('report timestamp mismatch')
        report_spot = number(report.get('current_price'))
        if report_spot is None or not math.isclose(report_spot, spot, rel_tol=1e-10):
            raise HistoryError('report spot mismatch')
        row.update(source_kind='full_snapshot', h365_stability=one_year_stability(report))
    for h in HORIZONS:
        short = record.get('horizons', {}).get(str(h), {})
        for q in QUANTILES:
            row[f'h{h}_p{q}'] = number(short.get(f'log_robust_p{q}_price'))
        for v in THRESHOLDS:
            row[f'h{h}_p_ge_{v}'] = number(short.get(f'p_ge_{v}'))
        row[f'h{h}_raw_episode_count'] = number(record.get('raw_episode_count', {}).get(str(h)))
        if report is not None:
            item = report.get('horizons', {}).get(str(h))
            if not isinstance(item, dict) or 'LOG_ROBUST_TAIL' not in item.get('distributions', {}):
                raise HistoryError('missing LOG_ROBUST_TAIL horizon')
            metric = item['distributions']['LOG_ROBUST_TAIL'].get('final_return', {})
            prices = metric.get('implicit_sol_prices', {})
            probs = item.get('empirical_price_threshold_probabilities', {}).get('LOG_ROBUST_TAIL', {})
            for q in QUANTILES:
                val = number(prices.get(f'p{q}'))
                prior = row[f'h{h}_p{q}']
                if val is not None and prior is not None and not math.isclose(val, prior, rel_tol=1e-10):
                    raise HistoryError('snapshot and history disagree')
                row[f'h{h}_p{q}'] = val
            for v in THRESHOLDS:
                val = number(probs.get(f'p_sol_ge_{v}'))
                prior = row[f'h{h}_p_ge_{v}']
                if val is not None and prior is not None and not math.isclose(val, prior, rel_tol=1e-10):
                    raise HistoryError('snapshot and history probabilities disagree')
                row[f'h{h}_p_ge_{v}'] = val
            row[f'h{h}_distinct_assets'] = number(item.get('distinct_assets'))
            row[f'h{h}_raw_episode_count'] = number(item.get('raw_episodes'))
        available = [row[f'h{h}_p{q}'] for q in QUANTILES if row[f'h{h}_p{q}'] is not None]
        if any(v <= 0 for v in available) or available != sorted(available):
            raise HistoryError('invalid price quantiles')
        if any(row[f'h{h}_p_ge_{v}'] is not None and not 0 <= row[f'h{h}_p_ge_{v}'] <= 100 for v in THRESHOLDS):
            raise HistoryError('probability outside 0–100')
    if any(row[f'h{h}_p50'] is None for h in (180,365,730)):
        raise HistoryError('missing core median')
    row['distinct_assets'] = row['h90_distinct_assets']
    row['raw_episode_count'] = row['h90_raw_episode_count']
    return row


def discover_snapshots(reports_dir, *, now=None):
    """Join real full snapshots to their authoritative JSONL provenance by timestamp.

    Missing archives use only fields actually present in JSONL. Corrupt full
    snapshots are excluded, never substituted by an invented or smoothed record.
    """
    root = Path(reports_dir)
    now = now or datetime.now(timezone.utc)
    history_path = root / 'sol_long_term_probability_cone_history.jsonl'
    records = []
    for index, line in enumerate(history_path.read_text(encoding='utf-8').splitlines(), 1):
        if line.strip():
            try:
                item = json.loads(line)
                if not isinstance(item, dict):
                    raise ValueError()
                records.append(item)
            except (ValueError, TypeError) as exc:
                raise HistoryError(f'invalid history JSONL line {index}') from exc
    full = {}
    for path in sorted((root/'sol_long_term_probability_cone_history').glob('*/sol_long_term_probability_cone.json')):
        try:
            payload = json.loads(path.read_text(encoding='utf-8'))
            key = timestamp(payload.get('generated_at_utc'))
            if key in full and full[key] != payload:
                raise HistoryError('conflicting full snapshots for one timestamp')
            full[key] = payload
        except (OSError, json.JSONDecodeError, AttributeError):
            continue
    current_path = root/'sol_long_term_probability_cone.json'
    current = json.loads(current_path.read_text(encoding='utf-8'))
    current_key = timestamp(current.get('generated_at_utc'))
    if current_key in full and full[current_key] != current:
        raise HistoryError('latest report conflicts with immutable snapshot')
    full[current_key] = current
    provenance = {}
    for record in records:
        key = timestamp(record.get('generated_at'))
        if key in provenance and provenance[key] != record:
            raise HistoryError('conflicting snapshot provenance')
        provenance[key] = record
    rows, warnings, seen = [], [], {}
    for record in records:
        try:
            key = timestamp(record.get('generated_at'))
            if key > now:
                raise HistoryError('future-dated snapshot')
            row = normalize_snapshot(record, full.get(key))
            if key in seen and row != seen[key]:
                raise HistoryError('conflicting snapshot provenance')
            if key not in seen:
                rows.append(row)
                seen[key] = row
        except (HistoryError, TypeError, AttributeError) as exc:
            warnings.append(str(exc))
    if not rows:
        raise HistoryError('no qualifying real snapshot')
    rows.sort(key=lambda r: timestamp(r['generated_at']))
    if current_key not in seen:
        raise HistoryError('latest report lacks valid authoritative history provenance')
    return rows, seen[current_key], warnings


def select_daily(snapshots):
    """Last qualifying real snapshot per Madrid date, before first ledger commit."""
    selected = {}
    for row in sorted(snapshots, key=lambda r: timestamp(r['generated_at'])):
        selected[row['date_local']] = row
    return [selected[key] for key in sorted(selected)]


def read_daily_csv(path):
    path = Path(path)
    if not path.exists():
        return []
    with path.open(newline='', encoding='utf-8') as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != FIELDS:
            raise HistoryError('unexpected daily ledger schema')
        rows = [{k: (v or None) if k in TEXT_FIELDS else number(v) for k,v in row.items()} for row in reader]
    dates = [r['date_local'] for r in rows]
    if dates != sorted(set(dates)):
        raise HistoryError('duplicate or unordered daily dates')
    for row in rows:
        if timestamp(row['generated_at']).astimezone(LOCAL_ZONE).date().isoformat() != row['date_local']:
            raise HistoryError('daily date does not match snapshot')
    return rows


def merge_daily(existing, snapshots):
    """Committed rows are immutable, including on same-day reruns."""
    known = {r['date_local'] for r in existing}
    cutoff = existing[-1]['date_local'] if existing else ''
    new = [r for r in select_daily(snapshots) if r['date_local'] not in known and r['date_local'] > cutoff]
    return list(existing) + new


def vintages(rows):
    result = []
    for row in rows:
        for h in HORIZONS:
            result.append(dict(forecast_date=row['date_local'], target_horizon_days=h,
                target_date=(date.fromisoformat(row['date_local'])+timedelta(days=h)).isoformat(),
                spot_at_forecast=row['spot_sol'], cohort_sha256=row['cohort_sha256'],
                **{f'p{q}': row.get(f'h{h}_p{q}') for q in QUANTILES},
                **{f'p_ge_{v}': row.get(f'h{h}_p_ge_{v}') for v in (200,300,500,800)}))
    return result


def csv_bytes(rows, fields, *, header=True):
    out = io.StringIO(newline='')
    writer = csv.DictWriter(out, fields, lineterminator='\n')
    if header:
        writer.writeheader()
    writer.writerows(rows)
    return out.getvalue().encode('utf-8')


def metric(values):
    vals = [v for x in values if (v := number(x)) is not None]
    if not vals:
        return dict(median=None, min=None, max=None, range=None, range_pct=None)
    med, lo, hi = median(vals), min(vals), max(vals)
    return dict(median=med, min=lo, max=hi, range=hi-lo, range_pct=(hi-lo)/abs(med)*100 if med else None)


def classify_drift(p50_range_pct, p300_range_pp):
    if (p50_range_pct is not None and p50_range_pct >= 40) or (p300_range_pp is not None and p300_range_pp >= 20):
        return 'VOLATILE'
    if p50_range_pct is not None and p300_range_pp is not None and p50_range_pct < 20 and p300_range_pp < 10:
        return 'STABLE'
    return 'CAUTION'


def recent_statistics(rows):
    keys = ('h180_p50','h365_p50','h730_p50','h730_p_ge_300','h730_p_ge_500')
    rows = sorted(rows, key=lambda r: r['date_local'])
    if rows:
        latest = date.fromisoformat(rows[-1]['date_local'])
        old_candidates = [r for r in rows if date.fromisoformat(r['date_local']) <= latest-timedelta(days=7)]
        old = old_candidates[-1] if old_candidates else rows[0]
        window = [r for r in rows if date.fromisoformat(r['date_local']) >= latest-timedelta(days=29)]
    else:
        old_candidates, window, old = [], [], None
    metrics = {k: metric(r.get(k) for r in window) for k in keys}
    return dict(trend_old=old, trend_new=rows[-1] if rows else None,
        short_7d=not bool(old_candidates), short_30d=len({r['date_local'] for r in window}) < 30,
        window_rows=window, metrics=metrics,
        drift_status=classify_drift(metrics['h730_p50']['range_pct'],metrics['h730_p_ge_300']['range']))
