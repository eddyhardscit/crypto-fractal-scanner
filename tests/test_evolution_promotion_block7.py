from __future__ import annotations
import json, tempfile, unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest import mock
import paper_trading_promotion_governor as g

NOW=datetime(2026,7,19,tzinfo=timezone.utc)

def candidate(status='CANDIDATE'):
    return {'candidate_id':'C1','strategy_id':'C1','family_id':'fam','portfolio_name':'CAND','parent_id':'P1','parent_portfolio':'PARENT','status':status,'active':True,'mutation':{'parameter':'reward_risk','old_value':1.5,'new_value':2.0}}

def review(delta=.1):
    return {'candidate_id':'C1','candidate_portfolio':'CAND','parent_portfolio':'PARENT','status':'PROMOTION_REVIEW_READY','matched_pairs':180,'mean_delta_r':delta,'bootstrap_ci_low_r':.04,'candidate_profit_factor':1.4,'parent_profit_factor':1.1}

class Block7RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); root=Path(self.tmp.name)
        names=['CONFIG_PATH','REVIEW_PATH','CANDIDATE_STATE_PATH','PROMOTION_STATE_PATH','GOVERNANCE_STATE_PATH','PLANS_PATH','EVENTS_PATH','REPORT_PATH','CONFIG_SNAPSHOT_PATH']
        self.paths={name:root/(name.lower()+('.csv' if name=='EVENTS_PATH' else '.json')) for name in names}
        self.paths['REPORT_PATH']=root/'report.md'
        self.patchers=[mock.patch.object(g,k,v) for k,v in self.paths.items()]
        [p.start() for p in self.patchers]
        self.paths['CANDIDATE_STATE_PATH'].write_text(json.dumps({'candidates':{'C1':candidate()}}))
        self.paths['REVIEW_PATH'].write_text(json.dumps({'candidates':[review()]}))
    def tearDown(self):
        [p.stop() for p in reversed(self.patchers)]; self.tmp.cleanup()
    def test_01_plan_created_for_review_ready(self):
        out=g.generate_plans(NOW); self.assertEqual(out['pending_approval'],1)
    def test_02_plan_is_stable(self):
        a=g.generate_plans(NOW)['plans'][0]['plan_id']; b=g.generate_plans(NOW)['plans'][0]['plan_id']; self.assertEqual(a,b)
    def test_03_wrong_status_no_plan(self):
        self.paths['REVIEW_PATH'].write_text(json.dumps({'candidates':[dict(review(),status='VALIDATING')]})); self.assertEqual(g.generate_plans(NOW)['plan_count'],0)
    def test_04_non_candidate_no_new_plan(self):
        self.paths['CANDIDATE_STATE_PATH'].write_text(json.dumps({'candidates':{'C1':candidate('MASTER')}})); self.assertEqual(g.generate_plans(NOW)['plan_count'],0)
    def test_05_review_change_stales_old_plan(self):
        g.generate_plans(NOW); self.paths['REVIEW_PATH'].write_text(json.dumps({'candidates':[review(.2)]})); out=g.generate_plans(NOW); self.assertEqual(sum(x['status']=='STALE' for x in out['plans']),1)
    def test_06_confirmation_strings_present(self):
        p=g.generate_plans(NOW)['plans'][0]; self.assertTrue(p['approval_confirmation'].startswith('APPROVE ')); self.assertTrue(p['execute_confirmation'].startswith('EXECUTE '))
    def test_07_no_automatic_promotion(self):
        out=g.run_promotion_governance_cycle(NOW); self.assertEqual(out['automatic_promotions'],0)
    def test_08_outputs_written(self):
        g.run_promotion_governance_cycle(NOW)
        for k in ['PLANS_PATH','GOVERNANCE_STATE_PATH','REPORT_PATH','CONFIG_SNAPSHOT_PATH']: self.assertTrue(self.paths[k].exists())
    def test_09_apply_roles_promotes_candidate(self):
        self.paths['PROMOTION_STATE_PATH'].write_text(json.dumps({'active_by_family':{'fam':{'status':'EXECUTED','candidate_id':'C1','parent_portfolio':'PARENT'}}}))
        cfg={'portfolios':[{'name':'PARENT','is_main':True},{'name':'CAND','is_main':False}]}
        out,count=g.apply_runtime_roles(cfg,{'candidates':{'C1':candidate('MASTER')}})
        by={x['name']:x for x in out['portfolios']}; self.assertFalse(by['PARENT']['is_main']); self.assertTrue(by['CAND']['is_main']); self.assertEqual(count['masters'],1)
    def test_10_no_active_promotion_keeps_config(self):
        cfg={'portfolios':[{'name':'PARENT','is_main':True},{'name':'CAND','is_main':False}]}; out,_=g.apply_runtime_roles(cfg,{'candidates':{'C1':candidate()}}); self.assertEqual(out,cfg)
    def test_11_review_hash_deterministic(self): self.assertEqual(g.review_hash(review()),g.review_hash(review()))
    def test_12_generated_time_not_in_review_hash(self):
        a=dict(review(),generated_utc='A'); b=dict(review(),generated_utc='B'); self.assertEqual(g.review_hash(a),g.review_hash(b))
    def test_13_default_safety(self):
        self.assertFalse(g.DEFAULT_CONFIG['automatic_promotion']); self.assertTrue(g.DEFAULT_CONFIG['human_approval_required']); self.assertFalse(g.DEFAULT_CONFIG['orders_allowed'])
    def test_14_plan_preserves_approved_status(self):
        out=g.generate_plans(NOW); doc=json.loads(self.paths['PLANS_PATH'].read_text()); doc['plans'][0]['status']='APPROVED'; self.paths['PLANS_PATH'].write_text(json.dumps(doc)); self.assertEqual(g.generate_plans(NOW)['plans'][0]['status'],'APPROVED')
    def test_15_active_promotion_count(self):
        self.paths['PROMOTION_STATE_PATH'].write_text(json.dumps({'active_by_family':{'fam':{'status':'EXECUTED'}}})); self.assertEqual(g.run_promotion_governance_cycle(NOW)['active_promotions'],1)
    def test_16_governor_never_modifies_candidate_state(self):
        before=self.paths['CANDIDATE_STATE_PATH'].read_text(); g.run_promotion_governance_cycle(NOW); self.assertEqual(before,self.paths['CANDIDATE_STATE_PATH'].read_text())
if __name__=='__main__': unittest.main()
