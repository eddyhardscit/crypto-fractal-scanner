# -*- coding: utf-8 -*-
"""Block 7 human-approved Paper promotion governance.

This module only generates and monitors immutable promotion plans from Block 6
PROMOTION_REVIEW_READY evidence. It never approves, executes, rolls back,
promotes, retires, changes live configuration or sends orders.

Explicit approval and execution are provided by the separate control-side CLI.
"""
from __future__ import annotations

import copy
import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

REPORTS_DIR = Path('reports')
CONFIG_PATH = Path('config/evolution_promotion_block7.json')
REVIEW_PATH = REPORTS_DIR / 'paper_trading_evolution_promotion_review.json'
CANDIDATE_STATE_PATH = REPORTS_DIR / 'paper_trading_evolution_candidate_state.json'
PROMOTION_STATE_PATH = REPORTS_DIR / 'paper_trading_evolution_promotion_state.json'
GOVERNANCE_STATE_PATH = REPORTS_DIR / 'paper_trading_evolution_promotion_governance_state.json'
PLANS_PATH = REPORTS_DIR / 'paper_trading_evolution_promotion_plans.json'
EVENTS_PATH = REPORTS_DIR / 'paper_trading_evolution_promotion_events.csv'
REPORT_PATH = REPORTS_DIR / 'paper_trading_evolution_promotion_report.md'
CONFIG_SNAPSHOT_PATH = REPORTS_DIR / 'paper_trading_evolution_promotion_config_snapshot.json'

SCHEMA_VERSION = 1
ENGINE_VERSION = 'block7-human-approved-promotion-v1'

EVENT_FIELDS = [
    'generated_utc', 'event_type', 'plan_id', 'candidate_id',
    'candidate_portfolio', 'parent_id', 'parent_portfolio', 'family_id',
    'old_status', 'new_status', 'review_hash', 'transaction_id',
    'approved_by', 'reason',
]

DEFAULT_CONFIG: dict[str, Any] = {
    'schema_version': 1,
    'enabled': True,
    'paper_only': True,
    'automatic_plan_generation': True,
    'human_approval_required': True,
    'explicit_execute_required': True,
    'automatic_promotion': False,
    'automatic_retirement': False,
    'automatic_rollback': False,
    'live_side_effects_allowed': False,
    'orders_allowed': False,
    'approval_ttl_hours': 72,
    'plan_ttl_hours': 168,
    'rollback_window_days': 30,
    'require_flat_parent_and_candidate': True,
    'retain_ex_master_active': True,
    'maximum_active_master_per_family': 1,
}


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso_utc(value: datetime | None = None) -> str:
    return (value or now_utc()).astimezone(timezone.utc).isoformat(timespec='seconds')


def deep_merge(base: dict[str, Any], custom: dict[str, Any]) -> dict[str, Any]:
    output = copy.deepcopy(base)
    for key, value in custom.items():
        if isinstance(value, dict) and isinstance(output.get(key), dict):
            output[key] = deep_merge(output[key], value)
        else:
            output[key] = copy.deepcopy(value)
    return output


def load_json(path: Path, default: Any) -> Any:
    try:
        value = json.loads(path.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError):
        return copy.deepcopy(default)
    return value


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(text, encoding='utf-8')
    temporary.replace(path)


def atomic_write_json(path: Path, value: Any) -> None:
    atomic_write_text(path, json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + '\n')


def append_csv(path: Path, fields: list[str], rows: Iterable[dict[str, Any]]) -> None:
    values = list(rows)
    if not values:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    exists = path.exists() and path.stat().st_size > 0
    with path.open('a', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction='ignore')
        if not exists:
            writer.writeheader()
        for row in values:
            writer.writerow({field: row.get(field, '') for field in fields})


def stable_hash(value: Any) -> str:
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), default=str)
    return hashlib.sha256(raw.encode('utf-8')).hexdigest()


def review_payload(row: dict[str, Any]) -> dict[str, Any]:
    excluded = {'generated_utc', 'decision_summary'}
    return {key: value for key, value in row.items() if key not in excluded}


def review_hash(row: dict[str, Any]) -> str:
    return stable_hash(review_payload(row))


