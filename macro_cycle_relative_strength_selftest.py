# -*- coding: utf-8 -*-
"""Offline self-test for Macro Cycle + Relative Strength upgrade."""

from __future__ import annotations

import math
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
import pandas as pd

# Offline test environment may not include yfinance. The production GitHub
# workflow installs it through the existing repository requirements.
try:
    import yfinance  # noqa: F401
except Exception:
    import types
    sys.modules["yfinance"] = types.SimpleNamespace()

import btc_macro_cycle_report as macro
import relative_strength_btc_report as relative


ROOT = Path(__file__).resolve().parent


def synthetic_ohlcv(days: int = 1800) -> pd.DataFrame:
    index = pd.date_range("2018-01-01", periods=days, freq="D")
    trend = np.exp(np.linspace(math.log(0.001), math.log(0.01), days))
    cycle = 1.0 + 0.10 * np.sin(np.linspace(0, 22, days))
    close = trend * cycle
    frame = pd.DataFrame(index=index)
    frame["Close"] = close
    frame["Open"] = close * 0.998
    frame["High"] = close * 1.02
    frame["Low"] = close * 0.98
    frame["Volume"] = 1000.0
    return frame[["Open", "High", "Low", "Close", "Volume"]]


def synthetic_btc(days: int = 3000) -> pd.DataFrame:
    index = pd.date_range("2014-09-17", periods=days, freq="D")
    t = (index - macro.GENESIS_DATE).days.to_numpy(dtype=float)
    close = 0.0000012 * np.power(t, 3.15)
    close *= np.exp(0.18 * np.sin(np.linspace(0, 20, days)))
    frame = pd.DataFrame(index=index)
    frame["Close"] = close
    frame["Open"] = close * 0.995
    frame["High"] = close * 1.025
    frame["Low"] = close * 0.975
    frame["Volume"] = 1.0
    return frame[["Open", "High", "Low", "Close", "Volume"]]


def test_relative_indicators() -> None:
    frame = relative.add_indicators(synthetic_ohlcv())
    weekly = relative.to_weekly(frame)
    highs, lows = relative.pivot_points(frame.tail(260))
    structure, score = relative.structure_label(highs, lows)
    levels = relative.support_resistance(frame, highs, lows)
    result = relative.score_pair(frame, weekly, score, levels)
    assert len(frame) == 1800
    assert not weekly.empty
    assert -8 <= result["raw_score"] <= 8
    assert result["candidate_score"] in {-1, 0, 1}
    assert isinstance(structure, str)


def test_power_law() -> None:
    frame = synthetic_btc()
    fit = macro.fit_power_law(frame)
    position = macro.current_power_position(frame, fit)
    stability = macro.fit_stability(frame)
    assert 2.0 < fit["beta"] < 4.5
    assert fit["r2_loglog"] > 0.8
    assert position["central_price"] > 0
    assert 0 <= position["residual_percentile"] <= 100
    assert stability["label"] in {"ALTA", "MEDIA", "BASSA", "NON DISPONIBILE"}


def test_cycle_angle() -> None:
    dates = pd.DatetimeIndex(["2009-01-01", "2010-01-01", "2011-01-01", "2012-01-01", "2013-01-01"])
    angles = macro.four_year_angle(dates)
    assert abs(angles[0]) < 0.02
    assert abs(angles[1] - math.pi / 2) < 0.04
    assert abs(angles[2] - math.pi) < 0.04
    assert abs(angles[3] - 3 * math.pi / 2) < 0.04
    assert abs(angles[4]) < 0.06 or abs(angles[4] - 2 * math.pi) < 0.06


def test_installer() -> None:
    with tempfile.TemporaryDirectory(prefix="macro-cycle-install-") as tmp_name:
        tmp = Path(tmp_name)
        for name in (
            "relative_strength_btc_report.py",
            "btc_macro_cycle_report.py",
            "macro_cycle_relative_strength_selftest.py",
            "apply_macro_cycle_relative_strength_upgrade.py",
        ):
            shutil.copy2(ROOT / name, tmp / name)

        compact = tmp / "compact_latest_report.py"
        compact.write_text(
            '''# -*- coding: utf-8 -*-\nSECTION_END = "<!-- COMPACT_SECTION_END:{key} -->"\nMARKER_SECTIONS = (\n    (\n        "global_confluence",\n        "<!-- GLOBAL_CONFLUENCE_START -->",\n        "<!-- GLOBAL_CONFLUENCE_END -->",\n        "Global",\n        True,\n    ),\n    (\n        "btc_sol_fractal",\n        "<!-- BTC_SOL_FRACTAL_START -->",\n        "<!-- BTC_SOL_FRACTAL_END -->",\n        "Fractal",\n        False,\n    ),\n)\n''',
            encoding="utf-8",
        )
        workflow = tmp / ".github" / "workflows" / "daily.yml"
        workflow.parent.mkdir(parents=True)
        workflow.write_text(
            '''name: Daily\non: workflow_dispatch\njobs:\n  run:\n    runs-on: ubuntu-latest\n    steps:\n      - name: Checkout\n        run: echo ok\n\n      - name: Technical\n        run: python technical_structure_report.py\n\n      - name: Global\n        run: python global_confluence_report.py\n\n      - name: Compact\n        run: python compact_latest_report.py\n''',
            encoding="utf-8",
        )
        subprocess.run([sys.executable, "apply_macro_cycle_relative_strength_upgrade.py"], cwd=tmp, check=True)
        compact_text = compact.read_text(encoding="utf-8")
        daily_text = (tmp / "prepared_macro_cycle_workflow" / "daily.yml").read_text(encoding="utf-8")
        assert "BTC_MACRO_CYCLE_START" in compact_text
        assert "RELATIVE_STRENGTH_BTC_START" in compact_text
        positions = [
            daily_text.find("python relative_strength_btc_report.py"),
            daily_text.find("python btc_macro_cycle_report.py"),
            daily_text.find("python global_confluence_report.py"),
        ]
        assert min(positions) >= 0 and positions == sorted(positions)


def main() -> int:
    test_relative_indicators()
    test_power_law()
    test_cycle_angle()
    test_installer()
    print("Macro Cycle + Relative Strength self-test: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
