# -*- coding: utf-8 -*-
"""Evaluate saved exchange-microstructure signals at 1/3/7/14/30 days.

The tracker never rewrites the first daily signal snapshot. It only fills matured
outcomes and produces calibration metrics used by the prediction overlay and by
the Global weight-calibration workflow.
"""

from __future__ import annotations

import math
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


REPORTS_DIR = Path("reports")
LATEST_REPORT = REPORTS_DIR / "latest_report.md"
HISTORY_PATH = REPORTS_DIR / "exchange_microstructure_history.csv"
METRICS_PATH = REPORTS_DIR / "exchange_signal_tracker_metrics.csv"
REPORT_PATH = REPORTS_DIR / "exchange_signal_tracker_report.md"

START_MARKER = "<!-- EXCHANGE_SIGNAL_TRACKER_START -->"
END_MARKER = "<!-- EXCHANGE_SIGNAL_TRACKER_END -->"

ASSETS = ("BTC", "SOL", "DOGE")
TICKERS = {"BTC": "BTC-USD", "SOL": "SOL-USD", "DOGE": "DOGE-USD"}
HORIZONS = (1, 3, 7, 14, 30)


BASE_COLUMNS = [
    "signal_date",
    "asset",
    "price",
    "raw_score",
    "candidate_global_score",
    "global_score",
    "global_activation_status",
    "bias",
    "confidence",
    "data_coverage",
    "exchange_count",
    "bullish_consensus_count",
    "bearish_consensus_count",
    "divergent_metric_count",
    "funding_rate_pct",
    "basis_pct",
    "price_change_24h_pct",
    "open_interest_usd_combined",
    "oi_change_4h_pct",
    "oi_change_24h_pct",
    "global_long_short_ratio",
    "top_position_long_short_ratio",
    "taker_buy_sell_ratio_4h",
    "taker_buy_sell_ratio_24h",
    "orderbook_imbalance_0_5pct",
    "orderbook_imbalance_1_0pct",
    "long_liquidation_usd_sample",
    "short_liquidation_usd_sample",
    "liquidation_events_sample",
    "scanner_positive_rate_30d",
    "scanner_return_p50_30d",
    "overlay_status",
    "overlay_weight",
    "adjusted_positive_rate_30d",
    "adjusted_return_p50_30d",
    "created_utc",
]


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def utc_now_text() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def safe_float(value: Any, default=np.nan):
    try:
        number = float(value)
        return number if np.isfinite(number) else default
    except (TypeError, ValueError):
        return default


def safe_int(value: Any, default=0) -> int:
    number = safe_float(value)
    return int(number) if not pd.isna(number) else default


def safe_str(value: Any, default="") -> str:
    if value is None:
        return default
    try:
        if pd.isna(value):
            return default
    except Exception:
        pass
    text = str(value).strip()
    return text if text and text.lower() not in {"nan", "none", "null"} else default


def parse_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return safe_str(value).lower() in {"true", "1", "yes", "y", "si", "sì"}


def horizon_columns(h: int) -> list[str]:
    return [
        f"target_date_{h}d",
        f"checked_{h}d",
        f"actual_date_{h}d",
        f"actual_price_{h}d",
        f"return_{h}d",
        f"drawdown_{h}d",
        f"max_gain_{h}d",
    ]


def all_columns() -> list[str]:
    columns = list(BASE_COLUMNS)
    for h in HORIZONS:
        columns.extend(horizon_columns(h))
    return columns


