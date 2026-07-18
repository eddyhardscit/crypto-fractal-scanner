# -*- coding: utf-8 -*-
"""Telegram command console for the RSI 5m paper scalper.

The script is designed for GitHub Actions polling. It reads the persistent
paper/shadow state and CSV ledgers, answers commands sent to the configured
Telegram chat, stores the last processed Telegram update id inside the same
state JSON, and exits.

No KuCoin private keys are used and no real orders can be created.
"""

from __future__ import annotations

import csv
import json
import math
import os
import shlex
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable
from zoneinfo import ZoneInfo

import requests

REPORTS_DIR = Path("reports")
STATE_PATH = REPORTS_DIR / "paper_rsi5_scalper_state.json"
TRADES_PATH = REPORTS_DIR / "paper_rsi5_scalper_trades.csv"
SIGNALS_PATH = REPORTS_DIR / "paper_rsi5_scalper_signals.csv"
SHADOW_TRADES_PATH = REPORTS_DIR / "paper_rsi5_scalper_shadow_trades.csv"
CONFIG_PATH = Path(os.getenv("RSI5_SCALPER_CONFIG", "paper_rsi5_scalper_config.json"))

MAX_TELEGRAM_MESSAGE = 3900


def telegram_token() -> str:
    return (
        os.getenv("RSI5_TELEGRAM_BOT_TOKEN", "").strip()
        or os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    )


def configured_chat_id() -> str:
    return (
        os.getenv("RSI5_TELEGRAM_CHAT_ID", "").strip()
        or os.getenv("TELEGRAM_CHAT_ID", "").strip()
    )


def api_url(method: str) -> str:
    token = telegram_token()
    if not token:
        raise RuntimeError("Token Telegram non configurato")
    return f"https://api.telegram.org/bot{token}/{method}"


def telegram_call(method: str, payload: dict[str, Any]) -> Any:
    response = requests.post(api_url(method), json=payload, timeout=25)
    response.raise_for_status()
    data = response.json()
    if not data.get("ok", False):
        raise RuntimeError(f"Telegram {method}: {data}")
    return data.get("result")


def split_message(text: str, limit: int = MAX_TELEGRAM_MESSAGE) -> list[str]:
    text = text.strip()
    if len(text) <= limit:
        return [text]
    chunks: list[str] = []
    current: list[str] = []
    current_len = 0
    for line in text.splitlines():
        extra = len(line) + (1 if current else 0)
        if current and current_len + extra > limit:
            chunks.append("\n".join(current))
            current = [line]
            current_len = len(line)
        else:
            current.append(line)
            current_len += extra
    if current:
        chunks.append("\n".join(current))
    return chunks


def send_message(chat_id: str, text: str) -> None:
    for chunk in split_message(text):
        telegram_call(
            "sendMessage",
            {
                "chat_id": chat_id,
                "text": chunk,
                "disable_web_page_preview": True,
            },
        )


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def save_state(state: dict[str, Any]) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    temporary = STATE_PATH.with_suffix(".json.tmp")
    temporary.write_text(
        json.dumps(state, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    temporary.replace(STATE_PATH)


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle))
    except Exception:
        return []


def as_float(value: Any, default: float = 0.0) -> float:
    try:
        number = float(value)
    except Exception:
        return default
    return number if math.isfinite(number) else default


def as_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except Exception:
        return default


def money(value: Any, signed: bool = False) -> str:
    number = as_float(value)
    prefix = "+" if signed and number > 0 else ""
    return f"{prefix}{number:,.2f} USDT".replace(",", "_").replace(".", ",").replace("_", ".")


def decimal(value: Any, digits: int = 2) -> str:
    return f"{as_float(value):.{digits}f}".replace(".", ",")


def pct(value: Any) -> str:
    return f"{decimal(value, 2)}%"


