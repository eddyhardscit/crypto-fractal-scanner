import csv
import re
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf
from tabulate import tabulate


REPORTS_DIR = Path("reports")

LATEST_REPORT_PATH = REPORTS_DIR / "latest_report.md"

REPORT_PATH = REPORTS_DIR / "module_signal_tracker_report.md"
REPORT_ALIAS_PATH = REPORTS_DIR / "module_signal_tracker.md"

GLOBAL_CONFLUENCE_METRICS_PATH = REPORTS_DIR / "global_confluence_metrics.csv"

HISTORY_CSV_PATH = REPORTS_DIR / "module_signal_tracker_history.csv"
METRICS_CSV_PATH = REPORTS_DIR / "module_signal_tracker_metrics.csv"

START_MARKER = "<!-- MODULE_ACCURACY_START -->"
END_MARKER = "<!-- MODULE_ACCURACY_END -->"

ASSETS = ["BTC", "SOL", "DOGE"]

TICKERS = {
    "BTC": "BTC-USD",
    "SOL": "SOL-USD",
    "DOGE": "DOGE-USD",
}

HORIZONS = [1, 3, 7, 14, 30, 60]

MODULES = [
    ("Global confluence", "global_score"),
    ("Scanner", "scanner_score"),
    ("Market regime", "market_score"),
    ("Tecnico", "technical_score_component"),
    ("Frattale SOL", "sol_fractal_score"),
]


def now_utc():
    return datetime.now(timezone.utc)


def now_utc_str():
    return now_utc().strftime("%Y-%m-%d %H:%M UTC")


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def clean_cell(value) -> str:
    if value is None:
        return ""

    s = str(value).strip()
    s = s.replace("**", "")
    s = s.replace("`", "")
    s = s.replace("\xa0", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def parse_number(value, default=np.nan):
    if value is None:
        return default

    s = str(value).strip()

    if not s or s.lower() in {"n/a", "nan", "none", "null", "-"}:
        return default

    match = re.search(r"[-+]?\d[\d\s.,]*", s)

    if not match:
        return default

    token = match.group(0).replace(" ", "")

    if "," in token:
        token = token.replace(".", "").replace(",", ".")
    elif "." in token:
        parts = token.split(".")
        if (
            len(parts) == 2
            and len(parts[1]) == 3
            and len(parts[0]) <= 3
            and parts[0] != "0"
        ):
            token = parts[0] + parts[1]

    try:
        return float(token)
    except Exception:
        return default


def parse_int(value, default=0):
    v = parse_number(value, default=np.nan)

    if pd.isna(v):
        return default

    try:
        return int(v)
    except Exception:
        return default


def parse_bool_nullable(value):
    if value is None:
        return np.nan

    if isinstance(value, bool):
        return value

    if isinstance(value, (int, float)) and not pd.isna(value):
        if int(value) == 1:
            return True
        if int(value) == 0:
            return False

    s = str(value).strip().lower()

    if s in {"true", "1", "yes", "si", "sì", "checked"}:
        return True

    if s in {"false", "0", "no", "unchecked", "n/a", "nan", "none", ""}:
        return False

    return np.nan


def fmt_score(value):
    try:
        value = int(value)
    except Exception:
        value = 0

    if value > 0:
        return f"+{value}"

    return str(value)


def fmt_pct(value, decimals=2, signed=False):
    if value is None or pd.isna(value):
        return "n/a"

    sign = "+" if signed and value > 0 else ""
    return f"{sign}{value:.{decimals}f}%".replace(".", ",")


def fmt_price(asset: str, value):
    if value is None or pd.isna(value):
        return "n/a"

    v = float(value)

    if asset == "DOGE":
        return f"{v:.5f}"

    s = f"{v:,.2f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def parse_date(value):
    if value is None or pd.isna(value):
        return pd.NaT

    try:
        ts = pd.to_datetime(value, errors="coerce")

        if pd.isna(ts):
            return pd.NaT

        if getattr(ts, "tzinfo", None) is not None:
            try:
                ts = ts.tz_convert(None)
            except Exception:
                ts = ts.tz_localize(None)

        return pd.Timestamp(ts).normalize()

    except Exception:
        return pd.NaT


def normalize_ohlcv(df):
    if df is None or df.empty:
        return pd.DataFrame()

    out = df.copy()

    if isinstance(out.columns, pd.MultiIndex):
        fields = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]

        level0 = list(out.columns.get_level_values(0))
        level1 = list(out.columns.get_level_values(1))

        if any(field in level0 for field in fields):
            tmp = {}

            for field in fields:
                if field in level0:
                    part = out.xs(field, axis=1, level=0)
                    tmp[field] = part.iloc[:, 0]

            out = pd.DataFrame(tmp)

        elif any(field in level1 for field in fields):
            tmp = {}

            for field in fields:
                if field in level1:
                    part = out.xs(field, axis=1, level=1)
                    tmp[field] = part.iloc[:, 0]

            out = pd.DataFrame(tmp)

    if "Close" not in out.columns:
        return pd.DataFrame()

    for col in ["Open", "High", "Low"]:
        if col not in out.columns:
            out[col] = out["Close"]

    if "Volume" not in out.columns:
        out["Volume"] = np.nan

    out = out[["Open", "High", "Low", "Close", "Volume"]].copy()
    out.index = pd.to_datetime(out.index, errors="coerce")

    try:
        out.index = out.index.tz_convert(None)
    except Exception:
        try:
            out.index = out.index.tz_localize(None)
        except Exception:
            pass

    out.index = out.index.normalize()
    out = out[~out.index.duplicated(keep="last")]
    out = out.sort_index()
    out = out.dropna(subset=["Close"])

    return out