def plan_id(candidate_id: str, digest: str) -> str:
    return 'PROMO-' + stable_hash({'candidate_id': candidate_id, 'review_hash': digest})[:20].upper()


def empty_promotion_state() -> dict[str, Any]:
    return {
        'schema_version': SCHEMA_VERSION,
        'engine_version': ENGINE_VERSION,
        'updated_utc': iso_utc(),
        'active_by_family': {},
        'transactions': [],
        'automatic_promotions': 0,
        'automatic_rollbacks': 0,
        'live_modified': False,
        'orders_sent': False,
    }


def load_config() -> dict[str, Any]:
    custom = load_json(CONFIG_PATH, {})
    config = deep_merge(DEFAULT_CONFIG, custom if isinstance(custom, dict) else {})
    atomic_write_json(CONFIG_SNAPSHOT_PATH, config)
    return config


def make_plan(review: dict[str, Any], candidate: dict[str, Any], when: datetime) -> dict[str, Any]:
    digest = review_hash(review)
    candidate_id = str(review.get('candidate_id') or candidate.get('candidate_id') or '')
    parent_id = str(candidate.get('parent_id') or '')
    pid = plan_id(candidate_id, digest)
    return {
        'schema_version': SCHEMA_VERSION,
        'engine_version': ENGINE_VERSION,
        'plan_id': pid,
        'status': 'PENDING_APPROVAL',
        'created_utc': iso_utc(when),
        'updated_utc': iso_utc(when),
        'candidate_id': candidate_id,
        'candidate_portfolio': str(candidate.get('portfolio_name') or review.get('candidate_portfolio') or ''),
        'parent_id': parent_id,
        'parent_portfolio': str(candidate.get('parent_portfolio') or review.get('parent_portfolio') or ''),
        'family_id': str(candidate.get('family_id') or ''),
        'mutation': copy.deepcopy(candidate.get('mutation') or {}),
        'review_hash': digest,
        'review_snapshot': review_payload(review),
        'human_approval_required': True,
        'explicit_execute_required': True,
        'approval_confirmation': f'APPROVE {pid} {candidate_id}',
        'execute_confirmation': f'EXECUTE {pid} {digest[:12]}',
        'rollback_confirmation_template': 'ROLLBACK <transaction_id>',
        'automatic_promotion': False,
        'automatic_retirement': False,
        'automatic_rollback': False,
        'live_modified': False,
        'orders_sent': False,
    }


