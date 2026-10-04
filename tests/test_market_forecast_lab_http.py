"""Provider retry and pacing tests for Market Forecast Lab."""
import urllib.error
import unittest
from unittest.mock import patch

from market_forecast_lab_http import call_with_retry
from market_forecast_lab_universe import fetch_markets


class RetryTests(unittest.TestCase):
    def http_error(self, code, retry_after=None):
        headers = {} if retry_after is None else {"Retry-After": str(retry_after)}
        return urllib.error.HTTPError("https://provider.test", code, "error", headers, None)

    def test_429_retries_and_honors_retry_after(self):
        calls = []
        sleeps = []
        def operation():
            calls.append(1)
            if len(calls) == 1:
                raise self.http_error(429, 7)
            return "ok"
        self.assertEqual(call_with_retry(operation, delays=(2,), sleep=sleeps.append), "ok")
        self.assertEqual(len(calls), 2)
        self.assertEqual(sleeps, [7.0])

    def test_503_uses_bounded_backoff(self):
        calls = []
        sleeps = []
        def operation():
            calls.append(1)
            if len(calls) < 3:
                raise self.http_error(503)
            return "ok"
        self.assertEqual(call_with_retry(operation, delays=(2, 5), sleep=sleeps.append), "ok")
        self.assertEqual(sleeps, [2.0, 5.0])

    def test_non_retryable_404_fails_immediately(self):
        sleeps = []
        def operation():
            raise self.http_error(404)
        with self.assertRaises(urllib.error.HTTPError):
            call_with_retry(operation, delays=(2, 5), sleep=sleeps.append)
        self.assertEqual(sleeps, [])

    def test_yfinance_rate_limit_class_is_retryable(self):
        class YFRateLimitError(Exception):
            pass
        calls = []
        def operation():
            calls.append(1)
            if len(calls) == 1:
                raise YFRateLimitError("Too Many Requests")
            return 3
        self.assertEqual(call_with_retry(operation, delays=(0,), sleep=lambda _: None), 3)
        self.assertEqual(len(calls), 2)


class CoinGeckoPacingTests(unittest.TestCase):
    def test_full_pages_are_paced_before_next_request(self):
        cfg = {
            "market_pages": 2,
            "market_per_page": 2,
            "market_page_pacing_seconds": 1.25,
        }
        pages = [
            [
                dict(id="a", symbol="a", name="A", market_cap_rank=1),
                dict(id="b", symbol="b", name="B", market_cap_rank=2),
            ],
            [dict(id="c", symbol="c", name="C", market_cap_rank=3)],
        ]
        with patch("market_forecast_lab_universe.request_json", side_effect=pages) as request, \
             patch("market_forecast_lab_universe.time.sleep") as sleep:
            result = fetch_markets(cfg)
        self.assertEqual(request.call_count, 2)
        sleep.assert_called_once_with(1.25)
        self.assertEqual([row["id"] for row in result["rows"]], ["a", "b", "c"])


if __name__ == "__main__":
    unittest.main()
