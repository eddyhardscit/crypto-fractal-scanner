"""Daily Telegram summary for the already-generated SOL long-term cone."""

from __future__ import annotations

import argparse
import json
import math
import os
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

from sol_long_term_history import read_daily_csv, recent_statistics


REPORT_PATH = Path("/opt/crypto-fractal-scanner-publisher/reports/sol_long_term_probability_cone.json")
HISTORY_PATH = Path("/opt/crypto-fractal-scanner-publisher/reports/sol_long_term_probability_cone_history.jsonl")
DAILY_HISTORY_PATH = Path("/opt/crypto-fractal-scanner-publisher/reports/sol_long_term_history/sol_long_term_daily_history.csv")
LONG_TERM_HISTORY_URL = "https://github.com/eddyhardscit/crypto-fractal-scanner/blob/main/reports/sol_long_term_history/README.md"
STATE_PATH = Path("/var/lib/crypto-sol-long-term-cone-telegram/state.json")
CREDENTIAL_PATH = Path(os.getenv("CREDENTIALS_DIRECTORY", "/run/credentials/crypto-sol-long-term-cone-telegram.service")) / "telegram.env"
LOCAL_ZONE = ZoneInfo("Europe/Madrid")


class SummaryError(RuntimeError):
    pass


def load_inputs() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    history = []
    for number, line in enumerate(HISTORY_PATH.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            history.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise SummaryError(f"history JSONL non valido alla riga {number}") from exc
    if report.get("role") != "DIAGNOSTIC_ONLY":
        raise SummaryError("report privo del ruolo DIAGNOSTIC_ONLY")
    for horizon in ("90", "180", "365", "730"):
        if horizon not in report.get("horizons", {}):
            raise SummaryError(f"horizon {horizon} assente")
    if not history:
        raise SummaryError("history JSONL vuoto")
    return report, history


def _number(value: Any) -> float | None:
    try:
        value = float(value)
    except (TypeError, ValueError):
        return None
    return value if math.isfinite(value) else None


def _money(value: Any) -> str:
    value = _number(value)
    return "N/D" if value is None else f"${value:,.2f}"


def _percent(value: Any, signed: bool = False) -> str:
    value = _number(value)
    if value is None:
        return "N/D"
    return f"{value:+.1f}%" if signed else f"{value:.1f}%"


def _points(value: Any) -> str:
    value = _number(value)
    return "N/D" if value is None else f"{value:+.1f} pp"


def _log_robust(report: dict[str, Any], horizon: str) -> tuple[dict[str, Any], dict[str, Any]]:
    item = report["horizons"][horizon]
    metric = item["distributions"]["LOG_ROBUST_TAIL"]["final_return"]
    probabilities = item["empirical_price_threshold_probabilities"]["LOG_ROBUST_TAIL"]
    return metric["implicit_sol_prices"], probabilities


def classify_one_year_stability(report: dict[str, Any]) -> str:
    """Classify explicit instability evidence; return N/D if inputs are absent.

    UNSTABLE requires at least two of: bootstrap p50 CI crosses zero,
    leave-one-year-out p50 range crosses zero, or similarity top-N p50 spread
    is at least 25 percentage points. One flag is CAUTION; none is STABLE.
    """
    item = report["horizons"]["365"]
    try:
        bootstrap = item["bootstrap_ci90"]["LOG_ROBUST_TAIL"]
        years = item["leave_one_year_out"]["LOG_ROBUST_TAIL"]
        sensitivity = report["similarity_sensitivity"]["365"]
        b_low, b_high = _number(bootstrap["p50_ci90_low"]), _number(bootstrap["p50_ci90_high"])
        y_low, y_high = _number(years["p50_min"]), _number(years["p50_max"])
        similarity_p50 = [_number(values["LOG_ROBUST_TAIL"]["p50"]) for values in sensitivity.values()]
    except (KeyError, TypeError):
        return "N/D"
    if None in (b_low, b_high, y_low, y_high) or any(value is None for value in similarity_p50):
        return "N/D"
    flags = [b_low < 0 < b_high, y_low < 0 < y_high, max(similarity_p50) - min(similarity_p50) >= 25.0]
    count = sum(flags)
    return "UNSTABLE" if count >= 2 else "CAUTION" if count == 1 else "STABLE"


def _previous_cohort(history: list[dict[str, Any]], current_sha: str) -> dict[str, Any] | None:
    for row in reversed(history[:-1]):
        if row.get("cohort_sha256") != current_sha:
            return row
    return None


def classify_trend(old: dict[str, Any], new: dict[str, Any]) -> tuple[str, dict[str, float | None]]:
    old_2y, new_2y = old.get("horizons", {}).get("730", {}), new.get("horizons", {}).get("730", {})
    old_p50, new_p50 = _number(old_2y.get("log_robust_p50_price")), _number(new_2y.get("log_robust_p50_price"))
    old_300, new_300 = _number(old_2y.get("p_ge_300")), _number(new_2y.get("p_ge_300"))
    old_500, new_500 = _number(old_2y.get("p_ge_500")), _number(new_2y.get("p_ge_500"))
    p50_change = ((new_p50 / old_p50) - 1.0) * 100.0 if old_p50 and new_p50 is not None else None
    p300_change = new_300 - old_300 if old_300 is not None and new_300 is not None else None
    p500_change = new_500 - old_500 if old_500 is not None and new_500 is not None else None
    changes = (p50_change, p300_change, p500_change)
    thresholds = (5.0, 3.0, 3.0)
    improving = sum(value is not None and value >= threshold for value, threshold in zip(changes, thresholds))
    worsening = sum(value is not None and value <= -threshold for value, threshold in zip(changes, thresholds))
    trend = "STRENGTHENING" if improving >= 2 else "WEAKENING" if worsening >= 2 else "STABLE"
    return trend, {"p50_change": p50_change, "p300_change": p300_change, "p500_change": p500_change}


def _daily_history_lines(daily_rows: list[dict[str, Any]]) -> list[str]:
    """Render observed forecast drift; never run the cone or infer missing days."""
    stats = recent_statistics(daily_rows)
    old, new = stats.get("trend_old") or {}, stats.get("trend_new") or {}
    lines = ["", "📈 Trend 7 giorni"]
    if old.get("date_local") and new.get("date_local"):
        lines.append(f"Osservazioni: {old['date_local']} → {new['date_local']}")
    if stats.get("short_7d", True):
        lines.append("storico <7 giorni")
    if not daily_rows:
        lines.append("Storico giornaliero non disponibile.")
    for label, field in (("6M", "h180_p50"), ("1Y", "h365_p50"), ("2Y", "h730_p50")):
        before, after = _number(old.get(field)), _number(new.get(field))
        change = (after / before - 1.0) * 100.0 if before and after is not None else None
        lines.append(f"{label} p50: {_money(before)} → {_money(after)} ({_percent(change, signed=True)})")
    for threshold in (300, 500):
        field = f"h730_p_ge_{threshold}"
        before, after = _number(old.get(field)), _number(new.get(field))
        change = after - before if before is not None and after is not None else None
        lines.append(f"2Y P≥${threshold}: {_percent(before)} → {_percent(after)} ({_points(change)})")
    lines.extend(["", "📊 Stabilità 30 giorni"])
    if stats.get("short_30d", True):
        lines.append("storico <30 giorni")
    metrics = stats.get("metrics") or {}
    p50, p300 = metrics.get("h730_p50") or {}, metrics.get("h730_p_ge_300") or {}
    lines.extend([
        "2Y p50:",
        f"mediana {_money(p50.get('median'))}",
        f"range {_money(p50.get('min'))}–{_money(p50.get('max'))}",
        "2Y P≥$300:",
        f"mediana {_percent(p300.get('median'))}",
        f"range {_percent(p300.get('min'))}–{_percent(p300.get('max'))}",
        f"FORECAST_DRIFT_STATUS={stats.get('drift_status', 'CAUTION')}",
        "DIAGNOSTIC ONLY — nessun uso operativo.",
        "", "🔗 Storico completo:", LONG_TERM_HISTORY_URL,
    ])
    return lines


def render_message(report: dict[str, Any], history: list[dict[str, Any]], state: dict[str, Any] | None = None, *, test: bool = False, now: datetime | None = None, daily_rows: list[dict[str, Any]] | None = None) -> str:
    state = state or {}
    now = now or datetime.now(timezone.utc)
    local_now = now.astimezone(LOCAL_ZONE)
    current = history[-1]
    current_sha = str(current.get("cohort_sha256", ""))
    p180, prob180 = _log_robust(report, "180")
    p365, prob365 = _log_robust(report, "365")
    p730, prob730 = _log_robust(report, "730")
    cohort = report["horizons"]["90"]
    lines = []
    if test:
        lines.extend(["🧪 TEST — SOL LONG-TERM CONE", ""])
    lines.extend([
        f"📊 SOL LONG-TERM CONE — {local_now:%d/%m/%Y}", "",
        f"SOL: {_money(report.get('current_price'))}", "",
        "6 mesi", f"p50: {_money(p180.get('p50'))}", f"p75: {_money(p180.get('p75'))}",
        f"P≥$200: {_percent(prob180.get('p_sol_ge_200'))}", f"P≥$300: {_percent(prob180.get('p_sol_ge_300'))}", "",
        "1 anno", f"p50: {_money(p365.get('p50'))}", f"P≥$300: {_percent(prob365.get('p_sol_ge_300'))}",
        f"P≥$500: {_percent(prob365.get('p_sol_ge_500'))}", f"Stabilità: {classify_one_year_stability(report)}", "",
        "2 anni", f"p50: {_money(p730.get('p50'))}", f"p75: {_money(p730.get('p75'))}", f"p90: {_money(p730.get('p90'))}",
        f"P≥$300: {_percent(prob730.get('p_sol_ge_300'))}", f"P≥$500: {_percent(prob730.get('p_sol_ge_500'))}",
        f"P≥$800: {_percent(prob730.get('p_sol_ge_800'))}", "",
        f"Cohort: {cohort.get('raw_episodes', 'N/D')} analoghi / {cohort.get('distinct_assets', 'N/D')} asset",
        f"Aggiornato: {report.get('generated_at_utc', 'N/D')}",
    ])
    old = _previous_cohort(history, current_sha)
    if old is not None:
        trend, delta = classify_trend(old, current)
        old_2y, new_2y = old["horizons"]["730"], current["horizons"]["730"]
        lines.extend(["", "Variazione ultimo cohort:",
            f"2Y p50: {_money(old_2y.get('log_robust_p50_price'))} → {_money(new_2y.get('log_robust_p50_price'))} ({_percent(delta['p50_change'], signed=True)})",
            f"P≥$300: {_percent(old_2y.get('p_ge_300'))} → {_percent(new_2y.get('p_ge_300'))} ({_points(delta['p300_change'])})",
            f"P≥$500: {_percent(old_2y.get('p_ge_500'))} → {_percent(new_2y.get('p_ge_500'))} ({_points(delta['p500_change'])})",
            f"SCENARIO_TREND={trend}"])
    if state.get("cohort_sha256") == current_sha:
        lines.extend(["", "ℹ️ Nessun nuovo cohort dall'ultimo aggiornamento."])
    lines.extend(_daily_history_lines(daily_rows or []))
    return "\n".join(lines)


def _load_env(path: Path) -> dict[str, str]:
    values = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def send_message(message: str) -> int | None:
    credentials = _load_env(CREDENTIAL_PATH)
    token, chat_id = credentials.get("TELEGRAM_BOT_TOKEN", ""), credentials.get("TELEGRAM_CHAT_ID", "")
    if not token or not chat_id or credentials.get("TELEGRAM_ENABLED", "true").lower() != "true":
        raise SummaryError("credential Telegram non configurata o disabilitata")
    payload = urllib.parse.urlencode({"chat_id": chat_id, "text": message, "disable_web_page_preview": "true"}).encode()
    request = urllib.request.Request(f"https://api.telegram.org/bot{token}/sendMessage", data=payload, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            result = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        raise SummaryError(f"Telegram HTTP {exc.code}") from None
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise SummaryError(f"invio Telegram fallito: {type(exc).__name__}") from None
    if result.get("ok") is not True:
        raise SummaryError("Telegram ha restituito ok=false")
    returned_chat = str(result.get("result", {}).get("chat", {}).get("id", ""))
    if returned_chat != str(chat_id):
        raise SummaryError("Telegram ha confermato una chat diversa")
    return result.get("result", {}).get("message_id")


def load_state() -> dict[str, Any]:
    try:
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return {}


def save_state(state: dict[str, Any]) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".state.", dir=STATE_PATH.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(state, handle, sort_keys=True)
            handle.write("\n"); handle.flush(); os.fsync(handle.fileno())
        os.chmod(temporary, 0o640)
        os.replace(temporary, STATE_PATH)
    finally:
        try: os.unlink(temporary)
        except FileNotFoundError: pass


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--test", action="store_true")
    parser.add_argument("--render-only", action="store_true")
    args = parser.parse_args()
    report, history = load_inputs()
    state = load_state()
    local_date = datetime.now(timezone.utc).astimezone(LOCAL_ZONE).date().isoformat()
    if not args.force and not args.test and state.get("last_local_date") == local_date:
        print("SKIP_ALREADY_SENT_TODAY")
        return 0
    if args.test and state.get("test_sent_at"):
        print("SKIP_TEST_ALREADY_SENT")
        return 0
    try:
        daily_rows = read_daily_csv(DAILY_HISTORY_PATH)
    except Exception:
        # Optional diagnostic history must not prevent the existing summary.
        daily_rows = []
    message = render_message(report, history, state, test=args.test, daily_rows=daily_rows)
    if args.render_only:
        print(message)
        return 0
    message_id = send_message(message)
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    if args.test:
        state.update({"test_sent_at": now, "test_message_id": message_id})
    else:
        state.update({"last_local_date": local_date, "cohort_sha256": history[-1].get("cohort_sha256"), "telegram_message_id": message_id, "sent_at_utc": now})
    save_state(state)
    print(f"TELEGRAM_SEND_OK message_id={message_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
