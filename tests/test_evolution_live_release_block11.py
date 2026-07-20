from __future__ import annotations
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest import mock

import evolution_live_release_admin as admin

NOW = datetime(2026, 7, 20, tzinfo=timezone.utc)


class Block11ControlTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        self.plans = root / 'plans.json'
        self.approvals = root / 'approvals.json'
        self.config = root / 'config.json'
        self.lock = root / 'lock'
        self.patchers = [
            mock.patch.object(admin, 'PLANS', self.plans),
            mock.patch.object(admin, 'APPROVALS', self.approvals),
            mock.patch.object(admin, 'CONFIG', self.config),
            mock.patch.object(admin, 'LOCK', self.lock),
        ]
        for patcher in self.patchers:
            patcher.start()
        self.config.write_text(json.dumps({'live_adapter_configured': True, 'approval_ttl_hours': 72}), encoding='utf-8')
        self.plan = {
            'plan_id': 'LIVE-1', 'plan_hash': 'abcdef1234567890',
            'status': 'LIVE_REVIEW_READY', 'candidate_id': 'C1',
            'candidate_portfolio': 'P1', 'change_domain': 'EXIT',
            'approval_confirmation': 'APPROVE LIVE LIVE-1 abcdef123456',
            'reject_confirmation': 'REJECT LIVE LIVE-1',
        }
        self.plans.write_text(json.dumps({'plans': [self.plan]}), encoding='utf-8')

    def tearDown(self):
        for patcher in reversed(self.patchers):
            patcher.stop()
        self.temp.cleanup()

    def test_01_list(self):
        self.assertEqual(admin.list_plans()[0]['plan_id'], 'LIVE-1')

    def test_02_status_has_no_execute(self):
        value = admin.status()
        self.assertFalse(value['execute_command_available'])
        self.assertNotIn('execute', value['available_commands'])

    def test_03_approve_requires_ready(self):
        self.plan['status'] = 'EVIDENCE_READY_ADAPTER_LOCKED'
        self.plans.write_text(json.dumps({'plans': [self.plan]}), encoding='utf-8')
        with self.assertRaises(RuntimeError):
            admin.approve('LIVE-1', 'tester', self.plan['approval_confirmation'], NOW)

    def test_04_approve_requires_exact_confirmation(self):
        with self.assertRaises(RuntimeError):
            admin.approve('LIVE-1', 'tester', 'wrong', NOW)

    def test_05_approve_writes_without_live(self):
        row = admin.approve('LIVE-1', 'tester', self.plan['approval_confirmation'], NOW)
        self.assertEqual(row['status'], 'APPROVED')
        self.assertFalse(row['live_execution_enabled'])
        self.assertFalse(row['live_modified'])
        self.assertFalse(row['orders_sent'])

    def test_06_adapter_must_be_configured(self):
        self.config.write_text(json.dumps({'live_adapter_configured': False}), encoding='utf-8')
        with self.assertRaises(RuntimeError):
            admin.approve('LIVE-1', 'tester', self.plan['approval_confirmation'], NOW)

    def test_07_reject(self):
        row = admin.reject('LIVE-1', 'tester', 'not suitable', self.plan['reject_confirmation'])
        self.assertEqual(row['status'], 'REJECTED')
        self.assertFalse(row['live_modified'])

    def test_08_revoke(self):
        approved = admin.approve('LIVE-1', 'tester', self.plan['approval_confirmation'], NOW)
        revoked = admin.revoke(approved['approval_id'], 'tester', f"REVOKE LIVE {approved['approval_id']}")
        self.assertEqual(revoked['status'], 'REVOKED')
        self.assertFalse(revoked['orders_sent'])


if __name__ == '__main__':
    unittest.main()
