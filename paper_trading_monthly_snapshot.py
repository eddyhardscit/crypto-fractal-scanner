# -*- coding: utf-8 -*-
"""Create an immutable monthly snapshot of the paper-trading laboratory."""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPORTS_DIR = Path("reports")
SNAPSHOT_DIR = REPORTS_DIR / "paper_trading_monthly_snapshots"

STATE_PATH = REPORTS_DIR / "paper_trading_state.json"
CONFIG_PATH = Path("paper_trading_config.json")
COMPARATIVE_PATH = REPORTS_DIR / "paper_trading_comparative_latest.json"
METRICS_PATH = REPORTS_DIR / "paper_trading_shadow_metrics.csv"
TRADE_LEDGER_PATH = REPORTS_DIR / "paper_trading_trade_log.csv"
SIGNAL_LEDGER_PATH = REPORTS_DIR / "paper_trading_signal_log.csv"
SOL_STATE_PATH = REPORTS_DIR / "sol_spot_adaptive_state.json"
SOL_LATEST_PATH = REPORTS_DIR / "sol_spot_adaptive_latest.json"
SOL_CONFIG_PATH = Path("sol_spot_adaptive_config.json")


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def read_json(path: Path) -> Any:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str | None:
    if not path.exists() or not path.is_file():
        return None
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(1024 * 1024)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def csv_row_count(path: Path) -> int:
    if not path.exists() or path.stat().st_size == 0:
        return 0
    with path.open("r", encoding="utf-8-sig", errors="replace") as handle:
        lines = sum(1 for _ in handle)
    return max(0, lines - 1)


def git_value(*args: str) -> str:
    try:
        return subprocess.check_output(
            ["git", *args],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except Exception:
        return ""


def summarize_portfolios(state: dict[str, Any] | None) -> dict[str, Any]:
    if not isinstance(state, dict):
        return {
            "portfolio_count": 0,
            "open_positions": 0,
            "closed_trades": 0,
            "winning_trades": 0,
        }

    portfolios = state.get("portfolios", {})
    if not isinstance(portfolios, dict):
        portfolios = {}

    return {
        "portfolio_count": len(portfolios),
        "open_positions": sum(
            len(item.get("open_positions", []))
            for item in portfolios.values()
            if isinstance(item, dict)
        ),
        "closed_trades": sum(
            int(item.get("closed_trades", 0))
            for item in portfolios.values()
            if isinstance(item, dict)
        ),
        "winning_trades": sum(
            int(item.get("winning_trades", 0))
            for item in portfolios.values()
            if isinstance(item, dict)
        ),
    }


def build_snapshot() -> tuple[Path, dict[str, Any]]:
    current = now_utc()
    month_key = current.strftime("%Y_%m")
    output = SNAPSHOT_DIR / f"snapshot_{month_key}.json"

    paper_state = read_json(STATE_PATH)
    comparative = read_json(COMPARATIVE_PATH)
    sol_state = read_json(SOL_STATE_PATH)
    sol_latest = read_json(SOL_LATEST_PATH)

    tracked_files = [
        STATE_PATH,
        CONFIG_PATH,
        COMPARATIVE_PATH,
        METRICS_PATH,
        TRADE_LEDGER_PATH,
        SIGNAL_LEDGER_PATH,
        SOL_STATE_PATH,
        SOL_LATEST_PATH,
        SOL_CONFIG_PATH,
    ]

    snapshot = {
        "schema_version": 1,
        "snapshot_month": current.strftime("%Y-%m"),
        "generated_utc": current.isoformat(timespec="seconds"),
        "repository": {
            "name": os.getenv("GITHUB_REPOSITORY", ""),
            "commit_sha": (
                os.getenv("GITHUB_SHA", "")
                or git_value("rev-parse", "HEAD")
            ),
            "branch": (
                os.getenv("GITHUB_REF_NAME", "")
                or git_value("rev-parse", "--abbrev-ref", "HEAD")
            ),
            "git_describe": git_value(
                "describe",
                "--always",
                "--dirty",
                "--tags",
            ),
        },
        "paper_trading": {
            "summary": summarize_portfolios(paper_state),
            "state": paper_state,
            "configuration": read_json(CONFIG_PATH),
            "comparative_latest": comparative,
            "trade_rows": csv_row_count(TRADE_LEDGER_PATH),
            "signal_rows": csv_row_count(SIGNAL_LEDGER_PATH),
        },
        "sol_spot_adaptive": {
            "state": sol_state,
            "latest": sol_latest,
            "configuration": read_json(SOL_CONFIG_PATH),
        },
        "integrity": {
            str(path): {
                "exists": path.exists(),
                "size_bytes": (
                    path.stat().st_size
                    if path.exists() and path.is_file()
                    else 0
                ),
                "sha256": file_sha256(path),
            }
            for path in tracked_files
        },
    }

    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)

    # One immutable snapshot per month. Manual reruns in the same month
    # reproduce the same path and refresh it only before the commit.
    output.write_text(
        json.dumps(
            snapshot,
            ensure_ascii=False,
            indent=2,
            allow_nan=False,
        ) + "\n",
        encoding="utf-8",
    )
    return output, snapshot


def main() -> None:
    output, snapshot = build_snapshot()
    summary = snapshot["paper_trading"]["summary"]
    print(
        json.dumps(
            {
                "status": "PASS",
                "snapshot": str(output),
                "month": snapshot["snapshot_month"],
                "portfolio_count": summary["portfolio_count"],
                "closed_trades": summary["closed_trades"],
                "trade_rows": snapshot["paper_trading"]["trade_rows"],
                "signal_rows": snapshot["paper_trading"]["signal_rows"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
