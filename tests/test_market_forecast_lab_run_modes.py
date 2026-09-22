"""Run-boundary tests: real file IO in isolated directories, no official writes."""
import copy
import io
import json
from pathlib import Path
import tempfile
import unittest
from contextlib import redirect_stderr
from types import SimpleNamespace
from unittest.mock import patch

import pandas as pd

import forecast_provenance as fp
import market_forecast_lab as lab
import market_forecast_lab_run as run
from market_forecast_lab_universe import load_config


def fingerprint(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob('*') if p.is_file()}


class RunModeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=Path(lab.ROOT).parent)
        self.root = Path(self.temp.name)
        self.reports = self.root / 'official/reports'
        self.provenance = self.reports / 'forecast_provenance'
        (self.provenance / 'raw_ohlc').mkdir(parents=True)
        (self.provenance / 'raw_market_snapshots.jsonl').write_text('')
        self.official = self.reports / 'market_forecast_lab'
        self.official_ctx = run.new_context('OFFICIAL_DAILY')
        run.initialize_scope(self.official, self.official_ctx)
        self.before = fingerprint(self.reports)

    def tearDown(self):
        self.temp.cleanup()

    def args(self, **kw):
        return SimpleNamespace(output=kw.get('output'), trial_root=kw.get('trial_root'))

    def payload(self, ctx):
        f = dict(**ctx, coingecko_id='bitcoin', forecast_date='2026-09-22',
                 forecast_id='lab:' + ctx['run_mode'] + ':fixture', input_manifest_id='sha256:test',
                 anchor_price=100, anchor_date='2026-09-22', N=40, status='VALID', rotation_ready=True,
                 paths=[dict(day=i,N=40,p10=-10,p25=-5,p50=2,p75=5,p90=10) for i in range(61)],
                 headlines=[dict(horizon=h, cone_width=10, quality={'N':40}) for h in (7,14,30,60)])
        u = dict(**ctx, snapshot_date='2026-09-22', rows=[dict(**ctx,coingecko_id='bitcoin',inclusion_status='INCLUDED')])
        evaluation = dict(forecast_id=f['forecast_id'], coingecko_id='bitcoin',horizon=1,actual_close=102)
        return u,[f],[evaluation]

    def trial_export(self):
        ctx = run.new_context('TRIAL')
        out,store = run.prepare_paths(self.args(trial_root=str(self.root/'evidence')), ctx,
                                      self.provenance,self.reports,lab.ROOT)
        u,fs,es = self.payload(ctx)
        lab.export(out,u,fs,[],es,load_config(),ctx)
        return out,store,ctx

    def test_manual_without_mode_cannot_become_official(self):
        with patch.object(lab,'execute') as execute,redirect_stderr(io.StringIO()),self.assertRaises(SystemExit) as raised:
            lab.main([])
        self.assertEqual(raised.exception.code,2)
        execute.assert_not_called()
        self.assertEqual(self.before,fingerprint(self.reports))

    def test_trial_does_not_append_official_universe_history(self):
        self.trial_export()
        self.assertFalse((self.official/'universe_history.jsonl').exists())
        self.assertEqual(self.before,fingerprint(self.reports))

    def test_trial_does_not_append_official_forecast_history(self):
        self.trial_export()
        self.assertFalse((self.official/'forecast_vintages.jsonl').exists())
        self.assertEqual(self.before,fingerprint(self.reports))

    def test_trial_does_not_append_official_path_history(self):
        self.trial_export()
        self.assertFalse((self.official/'forecast_path_versions.jsonl').exists())
        self.assertEqual(self.before,fingerprint(self.reports))

    def test_trial_does_not_append_official_evaluation_history(self):
        self.trial_export()
        self.assertFalse((self.official/'evaluation_versions.jsonl').exists())
        self.assertEqual(self.before,fingerprint(self.reports))

    def test_trial_raw_acquisition_does_not_modify_official_provenance(self):
        ctx=run.new_context('TRIAL');out,store=run.prepare_paths(self.args(trial_root=str(self.root/'evidence')),ctx,self.provenance,self.reports,lab.ROOT)
        frame=pd.DataFrame(dict(Open=[1.],High=[1.],Low=[1.],Close=[1.],Volume=[1.]),index=pd.to_datetime(['2026-09-22']))
        # Seed an isolated store, then perform an actual CAS install and ledger append.
        run.seed_trial_store(self.provenance,store,{}, {},ctx)
        with patch.multiple(fp,ROOT=store,RAW_DIR=store/'raw_ohlc',RAW_INDEX=store/'raw_market_snapshots.jsonl'):
            run.freeze_run_ohlc(frame,ticker='TEST-USD',as_of='2026-09-22',ctx=ctx)
        self.assertEqual(self.before,fingerprint(self.reports))
        row=json.loads((store/'raw_market_snapshots.jsonl').read_text())
        self.assertEqual(row['run_mode'],'TRIAL');self.assertIs(row['official_daily'],False)

    def test_trial_writer_cannot_use_official_root_even_directly(self):
        with patch.multiple(fp,ROOT=self.provenance,RAW_DIR=self.provenance/'raw_ohlc',RAW_INDEX=self.provenance/'raw_market_snapshots.jsonl'):
            with self.assertRaisesRegex(ValueError,'TRIAL_PROVENANCE_ISOLATION_REQUIRED'):
                run.freeze_run_ohlc(pd.DataFrame(),ticker='TEST',as_of='2026-09-22',ctx=run.new_context('TRIAL'))
        self.assertEqual(self.before,fingerprint(self.reports))

    def test_official_daily_appends_all_expected_histories(self):
        u,fs,es=self.payload(self.official_ctx)
        lab.export(self.official,u,fs,[],es,load_config(),self.official_ctx)
        for name in run.HISTORIES:
            rows=fp._read_jsonl(self.official/name)
            self.assertEqual(len(rows),1,name)
            self.assertTrue(all(run.is_official(r) for r in rows),name)
        self.assertIsNotNone(run.read_official_latest(self.official/'latest.json'))

    def test_official_daily_records_true(self):
        u,fs,es=self.payload(self.official_ctx);lab.export(self.official,u,fs,[],es,load_config(),self.official_ctx)
        f=fp._read_jsonl(self.official/'forecast_vintages.jsonl')[0]
        self.assertIs(f['official_daily'],True)
        for key in (*run.CONTEXT_FIELDS,'forecast_date','forecast_id','input_manifest_id'):self.assertIn(key,f)

    def test_trial_records_false_and_no_official_history_filenames(self):
        out,_,_=self.trial_export()
        for f in fp._read_jsonl(out/'trial_forecasts.jsonl'):
            self.assertIs(f['official_daily'],False);self.assertEqual(f['run_mode'],'TRIAL')
        for name in run.HISTORIES:self.assertFalse((out/name).exists())
        paths=json.loads((out/'forecast_paths_latest.json').read_text());self.assertEqual(paths['run_mode'],'TRIAL')

    def test_official_view_excludes_trial_and_unclassified(self):
        out,_,_=self.trial_export()
        self.assertIsNone(run.read_official_latest(out/'latest.json'))
        rows=[self.official_ctx,run.new_context('TRIAL'),dict(official_daily=True),dict(run_mode='OFFICIAL_DAILY')]
        self.assertEqual(run.official_rows(rows),[self.official_ctx])

    def test_mixed_mode_official_latest_rejected(self):
        u,fs,es=self.payload(self.official_ctx);lab.export(self.official,u,fs,[],es,load_config(),self.official_ctx)
        p=self.official/'latest.json';value=json.loads(p.read_text());value['forecasts'][0].update(run.new_context('TRIAL'));p.write_text(json.dumps(value))
        with self.assertRaisesRegex(ValueError,'MIXED_MODE_OFFICIAL_VIEW'):run.read_official_latest(p)

    def test_replay_cannot_export_or_append_provenance(self):
        ctx=run.new_context('REPLAY')
        with self.assertRaisesRegex(ValueError,'REPLAY_EXPORT_FORBIDDEN'):
            lab.export(self.official,{},[],[],[],load_config(),ctx)
        with self.assertRaisesRegex(ValueError,'REPLAY_PROVENANCE_WRITE_FORBIDDEN'):
            run.freeze_run_ohlc(pd.DataFrame(),ticker='TEST',as_of='2026-09-22',ctx=ctx)
        self.assertEqual(self.before,fingerprint(self.reports))

    def test_replay_cli_rejects_writable_paths(self):
        with redirect_stderr(io.StringIO()),self.assertRaises(SystemExit):
            lab.main(['--mode','REPLAY','--replay','x','--output',str(self.official)])

    def test_trial_paths_reject_official_aliases(self):
        for base in (self.provenance,self.reports):
            with self.assertRaisesRegex(ValueError,'TRIAL_ROOT_OVERLAPS_OFFICIAL_DATA'):
                run.prepare_paths(self.args(trial_root=str(base)),run.new_context('TRIAL'),self.provenance,self.reports,lab.ROOT)
        alias=self.root/'alias';alias.symlink_to(self.provenance,target_is_directory=True)
        with self.assertRaisesRegex(ValueError,'TRIAL_ROOT_OVERLAPS_OFFICIAL_DATA'):
            run.prepare_paths(self.args(trial_root=str(alias)),run.new_context('TRIAL'),self.provenance,self.reports,lab.ROOT)

    def test_trial_rejects_source_reports_even_with_alternate_legacy_reports(self):
        with self.assertRaisesRegex(ValueError,'TRIAL_ROOT_OVERLAPS_OFFICIAL_DATA'):
            run.prepare_paths(self.args(trial_root=str(self.reports/'other')),run.new_context('TRIAL'),
                              self.provenance,self.root/'different-reports',lab.ROOT)

    def test_official_acquisition_records_explicit_mode(self):
        frame=pd.DataFrame(dict(Open=[1.],High=[1.],Low=[1.],Close=[1.],Volume=[1.]),index=pd.to_datetime(['2026-09-22']))
        with patch.multiple(fp,ROOT=self.provenance,RAW_DIR=self.provenance/'raw_ohlc',RAW_INDEX=self.provenance/'raw_market_snapshots.jsonl'):
            run.freeze_run_ohlc(frame,ticker='TEST-USD',as_of='2026-09-22',ctx=self.official_ctx)
        row=json.loads((self.provenance/'raw_market_snapshots.jsonl').read_text())
        self.assertTrue(run.is_official(row))
        self.assertEqual(row['run_id'],self.official_ctx['run_id'])

    def test_trial_cannot_choose_official_output(self):
        with self.assertRaisesRegex(ValueError,'TRIAL_USES_TRIAL_ROOT'):
            run.prepare_paths(self.args(output=str(self.official)),run.new_context('TRIAL'),self.provenance,self.reports,lab.ROOT)

    def test_direct_trial_history_gate_rejected(self):
        with self.assertRaisesRegex(ValueError,'OFFICIAL_HISTORY_WRITE_FORBIDDEN'):
            lab.append_official_history(self.official,'forecast_vintages.jsonl',[],('forecast_id',),run.new_context('TRIAL'))

    def test_official_cannot_adopt_pre_release_trial_artifacts(self):
        legacy=self.root/'pre-release/market_forecast_lab';legacy.mkdir(parents=True);(legacy/'forecast_vintages.jsonl').write_text('{}\n')
        with self.assertRaisesRegex(ValueError,'UNCLASSIFIED_OUTPUT_DIRECTORY_REJECTED'):
            run.initialize_scope(legacy,self.official_ctx)

    def test_official_history_rejects_trial_rows(self):
        (self.official/'forecast_vintages.jsonl').write_text(json.dumps(run.new_context('TRIAL'))+'\n')
        with self.assertRaisesRegex(ValueError,'NON_OFFICIAL_HISTORY_REJECTED'):
            run.read_history(self.official,'forecast_vintages.jsonl',self.official_ctx)

    def test_run_ids_are_unique_across_trials_and_modes(self):
        records=[run.new_context(mode) for mode in run.MODES for _ in range(2)]
        self.assertEqual(len({r['run_id'] for r in records}),6)


if __name__=='__main__':unittest.main()