def ensure_columns(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for column in all_columns():
        if column not in out.columns:
            if column.startswith("checked_"):
                out[column] = False
            else:
                out[column] = ""
    return out[all_columns()]


def load_history() -> pd.DataFrame:
    if not HISTORY_PATH.exists():
        return ensure_columns(pd.DataFrame())
    try:
        return ensure_columns(pd.read_csv(HISTORY_PATH, dtype=str))
    except Exception:
        return ensure_columns(pd.DataFrame())


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8", newline="\n")
    tmp.replace(path)


def download_prices() -> dict[str, pd.DataFrame]:
    try:
        import yfinance as yf
    except Exception:
        return {asset: pd.DataFrame() for asset in ASSETS}

    result: dict[str, pd.DataFrame] = {}
    today = datetime.now(timezone.utc).date()
    start = today - timedelta(days=150)
    end = today + timedelta(days=2)
    for asset, ticker in TICKERS.items():
        try:
            df = yf.download(
                ticker,
                start=start.isoformat(),
                end=end.isoformat(),
                interval="1d",
                progress=False,
                auto_adjust=False,
                threads=False,
            )
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = [column[0] for column in df.columns]
            if not df.empty:
                df.index = pd.to_datetime(df.index).tz_localize(None)
                result[asset] = df[[column for column in ("Open", "High", "Low", "Close") if column in df.columns]].copy()
            else:
                result[asset] = pd.DataFrame()
        except Exception:
            result[asset] = pd.DataFrame()
    return result


def first_index_on_or_after(df: pd.DataFrame, target: datetime.date):
    if df.empty:
        return None
    candidates = df.index[df.index >= pd.Timestamp(target)]
    return candidates[0] if len(candidates) else None


def update_outcomes(history: pd.DataFrame, prices: dict[str, pd.DataFrame]) -> tuple[pd.DataFrame, int]:
    hist = ensure_columns(history)
    updated = 0
    today = datetime.now(timezone.utc).date()

    for idx, row in hist.iterrows():
        asset = safe_str(row.get("asset")).upper()
        if asset not in ASSETS:
            continue
        try:
            signal_date = pd.to_datetime(row.get("signal_date")).date()
        except Exception:
            continue
        signal_price = safe_float(row.get("price"))
        if pd.isna(signal_price) or signal_price <= 0:
            continue
        df = prices.get(asset, pd.DataFrame())
        if df.empty:
            continue

        for h in HORIZONS:
            checked_col = f"checked_{h}d"
            if parse_bool(row.get(checked_col)):
                continue
            target_date = signal_date + timedelta(days=h)
            hist.at[idx, f"target_date_{h}d"] = target_date.isoformat()
            if target_date > today:
                continue
            actual_index = first_index_on_or_after(df, target_date)
            if actual_index is None:
                continue
            start_index = first_index_on_or_after(df, signal_date)
            if start_index is None or actual_index < start_index:
                continue
            window = df.loc[start_index:actual_index]
            if window.empty or "Close" not in window.columns:
                continue
            actual_price = safe_float(window["Close"].iloc[-1])
            min_low = safe_float(window["Low"].min()) if "Low" in window.columns else np.nan
            max_high = safe_float(window["High"].max()) if "High" in window.columns else np.nan
            if pd.isna(actual_price):
                continue
            ret = (actual_price / signal_price - 1.0) * 100.0
            drawdown = (min_low / signal_price - 1.0) * 100.0 if not pd.isna(min_low) else np.nan
            max_gain = (max_high / signal_price - 1.0) * 100.0 if not pd.isna(max_high) else np.nan

            hist.at[idx, checked_col] = True
            hist.at[idx, f"actual_date_{h}d"] = actual_index.date().isoformat()
            hist.at[idx, f"actual_price_{h}d"] = actual_price
            hist.at[idx, f"return_{h}d"] = ret
            hist.at[idx, f"drawdown_{h}d"] = drawdown
            hist.at[idx, f"max_gain_{h}d"] = max_gain
            updated += 1

    return ensure_columns(hist), updated


def direction_correct(score: float, ret: float) -> bool:
    if score > 0:
        return ret > 0
    if score < 0:
        return ret < 0
    return False


def metric_status(controls: int) -> str:
    if controls >= 100:
        return "SOLIDO"
    if controls >= 60:
        return "UTILE"
    if controls >= 30:
        return "PRIMA CALIBRAZIONE"
    if controls > 0:
        return "FEEDBACK RAPIDO"
    return "RACCOLTA DATI"


def build_metrics(history: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for asset in ASSETS:
        asset_df = history[history["asset"].astype(str).str.upper() == asset].copy()
        for h in HORIZONS:
            checked = asset_df[asset_df[f"checked_{h}d"].map(parse_bool)].copy()
            checked["candidate_score_num"] = pd.to_numeric(checked["candidate_global_score"], errors="coerce").fillna(0)
            checked["return_num"] = pd.to_numeric(checked[f"return_{h}d"], errors="coerce")
            checked["drawdown_num"] = pd.to_numeric(checked[f"drawdown_{h}d"], errors="coerce")
            checked["max_gain_num"] = pd.to_numeric(checked[f"max_gain_{h}d"], errors="coerce")
            active = checked[(checked["candidate_score_num"] != 0) & checked["return_num"].notna()].copy()
            controls = len(active)
            if controls:
                correct = int(
                    active.apply(
                        lambda row: direction_correct(float(row["candidate_score_num"]), float(row["return_num"])),
                        axis=1,
                    ).sum()
                )
                accuracy = correct / controls * 100.0
                signed_return = active.apply(
                    lambda row: float(row["return_num"])
                    if float(row["candidate_score_num"]) > 0
                    else -float(row["return_num"]),
                    axis=1,
                )
                avg_signed = float(signed_return.mean())
                avg_return = float(active["return_num"].mean())
                avg_drawdown = float(active["drawdown_num"].mean())
                avg_max_gain = float(active["max_gain_num"].mean())
            else:
                correct = 0
                accuracy = np.nan
                avg_signed = np.nan
                avg_return = np.nan
                avg_drawdown = np.nan
                avg_max_gain = np.nan

            rows.append(
                {
                    "generated_utc": utc_now_iso(),
                    "asset": asset,
                    "horizon_days": h,
                    "horizon": f"{h}g",
                    "controls": controls,
                    "correct": correct,
                    "accuracy_direction_pct": accuracy,
                    "avg_return_pct": avg_return,
                    "avg_direction_adjusted_return_pct": avg_signed,
                    "avg_drawdown_pct": avg_drawdown,
                    "avg_max_gain_pct": avg_max_gain,
                    "status": metric_status(controls),
                    "module_key": "exchange_microstructure",
                    "module": "Microstruttura exchange",
                    "calibration_role": "CALIBRABILE",
                    "calibratable": True,
                    "parent_family": "",
                }
            )
    return pd.DataFrame(rows)


def fmt_pct(value: Any, decimals=2) -> str:
    number = safe_float(value)
    if pd.isna(number):
        return "n/a"
    return f"{float(number):+.{decimals}f}%".replace(".", ",")


def fmt_price(asset: Any, value: Any) -> str:
    number = safe_float(value)
    if pd.isna(number):
        return "n/a"
    asset_text = safe_str(asset).upper()
    if asset_text == "BTC":
        return f"{float(number):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    if asset_text == "DOGE":
        return f"{float(number):.5f}"
    return f"{float(number):.2f}".replace(".", ",")


def fmt_number(value: Any, decimals: int = 2) -> str:
    number = safe_float(value)
    if pd.isna(number):
        return "n/a"
    return f"{float(number):.{decimals}f}".replace(".", ",")


def md_table(headers: list[str], rows: list[list[str]]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    lines.extend("| " + " | ".join(str(cell).replace("|", "/") for cell in row) + " |" for row in rows)
    return "\n".join(lines)


def render(history: pd.DataFrame, metrics: pd.DataFrame, updated: int) -> str:
    latest_rows: list[list[str]] = []
    if not history.empty:
        latest = history.copy()
        latest["signal_date_sort"] = pd.to_datetime(latest["signal_date"], errors="coerce")
        latest = latest.sort_values(["signal_date_sort", "asset"], ascending=[False, True]).head(9)
        for _, row in latest.iterrows():
            latest_rows.append(
                [
                    safe_str(row.get("signal_date")),
                    safe_str(row.get("asset")),
                    fmt_price(row.get("asset"), row.get("price")),
                    str(safe_int(row.get("candidate_global_score"))),
                    str(safe_int(row.get("global_score"))),
                    fmt_number(row.get("raw_score"), 2),
                    safe_str(row.get("confidence")),
                    fmt_number(row.get("taker_buy_sell_ratio_4h"), 2),
                    fmt_pct(row.get("oi_change_24h_pct")),
                    fmt_pct((safe_float(row.get("orderbook_imbalance_0_5pct")) or 0.0) * 100.0),
                ]
            )

    metric_rows: list[list[str]] = []
    for _, row in metrics.iterrows():
        metric_rows.append(
            [
                safe_str(row["asset"]),
                safe_str(row["horizon"]),
                str(safe_int(row["controls"])),
                fmt_pct(row["accuracy_direction_pct"]),
                fmt_pct(row["avg_direction_adjusted_return_pct"]),
                fmt_pct(row["avg_drawdown_pct"]),
                fmt_pct(row["avg_max_gain_pct"]),
                safe_str(row["status"]),
            ]
        )

    lines = [
        "# Accuratezza dati exchange e microstruttura",
        "",
        f"Generato: {utc_now_text()}",
        "",
        "Questo tracker verifica se il segnale candidato exchange ±1 anticipa correttamente la direzione del prezzo a 1/3/7/14/30 giorni.",
        "Il peso Global resta 0 finché l'orizzonte 7g non ha almeno 30 controlli, accuratezza almeno 55% e return corretto direzione positivo. L'overlay a 30g ha un gate separato.",
        "",
        f"Controlli maturati completati in questa esecuzione: **{updated}**.",
        "",
        "## Ultime fotografie giornaliere",
        "",
        md_table(
            ["Data", "Asset", "Prezzo", "Candidato", "Peso Global", "Score raw", "Confidenza", "Taker 4h", "OI 24h", "Book 0,5%"],
            latest_rows,
        )
        if latest_rows
        else "_Nessuna fotografia exchange ancora salvata._",
        "",
        "## Accuratezza direzionale",
        "",
        md_table(
            ["Asset", "Orizzonte", "Controlli", "Accuratezza", "Return corretto direzione", "Drawdown medio", "Max gain medio", "Stato"],
            metric_rows,
        ),
        "",
        "## Regole",
        "",
        "- Sotto 30 controlli: solo raccolta dati; il segnale candidato non pesa nel Global.",
        "- Da 30 controlli a 7g: il peso Global può attivarsi soltanto con accuratezza almeno 55% e return corretto direzione positivo.",
        "- Da 30 controlli a 30g: l'overlay può attivarsi soltanto con accuratezza almeno 55%.",
        "- Da 60 controlli: la lettura diventa più utile.",
        "- Da 100 controlli: possibile revisione seria del peso ±1.",
        "- Se l'accuratezza scende sotto 45%, l'overlay viene sospeso, non invertito automaticamente.",
        "",
    ]
    return "\n".join(lines).rstrip() + "\n"


def inject(report: str) -> None:
    if not LATEST_REPORT.exists():
        atomic_write_text(LATEST_REPORT, f"{START_MARKER}\n{report.rstrip()}\n{END_MARKER}\n")
        return
    old = LATEST_REPORT.read_text(encoding="utf-8")
    block = f"{START_MARKER}\n{report.rstrip()}\n{END_MARKER}"
    if START_MARKER in old and END_MARKER in old:
        pattern = re.compile(re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER), re.DOTALL)
        new = pattern.sub(block, old, count=1)
    else:
        exchange_end = "<!-- EXCHANGE_MICROSTRUCTURE_END -->"
        if exchange_end in old:
            new = old.replace(exchange_end, exchange_end + "\n\n" + block, 1)
        else:
            anchor = "<!-- LIQUIDATION_SUMMARY_START -->"
            new = old.replace(anchor, block + "\n\n" + anchor, 1) if anchor in old else old.rstrip() + "\n\n" + block + "\n"
    atomic_write_text(LATEST_REPORT, new)


def main() -> None:
    history = load_history()
    if history.empty:
        metrics = build_metrics(history)
        metrics.to_csv(METRICS_PATH, index=False)
        report = render(history, metrics, 0)
        atomic_write_text(REPORT_PATH, report)
        inject(report)
        print("Exchange tracker: history non ancora disponibile; creato stato raccolta dati.")
        return

    prices = download_prices()
    history, updated = update_outcomes(history, prices)
    history.to_csv(HISTORY_PATH, index=False)
    metrics = build_metrics(history)
    metrics.to_csv(METRICS_PATH, index=False)
    report = render(history, metrics, updated)
    atomic_write_text(REPORT_PATH, report)
    inject(report)

    print(f"Exchange signal tracker scritto in: {REPORT_PATH}")
    print(f"Metriche tracker scritte in: {METRICS_PATH}")
    print(f"Outcomes aggiornati: {updated}")


if __name__ == "__main__":
    main()
