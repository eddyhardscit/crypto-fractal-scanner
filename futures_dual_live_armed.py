#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Futures Triple Live: executor KuCoin armato e protetto.

Strategie autorizzate:
- SHADOW_SCANNER_TOP5_BTC (2x isolated, rischio fisso);
- SHADOW_SCANNER_TOP5_LONG (2x isolated, rischio fisso);
- RSI5_RSI25_5X_WIDE (solo LONG, 5x isolated, max 500 USDT margine).

Capitale e rischio:
- capitale operativo fisso configurato, senza reinvestimento degli utili;
- massimo due posizioni per strategia e sei posizioni totali;
- vietate posizioni duplicate o opposte sullo stesso asset;
- protezione globale trailing: nuove aperture bloccate dopo 260 USDT
  di discesa dal massimo equity, con soglia minima iniziale 3.500 USDT;
- la RSI viene bloccata da sola dopo 3 perdite consecutive se il suo
  PnL realizzato cumulativo live è negativo.

Le posizioni già aperte restano gestite da stop, target e chiusura
della sorgente anche quando le nuove aperture vengono bloccate.
Prima di ogni nuova apertura il simbolo viene letto, eventualmente
spostato su ISOLATED e verificato; solo dopo viene inviato l'ordine.
I segnali non aperti vengono conservati come simulazioni ombra: quando
la sorgente chiude il trade, Telegram comunica se il trade teorico live
sarebbe terminato positivo o negativo e il relativo PnL stimato.