def download_prices(ticker: str):
    try:
        raw = yf.download(
            ticker,
            period="max",
            interval="1d",
            progress=False,
            auto_adjust=False,
            actions=False,
            threads=False,
        )
        return normalize_ohlcv(raw)

    except Exception as e:
        print(f"Download fallito per {ticker}: {e}")
        return pd.DataFrame()


def close_on_or_after(df: pd.DataFrame, date):
    if df is None or df.empty:
        return np.nan, pd.NaT

    date = parse_date(date)

    if pd.isna(date):
        return np.nan, pd.NaT

    sliced = df[df.index >= date].copy()

    if sliced.empty:
        return np.nan, pd.NaT

    actual_date = pd.Timestamp(sliced.index[0]).normalize()
    actual_price = parse_number(sliced.iloc[0]["Close"])

    return actual_price, actual_date


def period_stats(df: pd.DataFrame, start_date, end_date, start_price):
    if df is None or df.empty or pd.isna(start_price) or start_price == 0:
        return np.nan, np.nan

    start_date = parse_date(start_date)
    end_date = parse_date(end_date)

    if pd.isna(start_date) or pd.isna(end_date):
        return np.nan, np.nan

    sliced = df[(df.index >= start_date) & (df.index <= end_date)].copy()

    if sliced.empty:
        return np.nan, np.nan

    max_high = parse_number(sliced["High"].max())
    min_low = parse_number(sliced["Low"].min())

    max_gain = (max_high / start_price - 1) * 100 if not pd.isna(max_high) else np.nan
    drawdown = (min_low / start_price - 1) * 100 if not pd.isna(min_low) else np.nan

    return drawdown, max_gain


def read_csv_dicts(path: Path):
    if not path.exists():
        return []

    try:
        with path.open("r", encoding="utf-8", newline="") as f:
            return list(csv.DictReader(f))
    except Exception:
        return []


def read_global_metrics():
    rows = read_csv_dicts(GLOBAL_CONFLUENCE_METRICS_PATH)

    if not rows:
        raise RuntimeError(
            "module_signal_tracker.py: global_confluence_metrics.csv non trovato o vuoto. "
            "Esegui prima global_confluence_report.py."
        )

    out = {}

    for row in rows:
        asset = clean_cell(row.get("asset") or row.get("Asset")).upper()

        if asset not in ASSETS:
            continue

        out[asset] = {
            "asset": asset,
            "global_score": parse_int(
                row.get("global_score")
                or row.get("score")
                or row.get("total_score")
                or row.get("Punteggio"),
                0,
            ),
            "scanner_score": parse_int(row.get("scanner_score"), 0),
            "market_score": parse_int(row.get("market_score"), 0),
            "technical_score_component": parse_int(
                row.get("technical_score_component")
                or row.get("technical_score")
                or row.get("Tecnico"),
                0,
            ),
            "sol_fractal_score": parse_int(
                row.get("sol_fractal_score")
                or row.get("fractal_score")
                or row.get("Frattale"),
                0,
            ),
            "fractal_path_score": parse_int(row.get("fractal_path_score"), 0),
            "rsi_score": parse_int(row.get("rsi_score"), 0),
            "lifecycle_score_component": parse_int(row.get("lifecycle_score_component"), 0),
            "futures_score": parse_int(row.get("futures_score"), 0),
            "daily_change_score": parse_int(row.get("daily_change_score"), 0),
            "action": clean_cell(row.get("action") or row.get("Azione coerente")),
            "confluence": clean_cell(row.get("confluence") or row.get("Confluenza")),
            "bias": clean_cell(row.get("bias") or row.get("Bias")),
        }

    missing = [asset for asset in ASSETS if asset not in out]

    if missing:
        raise RuntimeError(
            "module_signal_tracker.py: asset mancanti in global_confluence_metrics.csv: "
            + ", ".join(missing)
        )

    return out


