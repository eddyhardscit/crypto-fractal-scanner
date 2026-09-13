"""Optional artifact-only extension of the canonical daily GitHub publisher."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import tempfile

from sol_long_term_history import (FIELDS, VINTAGE_FIELDS, HistoryError, csv_bytes,
    discover_snapshots, merge_daily, metric, read_daily_csv, recent_statistics, vintages)

OUTPUT_DIR = 'sol_long_term_history'
DAILY_CSV = 'sol_long_term_daily_history.csv'
VINTAGES_CSV = 'forecast_vintages.csv'
INDEX_SECTION = ('\n\n<!-- SOL_LONG_TERM_CONE_HISTORY_START -->\n'
    '## SOL Long-Term Cone History\n\n'
    '[SOL Long-Term Cone History](sol_long_term_history/README.md)\n'
    '<!-- SOL_LONG_TERM_CONE_HISTORY_END -->\n')


def add_index_link(index_path, dashboard_dir):
    """Only append the dedicated link, preserving all existing bytes."""
    index_path, dashboard_dir = Path(index_path), Path(dashboard_dir)
    if not index_path.is_file() or not (dashboard_dir/'README.md').is_file():
        return False
    original = index_path.read_bytes()
    if b'<!-- SOL_LONG_TERM_CONE_HISTORY_START -->' in original:
        return False
    atomic_write(index_path, original + INDEX_SECTION.encode('utf-8'))
    return True


def atomic_write(path, content):
    path = Path(path)
    fd, name = tempfile.mkstemp(prefix='.'+path.name+'.', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(name, 0o644)
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def generate(reports_dir, output_dir=None, *, now=None):
    """Prepare the whole bundle before writing; roll back handled write failures."""
    root = Path(reports_dir)
    out = Path(output_dir) if output_dir else root/OUTPUT_DIR
    snapshots, current, warnings = discover_snapshots(root, now=now)
    existing = read_daily_csv(out/DAILY_CSV)
    rows = merge_daily(existing, snapshots)
    new_rows = rows[len(existing):]
    daily_prefix = (out/DAILY_CSV).read_bytes() if existing else b''
    if daily_prefix and not daily_prefix.endswith(b'\n'):
        raise HistoryError('daily ledger lacks final newline; refusing mutation')
    daily_bytes = daily_prefix + csv_bytes(new_rows, FIELDS, header=not bool(existing))
    all_vintages = vintages(rows)
    vintage_path = out/VINTAGES_CSV
    expected_prefix = csv_bytes(vintages(existing), VINTAGE_FIELDS)
    if vintage_path.exists():
        old_vintages = vintage_path.read_bytes()
        if not old_vintages.endswith(b'\n'):
            raise HistoryError('vintage ledger lacks final newline; refusing mutation')
        # Numeric CSV strings may retain integer formatting from their initial
        # write. Compare parsed values, while preserving the original bytes.
        import csv, io
        actual = list(csv.DictReader(io.StringIO(old_vintages.decode('utf-8'))))
        expected = list(csv.DictReader(io.StringIO(expected_prefix.decode('utf-8'))))
        if len(actual) != len(expected):
            raise HistoryError('vintage ledger and daily ledger disagree')
        for left, right in zip(actual, expected):
            for key in VINTAGE_FIELDS:
                if left.get(key) == right.get(key):
                    continue
                try:
                    if float(left[key]) == float(right[key]):
                        continue
                except (ValueError, KeyError, TypeError):
                    pass
                raise HistoryError('immutable vintage ledger mismatch')
        vintage_bytes = old_vintages + csv_bytes(vintages(new_rows), VINTAGE_FIELDS, header=False)
    else:
        vintage_bytes = csv_bytes(all_vintages, VINTAGE_FIELDS)
    stats = recent_statistics(rows)
    full_p50 = metric(r['h730_p50'] for r in rows)
    full_p300 = metric(r['h730_p_ge_300'] for r in rows)
    manifest = dict(FIRST_REAL_SNAPSHOT=snapshots[0]['generated_at'],
        FIRST_AVAILABLE_LONG_TERM_SNAPSHOT=snapshots[0]['generated_at'],
        LATEST_REAL_SNAPSHOT=snapshots[-1]['generated_at'],
        DAILY_HISTORY_ROWS=len(rows), FORECAST_VINTAGE_ROWS=len(all_vintages),
        CURRENT_6M_P50=current['h180_p50'], CURRENT_1Y_P50=current['h365_p50'], CURRENT_2Y_P50=current['h730_p50'],
        CURRENT_2Y_P_GE_300=current['h730_p_ge_300'], CURRENT_2Y_P_GE_500=current['h730_p_ge_500'],
        CURRENT_2Y_P_GE_800=current['h730_p_ge_800'], HISTORY_2Y_P50_MIN=full_p50['min'],
        HISTORY_2Y_P50_MAX=full_p50['max'], HISTORY_2Y_P50_MEDIAN=full_p50['median'],
        HISTORY_2Y_P_GE_300_MIN=full_p300['min'], HISTORY_2Y_P_GE_300_MAX=full_p300['max'],
        FORECAST_DRIFT_STATUS=stats['drift_status'], QUALIFYING_REAL_SNAPSHOTS=len(snapshots),
        EXCLUDED_SNAPSHOT_REASONS=warnings)
    with tempfile.TemporaryDirectory(prefix='sol-cone-history-render-') as temporary:
        stage = Path(temporary)
        from sol_long_term_history_dashboard import render_dashboard
        render_dashboard(rows, current, stage, snapshots[0]['generated_at'], snapshots[-1]['generated_at'])
        (stage/DAILY_CSV).write_bytes(daily_bytes)
        (stage/VINTAGES_CSV).write_bytes(vintage_bytes)
        (stage/'availability.json').write_text(json.dumps(manifest, indent=2, allow_nan=False)+'\n', encoding='utf-8')
        candidates = {p.name: p.read_bytes() for p in stage.iterdir() if p.is_file()}
        required = {DAILY_CSV, VINTAGES_CSV, 'README.md', 'sol_long_term_cone_current.png',
            'sol_long_term_cone_history.png', 'sol_long_term_probability_history.png', 'availability.json'}
        if set(candidates) != required or not all(candidates.values()):
            raise HistoryError('incomplete dashboard bundle')
        out.mkdir(parents=True, exist_ok=True)
        before = {name: (out/name).read_bytes() if (out/name).exists() else None for name in candidates}
        changed = []
        try:
            for name, content in candidates.items():
                if before[name] != content:
                    atomic_write(out/name, content)
                    changed.append(name)
        except Exception:
            for name in reversed(changed):
                if before[name] is None:
                    (out/name).unlink()
                else:
                    atomic_write(out/name, before[name])
            raise
    manifest['OUTPUT_FILES'] = [str(out/name) for name in sorted(required)]
    return manifest


def publish(reports_dir, *, output_dir=None, index_path=None):
    """Never propagate a Long-Term failure to the existing forecast publisher."""
    root = Path(reports_dir)
    out = Path(output_dir) if output_dir else root/OUTPUT_DIR
    try:
        result = generate(root, out)
        print(json.dumps(result, indent=2))
        status = True
    except Exception as exc:
        print(f'LONG_TERM_HISTORY_RETAINED_LAST_VALID: {type(exc).__name__}')
        status = False
    try:
        add_index_link(index_path or root/'latest_report.md', out)
    except Exception as exc:
        print(f'LONG_TERM_HISTORY_INDEX_SKIPPED: {type(exc).__name__}')
    return status


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reports-dir', type=Path, default=Path(__file__).resolve().parent/'reports')
    parser.add_argument('--output-dir', type=Path)
    parser.add_argument('--index-path', type=Path)
    parser.add_argument('--best-effort', action='store_true')
    args = parser.parse_args()
    ok = publish(args.reports_dir, output_dir=args.output_dir, index_path=args.index_path)
    return 0 if ok or args.best_effort else 1


if __name__ == '__main__':
    raise SystemExit(main())