Questo programma può inviare ordini Futures.
Non contiene endpoint di trasferimento o prelievo.
"""

from __future__ import annotations

import argparse
import base64
import csv
import fcntl
import hashlib
import hmac
import json
import math
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation, ROUND_DOWN, ROUND_UP
from pathlib import Path
from typing import Any

DEFAULT_CONFIG = Path("futures_dual_live_config.json")
FUTURES_BASE = "https://api-futures.kucoin.com"

ACCOUNT_EP = "/api/v1/account-overview?currency=USDT"
POSITIONS_EP = "/api/v1/positions?currency=USDT"
POSITION_MODE_EP = "/api/v2/position/getPositionMode"
CONTRACTS_EP = "/api/v1/contracts/active"
TPSL_EP = "/api/v1/st-orders"
ORDER_EP = "/api/v1/orders"
ORDER_BY_CLIENT_EP = "/api/v1/orders/byClientOid"
STOP_ORDERS_EP = "/api/v1/stopOrders"
HISTORY_POSITIONS_EP = "/api/v1/history-positions"
MARGIN_MODE_GET_EP = "/api/v2/position/getMarginMode"
MARGIN_MODE_CHANGE_EP = "/api/v2/position/changeMarginMode"

STRATEGIES = {
    "SHADOW_SCANNER_TOP5_BTC": {
        "label": "Scanner Top 5 + forza BTC 1H",
        "allow_long": True,
        "allow_short": False,
        "leverage": 2.0,
        "sizing_mode": "FIXED_MARGIN",
        "max_margin_usdt": 150.0,
        "fixed_stop_pct": 0.05,
        "fixed_target_pct": 0.20,
        "max_open_positions": 0,
    },
    "SHADOW_SCANNER_TOP5_LONG": {
        "label": "Scanner Top 5 Long 1H",
        "allow_long": True,
        "allow_short": False,
        "leverage": 2.0,
        "sizing_mode": "FIXED_MARGIN",
        "max_margin_usdt": 150.0,
        "fixed_stop_pct": 0.05,
        "fixed_target_pct": 0.20,
        "max_open_positions": 0,
    },
    "RSI5_RSI25_5X_WIDE": {
        "label": "RSI 25 LONG · leva 5x · Wide",
        "allow_long": True,
        "allow_short": False,
        "leverage": 5.0,
        "sizing_mode": "FIXED_MARGIN",
        "max_margin_usdt": 500.0,
        "max_open_positions": 2,
    },
}

# Strategie sorgente che possono essere monitorate anche quando non sono
# abilitate nel conto reale. La Combo Adaptive resta laboratorio/dry-run,
# ma il suo esito teorico viene comunque ricostruito dopo un rifiuto live.
HYPOTHETICAL_STRATEGIES = {
    **STRATEGIES,
    "SHADOW_COMBO_ADAPTIVE": {
        "label": "Combo Adaptive",
        "allow_long": True,
        "allow_short": True,
        "leverage": 2.0,
        "sizing_mode": "FIXED_RISK",
    },
}

ASSET_ALIASES = {"BTC": "XBT"}
OID_NAMESPACE = uuid.UUID("2e93cbdb-2f48-429b-a3e2-8c1e4843d633")


class LiveError(RuntimeError):
    pass


class ApiError(LiveError):
    def __init__(self, message: str, code: str = "", status: int = 0):
        super().__init__(message)
        self.code = code
        self.status = status


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def iso_now() -> str:
    return utc_now().isoformat(timespec="seconds")


def parse_time(value: Any) -> datetime | None:
    if not value:
        return None
    text = str(value).strip().replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def seconds_old(value: Any) -> float:
    parsed = parse_time(value)
    if parsed is None:
        return float("inf")
    return max(0.0, (utc_now() - parsed).total_seconds())


def number(value: Any, default: float = 0.0) -> float:
    try:
        result = float(value)
    except Exception:
        return default
    return result if math.isfinite(result) else default


def decimal_value(value: Any, default: str = "0") -> Decimal:
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError):
        result = Decimal(default)
    return result if result.is_finite() else Decimal(default)


def floor_step(value: Decimal, step: Decimal) -> Decimal:
    if value <= 0 or step <= 0:
        return Decimal("0")
    return (value / step).to_integral_value(rounding=ROUND_DOWN) * step


def ceil_step(value: Decimal, step: Decimal) -> Decimal:
    if value <= 0 or step <= 0:
        return Decimal("0")
    return (value / step).to_integral_value(rounding=ROUND_UP) * step


def decimal_text(value: Decimal) -> str:
    text = format(value, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text or "0"


def first_value(row: dict[str, Any], names: tuple[str, ...]) -> Any:
    for name in names:
        value = row.get(name)
        if value not in (None, ""):
            return value
    return None


def read_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise LiveError(f"JSON non valido: {path}: {exc}") from exc


def atomic_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def append_jsonl(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False) + "\n")


def credentials_from_env() -> dict[str, str]:
    names = (
        "KUCOIN_FUTURES_API_KEY",
        "KUCOIN_FUTURES_API_SECRET",
        "KUCOIN_FUTURES_API_PASSPHRASE",
        "KUCOIN_FUTURES_API_KEY_VERSION",
    )
    values = {name: os.getenv(name, "").strip() for name in names}
    missing = [name for name, value in values.items() if not value]
    if missing:
        raise LiveError("Credenziali mancanti: " + ", ".join(missing))
    return values


def b64_hmac(secret: str, message: str) -> str:
    digest = hmac.new(
        secret.encode("utf-8"),
        message.encode("utf-8"),
        hashlib.sha256,
    ).digest()
    return base64.b64encode(digest).decode("ascii")


def signed_request(
    method: str,
    endpoint: str,
    creds: dict[str, str],
    timeout_seconds: int,
    body: dict[str, Any] | None = None,
) -> dict[str, Any]:
    method = method.upper()
    body_text = ""
    body_bytes = None
    if body is not None:
        body_text = json.dumps(
            body,
            ensure_ascii=False,
            separators=(",", ":"),
        )
        body_bytes = body_text.encode("utf-8")

    timestamp = str(int(time.time() * 1000))
    secret = creds["KUCOIN_FUTURES_API_SECRET"]
    headers = {
        "KC-API-KEY": creds["KUCOIN_FUTURES_API_KEY"],
        "KC-API-SIGN": b64_hmac(
            secret,
            timestamp + method + endpoint + body_text,
        ),
        "KC-API-TIMESTAMP": timestamp,
        "KC-API-PASSPHRASE": b64_hmac(
            secret,
            creds["KUCOIN_FUTURES_API_PASSPHRASE"],
        ),
        "KC-API-KEY-VERSION": creds[
            "KUCOIN_FUTURES_API_KEY_VERSION"
        ],
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "CryptoFractalScanner-FuturesDualLive/1.0",
    }
    request = urllib.request.Request(
        FUTURES_BASE + endpoint,
        data=body_bytes,
        method=method,
        headers=headers,
    )

    try:
        with urllib.request.urlopen(
            request,
            timeout=timeout_seconds,
        ) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        try:
            error_payload = json.loads(raw)
        except Exception:
            error_payload = {}
        code = str(error_payload.get("code", ""))
        message = str(error_payload.get("msg", raw))
        raise ApiError(
            f"KuCoin HTTP {exc.code}: {code} {message}",
            code=code,
            status=exc.code,
        ) from exc
    except urllib.error.URLError as exc:
        raise LiveError(f"Connessione KuCoin fallita: {exc}") from exc

    code = str(payload.get("code", ""))
    if code != "200000":
        raise ApiError(
            "KuCoin ha rifiutato la richiesta: "
            + json.dumps(payload, ensure_ascii=False),
            code=code,
        )
    return payload


def get_symbol_margin_mode(
    symbol: str,
    creds: dict[str, str],
    timeout_seconds: int,
) -> str:
    endpoint = MARGIN_MODE_GET_EP + "?" + urllib.parse.urlencode(
        {"symbol": symbol}
    )
    payload = signed_request(
        "GET", endpoint, creds, timeout_seconds
    )
    data = payload.get("data", {})
    if not isinstance(data, dict):
        raise LiveError(f"MARGIN_MODE_READ_FAILED:{symbol}")
    mode = str(data.get("marginMode") or "").strip().upper()
    if mode not in {"ISOLATED", "CROSS"}:
        raise LiveError(
            f"MARGIN_MODE_READ_FAILED:{symbol}:{mode or 'EMPTY'}"
        )
    return mode


def ensure_symbol_margin_mode(
    symbol: str,
    desired_mode: str,
    creds: dict[str, str],
    timeout_seconds: int,
    verify_attempts: int = 3,
    verify_delay_seconds: float = 0.5,
) -> dict[str, Any]:
    desired = str(desired_mode).strip().upper()
    if desired not in {"ISOLATED", "CROSS"}:
        raise LiveError(f"MARGIN_MODE_INVALID:{desired_mode}")

    before = get_symbol_margin_mode(
        symbol, creds, timeout_seconds
    )
    changed = before != desired
    if changed:
        signed_request(
            "POST",
            MARGIN_MODE_CHANGE_EP,
            creds,
            timeout_seconds,
            {"symbol": symbol, "marginMode": desired},
        )

    attempts = max(1, int(verify_attempts))
    delay = max(0.0, float(verify_delay_seconds))
    after = before
    for attempt in range(attempts):
        if attempt > 0 and delay > 0:
            time.sleep(delay)
        after = get_symbol_margin_mode(
            symbol, creds, timeout_seconds
        )
        if after == desired:
            return {
                "symbol": symbol,
                "before": before,
                "after": after,
                "desired": desired,
                "changed": changed,
                "verified": True,
                "verified_utc": iso_now(),
            }

    raise LiveError(
        f"MARGIN_MODE_VERIFY_FAILED:{symbol}:{after}:{desired}"
    )


def entry_margin_mode_guard(
    body: dict[str, Any],
    cfg: dict[str, Any],
    creds: dict[str, str],
    timeout_seconds: int,
) -> dict[str, Any]:
    if cfg.get("auto_ensure_margin_mode") is not True:
        raise LiveError("MARGIN_MODE_AUTO_GUARD_DISABLED")
    symbol = str(body.get("symbol") or "").strip()
    if not symbol:
        raise LiveError("MARGIN_MODE_SYMBOL_MISSING")
    desired = str(
        body.get("marginMode") or cfg.get("margin_mode") or ""
    ).upper()
    return ensure_symbol_margin_mode(
        symbol,
        desired,
        creds,
        timeout_seconds,
        int(cfg.get("margin_mode_verify_attempts", 3)),
        number(cfg.get("margin_mode_verify_delay_seconds"), 0.5),
    )


def submit_entry_order(
    body: dict[str, Any],
    cfg: dict[str, Any],
    creds: dict[str, str],
    timeout_seconds: int,
) -> tuple[dict[str, Any], dict[str, Any]]:
    guard = entry_margin_mode_guard(
        body, cfg, creds, timeout_seconds
    )
    try:
        response = signed_request(
            "POST", TPSL_EP, creds, timeout_seconds, body
        )
    except ApiError as exc:
        if (
            exc.code != "330005"
            or cfg.get("margin_mode_retry_on_330005") is not True
        ):
            raise
        # Una sola seconda verifica e un solo nuovo tentativo.
        delay = number(
            cfg.get("margin_mode_verify_delay_seconds"), 0.5
        )
        if delay > 0:
            time.sleep(delay)
        guard = entry_margin_mode_guard(
            body, cfg, creds, timeout_seconds
        )
        response = signed_request(
            "POST", TPSL_EP, creds, timeout_seconds, body
        )
        guard["order_retry_after_330005"] = True
    return response, guard


def public_get(endpoint: str, timeout_seconds: int) -> dict[str, Any]:
    request = urllib.request.Request(
        FUTURES_BASE + endpoint,
        method="GET",
        headers={
            "Accept": "application/json",
            "User-Agent": "CryptoFractalScanner-FuturesDualLive/1.0",
        },
    )
    try:
        with urllib.request.urlopen(
            request,
            timeout=timeout_seconds,
        ) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except Exception as exc:
        raise LiveError(f"Richiesta pubblica KuCoin fallita: {exc}") from exc
    if str(payload.get("code", "")) != "200000":
        raise LiveError(
            "KuCoin public API error: "
            + json.dumps(payload, ensure_ascii=False)
        )
    return payload


def get_order_by_client_oid(
    client_oid: str,
    creds: dict[str, str],
    timeout_seconds: int,
) -> dict[str, Any] | None:
    endpoint = ORDER_BY_CLIENT_EP + "?" + urllib.parse.urlencode(
        {"clientOid": client_oid}
    )
    try:
        payload = signed_request(
            "GET",
            endpoint,
            creds,
            timeout_seconds,
        )
    except ApiError as exc:
        if exc.status == 404 or exc.code in {
            "400100",
            "404000",
            "100001",
        }:
            return None
        raise
    data = payload.get("data")
    return data if isinstance(data, dict) and data else None


def deterministic_oid(action: str, source_trade_id: str) -> str:
    return str(
        uuid.uuid5(
            OID_NAMESPACE,
            f"{action}:{source_trade_id}",
        )
    )


def telegram_send(text: str, timeout_seconds: int) -> bool:
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat_id:
        return False
    payload = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": text,
        "disable_web_page_preview": "true",
    }).encode("utf-8")
    request = urllib.request.Request(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data=payload,
        method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    try:
        with urllib.request.urlopen(
            request,
            timeout=timeout_seconds,
        ) as response:
            result = json.loads(response.read().decode("utf-8"))
        return bool(result.get("ok"))
    except Exception:
        return False


def notify_once(
    state: dict[str, Any],
    event_key: str,
    text: str,
    timeout_seconds: int,
) -> None:
    """Invia una notifica best-effort una sola volta.

    Le notifiche operative di apertura e chiusura usano invece
    ``notify_reliably_once``: se Telegram non risponde vengono salvate
    in una coda persistente e ritentate ai cicli successivi.
    """
    sent = set(state.setdefault("telegram_sent", []))
    if event_key in sent:
        return
    if telegram_send(text, timeout_seconds):
        sent.add(event_key)
        state["telegram_sent"] = sorted(sent)


def _telegram_outbox(state: dict[str, Any]) -> dict[str, dict[str, Any]]:
    outbox = state.setdefault("telegram_outbox", {})
    if not isinstance(outbox, dict):
        outbox = {}
        state["telegram_outbox"] = outbox
    return outbox


def _telegram_delivery_stats(state: dict[str, Any]) -> dict[str, Any]:
    stats = state.setdefault(
        "telegram_delivery_stats",
        {
            "queued_total": 0,
            "sent_immediately": 0,
            "sent_after_retry": 0,
            "failed_attempts": 0,
            "last_success_utc": None,
            "last_failure_utc": None,
        },
    )
    if not isinstance(stats, dict):
        stats = {
            "queued_total": 0,
            "sent_immediately": 0,
            "sent_after_retry": 0,
            "failed_attempts": 0,
            "last_success_utc": None,
            "last_failure_utc": None,
        }
        state["telegram_delivery_stats"] = stats
    return stats


def notify_reliably_once(
    state: dict[str, Any],
    event_key: str,
    text: str,
    timeout_seconds: int,
) -> bool:
    """Invia subito oppure conserva la notifica per un retry persistente."""
    sent = set(state.setdefault("telegram_sent", []))
    outbox = _telegram_outbox(state)
    stats = _telegram_delivery_stats(state)
    if event_key in sent:
        outbox.pop(event_key, None)
        return True

    if telegram_send(text, timeout_seconds):
        sent.add(event_key)
        state["telegram_sent"] = sorted(sent)
        outbox.pop(event_key, None)
        stats["sent_immediately"] = int(stats.get("sent_immediately", 0)) + 1
        stats["last_success_utc"] = iso_now()
        return True

    item = outbox.get(event_key)
    if not isinstance(item, dict):
        item = {
            "event_key": event_key,
            "text": text,
            "queued_utc": iso_now(),
            "attempts": 0,
            "last_attempt_utc": None,
        }
        outbox[event_key] = item
        stats["queued_total"] = int(stats.get("queued_total", 0)) + 1
    else:
        item["text"] = text
    item["attempts"] = int(item.get("attempts", 0)) + 1
    item["last_attempt_utc"] = iso_now()
    stats["failed_attempts"] = int(stats.get("failed_attempts", 0)) + 1
    stats["last_failure_utc"] = iso_now()
    return False


def flush_telegram_outbox(
    state: dict[str, Any],
    timeout_seconds: int,
    max_items: int = 20,
) -> dict[str, int]:
    """Ritenta le notifiche operative non consegnate nei cicli precedenti."""
    sent = set(state.setdefault("telegram_sent", []))
    outbox = _telegram_outbox(state)
    stats = _telegram_delivery_stats(state)
    delivered = 0
    attempted = 0

    ordered = sorted(
        outbox.items(),
        key=lambda item: str(
            item[1].get("queued_utc", "")
            if isinstance(item[1], dict)
            else ""
        ),
    )
    for event_key, item in ordered[:max_items]:
        if event_key in sent:
            outbox.pop(event_key, None)
            continue
        if not isinstance(item, dict):
            outbox.pop(event_key, None)
            continue
        message = str(item.get("text") or "").strip()
        if not message:
            outbox.pop(event_key, None)
            continue
        attempted += 1
        item["attempts"] = int(item.get("attempts", 0)) + 1
        item["last_attempt_utc"] = iso_now()
        if telegram_send(message, timeout_seconds):
            sent.add(event_key)
            outbox.pop(event_key, None)
            delivered += 1
            stats["sent_after_retry"] = int(
                stats.get("sent_after_retry", 0)
            ) + 1
            stats["last_success_utc"] = iso_now()
        else:
            stats["failed_attempts"] = int(
                stats.get("failed_attempts", 0)
            ) + 1
            stats["last_failure_utc"] = iso_now()

    state["telegram_sent"] = sorted(sent)
    return {
        "attempted": attempted,
        "delivered": delivered,
        "pending": len(outbox),
    }


def normalize_simulated_positions(
    raw: Any,
) -> dict[str, dict[str, Any]]:
    if not isinstance(raw, dict):
        return {}
    container = raw.get("simulated_positions", raw)
    if isinstance(container, list):
        rows = {
            str(
                first_value(
                    row,
                    ("source_trade_id", "trade_id", "id"),
                )
                or index
            ): row
            for index, row in enumerate(container)
            if isinstance(row, dict)
        }
    elif isinstance(container, dict):
        rows = {
            str(key): value
            for key, value in container.items()
            if isinstance(value, dict)
        }
    else:
        return {}

    result: dict[str, dict[str, Any]] = {}
    for key, row in rows.items():
        normalized = dict(row)
        normalized["source_trade_id"] = str(
            first_value(
                row,
                ("source_trade_id", "trade_id", "id"),
            )
            or key
        )
        normalized["source_strategy"] = str(
            first_value(
                row,
                ("source_strategy", "strategy", "account"),
            )
            or ""
        )
        normalized["asset"] = str(
            first_value(
                row,
                ("asset", "symbol", "base_asset"),
            )
            or ""
        ).upper().replace("-USDT", "").replace("USDTM", "")
        normalized["side"] = str(
            first_value(
                row,
                ("side", "direction"),
            )
            or ""
        ).upper()
        normalized["entry_price"] = first_value(
            row,
            ("entry_price", "open_price", "start_price"),
        )
        normalized["stop_price"] = first_value(
            row,
            (
                "stop_price",
                "initial_stop_price",
                "stop_loss_price",
                "sl_price",
            ),
        )
        normalized["target_price"] = first_value(
            row,
            (
                "target_price",
                "take_profit_price",
                "tp_price",
            ),
        )
        normalized["source_opened_utc"] = first_value(
            row,
            (
                "opened_utc",
                "opened_at_utc",
                "generated_utc",
                "entry_utc",
                "created_utc",
            ),
        )
        normalized.setdefault("source_book", "DRY_RUN")
        result[normalized["source_trade_id"]] = normalized
    return result


def normalize_rsi_shadow_positions(
    raw: Any,
    account_name: str,
) -> dict[str, dict[str, Any]]:
    """Estrae solo le posizioni aperte del conto RSI Shadow autorizzato."""
    if not isinstance(raw, dict):
        return {}
    shadow_accounts = raw.get("shadow_accounts", {})
    if not isinstance(shadow_accounts, dict):
        return {}
    account = shadow_accounts.get(account_name, {})
    if not isinstance(account, dict):
        return {}
    positions = account.get("open_positions", [])
    if not isinstance(positions, list):
        return {}

    result: dict[str, dict[str, Any]] = {}
    for row in positions:
        if not isinstance(row, dict):
            continue
        trade_id = str(row.get("trade_id") or "").strip()
        if not trade_id:
            continue
        side = str(row.get("direction") or "").upper()
        if side != "LONG":
            continue
        result[trade_id] = {
            **row,
            "source_trade_id": trade_id,
            "source_strategy": account_name,
            "asset": str(row.get("asset") or "").upper(),
            "side": side,
            "entry_price": row.get("entry_price"),
            "stop_price": row.get("stop_price"),
            "target_price": row.get("target_price"),
            "source_opened_utc": (
                row.get("opened_at")
                or row.get("opened_candle_time")
            ),
            "source_book": "SHADOW",
        }
    return result


def _find_named_portfolio_node(raw: Any, account_name: str) -> dict[str, Any] | None:
    if isinstance(raw, dict):
        portfolios = raw.get("portfolios")
        if isinstance(portfolios, dict):
            node = portfolios.get(account_name)
            if isinstance(node, dict):
                return node
        if isinstance(portfolios, list):
            for row in portfolios:
                if not isinstance(row, dict):
                    continue
                name = str(first_value(row, ("name", "portfolio", "account")) or "")
                if name == account_name:
                    return row
        name = str(first_value(raw, ("name", "portfolio", "account")) or "")
        if name == account_name:
            return raw
        for value in raw.values():
            found = _find_named_portfolio_node(value, account_name)
            if found is not None:
                return found
    elif isinstance(raw, list):
        for value in raw:
            found = _find_named_portfolio_node(value, account_name)
            if found is not None:
                return found
    return None


def normalize_paper_shadow_positions(
    raw: Any,
    account_name: str,
) -> dict[str, dict[str, Any]]:
    """Estrae le posizioni aperte del portfolio Paper Shadow autorizzato."""
    node = _find_named_portfolio_node(raw, account_name)
    if not isinstance(node, dict):
        return {}

    positions: list[dict[str, Any]] = []
    for key in ("open_positions", "positions", "open_trades"):
        value = node.get(key)
        if isinstance(value, list):
            positions.extend(row for row in value if isinstance(row, dict))

    result: dict[str, dict[str, Any]] = {}
    for row in positions:
        status = str(first_value(row, ("status", "state", "trade_status")) or "").lower()
        closed_at = first_value(row, ("closed_at", "closed_utc", "exit_at", "exit_utc"))
        if status in {"closed", "completed", "exited"} or closed_at not in (None, ""):
            continue
        origin_id = str(first_value(row, ("trade_id", "source_trade_id", "position_id", "id")) or "").strip()
        if not origin_id:
            continue
        side = str(first_value(row, ("side", "direction", "position_side")) or "").upper()
        if side != "LONG":
            continue
        asset = str(first_value(row, ("asset", "symbol", "base_asset")) or "").upper()
        asset = asset.replace("-USDT", "").replace("USDTM", "")
        source_trade_id = f"{account_name}:{origin_id}"
        result[source_trade_id] = {
            **row,
            "origin_trade_id": origin_id,
            "source_trade_id": source_trade_id,
            "source_strategy": account_name,
            "asset": asset,
            "side": side,
            "entry_price": first_value(row, ("entry_price", "open_price", "start_price")),
            "stop_price": first_value(row, ("stop_price", "initial_stop_price", "stop_loss_price", "sl_price")),
            "target_price": first_value(row, ("target_price", "take_profit_price", "tp_price")),
            "source_opened_utc": first_value(row, ("opened_at", "opened_utc", "opened_at_utc", "entry_utc", "created_utc", "generated_utc")),
            "source_book": "PAPER_SHADOW",
        }
    return result


def merge_source_positions(
    dry_state: Any,
    paper_state: Any,
    paper_account: str,
    rsi_state: Any,
    rsi_account: str,
) -> dict[str, dict[str, Any]]:
    # Conserva tutti i segnali del dry-run nel flusso decisionale.
    # Le strategie non autorizzate non possono aprire ordini: vengono
    # classificate come STRATEGY_NOT_ENABLED, ma restano silenziose nel live.
    merged = normalize_simulated_positions(dry_state)
    merged.update(normalize_paper_shadow_positions(paper_state, paper_account))
    merged.update(normalize_rsi_shadow_positions(rsi_state, rsi_account))
    return merged


def contract_rows(payload: dict[str, Any]) -> list[dict[str, Any]]:
    data = payload.get("data", [])
    if isinstance(data, list):
        return [row for row in data if isinstance(row, dict)]
    if isinstance(data, dict) and data.get("symbol"):
        return [data]
    return []


def contract_index(
    rows: list[dict[str, Any]],
) -> dict[str, list[dict[str, Any]]]:
    result: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        if str(row.get("settleCurrency", "")).upper() != "USDT":
            continue
        base = str(
            row.get("baseCurrency")
            or row.get("displayBaseCurrency")
            or ""
        ).upper()
        if base:
            result.setdefault(base, []).append(row)
    return result


def choose_contract(
    asset: str,
    index: dict[str, list[dict[str, Any]]],
) -> dict[str, Any] | None:
    base = ASSET_ALIASES.get(asset.upper(), asset.upper())
    candidates = index.get(base, [])
    if not candidates:
        return None

    def score(row: dict[str, Any]) -> tuple[int, int, str]:
        symbol = str(row.get("symbol", ""))
        perpetual = row.get("expireDate") in (None, "", 0)
        normal = str(row.get("marketStage", "NORMAL")).upper() == "NORMAL"
        return (
            int(symbol.endswith("USDTM"))
            + int(perpetual)
            + int(normal),
            int(symbol.endswith("USDTM")),
            symbol,
        )

    return sorted(candidates, key=score, reverse=True)[0]


def active_exchange_positions(
    payload: dict[str, Any],
) -> list[dict[str, Any]]:
    data = payload.get("data", [])
    if not isinstance(data, list):
        return []
    result = []
    for row in data:
        if not isinstance(row, dict):
            continue
        quantity = number(
            row.get("currentQty", row.get("currentQuantity", 0))
        )
        if bool(row.get("isOpen")) or abs(quantity) > 0:
            copied = dict(row)
            copied["_quantity"] = quantity
            copied["_side"] = "LONG" if quantity > 0 else "SHORT"
            result.append(copied)
    return result



# TOP5_BTC_REGIME_FILTER_V1
def market_regime_status(cfg: dict[str, Any]) -> dict[str, Any]:
    # Legge il regime Research; Scanner Top 5 Long resta senza blocchi aggiuntivi.
    path = Path(str(cfg.get("market_regime_path", "")))
    result = {
        "source_path": str(path),
        "available": False,
        "fresh": False,
        "generated_utc": None,
        "age_seconds": None,
        "regime": "UNAVAILABLE",
        "raw_regime": None,
        "confidence_pct": None,
        "reason": None,
    }
    if not path.is_file():
        result["reason"] = "REGIME_FILE_MISSING"
        return result

    try:
        payload = read_json(path, {})
    except Exception as exc:
        result["reason"] = f"REGIME_FILE_INVALID: {exc}"
        return result

    if not isinstance(payload, dict):
        result["reason"] = "REGIME_PAYLOAD_NOT_OBJECT"
        return result

    current = payload.get("current_regime", {})
    if not isinstance(current, dict):
        result["reason"] = "CURRENT_REGIME_MISSING"
        return result

    raw_regime = str(current.get("regime") or "").strip().upper()
    regime = str(
        current.get("regime_family")
        or current.get("regime")
        or ""
    ).strip().upper()
    generated = current.get("generated_utc") or payload.get("generated_utc")
    age = seconds_old(generated)
    max_age = number(cfg.get("regime_max_age_seconds"), 1800.0)

    result.update({
        "available": bool(regime),
        "fresh": bool(regime) and age <= max_age,
        "generated_utc": generated,
        "age_seconds": round(age, 3) if math.isfinite(age) else None,
        "regime": regime or "UNAVAILABLE",
        "raw_regime": raw_regime or None,
        "confidence_pct": current.get("confidence_pct"),
        "reason": current.get("reason"),
    })
    return result


def regime_entry_block_reason(
    strategy: str,
    regime_info: dict[str, Any],
    cfg: dict[str, Any],
) -> str | None:
    if cfg.get("regime_filter_enabled") is not True:
        return None

    if strategy == "SHADOW_SCANNER_TOP5_BTC":
        if not regime_info.get("available") or not regime_info.get("fresh"):
            return "REGIME_DATA_WAIT"
        policies = cfg.get("strategy_blocked_regimes", {})
        if not isinstance(policies, dict):
            return "REGIME_DATA_WAIT"
        blocked = {
            str(value).strip().upper()
            for value in policies.get(strategy, [])
        }
        regime = str(regime_info.get("regime", "")).upper()
        if regime in blocked:
            return f"REGIME_BLOCK_{regime}"
        return None

    if strategy == "RSI5_RSI25_5X_WIDE":
        if cfg.get("rsi_regime_filter_enabled") is not True:
            return None
        if not regime_info.get("available") or not regime_info.get("fresh"):
            return "RSI_REGIME_DATA_WAIT"
        combined = "|".join(
            [
                str(regime_info.get("regime") or ""),
                str(regime_info.get("raw_regime") or ""),
            ]
        ).upper()
        blocked_tokens = [
            str(value).strip().upper()
            for value in cfg.get("rsi_blocked_regime_tokens", [])
            if str(value).strip()
        ]
        for token in blocked_tokens:
            if token in combined:
                return f"RSI_REGIME_BLOCK_{token}"
        return None

    return None


def validate_config(cfg: dict[str, Any]) -> None:
    expected = {
        "mode": "LIVE_ARMED_AUTO_FUNDING",
        "armed": True,
        "auto_start_on_funds": True,
        "compounding_enabled": False,
        "compounding_base": "FIXED_OPERATING_CAPITAL",
        "profit_reinvestment_enabled": False,
        "operating_capital_usdt": 3760.0,
        "minimum_operating_equity_usdt": 3500.0,
        "global_max_drawdown_usdt": 260.0,
        "margin_mode": "ISOLATED",
        "auto_ensure_margin_mode": True,
        "margin_mode_verify_attempts": 3,
        "margin_mode_verify_delay_seconds": 0.5,
        "margin_mode_retry_on_330005": True,
        "risk_per_trade_pct": 0.20,
        "max_total_open_risk_pct": 1.50,
        "max_total_positions": 0,
        "max_positions_per_strategy": 0,
        "max_position_margin_pct": 50.0,
        "daily_loss_limit_enabled": False,
        "daily_loss_limit_pct": 1.0,
        "rsi_max_margin_usdt": 500.0,
        "rsi_leverage": 5.0,
        "rsi_max_consecutive_losses": 3,
        "rsi_block_if_cumulative_pnl_negative": True,
    }
    errors = {
        key: {"actual": cfg.get(key), "expected": value}
        for key, value in expected.items()
        if cfg.get(key) != value
    }
    if errors:
        raise LiveError(
            "Configurazione live alterata: "
            + json.dumps(errors, ensure_ascii=False)
        )
    if set(cfg.get("strategies", [])) != set(STRATEGIES):
        raise LiveError("Strategie live diverse dalle tre autorizzate.")
    if cfg.get("track_rejected_trade_outcomes") is not True:
        raise LiveError("Monitoraggio esiti trade rifiutati non attivo.")
    if number(cfg.get("hypothetical_taker_fee_rate"), -1.0) < 0:
        raise LiveError("Commissione teorica non valida.")
    if not isinstance(cfg.get("hypothetical_close_csv_paths"), list):
        raise LiveError("Elenco CSV chiusure teoriche non valido.")

    if cfg.get("regime_filter_enabled") is not True:
        raise LiveError("Filtro regime non abilitato.")
    if not str(cfg.get("market_regime_path", "")).strip():
        raise LiveError("Percorso market regime mancante.")
    if number(cfg.get("regime_max_age_seconds")) != 1800.0:
        raise LiveError("Età massima regime diversa da 1800 secondi.")

    policies = cfg.get("strategy_blocked_regimes", {})
    if not isinstance(policies, dict):
        raise LiveError("Policy regime non valida.")
    blocked = {
        str(value).strip().upper()
        for value in policies.get("SHADOW_SCANNER_TOP5_BTC", [])
    }
    if blocked != {"TREND_UP"}:
        raise LiveError("Top5 BTC deve essere bloccata solo in TREND_UP.")
    top5_long_blocked = policies.get("SHADOW_SCANNER_TOP5_LONG", [])
    if top5_long_blocked not in (None, []):
        raise LiveError("Scanner Top 5 Long non deve avere filtri di regime.")

    if cfg.get("rsi_regime_filter_enabled") is not True:
        raise LiveError("Filtro regime RSI non abilitato.")
    required_tokens = {
        "TREND_DOWN",
        "ALT_ROTATION_DOWN",
        "RISK_OFF",
        "CRASH",
        "BEAR",
    }
    actual_tokens = {
        str(value).strip().upper()
        for value in cfg.get("rsi_blocked_regime_tokens", [])
    }
    if actual_tokens != required_tokens:
        raise LiveError("Token di blocco regime RSI alterati.")

    if not str(cfg.get("rsi_source_state_path", "")).strip():
        raise LiveError("Percorso sorgente RSI mancante.")
    if cfg.get("rsi_source_account") != "RSI5_RSI25_5X_WIDE":
        raise LiveError("Conto sorgente RSI non autorizzato.")
    if cfg.get("paper_source_account") != "SHADOW_SCANNER_TOP5_LONG":
        raise LiveError("Conto sorgente Scanner Top 5 Long non autorizzato.")
    if not str(cfg.get("paper_source_state_path", "")).strip():
        raise LiveError("Percorso sorgente Scanner Top 5 Long mancante.")
    if number(cfg.get("closure_settlement_wait_seconds")) < 300.0:
        raise LiveError("Attesa settlement chiusure troppo breve.")


def validate_dry_run_config(cfg: dict[str, Any]) -> None:
    dry_cfg = read_json(Path(cfg["dry_run_config_path"]))
    if not isinstance(dry_cfg, dict):
        raise LiveError("Configurazione dry-run mancante.")
    if dry_cfg.get("mode") != "DRY_RUN_ONLY":
        raise LiveError("La sorgente non è DRY_RUN_ONLY.")
    if dry_cfg.get("execution_enabled") is not False:
        raise LiveError("La sorgente dry-run risulta abilitata agli ordini.")
    source_names = {
        str(row.get("name"))
        for row in dry_cfg.get("sources", [])
        if isinstance(row, dict)
    }
    expected_sources = {
        "SHADOW_SCANNER_TOP5_BTC",
        "SHADOW_COMBO_ADAPTIVE",
    }
    if source_names != expected_sources:
        raise LiveError(
            "Le sorgenti dry-run non coincidono con "
            "SHADOW_SCANNER_TOP5_BTC e SHADOW_COMBO_ADAPTIVE."
        )
    rsi_path = Path(str(cfg.get("rsi_source_state_path", "")))
    if not rsi_path.is_file():
        raise LiveError("Stato sorgente RSI Shadow mancante.")
    paper_path = Path(str(cfg.get("paper_source_state_path", "")))
    if not paper_path.is_file():
        raise LiveError("Stato sorgente Scanner Top 5 Long mancante.")


def initial_strategy_stats() -> dict[str, dict[str, Any]]:
    return {
        strategy: {
            "closed_trades": 0,
            "winning_trades": 0,
            "losing_trades": 0,
            "consecutive_losses": 0,
            "realized_pnl_usdt": 0.0,
            "last_close_utc": None,
            "last_close_pnl_usdt": None,
        }
        for strategy in STRATEGIES
    }


def initial_state(current_ids: list[str]) -> dict[str, Any]:
    return {
        "schema_version": 5,
        "initialized": True,
        "armed_at_utc": iso_now(),
        "baseline_source_trade_ids": sorted(current_ids),
        "ignored_source_trade_ids": sorted(current_ids),
        "completed_source_trade_ids": [],
        "skipped_source_trade_ids": {},
        "rejected_trade_watches": {},
        "rejected_trade_watch_history": [],
        "rejected_trade_watch_stats": {
            "closed": 0,
            "positive": 0,
            "negative": 0,
            "breakeven": 0,
            "estimated_net_pnl_usdt": 0.0,
        },
        "first_seen_utc": {},
        "live_positions": {},
        "pending_entries": {},
        "telegram_sent": [],
        "telegram_outbox": {},
        "telegram_delivery_stats": {
            "queued_total": 0,
            "sent_immediately": 0,
            "sent_after_retry": 0,
            "failed_attempts": 0,
            "last_success_utc": None,
            "last_failure_utc": None,
        },
        "global_entry_block_latched": False,
        "global_entry_block_reason": None,
        "global_entry_block_utc": None,
        "rsi_entry_block_latched": False,
        "rsi_entry_block_reason": None,
        "rsi_entry_block_utc": None,
        "rsi_source_baselined": True,
        "paper_source_baselined": True,
        "day_utc": utc_now().date().isoformat(),
        "day_start_equity_usdt": 0.0,
        "high_water_equity_usdt": 0.0,
        "previous_equity_usdt": 0.0,
        "live_start_equity_usdt": 0.0,
        "strategy_stats": initial_strategy_stats(),
        "last_run_utc": None,
    }


def migrate_state(
    state: dict[str, Any],
    current_rsi_ids: set[str],
    current_paper_ids: set[str],
) -> None:
    state["schema_version"] = 5
    state.setdefault("telegram_outbox", {})
    _telegram_delivery_stats(state)
    state.setdefault("global_entry_block_latched", False)
    state.setdefault("global_entry_block_reason", None)
    state.setdefault("global_entry_block_utc", None)
    state.setdefault("rsi_entry_block_latched", False)
    state.setdefault("rsi_entry_block_reason", None)
    state.setdefault("rsi_entry_block_utc", None)
    state.setdefault("live_start_equity_usdt", 0.0)
    watches = state.setdefault("rejected_trade_watches", {})
    # Elimina eventuali osservazioni create dalle versioni precedenti per
    # strategie non più autorizzate nel live. In questo modo non arriverà
    # nemmeno il successivo messaggio di esito teorico alla loro chiusura.
    if isinstance(watches, dict):
        state["rejected_trade_watches"] = {
            trade_id: watch
            for trade_id, watch in watches.items()
            if not (
                isinstance(watch, dict)
                and str(watch.get("rejection_reason") or "")
                == "STRATEGY_NOT_ENABLED"
            )
        }
    state.setdefault("rejected_trade_watch_history", [])
    state.setdefault("rejected_trade_watch_stats", {
        "closed": 0,
        "positive": 0,
        "negative": 0,
        "breakeven": 0,
        "estimated_net_pnl_usdt": 0.0,
    })
    stats = state.setdefault("strategy_stats", {})
    for strategy, blank in initial_strategy_stats().items():
        row = stats.setdefault(strategy, {})
        for key, value in blank.items():
            row.setdefault(key, value)

    # Prima esecuzione della versione triple: ignora eventuali posizioni RSI
    # già aperte, così non entra a metà di un trade storico.
    if not state.get("rsi_source_baselined"):
        ignored = set(state.setdefault("ignored_source_trade_ids", []))
        ignored.update(current_rsi_ids)
        state["ignored_source_trade_ids"] = sorted(ignored)
        state["rsi_source_baselined"] = True
        state["rsi_source_baselined_utc"] = iso_now()

    # Prima esecuzione con Scanner Top 5 Long: ignora le posizioni Paper
    # già aperte, evitando di entrare a metà di un trade storico.
    if not state.get("paper_source_baselined"):
        ignored = set(state.setdefault("ignored_source_trade_ids", []))
        ignored.update(current_paper_ids)
        state["ignored_source_trade_ids"] = sorted(ignored)
        state["paper_source_baselined"] = True
        state["paper_source_baselined_utc"] = iso_now()


def update_equity_baselines(
    state: dict[str, Any],
    equity: float,
    managed_open: bool,
    cfg: dict[str, Any],
) -> tuple[bool, float, bool]:
    today = utc_now().date().isoformat()
    previous = number(state.get("previous_equity_usdt"))
    high_water = number(state.get("high_water_equity_usdt"))
    day_start = number(state.get("day_start_equity_usdt"))

    transfer_like = (
        not managed_open
        and (
            (previous <= 0 < equity)
            or (
                previous > 0
                and abs(equity - previous) / previous
                >= number(cfg["balance_reset_change_pct"]) / 100.0
            )
        )
    )

    if transfer_like:
        high_water = equity
        day_start = equity
        state["day_utc"] = today
        state["last_balance_reset_utc"] = iso_now()
    else:
        if state.get("day_utc") != today:
            state["day_utc"] = today
            day_start = equity
        if equity > high_water:
            high_water = equity
        if equity > 0 and high_water <= 0:
            high_water = equity
        if equity > 0 and day_start <= 0:
            day_start = equity

    if equity > 0 and number(state.get("live_start_equity_usdt")) <= 0:
        state["live_start_equity_usdt"] = equity
        state["live_start_equity_utc"] = iso_now()

    state["previous_equity_usdt"] = equity
    state["high_water_equity_usdt"] = high_water
    state["day_start_equity_usdt"] = day_start

    daily_loss_hit = (
        cfg.get("daily_loss_limit_enabled") is True
        and day_start > 0
        and equity
        <= day_start
        * (1.0 - number(cfg["daily_loss_limit_pct"]) / 100.0)
    )
    global_threshold = max(
        number(cfg["minimum_operating_equity_usdt"]),
        high_water - number(cfg["global_max_drawdown_usdt"]),
    )
    global_threshold_hit = (
        high_water > 0
        and equity > 0
        and equity <= global_threshold
    )
    return daily_loss_hit, global_threshold, global_threshold_hit



def hypothetical_policy(strategy: str) -> dict[str, Any] | None:
    policy = HYPOTHETICAL_STRATEGIES.get(strategy)
    return dict(policy) if isinstance(policy, dict) else None


def build_hypothetical_watch(
    intent: dict[str, Any],
    contract: dict[str, Any] | None,
    cfg: dict[str, Any],
    equity: float,
    rejection_reason: str,
    regime_info: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Crea la simulazione del trade non aperto con sizing live fisso.

    Usa il mark del momento quando disponibile. Se il contratto o il mark
    non sono utilizzabili, ripiega sui parametri già calcolati dalla sorgente.
    Non prepara né invia alcun ordine.
    """
    strategy = str(intent.get("source_strategy") or "")
    side = str(intent.get("side") or "").upper()
    asset = str(intent.get("asset") or "").upper()
    policy = hypothetical_policy(strategy)

    source_entry = number(intent.get("entry_price"))
    stop = number(intent.get("stop_price"))
    target = number(intent.get("target_price"))
    mark = number((contract or {}).get("markPrice") or (contract or {}).get("lastTradePrice"))
    entry = mark if mark > 0 else source_entry
    if side == "LONG" and not (stop < entry < target):
        entry = source_entry
    elif side == "SHORT" and not (target < entry < stop):
        entry = source_entry
    if side not in {"LONG", "SHORT"} or min(entry, stop, target) <= 0:
        raise LiveError("Parametri insufficienti per monitorare il trade rifiutato.")

    stop_distance_pct = abs(entry - stop) / entry * 100.0
    if stop_distance_pct <= 0:
        raise LiveError("Stop nullo nel trade rifiutato.")

    leverage = number((policy or {}).get("leverage"))
    if leverage <= 0:
        leverage = number(first_value(intent, ("planned_leverage", "leverage")), 1.0)
    sizing_mode = str((policy or {}).get("sizing_mode") or "SOURCE_FALLBACK")
    operating_capital = number(cfg.get("operating_capital_usdt"), 3760.0)

    if sizing_mode == "FIXED_MARGIN":
        margin = min(
            number(cfg.get("rsi_max_margin_usdt"), 500.0),
            number((policy or {}).get("max_margin_usdt"), 500.0),
        )
        notional = margin * leverage
    elif sizing_mode == "FIXED_RISK":
        risk = operating_capital * number(cfg.get("risk_per_trade_pct"), 0.2) / 100.0
        notional = risk / (stop_distance_pct / 100.0)
        margin_cap = operating_capital * number(cfg.get("max_position_margin_pct"), 50.0) / 100.0
        notional = min(notional, margin_cap * leverage)
        margin = notional / leverage
    else:
        notional = number(first_value(intent, ("planned_notional_usdt", "notional_usdt")))
        margin = number(first_value(intent, ("planned_margin_usdt", "margin_usdt")))
        if notional <= 0 and margin > 0 and leverage > 0:
            notional = margin * leverage
        if margin <= 0 and notional > 0 and leverage > 0:
            margin = notional / leverage

    if notional <= 0 or margin <= 0 or leverage <= 0:
        raise LiveError("Sizing teorico non ricostruibile.")

    return {
        "source_trade_id": str(intent.get("source_trade_id") or ""),
        "origin_trade_id": str(intent.get("origin_trade_id") or ""),
        "source_strategy": strategy,
        "strategy_label": str((policy or {}).get("label") or strategy),
        "source_book": str(intent.get("source_book") or "UNKNOWN"),
        "asset": asset,
        "side": side,
        "source_opened_utc": intent.get("source_opened_utc"),
        "rejection_reason": rejection_reason,
        "rejected_utc": iso_now(),
        "market_regime_at_rejection": str(
            (regime_info or {}).get("regime")
            or intent.get("entry_regime")
            or intent.get("regime")
            or "UNKNOWN"
        ).upper(),
        "regime_family_at_rejection": str(
            (regime_info or {}).get("regime_family")
            or intent.get("entry_regime_family")
            or intent.get("regime_family")
            or "UNKNOWN"
        ).upper(),
        "volatility_state_at_rejection": str(
            (regime_info or {}).get("volatility_state")
            or intent.get("entry_volatility_state")
            or intent.get("volatility_state")
            or "UNKNOWN"
        ).upper(),
        "entry_price": entry,
        "source_entry_price": source_entry,
        "entry_basis": "LIVE_MARK_AT_REJECTION" if mark > 0 and entry == mark else "SOURCE_ENTRY",
        "stop_price": stop,
        "target_price": target,
        "stop_distance_pct": stop_distance_pct,
        "leverage": leverage,
        "margin_usdt": margin,
        "notional_usdt": notional,
        "sizing_mode": sizing_mode,
        "operating_capital_usdt": operating_capital,
        "account_equity_at_rejection_usdt": equity,
        "status": "OPEN_SOURCE",
        "source_disappeared_utc": None,
    }


