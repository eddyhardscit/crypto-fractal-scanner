from copy import deepcopy
from datetime import date, timedelta
from pathlib import Path
import json
import tempfile
import unittest

import matplotlib.pyplot as plt

import sol_long_term_forward_views as forward


def observation(
    day="2026-09-17",
    offset=0,
):
    row = {
        "date_local": day,
        "generated_at": f"{day}T06:00:00Z",
        "spot_sol": 100.0 + offset,
    }

    for horizon in (
        90,
        180,
        365,
        730,
    ):
        row[f"h{horizon}_p10"] = (
            60 + horizon / 20 + offset
        )

        row[f"h{horizon}_p25"] = (
            80 + horizon / 20 + offset
        )

        row[f"h{horizon}_p50"] = (
            120 + horizon / 20 + offset
        )

        row[f"h{horizon}_p75"] = (
            180 + horizon / 20 + offset
        )

        row[f"h{horizon}_p90"] = (
            250 + horizon / 20 + offset
        )

    return row


class ForwardViewsTests(unittest.TestCase):

    def test_exact_target_dates(self):
        row = observation()

        figure = (
            forward.forward_calendar_figure(
                row
            )
        )

        try:
            axis = figure.axes[0]

            lines = {
                line.get_gid(): line
                for line in axis.lines
            }

            self.assertEqual(
                set(lines),
                {
                    "forward_p10",
                    "forward_p25",
                    "forward_p50",
                    "forward_p75",
                    "forward_p90",
                },
            )

            line = lines["forward_p50"]

            expected = [
                date(
                    2026,
                    9,
                    17,
                )
                + timedelta(days=horizon)
                for horizon, _
                in forward.FORWARD_HORIZONS
            ]

            actual = list(
                line.get_xdata()
            )

            self.assertEqual(
                actual,
                expected,
            )

            self.assertEqual(
                list(line.get_ydata()),
                [
                    row[
                        f"h{horizon}_p50"
                    ]
                    for horizon, _
                    in forward.FORWARD_HORIZONS
                ],
            )

        finally:
            plt.close(figure)

    def test_render_adds_forward_graphs_and_readme(self):
        rows = [
            observation(
                "2026-09-16"
            ),
            observation(
                "2026-09-17",
                2,
            ),
        ]

        before = deepcopy(rows)

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)

            (
                root / "README.md"
            ).write_text(
                "# SOL Long-Term Cone History\n\n"
                "## Current cone\n\n"
                "existing\n\n"
                "## Forecast history\n\n"
                "existing\n",
                encoding="utf-8",
            )

            files = (
                forward.render_forward_views(
                    rows,
                    rows[-1],
                    root,
                )
            )

            self.assertEqual(
                {
                    path.name
                    for path in files
                },
                {
                    forward.CALENDAR_NAME,
                    forward.VINTAGES_NAME,
                },
            )

            for path in files:
                self.assertIn(
                    "<svg",
                    path.read_text(
                        encoding="utf-8"
                    ),
                )

            report = (
                root / "README.md"
            ).read_text()

            self.assertIn(
                "## Forward calendar",
                report,
            )

            self.assertIn(
                "## Forward vintages",
                report,
            )

            target_6m = (
                date(
                    2026,
                    9,
                    17,
                )
                + timedelta(days=180)
            ).isoformat()

            self.assertIn(
                target_6m,
                report,
            )

        self.assertEqual(
            rows,
            before,
        )


    def test_short_term_context_uses_existing_outputs_only(self):
        with tempfile.TemporaryDirectory() as temporary:
            reports = Path(temporary) / "reports"
            output = reports / "sol_long_term_history"
            output.mkdir(parents=True)

            (reports / "scanner_forecast_latest.csv").write_text(
                "snapshot_date,asset,p10_30d_price,p25_30d_price,"

                "p50_30d_price,p75_30d_price,p90_30d_price\n"

                "2026-09-24,SOL,77,93,116,142,195\n",
                encoding="utf-8",
            )

            (reports / "sol_conditional_successor_current.json").write_text(
                json.dumps({
                    "status": "AVAILABLE",
                    "forecast_date": "2026-09-24",
                    "qualified_episodes": 8,
                    "q30": {
                        "p10_price": 92,
                        "p25_price": 98,
                        "p50_price": 144,
                        "p75_price": 185,
                        "p90_price": 248,
                    },
                }),
                encoding="utf-8",
            )

            (reports / "sol_conditional_successor_vintage_20260918.json").write_text(
                json.dumps({
                    "vintage_date": "2026-09-18",
                    "qualified_episodes": 8,
                    "q30": {
                        "p10_price": 97,
                        "p25_price": 110,
                        "p50_price": 169,
                        "p75_price": 188,
                        "p90_price": 214,
                    },
                }),
                encoding="utf-8",
            )

            context = forward._load_short_term_context(output)
            block = forward._forward_readme_block(observation(), context)

            self.assertIn("## Short-term context (30 giorni)", block)
            self.assertIn("Cono standard", block)
            self.assertIn("$144.00", block)
            self.assertIn("$169.00", block)
            self.assertIn("../latest_report.md", block)


if __name__ == "__main__":
    unittest.main()