def short_time(value: Any) -> str:
    raw = str(value or "—")
    if raw == "—":
        return raw
    try:
        stamp = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        if stamp.tzinfo is None:
            stamp = stamp.replace(tzinfo=timezone.utc)
        local = stamp.astimezone(ZoneInfo("Europe/Rome"))
        return local.strftime("%d/%m/%Y %H:%M") + " IT"
    except Exception:
        return raw


def profit_factor(gross_profit: Any, gross_loss: Any) -> str:
    profit = as_float(gross_profit)
    loss = as_float(gross_loss)
    if loss > 0:
        return f"{profit / loss:.2f}".replace(".", ",")
    return "∞" if profit > 0 else "0,00"


def account_definitions(config: dict[str, Any]) -> list[dict[str, Any]]:
    return [row for row in config.get("accounts", []) if isinstance(row, dict)]


def account_index(config: dict[str, Any]) -> dict[str, dict[str, Any]]:
    definitions = account_definitions(config)
    return {str(i): row for i, row in enumerate(definitions, start=1)}


def resolve_account(argument: str, config: dict[str, Any]) -> dict[str, Any] | None:
    needle = argument.strip().lower()
    if not needle:
        return None
    indexed = account_index(config)
    if needle in indexed:
        return indexed[needle]
    exact: list[dict[str, Any]] = []
    partial: list[dict[str, Any]] = []
    for definition in account_definitions(config):
        name = str(definition.get("name", "")).lower()
        label = str(definition.get("label", name)).lower()
        if needle in {name, label}:
            exact.append(definition)
        elif needle in name or needle in label:
            partial.append(definition)
    matches = exact or partial
    return matches[0] if len(matches) == 1 else None


def definition_number(definition: dict[str, Any], config: dict[str, Any]) -> int:
    target = str(definition.get("name", ""))
    for index, row in enumerate(account_definitions(config), start=1):
        if str(row.get("name", "")) == target:
            return index
    return 0


def strategy_text(definition: dict[str, Any], config: dict[str, Any]) -> str:
    direction = str(definition.get("direction", "LONG")).upper()
    trigger = as_float(definition.get("rsi_trigger"))
    leverage = as_float(definition.get("leverage"))
    capital = as_float(definition.get("initial_capital_usdt"))
    tp = as_float(
        definition.get("take_profit_pct", config.get("take_profit_pct"))
    ) * 100
    sl = as_float(
        definition.get("stop_loss_pct", config.get("stop_loss_pct"))
    ) * 100
    cooldown = as_int(config.get("cooldown_after_stop_bars")) * as_int(
        config.get("timeframe_minutes")
    )
    rearm = (
        as_float(config.get("long_rearm_rsi", 35.0))
        if direction == "LONG"
        else as_float(config.get("short_rearm_rsi", 65.0))
    )
    crossing = (
        f"RSI precedente > {trigger:.0f} e RSI attuale ≤ {trigger:.0f}"
        if direction == "LONG"
        else f"RSI precedente < {trigger:.0f} e RSI attuale ≥ {trigger:.0f}"
    )
    return (
        f"Strategia: {direction} RSI {trigger:.0f} su 5m\n"
        f"Ingresso: {crossing}\n"
        f"Leva paper: {leverage:.0f}× · margine massimo {money(capital)}\n"
        f"TP prezzo: {decimal(tp, 2)}% · SL prezzo: {decimal(sl, 2)}%\n"
        f"Riarmo: RSI {'≥' if direction == 'LONG' else '≤'} {rearm:.0f}\n"
        f"Cooldown dopo stop: {cooldown} minuti\n"
        "Una sola posizione operativa per conto; shadow senza limite globale."
    )


def list_accounts(config: dict[str, Any]) -> str:
    lines = [
        "📚 CONTI RSI 5M",
        "Usa il numero con /paper, /shadow, /signals, /trades o /strategy.",
        "",
    ]
    for index, definition in enumerate(account_definitions(config), start=1):
        lines.append(
            f"{index}. {definition.get('label', definition.get('name'))} "
            f"[{str(definition.get('direction', 'LONG')).upper()}]"
        )
    lines.extend(
        [
            "",
            "Esempi:",
            "/paper 5",
            "/shadow 5",
            "/signals 5",
            "/trades 5",
            "/strategy 5",
            "/why DOGE",
        ]
    )
    return "\n".join(lines)