def add_rejected_trade_watch(
    state: dict[str, Any],
    intent: dict[str, Any],
    contract: dict[str, Any] | None,
    cfg: dict[str, Any],
    equity: float,
    rejection_reason: str,
    regime_info: dict[str, Any] | None = None,
) -> dict[str, Any] | None:
    if cfg.get("track_rejected_trade_outcomes") is not True:
        return None
    # Una strategia esclusa dal live non rappresenta un trade "perso" dai
    # filtri operativi: continua nel dry-run, ma non genera osservazioni o
    # notifiche del conto reale.
    if rejection_reason == "STRATEGY_NOT_ENABLED":
        return None
    trade_id = str(intent.get("source_trade_id") or "")
    if not trade_id:
        return None
    watches = state.setdefault("rejected_trade_watches", {})
    if trade_id in watches:
        return watches[trade_id]
    try:
        watch = build_hypothetical_watch(
            intent, contract, cfg, equity, rejection_reason, regime_info
        )
    except LiveError as exc:
        log_event(
            cfg,
            "REJECTED_TRADE_WATCH_UNAVAILABLE",
            source_trade_id=trade_id,
            source_strategy=intent.get("source_strategy"),
            asset=intent.get("asset"),
            reason=rejection_reason,
            detail=str(exc),
        )
        return None
    watches[trade_id] = watch
    log_event(
        cfg,
        "REJECTED_TRADE_WATCH_STARTED",
        source_trade_id=trade_id,
        source_strategy=watch["source_strategy"],
        asset=watch["asset"],
        side=watch["side"],
        rejection_reason=rejection_reason,
        entry_price=watch["entry_price"],
        notional_usdt=watch["notional_usdt"],
        margin_usdt=watch["margin_usdt"],
    )
    return watch


def _normalized_trade_ids(value: Any) -> set[str]:
    text = str(value or "").strip()
    if not text:
        return set()
    ids = {text}
    if "::" in text:
        ids.add(text.split("::", 1)[1])
    if text.endswith(":SHADOW"):
        ids.add(text[:-7])
    if ":" in text:
        ids.add(text.split(":", 1)[1])
    return {item for item in ids if item}


def _row_matches_watch(row: dict[str, Any], watch: dict[str, Any]) -> bool:
    wanted = set()
    wanted.update(_normalized_trade_ids(watch.get("source_trade_id")))
    wanted.update(_normalized_trade_ids(watch.get("origin_trade_id")))
    found = set()
    for key in (
        "source_trade_id", "trade_id", "origin_trade_id", "position_id",
        "id", "client_trade_id",
    ):
        found.update(_normalized_trade_ids(row.get(key)))
    return bool(wanted & found)


