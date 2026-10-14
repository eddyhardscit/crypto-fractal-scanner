"""Calendar outcomes must use original closes, independently of RSI validity."""
import unittest
from unittest.mock import patch
import numpy as np
import pandas as pd
import scanner
from market_forecast_lab_engine import SharedSignatureIndex, paths_from_cohort

def prices():
    dates = pd.date_range('2023-01-01', periods=800)
    close = 100 + np.sin(np.arange(800) / 9) * 8 + np.arange(800) / 20
    # 15 identical closes give 14 zero differences: RSI is undefined.
    close[450:465] = close[450]
    return pd.DataFrame(dict(Open=close, High=close+1, Low=close-1,
                             Close=close, Volume=np.full(800, 100.)), index=dates)

class CalendarOutcomeTests(unittest.TestCase):
    def test_flat_price_day_is_not_missing_price(self):
        raw = prices()
        processed = scanner.add_indicators(raw)
        anchor = raw.index[410]
        self.assertNotIn(raw.index[464], processed.index)
        expected = (raw.Close.iloc[470] / raw.Close.iloc[410] - 1) * 100
        actual = scanner.future_stats(processed, processed.index.get_loc(anchor), raw)
        self.assertAlmostEqual(actual['return_60d'], expected)
        valid, paths = paths_from_cohort([dict(similar_asset='A', end_date=str(anchor.date()))], {'A': raw})
        self.assertEqual(len(valid), 1)
        self.assertAlmostEqual(paths[0, 60], expected)

    def test_contiguous_prices_preserve_all_statistics(self):
        raw = prices().iloc[:400]
        actual = scanner.future_stats(raw, 250, raw)
        for days in scanner.FORWARD_DAYS:
            segment = raw.Close.iloc[250:251+days]
            for metric, value in [('return', segment.iloc[-1]), ('drawdown', segment.min()), ('max_gain', segment.max())]:
                self.assertEqual(actual[f'{metric}_{days}d'], (value / segment.iloc[0] - 1) * 100)

    def test_true_gap_is_rejected_not_shifted(self):
        raw = prices().drop(prices().index[464])
        result = scanner.future_stats(raw, 410, raw)
        self.assertTrue(np.isnan(result['return_60d']))
        valid, paths = paths_from_cohort([dict(similar_asset='A', end_date=str(raw.index[410].date()))], {'A': raw})
        self.assertEqual(len(valid), 0)

    def test_invalid_close_or_duplicate_dates_fail_closed(self):
        for invalid in (0, -1, float('nan'), float('inf')):
            raw = prices()
            raw.loc[raw.index[430], 'Close'] = invalid
            self.assertTrue(np.isnan(scanner.future_stats(raw, 410, raw)['return_60d']))
        raw = prices()
        raw = pd.concat([raw, raw.iloc[[430]]]).sort_index()
        self.assertTrue(np.isnan(scanner.future_stats(raw, 410, raw)['return_60d']))

    def test_shared_index_keeps_selection_and_uses_raw_outcomes(self):
        raw = {'A': prices(), 'B': prices() * 1.03}
        processed = {t: scanner.add_indicators(f) for t, f in raw.items()}
        expected = scanner.find_similar_patterns('A', processed, raw)
        actual, _ = SharedSignatureIndex(processed, raw).match('A', processed['A'])
        pd.testing.assert_frame_equal(actual, expected, check_dtype=False)
        old_selection = scanner.find_similar_patterns('A', processed)
        cols = ['target','similar_asset','start_date','end_date','similarity']
        pd.testing.assert_frame_equal(actual[cols], old_selection[cols])


    def test_manifest_canonical_uses_raw_paths(self):
        import market_forecast_lab as lab
        from market_forecast_lab_universe import load_config
        raw = prices()
        anchor_date = str(raw.index[410].date())
        cohort = [dict(similar_asset='A', start_date='2023-01-01', end_date=anchor_date,
                       similarity=90., rank=i+1, **scanner.future_stats(raw, 410, raw)) for i in range(40)]
        canonical = dict(cohort=cohort, current_price=100., anchor_date=anchor_date)
        manifest = dict(lab.new_context('TRIAL'), raw_snapshot_ids={'A':'frozen'},
                        library_order=['A'], universe=[dict(inclusion_status='INCLUDED',
                        coingecko_id='test', ohlc_ticker='A')], canonical={'A':canonical},
                        as_of='2026-10-11', config=load_config(), quality_evaluations=[])
        with patch.object(lab.fp, 'load_frozen_ohlc', return_value=raw):
            forecasts, _ = lab.forecasts_from_manifest(manifest, 'fixture', index=object())
        self.assertEqual(forecasts[0]['N'], 40)
        self.assertEqual(forecasts[0]['cohort'], cohort)
        self.assertAlmostEqual(forecasts[0]['paths'][60]['p50'],
                               (raw.Close.iloc[470]/raw.Close.iloc[410]-1)*100)

    def test_timezone_and_missing_short_horizon(self):
        raw = prices()
        raw.index = raw.index.tz_localize('UTC')
        result = scanner.future_stats(raw, 410, raw)
        self.assertEqual(len(scanner.calendar_close_path(raw, str(raw.index[410].date()), 60)), 61)
        broken = raw.drop(raw.index[415])
        self.assertTrue(all(np.isnan(x) for x in scanner.future_stats(broken, 410, broken).values()))


    def test_interior_canonical_error_cannot_hide_in_quantiles(self):
        from market_forecast_lab_engine import build_forecast
        from market_forecast_lab_universe import load_config
        raw = prices()
        row = dict(similar_asset='A', end_date=str(raw.index[410].date()), similarity=90.,
                   **scanner.future_stats(raw, 410, raw))
        row['return_60d'] += .1
        with self.assertRaisesRegex(ValueError, 'CANONICAL_PATH_STATISTICS_MISMATCH'):
            build_forecast('test','A',[row],{'A':raw},100.,'2026-10-11',
                           '2026-10-11','fixture',load_config(),canonical={'forecast_id':'old'})


    def test_default_call_never_counts_rows_as_calendar_days(self):
        raw = prices()
        broken = raw.drop(raw.index[464])
        self.assertTrue(np.isnan(scanner.future_stats(broken, 410)['return_60d']))

if __name__ == '__main__':
    unittest.main()
