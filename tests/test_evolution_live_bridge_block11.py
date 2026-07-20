from __future__ import annotations
import csv
import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

import paper_trading_live_bridge as bridge

NOW = datetime(2026, 7, 20, tzinfo=timezone.utc)


def candidate(status='MASTER', mutation=None):
    return {
        'candidate_id': 'C1', 'portfolio_name': 'PORT-C1', 'family_id': 'trend',
        'status': status,
        'mutation': mutation or {
            'parameter': 'reward_risk', 'old_value': 1.5, 'new_value': 2.0,
            'mutation_type': 'single_parameter',
        },
    }


def transaction(days=40):
    return {
        'transaction_id': 'TX1', 'candidate_id': 'C1', 'status': 'EXECUTED',
        'executed_utc': bridge.iso(NOW - timedelta(days=days)),
    }


def validation(pairs=250, score=90, status='PROMOTION_REVIEW_READY'):
    return {'candidate_id': 'C1', 'matched_pairs': pairs, 'validation_score': score, 'status': status}


def post(pairs=180, health=85, status='HEALTHY'):
    return {'transaction_id': 'TX1', 'master_candidate_id': 'C1', 'matched_pairs': pairs, 'health_score': health, 'status': status}


def score(value=90, grade='A'):
    return {'strategy_id': 'C1', 'evolution_score': value, 'grade': grade}


def trades(n=120, r=0.2, liquidation=False):
    rows = []
    for index in range(n):
        rows.append({
            'portfolio': 'PORT-C1', 'asset': 'SOL',
            'closed_at': bridge.iso(NOW), 'r_multiple': r,
            'close_reason': 'LIQUIDATION' if liquidation and index == 0 else 'EXIT',
        })
    if n > 4 and not liquidation:
        rows[-1]['r_multiple'] = -1.0
    return rows