def generate_plans(when: datetime | None = None) -> dict[str, Any]:
    current = when or now_utc()
    config = load_config()
    review_doc = load_json(REVIEW_PATH, {'candidates': []})
    candidate_doc = load_json(CANDIDATE_STATE_PATH, {'candidates': {}})
    previous = load_json(PLANS_PATH, {'plans': []})
    previous_rows = [row for row in previous.get('plans', []) if isinstance(row, dict)] if isinstance(previous, dict) else []
    previous_by_id = {str(row.get('plan_id')): row for row in previous_rows}
    candidates = candidate_doc.get('candidates', {}) if isinstance(candidate_doc, dict) else {}
    reviews = review_doc.get('candidates', []) if isinstance(review_doc, dict) else []
    reviews = [row for row in reviews if isinstance(row, dict) and row.get('status') == 'PROMOTION_REVIEW_READY']
    current_plans: list[dict[str, Any]] = []
    new_events: list[dict[str, Any]] = []
    active_candidate_ids = set()

    for review in reviews:
        cid = str(review.get('candidate_id', ''))
        candidate = candidates.get(cid) if isinstance(candidates, dict) else None
        if not isinstance(candidate, dict):
            continue
        if not candidate.get('active', True) or str(candidate.get('status', 'CANDIDATE')) != 'CANDIDATE':
            continue
        fresh = make_plan(review, candidate, current)
        active_candidate_ids.add(cid)
        existing = previous_by_id.get(fresh['plan_id'])
        if existing:
            preserved = copy.deepcopy(existing)
            preserved.update({
                'updated_utc': iso_utc(current),
                'review_snapshot': fresh['review_snapshot'],
                'approval_confirmation': fresh['approval_confirmation'],
                'execute_confirmation': fresh['execute_confirmation'],
            })
            fresh = preserved
        else:
            new_events.append({
                'generated_utc': iso_utc(current), 'event_type': 'PROMOTION_PLAN_CREATED',
                'plan_id': fresh['plan_id'], 'candidate_id': cid,
                'candidate_portfolio': fresh['candidate_portfolio'], 'parent_id': fresh['parent_id'],
                'parent_portfolio': fresh['parent_portfolio'], 'family_id': fresh['family_id'],
                'old_status': '', 'new_status': 'PENDING_APPROVAL', 'review_hash': fresh['review_hash'],
                'transaction_id': '', 'approved_by': '', 'reason': 'Block 6 review ready',
            })
        current_plans.append(fresh)

    current_ids = {str(row.get('plan_id')) for row in current_plans}
    for old in previous_rows:
        if str(old.get('plan_id')) in current_ids:
            continue
        stale = copy.deepcopy(old)
        if stale.get('status') in {'PENDING_APPROVAL', 'APPROVED'}:
            stale['status'] = 'STALE'
            stale['updated_utc'] = iso_utc(current)
            stale['stale_reason'] = 'Candidate no longer review-ready or review hash changed.'
            new_events.append({
                'generated_utc': iso_utc(current), 'event_type': 'PROMOTION_PLAN_STALE',
                'plan_id': stale.get('plan_id'), 'candidate_id': stale.get('candidate_id'),
                'candidate_portfolio': stale.get('candidate_portfolio'), 'parent_id': stale.get('parent_id'),
                'parent_portfolio': stale.get('parent_portfolio'), 'family_id': stale.get('family_id'),
                'old_status': old.get('status'), 'new_status': 'STALE', 'review_hash': stale.get('review_hash'),
                'transaction_id': '', 'approved_by': '', 'reason': stale['stale_reason'],
            })
        current_plans.append(stale)

    current_plans.sort(key=lambda row: (str(row.get('created_utc', '')), str(row.get('plan_id', ''))))
    payload = {
        'schema_version': SCHEMA_VERSION,
        'engine_version': ENGINE_VERSION,
        'generated_utc': iso_utc(current),
        'paper_only': True,
        'human_approval_required': True,
        'automatic_promotions': 0,
        'automatic_retirements': 0,
        'automatic_rollbacks': 0,
        'live_modified': False,
        'orders_sent': False,
        'plan_count': len(current_plans),
        'pending_approval': sum(row.get('status') == 'PENDING_APPROVAL' for row in current_plans),
        'approved_waiting_execute': sum(row.get('status') == 'APPROVED' for row in current_plans),
        'executed': sum(row.get('status') == 'EXECUTED' for row in current_plans),
        'plans': current_plans,
    }
    atomic_write_json(PLANS_PATH, payload)
    append_csv(EVENTS_PATH, EVENT_FIELDS, new_events)
    return payload


def load_role_state() -> dict[str, Any]:
    value = load_json(PROMOTION_STATE_PATH, empty_promotion_state())
    return value if isinstance(value, dict) else empty_promotion_state()


def apply_runtime_roles(base_config: dict[str, Any], candidate_state: dict[str, Any]) -> tuple[dict[str, Any], dict[str, int]]:
    output = copy.deepcopy(base_config)
    promotion_state = load_role_state()
    active = promotion_state.get('active_by_family', {}) if isinstance(promotion_state, dict) else {}
    candidates = candidate_state.get('candidates', {}) if isinstance(candidate_state, dict) else {}
    master_candidate_ids = set()
    parent_portfolios = set()
    for row in active.values() if isinstance(active, dict) else []:
        if not isinstance(row, dict) or row.get('status') != 'EXECUTED':
            continue
        master_candidate_ids.add(str(row.get('candidate_id', '')))
        parent_portfolios.add(str(row.get('parent_portfolio', '')))

    candidate_name_by_id = {
        str(row.get('candidate_id')): str(row.get('portfolio_name'))
        for row in candidates.values() if isinstance(row, dict)
    }
    master_names = {candidate_name_by_id[cid] for cid in master_candidate_ids if cid in candidate_name_by_id}
    counts = {'masters': 0, 'ex_masters': 0}
    for portfolio in output.get('portfolios', []):
        if not isinstance(portfolio, dict):
            continue
        name = str(portfolio.get('name', ''))
        if name in parent_portfolios:
            portfolio['is_main'] = False
            portfolio['compact_shadow'] = True
            portfolio['evolution_status'] = 'EX_MASTER'
            portfolio['evolution_role_source'] = ENGINE_VERSION
            counts['ex_masters'] += 1
        elif name in master_names:
            portfolio['is_main'] = True
            portfolio['compact_shadow'] = False
            portfolio['evolution_status'] = 'MASTER'
            portfolio['evolution_role_source'] = ENGINE_VERSION
            counts['masters'] += 1
    return output, counts


