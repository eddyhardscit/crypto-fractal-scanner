# -*- coding: utf-8 -*-
"""Block 11 protected live release bridge.

This is the final evolution release gate. It converts fully validated Paper
promotions into immutable live-review plans. The default and installer-forced
mode is LOCKED_REVIEW_ONLY: it cannot alter the live bot, send orders, change
positions, enable futures or execute a release.

A future live release requires:
- a human-approved Paper MASTER;
- strong Block 6 validation;
- healthy Block 8 post-promotion comparison against EX_MASTER;
- high Block 9 Evolution Score and acceptable genetic memory;
- adequate Block 10 regime evidence;
- SOL-only live evidence for the configured target profile;
- NORMAL/WATCH crash guard;
- one parameter and one change domain only;
- a separately audited live adapter;
- exact human approval and a later explicit execution step.
"""
from __future__ import annotations

import copy
import csv
import hashlib
import json
import math
import re
import statistics
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPORTS = Path('reports')
CONFIG_PATH = Path('config/evolution_live_bridge_block11.json')
CANDIDATE_STATE = REPORTS / 'paper_trading_evolution_candidate_state.json'
VALIDATIONS = REPORTS / 'paper_trading_evolution_candidate_validations.csv'
PROMOTION_STATE = REPORTS / 'paper_trading_evolution_promotion_state.json'
POST_PROMOTION = REPORTS / 'paper_trading_evolution_post_promotion_comparisons.csv'
EVOLUTION_SCORES = REPORTS / 'paper_trading_evolution_scores.csv'
GENETIC_MEMORY = REPORTS / 'paper_trading_evolution_genetic_memory.json'
REGIME_MEMORY = REPORTS / 'paper_trading_evolution_regime_memory.json'
CRASH_GUARD_STATE = REPORTS / 'paper_trading_crash_guard_state.json'
TRADE_LOG = REPORTS / 'paper_trading_trade_log.csv'
APPROVALS = REPORTS / 'paper_trading_evolution_live_release_approvals.json'

STATE = REPORTS / 'paper_trading_evolution_live_bridge_state.json'
CANDIDATES_CSV = REPORTS / 'paper_trading_evolution_live_release_candidates.csv'
PLANS = REPORTS / 'paper_trading_evolution_live_release_plans.json'
HISTORY = REPORTS / 'paper_trading_evolution_live_release_history.csv'
REPORT = REPORTS / 'paper_trading_evolution_live_release_report.md'
CONFIG_SNAPSHOT = REPORTS / 'paper_trading_evolution_live_release_config_snapshot.json'

SCHEMA_VERSION = 1
ENGINE_VERSION = 'block11-protected-live-bridge-v1'

DEFAULT_CONFIG: dict[str, Any] = {
    'schema_version': 1,
    'enabled': True,
    'mode': 'LOCKED_REVIEW_ONLY',
    'paper_only_until_explicit_release': True,
    'live_adapter_configured': False,
    'live_execution_enabled': False,
    'human_approval_required': True,
    'explicit_execution_required': True,
    'transactional_backup_required': True,
    'previous_live_version_required': True,
    'rollback_blueprint_required': True,
    'orders_allowed': False,
    'live_side_effects_allowed': False,
    'automatic_release': False,
    'automatic_strategy_switching': False,
    'automatic_position_changes': False,
    'automatic_mutation': False,
    'automatic_promotion': False,
    'automatic_retirement': False,
    'automatic_rollback': False,
    'target_profile': {
        'profile_id': 'SOL_SPOT_100_EUR',
        'asset': 'SOL',
        'quote': 'USDT',
        'spot_only': True,
        'capital_ceiling_eur': 100.0,
        'maximum_open_positions': 1,
        'entry_notional_min_eur': 10.0,
        'entry_notional_max_eur': 20.0,
        'automatic_reinvestment': False,
    },
    'minimum_validation_pairs': 200,
    'minimum_validation_score': 85.0,
    'minimum_post_promotion_pairs': 150,
    'minimum_post_promotion_days': 30,
    'minimum_post_health_score': 75.0,
    'minimum_evolution_score': 85.0,
    'allowed_evolution_grades': ['S', 'A'],
    'minimum_sol_closed_trades': 100,
    'minimum_sol_profit_factor': 1.30,
    'minimum_sol_expectancy_r': 0.10,
    'maximum_sol_drawdown_r': 4.0,
    'maximum_sol_liquidations': 0,
    'minimum_regime_trades': 30,
    'allowed_regime_memory_statuses': ['FAVOR', 'NEUTRAL'],
    'blocked_genetic_memory_statuses': ['AVOID', 'CAUTION'],
    'allowed_crash_guard_levels': ['NORMAL', 'WATCH'],
    'allowed_post_promotion_statuses': ['HEALTHY'],
    'require_single_parameter_mutation': True,
    'allowed_change_domains': ['ENTRY', 'EXIT', 'RISK'],
    'maximum_change_domains_per_release': 1,
    'plan_ttl_days': 7,
    'approval_ttl_hours': 72,
}