def normalize_history_columns(df: pd.DataFrame):
    if df is None or df.empty:
        return pd.DataFrame()

    out = df.copy()

    rename_map = {
        "date": "signal_date",
        "Data": "signal_date",
        "Asset": "asset",
        "Prezzo": "price",
        "Global": "global_score",
        "global": "global_score",
        "Scanner": "scanner_score",
        "Market": "market_score",
        "Tecnico": "technical_score_component",
        "technical_score": "technical_score_component",
        "Frattale": "sol_fractal_score",
        "fractal_score": "sol_fractal_score",
        "Azione": "action",
    }

    for old, new in rename_map.items():
        if old in out.columns and new not in out.columns:
            out = out.rename(columns={old: new})

    required = [
        "signal_date",
        "asset",
        "ticker",
        "price",
        "global_score",
        "scanner_score",
        "market_score",
        "technical_score_component",
        "sol_fractal_score",
        "fractal_path_score",
        "rsi_score",
        "lifecycle_score_component",
        "futures_score",
        "daily_change_score",
        "action",
        "confluence",
        "bias",
    ]

    for col in required:
        if col not in out.columns:
            out[col] = np.nan

    out["asset"] = out["asset"].astype(str).str.upper().str.strip()

    out["signal_date"] = pd.to_datetime(out["signal_date"], errors="coerce")
    out["signal_date"] = out["signal_date"].dt.strftime("%Y-%m-%d")

    for col in [
        "price",
        "global_score",
        "scanner_score",
        "market_score",
        "technical_score_component",
        "sol_fractal_score",
        "fractal_path_score",
        "rsi_score",
        "lifecycle_score_component",
        "futures_score",
        "daily_change_score",
    ]:
        out[col] = out[col].map(lambda x: parse_number(x, np.nan))

    for col in [
        "global_score",
        "scanner_score",
        "market_score",
        "technical_score_component",
        "sol_fractal_score",
        "fractal_path_score",
        "rsi_score",
        "lifecycle_score_component",
        "futures_score",
        "daily_change_score",
    ]:
        out[col] = out[col].fillna(0).astype(int)

    return out


def load_history():
    if not HISTORY_CSV_PATH.exists():
        return pd.DataFrame()

    try:
        df = pd.read_csv(HISTORY_CSV_PATH)
    except Exception:
        return pd.DataFrame()

    return normalize_history_columns(df)


def build_today_signals(global_metrics, prices_by_asset):
    rows = []

    for asset in ASSETS:
        df = prices_by_asset.get(asset, pd.DataFrame())

        if df.empty:
            price = np.nan
            signal_date = pd.Timestamp(now_utc().date())
        else:
            signal_date = pd.Timestamp(df.index[-1]).normalize()
            price = parse_number(df.iloc[-1]["Close"])

        g = global_metrics[asset]

        rows.append(
            {
                "signal_date": signal_date.strftime("%Y-%m-%d"),
                "asset": asset,
                "ticker": TICKERS[asset],
                "price": price,
                "global_score": int(g["global_score"]),
                "scanner_score": int(g["scanner_score"]),
                "market_score": int(g["market_score"]),
                "technical_score_component": int(g["technical_score_component"]),
                "sol_fractal_score": int(g["sol_fractal_score"]),
                "fractal_path_score": int(g["fractal_path_score"]),
                "rsi_score": int(g["rsi_score"]),
                "lifecycle_score_component": int(g["lifecycle_score_component"]),
                "futures_score": int(g["futures_score"]),
                "daily_change_score": int(g["daily_change_score"]),
                "action": g.get("action", ""),
                "confluence": g.get("confluence", ""),
                "bias": g.get("bias", ""),
                "created_at_utc": now_utc().isoformat(),
            }
        )

    return pd.DataFrame(rows)


