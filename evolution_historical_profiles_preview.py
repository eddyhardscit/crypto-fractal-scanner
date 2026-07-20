#!/usr/bin/env python3
"""Preview historical Paper profiles that are absent from the current registry.

The script reads the remote permanent Paper ledgers entirely in memory and
builds a reviewable preview for legacy profiles found in runtime history but
missing from the current paper_trading_config.json / Evolution registry.

It does NOT modify the real registry, operational reports, services or orders.

Outputs:
- reports/evolution_historical_profiles_preview.json
- reports/evolution_historical_profiles_preview.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import uuid
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import evolution_runtime_snapshot as base
import evolution_runtime_snapshot_remote as remote


NAMESPACE = uuid.UUID("6f2f1e47-4adc-45fd-aada-e819b4de375d")


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def stable_uuid(profile_name: str) -> str:
    return str(
        uuid.uuid5(
            NAMESPACE,
            f"crypto-fractal-scanner:historical-profile:{profile_name}".lower(),
        )
    )


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_") or "unknown"


def short_hash(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:10]


def infer_profile(profile: str) -> dict[str, Any]:
    upper = profile.upper()

    rules = [
        (("COMBO_ADAPTIVE",), "combo_adaptive", "high"),
        (("COMBO_SCANNER",), "combo_scanner", "high"),
        (("COMBO_MEAN_REVERSION",), "combo_mean_reversion", "high"),
        (("COMBO_TREND",), "combo_trend", "high"),
        (("SCANNER_BOTTOM5",), "scanner_bottom5_short", "high"),
        (("SCANNER_TOP5",), "scanner_top5_long", "high"),
        (("GLOBAL_PURE",), "global_confluence_pure", "high"),
        (("RELATIVE_STRENGTH",), "relative_strength", "high"),
        (("DONCHIAN",), "donchian_breakout", "high"),
        (("BOLLINGER",), "bollinger_mean_reversion", "high"),
        (("EMA",), "ema_trend_following", "high"),
        (("RSI_LONG", "RSI_SHORT"), "rsi_extreme_reversal", "high"),
    ]

    engine = None
    confidence = "low"
    for tokens, candidate, level in rules:
        if any(token in upper for token in tokens):
            engine = candidate
            confidence = level
            break

    asset_scope = []
    for asset in ("BTC", "ETH", "SOL", "DOGE", "HYPE"):
        if re.search(rf"(^|_){asset}(_|$)", upper):
            asset_scope.append(asset)

    timeframe = None
    match = re.search(r"(?:^|_)(\d+)(M|H|D)(?:_|$)", upper)
    if match:
        timeframe = f"{match.group(1)}{match.group(2)}"

    direction = None
    if "SHORT" in upper:
        direction = "SHORT"
    elif "LONG" in upper:
        direction = "LONG"

    leverage = None
    lev_match = re.search(r"(?:^|_)(\d+)X(?:_|$)", upper)
    if lev_match:
        leverage = int(lev_match.group(1))

    if engine is None:
        engine = f"legacy_{slug(profile)}"

    return {
        "strategy_engine": engine,
        "family_id": engine,
        "inference_confidence": confidence,
        "asset_scope": asset_scope,
        "timeframe": timeframe,
        "direction": direction,
        "leverage": leverage,
    }


def timestamps(rows: list[dict[str, Any]]) -> tuple[str | None, str | None]:
    values = [
        base.row_timestamp(row)
        for row in rows
        if base.row_timestamp(row)
    ]
    if not values:
        return None, None
    # ISO-like timestamps sort lexicographically in the formats used by the bot.
    values = sorted(values)
    return values[0], values[-1]


def realized_pnl(rows: list[dict[str, Any]]) -> float | None:
    values: list[float] = []
    for row in rows:
        value = base.safe_float(
            base.first_present(
                row,
                (
                    "realized_pnl_eur",
                    "pnl_eur",
                    "profit_eur",
                    "net_pnl_eur",
                    "realized_pnl",
                ),
            )
        )
        if value is not None:
            values.append(value)
    return round(sum(values), 10) if values else None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    parser.add_argument(
        "--json-output",
        default="reports/evolution_historical_profiles_preview.json",
    )
    parser.add_argument(
        "--markdown-output",
        default="reports/evolution_historical_profiles_preview.md",
    )
    args = parser.parse_args()

    repo = Path(args.repo).expanduser().resolve()
    if not repo.is_dir():
        raise SystemExit(f"Repository not found: {repo}")

    os.chdir(repo)
    if str(repo) not in sys.path:
        sys.path.insert(0, str(repo))

    remote.load_service_environment(repo)
    import paper_trading_storage as storage

    client = storage.session()
    response = client.get(
        storage.api_url(f"/releases/tags/{storage.RELEASE_TAG}"),
        timeout=30,
    )
    if response.status_code >= 400:
        raise RuntimeError(
            f"Cannot read remote Paper release: HTTP {response.status_code}"
        )
    release = response.json()

    state_asset = remote.release_asset(release, storage.ASSET_NAME)
    trade_asset = remote.release_asset(release, storage.TRADE_LEDGER_ASSET_NAME)
    signal_asset = remote.release_asset(release, storage.SIGNAL_LEDGER_ASSET_NAME)

    state_zip = storage.download_asset_bytes(client, state_asset)
    trade_rows = remote.parse_csv_bytes(
        storage.download_asset_bytes(client, trade_asset)
    )
    signal_rows = remote.parse_csv_bytes(
        storage.download_asset_bytes(client, signal_asset)
    )

    paper_state, state_error = remote.zip_json(
        state_zip,
        "paper_trading_state.json",
    )
    open_rows, open_error = remote.zip_csv(
        state_zip,
        "paper_trading_open_positions.csv",
    )
    equity_rows, equity_error = remote.zip_csv(
        state_zip,
        "paper_trading_equity.csv",
    )

    registry_doc, registry_error = base.read_json(
        repo / "data/evolution/strategy_registry.json"
    )
    if registry_error:
        raise RuntimeError(f"Cannot read registry: {registry_error}")

    records = base.registry_records(registry_doc)
    registered_names = {
        str((item.get("metadata") or {}).get("legacy_profile_name") or item.get("name") or "").strip()
        for item in records
        if (item.get("metadata") or {}).get("source_kind") == "paper_portfolio"
    }

    state_by_name = base.extract_state_portfolios(paper_state)
    trades_by_name = base.group_rows_by_profile(trade_rows)
    signals_by_name = base.group_rows_by_profile(signal_rows)
    open_by_name = base.group_rows_by_profile(open_rows)
    equity_by_name = base.group_rows_by_profile(equity_rows)

    discovered = (
        set(state_by_name)
        | set(trades_by_name)
        | set(signals_by_name)
        | set(open_by_name)
        | set(equity_by_name)
    )
    historical_names = sorted(
        name for name in discovered if name and name not in registered_names
    )

    candidates: list[dict[str, Any]] = []
    for profile in historical_names:
        state = state_by_name.get(profile, {})
        trades = trades_by_name.get(profile, [])
        signals = signals_by_name.get(profile, [])
        positions = open_by_name.get(profile, [])

        state_positions = state.get("open_positions", [])
        open_count = (
            len(state_positions)
            if isinstance(state_positions, list)
            else len(positions)
        )
        if not open_count:
            open_count = len(positions)

        first_trade, last_trade = timestamps(trades)
        first_signal, last_signal = timestamps(signals)
        inference = infer_profile(profile)

        candidate = {
            "strategy_id": stable_uuid(profile),
            "family_id": inference["family_id"],
            "name": profile,
            "version": f"0.legacy.{short_hash(profile)}",
            "status": "BACKGROUND",
            "parent_id": None,
            "child_ids": [],
            "mutation": None,
            "created_by": "historical_runtime_import_preview",
            "source_kind": "historical_paper_profile",
            "source_path": "github_release_permanent_ledgers",
            "source_key": profile,
            "role": "HISTORICAL_BACKGROUND",
            "enabled": False,
            "evolution_policy": {
                "observe": True,
                "allow_mutation": False,
                "allow_automatic_promotion": False,
                "allow_live_side_effects": False,
                "require_human_review_before_reactivation": True,
            },
            "metadata": {
                "legacy_profile_name": profile,
                "strategy_engine": inference["strategy_engine"],
                "inference_confidence": inference["inference_confidence"],
                "asset_scope": inference["asset_scope"],
                "timeframe": inference["timeframe"],
                "direction": inference["direction"],
                "leverage": inference["leverage"],
                "historical_trade_rows": len(trades),
                "historical_signal_rows": len(signals),
                "historical_open_position_count": open_count,
                "historical_realized_pnl_eur": realized_pnl(trades),
                "first_trade_activity": first_trade,
                "last_trade_activity": last_trade,
                "first_signal_activity": first_signal,
                "last_signal_activity": last_signal,
                "requires_open_position_review": open_count > 0,
                "legacy_imported": True,
            },
        }
        candidates.append(candidate)

    ids = [item["strategy_id"] for item in candidates]
    existing_ids = {str(item.get("strategy_id")) for item in records}
    collisions = sorted(set(ids) & existing_ids)
    open_review = [
        item["name"]
        for item in candidates
        if item["metadata"]["requires_open_position_review"]
    ]
    low_confidence = [
        item["name"]
        for item in candidates
        if item["metadata"]["inference_confidence"] == "low"
    ]

    preview = {
        "schema_version": 1,
        "generated_at": utc_now_iso(),
        "repository": str(repo),
        "mode": "PREVIEW_ONLY",
        "safety": {
            "registry_written": False,
            "operational_files_changed": False,
            "services_restarted": False,
            "orders_sent": False,
            "remote_restore_called": False,
            "remote_upload_called": False,
        },
        "summary": {
            "historical_profile_count": len(candidates),
            "profiles_with_trade_history": sum(
                1 for item in candidates
                if item["metadata"]["historical_trade_rows"] > 0
            ),
            "profiles_with_signal_history": sum(
                1 for item in candidates
                if item["metadata"]["historical_signal_rows"] > 0
            ),
            "profiles_with_open_positions": len(open_review),
            "low_confidence_family_inferences": len(low_confidence),
            "current_registered_profile_count": len(registered_names),
        },
        "validation": {
            "valid": not collisions,
            "strategy_id_collisions": collisions,
            "profiles_requiring_open_position_review": open_review,
            "low_confidence_profiles": low_confidence,
            "source_errors": {
                key: value
                for key, value in {
                    "paper_state": state_error,
                    "open_positions": open_error,
                    "equity": equity_error,
                }.items()
                if value
            },
        },
        "historical_profiles": candidates,
        "apply_plan": {
            "next_action": (
                "Review this preview. A separate apply script may register these "
                "profiles as BACKGROUND without activating or mutating them."
            ),
            "status_rule": "All imported historical profiles start as BACKGROUND.",
            "open_position_rule": (
                "Profiles with historical open positions remain observation-only "
                "and require explicit review; no operational position is changed."
            ),
        },
    }

    lines = [
        "# Historical Paper Profiles Preview",
        "",
        f"Generated: `{preview['generated_at']}`",
        "",
        "> PREVIEW ONLY — no registry or trading file was modified.",
        "",
        "## Summary",
        "",
        f"- Historical profiles: **{len(candidates)}**",
        f"- With trade history: **{preview['summary']['profiles_with_trade_history']}**",
        f"- With signal history: **{preview['summary']['profiles_with_signal_history']}**",
        f"- With open positions requiring review: **{len(open_review)}**",
        f"- Low-confidence family inference: **{len(low_confidence)}**",
        f"- Validation: **{'OK' if preview['validation']['valid'] else 'ERROR'}**",
        "",
        "## Profiles",
        "",
        "| Name | Inferred family | Confidence | Trades | Signals | Open | Last activity |",
        "|---|---|---|---:|---:|---:|---|",
    ]
    for item in candidates:
        meta = item["metadata"]
        last_activity = meta["last_trade_activity"] or meta["last_signal_activity"]
        lines.append(
            f"| {item['name']} | {item['family_id']} | "
            f"{meta['inference_confidence']} | "
            f"{meta['historical_trade_rows']} | "
            f"{meta['historical_signal_rows']} | "
            f"{meta['historical_open_position_count']} | "
            f"{last_activity} |"
        )

    if open_review:
        lines += [
            "",
            "## Open-position review required",
            "",
        ]
        lines.extend(f"- `{name}`" for name in open_review)

    if low_confidence:
        lines += [
            "",
            "## Low-confidence family inference",
            "",
        ]
        lines.extend(f"- `{name}`" for name in low_confidence)

    json_path = repo / args.json_output
    markdown_path = repo / args.markdown_output
    base.atomic_write_json(json_path, preview)
    base.atomic_write_text(markdown_path, "\n".join(lines))

    print("=== HISTORICAL PAPER PROFILES PREVIEW ===")
    print(f"Profili storici: {len(candidates)}")
    print(
        "Con trade:",
        preview["summary"]["profiles_with_trade_history"],
    )
    print(
        "Con segnali:",
        preview["summary"]["profiles_with_signal_history"],
    )
    print(f"Con posizioni aperte da verificare: {len(open_review)}")
    print(f"Inferenze a bassa confidenza: {len(low_confidence)}")
    print(f"Collisioni ID: {len(collisions)}")
    print(f"Validazione: {'OK' if preview['validation']['valid'] else 'ERRORE'}")
    print(f"JSON: {json_path}")
    print(f"Markdown: {markdown_path}")
    print("Il registro reale NON è stato modificato.")
    print("Nessun file operativo è stato modificato.")
    print("Nessun servizio è stato riavviato.")
    return 0 if preview["validation"]["valid"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
