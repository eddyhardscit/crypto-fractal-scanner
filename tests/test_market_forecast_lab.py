"""Unit, state-transition and optional frozen-production parity checks (no network)."""
import copy
import hashlib
import json
import os
from pathlib import Path
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch

import numpy as np
import pandas as pd

import forecast_provenance as fp
import scanner as legacy
import market_forecast_lab as lab
from market_forecast_lab_engine import (
    LEGACY_IDS, SharedSignatureIndex, build_forecast, digest, edge_state, evaluate,
    load_legacy_inputs, paired_probability, paths_from_cohort, quality_components,
    rotation, verify_canonical,
)
from market_forecast_lab_universe import data_quality, load_config, load_registry, select_universe


def frame(seed=1, periods=1050, end='2026-09-22'):
    rng = np.random.default_rng(seed)
    close = 100 * np.exp(np.cumsum(rng.normal(0.0005, .025, periods)))
    return pd.DataFrame(dict(Open=close, High=close * 1.01, Low=close * .99,
                             Close=close, Volume=rng.integers(10000, 100000, periods)),
                        index=pd.date_range(end=end, periods=periods, freq='D'))


def mini_forecast(cid='test', date='2026-09-22', p50=10, valid=True):
    path = [dict(day=d, p10=-10, p25=0, p50=p50, p75=20, p90=30, N=40) for d in range(61)]
    return dict(forecast_id=cid + ':' + date, coingecko_id=cid, forecast_date=date,
                ohlc_ticker=cid.upper() + '-USD', anchor_date=date, anchor_price=100,
                paths=path, status='VALID' if valid else 'INSUFFICIENT_ANALOGUES', rotation_ready=valid,
                headlines=[dict(horizon=h, cone_width=20, quality={}) for h in (7, 14, 30, 60)])


class IndexTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = {f'T{i}-USD': legacy.add_indicators(frame(i)) for i in range(24)}
        cls.index = SharedSignatureIndex(cls.data)

    def test_shared_index_exact_legacy_order_and_values(self):
        for target in ('T0-USD', 'T1-USD', 'T2-USD'):
            with self.subTest(target=target):
                expected = legacy.find_similar_patterns(target, self.data)
                actual, clean = self.index.match(target, self.data[target])
                pd.testing.assert_frame_equal(actual, expected, check_dtype=False)
                pd.testing.assert_frame_equal(clean, legacy.deoverlap_matches(expected), check_dtype=False)

    def test_signatures_built_once_for_multiple_targets(self):
        with patch.object(legacy, 'make_signature_v2', wraps=legacy.make_signature_v2) as signature:
            self.index.match('T0-USD', self.data['T0-USD'])
            self.index.match('T1-USD', self.data['T1-USD'])
            self.assertEqual(signature.call_count, 2)  # current signatures only

    def test_top_200_and_40_clean(self):
        raw, clean = self.index.match('T0-USD', self.data['T0-USD'])
        self.assertEqual(len(raw), 200)
        self.assertEqual(len(clean), 40)

    def test_deoverlap(self):
        _, clean = self.index.match('T0-USD', self.data['T0-USD'])
        for _, group in clean.groupby('similar_asset'):
            dates = sorted(pd.to_datetime(group.end_date))
            self.assertTrue(all((b - a).days >= 90 for a, b in zip(dates, dates[1:])))

    def test_ties_preserve_legacy_sort_semantics(self):
        data = {'A': self.data['T0-USD'], 'B': self.data['T0-USD']}
        index = SharedSignatureIndex(data)
        actual, _ = index.match('A', data['A'])
        expected = legacy.find_similar_patterns('A', data)
        pd.testing.assert_frame_equal(actual, expected, check_dtype=False)

    def test_path_60_percentiles_headlines_and_anchor(self):
        _, clean = self.index.match('T0-USD', self.data['T0-USD'])
        cohort = clean.to_dict('records')
        valid, matrix = paths_from_cohort(cohort, self.data)
        f = build_forecast('test', 'T0-USD', cohort, self.data, 123, '2026-09-22',
                           '2026-09-22', 'input', load_config())
        self.assertEqual(len(f['paths']), 61)
        self.assertEqual(f['N'], 40)
        for day in range(61):
            for q in (10, 25, 50, 75, 90):
                self.assertEqual(f['paths'][day][f'p{q}'], np.percentile(matrix[:, day], q))
                self.assertEqual(f['paths'][0][f'p{q}_price'], 123)
        for h in f['headlines']:
            d = h['horizon']
            self.assertEqual(h['positive_close_pct'], (matrix[:, d] > 0).mean() * 100)
            self.assertEqual(h['drawdown']['p50'], np.percentile(matrix[:, :d+1].min(axis=1), 50))
            self.assertEqual(h['max_gain']['p90'], np.percentile(matrix[:, :d+1].max(axis=1), 90))

    def test_insufficient_sample_not_rotation_ready(self):
        _, clean = self.index.match('T0-USD', self.data['T0-USD'])
        f = build_forecast('test', 'T0-USD', clean.head(7).to_dict('records'), self.data,
                           100, '2026-09-22', '2026-09-22', 'input', load_config())
        self.assertEqual(f['N'], 7)
        self.assertFalse(f['rotation_ready'])
        self.assertEqual(f['status'], 'INSUFFICIENT_ANALOGUES')
        self.assertEqual(f['headlines'][0]['quality']['label'], 'INSUFFICIENT')

    def test_missing_path_cannot_fake_n(self):
        cohort = [{'similar_asset': 'missing', 'end_date': '2020-01-01'}]
        f = build_forecast('test', 'T0-USD', cohort, self.data, 100, '2026-09-22',
                           '2026-09-22', 'input', load_config())
        self.assertEqual(f['N'], 0)
        self.assertIsNone(f['paths'][60]['p50'])