def append_today_signals(history: pd.DataFrame, today_signals: pd.DataFrame):
    history = normalize_history_columns(history)
    today_signals = normalize_history_columns(today_signals)

    if history.empty:
        return today_signals.copy()

    key_today = set(
        zip(
            today_signals["signal_date"].astype(str),
            today_signals["asset"].astype(str),
        )
    )

    keep_mask = []

    for _, row in history.iterrows():
        key = (str(row.get("signal_date")), str(row.get("asset")))
        keep_mask.append(key not in key_today)

    history = history[keep_mask].copy()

    combined = pd.concat([history, today_signals], ignore_index=True)
    combined = combined.sort_values(["signal_date", "asset"]).reset_index(drop=True)

    return combined


def ensure_horizon_columns(out: pd.DataFrame):
    """
    Fix importante:
    Pandas/GitHub Actions può creare target_date_1d e actual_date_1d come float64
    se inizializzati con np.nan. Poi quando scriviamo '2026-07-10' esplode.

    Quindi:
    - colonne data = object/string
    - colonne checked = bool
    - colonne numeriche = float
    """

    for h in HORIZONS:
        date_cols = [
            f"target_date_{h}d",
            f"actual_date_{h}d",
        ]

        numeric_cols = [
            f"actual_price_{h}d",
            f"return_pct_{h}d",
            f"drawdown_pct_{h}d",
            f"max_gain_pct_{h}d",
        ]

        checked_col = f"checked_{h}d"

        for col in date_cols:
            if col not in out.columns:
                out[col] = ""
            out[col] = out[col].astype("object")

        for col in numeric_cols:
            if col not in out.columns:
                out[col] = np.nan
            out[col] = pd.to_numeric(out[col], errors="coerce")

        if checked_col not in out.columns:
            out[checked_col] = False
        out[checked_col] = out[checked_col].map(parse_bool_nullable).fillna(False).astype(bool)

    return out


def update_checks(history: pd.DataFrame, prices_by_asset):
    if history is None or history.empty:
        return pd.DataFrame()

    out = history.copy()
    out = ensure_horizon_columns(out)

    for idx, row in out.iterrows():
        asset = str(row.get("asset")).upper()
        df = prices_by_asset.get(asset, pd.DataFrame())

        if df.empty:
            continue

        signal_date = parse_date(row.get("signal_date"))
        price = parse_number(row.get("price"), np.nan)

        if pd.isna(signal_date) or pd.isna(price) or price == 0:
            continue

        latest_available = pd.Timestamp(df.index[-1]).normalize()

        for h in HORIZONS:
            checked_col = f"checked_{h}d"

            checked = parse_bool_nullable(out.at[idx, checked_col])

            if checked is True:
                continue

            target_date = signal_date + pd.Timedelta(days=h)

            # Ora questa colonna è object, quindi la stringa non rompe più Pandas.
            out.at[idx, f"target_date_{h}d"] = target_date.strftime("%Y-%m-%d")

            if target_date > latest_available:
                out.at[idx, checked_col] = False
                continue

            actual_price, actual_date = close_on_or_after(df, target_date)

            if pd.isna(actual_price) or pd.isna(actual_date):
                out.at[idx, checked_col] = False
                continue

            return_pct = (actual_price / price - 1) * 100
            drawdown_pct, max_gain_pct = period_stats(df, signal_date, actual_date, price)

            out.at[idx, f"actual_date_{h}d"] = actual_date.strftime("%Y-%m-%d")
            out.at[idx, f"actual_price_{h}d"] = actual_price
            out.at[idx, f"return_pct_{h}d"] = return_pct
            out.at[idx, f"drawdown_pct_{h}d"] = drawdown_pct
            out.at[idx, f"max_gain_pct_{h}d"] = max_gain_pct
            out.at[idx, checked_col] = True

    out = out.sort_values(["signal_date", "asset"]).reset_index(drop=True)
    out = ensure_horizon_columns(out)

    return out


def directional_correct(signal_score, return_pct):
    signal_score = parse_number(signal_score, 0)
    return_pct = parse_number(return_pct, np.nan)

    if pd.isna(return_pct):
        return np.nan

    if signal_score > 0:
        return bool(return_pct > 0)

    if signal_score < 0:
        return bool(return_pct < 0)

    return np.nan


