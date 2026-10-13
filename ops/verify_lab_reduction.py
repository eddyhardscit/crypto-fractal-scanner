import sys, tempfile, shutil, hashlib, json, csv, unittest, os, socket
from pathlib import Path
stage=Path(__file__).resolve().parents[1]
base=stage
sys.path[:0]=[str(stage),str(base)]
import lab_reduction as policy
import decision_report, price_coherence_sync, data_quality_coherence_report, global_confluence_report
import risk_calibration_report
class TestReduction(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory()
  self.root=Path(self.tmp.name)/'reports'; self.root.mkdir()
 def tearDown(self):self.tmp.cleanup()
 def test_risk_quarantines_poisoned_metrics_without_touching_log(self):
  (self.root/'risk_calibration_metrics.csv').write_text('asset,avg_actual_return_30d_pct,can_influence_decision\nBTC,11943126,True\n')
  log=self.root/'risk_calibration_log.csv'; log.write_bytes(b'original,unmodified\nBTC,631.23\n')
  before=log.read_bytes()
  policy.quarantine_risk(self.root)
  rows=policy.read_csv(self.root/'risk_calibration_metrics.csv')
  self.assertEqual(len(rows),3)
  self.assertTrue(all(x['can_influence_decision']=='False' and x['avg_actual_return_30d_pct']=='' for x in rows))
  self.assertEqual(log.read_bytes(),before)
 def test_risk_consumer_fail_closed_even_if_old_csv_survives(self):
  decision_report.read_csv_rows=lambda p: (_ for _ in ()).throw(AssertionError('quarantined CSV must not be read'))
  self.assertEqual(decision_report.read_risk_calibration(),{})
 def test_suspended_artifacts_not_repriced_or_declared_current(self):
  self.assertFalse(set(price_coherence_sync.CSV_SPECS)&policy.PAUSED_PRICE_FILES)
  self.assertFalse(set(price_coherence_sync.JSON_SPECS)&policy.PAUSED_PRICE_FILES)
  self.assertFalse(set(price_coherence_sync.MARKDOWN_REPORTS)&policy.PAUSED_PRICE_FILES)
  self.assertFalse(set(data_quality_coherence_report.MODULE_PRICE_SPECS)&set(policy.PAUSED_QUALITY_NAMES))
 def test_notice_and_archive_idempotent_and_tamper_detected(self):
  log=self.root/'btc_2022_vs_sol_2026_tracking_log.csv';log.write_text('unaltered')
  old=self.root/'fractal_path_tracker.md';old.write_text('old report')
  (self.root/'latest_report.md').write_text('base report')
  policy.archive_once(self.root);policy.archive_once(self.root)
  for _ in range(2):policy.paused_notice('fractal_path_tracker',self.root)
  text=(self.root/'latest_report.md').read_text()
  self.assertEqual(text.count('<!-- FRACTAL_PATH_TRACKER_START -->'),1)
  policy.verify_frozen(self.root)
  log.write_text('changed')
  with self.assertRaisesRegex(RuntimeError,'SUSPENDED_ARTIFACT_CHANGED'):policy.verify_frozen(self.root)
 def test_validation_no_data_is_not_success(self):
  from datetime import date
  r=policy.validation_summary(self.root,date(2026,11,13))
  self.assertEqual(r['status'],'REVIEW_REQUIRED_PAUSE_EXPANSION')
  self.assertFalse(r['automatic_promotion'])
 def test_validation_excludes_current_day_and_preintervention(self):
  from datetime import date
  d=self.root/'market_forecast_lab';d.mkdir()
  rows=[{'official_daily':'True','horizon':'7','forecast_id':f'lab:OFFICIAL_DAILY:bitcoin:{day}:hash','target_date':target,'coingecko_id':'bitcoin','p50_error_absolute':'1','actual_return':'2'} for day,target in [('2026-10-13','2026-10-20'),('2026-10-14','2026-10-21'),('2026-10-15','2026-10-22')]]
  with (d/'evaluation_latest.csv').open('w') as f:
   w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
  self.assertEqual(policy.validation_summary(self.root,date(2026,10,22))['eligible_observations'],1)
suite=unittest.defaultTestLoader.loadTestsFromTestCase(TestReduction)
res=unittest.TextTestRunner(verbosity=2).run(suite)
if not res.wasSuccessful():raise SystemExit(1)
# Integration on copied reports only, with network forbidden.
with tempfile.TemporaryDirectory(prefix='lab-reduction-offline-') as tmp:
 root=Path(tmp)/'reports';root.mkdir()
 needed=['latest_report.md','latest_market_snapshot.json','latest_market_snapshot.csv','latest_scanner_summary.csv','latest_scanner_summary.json','scanner_forecast_latest.csv','technical_structure_metrics.csv','classic_technical_confirmation_metrics.csv','classic_technical_visual_metrics.csv','exchange_microstructure_metrics.csv','global_confluence_metrics.csv','risk_calibration_metrics.csv','risk_calibration_log.csv','btc_2022_vs_sol_2026_tracking_log.csv','btc_2022_vs_sol_2026_metrics.csv','fractal_path_tracker_metrics.csv','rsi_top_cycle_metrics.csv']
 for name in needed:
  p=base/'reports'/name
  if p.exists():shutil.copy2(p,root/name)
 old=os.getcwd();os.chdir(tmp)
 original_socket=socket.socket
 socket.socket=lambda *a,**k: (_ for _ in ()).throw(AssertionError('network forbidden in offline verification'))
 try:
  policy.archive_once(root)
  risk_calibration_report.main()
  for key in policy.PAUSED:__import__(key).main()
  components=global_confluence_report.build_components((root/'latest_report.md').read_text())
  assert all(components[a][c]['score']==0 for a in global_confluence_report.ASSETS for c in policy.PAUSED_COMPONENTS)
  # Restore patched reader after the dedicated fail-closed test.
  import importlib
  importlib.reload(decision_report)
  global_confluence_report.main()
  decision_report.main()
  policy.finalize(root)
  from compact_latest_report import compact_latest_report,validate_compact_structure
  compact_latest_report(root/'latest_report.md')
  text=(root/'latest_report.md').read_text();validate_compact_structure(text)
  for k in ['btc_sol_fractal','fractal_path','rsi_top_cycle','sol_onchain','extreme_cases','risk_calibration']:
   assert '<!-- COMPACT_SECTION_START:'+k+' -->' in text,k
  policy.verify_frozen(root)
  print('OFFLINE_INTEGRATION=PASS archived bytes unchanged, paused components zero, report structure valid, no network')
 finally:socket.socket=original_socket;os.chdir(old)