class UniverseTests(unittest.TestCase):
    def setUp(self):
        self.config = load_config()
        self.data = {'T': legacy.add_indicators(frame())}
        self.registry = {'test': dict(classification='NATIVE', target_enabled=True, analogue_enabled=False, ohlc_ticker='T')}
        self.snapshot = dict(generated_at='2026-09-22T00:00:00Z', rows=[self.coin('test', 1)])

    def coin(self, cid, rank):
        return dict(id=cid, symbol=cid, name=cid, market_cap_rank=rank, market_cap=100, total_volume=10)

    def select(self):
        return select_universe(self.snapshot, self.registry, self.data, '2026-09-22', self.config)

    def test_top50_eligible_not_provider_rank50(self):
        self.snapshot['rows'] = [self.coin('unknown', 1)] + [self.coin('id' + str(i), i + 2) for i in range(60)]
        for i in range(60):
            self.registry['id' + str(i)] = self.registry['test']
        result = self.select()
        included = [r for r in result if r['inclusion_status'] == 'INCLUDED']
        self.assertEqual(len(included), 50)
        self.assertEqual(included[-1]['provider_rank'], 51)
        self.assertEqual(included[-1]['eligible_rank'], 50)

    def test_all_duplicate_and_stablecoin_exclusions(self):
        for reason in ('STABLECOIN', 'WRAPPED_DUPLICATE', 'BRIDGED_DUPLICATE', 'LIQUID_STAKING_DUPLICATE', 'SYNTHETIC_DUPLICATE'):
            with self.subTest(reason=reason):
                self.registry['test']['classification'] = reason
                self.assertEqual(self.select()[0]['exclusion_reason'], reason)

    def test_unknown_pending(self):
        self.registry.clear()
        self.assertEqual(self.select()[0]['inclusion_status'], 'PENDING_CLASSIFICATION')

    def test_target_disabled_library_enabled(self):
        self.registry['test'].update(target_enabled=False, analogue_enabled=True)
        self.assertEqual(self.select()[0]['exclusion_reason'], 'TARGET_DISABLED')

    def test_no_mapping(self):
        self.registry['test']['ohlc_ticker'] = None
        self.assertEqual(self.select()[0]['exclusion_reason'], 'NO_RELIABLE_OHLC_MAPPING')

    def test_unverified_mapping_has_explicit_exclusion_reason(self):
        rows = select_universe(self.snapshot, self.registry, self.data, '2026-09-22', self.config,
                               {'T': 'ValueError:OHLC_IDENTITY_NOT_VERIFIED'})
        self.assertEqual(rows[0]['exclusion_reason'], 'NO_RELIABLE_OHLC_MAPPING')

    def test_insufficient_data_excluded(self):
        self.data['T'] = self.data['T'].tail(50)
        self.assertEqual(self.select()[0]['exclusion_reason'], 'INSUFFICIENT_HISTORY')

    def test_gapped_history_excluded(self):
        self.data['T'] = self.data['T'].drop(self.data['T'].index[-5:-3])
        self.assertEqual(self.select()[0]['exclusion_reason'], 'GAPPED_DAILY_HISTORY')

    def test_one_missing_current_day_is_disclosed_limited(self):
        self.data['T'] = self.data['T'].drop(self.data['T'].index[-2])
        row = self.select()[0]
        self.assertEqual(row['inclusion_status'], 'INCLUDED')
        self.assertEqual(row['data_quality'], 'LIMITED_CLOSE_ONLY_INPUT')

    def test_high_low_inconsistency_disclosed_close_only(self):
        self.data['T'].loc[self.data['T'].index[-1], 'High'] = 1
        row = self.select()[0]
        self.assertEqual(row['inclusion_status'], 'INCLUDED')
        self.assertEqual(row['data_quality'], 'LIMITED_CLOSE_ONLY_INPUT')

    def test_wrong_yahoo_identity_cannot_acquire_ohlc(self):
        registry = {'test': dict(target_enabled=True, ohlc_ticker='TEST-USD')}
        metadata = dict(symbol='TEST-USD', currency='USD', instrumentType='CRYPTOCURRENCY',
                        shortName='Unrelated Token USD', longName='Unrelated Token USD')
        with patch.object(lab.yf, 'Ticker') as ticker, patch.object(lab.yf, 'download') as download:
            ticker.return_value.get_history_metadata.return_value = metadata
            errors, _ = lab.acquire_extra(registry, self.snapshot, {}, {}, {}, [], '2026-09-22', lab.new_context('TRIAL'))
        self.assertIn('OHLC_IDENTITY_NOT_VERIFIED', errors['TEST-USD'])
        download.assert_not_called()

    def test_stale_data_excluded(self):
        self.data['T'] = self.data['T'].iloc[:-4]
        self.assertEqual(self.select()[0]['exclusion_reason'], 'STALE_OR_FUTURE_CLOSE')

    def test_stale_membership_fails_closed(self):
        self.snapshot['generated_at'] = '2026-09-01T00:00:00Z'
        with self.assertRaisesRegex(ValueError, 'STALE_OR_FUTURE_UNIVERSE'):
            self.select()

    def test_duplicate_identity_rejected(self):
        self.snapshot['rows'] *= 2
        with self.assertRaisesRegex(ValueError, 'DUPLICATE_MARKET_ID'):
            self.select()

    def test_registry_unique_targets_and_legacy_library(self):
        registry = load_registry()
        library = [r['ohlc_ticker'] for r in registry.values() if r['analogue_enabled']]
        self.assertEqual(library, legacy.CRYPTO_TICKERS)
        self.assertTrue(any(not r['target_enabled'] and r['analogue_enabled'] for r in registry.values()))