def operational_metrics(
    definition: dict[str, Any], state: dict[str, Any]
) -> dict[str, Any]:
    name = str(definition.get("name", ""))
    account = dict(state.get("accounts", {}).get(name, {}))
    closed = as_int(account.get("closed_trades"))
    wins = as_int(account.get("winning_trades"))
    return {
        "account": account,
        "closed": closed,
        "wins": wins,
        "win_rate": wins / closed * 100 if closed else 0.0,
        "pf": profit_factor(
            account.get("gross_profit_usdt"), account.get("gross_loss_usdt")
        ),
    }


def format_paper_account(
    definition: dict[str, Any], config: dict[str, Any], state: dict[str, Any]
) -> str:
    number = definition_number(definition, config)
    metrics = operational_metrics(definition, state)
    account = metrics["account"]
    if not account:
        return f"#{number} {definition.get('label')}\nStato non ancora disponibile."
    position = account.get("open_position")
    if position:
        position_text = (
            f"APERTA: {position.get('direction')} {position.get('asset')}\n"
            f"Entrata {as_float(position.get('entry_price')):.8g} · "
            f"TP {as_float(position.get('target_price')):.8g} · "
            f"SL {as_float(position.get('stop_price')):.8g}\n"
            f"Aperta: {short_time(position.get('opened_at'))}"
        )
    else:
        position_text = "Posizione: nessuna"
    return (
        f"📘 PAPER #{number} — {definition.get('label')}\n"
        f"Saldo: {money(account.get('balance_usdt'))}\n"
        f"Trade chiusi: {metrics['closed']} · vinti: {metrics['wins']} · "
        f"WR {decimal(metrics['win_rate'], 1)}% · PF {metrics['pf']}\n"
        f"Max DD: {pct(account.get('max_drawdown_pct'))}\n"
        f"{position_text}"
    )


def format_shadow_account(
    definition: dict[str, Any], config: dict[str, Any], state: dict[str, Any]
) -> str:
    number = definition_number(definition, config)
    name = str(definition.get("name", ""))
    shadow = dict(state.get("shadow_accounts", {}).get(name, {}))
    if not shadow:
        return f"#{number} {definition.get('label')}\nShadow non ancora disponibile."
    closed = as_int(shadow.get("closed_trades"))
    wins = as_int(shadow.get("winning_trades"))
    win_rate = wins / closed * 100 if closed else 0.0
    positions = list(shadow.get("open_positions", []))
    open_assets = ", ".join(
        f"{row.get('asset')}@{as_float(row.get('entry_price')):.8g}" for row in positions[:8]
    )
    if len(positions) > 8:
        open_assets += f" … +{len(positions) - 8}"
    return (
        f"📙 SHADOW #{number} — {definition.get('label')}\n"
        f"Trade chiusi: {closed} · vinti: {wins} · WR {decimal(win_rate, 1)}%\n"
        f"PF {profit_factor(shadow.get('gross_profit_usdt'), shadow.get('gross_loss_usdt'))} · "
        f"P/L norm. {money(shadow.get('net_pnl_usdt'), signed=True)}\n"
        f"Posizioni aperte: {len(positions)}"
        + (f"\n{open_assets}" if open_assets else "")
    )


def select_definitions(argument: str, config: dict[str, Any]) -> list[dict[str, Any]]:
    needle = argument.strip().lower()
    definitions = account_definitions(config)
    if not needle or needle == "all":
        return definitions
    if needle in {"long", "short"}:
        return [
            row
            for row in definitions
            if str(row.get("direction", "LONG")).lower() == needle
        ]
    account = resolve_account(needle, config)
    return [account] if account else []


