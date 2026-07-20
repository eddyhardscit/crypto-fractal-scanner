#!/usr/bin/env python3
"""Block 11 protected live-release review administration.

Commands: list, status, approve, reject, revoke.
There is deliberately no execute command. Approval does not modify live.
"""
from __future__ import annotations

import argparse
import copy
import fcntl
import json
import os
import tempfile
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

CONTROL = Path('/root/crypto-fractal-scanner')
RUNTIME = Path('/opt/crypto-fractal-scanner-vps')
REPORTS = RUNTIME / 'reports'
PLANS = REPORTS / 'paper_trading_evolution_live_release_plans.json'
APPROVALS = REPORTS / 'paper_trading_evolution_live_release_approvals.json'
CONFIG = RUNTIME / 'config/evolution_live_bridge_block11.json'
LOCK = CONTROL / 'data/evolution/live_release_admin.lock'
COMMANDS = {'list', 'status', 'approve', 'reject', 'revoke'}


def now() -> datetime:
    return datetime.now(timezone.utc)


def iso(value: datetime | None = None) -> str:
    return (value or now()).astimezone(timezone.utc).isoformat(timespec='seconds')


def read(path: Path, default: Any) -> Any:
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError):
        return copy.deepcopy(default)


def atomic(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    owner = path.stat() if path.exists() else (PLANS.stat() if PLANS.exists() else None)
    fd, temporary = tempfile.mkstemp(prefix='.' + path.name + '.', suffix='.tmp', dir=str(path.parent), text=True)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as handle:
            json.dump(value, handle, ensure_ascii=False, indent=2, sort_keys=True)
            handle.write('\n'); handle.flush(); os.fsync(handle.fileno())
        if owner is not None:
            os.chmod(temporary, owner.st_mode & 0o777)
            os.chown(temporary, owner.st_uid, owner.st_gid)
        os.replace(temporary, path)
    except Exception:
        try:
            os.unlink(temporary)
        except OSError:
            pass
        raise


def plans_doc() -> dict[str, Any]:
    value = read(PLANS, {'plans': []})
    return value if isinstance(value, dict) else {'plans': []}


def approvals_doc() -> dict[str, Any]:
    value = read(APPROVALS, {'approvals': []})
    if not isinstance(value, dict):
        value = {'approvals': []}
    value.setdefault('approvals', [])
    return value


def find_plan(plan_id: str) -> tuple[dict[str, Any], dict[str, Any]]:
    document = plans_doc()
    for row in document.get('plans', []):
        if isinstance(row, dict) and row.get('plan_id') == plan_id:
            return document, row
    raise RuntimeError(f'Unknown live-release plan: {plan_id}')


def list_plans() -> list[dict[str, Any]]:
    return [{
        'plan_id': row.get('plan_id'),
        'status': row.get('status'),
        'candidate': row.get('candidate_portfolio'),
        'change_domain': row.get('change_domain'),
        'plan_hash': row.get('plan_hash'),
        'approval_confirmation': row.get('approval_confirmation'),
        'live_execution_enabled': False,
    } for row in plans_doc().get('plans', []) if isinstance(row, dict)]


def status() -> dict[str, Any]:
    config = read(CONFIG, {})
    approvals = approvals_doc().get('approvals', [])
    return {
        'mode': 'LOCKED_REVIEW_ONLY',
        'live_adapter_configured': bool(config.get('live_adapter_configured', False)),
        'live_execution_enabled': False,
        'available_commands': sorted(COMMANDS),
        'execute_command_available': False,
        'approval_count': len(approvals),
        'live_modified': False,
        'orders_sent': False,
    }


def save_approval(row: dict[str, Any]) -> dict[str, Any]:
    document = approvals_doc()
    rows = [item for item in document['approvals'] if item.get('approval_id') != row.get('approval_id')]
    rows.append(row)
    document.update({
        'schema_version': 1,
        'engine_version': 'block11-protected-live-bridge-v1',
        'updated_utc': iso(),
        'live_execution_enabled': False,
        'live_modified': False,
        'orders_sent': False,
        'approvals': rows,
    })
    atomic(APPROVALS, document)
    return row


def approve(plan_id: str, approved_by: str, confirmation: str, when: datetime | None = None) -> dict[str, Any]:
    current = when or now()
    _, plan = find_plan(plan_id)
    if plan.get('status') != 'LIVE_REVIEW_READY':
        raise RuntimeError(f"Plan is not LIVE_REVIEW_READY: {plan.get('status')}")
    if confirmation != plan.get('approval_confirmation'):
        raise RuntimeError('Exact approval confirmation does not match')
    config = read(CONFIG, {})
    if not bool(config.get('live_adapter_configured', False)):
        raise RuntimeError('Live adapter is not configured')
    approval = {
        'schema_version': 1,
        'approval_id': 'LAPR-' + uuid.uuid4().hex[:20].upper(),
        'plan_id': plan_id,
        'plan_hash': plan.get('plan_hash'),
        'candidate_id': plan.get('candidate_id'),
        'candidate_portfolio': plan.get('candidate_portfolio'),
        'change_domain': plan.get('change_domain'),
        'approved_by': approved_by,
        'approved_utc': iso(current),
        'expires_utc': iso(current + timedelta(hours=int(config.get('approval_ttl_hours', 72)))),
        'status': 'APPROVED',
        'human_approval': True,
        'explicit_execution_still_required': True,
        'live_execution_enabled': False,
        'live_modified': False,
        'orders_sent': False,
    }
    return save_approval(approval)


def reject(plan_id: str, rejected_by: str, reason: str, confirmation: str) -> dict[str, Any]:
    _, plan = find_plan(plan_id)
    if confirmation != plan.get('reject_confirmation'):
        raise RuntimeError('Exact rejection confirmation does not match')
    row = {
        'schema_version': 1,
        'approval_id': 'LREJ-' + uuid.uuid4().hex[:20].upper(),
        'plan_id': plan_id,
        'plan_hash': plan.get('plan_hash'),
        'candidate_id': plan.get('candidate_id'),
        'rejected_by': rejected_by,
        'rejected_utc': iso(),
        'reason': reason,
        'status': 'REJECTED',
        'live_execution_enabled': False,
        'live_modified': False,
        'orders_sent': False,
    }
    return save_approval(row)


def revoke(approval_id: str, revoked_by: str, confirmation: str) -> dict[str, Any]:
    document = approvals_doc()
    for row in document.get('approvals', []):
        if row.get('approval_id') == approval_id:
            if confirmation != f'REVOKE LIVE {approval_id}':
                raise RuntimeError('Exact revoke confirmation does not match')
            row.update({
                'status': 'REVOKED', 'revoked_by': revoked_by,
                'revoked_utc': iso(), 'live_execution_enabled': False,
                'live_modified': False, 'orders_sent': False,
            })
            atomic(APPROVALS, document)
            return row
    raise RuntimeError(f'Unknown approval: {approval_id}')


def locked():
    LOCK.parent.mkdir(parents=True, exist_ok=True)
    handle = LOCK.open('a+')
    fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
    return handle


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('list')
    sub.add_parser('status')
    approve_parser = sub.add_parser('approve')
    approve_parser.add_argument('--plan-id', required=True)
    approve_parser.add_argument('--approved-by', required=True)
    approve_parser.add_argument('--confirmation', required=True)
    reject_parser = sub.add_parser('reject')
    reject_parser.add_argument('--plan-id', required=True)
    reject_parser.add_argument('--rejected-by', required=True)
    reject_parser.add_argument('--reason', required=True)
    reject_parser.add_argument('--confirmation', required=True)
    revoke_parser = sub.add_parser('revoke')
    revoke_parser.add_argument('--approval-id', required=True)
    revoke_parser.add_argument('--revoked-by', required=True)
    revoke_parser.add_argument('--confirmation', required=True)
    args = parser.parse_args()
    handle = locked()
    try:
        if args.command == 'list':
            result = list_plans()
        elif args.command == 'status':
            result = status()
        elif args.command == 'approve':
            result = approve(args.plan_id, args.approved_by, args.confirmation)
        elif args.command == 'reject':
            result = reject(args.plan_id, args.rejected_by, args.reason, args.confirmation)
        else:
            result = revoke(args.approval_id, args.revoked_by, args.confirmation)
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    except Exception as exc:
        print(f'Block 11 live-release administration failed: {exc}')
        return 2
    finally:
        handle.close()


if __name__ == '__main__':
    raise SystemExit(main())