class Block11RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        names = {
            'CONFIG_PATH': 'config.json', 'CANDIDATE_STATE': 'candidate.json',
            'VALIDATIONS': 'validations.csv', 'PROMOTION_STATE': 'promotions.json',
            'POST_PROMOTION': 'post.csv', 'EVOLUTION_SCORES': 'scores.csv',
            'GENETIC_MEMORY': 'genetic.json', 'REGIME_MEMORY': 'regime.json',
            'CRASH_GUARD_STATE': 'crash.json', 'TRADE_LOG': 'trades.csv',
            'APPROVALS': 'approvals.json', 'STATE': 'state.json',
            'CANDIDATES_CSV': 'candidates.csv', 'PLANS': 'plans.json',
            'HISTORY': 'history.csv', 'REPORT': 'report.md',
            'CONFIG_SNAPSHOT': 'snapshot.json',
        }
        self.paths = {key: root / value for key, value in names.items()}
        self.patchers = [mock.patch.object(bridge, key, value) for key, value in self.paths.items()]
        for patcher in self.patchers:
            patcher.start()

    def tearDown(self):
        for patcher in reversed(self.patchers):
            patcher.stop()
        self.temp.cleanup()

    def write_csv(self, path, rows):
        if not rows:
            path.write_text('', encoding='utf-8')
            return
        fields = sorted({key for row in rows for key in row})
        with path.open('w', encoding='utf-8', newline='') as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader(); writer.writerows(rows)

    def inputs(self, *, cand=None, tx=None, val=None, postrow=None, scorerow=None,
               genetic=None, regime=None, crash='NORMAL', traderows=None, adapter=False,
               approvals=None):
        cand = cand or candidate(); tx = tx or transaction(); val = val or validation()
        postrow = postrow or post(); scorerow = scorerow or score()
        self.paths['CONFIG_PATH'].write_text(json.dumps({'live_adapter_configured': adapter}), encoding='utf-8')
        self.paths['CANDIDATE_STATE'].write_text(json.dumps({'candidates': {'C1': cand}}), encoding='utf-8')
        self.paths['PROMOTION_STATE'].write_text(json.dumps({'transactions': [tx], 'active_by_family': {}}), encoding='utf-8')
        self.write_csv(self.paths['VALIDATIONS'], [val])
        self.write_csv(self.paths['POST_PROMOTION'], [postrow])
        self.write_csv(self.paths['EVOLUTION_SCORES'], [scorerow])
        self.paths['GENETIC_MEMORY'].write_text(json.dumps(genetic or {'records': {}}), encoding='utf-8')
        self.paths['REGIME_MEMORY'].write_text(json.dumps(regime or {
            'current_regime': 'BULL_TREND',
            'records': {'trend|BULL_TREND': {'status': 'FAVOR', 'closed_trades': 60}},
        }), encoding='utf-8')
        self.paths['CRASH_GUARD_STATE'].write_text(json.dumps({'previous_level': crash}), encoding='utf-8')
        self.write_csv(self.paths['TRADE_LOG'], traderows if traderows is not None else trades())
        self.paths['APPROVALS'].write_text(json.dumps(approvals or {'approvals': []}), encoding='utf-8')

    def evaluate(self, **kwargs):
        self.inputs(**kwargs)
        result = bridge.run_live_bridge_cycle(NOW)
        plans = json.loads(self.paths['PLANS'].read_text(encoding='utf-8'))['plans']
        return result, plans[0]

    def test_01_empty_cycle(self):
        self.paths['CONFIG_PATH'].write_text('{}', encoding='utf-8')
        self.paths['CANDIDATE_STATE'].write_text('{"candidates":{}}', encoding='utf-8')
        self.paths['PROMOTION_STATE'].write_text('{"transactions":[],"active_by_family":{}}', encoding='utf-8')
        for key in ('VALIDATIONS', 'POST_PROMOTION', 'EVOLUTION_SCORES', 'TRADE_LOG'):
            self.paths[key].write_text('', encoding='utf-8')
        for key, value in (('GENETIC_MEMORY', {'records': {}}), ('REGIME_MEMORY', {'records': {}}), ('CRASH_GUARD_STATE', {}), ('APPROVALS', {'approvals': []})):
            self.paths[key].write_text(json.dumps(value), encoding='utf-8')
        result = bridge.run_live_bridge_cycle(NOW)
        self.assertEqual(result['plans'], 0)

    def test_02_exit_domain(self):
        self.assertEqual(bridge.mutation_domain({'parameter': 'reward_risk'}), 'EXIT')

    def test_03_entry_domain(self):
        self.assertEqual(bridge.mutation_domain({'parameter': 'entry_rsi'}), 'ENTRY')

    def test_04_risk_domain(self):
        self.assertEqual(bridge.mutation_domain({'parameter': 'risk_per_trade'}), 'RISK')

    def test_05_unknown_domain(self):
        self.assertEqual(bridge.mutation_domain({'parameter': 'foo'}), 'UNKNOWN')

    def test_06_non_master_rejected(self):
        _, plan = self.evaluate(cand=candidate(status='CANDIDATE'))
        self.assertIn('NOT_CURRENT_PAPER_MASTER', plan['reason_codes'])

    def test_07_validation_sample_gate(self):
        _, plan = self.evaluate(val=validation(pairs=199))
        self.assertIn('VALIDATION_SAMPLE_TOO_SMALL', plan['reason_codes'])

    def test_08_validation_score_gate(self):
        _, plan = self.evaluate(val=validation(score=84))
        self.assertIn('VALIDATION_SCORE_TOO_LOW', plan['reason_codes'])

    def test_09_post_health_gate(self):
        _, plan = self.evaluate(postrow=post(status='WATCH'))
        self.assertIn('POST_PROMOTION_NOT_HEALTHY', plan['reason_codes'])

    def test_10_monitoring_days_gate(self):
        _, plan = self.evaluate(tx=transaction(days=29))
        self.assertIn('POST_PROMOTION_MONITORING_TOO_SHORT', plan['reason_codes'])

    def test_11_evolution_score_gate(self):
        _, plan = self.evaluate(scorerow=score(value=84))
        self.assertIn('EVOLUTION_SCORE_TOO_LOW', plan['reason_codes'])

    def test_12_sol_sample_gate(self):
        _, plan = self.evaluate(traderows=trades(n=99))
        self.assertIn('SOL_SAMPLE_TOO_SMALL', plan['reason_codes'])

    def test_13_liquidation_gate(self):
        _, plan = self.evaluate(traderows=trades(liquidation=True))
        self.assertIn('SOL_LIQUIDATION_PRESENT', plan['reason_codes'])

    def test_14_crash_guard_gate(self):
        _, plan = self.evaluate(crash='CRASH')
        self.assertIn('CRASH_GUARD_NOT_NORMAL', plan['reason_codes'])

    def test_15_genetic_avoid_gate(self):
        genetic = {'records': {'x': {'family_id': 'trend', 'parameter': 'reward_risk', 'status': 'AVOID'}}}
        _, plan = self.evaluate(genetic=genetic)
        self.assertIn('GENETIC_MEMORY_BLOCK', plan['reason_codes'])

    def test_16_regime_avoid_gate(self):
        regime = {'current_regime': 'BULL_TREND', 'records': {'trend|BULL_TREND': {'status': 'AVOID', 'closed_trades': 100}}}
        _, plan = self.evaluate(regime=regime)
        self.assertIn('REGIME_MEMORY_NOT_READY', plan['reason_codes'])

    def test_17_adapter_locked_when_evidence_ready(self):
        _, plan = self.evaluate(adapter=False)
        self.assertTrue(plan['evidence_ready'])
        self.assertEqual(plan['status'], 'EVIDENCE_READY_ADAPTER_LOCKED')

    def test_18_adapter_true_cannot_enable_execution(self):
        result, plan = self.evaluate(adapter=True)
        self.assertEqual(plan['status'], 'LIVE_REVIEW_READY')
        self.assertFalse(result['live_execution_enabled'])

    def test_19_valid_approval_changes_status(self):
        self.inputs(adapter=True)
        first = bridge.run_live_bridge_cycle(NOW)
        plan = json.loads(self.paths['PLANS'].read_text(encoding='utf-8'))['plans'][0]
        approval = {'plan_id': plan['plan_id'], 'plan_hash': plan['plan_hash'], 'status': 'APPROVED', 'expires_utc': bridge.iso(NOW + timedelta(hours=24))}
        self.paths['APPROVALS'].write_text(json.dumps({'approvals': [approval]}), encoding='utf-8')
        bridge.run_live_bridge_cycle(NOW)
        updated = json.loads(self.paths['PLANS'].read_text(encoding='utf-8'))['plans'][0]
        self.assertEqual(updated['status'], 'APPROVED_WAITING_EXPLICIT_EXECUTION')

    def test_20_plan_id_is_stable(self):
        _, first = self.evaluate(adapter=True)
        bridge.run_live_bridge_cycle(NOW)
        second = json.loads(self.paths['PLANS'].read_text(encoding='utf-8'))['plans'][0]
        self.assertEqual(first['plan_id'], second['plan_id'])

    def test_21_outputs_and_safety(self):
        result, _ = self.evaluate()
        for key in ('STATE', 'CANDIDATES_CSV', 'PLANS', 'HISTORY', 'REPORT', 'CONFIG_SNAPSHOT'):
            self.assertTrue(self.paths[key].exists())
        self.assertEqual(result['automatic_releases'], 0)
        self.assertFalse(result['live_modified'])
        self.assertFalse(result['orders_sent'])

    def test_22_config_forces_locked_mode(self):
        self.paths['CONFIG_PATH'].write_text(json.dumps({'mode': 'LIVE', 'live_execution_enabled': True, 'orders_allowed': True}), encoding='utf-8')
        config = bridge.load_config()
        self.assertEqual(config['mode'], 'LOCKED_REVIEW_ONLY')
        self.assertFalse(config['live_execution_enabled'])
        self.assertFalse(config['orders_allowed'])


if __name__ == '__main__':
    unittest.main()
