"""Legacy-compatible shared signatures, canonical imports and descriptive statistics."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.spatial.distance import cosine

import forecast_provenance as fp
import scanner as legacy

QUANTILES = (10, 25, 50, 75, 90)
HORIZONS = (7, 14, 30, 60)
EVALUATION_DAYS = (1, 3, 7, 14, 30, 60)
LEGACY_IDS = {'BTC-USD': 'bitcoin', 'SOL-USD': 'solana', 'DOGE-USD': 'dogecoin'}
SEMANTICS = 'CLOSE_ONLY_LEGACY_COMPATIBLE'


def digest(value):
    return hashlib.sha256(fp.canonical_json(value)).hexdigest()


def read_jsonl(path):
    return fp._read_jsonl(Path(path))


def load_legacy_inputs(reports, as_of):
    """Require one complete canonical scanner run; never rescan canonical assets."""
    records = [r for r in read_jsonl(reports / 'forecast_provenance/forecast_versions.jsonl')
               if r['forecast_date'] == as_of and r['asset'] in LEGACY_IDS]
    canonical = {}
    for ticker in LEGACY_IDS:
        candidates = [r for r in records if r['asset'] == ticker]
        if not candidates:
            raise ValueError('MISSING_CANONICAL_FORECAST:' + ticker)
        canonical[ticker] = max(candidates, key=lambda r: (r['generated_at_utc'], r['forecast_id']))
    runs = {r['run_id'] for r in canonical.values()}
    if len(runs) != 1:
        raise ValueError('MIXED_CANONICAL_RUNS')
    run_id = next(iter(runs))
    snapshots = {r['ticker']: r['snapshot_id'] for r in read_jsonl(fp.RAW_INDEX)
                 if r['run_id'] == run_id and r['purpose'] == 'forecast_generation_and_evaluation'}
    # Missing run membership cannot be inferred from an unrelated cached download.
    raw, processed = {}, {}
    for ticker in legacy.CRYPTO_TICKERS:
        if ticker not in snapshots:
            continue
        raw[ticker] = fp.load_frozen_ohlc(snapshots[ticker])
        if len(raw[ticker]) > 300:
            frame = legacy.add_indicators(raw[ticker])
            if len(frame) > 250:
                processed[ticker] = frame
    for ticker, record in canonical.items():
        if snapshots.get(ticker) != record['raw_market_snapshot_id']:
            raise ValueError('CANONICAL_TARGET_SNAPSHOT_MISMATCH:' + ticker)
        cohort_hash = record['cohort_id'].split(':', 1)[1]
        cohort = json.loads((fp.COHORT_DIR / (cohort_hash + '.json')).read_text())
        body = {k: cohort[k] for k in ('schema_version', 'target', 'cases_used', 'matches')}
        if digest(body) != cohort_hash or cohort['target'] != ticker:
            raise ValueError('CANONICAL_COHORT_HASH_MISMATCH')
        record['cohort'] = cohort['matches']
        anchor = fp.load_frozen_ohlc(record['price_market_snapshot_id'])
        if len(anchor) != 1 or not np.isclose(float(anchor.Close.iloc[0]), float(record['current_price']), rtol=0, atol=1e-12):
            raise ValueError('CANONICAL_ANCHOR_MISMATCH')
        record['anchor_date'] = anchor.index[0].date().isoformat()
    return raw, processed, snapshots, canonical


class SharedSignatureIndex:
    """Same enumeration, scalar scipy cosine and pandas sort as scanner.py.

    Historical signatures are built once. No vectorized distance/sort substitution.
    Library order is significant for ties and is retained in the input manifest.
    """
    def __init__(self, data):
        if (legacy.WINDOW, legacy.STEP, legacy.TOP_N, legacy.MIN_GAP_DAYS, legacy.CLEAN_TOP_N) != (100, 5, 200, 90, 40):
            raise ValueError('LEGACY_CONFIG_CHANGED')
        self.data, self.episodes, self.signatures = data, [], []
        for ticker, frame in data.items():
            for start in range(0, len(frame) - legacy.WINDOW - max(legacy.FORWARD_DAYS), legacy.STEP):
                signature = legacy.make_signature_v2(frame, start_idx=start)
                if signature is not None:
                    self.episodes.append((ticker, start, start + legacy.WINDOW - 1))
                    self.signatures.append(signature)
        self.signature_bytes = sum(s.nbytes for s in self.signatures)

    def match(self, ticker, frame):
        signature = legacy.make_signature_v2(frame)
        if signature is None:
            return pd.DataFrame(), pd.DataFrame()
        rows = []
        for (asset, start, end), historical in zip(self.episodes, self.signatures):
            data = self.data[asset]
            if asset == ticker and end >= len(data) - max(legacy.FORWARD_DAYS) - 5:
                continue
            similarity = 1 - cosine(signature, historical)
            if np.isnan(similarity):
                continue
            rows.append(dict(target=ticker, similar_asset=asset,
                             start_date=data.index[start].date(), end_date=data.index[end].date(),
                             similarity=similarity * 100))
        if not rows:
            return pd.DataFrame(), pd.DataFrame()
        # Identical quicksort input order; statistics do not affect ranking.
        top = pd.DataFrame(rows).sort_values('similarity', ascending=False).head(legacy.TOP_N)
        for pos, row in top.iterrows():
            data = self.data[row.similar_asset]
            end = data.index.get_loc(pd.Timestamp(row.end_date))
            for key, value in legacy.future_stats(data, end).items():
                top.loc[pos, key] = value
        return top, legacy.deoverlap_matches(top)


def paths_from_cohort(cohort, data):
    """Do not silently drop episodes: return valid rows and their true N."""
    valid, paths = [], []
    for row in cohort:
        frame = data.get(row['similar_asset'])
        if frame is None:
            continue
        end_date = pd.Timestamp(row['end_date'])
        if end_date not in frame.index:
            continue
        end = frame.index.get_loc(end_date)
        future = frame.iloc[end:end + 61]
        if len(future) != 61 or not ((future.index[1:] - future.index[:-1]) == pd.Timedelta(days=1)).all():
            continue
        close = future.Close.to_numpy(float)
        if not np.isfinite(close).all() or (close <= 0).any():
            continue
        paths.append((close / close[0] - 1) * 100)
        valid.append(row)
    return valid, np.asarray(paths).reshape(-1, 61)


def percentiles(values):
    return {f'p{q}': float(np.percentile(values, q)) for q in QUANTILES} if len(values) else {f'p{q}': None for q in QUANTILES}


def quality_components(n, distinct, similarity, width, evaluations, config):
    rules = config['quality']
    mature = len(evaluations) >= rules['minimum_evaluations']
    metrics = dict(historical_controls=len(evaluations),
                   MAE_vs_P50=float(np.mean([e['p50_error_absolute'] for e in evaluations])) if mature else None,
                   P25_P75_coverage=float(np.mean([e['inside_p25_p75'] for e in evaluations])) if mature else None,
                   P10_P90_coverage=float(np.mean([e['inside_p10_p90'] for e in evaluations])) if mature else None)
    good = (distinct >= rules['minimum_distinct_assets'] and similarity is not None
            and similarity >= rules['minimum_similarity'] and width is not None
            and width <= rules['maximum_cone_width_pp'])
    if n < 40:
        label = 'INSUFFICIENT'
    elif mature:
        calibrated = (metrics['P25_P75_coverage'] >= rules['central_coverage_min']
                      and metrics['P10_P90_coverage'] >= rules['outer_coverage_min'])
        label = 'MATURE_GOOD' if good and calibrated else 'MATURE_MIXED'
    else:
        label = 'PROVISIONAL_GOOD' if good else 'PROVISIONAL_LIMITED'
    return dict(data_quality='GOOD', N=n, distinct_analogue_assets=distinct,
                similarity=similarity, cone_width=width, label=label, **metrics)


def build_forecast(cid, ticker, cohort, data, anchor, anchor_date, as_of, manifest_id,
                   config, evaluations=(), canonical=None, data_quality='GOOD'):
    valid, matrix = paths_from_cohort(cohort, data)
    n = len(matrix)
    similarity = [float(r['similarity']) for r in valid]
    distinct = len({r['similar_asset'] for r in valid})
    path = []
    for day in range(61):
        values = percentiles(matrix[:, day])
        path.append(dict(day=day, N=n, **values,
                         **{f'{key}_price': anchor * (1 + val / 100) if val is not None else None
                            for key, val in values.items()}))
    headlines = []
    for horizon in HORIZONS:
        p = path[horizon]
        controls = [e for e in evaluations if e['coingecko_id'] == cid and e['horizon'] == horizon]
        width = p['p75'] - p['p25'] if n else None
        headlines.append(dict(horizon=horizon, N=n, percentile_return={f'p{q}': p[f'p{q}'] for q in QUANTILES},
                              implicit_price={f'p{q}': p[f'p{q}_price'] for q in QUANTILES},
                              positive_close_pct=float((matrix[:, horizon] > 0).mean() * 100) if n else None,
                              negative_close_pct=float((matrix[:, horizon] < 0).mean() * 100) if n else None,
                              drawdown=percentiles(matrix[:, :horizon + 1].min(axis=1)),
                              max_gain=percentiles(matrix[:, :horizon + 1].max(axis=1)),
                              distinct_analogue_assets=distinct,
                              similarity_mean=float(np.mean(similarity)) if n else None,
                              similarity_median=float(np.median(similarity)) if n else None,
                              cone_width=width,
                              quality=quality_components(n, distinct, float(np.mean(similarity)) if n else None,
                                                         width, controls, config)))
    for headline in headlines:
        headline['quality']['data_quality'] = data_quality
        if data_quality != 'GOOD' and n == 40:
            headline['quality']['label'] = ('MATURE_MIXED' if headline['quality']['MAE_vs_P50'] is not None
                                            else 'PROVISIONAL_LIMITED')
    body = dict(schema_version=1, coingecko_id=cid, ohlc_ticker=ticker, forecast_date=as_of,
                anchor_price=anchor, anchor_date=anchor_date, anchor_semantics='SHARED_SNAPSHOT' if canonical else 'LATEST_OHLC_CLOSE',
                input_manifest_id=manifest_id, method=SEMANTICS, N=n,
                status='VALID' if n == 40 else 'INSUFFICIENT_ANALOGUES',
                rotation_ready=n == 40, cohort=valid, requested_cohort_count=len(cohort),
                paths=path, headlines=headlines,
                canonical_forecast_id=canonical.get('forecast_id') if canonical else None,
                canonical_cohort_id=canonical.get('cohort_id') if canonical else None,
                canonical_anchor_snapshot_id=canonical.get('price_market_snapshot_id') if canonical else None)
    body['forecast_id'] = 'lab:' + cid + ':' + as_of + ':' + digest(body)
    return body


def verify_canonical(forecast, record, reports):
    """Parity against frozen matches, scanner percentiles and tracker 7/14/30."""
    if forecast['cohort'] != record['cohort'] or forecast['N'] != len(record['cohort']):
        raise ValueError('CANONICAL_COHORT_OR_N_CHANGED')
    if forecast['anchor_price'] != record['current_price']:
        raise ValueError('CANONICAL_ANCHOR_CHANGED')
    ticker = forecast['ohlc_ticker']
    symbol = ticker.removesuffix('-USD')
    reference = pd.read_csv(reports / (symbol + '_percentiles.csv'))
    for headline in forecast['headlines']:
        horizon = headline['horizon']
        for metric, values in [('return', headline['percentile_return']), ('drawdown', headline['drawdown']), ('max_gain', headline['max_gain'])]:
            for q in QUANTILES:
                cohort_value = float(np.percentile([r[f'{metric}_{horizon}d'] for r in record['cohort']], q))
                np.testing.assert_allclose(values[f'p{q}'], cohort_value, rtol=0, atol=1e-10)
                # Legacy scanner exports 30d percentile table; all horizons use frozen cohort stats.
                ref = reference[(reference.metric == f'{metric}_{horizon}d') & (reference.percentile == q)]
                if not ref.empty:
                    np.testing.assert_allclose(values[f'p{q}'], ref.percent_value.iloc[0], rtol=0, atol=1e-10)
    tracker = pd.read_csv(reports / 'forecast_provenance/scanner_forecast_versions.csv')
    tracker = tracker[(tracker.target_ticker == ticker) & (tracker.snapshot_date == forecast['forecast_date'])]
    for horizon in (7, 14, 30):
        rows = tracker[tracker.horizon_day == horizon]
        if rows.empty:
            raise ValueError('MISSING_CANONICAL_TRACKER_HORIZON')
        row = rows.sort_values('generated_at_utc').iloc[-1]
        np.testing.assert_allclose(row.current_price, forecast['anchor_price'], rtol=0, atol=1e-10)
        if row.cases_used != forecast['N']:
            raise ValueError('CANONICAL_TRACKER_N_MISMATCH')
        for q in QUANTILES:
            for suffix, key in [('pct', f'p{q}'), ('price', f'p{q}_price')]:
                np.testing.assert_allclose(row[f'p{q}_{suffix}'], forecast['paths'][horizon][key], rtol=0, atol=1e-8)
    return 'PASS'


def evaluate(vintages, raw, snapshot_ids, as_of):
    """Calendar-date close only, independent of current target membership."""
    evaluations = []
    for vintage in vintages:
        if vintage['status'] != 'VALID':
            continue
        ticker = vintage['ohlc_ticker']
        frame = raw.get(ticker)
        if frame is None:
            continue
        start = pd.Timestamp(vintage['anchor_date'])
        anchor = vintage['anchor_price']
        for horizon in EVALUATION_DAYS:
            due = start + pd.Timedelta(days=horizon)
            if (due.date() < pd.Timestamp(vintage['forecast_date']).date()
                    or due.date() >= pd.Timestamp(as_of).date() or due not in frame.index):
                continue  # today's daily candle is not a completed actual
            segment = frame.loc[start:due, 'Close']
            if len(segment) != horizon + 1 or not ((segment.index[1:] - segment.index[:-1]) == pd.Timedelta(days=1)).all():
                continue
            actual = float(segment.iloc[-1])
            result = (actual / anchor - 1) * 100
            p = vintage['paths'][horizon]
            signed = result - p['p50']
            evaluations.append(dict(forecast_id=vintage['forecast_id'], coingecko_id=vintage['coingecko_id'],
                                    horizon=horizon, target_date=due.date().isoformat(), actual_close=actual,
                                    actual_return=result, p50_error_signed=signed, p50_error_absolute=abs(signed),
                                    direction_forecast='UP' if p['p50'] >= 0 else 'DOWN',
                                    direction_actual='UP' if result >= 0 else 'DOWN',
                                    direction_correct=(result >= 0) == (p['p50'] >= 0),
                                    inside_p25_p75=p['p25'] <= result <= p['p75'],
                                    inside_p10_p90=p['p10'] <= result <= p['p90'],
                                    actual_drawdown=(min(anchor, float(segment.min())) / anchor - 1) * 100,
                                    actual_max_gain=(max(anchor, float(segment.max())) / anchor - 1) * 100,
                                    actual_snapshot_id=snapshot_ids[ticker], method=SEMANTICS))
    return evaluations


def paired_probability(*_args, **_kwargs):
    # V1 analogue selections do not define a genuinely paired sampling design.
    return {'probability': None, 'N_PAIR': 0, 'reason': 'NO_COMPARABLE_PAIRED_OBSERVATIONS'}


def edge_state(edges, config):
    rules = config['rotation']
    if not edges or edges[-1] is None:
        return 'INSUFFICIENT_DATA'
    current = edges[-1]
    recent = edges[-rules['snapshot_window']:]
    positive = sum(e is not None and e >= rules['ordinary_edge_pp'] for e in recent)
    negative = sum(e is not None and e <= -rules['ordinary_edge_pp'] for e in recent)
    if current >= rules['ordinary_edge_pp'] and positive >= rules['persistence_count']:
        return 'PERSISTENT_EDGE'
    if current <= -rules['ordinary_edge_pp'] and negative >= rules['persistence_count']:
        return 'PERSISTENT_RELATIVE_WEAKNESS'
    if current >= rules['strong_edge_pp']:
        return 'STRONG_CURRENT_EDGE'
    if current >= rules['ordinary_edge_pp']:
        return 'ONE_DAY_EDGE'
    if len(recent) < rules['snapshot_window']:
        return 'WARMUP'
    return 'NO_CLEAR_EDGE'


def rotation(forecasts, history, config):
    """Benchmarks share one forecast date. Persistence cannot cross missing days."""
    by_date = {}
    for f in history + forecasts:
        by_date.setdefault(f['forecast_date'], {})[f['coingecko_id']] = f
    results = []
    for forecast in forecasts:
        date = pd.Timestamp(forecast['forecast_date'])
        days = [(date - pd.Timedelta(days=d)).date().isoformat() for d in (2, 1, 0)]
        for horizon in HORIZONS:
            snapshots = []
            for day in days:
                group = by_date.get(day, {})
                target = group.get(forecast['coingecko_id'])
                good = {cid: f for cid, f in group.items() if f['rotation_ready']}
                medians = [f['paths'][horizon]['p50'] for f in good.values()]
                benchmarks = {'SOL': good.get('solana'), 'BTC': good.get('bitcoin')}
                edges = {}
                for name, bench in benchmarks.items():
                    edges['edge_vs_' + name] = (target['paths'][horizon]['p50'] - bench['paths'][horizon]['p50']
                                                if target and target['rotation_ready'] and bench else None)
                edges['edge_vs_top50_median'] = (target['paths'][horizon]['p50'] - float(np.median(medians))
                                                if target and target['rotation_ready'] and medians else None)
                snapshots.append(dict(forecast_date=day, forecast_id=target['forecast_id'] if target else None,
                                      benchmark_count=len(medians), **edges))
            current = snapshots[-1]
            headline = next(h for h in forecast['headlines'] if h['horizon'] == horizon)
            p = forecast['paths'][horizon]
            states, persistence = {}, {}
            for benchmark in ('SOL', 'BTC', 'top50_median'):
                key = 'edge_vs_' + benchmark
                edges = [s[key] for s in snapshots]
                # Leading gaps represent a warmup; internal gaps remain missing observations.
                while edges and edges[0] is None:
                    edges = edges[1:]
                states[benchmark] = edge_state(edges, config)
                persistence[benchmark] = sum(e is not None and e >= config['rotation']['ordinary_edge_pp'] for e in edges)
            results.append(dict(coingecko_id=forecast['coingecko_id'], forecast_id=forecast['forecast_id'],
                                horizon=horizon, **{k: v for k, v in current.items() if k.startswith('edge_')},
                                P10=p['p10'], P25=p['p25'], P75=p['p75'],
                                P75_P25_width=headline['cone_width'], quality=headline['quality'],
                                states=states, persistence=persistence, last_3_snapshots=snapshots,
                                paired_probability=paired_probability(),
                                benchmark_count=current['benchmark_count']))
    return results