CANDIDATE_FIELDS = [
    'generated_utc', 'plan_id', 'candidate_id', 'candidate_portfolio',
    'family_id', 'transaction_id', 'status', 'evidence_ready',
    'adapter_configured', 'approval_status', 'change_domain',
    'validation_pairs', 'validation_score', 'post_pairs',
    'post_days', 'post_health_score', 'evolution_score',
    'evolution_grade', 'sol_closed_trades', 'sol_profit_factor',
    'sol_expectancy_r', 'sol_max_drawdown_r', 'sol_liquidations',
    'current_regime', 'regime_memory_status', 'regime_trades',
    'genetic_memory_status', 'crash_guard_level', 'reason_codes',
]
HISTORY_FIELDS = [
    'generated_utc', 'plan_id', 'candidate_id', 'previous_status',
    'current_status', 'evidence_ready', 'approval_status', 'reason_codes',
]


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso(value: datetime | None = None) -> str:
    return (value or now_utc()).astimezone(timezone.utc).isoformat(timespec='seconds')


def finite(value: Any, default: float = 0.0) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return default
    return number if math.isfinite(number) else default


def integer(value: Any, default: int = 0) -> int:
    return int(finite(value, default))


def truthy(value: Any) -> bool:
    return str(value).strip().lower() in {'1', 'true', 'yes', 'y'}


def slug(value: Any) -> str:
    text = re.sub(r'[^A-Za-z0-9]+', '-', str(value or '').strip()).strip('-').lower()
    return text or 'unknown'


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
        return json.loads(path.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError):
        return copy.deepcopy(default)


def atomic_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(text, encoding='utf-8')
    temporary.replace(path)


def atomic_json(path: Path, value: Any) -> None:
    atomic_text(path, json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + '\n')


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    try:
        with path.open('r', encoding='utf-8', newline='') as handle:
            return list(csv.DictReader(handle))
    except (OSError, csv.Error):
        return []


def write_csv(path: Path, fields: list[str], rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction='ignore')
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, '') for field in fields})


def append_csv(path: Path, fields: list[str], rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    exists = path.exists() and path.stat().st_size > 0
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction='ignore')
        if not exists:
            writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, '') for field in fields})


def parse_time(value: Any) -> datetime | None:
    text = str(value or '').strip()
    if not text:
        return None
    if text.endswith('Z'):
        text = text[:-1] + '+00:00'
    try:
        result = datetime.fromisoformat(text)
    except ValueError:
        return None
    if result.tzinfo is None:
        result = result.replace(tzinfo=timezone.utc)
    return result.astimezone(timezone.utc)


def stable_hash(value: Any) -> str:
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), default=str)
    return hashlib.sha256(raw.encode('utf-8')).hexdigest()