def summary_text(config: dict[str, Any], state: dict[str, Any]) -> str:
    paper_closed = 0
    paper_open = 0
    paper_pnl = 0.0
    shadow_closed = 0
    shadow_open = 0
    shadow_pnl = 0.0
    for definition in account_definitions(config):
        name = str(definition.get("name", ""))
        account = dict(state.get("accounts", {}).get(name, {}))
        shadow = dict(state.get("shadow_accounts", {}).get(name, {}))
        paper_closed += as_int(account.get("closed_trades"))
        paper_open += 1 if account.get("open_position") else 0
        paper_pnl += as_float(account.get("balance_usdt")) - as_float(
            definition.get("initial_capital_usdt")
        )
        shadow_closed += as_int(shadow.get("closed_trades"))
        shadow_open += len(shadow.get("open_positions", []))
        shadow_pnl += as_float(shadow.get("net_pnl_usdt"))
    return (
        "📊 RSI 5M — RIEPILOGO\n"
        f"Paper: {paper_open} aperte · {paper_closed} chiuse · "
        f"P/L totale {money(paper_pnl, signed=True)}\n"
        f"Shadow: {shadow_open} aperte · {shadow_closed} chiuse · "
        f"P/L norm. {money(shadow_pnl, signed=True)}\n"
        f"Ultima candela elaborata: {short_time(state.get('last_processed_candle'))}"
    )


def recent_rows(
    rows: Iterable[dict[str, str]],
    *,
    account: str | None = None,
    asset: str | None = None,
    limit: int = 8,
) -> list[dict[str, str]]:
    output: list[dict[str, str]] = []
    for row in reversed(list(rows)):
        if account and str(row.get("account", "")) != account:
            continue
        if asset and str(row.get("asset", "")).upper() != asset.upper():
            continue
        output.append(row)
        if len(output) >= limit:
            break
    return output


def format_signals(argument: str, config: dict[str, Any]) -> str:
    rows = read_csv(SIGNALS_PATH)
    account: str | None = None
    asset: str | None = None
    title = "ultimi segnali"
    if argument:
        definition = resolve_account(argument, config)
        if definition:
            account = str(definition.get("name"))
            title = str(definition.get("label"))
        else:
            asset = argument.upper()
            title = asset
    selected = recent_rows(rows, account=account, asset=asset, limit=10)
    if not selected:
        return f"🔎 SIGNALS — {title}\nNessun segnale registrato."
    lines = [f"🔎 SIGNALS — {title}"]
    for row in selected:
        lines.append(
            f"• {short_time(row.get('candle_time'))} · {row.get('asset')} · "
            f"{row.get('account_label')} · RSI {decimal(row.get('current_rsi'), 2)} · "
            f"{row.get('decision')}\n  {row.get('reason')}"
        )
    return "\n".join(lines)


def format_trades(
    argument: str,
    config: dict[str, Any],
    *,
    shadow: bool = False,
) -> str:
    definition = resolve_account(argument, config)
    if not definition:
        return "Conto non riconosciuto. Usa /list e poi, per esempio, /trades 5."
    path = SHADOW_TRADES_PATH if shadow else TRADES_PATH
    rows = recent_rows(
        read_csv(path),
        account=str(definition.get("name")),
        limit=8,
    )
    book = "SHADOW" if shadow else "PAPER"
    if not rows:
        return f"🧾 {book} — {definition.get('label')}\nNessun trade chiuso."
    lines = [f"🧾 {book} — {definition.get('label')}"]
    for row in rows:
        pnl = money(row.get("net_pnl_usdt"), signed=True)
        lines.append(
            f"• {row.get('asset')} {row.get('direction')} · {row.get('close_reason')} · "
            f"{pnl}\n  {short_time(row.get('opened_at'))} → "
            f"{short_time(row.get('closed_at'))}"
        )
    return "\n".join(lines)