def _close_record_from_row(row: dict[str, Any]) -> dict[str, Any] | None:
    event = str(first_value(row, (
        "intent_type", "event_type", "event", "action", "type",
        "status", "state", "trade_status",
    )) or "").upper()
    exit_price = number(first_value(row, (
        "source_exit_price", "exit_price", "close_price", "closed_price",
        "exit_mark_price", "price_exit",
    )))
    pnl_value = first_value(row, (
        "net_pnl_usdt", "realized_pnl_usdt", "pnl_usdt", "net_pnl",
        "pnl", "source_net_pnl_eur", "net_pnl_eur",
    ))
    pnl = number(pnl_value, float("nan"))
    close_time = first_value(row, (
        "closed_at", "closed_utc", "close_time", "exit_time", "exit_utc",
        "generated_utc", "timestamp",
    ))
    close_reason = first_value(row, (
        "exit_reason", "close_reason", "reason", "last_close_reason",
    ))
    closed_marker = (
        any(token in event for token in ("CLOSE", "CLOSED", "EXIT", "STOP", "TARGET", "COMPLETED"))
        or exit_price > 0
        or math.isfinite(pnl)
    )
    if not closed_marker:
        return None
    currency = "USDT"
    if row.get("source_net_pnl_eur") not in (None, "") or row.get("net_pnl_eur") not in (None, ""):
        currency = "EUR"
    return {
        "exit_price": exit_price if exit_price > 0 else None,
        "source_net_pnl": pnl if math.isfinite(pnl) else None,
        "source_pnl_currency": currency,
        "closed_utc": close_time,
        "close_reason": str(close_reason or event or "SOURCE_CLOSED"),
        "source_notional_usdt": number(first_value(row, (
            "planned_notional_usdt", "notional_usdt", "source_notional_usdt",
        ))),
        "raw": row,
    }


def _scan_json_for_close(obj: Any, watch: dict[str, Any]) -> dict[str, Any] | None:
    if isinstance(obj, dict):
        if _row_matches_watch(obj, watch):
            record = _close_record_from_row(obj)
            if record is not None:
                return record
        for value in obj.values():
            found = _scan_json_for_close(value, watch)
            if found is not None:
                return found
    elif isinstance(obj, list):
        for value in obj:
            found = _scan_json_for_close(value, watch)
            if found is not None:
                return found
    return None


def _candidate_close_csv_paths(cfg: dict[str, Any]) -> list[Path]:
    result: list[Path] = []
    seen: set[str] = set()
    for raw in cfg.get("hypothetical_close_csv_paths", []):
        path = Path(str(raw))
        if path.is_file() and str(path) not in seen:
            seen.add(str(path))
            result.append(path)
    report_dir = Path(str(cfg.get("state_path", "reports/x"))).parent
    patterns = cfg.get("hypothetical_close_csv_globs", [])
    for pattern in patterns if isinstance(patterns, list) else []:
        for path in sorted(report_dir.glob(str(pattern))):
            if path.is_file() and str(path) not in seen:
                seen.add(str(path))
                result.append(path)
    return result


def find_source_close_record(
    watch: dict[str, Any],
    cfg: dict[str, Any],
    dry_state: Any,
    paper_state: Any,
    rsi_state: Any,
) -> dict[str, Any] | None:
    for payload in (dry_state, paper_state, rsi_state):
        found = _scan_json_for_close(payload, watch)
        if found is not None:
            return found
    for path in _candidate_close_csv_paths(cfg):
        try:
            with path.open(errors="replace", newline="") as handle:
                for row in csv.DictReader(handle):
                    if not isinstance(row, dict) or not _row_matches_watch(row, watch):
                        continue
                    found = _close_record_from_row(row)
                    if found is not None:
                        found["source_path"] = str(path)
                        return found
        except (OSError, csv.Error):
            continue
    return None


def calculate_hypothetical_outcome(
    watch: dict[str, Any],
    close: dict[str, Any],
    cfg: dict[str, Any],
) -> dict[str, Any]:
    entry = number(watch.get("entry_price"))
    exit_price = number(close.get("exit_price"))
    notional = number(watch.get("notional_usdt"))
    side = str(watch.get("side") or "").upper()
    fee_rate = number(cfg.get("hypothetical_taker_fee_rate"), 0.0006)
    gross = float("nan")
    entry_fee = float("nan")
    exit_fee = float("nan")
    net = float("nan")
    method = "PRICE_RECONSTRUCTION"

    if min(entry, exit_price, notional) > 0 and side in {"LONG", "SHORT"}:
        quantity = notional / entry
        gross = quantity * (exit_price - entry)
        if side == "SHORT":
            gross = -gross
        entry_fee = notional * fee_rate
        exit_notional = quantity * exit_price
        exit_fee = exit_notional * fee_rate
        net = gross - entry_fee - exit_fee
    else:
        source_pnl = close.get("source_net_pnl")
        source_notional = number(close.get("source_notional_usdt"))
        if source_pnl is not None and math.isfinite(number(source_pnl, float("nan"))):
            net = number(source_pnl)
            if source_notional > 0 and notional > 0:
                net *= notional / source_notional
            gross = net
            entry_fee = 0.0
            exit_fee = 0.0
            method = "SCALED_SOURCE_PNL"
        else:
            raise LiveError("Chiusura sorgente senza prezzo o PnL utilizzabile.")

    threshold = number(cfg.get("hypothetical_breakeven_epsilon_usdt"), 0.01)
    if net > threshold:
        result = "POSITIVE"
    elif net < -threshold:
        result = "NEGATIVE"
    else:
        result = "BREAKEVEN"
    return {
        "result": result,
        "gross_pnl_usdt": gross,
        "entry_fee_estimate_usdt": entry_fee,
        "exit_fee_estimate_usdt": exit_fee,
        "estimated_net_pnl_usdt": net,
        "calculation_method": method,
        "funding_included": False,
        "exit_price": exit_price if exit_price > 0 else None,
        "closed_utc": close.get("closed_utc") or iso_now(),
        "close_reason": close.get("close_reason") or "SOURCE_CLOSED",
        "source_path": close.get("source_path"),
    }


def format_rejected_trade_outcome_message(
    watch: dict[str, Any],
    outcome: dict[str, Any],
    stats: dict[str, Any],
) -> str:
    result_label = {
        "POSITIVE": "✅ POSITIVO",
        "NEGATIVE": "❌ NEGATIVO",
        "BREAKEVEN": "➖ PAREGGIO",
    }.get(str(outcome.get("result")), str(outcome.get("result")))
    method_note = (
        "ricostruzione da prezzi e commissioni taker stimate"
        if outcome.get("calculation_method") == "PRICE_RECONSTRUCTION"
        else "PnL sorgente ridimensionato"
    )
    return (
        "🧪 FUTURES LIVE — ESITO TRADE NON APERTO\n\n"
        f"Strategia: {watch.get('strategy_label') or watch.get('source_strategy')}\n"
        f"Asset: {watch.get('asset')}\n"
        f"Lato: {watch.get('side')}\n"
        f"Motivo mancata apertura: {human_rejection_reason(str(watch.get('rejection_reason') or ''))}\n\n"
        f"Entrata teorica: {number(watch.get('entry_price')):.8g}\n"
        f"Uscita sorgente: {number(outcome.get('exit_price')):.8g}\n"
        f"Motivo chiusura: {outcome.get('close_reason')}\n"
        f"Leva teorica: {number(watch.get('leverage')):.0f}x\n"
        f"Margine teorico: {number(watch.get('margin_usdt')):.2f} USDT\n"
        f"Nozionale teorico: {number(watch.get('notional_usdt')):.2f} USDT\n\n"
        f"Esito: {result_label}\n"
        f"PnL lordo teorico: {number(outcome.get('gross_pnl_usdt')):+.2f} USDT\n"
        f"Commissioni stimate: -{number(outcome.get('entry_fee_estimate_usdt')) + number(outcome.get('exit_fee_estimate_usdt')):.2f} USDT\n"
        f"PnL netto teorico: {number(outcome.get('estimated_net_pnl_usdt')):+.2f} USDT\n"
        f"Metodo: {method_note}; funding escluso.\n\n"
        f"Storico trade non aperti: {int(stats.get('positive', 0))} positivi / "
        f"{int(stats.get('negative', 0))} negativi / {int(stats.get('breakeven', 0))} pari · "
        f"PnL teorico cumulativo {number(stats.get('estimated_net_pnl_usdt')):+.2f} USDT\n\n"
        "Nessun ordine reale era stato aperto su KuCoin."
    )


def bootstrap_recent_rejected_trade_watches(
    state: dict[str, Any],
    simulated: dict[str, dict[str, Any]],
    contracts: dict[str, list[dict[str, Any]]],
    cfg: dict[str, Any],
    equity: float,
    regime_info: dict[str, Any] | None = None,
) -> int:
    """Aggancia i rifiuti recenti già presenti nello stato al primo avvio v5."""
    watches = state.setdefault("rejected_trade_watches", {})
    historical_ids = {
        str(row.get("source_trade_id") or "")
        for row in state.get("rejected_trade_watch_history", [])
        if isinstance(row, dict)
    }
    skipped = state.setdefault("skipped_source_trade_ids", {})
    max_age = number(
        cfg.get("hypothetical_bootstrap_recent_skips_hours"), 24.0
    ) * 3600.0
    created = 0
    for trade_id, intent in simulated.items():
        if trade_id in watches or trade_id in historical_ids:
            continue
        info = skipped.get(trade_id)
        if not isinstance(info, dict):
            continue
        skipped_utc = info.get("skipped_utc")
        if skipped_utc and seconds_old(skipped_utc) > max_age:
            continue
        reason = str(info.get("reason") or "PREVIOUSLY_REJECTED")
        contract = choose_contract(
            str(intent.get("asset") or "").upper(), contracts
        )
        if add_rejected_trade_watch(
            state, intent, contract, cfg, equity, reason, regime_info
        ) is not None:
            created += 1
    return created


def settle_rejected_trade_watches(
    state: dict[str, Any],
    current_source_ids: set[str],
    cfg: dict[str, Any],
    dry_state: Any,
    paper_state: Any,
    rsi_state: Any,
    timeout_seconds: int,
) -> None:
    watches = state.setdefault("rejected_trade_watches", {})
    history = state.setdefault("rejected_trade_watch_history", [])
    stats = state.setdefault("rejected_trade_watch_stats", {
        "closed": 0,
        "positive": 0,
        "negative": 0,
        "breakeven": 0,
        "estimated_net_pnl_usdt": 0.0,
    })
    for trade_id, watch in list(watches.items()):
        if trade_id in current_source_ids:
            continue
        watch.setdefault("source_disappeared_utc", iso_now())
        close = find_source_close_record(
            watch, cfg, dry_state, paper_state, rsi_state
        )
        if close is None:
            continue
        try:
            outcome = calculate_hypothetical_outcome(watch, close, cfg)
        except LiveError as exc:
            watch["settlement_error"] = str(exc)
            continue
        result_key = str(outcome["result"]).lower()
        stats["closed"] = int(stats.get("closed", 0)) + 1
        stats[result_key] = int(stats.get(result_key, 0)) + 1
        stats["estimated_net_pnl_usdt"] = (
            number(stats.get("estimated_net_pnl_usdt"))
            + number(outcome.get("estimated_net_pnl_usdt"))
        )
        settled = {**watch, **outcome, "settled_utc": iso_now()}
        history.append(settled)
        max_history = int(cfg.get("hypothetical_history_limit", 500))
        if len(history) > max_history:
            del history[:-max_history]
        watches.pop(trade_id, None)
        log_event(
            cfg,
            "REJECTED_TRADE_WATCH_CLOSED",
            source_trade_id=trade_id,
            source_strategy=watch.get("source_strategy"),
            asset=watch.get("asset"),
            result=outcome.get("result"),
            estimated_net_pnl_usdt=outcome.get("estimated_net_pnl_usdt"),
            rejection_reason=watch.get("rejection_reason"),
        )
        notify_once(
            state,
            f"rejected-outcome:{trade_id}",
            format_rejected_trade_outcome_message(watch, outcome, stats),
            timeout_seconds,
        )


def build_entry_plan(
    intent: dict[str, Any],
    contract: dict[str, Any],
    cfg: dict[str, Any],
    equity: float,
    available_balance: float,
) -> dict[str, Any]:
    strategy = str(intent.get("source_strategy", ""))
    side = str(intent.get("side", "")).upper()
    asset = str(intent.get("asset", "")).upper()

    if strategy not in STRATEGIES:
        raise LiveError("Strategia non autorizzata.")
    strategy_cfg = STRATEGIES[strategy]
    if side not in {"LONG", "SHORT"}:
        raise LiveError("Direzione non valida.")
    if side == "LONG" and not strategy_cfg["allow_long"]:
        raise LiveError("LONG non autorizzato per questa strategia.")
    if side == "SHORT" and not strategy_cfg["allow_short"]:
        raise LiveError("SHORT non autorizzato per questa strategia.")

    mark = decimal_value(
        contract.get("markPrice")
        or contract.get("lastTradePrice")
    )
    source_entry = decimal_value(intent.get("entry_price"))
    stop = decimal_value(intent.get("stop_price"))
    target = decimal_value(intent.get("target_price"))
    tick = decimal_value(contract.get("tickSize"), "0.00000001")
    multiplier = decimal_value(contract.get("multiplier"))
    lot = decimal_value(contract.get("lotSize"), "1")
    leverage = decimal_value(strategy_cfg["leverage"])
    operating_capital = decimal_value(cfg["operating_capital_usdt"])
    available_d = decimal_value(available_balance)

    if min(mark, stop, target, multiplier, lot) <= 0:
        raise LiveError("Mark, stop, target o contratto non validi.")

    entry_deviation_pct = Decimal("0")
    if source_entry > 0:
        entry_deviation_pct = (
            abs(mark - source_entry) / source_entry * Decimal("100")
        )
        if entry_deviation_pct > decimal_value(
            cfg["max_entry_deviation_pct"]
        ):
            raise LiveError("Prezzo troppo distante dal segnale sorgente.")

    if side == "LONG":
        if not (stop < mark < target):
            raise LiveError("Stop/target LONG non più validi.")
        stop = floor_step(stop, tick)
        target = ceil_step(target, tick)
        exchange_side = "buy"
        trigger_up = target
        trigger_down = stop
    else:
        if not (target < mark < stop):
            raise LiveError("Stop/target SHORT non più validi.")
        stop = ceil_step(stop, tick)
        target = floor_step(target, tick)
        exchange_side = "sell"
        trigger_up = stop
        trigger_down = target

    # TOP5_FIXED_STOP_V1
    fixed_stop_pct = decimal_value(strategy_cfg.get("fixed_stop_pct", "0"))
    if fixed_stop_pct > 0:
        if side == "LONG":
            stop = floor_step(mark * (Decimal("1") - fixed_stop_pct), tick)
            trigger_down = stop
        else:
            stop = ceil_step(mark * (Decimal("1") + fixed_stop_pct), tick)
            trigger_up = stop

    # TOP5_FIXED_TARGET_V1
    fixed_target_pct = decimal_value(
        strategy_cfg.get("fixed_target_pct", "0")
    )
    if fixed_target_pct > 0:
        if side == "LONG":
            target = ceil_step(
                mark * (Decimal("1") + fixed_target_pct),
                tick,
            )
            trigger_up = target
        else:
            target = floor_step(
                mark * (Decimal("1") - fixed_target_pct),
                tick,
            )
            trigger_down = target

    stop_distance_pct = abs(mark - stop) / mark * Decimal("100")
    if stop_distance_pct <= 0:
        raise LiveError("Distanza stop nulla.")

    reserve = (
        operating_capital
        * decimal_value(cfg["available_margin_reserve_pct"])
        / Decimal("100")
    )
    margin_cap_available = max(Decimal("0"), available_d - reserve)

    sizing_mode = str(strategy_cfg["sizing_mode"])
    if sizing_mode == "FIXED_MARGIN":
        requested_margin = min(
            decimal_value(cfg["rsi_max_margin_usdt"]),
            decimal_value(strategy_cfg["max_margin_usdt"]),
            margin_cap_available,
        )
        requested_notional = requested_margin * leverage
        risk_budget = (
            requested_notional
            * stop_distance_pct
            / Decimal("100")
        )
    else:
        risk_budget = (
            operating_capital
            * decimal_value(cfg["risk_per_trade_pct"])
            / Decimal("100")
        )
        risk_based_notional = (
            risk_budget / (stop_distance_pct / Decimal("100"))
        )
        margin_cap_strategy = (
            operating_capital
            * decimal_value(cfg["max_position_margin_pct"])
            / Decimal("100")
        )
        margin_cap = min(margin_cap_strategy, margin_cap_available)
        requested_notional = min(
            risk_based_notional,
            margin_cap * leverage,
        )

    denominator = mark * multiplier
    if denominator <= 0:
        raise LiveError("Multiplier contratto non valido.")
    raw_contracts = requested_notional / denominator
    contracts_d = floor_step(raw_contracts, lot)

    maximum_qty = decimal_value(
        contract.get("marketMaxOrderQty")
        or contract.get("maxOrderQty")
        or "0"
    )
    if maximum_qty > 0:
        contracts_d = min(contracts_d, floor_step(maximum_qty, lot))

    if contracts_d != contracts_d.to_integral_value():
        raise LiveError("Size contrattuale non intera.")
    contracts = int(contracts_d)
    actual_notional = contracts_d * multiplier * mark
    actual_margin = actual_notional / leverage
    actual_risk = (
        actual_notional
        * stop_distance_pct
        / Decimal("100")
    )

    if contracts <= 0:
        raise LiveError("Size inferiore al minimo contrattuale.")
    if sizing_mode == "FIXED_RISK":
        if actual_risk > risk_budget + Decimal("0.00000001"):
            raise LiveError("Rischio effettivo sopra il budget fisso.")
    else:
        if actual_margin > decimal_value(cfg["rsi_max_margin_usdt"]):
            raise LiveError("Margine RSI superiore a 500 USDT.")
    if actual_margin > margin_cap_available:
        raise LiveError("Margine disponibile insufficiente.")
    if str(contract.get("marketStage", "NORMAL")).upper() != "NORMAL":
        raise LiveError("Contratto non in market stage NORMAL.")
    if decimal_value(contract.get("maxLeverage"), "100") < leverage:
        raise LiveError(
            f"Contratto incompatibile con leva {decimal_text(leverage)}x."
        )

    trade_id = str(intent["source_trade_id"])
    client_oid = deterministic_oid("open", trade_id)
    body = {
        "clientOid": client_oid,
        "symbol": str(contract["symbol"]),
        "marginMode": cfg["margin_mode"],
        "leverage": int(leverage),
        "positionSide": "BOTH",
        "side": exchange_side,
        "type": "market",
        "size": contracts,
        "stopPriceType": "TP",
        "triggerStopUpPrice": decimal_text(trigger_up),
        "triggerStopDownPrice": decimal_text(trigger_down),
        "reduceOnly": False,
        "remark": "fdl_entry",
    }

    return {
        "source_trade_id": trade_id,
        "source_strategy": strategy,
        "strategy_label": str(strategy_cfg["label"]),
        "asset": asset,
        "side": side,
        "symbol": str(contract["symbol"]),
        "client_oid": client_oid,
        "contracts": contracts,
        "source_entry_price": float(source_entry),
        "entry_mark_price": float(mark),
        "entry_deviation_pct": float(entry_deviation_pct),
        "stop_price": float(stop),
        "target_price": float(target),
        "stop_distance_pct": float(stop_distance_pct),
        "sizing_equity_usdt": float(operating_capital),
        "actual_account_equity_usdt": equity,
        "available_balance_before_usdt": available_balance,
        "risk_budget_usdt": float(risk_budget),
        "actual_risk_usdt": float(actual_risk),
        "notional_usdt": float(actual_notional),
        "margin_usdt": float(actual_margin),
        "leverage": float(leverage),
        "sizing_mode": sizing_mode,
        "compounding_base": "FIXED_OPERATING_CAPITAL",
        "operating_capital_usdt": float(operating_capital),
        "profit_reinvestment_enabled": False,
        "order_body": body,
    }