def load_config() -> dict[str, Any]:
    custom = load_json(CONFIG_PATH, {})
    config = deep_merge(DEFAULT_CONFIG, custom if isinstance(custom, dict) else {})
    # Hard safety locks for this initial Block 11 release.
    config['mode'] = 'LOCKED_REVIEW_ONLY'
    config['live_execution_enabled'] = False
    config['orders_allowed'] = False
    config['live_side_effects_allowed'] = False
    config['automatic_release'] = False
    config['automatic_strategy_switching'] = False
    config['automatic_position_changes'] = False
    atomic_json(CONFIG_SNAPSHOT, config)
    return config


def latest_by(rows: list[dict[str, Any]], key: str) -> dict[str, dict[str, Any]]:
    output: dict[str, dict[str, Any]] = {}
    for row in rows:
        identity = str(row.get(key, '')).strip()
        if identity:
            output[identity] = row
    return output


def executed_transactions(document: dict[str, Any]) -> list[dict[str, Any]]:
    rows = list(document.get('transactions', []) or []) if isinstance(document, dict) else []
    active = document.get('active_by_family', {}) if isinstance(document, dict) else {}
    if isinstance(active, dict):
        rows.extend(row for row in active.values() if isinstance(row, dict))
    output, seen = [], set()
    for row in rows:
        if not isinstance(row, dict) or str(row.get('status', '')).upper() != 'EXECUTED':
            continue
        key = str(row.get('transaction_id') or row.get('candidate_id') or '')
        if key and key not in seen:
            seen.add(key)
            output.append(row)
    return output


def mutation_domain(mutation: dict[str, Any]) -> str:
    parameter = str(mutation.get('parameter', '')).lower()
    if any(token in parameter for token in ('entry', 'trigger', 'signal', 'rsi', 'breakout')):
        return 'ENTRY'
    if any(token in parameter for token in ('exit', 'reward_risk', 'take_profit', 'trailing', 'holding')):
        return 'EXIT'
    if any(token in parameter for token in ('risk', 'size', 'position', 'stop', 'allocation', 'exposure')):
        return 'RISK'
    return 'UNKNOWN'


def single_parameter_mutation(candidate: dict[str, Any]) -> bool:
    mutation = candidate.get('mutation', {}) or {}
    return (
        isinstance(mutation, dict)
        and bool(str(mutation.get('parameter', '')).strip())
        and str(mutation.get('mutation_type', 'single_parameter')) == 'single_parameter'
        and not isinstance(mutation.get('parameters'), (list, tuple, dict))
    )


def profit_factor(values: list[float]) -> float:
    gains = sum(value for value in values if value > 0)
    losses = abs(sum(value for value in values if value < 0))
    return (99.0 if gains > 0 else 0.0) if losses <= 1e-12 else gains / losses


def max_drawdown(values: list[float]) -> float:
    total = peak = worst = 0.0
    for value in values:
        total += value
        peak = max(peak, total)
        worst = max(worst, peak - total)
    return worst


def sol_metrics(rows: list[dict[str, Any]], portfolio: str) -> dict[str, Any]:
    closed = []
    for row in rows:
        if str(row.get('portfolio', '')).strip() != portfolio:
            continue
        asset = str(row.get('asset') or row.get('symbol') or '').upper()
        if not (asset == 'SOL' or asset.startswith('SOL-') or asset.startswith('SOL/')):
            continue
        if not str(row.get('closed_at', '')).strip():
            continue
        closed.append(row)
    values = [finite(row.get('r_multiple')) for row in closed]
    return {
        'closed_trades': len(values),
        'expectancy_r': statistics.mean(values) if values else 0.0,
        'profit_factor': profit_factor(values),
        'max_drawdown_r': max_drawdown(values),
        'liquidations': sum(
            str(row.get('close_reason', '')).upper().startswith('LIQUIDATION')
            for row in closed
        ),
    }


def crash_level(document: dict[str, Any]) -> str:
    if not isinstance(document, dict):
        return 'UNKNOWN'
    for value in (
        document.get('level'),
        (document.get('context') or {}).get('level') if isinstance(document.get('context'), dict) else None,
        document.get('previous_level'),
        document.get('guard_level'),
    ):
        if str(value or '').strip():
            return str(value).upper()
    return 'UNKNOWN'