def open_positions_text(config: dict[str, Any], state: dict[str, Any]) -> str:
    lines = ["📌 POSIZIONI APERTE"]
    paper_count = 0
    for index, definition in enumerate(account_definitions(config), start=1):
        name = str(definition.get("name"))
        position = state.get("accounts", {}).get(name, {}).get("open_position")
        if not position:
            continue
        paper_count += 1
        lines.append(
            f"PAPER #{index} {definition.get('label')}: "
            f"{position.get('direction')} {position.get('asset')} @ "
            f"{as_float(position.get('entry_price')):.8g}"
        )
    if not paper_count:
        lines.append("Paper: nessuna.")
    shadow_count = 0
    for index, definition in enumerate(account_definitions(config), start=1):
        name = str(definition.get("name"))
        positions = state.get("shadow_accounts", {}).get(name, {}).get("open_positions", [])
        if positions:
            shadow_count += len(positions)
            assets = ", ".join(str(row.get("asset")) for row in positions[:8])
            lines.append(f"SHADOW #{index} {definition.get('label')}: {len(positions)} ({assets})")
    if not shadow_count:
        lines.append("Shadow: nessuna.")
    return "\n".join(lines)


def help_text() -> str:
    return (
        "🤖 COMANDI RSI 5M\n"
        "/list — elenco numerato degli 8 conti\n"
        "/summary — riepilogo Paper + Shadow\n"
        "/paper [numero|all|long|short] — stato conti operativi\n"
        "/shadow [numero|all|long|short] — statistiche shadow\n"
        "/short — i quattro conti short paper\n"
        "/long — i quattro conti long paper\n"
        "/open — tutte le posizioni aperte\n"
        "/signals [numero|asset] — ultimi segnali e motivi\n"
        "/why ASSET — perché un segnale è stato aperto o saltato\n"
        "/trades NUMERO — ultimi trade paper chiusi\n"
        "/shadowtrades NUMERO — ultimi trade shadow chiusi\n"
        "/strategy NUMERO — regole del conto\n"
        "/help — questa lista\n\n"
        "Esempio: /list, poi /paper 5 oppure /why DOGE.\n"
        "Le risposte arrivano al successivo ciclo GitHub Actions, normalmente entro 5–8 minuti."
    )


def command_response(
    text: str,
    config: dict[str, Any],
    state: dict[str, Any],
) -> str:
    try:
        parts = shlex.split(text.strip())
    except ValueError:
        parts = text.strip().split()
    if not parts:
        return help_text()
    command = parts[0].split("@", 1)[0].lower()
    argument = " ".join(parts[1:]).strip()

    if command in {"/start", "/help", "/commands", "/menu"}:
        return help_text()
    if command == "/list":
        return list_accounts(config)
    if command in {"/summary", "/status", "/count"}:
        return summary_text(config, state)
    if command == "/open":
        return open_positions_text(config, state)
    if command in {"/paper", "/account"}:
        definitions = select_definitions(argument, config)
        if not definitions:
            return "Conto non riconosciuto. Usa /list."
        return "\n\n".join(format_paper_account(row, config, state) for row in definitions)
    if command == "/shadow":
        definitions = select_definitions(argument, config)
        if not definitions:
            return "Conto non riconosciuto. Usa /list."
        return "\n\n".join(format_shadow_account(row, config, state) for row in definitions)
    if command == "/short":
        definitions = select_definitions("short", config)
        return "\n\n".join(format_paper_account(row, config, state) for row in definitions)
    if command == "/long":
        definitions = select_definitions("long", config)
        return "\n\n".join(format_paper_account(row, config, state) for row in definitions)
    if command in {"/signals", "/signal", "/why"}:
        if command == "/why" and not argument:
            return "Scrivi l'asset, per esempio /why DOGE."
        return format_signals(argument, config)
    if command == "/trades":
        return format_trades(argument, config, shadow=False)
    if command == "/shadowtrades":
        return format_trades(argument, config, shadow=True)
    if command == "/strategy":
        definition = resolve_account(argument, config)
        if not definition:
            return "Conto non riconosciuto. Usa /list e poi /strategy NUMERO."
        number = definition_number(definition, config)
        return (
            f"⚙️ STRATEGIA #{number} — {definition.get('label')}\n"
            + strategy_text(definition, config)
        )
    return "Comando non riconosciuto. Usa /help."


