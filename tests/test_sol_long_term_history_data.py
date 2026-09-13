"""Data-contract regression tests; fixtures never write authoritative reports."""
from __future__ import annotations

import copy
import json
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import sol_long_term_history as history


REAL_REPORTS = Path('/opt/crypto-fractal-scanner-publisher/reports')
FIXTURE_NOW = datetime(2026, 10, 1, tzinfo=timezone.utc)


def record(at='2026-09-03T06:00:00Z', *, median=150.0):
    return {
        'generated_at': at,
        'cohort_sha256': 'a' * 64,
        'current_sol_price': 100.0,
        'canonical_cohort_count': 40,
        'raw_episode_count': {'90': 40, '180': 39, '365': 35, '730': 30},
        'horizons': {
            str(days): {
                'log_robust_p50_price': median,
                'log_robust_p75_price': median + 100,
                'log_robust_p90_price': median + 300,
                'p_ge_200': 35.0,
                'p_ge_300': 25.0,
                'p_ge_500': 10.0,
                'p_ge_800': 0.0,
            }
            for days in (180, 365, 730)
        },
    }


def full_snapshot(short):
    result = {
        'role': 'DIAGNOSTIC_ONLY',
        'target': 'SOL-USD',
        'generated_at_utc': short['generated_at'],
        'current_price': short['current_sol_price'],
        'horizons': {},
    }
    for days in history.HORIZONS:
        saved = short['horizons'].get(str(days), short['horizons']['180'])
        result['horizons'][str(days)] = {
            'distinct_assets': 27,
            'raw_episodes': short['raw_episode_count'][str(days)],
            'distributions': {
                'LOG_ROBUST_TAIL': {
                    'final_return': {
                        'implicit_sol_prices': {
                            'p10': 40.0,
                            'p25': 80.0,
                            **{f'p{q}': saved[f'log_robust_p{q}_price'] for q in (50, 75, 90)},
                        }
                    }
                }
            },
            'empirical_price_threshold_probabilities': {
                'LOG_ROBUST_TAIL': {
                    f'p_sol_ge_{v}': saved[f'p_ge_{v}'] for v in (200, 300, 500, 800)
                }
            },
        }
    return result