def genetic_record(document: dict[str, Any], candidate: dict[str, Any]) -> dict[str, Any]:
    records = document.get('records', {}) if isinstance(document, dict) else {}
    if not isinstance(records, dict):
        return {}
    family = slug(candidate.get('family_id', 'unknown'))
    mutation = candidate.get('mutation', {}) or {}
    parameter = str(mutation.get('parameter', ''))
    for record in records.values():
        if not isinstance(record, dict):
            continue
        if slug(record.get('family_id')) not in {family, 'global'}:
            continue
        if str(record.get('parameter', '')) != parameter:
            continue
        return record
    return {}


def regime_record(document: dict[str, Any], candidate: dict[str, Any]) -> tuple[str, dict[str, Any]]:
    current = str(document.get('current_regime', 'UNKNOWN')).upper() if isinstance(document, dict) else 'UNKNOWN'
    records = document.get('records', {}) if isinstance(document, dict) else {}
    key = f"{slug(candidate.get('family_id', 'unknown'))}|{current}"
    record = records.get(key, {}) if isinstance(records, dict) else {}
    return current, record if isinstance(record, dict) else {}


def approval_index(document: dict[str, Any]) -> dict[str, dict[str, Any]]:
    rows = document.get('approvals', []) if isinstance(document, dict) else []
    output = {}
    for row in rows if isinstance(rows, list) else []:
        if isinstance(row, dict) and row.get('plan_id'):
            output[str(row['plan_id'])] = row
    return output


def plan_payload(candidate: dict[str, Any], transaction: dict[str, Any], target: dict[str, Any]) -> dict[str, Any]:
    return {
        'candidate_id': candidate.get('candidate_id'),
        'candidate_portfolio': candidate.get('portfolio_name'),
        'family_id': candidate.get('family_id'),
        'transaction_id': transaction.get('transaction_id'),
        'mutation': candidate.get('mutation', {}),
        'target_profile': target,
        'single_change_domain': mutation_domain(candidate.get('mutation', {}) or {}),
    }