def register_commands(state: dict[str, Any]) -> None:
    if state.get("telegram_commands_registered_v1"):
        return
    commands = [
        {"command": "list", "description": "Elenco numerato dei conti"},
        {"command": "summary", "description": "Riepilogo Paper e Shadow"},
        {"command": "count", "description": "Conta operazioni aperte e chiuse"},
        {"command": "paper", "description": "Stato conti paper"},
        {"command": "shadow", "description": "Statistiche conti shadow"},
        {"command": "short", "description": "Stato dei conti short"},
        {"command": "long", "description": "Stato dei conti long"},
        {"command": "open", "description": "Posizioni aperte"},
        {"command": "signals", "description": "Ultimi segnali e motivi"},
        {"command": "why", "description": "Controlla un asset, es. /why DOGE"},
        {"command": "trades", "description": "Ultimi trade paper di un conto"},
        {"command": "shadowtrades", "description": "Ultimi trade shadow di un conto"},
        {"command": "strategy", "description": "Regole di un conto"},
        {"command": "help", "description": "Lista completa dei comandi"},
    ]
    telegram_call("setMyCommands", {"commands": commands})
    state["telegram_commands_registered_v1"] = True


def poll_updates(state: dict[str, Any]) -> list[dict[str, Any]]:
    offset = as_int(state.get("telegram_command_offset"), 0)
    payload: dict[str, Any] = {
        "timeout": 0,
        "limit": 100,
        "allowed_updates": ["message"],
    }
    if offset > 0:
        payload["offset"] = offset
    result = telegram_call("getUpdates", payload)
    return result if isinstance(result, list) else []


def process_commands() -> dict[str, Any]:
    if not telegram_token() or not configured_chat_id():
        return {"ok": True, "configured": False, "processed": 0}
    config = load_json(CONFIG_PATH, {})
    state = load_json(STATE_PATH, {})
    if not config or not state:
        return {
            "ok": False,
            "configured": True,
            "processed": 0,
            "error": "configurazione o stato RSI5 non disponibile",
        }

    try:
        register_commands(state)
    except Exception as exc:
        print(f"Registrazione comandi Telegram non riuscita: {exc}")
    updates = poll_updates(state)
    allowed_chat = configured_chat_id()
    processed = 0
    ignored = 0
    max_update_id = as_int(state.get("telegram_command_offset"), 0) - 1

    for update in updates:
        update_id = as_int(update.get("update_id"), -1)
        max_update_id = max(max_update_id, update_id)
        message = update.get("message") or {}
        chat_id = str((message.get("chat") or {}).get("id", ""))
        text = str(message.get("text", "")).strip()
        if chat_id != allowed_chat or not text.startswith("/"):
            ignored += 1
            continue
        try:
            response = command_response(text, config, state)
            send_message(chat_id, response)
        except Exception as exc:
            try:
                send_message(chat_id, f"Errore nel comando: {exc}")
            except Exception as send_exc:
                print(f"Risposta Telegram non inviata: {send_exc}")
        processed += 1

    if max_update_id >= 0:
        state["telegram_command_offset"] = max_update_id + 1
    save_state(state)
    return {
        "ok": True,
        "configured": True,
        "processed": processed,
        "ignored": ignored,
        "updates": len(updates),
        "next_offset": state.get("telegram_command_offset", 0),
    }


def main() -> None:
    result = process_commands()
    print(json.dumps(result, ensure_ascii=False))
    if not result.get("ok", False):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