def close_order_body(
    live: dict[str, Any],
    exchange_quantity: float,
    cfg: dict[str, Any],
) -> tuple[str, dict[str, Any]]:
    trade_id = str(live["source_trade_id"])
    client_oid = deterministic_oid("close", trade_id)
    return client_oid, {
        "clientOid": client_oid,
        "symbol": str(live["symbol"]),
        "marginMode": cfg["margin_mode"],
        "leverage": int(number(live.get("leverage"), 2.0)),
        "positionSide": "BOTH",
        "side": "sell" if live["side"] == "LONG" else "buy",
        "type": "market",
        "size": int(abs(exchange_quantity)),
        "reduceOnly": True,
        "remark": "fdl_close",
    }


def cancel_symbol_stops(
    symbol: str,
    creds: dict[str, str],
    timeout_seconds: int,
) -> None:
    endpoint = STOP_ORDERS_EP + "?" + urllib.parse.urlencode(
        {"symbol": symbol}
    )
    try:
        signed_request(
            "DELETE",
            endpoint,
            creds,
            timeout_seconds,
        )
    except ApiError as exc:
        if exc.code not in {
            "300004",
            "300009",
            "400100",
            "404000",
        }:
            raise


def epoch_millis(value: Any) -> int:
    parsed = parse_time(value)
    if parsed is None:
        return 0
    return int(parsed.timestamp() * 1000)


def latest_position_history(
    live: dict[str, Any],
    creds: dict[str, str],
    timeout_seconds: int,
) -> dict[str, Any] | None:
    opened_ms = epoch_millis(
        live.get("submitted_utc") or live.get("prepared_utc")
    )
    if opened_ms <= 0:
        opened_ms = int((time.time() - 86400) * 1000)
    start_ms = max(0, opened_ms - 5 * 60 * 1000)
    end_ms = int(time.time() * 1000) + 60 * 1000
    endpoint = HISTORY_POSITIONS_EP + "?" + urllib.parse.urlencode({
        "symbol": str(live.get("symbol") or ""),
        "from": start_ms,
        "to": end_ms,
        "limit": 50,
    })
    try:
        payload = signed_request(
            "GET", endpoint, creds, timeout_seconds
        )
    except (ApiError, LiveError):
        return None
    data = payload.get("data", {})
    items = data.get("items", []) if isinstance(data, dict) else []
    if not isinstance(items, list):
        return None

    expected_side = str(live.get("side") or "").upper()
    matches: list[dict[str, Any]] = []
    for row in items:
        if not isinstance(row, dict):
            continue
        if str(row.get("symbol") or "") != str(live.get("symbol") or ""):
            continue
        side = str(row.get("side") or "").upper()
        type_text = str(row.get("type") or "").upper()
        if expected_side and side and side != expected_side:
            continue
        if expected_side and type_text and expected_side not in type_text:
            continue
        open_ms = int(number(row.get("openTime")))
        close_ms = int(number(row.get("closeTime")))
        if close_ms <= 0 or close_ms < opened_ms - 120000:
            continue
        if open_ms > 0 and abs(open_ms - opened_ms) > 10 * 60 * 1000:
            continue
        matches.append(row)
    if not matches:
        return None
    matches.sort(key=lambda row: int(number(row.get("closeTime"))))
    return matches[-1]


def update_strategy_stats(
    state: dict[str, Any],
    strategy: str,
    pnl_usdt: float,
    close_utc: str,
    cfg: dict[str, Any],
) -> dict[str, Any]:
    stats_all = state.setdefault("strategy_stats", {})
    stats = stats_all.setdefault(
        strategy, initial_strategy_stats().get(strategy, {}).copy()
    )
    stats["closed_trades"] = int(stats.get("closed_trades", 0)) + 1
    stats["realized_pnl_usdt"] = (
        number(stats.get("realized_pnl_usdt")) + pnl_usdt
    )
    stats["last_close_utc"] = close_utc
    stats["last_close_pnl_usdt"] = pnl_usdt
    if pnl_usdt < -1e-9:
        stats["losing_trades"] = int(stats.get("losing_trades", 0)) + 1
        stats["consecutive_losses"] = (
            int(stats.get("consecutive_losses", 0)) + 1
        )
    else:
        if pnl_usdt > 1e-9:
            stats["winning_trades"] = (
                int(stats.get("winning_trades", 0)) + 1
            )
        stats["consecutive_losses"] = 0

    if strategy == "RSI5_RSI25_5X_WIDE":
        streak = int(stats.get("consecutive_losses", 0))
        cumulative = number(stats.get("realized_pnl_usdt"))
        if (
            streak >= int(cfg["rsi_max_consecutive_losses"])
            and (
                cfg.get("rsi_block_if_cumulative_pnl_negative") is not True
                or cumulative < 0
            )
        ):
            state["rsi_entry_block_latched"] = True
            state["rsi_entry_block_reason"] = (
                f"RSI_{streak}_CONSECUTIVE_LOSSES_AND_NEGATIVE_PNL"
            )
            state["rsi_entry_block_utc"] = iso_now()
    return stats


def exchange_position_snapshot(
    live: dict[str, Any],
    exchange: dict[str, Any] | None,
) -> dict[str, Any]:
    row = dict(live)
    if not isinstance(exchange, dict):
        row.setdefault("current_price", None)
        row.setdefault("unrealized_pnl_usdt", None)
        return row
    current_price = number(
        exchange.get("markPrice") or exchange.get("avgEntryPrice")
    )
    entry_price = number(
        exchange.get("avgEntryPrice") or live.get("entry_mark_price")
    )
    quantity = abs(number(exchange.get("_quantity")))
    row.update({
        "current_price": current_price,
        "actual_entry_price": entry_price,
        "unrealized_pnl_usdt": number(exchange.get("unrealisedPnl")),
        "exchange_margin_usdt": number(
            exchange.get("posMargin") or exchange.get("posInit")
        ),
        "exchange_notional_usdt": abs(number(exchange.get("markValue"))),
        "exchange_leverage": number(
            exchange.get("leverage") or live.get("leverage")
        ),
        "exchange_quantity": quantity,
        "liquidation_price": number(exchange.get("liquidationPrice")),
    })
    return row


def account_pnl_snapshot(
    account: dict[str, Any],
    state: dict[str, Any],
    cfg: dict[str, Any],
) -> dict[str, float]:
    equity = number(account.get("accountEquity"))
    open_pnl = number(account.get("unrealisedPNL"))
    start_equity = number(state.get("live_start_equity_usdt"))
    if start_equity <= 0:
        start_equity = number(cfg["operating_capital_usdt"])
    total_pnl = equity - start_equity
    return {
        "start_equity_usdt": start_equity,
        "equity_usdt": equity,
        "total_pnl_usdt": total_pnl,
        "open_pnl_usdt": open_pnl,
        "estimated_closed_pnl_usdt": total_pnl - open_pnl,
    }


def format_open_positions_digest(state: dict[str, Any]) -> str:
    positions = state.get("live_positions", {})
    if not isinstance(positions, dict) or not positions:
        return "Posizioni aperte: nessuna"
    lines = ["POSIZIONI APERTE"]
    for live in positions.values():
        if not isinstance(live, dict):
            continue
        snapshot = live.get("last_exchange_snapshot")
        row = snapshot if isinstance(snapshot, dict) else live
        lines.extend([
            (
                f"• {live.get('strategy_label') or live.get('source_strategy')} "
                f"| {live.get('asset')} {live.get('side')}"
            ),
            (
                f"  Entrata {number(row.get('actual_entry_price') or live.get('entry_mark_price')):.8f} "
                f"| Corrente {number(row.get('current_price')):.8f}"
            ),
            (
                f"  Leva {number(row.get('exchange_leverage') or live.get('leverage')):.0f}x "
                f"| Margine {number(row.get('exchange_margin_usdt') or live.get('margin_usdt')):.2f} "
                f"| Nozionale {number(row.get('exchange_notional_usdt') or live.get('notional_usdt')):.2f} USDT"
            ),
            (
                f"  Stop {number(live.get('stop_price')):.8f} "
                f"| Target {number(live.get('target_price')):.8f} "
                f"| PnL {number(row.get('unrealized_pnl_usdt')):+.2f} USDT"
            ),
        ])
    return "\n".join(lines)


REJECTION_REASON_LABELS = {
    "STRATEGY_NOT_ENABLED": "strategia non abilitata nel conto live",
    "RSI_STRATEGY_LATCHED": "RSI sospesa dopo tre perdite consecutive con PnL negativo",
    "STALE_SIGNAL": "segnale troppo vecchio",
    "MAX_TOTAL_POSITIONS": "limite globale disattivato",
    "MAX_POSITIONS_PER_STRATEGY": "raggiunto il limite configurato per questa strategia",
    "DUPLICATE_SAME_ASSET": "esiste già una posizione nello stesso verso sullo stesso asset",
    "OPPOSITE_SAME_ASSET": "esiste già una posizione opposta sullo stesso asset",
    "NO_USDTM_CONTRACT": "contratto Futures USDT-M non disponibile",
    "MAX_TOTAL_OPEN_RISK": "raggiunto il rischio aperto complessivo massimo",
    "RSI_REGIME_BLOCKED": "regime non compatibile con la RSI long",
    "REGIME_BLOCKED": "regime non compatibile con la strategia",
    "MARGIN_MODE_AUTO_SWITCH_FAILED": "impossibile impostare e verificare la modalità isolated del contratto",
}


def human_rejection_reason(reason: str) -> str:
    if reason.startswith("ENTRY_BLOCKED_"):
        details = reason.removeprefix("ENTRY_BLOCKED_").replace("_", " ")
        return f"blocco generale attivo: {details}"
    if reason.startswith("ENTRY_DEVIATION"):
        return "prezzo troppo distante dall'entrata sorgente"
    return REJECTION_REASON_LABELS.get(reason, reason.replace("_", " ").lower())


def rejection_reason_for_message(
    intent: dict[str, Any], reason: str
) -> str:
    asset = str(intent.get("asset") or "n/d").upper()
    side = str(intent.get("side") or "").upper()
    if reason == "DUPLICATE_SAME_ASSET":
        return f"esiste già una posizione REALE LIVE su {asset} {side}"
    if reason == "OPPOSITE_SAME_ASSET":
        existing_side = "SHORT" if side == "LONG" else "LONG" if side == "SHORT" else "opposta"
        return f"esiste già una posizione REALE LIVE su {asset} {existing_side}"
    return human_rejection_reason(reason)


def should_notify_rejected_entry(reason: str, cfg: dict[str, Any]) -> bool:
    return (
        bool(cfg.get("notify_rejected_entries", True))
        and reason != "STRATEGY_NOT_ENABLED"
    )


def format_rejected_trade_message(
    intent: dict[str, Any],
    reason: str,
    account: dict[str, Any],
    state: dict[str, Any],
    cfg: dict[str, Any],
) -> str:
    pnl = account_pnl_snapshot(account, state, cfg)
    return (
        "FUTURES LIVE — TRADE NON APERTO\n"
        f"Strategia: {intent.get('source_strategy') or 'n/d'}\n"
        f"Asset: {intent.get('asset') or 'n/d'} {intent.get('side') or ''}\n"
        f"Entrata sorgente: {number(intent.get('entry_price')):.8f}\n"
        f"Stop sorgente: {number(intent.get('stop_price')):.8f}\n"
        f"Target sorgente: {number(intent.get('target_price')):.8f}\n"
        f"Motivo: {rejection_reason_for_message(intent, reason)}\n"
        f"Codice: {reason}\n"
        f"Equity residua: {pnl['equity_usdt']:.2f} USDT\n"
        f"Disponibile: {number(account.get('availableBalance')):.2f} USDT\n"
        f"PnL conto: {pnl['total_pnl_usdt']:+.2f} USDT"
    )


def format_open_trade_message(
    live: dict[str, Any],
    account: dict[str, Any],
    state: dict[str, Any],
    cfg: dict[str, Any],
    recovered: bool = False,
) -> str:
    pnl = account_pnl_snapshot(account, state, cfg)
    title = (
        "FUTURES LIVE — APERTURA RECUPERATA"
        if recovered
        else "FUTURES LIVE — APERTURA"
    )
    return (
        f"{title}\n"
        f"Strategia: {live.get('strategy_label') or live['source_strategy']}\n"
        f"ID: {live['source_strategy']}\n"
        f"Asset: {live['asset']} {live['side']}\n"
        f"Entrata stimata: {number(live.get('entry_mark_price')):.8f}\n"
        f"Leva: {number(live.get('leverage')):.0f}x isolated\n"
        f"Margine: {number(live.get('margin_usdt')):.2f} USDT\n"
        f"Nozionale: {number(live.get('notional_usdt')):.2f} USDT\n"
        f"Stop: {number(live.get('stop_price')):.8f}\n"
        f"Target: {number(live.get('target_price')):.8f}\n"
        f"Rischio allo stop: {number(live.get('actual_risk_usdt')):.2f} USDT\n"
        f"Equity residua: {pnl['equity_usdt']:.2f} USDT\n"
        f"Disponibile: {number(account.get('availableBalance')):.2f} USDT\n"
        f"PnL conto: {pnl['total_pnl_usdt']:+.2f} USDT\n\n"
        + format_open_positions_digest(state)
    )


def format_close_trade_message(
    live: dict[str, Any],
    history: dict[str, Any],
    account: dict[str, Any],
    state: dict[str, Any],
    cfg: dict[str, Any],
) -> str:
    pnl = account_pnl_snapshot(account, state, cfg)
    strategy_stats = state.get("strategy_stats", {}).get(
        live["source_strategy"], {}
    )
    return (
        "FUTURES LIVE — CHIUSURA\n"
        f"Strategia: {live.get('strategy_label') or live['source_strategy']}\n"
        f"Asset: {live['asset']} {live['side']}\n"
        f"Entrata: {number(history.get('openPrice')):.8f}\n"
        f"Uscita: {number(history.get('closePrice')):.8f}\n"
        f"PnL trade: {number(history.get('pnl')):+.2f} USDT\n"
        f"Fee: {number(history.get('tradeFee')):.2f} USDT\n"
        f"Funding: {number(history.get('fundingFee')):+.2f} USDT\n"
        f"PnL strategia: {number(strategy_stats.get('realized_pnl_usdt')):+.2f} USDT\n"
        f"Perdite consecutive: {int(strategy_stats.get('consecutive_losses', 0))}\n"
        f"Equity residua: {pnl['equity_usdt']:.2f} USDT\n"
        f"Disponibile: {number(account.get('availableBalance')):.2f} USDT\n"
        f"PnL conto: {pnl['total_pnl_usdt']:+.2f} USDT\n\n"
        + format_open_positions_digest(state)
    )