def module_status(count):
    count = int(count)

    if count < 30:
        return "RACCOLTA DATI"

    if count < 60:
        return "OSSERVAZIONE 30+"

    if count < 100:
        return "CALIBRAZIONE UTILE"

    return "PESO VALUTABILE"


def build_latest_signals_table(history: pd.DataFrame):
    if history is None or history.empty:
        return pd.DataFrame()

    data = history.copy()
    data["signal_dt"] = pd.to_datetime(data["signal_date"], errors="coerce")
    data = data.sort_values(["signal_dt", "asset"]).tail(12).copy()

    rows = []

    for _, row in data.iterrows():
        asset = row["asset"]

        rows.append(
            {
                "Data": row["signal_date"],
                "Asset": asset,
                "Prezzo": fmt_price(asset, row["price"]),
                "Global": fmt_score(row["global_score"]),
                "Scanner": fmt_score(row["scanner_score"]),
                "Market": fmt_score(row["market_score"]),
                "Tecnico": fmt_score(row["technical_score_component"]),
                "Frattale": fmt_score(row["sol_fractal_score"]),
                "Azione": clean_cell(row["action"]),
            }
        )

    return pd.DataFrame(rows)


def build_check_status_table(history: pd.DataFrame):
    rows = []

    for asset in ASSETS:
        d = history[history["asset"] == asset].copy()

        row = {
            "Asset": asset,
            "Segnali salvati": len(d),
        }

        for h in HORIZONS:
            checked_col = f"checked_{h}d"

            if checked_col not in d.columns:
                count = 0
            else:
                checked_mask = d[checked_col].map(parse_bool_nullable).fillna(False).astype(bool)
                count = int(checked_mask.sum())

            row[f"{h}g controllati"] = count

        rows.append(row)

    return pd.DataFrame(rows)


def build_accuracy_table(history: pd.DataFrame):
    rows = []

    for asset in ASSETS:
        asset_df = history[history["asset"] == asset].copy()

        for h in HORIZONS:
            checked_col = f"checked_{h}d"
            return_col = f"return_pct_{h}d"
            drawdown_col = f"drawdown_pct_{h}d"
            max_gain_col = f"max_gain_pct_{h}d"

            if checked_col not in asset_df.columns:
                checked = pd.DataFrame()
            else:
                checked_mask = asset_df[checked_col].map(parse_bool_nullable).fillna(False).astype(bool)
                checked = asset_df[checked_mask].copy()

            for module_name, module_col in MODULES:
                if module_col not in checked.columns or return_col not in checked.columns:
                    module_checked = pd.DataFrame()
                else:
                    module_checked = checked[
                        checked[module_col].map(lambda x: parse_number(x, 0) != 0)
                    ].copy()

                if module_checked.empty:
                    rows.append(
                        {
                            "Asset": asset,
                            "Orizzonte": f"{h}g",
                            "Modulo": module_name,
                            "Controlli": 0,
                            "Accuratezza direzione": "n/a",
                            "Return medio": "n/a",
                            "Drawdown medio": "n/a",
                            "Max gain medio": "n/a",
                            "Stato": "RACCOLTA DATI",
                        }
                    )
                    continue

                correct_values = []

                for _, r in module_checked.iterrows():
                    correct = directional_correct(r.get(module_col), r.get(return_col))
                    if not pd.isna(correct):
                        correct_values.append(bool(correct))

                if correct_values:
                    accuracy = sum(correct_values) / len(correct_values) * 100
                    accuracy_text = fmt_pct(accuracy, signed=False)
                else:
                    accuracy_text = "n/a"

                returns = pd.to_numeric(module_checked[return_col], errors="coerce")
                drawdowns = pd.to_numeric(module_checked[drawdown_col], errors="coerce")
                max_gains = pd.to_numeric(module_checked[max_gain_col], errors="coerce")

                count = int(len(correct_values))

                rows.append(
                    {
                        "Asset": asset,
                        "Orizzonte": f"{h}g",
                        "Modulo": module_name,
                        "Controlli": count,
                        "Accuratezza direzione": accuracy_text,
                        "Return medio": fmt_pct(returns.mean(), signed=True),
                        "Drawdown medio": fmt_pct(drawdowns.mean(), signed=True),
                        "Max gain medio": fmt_pct(max_gains.mean(), signed=True),
                        "Stato": module_status(count),
                    }
                )

    return pd.DataFrame(rows)


def df_to_markdown(df: pd.DataFrame):
    if df is None or df.empty:
        return "_Nessun dato disponibile._"

    return tabulate(df, headers="keys", tablefmt="pipe", showindex=False)