class VintageEvaluationTests(unittest.TestCase):
    def setUp(self):
        # Keep all test bytes on the publisher volume.
        self.temp = tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1] / 'reports')
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def test_immutable_vintage_idempotent_and_conflict(self):
        path = self.root / 'vintages.jsonl'
        f = mini_forecast()
        lab.immutable_append(path, [f], ('coingecko_id', 'forecast_date'))
        before = path.read_bytes()
        lab.immutable_append(path, [f], ('coingecko_id', 'forecast_date'))
        self.assertEqual(path.read_bytes(), before)
        f['anchor_price'] = 999
        with self.assertRaisesRegex(ValueError, 'IMMUTABLE_VINTAGE_CONFLICT'):
            lab.immutable_append(path, [f], ('coingecko_id', 'forecast_date'))
        self.assertEqual(path.read_bytes(), before)

    def test_exit_stops_and_reentry_resumes_forecasts(self):
        manifest = dict(**lab.new_context('OFFICIAL_DAILY'), raw_snapshot_ids={}, library_order=[], as_of='2026-09-22', config=load_config(),
                        quality_evaluations=[], canonical={}, universe=[])
        index = SharedSignatureIndex({})
        original = {**mini_forecast(), **lab.context(manifest)}
        output, _ = lab.forecasts_from_manifest(manifest, 'hash', index, [original])
        self.assertEqual(output, [])
        manifest['universe'] = [dict(coingecko_id='test', ohlc_ticker='TEST-USD', inclusion_status='INCLUDED')]
        # Same-day retry imports the immutable vintage; next-day reentry creates a new one.
        output, _ = lab.forecasts_from_manifest(manifest, 'hash', index, [original])
        self.assertEqual(output, [original])
        manifest.update(as_of='2026-09-24', raw_snapshot_ids={'TEST-USD': 'fake'})
        manifest['canonical'] = {'TEST-USD': dict(cohort=[], current_price=100, anchor_date='2026-09-24')}
        with patch.object(fp, 'load_frozen_ohlc', return_value=frame(end='2026-09-24')):
            output, _ = lab.forecasts_from_manifest(manifest, 'hash', index, [original])
        self.assertEqual(output[0]['forecast_date'], '2026-09-24')
        self.assertNotEqual(output[0]['forecast_id'], original['forecast_id'])

    def test_exited_vintage_evaluates_all_six_horizons(self):
        f = mini_forecast(date='2026-07-01')
        dates = pd.date_range('2026-07-01', periods=62)
        raw = {'TEST-USD': pd.DataFrame({'Close': np.arange(100, 162)}, index=dates)}
        result = evaluate([f], raw, {'TEST-USD': 'sha256:actual'}, '2026-09-22')
        self.assertEqual([e['horizon'] for e in result], [1, 3, 7, 14, 30, 60])
        row = result[2]
        self.assertAlmostEqual(row['actual_return'], 7)
        self.assertAlmostEqual(row['p50_error_signed'], -3)
        self.assertAlmostEqual(row['p50_error_absolute'], 3)
        self.assertEqual(row['actual_drawdown'], 0)
        self.assertAlmostEqual(row['actual_max_gain'], 7)
        self.assertTrue(row['direction_correct'])
        self.assertTrue(row['inside_p25_p75'])
        self.assertTrue(row['inside_p10_p90'])

    def test_stale_anchor_cannot_evaluate_preissuance_actuals(self):
        f = mini_forecast(date='2026-09-22')
        f['anchor_date'] = '2026-09-20'
        raw = {'TEST-USD': frame(end='2026-09-26')}
        results = evaluate([f], raw, {'TEST-USD': 'actual'}, '2026-09-26')
        self.assertNotIn(1, [r['horizon'] for r in results])
        self.assertIn(3, [r['horizon'] for r in results])
        self.assertTrue(all(r['target_date'] >= f['forecast_date'] for r in results))

    def test_incomplete_today_candle_not_evaluated(self):
        f = mini_forecast(date='2026-09-21')
        data = {'TEST-USD': frame()}
        self.assertEqual(evaluate([f], data, {'TEST-USD': 'x'}, '2026-09-22'), [])

    def test_provenance_dedup_hash_and_restore(self):
        raw_dir = self.root / 'raw_ohlc'
        with patch.object(fp, 'RAW_DIR', raw_dir), patch.object(fp, 'RAW_INDEX', self.root / 'raw.jsonl'):
            args = dict(ticker='TEST-USD', source='test', downloaded_at_utc='2026-09-22T00:00:00Z',
                        requested_interval='1d', requested_range='test', run_id='test', purpose='test')
            sid = fp.freeze_ohlc(frame(), **args)
            sid2 = fp.freeze_ohlc(frame(), **args)
            self.assertEqual(sid, sid2)
            self.assertEqual(len(list(raw_dir.glob('*.csv'))), 1)
            restored = fp.load_frozen_ohlc(sid)
            np.testing.assert_allclose(restored.Close, frame().Close, rtol=1e-14)
            path = next(raw_dir.glob('*.csv'))
            path.chmod(0o644)
            path.write_bytes(b'tampered')
            with self.assertRaisesRegex(RuntimeError, 'HISTORICAL_RAW_DATA_NOT_FROZEN'):
                fp.load_frozen_ohlc(sid)

    def test_replay_full_forecast_is_read_only_and_deterministic(self):
        raw_dir = self.root / 'raw_ohlc'
        attrs = dict(ROOT=self.root, RAW_DIR=raw_dir, RAW_INDEX=self.root / 'raw_market_snapshots.jsonl',
                     COHORT_DIR=self.root / 'cohorts')
        with patch.multiple(fp, **attrs):
            sid = fp.freeze_ohlc(frame(), ticker='TEST-USD', source='test',
                                 downloaded_at_utc='2026-09-22T00:00:00Z', requested_interval='1d',
                                 requested_range='test', run_id='test', purpose='test')
            output = self.root / 'market_forecast_lab'
            manifest = dict(**lab.new_context('TRIAL'), schema_version=2, as_of='2026-09-22', config=load_config(),
                            raw_snapshot_ids={'TEST-USD': sid}, library_order=['TEST-USD'],
                            canonical={}, quality_evaluations=[], source_hashes=lab.source_hashes(),
                            universe=[dict(coingecko_id='test', ohlc_ticker='TEST-USD', inclusion_status='INCLUDED')])
            manifest_id = lab.store_input(output, manifest)
            forecasts, _ = lab.forecasts_from_manifest(manifest, manifest_id)
            lab.immutable_append(output / 'trial_forecasts.jsonl', forecasts, ('coingecko_id', 'forecast_date'))
            before = {str(p): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
            args = SimpleNamespace(run_context=lab.new_context('REPLAY'), replay=str(output / 'inputs' / (manifest_id.split(':')[1] + '.json')),
                                   provenance_root=str(self.root), legacy_reports=str(self.root))
            with patch.object(lab.yf, 'download', side_effect=AssertionError('network forbidden')):
                lab.replay(args)
            after = {str(p): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
            self.assertEqual(before, after)
            with patch.object(lab, 'source_hashes', return_value={}):
                with self.assertRaisesRegex(ValueError, 'REPLAY_REQUIRES_ORIGINAL_SOURCE'):
                    lab.replay(args)

    def test_input_manifest_content_addressed(self):
        manifest = {'raw_snapshot_ids': {'TEST-USD': 'sha256:test'}}
        sid = lab.store_input(self.root, manifest)
        self.assertEqual(sid, lab.store_input(self.root, manifest))
        self.assertEqual(len(list((self.root / 'inputs').glob('*.json'))), 1)


class RotationQualityTests(unittest.TestCase):
    def setUp(self):
        self.config = load_config()

    def test_rotation_math_all_horizons(self):
        rows = rotation([mini_forecast('test', p50=12), mini_forecast('solana', p50=4),
                         mini_forecast('bitcoin', p50=-2)], [], self.config)
        for row in [r for r in rows if r['coingecko_id'] == 'test']:
            self.assertEqual(row['edge_vs_SOL'], 8)
            self.assertEqual(row['edge_vs_BTC'], 14)
            self.assertEqual(row['edge_vs_top50_median'], 8)
            self.assertEqual(row['P75_P25_width'], 20)

    def test_anti_churn_states(self):
        cases = [([], 'INSUFFICIENT_DATA'), ([None], 'INSUFFICIENT_DATA'),
                 ([0], 'WARMUP'), ([0, 0, 0], 'NO_CLEAR_EDGE'), ([4], 'ONE_DAY_EDGE'),
                 ([0, 4, 5], 'PERSISTENT_EDGE'), ([11], 'STRONG_CURRENT_EDGE'),
                 ([-5, 0, -4], 'PERSISTENT_RELATIVE_WEAKNESS'), ([4, 0, 0], 'NO_CLEAR_EDGE')]
        for edges, expected in cases:
            with self.subTest(edges=edges):
                self.assertEqual(edge_state(edges, self.config), expected)

    def test_persistence_not_inflated_by_same_day_versions(self):
        now = [mini_forecast('test', p50=6), mini_forecast('solana', p50=0)]
        rows = rotation(now, now * 3, self.config)
        self.assertEqual(rows[0]['states']['SOL'], 'ONE_DAY_EDGE')
        self.assertEqual(rows[0]['persistence']['SOL'], 1)

    def test_persistence_over_last_three_daily_snapshots(self):
        old = [mini_forecast(cid, date, p50) for date in ('2026-09-20', '2026-09-21')
               for cid, p50 in [('test', 6), ('solana', 0)]]
        rows = rotation([mini_forecast('test', p50=6), mini_forecast('solana', p50=0)], old, self.config)
        self.assertEqual(rows[0]['states']['SOL'], 'PERSISTENT_EDGE')
        self.assertEqual(len(rows[0]['last_3_snapshots']), 3)

    def test_missing_benchmark_and_insufficient_targets(self):
        rows = rotation([mini_forecast(valid=False)], [], self.config)
        self.assertIsNone(rows[0]['edge_vs_SOL'])
        self.assertIsNone(rows[0]['edge_vs_top50_median'])
        self.assertEqual(rows[0]['states']['SOL'], 'INSUFFICIENT_DATA')

    def test_paired_probability_na_and_n_pair(self):
        self.assertEqual(paired_probability()['N_PAIR'], 0)
        self.assertIsNone(paired_probability()['probability'])

    def test_immature_metrics_na_not_zero(self):
        q = quality_components(40, 10, 80, 40, [], self.config)
        self.assertEqual(q['label'], 'PROVISIONAL_GOOD')
        for key in ('MAE_vs_P50', 'P25_P75_coverage', 'P10_P90_coverage'):
            self.assertIsNone(q[key])

    def test_mature_quality_transparent_components(self):
        controls = [dict(p50_error_absolute=5, inside_p25_p75=True, inside_p10_p90=True)] * 30
        q = quality_components(40, 10, 80, 40, controls, self.config)
        self.assertEqual(q['label'], 'MATURE_GOOD')
        self.assertEqual(q['MAE_vs_P50'], 5)
        self.assertEqual(q['P25_P75_coverage'], 1)
        q = quality_components(40, 2, 20, 400, controls, self.config)
        self.assertEqual(q['label'], 'MATURE_MIXED')


@unittest.skipUnless(os.getenv('LAB_REAL_PARITY_REPORTS'), 'Set LAB_REAL_PARITY_REPORTS for frozen production parity')
class RealLegacyParityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reports = Path(os.environ['LAB_REAL_PARITY_REPORTS'])
        cls.raw, cls.data, cls.ids, cls.canonical = load_legacy_inputs(cls.reports, '2026-09-22')
        cls.before = {str(p): hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in cls.reports.rglob('*') if p.is_file() and 'market_forecast_lab' not in str(p)}
        cls.index = SharedSignatureIndex(cls.data)

    def parity(self, ticker):
        record = self.canonical[ticker]
        # Independent legacy baseline: its original per-target signature construction.
        expected = legacy.find_similar_patterns(ticker, self.data)
        actual, clean = self.index.match(ticker, self.data[ticker])
        pd.testing.assert_frame_equal(actual, expected, check_dtype=False)
        pd.testing.assert_frame_equal(clean, legacy.deoverlap_matches(expected), check_dtype=False)
        keys = ['similar_asset', 'start_date', 'end_date']
        self.assertEqual(clean[keys].astype(str).values.tolist(),
                         [[str(r[k]) for k in keys] for r in record['cohort']])
        self.assertEqual(len(clean), 40)
        f = build_forecast(LEGACY_IDS[ticker], ticker, record['cohort'], self.data,
                           record['current_price'], record['anchor_date'], '2026-09-22', 'test',
                           load_config(), canonical=record)
        self.assertEqual(verify_canonical(f, record, self.reports), 'PASS')

    def test_btc_parity(self):
        self.parity('BTC-USD')

    def test_sol_parity(self):
        self.parity('SOL-USD')

    def test_doge_parity(self):
        self.parity('DOGE-USD')

    def test_z_no_legacy_output_mutation(self):
        after = {str(p): hashlib.sha256(p.read_bytes()).hexdigest()
                 for p in self.reports.rglob('*') if p.is_file() and 'market_forecast_lab' not in str(p)}
        self.assertEqual(self.before, after)


if __name__ == '__main__':
    unittest.main()