def log_event(
    cfg: dict[str, Any],
    event_type: str,
    **details: Any,
) -> None:
    append_jsonl(
        Path(cfg["event_log_path"]),
        {
            "generated_utc": iso_now(),
            "event_type": event_type,
            **details,
        },
    )


def write_report(
    cfg: dict[str, Any],
    report: dict[str, Any],
) -> None:
    atomic_json(Path(cfg["latest_json_path"]), report)
    account = report["account"]
    protection = report.get("capital_protection", {})
    rsi = report.get("rsi_guard", {})
    lines = [
        "# Futures Triple Live — armato",
        "",
        f"Generato: **{report['generated_utc']}**",
        "",
        f"- Stato: **{report['status']}**",
        f"- Equity residua: **{account['equity_usdt']:.4f} USDT**",
        f"- Disponibile: **{account['available_usdt']:.4f} USDT**",
        f"- PnL totale conto: **{account['total_pnl_usdt']:+.4f} USDT**",
        f"- PnL aperto: **{account['open_pnl_usdt']:+.4f} USDT**",
        "- Compounding: **NO — capitale operativo fisso 3.760 USDT**",
        (
            "- Soglia blocco globale corrente: **"
            f"{number(protection.get('global_block_threshold_usdt')):.4f} USDT**"
        ),
        (
            "- Blocco globale: **"
            + ("ATTIVO" if protection.get("latched") else "non attivo")
            + "**"
        ),
        (
            "- Blocco RSI: **"
            + ("ATTIVO" if rsi.get("latched") else "non attivo")
            + "**"
        ),
        (
            "- PnL RSI live: **"
            f"{number(rsi.get('realized_pnl_usdt')):+.4f} USDT**"
        ),
        (
            "- Perdite RSI consecutive: **"
            f"{int(rsi.get('consecutive_losses', 0))}**"
        ),
        "",
        "## Strategie",
        "",
        "- `SHADOW_SCANNER_TOP5_BTC` — LONG, 2x, rischio fisso",
        "- `SHADOW_SCANNER_TOP5_LONG` — solo LONG, 2x, rischio fisso",
        "- `RSI5_RSI25_5X_WIDE` — LONG, 5x, max 500 USDT margine",
        "",
        "## Blocchi",
        "",
    ]
    blockers = report.get("blockers", [])
    lines.extend(
        [f"- `{value}`" for value in blockers]
        if blockers
        else ["_Nessuno._"]
    )
    lines.extend(["", "## Posizioni live gestite", ""])
    positions = report.get("live_positions", [])
    if not positions:
        lines.append("_Nessuna._")
    else:
        lines.extend([
            "| Strategia | Asset | Lato | Entrata | Corrente | Leva | Margine | Nozionale | Stop | Target | PnL aperto |",
            "| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ])
        for row in positions:
            lines.append(
                f"| {row['source_strategy']} | {row['asset']} | "
                f"{row['side']} | "
                f"{number(row.get('actual_entry_price') or row.get('entry_mark_price')):.8f} | "
                f"{number(row.get('current_price')):.8f} | "
                f"{number(row.get('exchange_leverage') or row.get('leverage')):.0f}x | "
                f"{number(row.get('exchange_margin_usdt') or row.get('margin_usdt')):.4f} | "
                f"{number(row.get('exchange_notional_usdt') or row.get('notional_usdt')):.4f} | "
                f"{number(row.get('stop_price')):.8f} | "
                f"{number(row.get('target_price')):.8f} | "
                f"{number(row.get('unrealized_pnl_usdt')):+.4f} |"
            )
    path = Path(cfg["report_path"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def recover_pending_entries(
    state: dict[str, Any],
    cfg: dict[str, Any],
    creds: dict[str, str],
    timeout_seconds: int,
) -> list[tuple[str, dict[str, Any]]]:
    """Recupera entrate pendenti e restituisce quelle diventate live.

    Le versioni precedenti recuperavano correttamente l'ordine, ma non
    generavano il messaggio Telegram di apertura. Il chiamante ora usa
    l'elenco restituito per inviare una notifica affidabile.
    """
    pending = state.setdefault("pending_entries", {})
    live_positions = state.setdefault("live_positions", {})
    recovered: list[tuple[str, dict[str, Any]]] = []
    for trade_id, item in list(pending.items()):
        if not isinstance(item, dict):
            pending.pop(trade_id, None)
            continue
        client_oid = str(item.get("client_oid", ""))
        order = get_order_by_client_oid(
            client_oid,
            creds,
            timeout_seconds,
        )
        if order is None:
            if seconds_old(item.get("prepared_utc")) < number(
                cfg["pending_retry_after_seconds"]
            ):
                continue
            response, margin_guard = submit_entry_order(
                item["order_body"],
                cfg,
                creds,
                timeout_seconds,
            )
            item.setdefault("plan", {})["margin_mode_guard"] = margin_guard
            order_id = response.get("data", {}).get("orderId")
        else:
            order_id = order.get("id") or order.get("orderId")
        live = dict(item["plan"])
        live["order_id"] = order_id
        live["submitted_utc"] = iso_now()
        live["closing"] = False
        live_positions[trade_id] = live
        pending.pop(trade_id, None)
        log_event(
            cfg,
            "LIVE_ENTRY_RECOVERED",
            source_trade_id=trade_id,
            order_id=order_id,
        )
        recovered.append((trade_id, live))
    return recovered


def run(config_path: Path) -> dict[str, Any]:
    cfg = read_json(config_path)
    if not isinstance(cfg, dict):
        raise LiveError("Configurazione live mancante.")
    validate_config(cfg)
    validate_dry_run_config(cfg)

    lock_path = Path(cfg["lock_path"])
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("a+") as lock:
        try:
            fcntl.flock(
                lock.fileno(),
                fcntl.LOCK_EX | fcntl.LOCK_NB,
            )
        except BlockingIOError:
            return {
                "status": "SKIPPED_ALREADY_RUNNING",
                "generated_utc": iso_now(),
            }

        creds = credentials_from_env()
        timeout_seconds = int(cfg["timeout_seconds"])

        account = signed_request(
            "GET", ACCOUNT_EP, creds, timeout_seconds
        ).get("data", {})
        positions_payload = signed_request(
            "GET", POSITIONS_EP, creds, timeout_seconds
        )
        position_mode_data = signed_request(
            "GET", POSITION_MODE_EP, creds, timeout_seconds
        ).get("data", {})
        contracts_payload = public_get(CONTRACTS_EP, timeout_seconds)

        if not isinstance(account, dict):
            account = {}
        if not isinstance(position_mode_data, dict):
            position_mode_data = {}

        equity = number(account.get("accountEquity"))
        available_balance = number(account.get("availableBalance"))
        exchange_positions = active_exchange_positions(positions_payload)
        position_mode = int(
            number(position_mode_data.get("positionMode"), -1)
        )

        dry_state = read_json(Path(cfg["dry_run_state_path"]), {})
        paper_state = read_json(Path(cfg["paper_source_state_path"]), {})
        rsi_state = read_json(Path(cfg["rsi_source_state_path"]), {})
        paper_positions = normalize_paper_shadow_positions(
            paper_state, str(cfg["paper_source_account"])
        )
        rsi_positions = normalize_rsi_shadow_positions(
            rsi_state, str(cfg["rsi_source_account"])
        )
        simulated = merge_source_positions(
            dry_state,
            paper_state,
            str(cfg["paper_source_account"]),
            rsi_state,
            str(cfg["rsi_source_account"]),
        )
        regime_info = market_regime_status(cfg)

        state_path = Path(cfg["state_path"])
        state = read_json(state_path)
        if not isinstance(state, dict):
            state = initial_state(list(simulated))
            atomic_json(state_path, state)
            log_event(
                cfg,
                "LIVE_EXECUTOR_BASELINED",
                baseline_source_trade_ids=sorted(simulated),
            )
        else:
            migrate_state(state, set(rsi_positions), set(paper_positions))

        retry_result = flush_telegram_outbox(
            state, timeout_seconds
        )
        if retry_result["attempted"]:
            # Persistenza immediata: evita duplicati se un messaggio viene
            # consegnato e un errore successivo interrompe il ciclo.
            atomic_json(state_path, state)

        recovered_entries = recover_pending_entries(
            state, cfg, creds, timeout_seconds
        )
        for recovered_trade_id, recovered_live in recovered_entries:
            notify_reliably_once(
                state,
                f"opened:{recovered_trade_id}",
                format_open_trade_message(
                    recovered_live, account, state, cfg, recovered=True
                ),
                timeout_seconds,
            )
        if recovered_entries:
            atomic_json(state_path, state)

        live_positions = state.setdefault("live_positions", {})

        # Recupera una notifica di apertura eventualmente persa dalle
        # versioni precedenti (per esempio un ordine entrato tramite
        # pending-entry recovery). Non duplica messaggi già inviati o in coda.
        sent_open_events = set(state.setdefault("telegram_sent", []))
        queued_open_events = set(_telegram_outbox(state))
        backfilled_open_alerts = 0
        for existing_trade_id, existing_live in live_positions.items():
            open_event = f"opened:{existing_trade_id}"
            if open_event in sent_open_events or open_event in queued_open_events:
                continue
            if not isinstance(existing_live, dict):
                continue
            notify_reliably_once(
                state,
                open_event,
                format_open_trade_message(
                    existing_live, account, state, cfg, recovered=True
                ),
                timeout_seconds,
            )
            backfilled_open_alerts += 1
        if backfilled_open_alerts:
            atomic_json(state_path, state)

        completed = set(state.get("completed_source_trade_ids", []))
        ignored = set(state.get("ignored_source_trade_ids", []))
        skipped = state.setdefault("skipped_source_trade_ids", {})
        first_seen = state.setdefault("first_seen_utc", {})

        current_source_ids = set(simulated)
        for trade_id in current_source_ids:
            first_seen.setdefault(trade_id, iso_now())

        settle_rejected_trade_watches(
            state,
            current_source_ids,
            cfg,
            dry_state,
            paper_state,
            rsi_state,
            timeout_seconds,
        )

        exchange_by_symbol = {
            str(row.get("symbol")): row
            for row in exchange_positions
        }

        # Finalizza le posizioni già chiuse su KuCoin usando lo storico
        # ufficiale delle posizioni, così il PnL per strategia è reale.
        for trade_id, live in list(live_positions.items()):
            exchange = exchange_by_symbol.get(str(live.get("symbol")))
            if exchange is not None:
                live["last_exchange_snapshot"] = exchange_position_snapshot(
                    live, exchange
                )
                live.pop("settlement_pending_utc", None)
                continue
            if seconds_old(live.get("submitted_utc")) < number(
                cfg["position_visibility_grace_seconds"]
            ):
                continue

            if not live.get("settlement_pending_utc"):
                live["settlement_pending_utc"] = iso_now()
                try:
                    cancel_symbol_stops(
                        str(live["symbol"]), creds, timeout_seconds
                    )
                except LiveError:
                    pass

            history = latest_position_history(
                live, creds, timeout_seconds
            )
            if history is None:
                if seconds_old(live.get("settlement_pending_utc")) >= number(
                    cfg["closure_settlement_wait_seconds"]
                ):
                    notify_once(
                        state,
                        f"settlement-delay:{trade_id}",
                        "FUTURES LIVE — settlement in attesa\n"
                        f"Strategia: {live['source_strategy']}\n"
                        f"Asset: {live['asset']}\n"
                        "La posizione risulta chiusa, ma il PnL KuCoin "
                        "non è ancora disponibile. Nessuna nuova entrata "
                        "su questo slot finché il dato non viene acquisito.",
                        timeout_seconds,
                    )
                continue

            pnl_usdt = number(history.get("pnl"))
            close_utc = (
                datetime.fromtimestamp(
                    number(history.get("closeTime")) / 1000.0,
                    tz=timezone.utc,
                ).isoformat()
                if number(history.get("closeTime")) > 0
                else iso_now()
            )
            live_positions.pop(trade_id, None)
            completed.add(trade_id)
            stats_before_block = bool(
                state.get("rsi_entry_block_latched")
            )
            stats = update_strategy_stats(
                state,
                str(live["source_strategy"]),
                pnl_usdt,
                close_utc,
                cfg,
            )
            log_event(
                cfg,
                "LIVE_POSITION_CLOSED_ON_EXCHANGE",
                source_trade_id=trade_id,
                source_strategy=live["source_strategy"],
                asset=live["asset"],
                pnl_usdt=pnl_usdt,
                trade_fee_usdt=number(history.get("tradeFee")),
                funding_fee_usdt=number(history.get("fundingFee")),
                open_price=number(history.get("openPrice")),
                close_price=number(history.get("closePrice")),
            )
            notify_reliably_once(
                state,
                f"closed:{trade_id}",
                format_close_trade_message(
                    live, history, account, state, cfg
                ),
                timeout_seconds,
            )
            if (
                not stats_before_block
                and state.get("rsi_entry_block_latched")
            ):
                notify_once(
                    state,
                    "rsi-block-latched",
                    "FUTURES LIVE — RSI BLOCCATA\n"
                    "Nuove aperture bloccate solo per "
                    "RSI 25 LONG 5x Wide.\n"
                    f"Perdite consecutive: "
                    f"{int(stats.get('consecutive_losses', 0))}\n"
                    f"PnL RSI live: "
                    f"{number(stats.get('realized_pnl_usdt')):+.2f} USDT\n"
                    "Scanner Top5 BTC e Scanner Top5 Long restano attive.",
                    timeout_seconds,
                )

        managed_symbols = {
            str(row.get("symbol"))
            for row in live_positions.values()
        }
        unmanaged_positions = [
            row
            for row in exchange_positions
            if str(row.get("symbol")) not in managed_symbols
        ]

        daily_loss_hit, global_threshold, global_threshold_hit = (
            update_equity_baselines(
                state, equity, bool(live_positions), cfg
            )
        )
        if (
            global_threshold_hit
            and not state.get("global_entry_block_latched")
        ):
            state["global_entry_block_latched"] = True
            state["global_entry_block_reason"] = (
                "EQUITY_BELOW_PROTECTED_THRESHOLD"
            )
            state["global_entry_block_utc"] = iso_now()
            notify_once(
                state,
                "global-entry-block-latched",
                "FUTURES LIVE — BLOCCO GENERALE\n"
                "Nuove aperture bloccate per tutte le strategie.\n"
                f"Equity: {equity:.2f} USDT\n"
                f"Soglia protetta: {global_threshold:.2f} USDT\n"
                f"Massimo equity: "
                f"{number(state.get('high_water_equity_usdt')):.2f} USDT\n"
                "Le posizioni già aperte restano protette da stop e target.",
                timeout_seconds,
            )

        # Una posizione resta aperta fino a quando la sorgente la chiude.
        # I blocchi di capitale impediscono solo nuove entrate.
        for trade_id, live in list(live_positions.items()):
            exchange = exchange_by_symbol.get(str(live.get("symbol")))
            if exchange is None or bool(live.get("closing")):
                continue
            if trade_id in current_source_ids:
                continue

            close_oid, close_body = close_order_body(
                live, number(exchange.get("_quantity")), cfg
            )
            live["closing"] = True
            live["close_client_oid"] = close_oid
            live["close_prepared_utc"] = iso_now()
            atomic_json(state_path, state)

            existing = get_order_by_client_oid(
                close_oid, creds, timeout_seconds
            )
            if existing is None:
                response = signed_request(
                    "POST", ORDER_EP, creds, timeout_seconds, close_body
                )
                order_id = response.get("data", {}).get("orderId")
            else:
                order_id = existing.get("id") or existing.get("orderId")

            live["close_order_id"] = order_id
            live["close_submitted_utc"] = iso_now()
            atomic_json(state_path, state)
            log_event(
                cfg,
                "LIVE_CLOSE_SUBMITTED",
                source_trade_id=trade_id,
                order_id=order_id,
                reason="SOURCE_CLOSED",
            )

        blockers: list[str] = []
        if equity < number(cfg["minimum_operating_equity_usdt"]):
            blockers.append("WAITING_FOR_FUNDS_OR_EQUITY_FLOOR")
        if state.get("global_entry_block_latched"):
            blockers.append("GLOBAL_PROTECTED_EQUITY_BLOCK")
        if position_mode != 0:
            blockers.append("POSITION_MODE_NOT_ONE_WAY")
        if unmanaged_positions:
            blockers.append("UNMANAGED_EXCHANGE_POSITION")
        if daily_loss_hit:
            blockers.append("DAILY_LOSS_LIMIT_1_PERCENT")
        if state.get("pending_entries"):
            blockers.append("PENDING_ENTRY_RECOVERY")
        if any(
            bool(row.get("closing"))
            or bool(row.get("settlement_pending_utc"))
            for row in live_positions.values()
        ):
            blockers.append("CLOSE_OR_SETTLEMENT_IN_PROGRESS")

        handled = (
            completed
            | ignored
            | set(skipped)
            | set(live_positions)
            | set(state.get("pending_entries", {}))
        )
        candidates = [
            row
            for trade_id, row in simulated.items()
            if trade_id not in handled
        ]
        candidates.sort(
            key=lambda row: str(row.get("source_opened_utc") or "")
        )

        contracts = contract_index(contract_rows(contracts_payload))
        bootstrapped_watches = bootstrap_recent_rejected_trade_watches(
            state, simulated, contracts, cfg, equity, regime_info
        )
        if bootstrapped_watches:
            log_event(
                cfg,
                "REJECTED_TRADE_WATCH_BOOTSTRAP",
                created=bootstrapped_watches,
            )
        strategy_counts = Counter(
            str(row.get("source_strategy"))
            for row in live_positions.values()
        )
        occupied_assets = {
            str(row.get("asset")): str(row.get("side"))
            for row in live_positions.values()
        }
        total_planned_risk = sum(
            number(row.get("actual_risk_usdt"))
            for row in live_positions.values()
        )

        for intent in candidates:
            trade_id = str(intent["source_trade_id"])
            strategy = str(intent.get("source_strategy", ""))
            asset = str(intent.get("asset", "")).upper()
            side = str(intent.get("side", "")).upper()

            reason: str | None = None
            regime_reason = regime_entry_block_reason(
                strategy, regime_info, cfg
            )

            if strategy not in set(cfg.get("strategies", [])):
                reason = "STRATEGY_NOT_ENABLED"
            elif blockers == ["WAITING_FOR_FUNDS_OR_EQUITY_FLOOR"]:
                # Finché il conto non è finanziato, conserva il segnale
                # solo per la finestra di freschezza configurata.
                continue
            if blockers:
                reason = "ENTRY_BLOCKED_" + "_".join(blockers)
            elif (
                strategy == "RSI5_RSI25_5X_WIDE"
                and state.get("rsi_entry_block_latched")
            ):
                reason = "RSI_STRATEGY_LATCHED"
            elif seconds_old(first_seen.get(trade_id)) > number(
                cfg["max_signal_age_seconds"]
            ):
                reason = "STALE_SIGNAL"
            elif regime_reason in {
                "REGIME_DATA_WAIT",
                "RSI_REGIME_DATA_WAIT",
            }:
                continue
            elif regime_reason is not None:
                reason = regime_reason
            elif (
                int(
                    STRATEGIES[strategy].get(
                        "max_open_positions",
                        0,
                    )
                ) > 0
                and strategy_counts[strategy] >= int(
                    STRATEGIES[strategy]["max_open_positions"]
                )
            ):
                reason = "MAX_POSITIONS_PER_STRATEGY"
            elif asset in occupied_assets:
                reason = (
                    "DUPLICATE_SAME_ASSET"
                    if occupied_assets[asset] == side
                    else "OPPOSITE_SAME_ASSET"
                )

            contract = choose_contract(asset, contracts)
            if reason is None and contract is None:
                reason = "NO_USDTM_CONTRACT"

            if reason is not None:
                skipped[trade_id] = {
                    "reason": reason,
                    "skipped_utc": iso_now(),
                }
                log_event(
                    cfg,
                    "LIVE_ENTRY_SKIPPED",
                    source_trade_id=trade_id,
                    source_strategy=strategy,
                    asset=asset,
                    reason=reason,
                )
                watch = add_rejected_trade_watch(
                    state, intent, contract, cfg, equity, reason, regime_info
                )
                if should_notify_rejected_entry(reason, cfg):
                    notify_once(
                        state,
                        f"rejected:{trade_id}",
                        format_rejected_trade_message(
                            intent, reason, account, state, cfg
                        ) + ("\nEsito teorico alla chiusura: in osservazione." if watch else ""),
                        timeout_seconds,
                    )
                continue

            try:
                plan = build_entry_plan(
                    intent,
                    contract,
                    cfg,
                    equity,
                    available_balance,
                )
            except LiveError as exc:
                skipped[trade_id] = {
                    "reason": str(exc),
                    "skipped_utc": iso_now(),
                }
                error_reason = str(exc)
                log_event(
                    cfg,
                    "LIVE_ENTRY_SKIPPED",
                    source_trade_id=trade_id,
                    source_strategy=strategy,
                    asset=asset,
                    reason=error_reason,
                )
                watch = add_rejected_trade_watch(
                    state, intent, contract, cfg, equity, error_reason, regime_info
                )
                if should_notify_rejected_entry(error_reason, cfg):
                    notify_once(
                        state,
                        f"rejected:{trade_id}",
                        format_rejected_trade_message(
                            intent, error_reason, account, state, cfg
                        ) + ("\nEsito teorico alla chiusura: in osservazione." if watch else ""),
                        timeout_seconds,
                    )
                continue

            maximum_total_risk = (
                number(cfg["operating_capital_usdt"])
                * number(cfg["max_total_open_risk_pct"])
                / 100.0
            )
            if (
                total_planned_risk + plan["actual_risk_usdt"]
                > maximum_total_risk + 1e-9
            ):
                risk_reason = "MAX_TOTAL_OPEN_RISK"
                skipped[trade_id] = {
                    "reason": risk_reason,
                    "skipped_utc": iso_now(),
                }
                log_event(
                    cfg,
                    "LIVE_ENTRY_SKIPPED",
                    source_trade_id=trade_id,
                    source_strategy=strategy,
                    asset=asset,
                    reason=risk_reason,
                )
                watch = add_rejected_trade_watch(
                    state, intent, contract, cfg, equity, risk_reason, regime_info
                )
                if should_notify_rejected_entry(risk_reason, cfg):
                    notify_once(
                        state,
                        f"rejected:{trade_id}",
                        format_rejected_trade_message(
                            intent, risk_reason, account, state, cfg
                        ) + ("\nEsito teorico alla chiusura: in osservazione." if watch else ""),
                        timeout_seconds,
                    )
                continue

            body = plan.pop("order_body")
            try:
                margin_guard = entry_margin_mode_guard(
                    body, cfg, creds, timeout_seconds
                )
            except (ApiError, LiveError) as exc:
                margin_reason = "MARGIN_MODE_AUTO_SWITCH_FAILED"
                skipped[trade_id] = {
                    "reason": margin_reason,
                    "detail": str(exc),
                    "skipped_utc": iso_now(),
                }
                log_event(
                    cfg,
                    "LIVE_ENTRY_SKIPPED",
                    source_trade_id=trade_id,
                    source_strategy=strategy,
                    asset=asset,
                    reason=margin_reason,
                    detail=str(exc),
                )
                watch = add_rejected_trade_watch(
                    state, intent, contract, cfg, equity, margin_reason, regime_info
                )
                if should_notify_rejected_entry(margin_reason, cfg):
                    notify_once(
                        state,
                        f"rejected:{trade_id}",
                        format_rejected_trade_message(
                            intent, margin_reason, account, state, cfg
                        ) + ("\nEsito teorico alla chiusura: in osservazione." if watch else ""),
                        timeout_seconds,
                    )
                continue

            plan["margin_mode_guard"] = margin_guard
            if margin_guard.get("changed"):
                log_event(
                    cfg,
                    "LIVE_MARGIN_MODE_SWITCHED",
                    source_trade_id=trade_id,
                    source_strategy=strategy,
                    asset=asset,
                    symbol=plan["symbol"],
                    before=margin_guard.get("before"),
                    after=margin_guard.get("after"),
                )

            state["pending_entries"][trade_id] = {
                "client_oid": plan["client_oid"],
                "prepared_utc": iso_now(),
                "plan": plan,
                "order_body": body,
            }
            atomic_json(state_path, state)

            existing = get_order_by_client_oid(
                plan["client_oid"], creds, timeout_seconds
            )
            if existing is None:
                response, margin_guard = submit_entry_order(
                    body, cfg, creds, timeout_seconds
                )
                plan["margin_mode_guard"] = margin_guard
                state["pending_entries"][trade_id]["plan"][
                    "margin_mode_guard"
                ] = margin_guard
                order_id = response.get("data", {}).get("orderId")
            else:
                order_id = existing.get("id") or existing.get("orderId")

            live = dict(plan)
            live["order_id"] = order_id
            live["submitted_utc"] = iso_now()
            live["closing"] = False
            live_positions[trade_id] = live
            state["pending_entries"].pop(trade_id, None)

            strategy_counts[strategy] += 1
            occupied_assets[asset] = side
            total_planned_risk += live["actual_risk_usdt"]
            available_balance = max(
                0.0, available_balance - live["margin_usdt"]
            )

            log_event(
                cfg,
                "LIVE_ENTRY_SUBMITTED",
                source_trade_id=trade_id,
                source_strategy=strategy,
                asset=asset,
                side=side,
                symbol=live["symbol"],
                contracts=live["contracts"],
                leverage=live["leverage"],
                risk_usdt=live["actual_risk_usdt"],
                margin_usdt=live["margin_usdt"],
                order_id=order_id,
            )
            notify_reliably_once(
                state,
                f"opened:{trade_id}",
                format_open_trade_message(
                    live, account, state, cfg
                ),
                timeout_seconds,
            )

        state["completed_source_trade_ids"] = sorted(completed)
        state["ignored_source_trade_ids"] = sorted(ignored)
        state["last_run_utc"] = iso_now()
        atomic_json(state_path, state)

        if equity < number(cfg["minimum_operating_equity_usdt"]):
            status = "ARMED_WAITING_FUNDS"
        elif state.get("global_entry_block_latched"):
            status = "GLOBAL_EQUITY_BLOCKED"
        elif blockers:
            status = "ARMED_BLOCKED"
        elif state.get("rsi_entry_block_latched"):
            status = "ARMED_ACTIVE_RSI_BLOCKED"
        else:
            status = "ARMED_ACTIVE"

        account_pnl = account_pnl_snapshot(account, state, cfg)
        report_positions = [
            exchange_position_snapshot(
                live,
                exchange_by_symbol.get(str(live.get("symbol"))),
            )
            for live in live_positions.values()
        ]
        rsi_stats = state.get("strategy_stats", {}).get(
            "RSI5_RSI25_5X_WIDE", {}
        )
        report = {
            "status": status,
            "generated_utc": iso_now(),
            "mode": cfg["mode"],
            "armed": True,
            "auto_start_on_funds": True,
            "strategies": list(cfg["strategies"]),
            "market_regime": regime_info,
            "strategy_entry_filters": {
                "SHADOW_SCANNER_TOP5_BTC": (
                    regime_entry_block_reason(
                        "SHADOW_SCANNER_TOP5_BTC", regime_info, cfg
                    )
                    or "ENABLED"
                ),
                "SHADOW_SCANNER_TOP5_LONG": "ENABLED",
                "RSI5_RSI25_5X_WIDE": (
                    "RSI_STRATEGY_LATCHED"
                    if state.get("rsi_entry_block_latched")
                    else (
                        regime_entry_block_reason(
                            "RSI5_RSI25_5X_WIDE",
                            regime_info,
                            cfg,
                        )
                        or "ENABLED"
                    )
                ),
            },
            "concurrency": {
                "max_positions_per_strategy": int(
                    cfg["max_positions_per_strategy"]
                ),
                "max_total_positions": int(cfg["max_total_positions"]),
                "same_asset_duplicate_allowed": False,
                "same_asset_opposite_allowed": False,
            },
            "account": {
                **account_pnl,
                "available_usdt": number(account.get("availableBalance")),
                "position_margin_usdt": number(
                    account.get("positionMargin")
                ),
                "order_margin_usdt": number(account.get("orderMargin")),
                "risk_ratio": number(account.get("riskRatio")),
            },
            "missed_trade_tracker": {
                "enabled": bool(cfg.get("track_rejected_trade_outcomes")),
                "open_watches": len(state.get("rejected_trade_watches", {})),
                "bootstrapped_this_run": bootstrapped_watches,
                "statistics": state.get("rejected_trade_watch_stats", {}),
                "recent_outcomes": state.get("rejected_trade_watch_history", [])[-10:],
                "funding_included": False,
            },
            "telegram_delivery": {
                "reliable_open_close_enabled": True,
                "pending_notifications": len(
                    state.get("telegram_outbox", {})
                    if isinstance(state.get("telegram_outbox"), dict)
                    else {}
                ),
                "statistics": state.get("telegram_delivery_stats", {}),
            },
            "margin_mode_guard": {
                "enabled": bool(cfg.get("auto_ensure_margin_mode")),
                "desired_mode": str(cfg.get("margin_mode")),
                "verify_attempts": int(
                    cfg.get("margin_mode_verify_attempts", 3)
                ),
                "verify_delay_seconds": number(
                    cfg.get("margin_mode_verify_delay_seconds"), 0.5
                ),
                "retry_once_on_330005": bool(
                    cfg.get("margin_mode_retry_on_330005")
                ),
            },
            "fixed_sizing": {
                "compounding_enabled": False,
                "compounding_base": "FIXED_OPERATING_CAPITAL",
                "profit_reinvestment_enabled": False,
                "operating_capital_usdt": number(
                    cfg["operating_capital_usdt"]
                ),
                "standard_risk_per_trade_pct": number(
                    cfg["risk_per_trade_pct"]
                ),
                "standard_risk_per_trade_usdt": (
                    number(cfg["operating_capital_usdt"])
                    * number(cfg["risk_per_trade_pct"])
                    / 100.0
                ),
                "rsi_max_margin_usdt": number(
                    cfg["rsi_max_margin_usdt"]
                ),
                "rsi_leverage": number(cfg["rsi_leverage"]),
                "max_total_open_risk_pct": number(
                    cfg["max_total_open_risk_pct"]
                ),
                "max_total_open_risk_usdt": (
                    number(cfg["operating_capital_usdt"])
                    * number(cfg["max_total_open_risk_pct"])
                    / 100.0
                ),
            },
            "capital_protection": {
                "latched": bool(
                    state.get("global_entry_block_latched")
                ),
                "reason": state.get("global_entry_block_reason"),
                "high_water_equity_usdt": number(
                    state.get("high_water_equity_usdt")
                ),
                "global_block_threshold_usdt": global_threshold,
                "max_drawdown_from_high_usdt": number(
                    cfg["global_max_drawdown_usdt"]
                ),
                "absolute_floor_usdt": number(
                    cfg["minimum_operating_equity_usdt"]
                ),
            },
            "rsi_guard": {
                "latched": bool(state.get("rsi_entry_block_latched")),
                "reason": state.get("rsi_entry_block_reason"),
                "max_consecutive_losses": int(
                    cfg["rsi_max_consecutive_losses"]
                ),
                "consecutive_losses": int(
                    rsi_stats.get("consecutive_losses", 0)
                ),
                "realized_pnl_usdt": number(
                    rsi_stats.get("realized_pnl_usdt")
                ),
                "closed_trades": int(rsi_stats.get("closed_trades", 0)),
            },
            "strategy_stats": state.get("strategy_stats", {}),
            "position_mode": position_mode,
            "blockers": blockers,
            "source_open_positions": len(simulated),
            "source_open_positions_by_strategy": dict(
                Counter(
                    str(row.get("source_strategy"))
                    for row in simulated.values()
                )
            ),
            "baseline_ignored_positions": len(ignored),
            "live_positions": report_positions,
            "unmanaged_exchange_positions": [
                {
                    "symbol": row.get("symbol"),
                    "quantity": row.get("_quantity"),
                    "side": row.get("_side"),
                }
                for row in unmanaged_positions
            ],
            "orders_capability_enabled": True,
            "transfers_capability_enabled": False,
            "withdrawals_capability_enabled": False,
        }
        write_report(cfg, report)
        return report

def reset_global_block(config_path: Path) -> dict[str, Any]:
    cfg = read_json(config_path)
    validate_config(cfg)
    state_path = Path(cfg["state_path"])
    state = read_json(state_path)
    if not isinstance(state, dict):
        raise LiveError("Stato live mancante.")
    if state.get("live_positions"):
        raise LiveError(
            "Non si può resettare il blocco globale con posizioni gestite."
        )
    state["global_entry_block_latched"] = False
    state["global_entry_block_reason"] = None
    state["global_entry_block_utc"] = None
    state["high_water_equity_usdt"] = number(
        state.get("previous_equity_usdt")
    )
    state["day_start_equity_usdt"] = number(
        state.get("previous_equity_usdt")
    )
    state["day_utc"] = utc_now().date().isoformat()
    state["global_entry_block_reset_utc"] = iso_now()
    atomic_json(state_path, state)
    return {
        "status": "GLOBAL_ENTRY_BLOCK_RESET",
        "generated_utc": iso_now(),
    }


def reset_rsi_block(config_path: Path) -> dict[str, Any]:
    cfg = read_json(config_path)
    validate_config(cfg)
    state_path = Path(cfg["state_path"])
    state = read_json(state_path)
    if not isinstance(state, dict):
        raise LiveError("Stato live mancante.")
    for live in state.get("live_positions", {}).values():
        if live.get("source_strategy") == "RSI5_RSI25_5X_WIDE":
            raise LiveError(
                "Non si può resettare la RSI con una posizione RSI aperta."
            )
    state["rsi_entry_block_latched"] = False
    state["rsi_entry_block_reason"] = None
    state["rsi_entry_block_utc"] = None
    stats = state.setdefault("strategy_stats", {}).setdefault(
        "RSI5_RSI25_5X_WIDE", {}
    )
    stats["consecutive_losses"] = 0
    state["rsi_entry_block_reset_utc"] = iso_now()
    atomic_json(state_path, state)
    return {
        "status": "RSI_ENTRY_BLOCK_RESET",
        "generated_utc": iso_now(),
        "rsi_realized_pnl_usdt": number(stats.get("realized_pnl_usdt")),
    }


def preflight(config_path: Path) -> dict[str, Any]:
    cfg = read_json(config_path)
    if not isinstance(cfg, dict):
        raise LiveError("Configurazione live mancante.")
    validate_config(cfg)
    validate_dry_run_config(cfg)
    paper_state = read_json(Path(cfg["paper_source_state_path"]), {})
    paper = normalize_paper_shadow_positions(
        paper_state, str(cfg["paper_source_account"])
    )
    rsi_state = read_json(Path(cfg["rsi_source_state_path"]), {})
    rsi = normalize_rsi_shadow_positions(
        rsi_state, str(cfg["rsi_source_account"])
    )
    return {
        "status": "PREFLIGHT_PASS",
        "generated_utc": iso_now(),
        "strategies": sorted(STRATEGIES),
        "scanner_top5_long_open_source_positions": len(paper),
        "rsi_open_source_positions": len(rsi),
        "rejected_trade_outcome_tracking": bool(
            cfg.get("track_rejected_trade_outcomes")
        ),
        "orders_sent": False,
    }


def self_test() -> dict[str, Any]:
    standard_intent = {
        "source_trade_id": "test-standard-long",
        "source_strategy": "SHADOW_SCANNER_TOP5_LONG",
        "asset": "SOL",
        "side": "LONG",
        "entry_price": 100,
        "stop_price": 95,
        "target_price": 110,
    }
    rsi_intent = {
        "source_trade_id": "test-rsi-long",
        "source_strategy": "RSI5_RSI25_5X_WIDE",
        "asset": "SOL",
        "side": "LONG",
        "entry_price": 100,
        "stop_price": 99.5,
        "target_price": 101,
    }
    contract = {
        "symbol": "SOLUSDTM",
        "baseCurrency": "SOL",
        "settleCurrency": "USDT",
        "markPrice": "100",
        "multiplier": "0.1",
        "lotSize": 1,
        "tickSize": "0.001",
        "maxLeverage": 50,
        "marketStage": "NORMAL",
        "marketMaxOrderQty": 1000000,
    }
    cfg = {
        "operating_capital_usdt": 3760.0,
        "margin_mode": "ISOLATED",
        "auto_ensure_margin_mode": True,
        "margin_mode_verify_attempts": 3,
        "margin_mode_verify_delay_seconds": 0.0,
        "margin_mode_retry_on_330005": True,
        "risk_per_trade_pct": 0.20,
        "max_position_margin_pct": 50.0,
        "available_margin_reserve_pct": 2.0,
        "max_entry_deviation_pct": 1.0,
        "rsi_max_margin_usdt": 500.0,
        "rsi_max_consecutive_losses": 3,
        "rsi_block_if_cumulative_pnl_negative": True,
        "minimum_operating_equity_usdt": 3500.0,
        "global_max_drawdown_usdt": 260.0,
        "balance_reset_change_pct": 20.0,
        "daily_loss_limit_enabled": False,
        "daily_loss_limit_pct": 1.0,
        "track_rejected_trade_outcomes": True,
        "reliable_open_close_telegram": True,
        "telegram_retry_outbox": True,
        "recovered_entries_notify": True,
        "hypothetical_taker_fee_rate": 0.0006,
        "hypothetical_breakeven_epsilon_usdt": 0.01,
        "hypothetical_history_limit": 500,
        "hypothetical_bootstrap_recent_skips_hours": 24.0,
        "hypothetical_close_csv_paths": [],
        "hypothetical_close_csv_globs": [],
    }

    plan_3800 = build_entry_plan(
        standard_intent,
        contract,
        cfg,
        equity=3800.0,
        available_balance=3800.0,
    )
    plan_10000 = build_entry_plan(
        standard_intent,
        contract,
        cfg,
        equity=10000.0,
        available_balance=10000.0,
    )
    rsi_plan = build_entry_plan(
        rsi_intent,
        contract,
        cfg,
        equity=3800.0,
        available_balance=3800.0,
    )

    assert abs(plan_3800["risk_budget_usdt"] - 15.0) < 1e-9
    assert plan_10000["contracts"] == plan_3800["contracts"]
    assert plan_3800["leverage"] == 2.0
    assert plan_3800["compounding_base"] == "FIXED_OPERATING_CAPITAL"
    assert rsi_plan["leverage"] == 5.0
    assert rsi_plan["margin_usdt"] <= 500.0 + 1e-9
    assert abs(rsi_plan["actual_risk_usdt"] - 12.5) < 1e-9

    rsi_source = normalize_rsi_shadow_positions(
        {
            "shadow_accounts": {
                "RSI5_RSI25_5X_WIDE": {
                    "open_positions": [
                        {
                            "trade_id": "rsi:1:SHADOW",
                            "direction": "LONG",
                            "asset": "SUI",
                            "entry_price": 1.0,
                            "stop_price": 0.995,
                            "target_price": 1.01,
                            "opened_at": "2026-07-21T00:00:00+00:00",
                        }
                    ]
                }
            }
        },
        "RSI5_RSI25_5X_WIDE",
    )
    assert rsi_source["rsi:1:SHADOW"]["source_strategy"] == (
        "RSI5_RSI25_5X_WIDE"
    )

    paper_source = normalize_paper_shadow_positions(
        {
            "portfolios": {
                "SHADOW_SCANNER_TOP5_LONG": {
                    "open_positions": [
                        {
                            "trade_id": "paper-1",
                            "asset": "NEAR",
                            "side": "LONG",
                            "entry_price": 5.0,
                            "stop_price": 4.8,
                            "target_price": 5.4,
                            "opened_at": "2026-07-21T00:00:00+00:00",
                        }
                    ]
                }
            }
        },
        "SHADOW_SCANNER_TOP5_LONG",
    )
    paper_id = "SHADOW_SCANNER_TOP5_LONG:paper-1"
    assert paper_source[paper_id]["source_strategy"] == (
        "SHADOW_SCANNER_TOP5_LONG"
    )

    state = initial_state([])
    state["high_water_equity_usdt"] = 10000.0
    state["previous_equity_usdt"] = 10000.0
    daily, threshold, hit = update_equity_baselines(
        state, 9740.0, False, cfg
    )
    assert daily is False
    assert threshold == 9740.0
    assert hit is True

    for pnl in (-5.0, -4.0, -3.0):
        stats = update_strategy_stats(
            state,
            "RSI5_RSI25_5X_WIDE",
            pnl,
            iso_now(),
            cfg,
        )
    assert stats["consecutive_losses"] == 3
    assert stats["realized_pnl_usdt"] == -12.0
    assert state["rsi_entry_block_latched"] is True

    combo_intent = {
        "source_trade_id": "SHADOW_COMBO_ADAPTIVE::combo-1",
        "source_strategy": "SHADOW_COMBO_ADAPTIVE",
        "asset": "HYPE",
        "side": "SHORT",
        "entry_price": 100.0,
        "stop_price": 102.0,
        "target_price": 96.0,
        "planned_leverage": 2.0,
        "planned_notional_usdt": 376.0,
        "planned_margin_usdt": 188.0,
    }
    combo_contract = dict(contract)
    combo_contract["symbol"] = "HYPEUSDTM"
    combo_contract["baseCurrency"] = "HYPE"
    combo_watch = build_hypothetical_watch(
        combo_intent,
        combo_contract,
        cfg,
        3760.0,
        "STRATEGY_NOT_ENABLED",
    )
    assert combo_watch["leverage"] == 2.0
    assert combo_watch["notional_usdt"] > 0
    positive = calculate_hypothetical_outcome(
        combo_watch,
        {
            "exit_price": 96.0,
            "close_reason": "TARGET",
            "closed_utc": iso_now(),
        },
        cfg,
    )
    assert positive["result"] == "POSITIVE"
    assert positive["estimated_net_pnl_usdt"] > 0
    negative = calculate_hypothetical_outcome(
        combo_watch,
        {
            "exit_price": 102.0,
            "close_reason": "STOP",
            "closed_utc": iso_now(),
        },
        cfg,
    )
    assert negative["result"] == "NEGATIVE"
    assert negative["estimated_net_pnl_usdt"] < 0
    close_row = {
        "intent_type": "CLOSE_DRY_RUN",
        "source_trade_id": "SHADOW_COMBO_ADAPTIVE::combo-1",
        "source_exit_price": "96.0",
        "source_net_pnl_eur": "12.5",
        "generated_utc": iso_now(),
        "reason": "source_position_closed",
    }
    assert _row_matches_watch(close_row, combo_watch)
    parsed_close = _close_record_from_row(close_row)
    assert parsed_close is not None
    assert parsed_close["exit_price"] == 96.0
    outcome_text = format_rejected_trade_outcome_message(
        combo_watch,
        positive,
        {
            "positive": 1,
            "negative": 0,
            "breakeven": 0,
            "estimated_net_pnl_usdt": positive["estimated_net_pnl_usdt"],
        },
    )
    assert "ESITO TRADE NON APERTO" in outcome_text
    assert "POSITIVO" in outcome_text
    assert "Nessun ordine reale" in outcome_text

    api_endpoints = {
        ACCOUNT_EP,
        POSITIONS_EP,
        POSITION_MODE_EP,
        CONTRACTS_EP,
        TPSL_EP,
        ORDER_EP,
        ORDER_BY_CLIENT_EP,
        STOP_ORDERS_EP,
        HISTORY_POSITIONS_EP,
        MARGIN_MODE_GET_EP,
        MARGIN_MODE_CHANGE_EP,
    }
    assert all(
        "transfer" not in value.lower()
        and "withdraw" not in value.lower()
        for value in api_endpoints
    )

    assert human_rejection_reason("STRATEGY_NOT_ENABLED") == (
        "strategia non abilitata nel conto live"
    )
    rejected_text = format_rejected_trade_message(
        {
            "source_strategy": "SHADOW_COMBO_ADAPTIVE",
            "asset": "HYPE",
            "side": "SHORT",
            "entry_price": 58.0,
            "stop_price": 59.0,
            "target_price": 56.0,
        },
        "STRATEGY_NOT_ENABLED",
        {"accountEquity": 3760.0, "availableBalance": 3760.0, "unrealisedPNL": 0.0},
        {"live_start_equity_usdt": 3760.0},
        cfg,
    )
    assert "TRADE NON APERTO" in rejected_text
    assert "Combo" not in rejected_text or "SHADOW_COMBO_ADAPTIVE" in rejected_text
    assert "strategia non abilitata" in rejected_text
    assert should_notify_rejected_entry("STRATEGY_NOT_ENABLED", cfg) is False
    assert add_rejected_trade_watch(
        {}, combo_intent, None, cfg, 3760.0,
        "STRATEGY_NOT_ENABLED", None
    ) is None

    duplicate_text = format_rejected_trade_message(
        {**combo_intent, "asset": "LAB", "side": "LONG"},
        "DUPLICATE_SAME_ASSET",
        {"accountEquity": 3760.0, "availableBalance": 3700.0},
        initial_state([]),
        cfg,
    )
    assert "posizione REALE LIVE su LAB LONG" in duplicate_text

    original_telegram_send = globals()["telegram_send"]
    try:
        attempts = {"count": 0}

        def fake_send(message: str, timeout: int) -> bool:
            attempts["count"] += 1
            return attempts["count"] >= 2

        globals()["telegram_send"] = fake_send
        delivery_state: dict[str, Any] = {
            "telegram_sent": [],
            "telegram_outbox": {},
        }
        assert notify_reliably_once(
            delivery_state, "opened:test", "test message", 1
        ) is False
        assert "opened:test" in delivery_state["telegram_outbox"]
        retry = flush_telegram_outbox(delivery_state, 1)
        assert retry["delivered"] == 1
        assert retry["pending"] == 0
        assert "opened:test" in delivery_state["telegram_sent"]
    finally:
        globals()["telegram_send"] = original_telegram_send

    original_signed_request = globals()["signed_request"]
    margin_calls: list[tuple[str, str, dict[str, Any] | None]] = []
    margin_modes = {"SOLUSDTM": "CROSS"}

    def fake_signed_request(
        method: str,
        endpoint: str,
        creds: dict[str, str],
        timeout_seconds: int,
        body: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        margin_calls.append((method, endpoint, body))
        if endpoint.startswith(MARGIN_MODE_GET_EP):
            symbol = urllib.parse.parse_qs(
                urllib.parse.urlsplit(endpoint).query
            )["symbol"][0]
            return {
                "code": "200000",
                "data": {
                    "symbol": symbol,
                    "marginMode": margin_modes[symbol],
                },
            }
        if endpoint == MARGIN_MODE_CHANGE_EP:
            assert body is not None
            margin_modes[str(body["symbol"])] = str(
                body["marginMode"]
            ).upper()
            return {
                "code": "200000",
                "data": {
                    "symbol": body["symbol"],
                    "marginMode": body["marginMode"],
                },
            }
        if endpoint == TPSL_EP:
            return {
                "code": "200000",
                "data": {"orderId": "test-order"},
            }
        raise AssertionError((method, endpoint, body))

    globals()["signed_request"] = fake_signed_request
    try:
        guard = ensure_symbol_margin_mode(
            "SOLUSDTM",
            "ISOLATED",
            {},
            20,
            verify_attempts=3,
            verify_delay_seconds=0.0,
        )
        assert guard["before"] == "CROSS"
        assert guard["after"] == "ISOLATED"
        assert guard["changed"] is True
        assert margin_modes["SOLUSDTM"] == "ISOLATED"

        margin_calls.clear()
        response, guarded = submit_entry_order(
            {
                "symbol": "SOLUSDTM",
                "marginMode": "ISOLATED",
            },
            cfg,
            {},
            20,
        )
        assert response["data"]["orderId"] == "test-order"
        assert guarded["verified"] is True
        assert not any(
            endpoint == MARGIN_MODE_CHANGE_EP
            for _, endpoint, _ in margin_calls
        )
    finally:
        globals()["signed_request"] = original_signed_request

    assert human_rejection_reason(
        "MARGIN_MODE_AUTO_SWITCH_FAILED"
    ) == (
        "impossibile impostare e verificare la modalità isolated del contratto"
    )

    return {
        "status": "PASS",
        "tests": 54,
        "strategies": sorted(STRATEGIES),
        "max_positions_per_strategy": 0,
        "max_total_positions": 0,
        "compounding_enabled": False,
        "operating_capital_usdt": 3760.0,
        "standard_risk_per_trade_usdt": 7.52,
        "rsi_max_margin_usdt": 500.0,
        "rsi_leverage": 5.0,
        "global_max_drawdown_usdt": 260.0,
        "auto_ensure_margin_mode": True,
        "margin_mode": "ISOLATED",
        "margin_mode_verify_attempts": 3,
        "margin_mode_retry_on_330005": True,
        "track_rejected_trade_outcomes": True,
        "reliable_open_close_telegram": True,
        "telegram_retry_outbox": True,
        "recovered_entries_notify": True,
        "existing_open_positions_backfill": True,
        "hypothetical_taker_fee_rate": 0.0006,
        "orders_capability_enabled": True,
        "transfers_capability_enabled": False,
        "withdrawals_capability_enabled": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--preflight", action="store_true")
    parser.add_argument("--reset-global-block", action="store_true")
    parser.add_argument("--reset-rsi-block", action="store_true")
    parser.add_argument(
        "--reset-kill-switch",
        action="store_true",
        help="Alias compatibile per --reset-global-block",
    )
    args = parser.parse_args()

    if args.self_test:
        result = self_test()
    elif args.preflight:
        result = preflight(Path(args.config))
    elif args.reset_rsi_block:
        result = reset_rsi_block(Path(args.config))
    elif args.reset_global_block or args.reset_kill_switch:
        result = reset_global_block(Path(args.config))
    else:
        result = run(Path(args.config))

    # Non stampare l’intero stato operativo: può contenere decine di MB.
    # Il risultato completo resta salvato nei file di stato/report.
    if isinstance(result, dict):
        summary = {}

        for key, value in result.items():
            if value is None or isinstance(value, (bool, int, float)):
                summary[key] = value
            elif isinstance(value, str):
                summary[key] = (
                    value
                    if len(value) <= 300
                    else value[:300] + "…"
                )
            elif isinstance(value, (list, tuple, set, dict)):
                summary[f"{key}_count"] = len(value)

        summary["top_level_key_count"] = len(result)
    else:
        summary = {
            "result_type": type(result).__name__,
        }

    print(
        json.dumps(
            summary,
            ensure_ascii=False,
            separators=(",", ":"),
            default=str,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