def render_report(plans: dict[str, Any], when: datetime) -> str:
    promotion_state = load_role_state()
    active = promotion_state.get('active_by_family', {}) if isinstance(promotion_state, dict) else {}
    lines = [
        '# Blocco 7 — Governance promozioni Paper', '', f'Generato: {iso_utc(when)}', '',
        '> Nessuna promozione automatica. Approvazione umana e comando di esecuzione separato sono obbligatori.', '',
        '## Stato', '',
        f"- Piani totali: **{plans.get('plan_count', 0)}**",
        f"- In attesa di approvazione: **{plans.get('pending_approval', 0)}**",
        f"- Approvati ma non eseguiti: **{plans.get('approved_waiting_execute', 0)}**",
        f"- Promozioni Paper attive: **{len(active) if isinstance(active, dict) else 0}**",
        '- Promozioni automatiche: **0**', '- Rollback automatici: **0**', '',
        '## Piani', '',
        '| Piano | Candidata | Genitore | Stato | Review hash |',
        '| --- | --- | --- | --- | --- |',
    ]
    for row in plans.get('plans', []):
        lines.append(f"| {row.get('plan_id')} | {row.get('candidate_portfolio')} | {row.get('parent_portfolio')} | {row.get('status')} | `{str(row.get('review_hash', ''))[:12]}` |")
    if not plans.get('plans'):
        lines.append('| — | — | — | Nessun piano | — |')
    lines += ['', '## Sicurezza', '',
              '- Il piano è legato all’hash esatto della valutazione Block 6.',
              '- Approvazione e esecuzione sono due azioni manuali distinte.',
              '- Prima della promozione candidata e genitore devono essere senza posizioni aperte.',
              '- Il genitore diventa `EX_MASTER` ma resta attivo in Paper.',
              '- Ogni transazione ha backup e rollback esplicito.', '']
    text = '\n'.join(lines)
    atomic_write_text(REPORT_PATH, text)
    return text


def run_promotion_governance_cycle(when: datetime | None = None) -> dict[str, Any]:
    current = when or now_utc()
    config = load_config()
    if not config.get('enabled', True):
        return {'enabled': False, 'status': 'DISABLED', 'plans': 0, 'pending_approval': 0,
                'approved_waiting_execute': 0, 'active_promotions': 0,
                'automatic_promotions': 0, 'automatic_rollbacks': 0, 'report_markdown': ''}
    plans = generate_plans(current)
    promotion_state = load_role_state()
    active = promotion_state.get('active_by_family', {}) if isinstance(promotion_state, dict) else {}
    governance = {
        'schema_version': SCHEMA_VERSION, 'engine_version': ENGINE_VERSION,
        'updated_utc': iso_utc(current), 'status': 'OK',
        'plans': plans.get('plan_count', 0), 'pending_approval': plans.get('pending_approval', 0),
        'approved_waiting_execute': plans.get('approved_waiting_execute', 0),
        'active_promotions': len(active) if isinstance(active, dict) else 0,
        'human_approval_required': True, 'explicit_execute_required': True,
        'automatic_promotions': 0, 'automatic_retirements': 0, 'automatic_rollbacks': 0,
        'candidate_state_modified': False, 'parent_state_modified': False,
        'live_modified': False, 'orders_sent': False,
    }
    atomic_write_json(GOVERNANCE_STATE_PATH, governance)
    governance['report_markdown'] = render_report(plans, current)
    return governance