def evaluate_candidate(
    candidate: dict[str, Any],
    transaction: dict[str, Any],
    validation: dict[str, Any],
    post: dict[str, Any],
    score: dict[str, Any],
    genetic: dict[str, Any],
    regime_doc: dict[str, Any],
    crash_guard: dict[str, Any],
    trades: list[dict[str, Any]],
    approvals: dict[str, dict[str, Any]],
    config: dict[str, Any],
    when: datetime,
) -> dict[str, Any]:
    reasons: list[str] = []
    candidate_id = str(candidate.get('candidate_id', ''))
    portfolio = str(candidate.get('portfolio_name', ''))
    target = copy.deepcopy(config.get('target_profile', {}))
    mutation = candidate.get('mutation', {}) or {}
    domain = mutation_domain(mutation)

    if str(candidate.get('status', '')).upper() != 'MASTER':
        reasons.append('NOT_CURRENT_PAPER_MASTER')
    if not single_parameter_mutation(candidate):
        reasons.append('MUTATION_NOT_SINGLE_PARAMETER')
    if domain not in {str(value).upper() for value in config.get('allowed_change_domains', [])}:
        reasons.append('CHANGE_DOMAIN_NOT_ALLOWED')

    validation_pairs = integer(validation.get('matched_pairs'))
    validation_score = finite(validation.get('validation_score'))
    if validation_pairs < integer(config.get('minimum_validation_pairs'), 200):
        reasons.append('VALIDATION_SAMPLE_TOO_SMALL')
    if validation_score < finite(config.get('minimum_validation_score'), 85):
        reasons.append('VALIDATION_SCORE_TOO_LOW')
    if str(validation.get('status', '')).upper() != 'PROMOTION_REVIEW_READY':
        reasons.append('VALIDATION_NOT_PROMOTION_READY')

    post_pairs = integer(post.get('matched_pairs'))
    post_health = finite(post.get('health_score'))
    post_status = str(post.get('status', '')).upper()
    if post_status not in {str(value).upper() for value in config.get('allowed_post_promotion_statuses', [])}:
        reasons.append('POST_PROMOTION_NOT_HEALTHY')
    if post_pairs < integer(config.get('minimum_post_promotion_pairs'), 150):
        reasons.append('POST_PROMOTION_SAMPLE_TOO_SMALL')
    if post_health < finite(config.get('minimum_post_health_score'), 75):
        reasons.append('POST_PROMOTION_HEALTH_TOO_LOW')

    executed = parse_time(transaction.get('executed_utc'))
    post_days = (when - executed).total_seconds() / 86400 if executed else 0.0
    if post_days < finite(config.get('minimum_post_promotion_days'), 30):
        reasons.append('POST_PROMOTION_MONITORING_TOO_SHORT')

    evolution_score = finite(score.get('evolution_score'))
    evolution_grade = str(score.get('grade', '')).upper()
    if evolution_score < finite(config.get('minimum_evolution_score'), 85):
        reasons.append('EVOLUTION_SCORE_TOO_LOW')
    if evolution_grade not in {str(value).upper() for value in config.get('allowed_evolution_grades', [])}:
        reasons.append('EVOLUTION_GRADE_NOT_ALLOWED')

    sol = sol_metrics(trades, portfolio)
    if integer(sol.get('closed_trades')) < integer(config.get('minimum_sol_closed_trades'), 100):
        reasons.append('SOL_SAMPLE_TOO_SMALL')
    if finite(sol.get('profit_factor')) < finite(config.get('minimum_sol_profit_factor'), 1.30):
        reasons.append('SOL_PROFIT_FACTOR_TOO_LOW')
    if finite(sol.get('expectancy_r')) < finite(config.get('minimum_sol_expectancy_r'), 0.10):
        reasons.append('SOL_EXPECTANCY_TOO_LOW')
    if finite(sol.get('max_drawdown_r')) > finite(config.get('maximum_sol_drawdown_r'), 4.0):
        reasons.append('SOL_DRAWDOWN_TOO_HIGH')
    if integer(sol.get('liquidations')) > integer(config.get('maximum_sol_liquidations'), 0):
        reasons.append('SOL_LIQUIDATION_PRESENT')

    genetic_status = str(genetic.get('status', 'NO_HISTORY')).upper()
    if truthy(genetic.get('block_new_candidates')) or genetic_status in {
        str(value).upper() for value in config.get('blocked_genetic_memory_statuses', [])
    }:
        reasons.append('GENETIC_MEMORY_BLOCK')

    current_regime, regime = regime_record(regime_doc, candidate)
    regime_status = str(regime.get('status', 'NO_HISTORY')).upper()
    regime_trades = integer(regime.get('closed_trades'))
    if regime_status not in {str(value).upper() for value in config.get('allowed_regime_memory_statuses', [])}:
        reasons.append('REGIME_MEMORY_NOT_READY')
    if regime_trades < integer(config.get('minimum_regime_trades'), 30):
        reasons.append('REGIME_SAMPLE_TOO_SMALL')

    guard = crash_level(crash_guard)
    if guard not in {str(value).upper() for value in config.get('allowed_crash_guard_levels', [])}:
        reasons.append('CRASH_GUARD_NOT_NORMAL')

    evidence_ready = not reasons
    release_payload = plan_payload(candidate, transaction, target)
    plan_hash = stable_hash(release_payload)
    plan_id = 'LIVE-' + stable_hash({
        'candidate_id': candidate_id,
        'transaction_id': transaction.get('transaction_id'),
        'plan_hash': plan_hash,
    })[:20].upper()

    adapter = truthy(config.get('live_adapter_configured'))
    if evidence_ready and not adapter:
        status = 'EVIDENCE_READY_ADAPTER_LOCKED'
    elif evidence_ready and adapter:
        status = 'LIVE_REVIEW_READY'
    else:
        status = 'NOT_ELIGIBLE'

    approval = approvals.get(plan_id, {})
    approval_status = str(approval.get('status', 'NONE')).upper()
    if (
        status == 'LIVE_REVIEW_READY'
        and approval_status == 'APPROVED'
        and str(approval.get('plan_hash', '')) == plan_hash
        and (parse_time(approval.get('expires_utc')) or when) >= when
    ):
        status = 'APPROVED_WAITING_EXPLICIT_EXECUTION'

    return {
        'schema_version': SCHEMA_VERSION,
        'engine_version': ENGINE_VERSION,
        'generated_utc': iso(when),
        'plan_id': plan_id,
        'plan_hash': plan_hash,
        'status': status,
        'candidate_id': candidate_id,
        'candidate_portfolio': portfolio,
        'family_id': str(candidate.get('family_id', '')),
        'transaction_id': str(transaction.get('transaction_id', '')),
        'paper_promotion_executed_utc': str(transaction.get('executed_utc', '')),
        'evidence_ready': evidence_ready,
        'adapter_configured': adapter,
        'live_execution_enabled': False,
        'approval_status': approval_status,
        'approval_confirmation': f'APPROVE LIVE {plan_id} {plan_hash[:12]}',
        'reject_confirmation': f'REJECT LIVE {plan_id}',
        'change_domain': domain,
        'mutation': copy.deepcopy(mutation),
        'target_profile': target,
        'validation_pairs': validation_pairs,
        'validation_score': validation_score,
        'post_pairs': post_pairs,
        'post_days': round(post_days, 2),
        'post_health_score': post_health,
        'post_status': post_status,
        'evolution_score': evolution_score,
        'evolution_grade': evolution_grade,
        'sol_closed_trades': integer(sol.get('closed_trades')),
        'sol_profit_factor': finite(sol.get('profit_factor')),
        'sol_expectancy_r': finite(sol.get('expectancy_r')),
        'sol_max_drawdown_r': finite(sol.get('max_drawdown_r')),
        'sol_liquidations': integer(sol.get('liquidations')),
        'current_regime': current_regime,
        'regime_memory_status': regime_status,
        'regime_trades': regime_trades,
        'genetic_memory_status': genetic_status,
        'crash_guard_level': guard,
        'reason_codes': reasons,
        'human_approval_required': True,
        'explicit_execution_required': True,
        'transactional_backup_required': True,
        'previous_live_version_required': True,
        'rollback_blueprint_required': True,
        'automatic_release': False,
        'live_modified': False,
        'orders_sent': False,
        'execution_note': 'Execution is deliberately unavailable in Block 11 locked-review mode.',
    }


