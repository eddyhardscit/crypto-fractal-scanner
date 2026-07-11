# -*- coding: utf-8 -*-
"""Decide whether the GitHub-hosted KuCoin fallback collector should run.

If a validated external collector published a sufficiently fresh full snapshot,
the GitHub fallback skips collection so it does not overwrite the full state.
When the external state becomes stale or incomplete, the KuCoin fallback resumes.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path

SNAPSHOT_PATH = Path("reports/exchange_market_data_snapshot.json")
HEALTH_PATH = Path("reports/exchange_market_data_health.json")


def parse_time(value: str) -> datetime | None:
    try:
        parsed = datetime.fromisoformat((value or "").replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def read_json(path: Path) -> dict:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        return payload if isinstance(payload, dict) else {}
    except Exception:
        return {}


def main() -> None:
    snapshot = read_json(SNAPSHOT_PATH)
    health = read_json(HEALTH_PATH)
    mode = str(snapshot.get("collector_mode") or health.get("collector_mode") or "")
    generated = parse_time(str(snapshot.get("generated_utc") or health.get("generated_utc") or ""))
    available = int(health.get("available_exchange_asset_pairs") or 0)
    max_age_minutes = int(os.getenv("EXTERNAL_COLLECTOR_FRESH_MINUTES", "90"))
    age_minutes = None
    if generated is not None:
        age_minutes = max(0.0, (datetime.now(timezone.utc) - generated).total_seconds() / 60.0)

    external_fresh = (
        mode.startswith("external-")
        and available >= int(os.getenv("EXTERNAL_MIN_AVAILABLE_PAIRS", "6"))
        and age_minutes is not None
        and age_minutes <= max_age_minutes
    )
    run_fallback = not external_fresh
    reason = (
        f"external state fresh ({age_minutes:.1f} min, {available}/9 pairs)"
        if external_fresh
        else f"fallback required (mode={mode or 'missing'}, age={age_minutes}, pairs={available}/9)"
    )

    output_path = os.getenv("GITHUB_OUTPUT", "").strip()
    lines = [f"run_fallback={'true' if run_fallback else 'false'}", f"reason={reason}"]
    if output_path:
        with Path(output_path).open("a", encoding="utf-8") as handle:
            handle.write("\n".join(lines) + "\n")
    print("; ".join(lines))


if __name__ == "__main__":
    main()
