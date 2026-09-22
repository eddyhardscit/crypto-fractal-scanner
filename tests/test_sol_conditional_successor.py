import unittest

import numpy as np
import pandas as pd

import sol_conditional_successor as conditional


def frame(values):
    return pd.DataFrame(
        {
            "Close": values,
        },
        index=pd.date_range(
            "2020-01-01",
            periods=len(values),
            freq="D",
        ),
    )


class SolConditionalSuccessorTests(
    unittest.TestCase
):

    def test_current_model_filters_the_40_not_direct_top8(self):
        qualifying = (
            [100.0, 94.0, 111.0]
            + list(
                np.linspace(
                    111.0,
                    180.0,
                    61,
                )
            )[1:]
            + [180.0] * 10
        )

        wrong_order = (
            [100.0, 111.0, 94.0]
            + [100.0] * 70
        )

        matches = pd.DataFrame([
            {
                "similar_asset": "A-USD",
                "start_date": "2019-01-01",
                "end_date": "2020-01-01",
                "similarity": 99.0,
            },
            {
                "similar_asset": "B-USD",
                "start_date": "2019-01-01",
                "end_date": "2020-01-01",
                "similarity": 98.0,
            },
        ])

        paths = (
            conditional.build_conditioned_paths(
                matches,
                {
                    "A-USD": frame(
                        qualifying
                    ),
                    "B-USD": frame(
                        wrong_order
                    ),
                },
            )
        )

        self.assertEqual(
            len(paths),
            1,
        )

        self.assertEqual(
            paths.iloc[0][
                "similar_asset"
            ],
            "A-USD",
        )

    def test_frozen_cohort_is_8_episodes_from_6_assets(self):
        self.assertEqual(
            len(
                conditional.FROZEN_COHORT
            ),
            8,
        )

        self.assertEqual(
            len({
                item[0]
                for item
                in conditional.FROZEN_COHORT
            }),
            6,
        )

    def test_report_explains_dynamic_and_frozen_are_separate(self):
        dynamic = {
            "status": "AVAILABLE",
            "forecast_date": "2026-09-22",
            "qualified_episodes": 8,
            "distinct_assets": 6,
            "small_sample": True,
            "chart_filename": "dynamic.png",
            "q30": {
                "p10_price": 90,
                "p25_price": 100,
                "p50_price": 150,
                "p75_price": 180,
                "p90_price": 220,
            },
            "path_classes_60d": {},
            "episodes": [],
        }

        frozen = {
            "status": "AVAILABLE",
            "chart_filename": "frozen.png",
            "q30": {
                "p10_price": 90,
                "p25_price": 100,
                "p50_price": 168,
                "p75_price": 200,
                "p90_price": 250,
            },
            "actual_progress": {
                "actual_available": False,
            },
            "meta": {
                "episodes": [],
                "reproduced_medians": {
                    "7": -11.51,
                    "14": 8.85,
                    "21": 36.80,
                    "30": 49.55,
                },
            },
        }

        raw = {
            "count": 40,
            "p10_price": 79,
            "p25_price": 96,
            "p50_price": 122,
            "p75_price": 156,
            "p90_price": 204,
        }

        text = "\n".join(
            conditional.report_lines(
                dynamic,
                frozen,
                raw,
                "2026-09-22",
            )
        )

        self.assertIn(
            "40 analoghi",
            text,
        )

        self.assertIn(
            "Conditional Successor corrente",
            text,
        )

        self.assertIn(
            "Vintage originale",
            text,
        )

        self.assertIn(
            "asset possono cambiare",
            text,
        )

        self.assertIn(
            "non vengono mediati",
            text,
        )


if __name__ == "__main__":
    unittest.main()