def render_report(plans: list[dict[str, Any]], config: dict[str, Any], when: datetime) -> str:
    ready = [row for row in plans if row.get('status') == 'LIVE_REVIEW_READY']
    adapter_locked = [row for row in plans if row.get('status') == 'EVIDENCE_READY_ADAPTER_LOCKED']
    approved = [row for row in plans if row.get('status') == 'APPROVED_WAITING_EXPLICIT_EXECUTION']
    lines = [
        '# Blocco 11 — Collegamento protetto al live', '',
        f'Generato: {iso(when)}', '',
        '> Modalità LOCKED_REVIEW_ONLY. Il blocco prepara piani immutabili, ma non può modificare il bot reale o inviare ordini.', '',
        '## Stato', '',
        f"- Promozioni Paper esaminate: **{len(plans)}**",
        f"- Pronte per revisione live: **{len(ready)}**",
        f"- Evidenza pronta ma adattatore bloccato: **{len(adapter_locked)}**",
        f"- Approvate in attesa di esecuzione esplicita: **{len(approved)}**",
        f"- Adattatore live configurato: **{'SI' if truthy(config.get('live_adapter_configured')) else 'NO'}**",
        '- Esecuzione live automatica: **NO**',
        '- Ordini inviati: **0**', '',
        '## Target iniziale', '',
        f"- Profilo: **{config.get('target_profile', {}).get('profile_id')}**",
        '- Solo SOL/USDT Spot',
        '- Capitale massimo 100 €',
        '- Una sola posizione',
        '- Ingressi 10–20 €',
        '- Nessun reinvestimento automatico', '',
        '## Piani', '',
        '| Piano | Candidata | Stato | Dominio | Validation | Post | Score | SOL trade | Regime | Crash |',
        '| --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- |',
    ]
    for row in plans:
        lines.append(
            f"| {row.get('plan_id')} | {row.get('candidate_portfolio')} | {row.get('status')} | "
            f"{row.get('change_domain')} | {finite(row.get('validation_score')):.1f} | "
            f"{finite(row.get('post_health_score')):.1f} | {finite(row.get('evolution_score')):.1f} | "
            f"{row.get('sol_closed_trades')} | {row.get('regime_memory_status')} | {row.get('crash_guard_level')} |"
        )
    if not plans:
        lines.append('| — | Nessuna promozione Paper eseguita | WAITING | — | 0 | 0 | 0 | 0 | — | — |')
    lines.extend([
        '', '## Sicurezza', '',
        '- Non vengono modificati `sol_spot_live_guarded.py`, `sol_spot_live_config.json`, `sol-live.service` o `sol-live.timer`.',
        '- Un rilascio potrà cambiare un solo parametro e un solo dominio tra ENTRY, EXIT o RISK.',
        '- Approvazione ed esecuzione sono due atti umani distinti.',
        '- Prima dell’esecuzione saranno obbligatori backup transazionale, versione precedente e piano di rollback.',
        '- L’adattatore reale resta bloccato finché non viene verificato separatamente sul codice live corrente.', '',
    ])
    text = '\n'.join(lines)
    atomic_text(REPORT, text)
    return text


