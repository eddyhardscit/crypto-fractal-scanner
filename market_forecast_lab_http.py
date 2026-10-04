"""Bounded retry helpers for Forecast Lab provider HTTP calls."""
from __future__ import annotations

from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import json
import time
import urllib.request

RETRYABLE_HTTP_STATUS = frozenset((429, 500, 502, 503, 504))
DEFAULT_RETRY_DELAYS_SECONDS = (2.0, 5.0, 10.0, 20.0)
DEFAULT_RETRY_AFTER_CAP_SECONDS = 60.0


def status_code(exc):
    """Extract an HTTP status from urllib/requests-style exceptions."""
    if type(exc).__name__ == "YFRateLimitError":
        return 429
    for source in (exc, getattr(exc, "response", None)):
        if source is None:
            continue
        for name in ("code", "status", "status_code"):
            value = getattr(source, name, None)
            if isinstance(value, int):
                return value
    return None


def is_retryable(exc):
    return status_code(exc) in RETRYABLE_HTTP_STATUS


def _retry_after_seconds(exc, *, now=None):
    headers = getattr(exc, "headers", None)
    if headers is None and getattr(exc, "response", None) is not None:
        headers = getattr(exc.response, "headers", None)
    value = headers.get("Retry-After") if headers is not None else None
    if value is None:
        return None
    try:
        return max(0.0, float(value))
    except (TypeError, ValueError):
        pass
    try:
        when = parsedate_to_datetime(str(value))
        if when.tzinfo is None:
            when = when.replace(tzinfo=timezone.utc)
        current = now or datetime.now(timezone.utc)
        return max(0.0, (when - current).total_seconds())
    except (TypeError, ValueError, OverflowError):
        return None


def call_with_retry(call, *, delays=DEFAULT_RETRY_DELAYS_SECONDS,
                    retry_after_cap=DEFAULT_RETRY_AFTER_CAP_SECONDS,
                    sleep=time.sleep, on_retry=None):
    """Retry only throttling/server errors; all other failures remain fail-fast."""
    delays = tuple(float(value) for value in delays)
    for attempt in range(1, len(delays) + 2):
        try:
            return call()
        except Exception as exc:
            if not is_retryable(exc) or attempt > len(delays):
                raise
            retry_after = _retry_after_seconds(exc)
            delay = retry_after if retry_after is not None else delays[attempt - 1]
            delay = min(max(0.0, delay), float(retry_after_cap))
            if on_retry is not None:
                on_retry(dict(
                    attempt=attempt,
                    max_attempts=len(delays) + 1,
                    status=status_code(exc),
                    delay_seconds=delay,
                    error_type=type(exc).__name__,
                ))
            sleep(delay)


def request_json(request, *, timeout, on_retry=None):
    def load():
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.load(response)
    return call_with_retry(load, on_retry=on_retry)
