"""Failure injection around the official directory commit, using real filesystem IO."""
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import forecast_provenance as fp
import market_forecast_lab as lab
import market_forecast_lab_publication as publication
import market_forecast_lab_run as run
from market_forecast_lab_universe import load_config


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=lab.ROOT.parent)
        self.root = Path(self.temp.name)
        self.output = self.root / 'reports/market_forecast_lab'
        self.output.parent.mkdir()
        self.runtime = self.root / 'runtime'
        self.ctx = run.new_context('OFFICIAL_DAILY')

    def tearDown(self):
        self.temp.cleanup()

    def snapshot(self):
        return {str(p.relative_to(self.output)): p.read_bytes() for p in self.output.rglob('*') if p.is_file()}

    def write(self, stage, day='2026-09-22', complete=True):
        u = dict(**self.ctx, snapshot_date=day, rows=[])
        lab.export(stage, u, [], [], [], load_config(), dict(**self.ctx, universe_complete=complete))

    def publish(self):
        with publication.official_transaction(self.output, self.runtime, self.ctx) as stage:
            self.write(stage)

    def test_first_generation_appears_only_at_commit(self):
        with publication.official_transaction(self.output, self.runtime, self.ctx) as stage:
            self.write(stage)
            self.assertFalse(self.output.exists())
        self.assertIsNotNone(run.read_official_latest(self.output/'latest.json'))

    def test_first_failure_leaves_no_official_directory(self):
        with self.assertRaisesRegex(RuntimeError, 'injected'):
            with publication.official_transaction(self.output, self.runtime, self.ctx) as stage:
                self.write(stage)
                raise RuntimeError('injected')
        self.assertFalse(self.output.exists())

    def test_failure_between_history_appends_retains_all_last_valid_bytes(self):
        self.publish(); before=self.snapshot()
        original=lab.append_official_history
        def fail(out,name,*args):
            if name == 'forecast_path_versions.jsonl': raise RuntimeError('injected')
            return original(out,name,*args)
        with patch.object(lab,'append_official_history',side_effect=fail),self.assertRaises(RuntimeError):
            with publication.official_transaction(self.output,self.runtime,self.ctx) as stage:
                self.write(stage,day='2026-09-23')
        self.assertEqual(before,self.snapshot())

    def test_failure_between_latest_files_retains_last_valid_bytes(self):
        self.publish();before=self.snapshot()
        original=lab.write_csv
        def fail(path,*args):
            if path.name=='rotation_latest.csv':raise RuntimeError('injected')
            return original(path,*args)
        with patch.object(lab,'write_csv',side_effect=fail),self.assertRaises(RuntimeError):
            with publication.official_transaction(self.output,self.runtime,self.ctx) as stage:
                self.write(stage,day='2026-09-23')
        self.assertEqual(before,self.snapshot())

    def test_incomplete_universe_cannot_replace_valid_generation(self):
        self.publish();before=self.snapshot()
        with self.assertRaisesRegex(ValueError,'INCOMPLETE_OFFICIAL_GENERATION'):
            with publication.official_transaction(self.output,self.runtime,self.ctx) as stage:
                self.write(stage,day='2026-09-23',complete=False)
        self.assertEqual(before,self.snapshot())

    def test_failed_rename_retains_last_valid_generation(self):
        self.publish();before=self.snapshot()
        with patch.object(publication,'exchange_directories',side_effect=OSError('injected')),self.assertRaises(OSError):
            with publication.official_transaction(self.output,self.runtime,self.ctx) as stage:self.write(stage,day='2026-09-23')
        self.assertEqual(before,self.snapshot())

    def test_same_day_histories_are_idempotent(self):
        self.publish();before=self.snapshot()
        self.publish()
        for name in run.HISTORIES:self.assertEqual(before[name],self.snapshot()[name])

    def test_next_day_retains_history_and_exchanges_whole_directory(self):
        self.publish();old=(self.output/'universe_history.jsonl').read_bytes()
        with publication.official_transaction(self.output,self.runtime,self.ctx) as stage:
            self.write(stage,day='2026-09-23')
            self.assertEqual((self.output/'universe_history.jsonl').read_bytes(),old)
        rows=fp._read_jsonl(self.output/'universe_history.jsonl')
        self.assertEqual([r['snapshot_date'] for r in rows],['2026-09-22','2026-09-23'])

    def test_history_truncation_rejected_before_commit(self):
        self.publish();before=self.snapshot()
        with self.assertRaisesRegex(ValueError,'OFFICIAL_HISTORY_NOT_APPEND_ONLY'):
            with publication.official_transaction(self.output,self.runtime,self.ctx) as stage:
                self.write(stage,day='2026-09-23')
                (stage/'universe_history.jsonl').write_text('')
        self.assertEqual(before,self.snapshot())

    def test_missing_manifest_rejected_before_commit(self):
        self.publish();before=self.snapshot()
        with self.assertRaises(FileNotFoundError):
            with publication.official_transaction(self.output,self.runtime,self.ctx) as stage:
                self.write(stage,day='2026-09-23')
                path=stage/'latest.json';latest=json.loads(path.read_text())
                latest['forecasts']=[dict(**self.ctx,input_manifest_id='sha256:'+'a'*64)]
                path.write_text(json.dumps(latest))
        self.assertEqual(before,self.snapshot())

    def test_concurrent_writer_cannot_enter(self):
        with publication.official_transaction(self.output,self.runtime,self.ctx) as stage:
            with self.assertRaises(BlockingIOError):
                with publication.official_transaction(self.output,self.runtime,self.ctx):pass
            self.write(stage)

    def test_runtime_files_never_published(self):
        with publication.official_transaction(self.output,self.runtime,self.ctx) as stage:
            self.write(stage);(stage/'.run.lock').touch();(stage/'.yfinance-cache').mkdir()
            (stage/'.yfinance-cache/cache.sqlite').write_text('runtime')
        self.assertFalse((self.output/'.run.lock').exists())
        self.assertFalse((self.output/'.yfinance-cache').exists())

    def test_publisher_failure_continues_after_paper_and_logs_marker(self):
        text=(lab.ROOT/'deploy/crypto-daily-scanner-cycle').read_text()
        start=text.index('if ! "$PYTHON" market_forecast_lab.py')
        self.assertGreater(start,text.index('"$PYTHON" paper_trading_report.py'))
        block=text[start:text.index('\nfi',start)+3]
        result=subprocess.run(['bash','-c','set -Eeuo pipefail\nPYTHON=/bin/false\n'+block+'\necho PUBLISHER_CONTINUES'],capture_output=True,text=True)
        self.assertEqual(result.returncode,0)
        self.assertEqual(result.stdout.splitlines(),['MARKET_FORECAST_LAB_FAILED','PUBLISHER_CONTINUES'])
        self.assertIn('--mode OFFICIAL_DAILY',block)
        self.assertIn('git add reports/',text)


if __name__=='__main__':unittest.main()