def build_report(history: pd.DataFrame):
    generated = now_utc_str()

    latest_table = build_latest_signals_table(history)
    check_status_table = build_check_status_table(history)
    accuracy_table = build_accuracy_table(history)

    signal_count = len(history) if history is not None else 0

    report = f"""{START_MARKER}
# Accuratezza moduli / autocalibrazione allargata

Generato: {generated}

Questo report salva ogni giorno i segnali dei moduli e controlla, dopo vari orizzonti, quali moduli stanno davvero aiutando.

Moduli controllati:

- Global Confluence
- Scanner grezzo
- Market regime
- Struttura tecnica
- Frattale SOL/BTC, solo per SOL

Orizzonti controllati: 1, 3, 7, 14, 30 e 60 giorni.

Segnali totali salvati: **{signal_count}**.

## Ultimi segnali salvati

{df_to_markdown(latest_table)}

## Stato controlli

{df_to_markdown(check_status_table)}

## Accuratezza direzionale per modulo

{df_to_markdown(accuracy_table)}

## Come leggerlo

- Prima di 30 controlli per asset/modulo, è solo raccolta dati.
- Dopo 30 controlli, il modulo può iniziare a dare una calibrazione leggera.
- Dopo 60 controlli, la lettura diventa più utile.
- Dopo 100+ controlli, i pesi dei moduli possono essere regolati con più fiducia.

Questo report non cambia ancora automaticamente i pesi del Global Confluence. Serve prima a capire quali moduli funzionano davvero.

Nota tecnica: questo file ora legge i punteggi reali da **global_confluence_metrics.csv** e forza le colonne data come testo. Quindi non deve più dare errore `Invalid value '2026-07-10' for dtype 'float64'`.
{END_MARKER}
"""

    return report


def replace_block_in_latest(latest_text: str, block_text: str):
    if START_MARKER in latest_text and END_MARKER in latest_text:
        pattern = re.compile(
            re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
            flags=re.DOTALL,
        )
        return pattern.sub(block_text.rstrip(), latest_text)

    insert_after = "<!-- CALIBRATION_READABLE_END -->"

    if insert_after in latest_text:
        idx = latest_text.index(insert_after) + len(insert_after)
        return latest_text[:idx] + "\n\n" + block_text.rstrip() + "\n" + latest_text[idx:]

    return latest_text.rstrip() + "\n\n" + block_text.rstrip() + "\n"


def write_metrics(accuracy_df: pd.DataFrame):
    if accuracy_df is None or accuracy_df.empty:
        return

    METRICS_CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    accuracy_df.to_csv(METRICS_CSV_PATH, index=False)


def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    global_metrics = read_global_metrics()

    prices_by_asset = {}

    for asset in ASSETS:
        prices_by_asset[asset] = download_prices(TICKERS[asset])

    old_history = load_history()
    today_signals = build_today_signals(global_metrics, prices_by_asset)

    history = append_today_signals(old_history, today_signals)
    history = update_checks(history, prices_by_asset)

    history.to_csv(HISTORY_CSV_PATH, index=False)

    accuracy_df = build_accuracy_table(history)
    write_metrics(accuracy_df)

    report_text = build_report(history)

    write_text(REPORT_PATH, report_text)
    write_text(REPORT_ALIAS_PATH, report_text)

    latest_text = read_text(LATEST_REPORT_PATH)
    latest_updated = replace_block_in_latest(latest_text, report_text)
    write_text(LATEST_REPORT_PATH, latest_updated)

    print(f"Module Signal Tracker scritto in: {REPORT_PATH}")
    print(f"Alias scritto in: {REPORT_ALIAS_PATH}")
    print(f"History CSV scritto in: {HISTORY_CSV_PATH}")
    print(f"Metrics CSV scritto in: {METRICS_CSV_PATH}")
    print(f"Latest report aggiornato: {LATEST_REPORT_PATH}")

    latest = today_signals.sort_values("asset")

    for _, row in latest.iterrows():
        print(
            f"{row['asset']}: "
            f"Global {fmt_score(row['global_score'])} | "
            f"Scanner {fmt_score(row['scanner_score'])} | "
            f"Market {fmt_score(row['market_score'])} | "
            f"Tecnico {fmt_score(row['technical_score_component'])} | "
            f"Frattale {fmt_score(row['sol_fractal_score'])}"
        )


if __name__ == "__main__":
    main()