def load_state() -> dict[str, Any]:
    default = {
        'schema_version': SCHEMA_VERSION,
        'engine_version': ENGINE_VERSION,
        'created_utc': iso(),
        'updated_utc': iso(),
        'plans': {},
        'cycles': 0,
    }
    value = load_json(STATE, default)
    if not isinstance(value, dict):
        value = default
    value.setdefault('plans', {})
    value.setdefault('cycles', 0)
    return value


def run_live_bridge_cycle(when: datetime | None = None) -> dict[str, Any]:
    current = when or now_utc()
    config = load_config()
    if not truthy(config.get('enabled', True)):
        return {
            'enabled': False, 'status': 'DISABLED', 'mode': 'LOCKED_REVIEW_ONLY',
            'plans': 0, 'review_ready': 0, 'adapter_locked': 0, 'approved': 0,
            'automatic_releases': 0, 'live_modified': False, 'orders_sent': False,
            'report_markdown': '',
        }

    candidate_doc = load_json(CANDIDATE_STATE, {'candidates': {}})
    candidates = candidate_doc.get('candidates', {}) if isinstance(candidate_doc, dict) else {}
    validation_index = latest_by(read_csv(VALIDATIONS), 'candidate_id')
    promotion_doc = load_json(PROMOTION_STATE, {'transactions': [], 'active_by_family': {}})
    transactions = executed_transactions(promotion_doc if isinstance(promotion_doc, dict) else {})
    post_by_candidate = latest_by(read_csv(POST_PROMOTION), 'master_candidate_id')
    post_by_transaction = latest_by(read_csv(POST_PROMOTION), 'transaction_id')
    score_index = latest_by(read_csv(EVOLUTION_SCORES), 'strategy_id')
    genetic_doc = load_json(GENETIC_MEMORY, {'records': {}})
    regime_doc = load_json(REGIME_MEMORY, {'current_regime': 'UNKNOWN', 'records': {}})
    crash_doc = load_json(CRASH_GUARD_STATE, {})
    trades = read_csv(TRADE_LOG)
    approval_doc = load_json(APPROVALS, {'approvals': []})
    approvals = approval_index(approval_doc if isinstance(approval_doc, dict) else {})

    rows: list[dict[str, Any]] = []
    for transaction in transactions:
        candidate_id = str(transaction.get('candidate_id', ''))
        candidate = candidates.get(candidate_id) if isinstance(candidates, dict) else None
        if not isinstance(candidate, dict):
            continue
        post = post_by_candidate.get(candidate_id) or post_by_transaction.get(str(transaction.get('transaction_id', ''))) or {}
        rows.append(evaluate_candidate(
            candidate, transaction, validation_index.get(candidate_id, {}), post,
            score_index.get(candidate_id, {}), genetic_record(genetic_doc, candidate),
            regime_doc if isinstance(regime_doc, dict) else {},
            crash_doc if isinstance(crash_doc, dict) else {}, trades, approvals, config, current,
        ))

    rows.sort(key=lambda row: (truthy(row.get('evidence_ready')), finite(row.get('evolution_score'))), reverse=True)
    atomic_json(PLANS, {
        'schema_version': SCHEMA_VERSION,
        'engine_version': ENGINE_VERSION,
        'generated_utc': iso(current),
        'mode': 'LOCKED_REVIEW_ONLY',
        'live_adapter_configured': False,
        'live_execution_enabled': False,
        'human_approval_required': True,
        'explicit_execution_required': True,
        'automatic_releases': 0,
        'live_modified': False,
        'orders_sent': False,
        'plans': rows,
    })
    write_csv(CANDIDATES_CSV, CANDIDATE_FIELDS, [
        {**row, 'reason_codes': ';'.join(row.get('reason_codes', []))} for row in rows
    ])

    state = load_state()
    events = []
    old_plans = state.setdefault('plans', {})
    for row in rows:
        pid = str(row.get('plan_id', ''))
        previous = old_plans.get(pid, {})
        old_status = str(previous.get('status', ''))
        new_status = str(row.get('status', ''))
        if not previous or old_status != new_status:
            events.append({
                'generated_utc': iso(current), 'plan_id': pid,
                'candidate_id': row.get('candidate_id'),
                'previous_status': old_status or 'NEW', 'current_status': new_status,
                'evidence_ready': row.get('evidence_ready'),
                'approval_status': row.get('approval_status'),
                'reason_codes': ';'.join(row.get('reason_codes', [])),
            })
        old_plans[pid] = {'status': new_status, 'updated_utc': iso(current)}
    append_csv(HISTORY, HISTORY_FIELDS, events)
    state['updated_utc'] = iso(current)
    state['cycles'] = integer(state.get('cycles')) + 1
    state['mode'] = 'LOCKED_REVIEW_ONLY'
    state['live_adapter_configured'] = False
    state['live_execution_enabled'] = False
    state['automatic_releases'] = 0
    state['live_modified'] = False
    state['orders_sent'] = False
    atomic_json(STATE, state)

    report = render_report(rows, config, current)
    return {
        'enabled': True,
        'status': 'OK',
        'mode': 'LOCKED_REVIEW_ONLY',
        'plans': len(rows),
        'review_ready': sum(row.get('status') == 'LIVE_REVIEW_READY' for row in rows),
        'adapter_locked': sum(row.get('status') == 'EVIDENCE_READY_ADAPTER_LOCKED' for row in rows),
        'approved': sum(row.get('status') == 'APPROVED_WAITING_EXPLICIT_EXECUTION' for row in rows),
        'not_eligible': sum(row.get('status') == 'NOT_ELIGIBLE' for row in rows),
        'live_adapter_configured': False,
        'live_execution_enabled': False,
        'human_approval_required': True,
        'explicit_execution_required': True,
        'rollback_blueprint_required': True,
        'automatic_releases': 0,
        'automatic_strategy_switches': 0,
        'automatic_position_changes': 0,
        'live_modified': False,
        'orders_sent': False,
        'report_markdown': report,
    }