class TemporarySources(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='cone-data-test-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def sources(self, records, *, current=None, archives=()):
        (self.root / 'sol_long_term_probability_cone_history.jsonl').write_text(
            ''.join(json.dumps(item) + '\n' for item in records), encoding='utf-8')
        current = current if current is not None else full_snapshot(records[-1])
        (self.root / 'sol_long_term_probability_cone.json').write_text(json.dumps(current), encoding='utf-8')
        for index, payload in enumerate(archives):
            archive = self.root / 'sol_long_term_probability_cone_history' / str(index)
            archive.mkdir(parents=True)
            (archive / 'sol_long_term_probability_cone.json').write_text(json.dumps(payload), encoding='utf-8')
        return self.root

    def discover(self):
        return history.discover_snapshots(self.root, now=FIXTURE_NOW)

    def test_no_invented_backfill_or_gap_rows(self):
        first = record('2026-09-03T06:00:00Z')
        last = record('2026-09-13T06:00:00Z')
        self.sources([first, last])
        rows, current, _ = self.discover()
        daily = history.merge_daily([], rows)
        self.assertEqual([row['date_local'] for row in daily], ['2026-09-03', '2026-09-13'])
        self.assertEqual(daily[-1], current)
        self.assertEqual(len(history.vintages(daily)), 8)

    def test_madrid_date_and_latest_snapshot_despite_input_order(self):
        early = record('2026-09-03T21:30:00Z', median=140)
        same_local_day = record('2026-09-03T22:30:00Z', median=145)
        later = record('2026-09-04T20:00:00Z', median=150)
        self.sources([later, same_local_day, early], current=full_snapshot(later))
        rows, _, _ = self.discover()
        daily = history.select_daily(rows)
        self.assertEqual([row['date_local'] for row in daily], ['2026-09-03', '2026-09-04'])
        self.assertEqual(daily[-1]['generated_at'], later['generated_at'])
        self.assertEqual(daily[-1]['h730_p50'], 150)

    def test_madrid_dst_repeated_hour_still_one_daily_observation(self):
        # At the autumn transition both UTC instants belong to the same Madrid day.
        first = history.normalize_snapshot(record('2026-10-25T00:30:00Z', median=140))
        second = history.normalize_snapshot(record('2026-10-25T01:30:00Z', median=150))
        self.assertEqual(history.select_daily([second, first]), [second])

    def test_last_qualifying_snapshot_excludes_later_invalid_archive(self):
        first = record('2026-09-03T06:00:00Z', median=140)
        qualifying = record('2026-09-03T09:00:00Z', median=150)
        invalid = record('2026-09-03T12:00:00Z', median=160)
        invalid_report = full_snapshot(invalid)
        invalid_report['role'] = 'INVALID'
        self.sources([first, invalid, qualifying], current=full_snapshot(qualifying), archives=[invalid_report])
        rows, _, warnings = self.discover()
        self.assertEqual(len(rows), 2)
        self.assertTrue(warnings)
        self.assertEqual(history.select_daily(rows)[0]['generated_at'], qualifying['generated_at'])

    def test_identical_duplicate_snapshot_is_idempotent(self):
        item = record()
        self.sources([item, copy.deepcopy(item)])
        rows, _, warnings = self.discover()
        self.assertEqual(len(rows), 1)
        self.assertEqual(warnings, [])

    def test_rerun_preserves_committed_same_day_then_appends_next_date(self):
        committed = history.normalize_snapshot(record('2026-09-03T06:00:00Z', median=140))
        later = history.normalize_snapshot(record('2026-09-03T16:00:00Z', median=160))
        tomorrow = history.normalize_snapshot(record('2026-09-04T06:00:00Z', median=170))
        baseline = copy.deepcopy(committed)
        self.assertEqual(history.merge_daily([committed], [later]), [baseline])
        merged = history.merge_daily([committed], [tomorrow, later])
        self.assertEqual(merged, [baseline, tomorrow])
        self.assertEqual(committed, baseline)
        self.assertEqual(history.merge_daily(merged, [tomorrow, later]), merged)

    def test_append_only_does_not_insert_late_discovered_dates_before_cutoff(self):
        committed = history.normalize_snapshot(record('2026-09-05T06:00:00Z'))
        late_archive = history.normalize_snapshot(record('2026-09-04T06:00:00Z'))
        self.assertEqual(history.merge_daily([committed], [late_archive, committed]), [committed])

    def test_csv_roundtrip_preserves_missing_and_zero_probabilities(self):
        row = history.normalize_snapshot(record())
        path = self.root / 'daily.csv'
        data = history.csv_bytes([row], history.FIELDS)
        path.write_bytes(data)
        recovered = history.read_daily_csv(path)
        self.assertEqual(recovered, [row])
        self.assertIsNone(recovered[0]['h180_p10'])
        self.assertIsNone(recovered[0]['h180_p_ge_150'])
        self.assertEqual(recovered[0]['h180_p_ge_800'], 0.0)
        self.assertEqual(path.read_bytes(), data)

    def test_csv_rejects_duplicate_dates(self):
        row = history.normalize_snapshot(record())
        path = self.root / 'daily.csv'
        path.write_bytes(history.csv_bytes([row, row], history.FIELDS))
        with self.assertRaises(history.HistoryError):
            history.read_daily_csv(path)

    def test_missing_archive_uses_only_values_actually_recorded_in_jsonl(self):
        past, current = record(), record('2026-09-04T06:00:00Z')
        self.sources([past, current])
        rows, _, _ = self.discover()
        first = rows[0]
        self.assertEqual(first['source_kind'], 'history_jsonl')
        self.assertEqual(first['h180_p50'], past['horizons']['180']['log_robust_p50_price'])
        for field in ('h90_p50', 'h180_p10', 'h180_p25', 'h180_p_ge_150', 'distinct_assets'):
            self.assertIsNone(first[field], field)
        self.assertEqual(first['h365_stability'], 'N/D')
        ninety_days = history.vintages([first])[0]
        self.assertIsNone(ninety_days['p50'])
        self.assertIsNone(ninety_days['p_ge_300'])

    def test_vintage_dates_use_exact_day_offsets_including_leap_year(self):
        row = history.normalize_snapshot(record('2024-02-28T06:00:00Z'))
        vintages = history.vintages([row])
        self.assertEqual([item['target_horizon_days'] for item in vintages], [90, 180, 365, 730])
        for item in vintages:
            self.assertEqual(date.fromisoformat(item['target_date']) - date(2024, 2, 28),
                             timedelta(days=item['target_horizon_days']))
            self.assertEqual(item['forecast_date'], '2024-02-28')
            self.assertEqual(item['spot_at_forecast'], row['spot_sol'])
            self.assertEqual(item['cohort_sha256'], row['cohort_sha256'])

    def test_no_outcomes_or_early_maturity_for_any_vintage(self):
        rows = [history.normalize_snapshot(record(day)) for day in ('2020-01-01T06:00:00Z', '2026-09-13T06:00:00Z')]
        for item in history.vintages(rows):
            self.assertEqual(set(item), set(history.VINTAGE_FIELDS))
            self.assertGreater(item['target_date'], item['forecast_date'])
            self.assertFalse(any(term in field for field in item for term in ('outcome', 'matured', 'realized')))

    def test_future_noncurrent_snapshot_is_excluded(self):
        good, future = record(), record('2099-01-01T06:00:00Z')
        self.sources([good, future], current=full_snapshot(good))
        rows, current, warnings = self.discover()
        self.assertEqual(rows, [current])
        self.assertTrue(any('future' in warning for warning in warnings))

    def test_future_current_snapshot_fails_closed(self):
        self.sources([record(), record('2099-01-01T06:00:00Z')])
        with self.assertRaises(history.HistoryError):
            self.discover()

    def test_current_without_matching_authoritative_provenance_fails_closed(self):
        self.sources([record()], current=full_snapshot(record('2026-09-04T06:00:00Z')))
        with self.assertRaises(history.HistoryError):
            self.discover()

    def test_invalid_current_does_not_silently_publish_other_snapshot(self):
        good, latest = record(), record('2026-09-04T06:00:00Z')
        invalid_report = full_snapshot(latest)
        invalid_report['target'] = 'BTC-USD'
        self.sources([good, latest], current=invalid_report)
        with self.assertRaises(history.HistoryError):
            self.discover()

    def test_conflicting_current_vs_archive_fails_closed(self):
        good = record()
        archive = full_snapshot(good)
        current = copy.deepcopy(archive)
        current['current_price'] += 1
        self.sources([good], current=current, archives=[archive])
        with self.assertRaises(history.HistoryError):
            self.discover()

    def test_conflicting_jsonl_provenance_for_current_fails_closed(self):
        good = record()
        conflicting = copy.deepcopy(good)
        conflicting['cohort_sha256'] = 'b' * 64
        self.sources([good, conflicting], current=full_snapshot(good))
        with self.assertRaises(history.HistoryError):
            self.discover()

    def test_missing_hash_invalid_quantiles_and_probabilities_are_rejected(self):
        changes = (
            lambda item: item.update(cohort_sha256=''),
            lambda item: item['horizons']['730'].update(log_robust_p75_price=10),
            lambda item: item['horizons']['730'].update(p_ge_300=100.01),
            lambda item: item['horizons']['730'].update(p_ge_500=-0.1),
            lambda item: item['horizons']['730'].update(log_robust_p50_price=None),
        )
        for change in changes:
            with self.subTest(change=change):
                item = record()
                change(item)
                with self.assertRaises(history.HistoryError):
                    history.normalize_snapshot(item)

    def test_nonfinite_values_remain_missing_in_optional_fields(self):
        item = record()
        item['horizons']['180'].update(log_robust_p10_price=float('nan'), p_ge_800=float('inf'))
        normalized = history.normalize_snapshot(item)
        self.assertIsNone(normalized['h180_p10'])
        self.assertIsNone(normalized['h180_p_ge_800'])


@unittest.skipUnless((REAL_REPORTS / 'sol_long_term_probability_cone_history.jsonl').is_file(),
                     'authoritative on-host reports unavailable')
class RealSourceReadOnlyTests(unittest.TestCase):
    def test_real_history_dates_and_values_are_actual_source_observations(self):
        raw = [json.loads(line) for line in (REAL_REPORTS / 'sol_long_term_probability_cone_history.jsonl')
               .read_text(encoding='utf-8').splitlines() if line.strip()]
        rows, current, warnings = history.discover_snapshots(REAL_REPORTS)
        self.assertEqual(warnings, [])
        source_by_time = {item['generated_at']: item for item in raw}
        self.assertEqual({row['generated_at'] for row in rows}, set(source_by_time))
        for row in rows:
            source = source_by_time[row['generated_at']]
            self.assertEqual(row['cohort_sha256'], source['cohort_sha256'])
            self.assertEqual(row['spot_sol'], source['current_sol_price'])
            for horizon in (180, 365, 730):
                self.assertEqual(row[f'h{horizon}_p50'], source['horizons'][str(horizon)]['log_robust_p50_price'])
        daily = history.select_daily(rows)
        real_days = {history.timestamp(item['generated_at']).astimezone(history.LOCAL_ZONE).date().isoformat()
                     for item in raw}
        self.assertEqual({row['date_local'] for row in daily}, real_days)
        self.assertEqual(len(daily), len(real_days))
        self.assertEqual(len(history.vintages(daily)), len(real_days) * 4)
        for row in daily:
            candidates = [item for item in rows if item['date_local'] == row['date_local']]
            self.assertEqual(row['generated_at'], max(candidates, key=lambda item: history.timestamp(item['generated_at']))['generated_at'])
        latest_report = json.loads((REAL_REPORTS / 'sol_long_term_probability_cone.json').read_text(encoding='utf-8'))
        self.assertEqual(current['generated_at'], latest_report['generated_at_utc'])
        self.assertEqual(current['source_kind'], 'full_snapshot')
        self.assertEqual(rows[0]['generated_at'], min(raw, key=lambda item: history.timestamp(item['generated_at']))['generated_at'])


if __name__ == '__main__':
    unittest.main()
