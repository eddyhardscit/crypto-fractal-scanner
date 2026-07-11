import csv
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf


REPORTS_DIR = Path("reports")
LATEST_REPORT_PATH = REPORTS_DIR / "latest_report.md"

REPORT_PATH = REPORTS_DIR / "module_signal_tracker_report.md"
SHORT_REPORT_PATH = REPORTS_DIR / "module_signal_tracker.md"
HISTORY_CSV_PATH = REPORTS_DIR / "module_signal_tracker_history.csv"
METRICS_CSV_PATH = REPORTS_DIR / "module_signal_tracker_metrics.csv"

GLOBAL_METRICS_CSV_PATH = REPORTS_DIR / "global_confluence_metrics.csv"

START_MARKER = "<!-- MODULE_ACCURACY_START -->"
END_MARKER = "<!-- MODULE_ACCURACY_END -->"

ASSETS = ["BTC", "SOL", "DOGE"]

TICKERS = {
    "BTC": "BTC-USD",
    "SOL": "SOL-USD",
    "DOGE": "DOGE-USD",
}

# Controlli giornalieri più ravvicinati.
# 1/2/3g = feedback rapido
# 5/7/10g = feedback settimanale
# 14/21g = swing
# 30/45/60g = calibrazione più seria
HORIZONS = [1, 2, 3, 5, 7, 10, 14, 21, 30, 45, 60]

# Una sola fotografia per data + asset. La prima esecuzione del giorno viene
# congelata; eventuali rerun possono soltanto completare campi realmente vuoti.
DAILY_SIGNAL_POLICY = "KEEP_FIRST_SNAPSHOT"

# Ruoli:
# - benchmark: aggregato finale da osservare, non è un peso interno da modificare;
# - calibratable: modulo reale il cui peso potrà essere valutato in futuro;
# - diagnostic: dato utile per capire l'origine del segnale, ma già incluso
#   in una famiglia e quindi non deve ricevere un peso separato.
MODULES = [
    {
        "key": "global",
        "label": "Global confluence",
        "score_col": "global_score",
        "role": "BENCHMARK",
        "calibratable": False,
        "parent_family": "",
    },
    {
        "key": "statistical_family",
        "label": "Famiglia statistica",
        "score_col": "statistical_family_score",
        "role": "CALIBRABILE",
        "calibratable": True,
        "parent_family": "",
    },
    {
        "key": "scanner",
        "label": "Scanner grezzo",
        "score_col": "scanner_score",
        "role": "DIAGNOSTICO",
        "calibratable": False,
        "parent_family": "statistical_family",
    },
    {
        "key": "market",
        "label": "Market regime grezzo",
        "score_col": "market_score",
        "role": "DIAGNOSTICO",
        "calibratable": False,
        "parent_family": "statistical_family",
    },
    {
        "key": "technical",
        "label": "Tecnico",
        "score_col": "technical_score_component",
        "role": "CALIBRABILE",
        "calibratable": True,
        "parent_family": "",
    },
    {
        "key": "classic_technical",
        "label": "Classic technical",
        "score_col": "classic_technical_score_component",
        "role": "CALIBRABILE",
        "calibratable": True,
        "parent_family": "",
    },
    {
        "key": "exchange_microstructure",
        "label": "Microstruttura exchange",
        "score_col": "exchange_candidate_score_component",
        "role": "CALIBRABILE / NON PESATO FINO AL GATE",
        "calibratable": True,
        "parent_family": "",
    },
    {
        "key": "sol_fractal",
        "label": "Frattale SOL",
        "score_col": "sol_fractal_score",
        "role": "CALIBRABILE",
        "calibratable": True,
        "parent_family": "",
    },
]

BASE_HISTORY_COLUMNS = [
    "signal_date",
    "asset",
    "ticker",
    "price",
    "action",
    "confluence",
    "bias",
    "reliability",
    "global_score",
    "statistical_family_score",
    "statistical_family_reason",
    "statistical_family_source",
    "scanner_score",
    "market_score",
    "market_matches",
    "technical_score_component",
    "classic_technical_score_component",
    "exchange_flow_score_component",
    "exchange_candidate_score_component",
    "exchange_global_activation_status",
    "exchange_count",
    "exchange_kucoin_available",
    "exchange_raw_score",
    "exchange_confidence",
    "sol_fractal_score",
    "classic_technical_raw_score",
    "classic_technical_verdict",
    "classic_technical_risk",
    "classic_technical_stage",
    "classic_technical_structure",
    "classic_technical_wyckoff",
    "sol_fractal_verdict",
    "sol_fractal_similarity",
    "sol_fractal_tracking",
    "created_utc",
    "updated_utc",
]


def now_utc_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def now_utc_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def replace_or_insert_block(text: str, block: str) -> str:
    full_block = f"{START_MARKER}\n{block.rstrip()}\n{END_MARKER}"

    if START_MARKER in text and END_MARKER in text:
        pattern = re.compile(
            re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
            flags=re.DOTALL,
        )
        return pattern.sub(full_block, text)

    global_weight_start = "<!-- GLOBAL_WEIGHT_CALIBRATION_START -->"
    if global_weight_start in text:
        return text.replace(global_weight_start, full_block + "\n\n" + global_weight_start, 1)

    decision_end = "<!-- DECISION_REPORT_END -->"
    if decision_end in text:
        return text.replace(decision_end, decision_end + "\n\n" + full_block, 1)

    return text.rstrip() + "\n\n" + full_block + "\n"


def safe_float(value, default=np.nan):
    try:
        if value is None:
            return default
        if isinstance(value, str):
            s = value.strip()
            if not s or s.lower() in {"nan", "none", "n/a", "null"}:
                return default
            s = s.replace("%", "").replace("$", "").replace(" ", "")
            if "," in s:
                s = s.replace(".", "").replace(",", ".")
            return float(s)
        if pd.isna(value):
            return default
        return float(value)
    except Exception:
        return default


def safe_int(value, default=0) -> int:
    v = safe_float(value, np.nan)
    if pd.isna(v):
        return default
    return int(v)


def safe_str(value, default="") -> str:
    if value is None:
        return default
    try:
        if pd.isna(value):
            return default
    except Exception:
        pass
    return str(value)


def is_blank_value(value) -> bool:
    """Riconosce soltanto valori realmente mancanti, senza confondere 0/False con vuoto."""
    if value is None:
        return True

    if isinstance(value, str):
        return value.strip().lower() in {"", "nan", "none", "n/a", "null"}

    try:
        return bool(pd.isna(value))
    except Exception:
        return False


def parse_bool(value) -> bool:
    if isinstance(value, bool):
        return value
    s = safe_str(value).strip().lower()
    return s in {"true", "1", "yes", "y", "si", "sì"}


def fmt_signed_int(value) -> str:
    if value is None or pd.isna(value):
        return "0"
    v = int(value)
    if v > 0:
        return f"+{v}"
    return str(v)


def fmt_pct(value, decimals: int = 2) -> str:
    if value is None or pd.isna(value):
        return "n/a"
    return f"{float(value):+.{decimals}f}%".replace(".", ",")


def fmt_pct_plain(value, decimals: int = 2) -> str:
    if value is None or pd.isna(value):
        return "n/a"
    return f"{float(value):.{decimals}f}%".replace(".", ",")


def fmt_price(asset: str, value) -> str:
    if value is None or pd.isna(value):
        return "n/a"

    v = float(value)

    if asset == "BTC":
        return f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    if asset == "DOGE":
        return f"{v:.5f}"

    return f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def md_table(headers, rows) -> str:
    out = []
    out.append("| " + " | ".join(headers) + " |")
    out.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for row in rows:
        out.append("| " + " | ".join(str(x) for x in row) + " |")
    return "\n".join(out)


def first_present(row: dict, keys):
    for key in keys:
        value = row.get(key)
        if value is None:
            continue
        if isinstance(value, str) and not value.strip():
            continue
        return value
    return None


def same_sign(a: int, b: int) -> bool:
    return (a > 0 and b > 0) or (a < 0 and b < 0)


def derive_statistical_family_score(scanner_score, market_score, market_matches=None):
    """
    Replica la logica prudente del Global Confluence:
    - Scanner è il segnale principale;
    - Market Regime può aggiungere al massimo 1 punto;
    - il bonus richiede almeno 10 match e concordanza di segno;
    - la famiglia resta limitata a ±4;
    - Market non crea da solo un segnale se Scanner è neutro.
    """
    scanner = max(-3, min(3, safe_int(scanner_score, 0)))
    market = max(-3, min(3, safe_int(market_score, 0)))

    matches_value = safe_float(market_matches, np.nan)
    matches = None if pd.isna(matches_value) else int(matches_value)

    family = scanner

    if scanner == 0:
        reason = "Scanner neutro: Market Regime resta diagnostico e non crea da solo il segnale."
    elif matches is None:
        reason = "Match regime non disponibili: la famiglia usa soltanto il punteggio Scanner."
    elif matches < 10:
        reason = (
            f"Match regime {matches}: sotto 10, quindi nessun bonus; "
            "la famiglia usa il punteggio Scanner."
        )
    elif same_sign(scanner, market):
        family += 1 if scanner > 0 else -1
        reason = (
            f"Scanner e Market Regime concordi con {matches} match: "
            "bonus massimo di 1 punto."
        )
    elif market == 0:
        reason = "Market Regime neutro: resta il punteggio Scanner."
    else:
        reason = "Scanner e Market Regime non concordi: nessun bonus alla famiglia statistica."

    family = max(-4, min(4, family))
    return family, reason


def statistical_family_from_global_row(row: dict):
    scanner_score = safe_int(row.get("scanner_score"), 0)
    market_score = safe_int(row.get("market_score"), 0)

    market_matches = first_present(
        row,
        [
            "market_matches",
            "market_regime_matches",
            "statistical_family_market_matches",
            "market_match_count",
        ],
    )

    exact_score = first_present(
        row,
        [
            "statistical_family_score",
            "statistical_family_score_component",
            "statistics_family_score",
            "stat_family_score",
            "family_statistical_score",
        ],
    )

    exact_reason = first_present(
        row,
        [
            "statistical_family_reason",
            "statistics_family_reason",
            "stat_family_reason",
            "family_statistical_reason",
        ],
    )

    if exact_score is not None:
        return (
            max(-4, min(4, safe_int(exact_score, 0))),
            safe_str(exact_reason) or "Punteggio letto direttamente dal Global Confluence.",
            "GLOBAL_METRICS",
            safe_float(market_matches),
        )

    derived_score, derived_reason = derive_statistical_family_score(
        scanner_score,
        market_score,
        market_matches,
    )
    return derived_score, derived_reason, "DERIVED_FALLBACK", safe_float(market_matches)


def horizon_columns(h: int):
    suffix = f"{h}d"
    return [
        f"target_date_{suffix}",
        f"checked_{suffix}",
        f"actual_date_{suffix}",
        f"actual_price_{suffix}",
        f"return_{suffix}",
        f"drawdown_{suffix}",
        f"max_gain_{suffix}",
    ]


def all_history_columns():
    cols = list(BASE_HISTORY_COLUMNS)
    for h in HORIZONS:
        cols.extend(horizon_columns(h))
    return cols


def ensure_history_columns(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    for col in BASE_HISTORY_COLUMNS:
        if col not in out.columns:
            out[col] = ""

    for h in HORIZONS:
        suffix = f"{h}d"

        text_cols = [
            f"target_date_{suffix}",
            f"actual_date_{suffix}",
        ]
        bool_cols = [
            f"checked_{suffix}",
        ]
        num_cols = [
            f"actual_price_{suffix}",
            f"return_{suffix}",
            f"drawdown_{suffix}",
            f"max_gain_{suffix}",
        ]

        for col in text_cols:
            if col not in out.columns:
                out[col] = ""
            out[col] = out[col].astype("object")

        for col in bool_cols:
            if col not in out.columns:
                out[col] = False
            out[col] = out[col].map(parse_bool).astype(bool)

        for col in num_cols:
            if col not in out.columns:
                out[col] = np.nan
            out[col] = pd.to_numeric(out[col], errors="coerce")

    numeric_base_cols = [
        "price",
        "global_score",
        "statistical_family_score",
        "scanner_score",
        "market_score",
        "market_matches",
        "technical_score_component",
        "classic_technical_score_component",
        "sol_fractal_score",
        "classic_technical_raw_score",
        "sol_fractal_similarity",
    ]

    for col in numeric_base_cols:
        if col not in out.columns:
            out[col] = np.nan
        out[col] = pd.to_numeric(out[col], errors="coerce")

    for col in [
        "signal_date",
        "asset",
        "ticker",
        "action",
        "confluence",
        "bias",
        "reliability",
        "statistical_family_reason",
        "statistical_family_source",
        "created_utc",
        "updated_utc",
    ]:
        if col not in out.columns:
            out[col] = ""
        out[col] = out[col].astype("object")

    return out[all_history_columns()]


def normalize_yfinance_df(df: pd.DataFrame) -> pd.DataFrame:
    if df is None or df.empty:
        return pd.DataFrame()

    out = df.copy()

    if isinstance(out.columns, pd.MultiIndex):
        out.columns = [c[0] for c in out.columns]

    rename = {}
    for c in out.columns:
        cl = str(c).strip().lower()
        if cl == "open":
            rename[c] = "Open"
        elif cl == "high":
            rename[c] = "High"
        elif cl == "low":
            rename[c] = "Low"
        elif cl == "close":
            rename[c] = "Close"
        elif cl == "adj close":
            rename[c] = "Adj Close"
        elif cl == "volume":
            rename[c] = "Volume"

    out = out.rename(columns=rename)

    required = ["Open", "High", "Low", "Close"]
    for col in required:
        if col not in out.columns:
            return pd.DataFrame()

    if "Volume" not in out.columns:
        out["Volume"] = 0

    out = out[["Open", "High", "Low", "Close", "Volume"]].copy()
    out = out.dropna(subset=["Open", "High", "Low", "Close"])

    out.index = pd.to_datetime(out.index).tz_localize(None)
    out = out.sort_index()

    return out


def download_price_data():
    data = {}

    for asset, ticker in TICKERS.items():
        try:
            df = yf.download(
                ticker,
                period="900d",
                interval="1d",
                auto_adjust=False,
                progress=False,
                threads=False,
            )
            data[asset] = normalize_yfinance_df(df)
        except Exception:
            data[asset] = pd.DataFrame()

    return data


def read_global_metrics_rows():
    if not GLOBAL_METRICS_CSV_PATH.exists():
        return []

    try:
        with GLOBAL_METRICS_CSV_PATH.open("r", newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
    except Exception:
        return []

    latest_by_asset = {}

    for row in rows:
        asset = safe_str(row.get("asset")).upper().strip()
        if asset in ASSETS:
            latest_by_asset[asset] = row

    return [latest_by_asset[a] for a in ASSETS if a in latest_by_asset]


def load_history() -> pd.DataFrame:
    if not HISTORY_CSV_PATH.exists():
        return ensure_history_columns(pd.DataFrame())

    try:
        df = pd.read_csv(HISTORY_CSV_PATH, dtype=str)
    except Exception:
        return ensure_history_columns(pd.DataFrame())

    return ensure_history_columns(df)


def backfill_prudent_statistical_family(history: pd.DataFrame):
    """
    Completa soltanto le vecchie righe create prima dell'introduzione della
    Famiglia statistica.

    Regola prudente:
    - non modifica righe che hanno già source/reason della famiglia;
    - non inventa il numero storico di match del Market Regime;
    - usa quindi il solo Scanner grezzo, limitato a +/-3;
    - Market resta diagnostico e non riceve un bonus retroattivo;
    - conserva tutti i controlli 1g/2g/... già maturati.

    Ritorna il DataFrame aggiornato e il numero di righe completate.
    """
    out = ensure_history_columns(history)

    if out.empty:
        return out, 0

    backfilled = 0
    updated = now_utc_iso()

    for idx, row in out.iterrows():
        source = safe_str(row.get("statistical_family_source")).strip()
        reason = safe_str(row.get("statistical_family_reason")).strip()
        existing_score = safe_float(row.get("statistical_family_score"), np.nan)

        # Una riga già prodotta dal nuovo tracker non va mai reinterpretata.
        if source or reason:
            continue

        # Se esiste già un punteggio storico esplicito non nullo, lo conserva
        # e aggiunge soltanto i metadati mancanti.
        if not pd.isna(existing_score) and int(existing_score) != 0:
            preserved = max(-4, min(4, int(existing_score)))
            out.at[idx, "statistical_family_score"] = preserved
            out.at[idx, "statistical_family_reason"] = (
                "Punteggio storico già presente: conservato senza ricalcolo retroattivo."
            )
            out.at[idx, "statistical_family_source"] = "BACKFILL_PRESERVED_EXISTING"
            out.at[idx, "updated_utc"] = updated
            backfilled += 1
            continue

        scanner = max(-3, min(3, safe_int(row.get("scanner_score"), 0)))

        out.at[idx, "statistical_family_score"] = scanner
        out.at[idx, "statistical_family_reason"] = (
            "Backfill prudente: usato soltanto Scanner grezzo; numero storico "
            "dei match Market Regime non disponibile, quindi nessun bonus retroattivo."
        )
        out.at[idx, "statistical_family_source"] = "BACKFILL_PRUDENTE_SCANNER_ONLY"
        out.at[idx, "updated_utc"] = updated
        backfilled += 1

    return ensure_history_columns(out), backfilled


def build_signal_rows(global_rows, price_data):
    created = now_utc_iso()
    out_rows = []

    for row in global_rows:
        asset = safe_str(row.get("asset")).upper().strip()
        if asset not in ASSETS:
            continue

        ticker = TICKERS[asset]
        df = price_data.get(asset, pd.DataFrame())

        if df is not None and not df.empty:
            signal_date = df.index[-1].strftime("%Y-%m-%d")
            price = float(df["Close"].iloc[-1])
        else:
            generated = safe_str(row.get("generated_utc"))
            try:
                signal_date = pd.to_datetime(generated).date().isoformat()
            except Exception:
                signal_date = datetime.now(timezone.utc).date().isoformat()
            price = np.nan

        family_score, family_reason, family_source, market_matches = statistical_family_from_global_row(row)

        signal = {
            "signal_date": signal_date,
            "asset": asset,
            "ticker": ticker,
            "price": price,
            "action": safe_str(row.get("action")),
            "confluence": safe_str(row.get("confluence")),
            "bias": safe_str(row.get("bias")),
            "reliability": safe_str(row.get("reliability")),
            "global_score": safe_int(row.get("global_score", row.get("score")), 0),
            "statistical_family_score": family_score,
            "statistical_family_reason": family_reason,
            "statistical_family_source": family_source,
            "scanner_score": safe_int(row.get("scanner_score"), 0),
            "market_score": safe_int(row.get("market_score"), 0),
            "market_matches": market_matches,
            "technical_score_component": safe_int(row.get("technical_score_component"), 0),
            "classic_technical_score_component": safe_int(row.get("classic_technical_score_component"), 0),
            "exchange_flow_score_component": safe_int(row.get("exchange_flow_score_component"), 0),
            "exchange_candidate_score_component": safe_int(row.get("exchange_candidate_score_component"), 0),
            "exchange_global_activation_status": safe_str(row.get("exchange_global_activation_status")),
            "exchange_count": safe_int(row.get("exchange_count"), 0),
            "exchange_kucoin_available": safe_str(row.get("exchange_kucoin_available")),
            "exchange_raw_score": safe_float(row.get("exchange_raw_score")),
            "exchange_confidence": safe_str(row.get("exchange_confidence")),
            "sol_fractal_score": safe_int(row.get("sol_fractal_score"), 0),
            "classic_technical_raw_score": safe_float(row.get("classic_technical_raw_score")),
            "classic_technical_verdict": safe_str(row.get("classic_technical_verdict")),
            "classic_technical_risk": safe_str(row.get("classic_technical_risk")),
            "classic_technical_stage": safe_str(row.get("classic_technical_stage")),
            "classic_technical_structure": safe_str(row.get("classic_technical_structure")),
            "classic_technical_wyckoff": safe_str(row.get("classic_technical_wyckoff")),
            "sol_fractal_verdict": safe_str(row.get("sol_fractal_verdict")),
            "sol_fractal_similarity": safe_float(row.get("sol_fractal_similarity")),
            "sol_fractal_tracking": safe_str(row.get("sol_fractal_tracking")),
            "created_utc": created,
            "updated_utc": created,
        }

        for h in HORIZONS:
            target = pd.to_datetime(signal_date).date() + timedelta(days=h)
            signal[f"target_date_{h}d"] = target.isoformat()
            signal[f"checked_{h}d"] = False
            signal[f"actual_date_{h}d"] = ""
            signal[f"actual_price_{h}d"] = np.nan
            signal[f"return_{h}d"] = np.nan
            signal[f"drawdown_{h}d"] = np.nan
            signal[f"max_gain_{h}d"] = np.nan

        out_rows.append(signal)

    return out_rows


def upsert_today_signals(history: pd.DataFrame, new_rows) -> pd.DataFrame:
    """
    Mantiene una sola fotografia per ``signal_date + asset``.

    Regola KEEP_FIRST_SNAPSHOT:
    - la prima esecuzione del giorno crea la riga;
    - i rerun dello stesso giorno NON cambiano prezzo, punteggi, azione o metadati;
    - un rerun può soltanto completare campi base realmente vuoti e target_date mancanti;
    - i controlli degli orizzonti già maturati non vengono mai toccati.
    """
    hist = ensure_history_columns(history)

    if not new_rows:
        return hist

    new_df = ensure_history_columns(pd.DataFrame(new_rows))

    for _, row in new_df.iterrows():
        signal_date = safe_str(row["signal_date"]).strip()
        asset = safe_str(row["asset"]).strip().upper()

        mask = (
            (hist["signal_date"].astype(str).str.strip() == signal_date)
            & (hist["asset"].astype(str).str.strip().str.upper() == asset)
        )

        if mask.any():
            idx = hist.index[mask][0]
            changed = False

            # La fotografia originaria resta intatta. Completa soltanto campi
            # davvero vuoti; created_utc/updated_utc non sono dati di segnale.
            for col in BASE_HISTORY_COLUMNS:
                if col in {"created_utc", "updated_utc"}:
                    continue

                if is_blank_value(hist.at[idx, col]) and not is_blank_value(row[col]):
                    hist.at[idx, col] = row[col]
                    changed = True

            # Le date target sono deterministiche e possono essere completate
            # se una vecchia riga ne era priva. Tutto il resto degli orizzonti
            # deve essere preservato.
            for h in HORIZONS:
                col = f"target_date_{h}d"
                if is_blank_value(hist.at[idx, col]) and not is_blank_value(row[col]):
                    hist.at[idx, col] = row[col]
                    changed = True

            if is_blank_value(hist.at[idx, "created_utc"]):
                hist.at[idx, "created_utc"] = row["created_utc"]
                changed = True

            if changed:
                hist.at[idx, "updated_utc"] = now_utc_iso()
        else:
            hist = pd.concat([hist, pd.DataFrame([row])], ignore_index=True)

    hist = ensure_history_columns(hist)
    hist = hist.sort_values(["signal_date", "asset"]).reset_index(drop=True)

    return hist

def get_first_index_on_or_after(df: pd.DataFrame, target_date):
    if df.empty:
        return None

    target_ts = pd.Timestamp(target_date)

    candidates = df.index[df.index >= target_ts]
    if len(candidates) == 0:
        return None

    return candidates[0]


def update_checks(history: pd.DataFrame, price_data) -> pd.DataFrame:
    out = ensure_history_columns(history)

    if out.empty:
        return out

    for idx, row in out.iterrows():
        asset = safe_str(row["asset"]).upper()
        if asset not in ASSETS:
            continue

        df = price_data.get(asset, pd.DataFrame())
        if df is None or df.empty:
            continue

        signal_date_str = safe_str(row["signal_date"])
        try:
            signal_date = pd.to_datetime(signal_date_str).date()
        except Exception:
            continue

        signal_price = safe_float(row["price"])
        if pd.isna(signal_price) or signal_price <= 0:
            continue

        last_available_date = df.index[-1].date()

        for h in HORIZONS:
            suffix = f"{h}d"

            checked_col = f"checked_{suffix}"
            target_col = f"target_date_{suffix}"
            actual_date_col = f"actual_date_{suffix}"
            actual_price_col = f"actual_price_{suffix}"
            return_col = f"return_{suffix}"
            drawdown_col = f"drawdown_{suffix}"
            max_gain_col = f"max_gain_{suffix}"

            target_date = signal_date + timedelta(days=h)
            out.at[idx, target_col] = target_date.isoformat()

            if parse_bool(out.at[idx, checked_col]):
                continue

            if target_date > last_available_date:
                continue

            actual_idx = get_first_index_on_or_after(df, target_date)
            if actual_idx is None:
                continue

            actual_price = float(df.loc[actual_idx, "Close"])

            start_ts = pd.Timestamp(signal_date)
            end_ts = pd.Timestamp(actual_idx)

            window = df[(df.index > start_ts) & (df.index <= end_ts)].copy()

            if window.empty:
                min_low = actual_price
                max_high = actual_price
            else:
                min_low = float(window["Low"].min())
                max_high = float(window["High"].max())

            ret = (actual_price / signal_price - 1) * 100
            drawdown = (min_low / signal_price - 1) * 100
            max_gain = (max_high / signal_price - 1) * 100

            out.at[idx, checked_col] = True
            out.at[idx, actual_date_col] = pd.Timestamp(actual_idx).strftime("%Y-%m-%d")
            out.at[idx, actual_price_col] = actual_price
            out.at[idx, return_col] = ret
            out.at[idx, drawdown_col] = drawdown
            out.at[idx, max_gain_col] = max_gain
            out.at[idx, "updated_utc"] = now_utc_iso()

    return ensure_history_columns(out)


def direction_correct(score, actual_return) -> bool:
    if pd.isna(score) or pd.isna(actual_return):
        return False

    score = float(score)
    actual_return = float(actual_return)

    if score > 0 and actual_return > 0:
        return True

    if score < 0 and actual_return < 0:
        return True

    return False


def metric_status(controls: int) -> str:
    if controls >= 100:
        return "MATURO"
    if controls >= 60:
        return "UTILE"
    if controls >= 30:
        return "PRIMA CALIBRAZIONE"
    if controls > 0:
        return "FEEDBACK RAPIDO"
    return "RACCOLTA DATI"


def horizon_family(h: int) -> str:
    if h <= 3:
        return "BREVE"
    if h <= 10:
        return "SETTIMANALE"
    if h <= 21:
        return "SWING"
    return "MEDIO"


def build_metrics(history: pd.DataFrame) -> pd.DataFrame:
    rows = []
    generated = now_utc_iso()

    hist = ensure_history_columns(history)

    for asset in ASSETS:
        asset_df = hist[hist["asset"].astype(str).str.upper() == asset].copy()

        for h in HORIZONS:
            suffix = f"{h}d"
            checked_col = f"checked_{suffix}"
            return_col = f"return_{suffix}"
            drawdown_col = f"drawdown_{suffix}"
            max_gain_col = f"max_gain_{suffix}"

            checked_df = asset_df[asset_df[checked_col].map(parse_bool)].copy()

            for module in MODULES:
                score_col = module["score_col"]
                module_df = checked_df.copy()

                if score_col not in module_df.columns:
                    module_df[score_col] = 0

                module_df[score_col] = pd.to_numeric(module_df[score_col], errors="coerce").fillna(0)
                module_df[return_col] = pd.to_numeric(module_df[return_col], errors="coerce")
                module_df[drawdown_col] = pd.to_numeric(module_df[drawdown_col], errors="coerce")
                module_df[max_gain_col] = pd.to_numeric(module_df[max_gain_col], errors="coerce")

                active_df = module_df[module_df[score_col] != 0].copy()

                controls = int(len(active_df))

                if controls > 0:
                    correct = int(
                        active_df.apply(
                            lambda r: direction_correct(r[score_col], r[return_col]),
                            axis=1,
                        ).sum()
                    )
                    accuracy = correct / controls * 100
                    avg_return = float(active_df[return_col].mean())
                    avg_drawdown = float(active_df[drawdown_col].mean())
                    avg_max_gain = float(active_df[max_gain_col].mean())

                    signed_outcome = active_df.apply(
                        lambda r: float(r[return_col]) if float(r[score_col]) > 0 else -float(r[return_col]),
                        axis=1,
                    )
                    avg_direction_adjusted_return = float(signed_outcome.mean())
                else:
                    correct = 0
                    accuracy = np.nan
                    avg_return = np.nan
                    avg_drawdown = np.nan
                    avg_max_gain = np.nan
                    avg_direction_adjusted_return = np.nan

                rows.append(
                    {
                        "generated_utc": generated,
                        "asset": asset,
                        "horizon_days": h,
                        "horizon": f"{h}g",
                        "horizon_family": horizon_family(h),
                        "module_key": module["key"],
                        "module": module["label"],
                        "calibration_role": module["role"],
                        "calibratable": bool(module["calibratable"]),
                        "parent_family": module["parent_family"],
                        "controls": controls,
                        "correct": correct,
                        "accuracy_direction_pct": accuracy,
                        "avg_return_pct": avg_return,
                        "avg_direction_adjusted_return_pct": avg_direction_adjusted_return,
                        "avg_drawdown_pct": avg_drawdown,
                        "avg_max_gain_pct": avg_max_gain,
                        "status": metric_status(controls),
                    }
                )

    return pd.DataFrame(rows)


def compact_latest_signals(history: pd.DataFrame, n: int = 12):
    if history.empty:
        return []

    hist = history.copy()
    hist["signal_date_sort"] = pd.to_datetime(hist["signal_date"], errors="coerce")
    hist = hist.sort_values(["signal_date_sort", "asset"], ascending=[False, True]).head(n)

    rows = []

    for _, r in hist.iterrows():
        asset = safe_str(r["asset"])
        rows.append(
            [
                safe_str(r["signal_date"]),
                asset,
                fmt_price(asset, safe_float(r["price"])),
                fmt_signed_int(safe_int(r["global_score"])),
                fmt_signed_int(safe_int(r["statistical_family_score"])),
                fmt_signed_int(safe_int(r["scanner_score"])),
                fmt_signed_int(safe_int(r["market_score"])),
                fmt_signed_int(safe_int(r["technical_score_component"])),
                fmt_signed_int(safe_int(r["classic_technical_score_component"])),
                fmt_signed_int(safe_int(r["sol_fractal_score"])),
                safe_str(r["action"]),
            ]
        )

    return rows


def status_rows(history: pd.DataFrame):
    rows = []

    for asset in ASSETS:
        asset_df = history[history["asset"].astype(str).str.upper() == asset].copy()
        row = [asset, str(len(asset_df))]

        for h in HORIZONS:
            checked_col = f"checked_{h}d"
            checked = int(asset_df[checked_col].map(parse_bool).sum()) if checked_col in asset_df.columns else 0
            row.append(str(checked))

        rows.append(row)

    return rows


def global_horizon_rows(metrics: pd.DataFrame):
    rows = []

    if metrics.empty:
        return rows

    global_metrics = metrics[metrics["module_key"] == "global"].copy()

    for asset in ASSETS:
        for h in HORIZONS:
            m = global_metrics[
                (global_metrics["asset"] == asset)
                & (global_metrics["horizon_days"] == h)
            ]

            if m.empty:
                continue

            r = m.iloc[0]
            rows.append(
                [
                    asset,
                    f"{h}g",
                    str(int(r["controls"])),
                    fmt_pct_plain(r["accuracy_direction_pct"]),
                    fmt_pct(r["avg_return_pct"]),
                    fmt_pct(r["avg_direction_adjusted_return_pct"]),
                    r["status"],
                ]
            )

    return rows


def module_rows_with_controls(metrics: pd.DataFrame, max_rows: int = 200):
    if metrics.empty:
        return []

    m = metrics.copy()
    m["controls"] = pd.to_numeric(m["controls"], errors="coerce").fillna(0).astype(int)
    m = m[m["controls"] > 0].copy()

    if m.empty:
        return []

    order = {h: i for i, h in enumerate(HORIZONS)}
    module_order = {module["key"]: i for i, module in enumerate(MODULES)}

    m["h_order"] = m["horizon_days"].map(order).fillna(999)
    m["module_order"] = m["module_key"].map(module_order).fillna(999)

    m = m.sort_values(["asset", "h_order", "module_order"]).head(max_rows)

    rows = []

    for _, r in m.iterrows():
        rows.append(
            [
                r["asset"],
                r["horizon"],
                r["module"],
                r["calibration_role"],
                str(int(r["controls"])),
                fmt_pct_plain(r["accuracy_direction_pct"]),
                fmt_pct(r["avg_return_pct"]),
                fmt_pct(r["avg_direction_adjusted_return_pct"]),
                fmt_pct(r["avg_drawdown_pct"]),
                fmt_pct(r["avg_max_gain_pct"]),
                r["status"],
            ]
        )

    return rows


def next_pending_checks(history: pd.DataFrame):
    rows = []
    today = datetime.now(timezone.utc).date()

    for asset in ASSETS:
        asset_df = history[history["asset"].astype(str).str.upper() == asset].copy()
        if asset_df.empty:
            continue

        candidates = []

        for _, r in asset_df.iterrows():
            signal_date = safe_str(r["signal_date"])
            try:
                sd = pd.to_datetime(signal_date).date()
            except Exception:
                continue

            for h in HORIZONS:
                checked = parse_bool(r.get(f"checked_{h}d", False))
                if checked:
                    continue

                target = sd + timedelta(days=h)
                days_left = (target - today).days
                if days_left >= 0:
                    candidates.append((target, h, signal_date, days_left))

        if not candidates:
            continue

        candidates.sort(key=lambda x: x[0])
        target, h, signal_date, days_left = candidates[0]

        if days_left == 0:
            left = "oggi / appena dati disponibili"
        elif days_left == 1:
            left = "domani"
        else:
            left = f"tra {days_left} giorni"

        rows.append(
            [
                asset,
                signal_date,
                f"{h}g",
                target.isoformat(),
                left,
            ]
        )

    return rows


def build_report(
    history: pd.DataFrame,
    metrics: pd.DataFrame,
    backfilled_rows_this_run: int = 0,
) -> str:
    generated = now_utc_str()

    latest_rows = compact_latest_signals(history)
    stat_rows = status_rows(history)
    global_rows = global_horizon_rows(metrics)
    module_rows = module_rows_with_controls(metrics)
    pending_rows = next_pending_checks(history)

    lines = []

    lines.append("# Accuratezza moduli / autocalibrazione allargata")
    lines.append("")
    lines.append(f"Generato: {generated}")
    lines.append("")
    lines.append(
        "Questo report salva ogni giorno i segnali dei moduli e controlla ogni giorno "
        "quali orizzonti sono maturati."
    )
    lines.append("")
    lines.append("La calibrazione ora controlla questi orizzonti:")
    lines.append("")
    lines.append("- **1g / 2g / 3g** = feedback rapidissimo")
    lines.append("- **5g / 7g / 10g** = feedback settimanale")
    lines.append("- **14g / 21g** = feedback swing")
    lines.append("- **30g / 45g / 60g** = feedback più serio")
    lines.append("")
    lines.append("Moduli controllati:")
    lines.append("")
    lines.append("- Global Confluence = benchmark dell'aggregato finale")
    lines.append("- **Famiglia statistica Scanner + Market Regime = modulo calibrabile reale**")
    lines.append("- Scanner grezzo = diagnostico, già incluso nella famiglia statistica")
    lines.append("- Market Regime grezzo = diagnostico, già incluso nella famiglia statistica")
    lines.append("- Struttura tecnica")
    lines.append("- Classic technical confirmation")
    lines.append("- Microstruttura exchange, OI/funding/taker flow/order book")
    lines.append("- Frattale SOL/BTC, solo per SOL")
    lines.append("# EXCHANGE_MICROSTRUCTURE_TRACKER_PATCH_V2_1")
    lines.append("")
    lines.append(
        "Regola anti-doppio-conteggio: **Scanner e Market Regime continuano a essere misurati separatamente "
        "solo per diagnosi, ma non devono ricevere due modifiche di peso autonome**. "
        "La calibrazione dei pesi deve agire sulla Famiglia statistica."
    )
    lines.append("")
    lines.append(
        "Nota: i controlli vengono aggiornati **ogni giorno**, ma i pesi del Global non devono "
        "cambiare automaticamente sotto 30 controlli. Prima si osserva, poi si calibra."
    )
    lines.append("")
    lines.append(f"Segnali totali salvati: **{len(history)}**.")
    lines.append("")

    backfill_count = 0
    if "statistical_family_source" in history.columns:
        backfill_count = int(
            history["statistical_family_source"]
            .astype(str)
            .str.startswith("BACKFILL_")
            .sum()
        )

    if backfill_count > 0:
        lines.append(
            f"Backfill storico Famiglia statistica: **{backfill_count} righe totali già completate nel diario**; "
            f"righe completate in questa esecuzione: **{int(backfilled_rows_this_run)}**. "
            "Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare "
            "un bonus Market Regime storico."
        )
    else:
        lines.append(
            f"Backfill storico Famiglia statistica: nessuna riga storica completata; "
            f"righe completate in questa esecuzione: **{int(backfilled_rows_this_run)}**."
        )
    lines.append("")
    lines.append(
        "Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. "
        "Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto "
        "completare campi realmente mancanti."
    )
    lines.append("")

    lines.append("## Ultimi segnali salvati")
    lines.append("")

    if latest_rows:
        lines.append(
            md_table(
                [
                    "Data",
                    "Asset",
                    "Prezzo",
                    "Global",
                    "Famiglia stat.",
                    "Scanner grezzo",
                    "Market grezzo",
                    "Tecnico",
                    "Classic",
                    "Frattale",
                    "Azione",
                ],
                latest_rows,
            )
        )
    else:
        lines.append("Nessun segnale salvato.")

    lines.append("")
    lines.append("## Stato controlli per orizzonte")
    lines.append("")
    lines.append(
        md_table(
            ["Asset", "Segnali salvati"] + [f"{h}g" for h in HORIZONS],
            stat_rows,
        )
    )

    lines.append("")
    lines.append("## Prossimi controlli in arrivo")
    lines.append("")

    if pending_rows:
        lines.append(
            md_table(
                ["Asset", "Segnale", "Orizzonte", "Data target", "Quando"],
                pending_rows,
            )
        )
    else:
        lines.append("Non ci sono controlli pendenti.")

    lines.append("")
    lines.append("## Lettura rapida Global Confluence")
    lines.append("")

    if global_rows:
        lines.append(
            md_table(
                [
                    "Asset",
                    "Orizzonte",
                    "Controlli",
                    "Accuratezza direzione",
                    "Return medio",
                    "Return corretto direzione",
                    "Stato",
                ],
                global_rows,
            )
        )
    else:
        lines.append("Nessun controllo Global ancora maturato.")

    lines.append("")
    lines.append("## Accuratezza direzionale per modulo")
    lines.append("")

    if module_rows:
        lines.append(
            md_table(
                [
                    "Asset",
                    "Orizzonte",
                    "Modulo",
                    "Ruolo",
                    "Controlli",
                    "Accuratezza direzione",
                    "Return medio",
                    "Return corretto direzione",
                    "Drawdown medio",
                    "Max gain medio",
                    "Stato",
                ],
                module_rows,
            )
        )
    else:
        lines.append(
            "Nessun controllo modulo ancora maturato. Dal primo giorno utile compariranno "
            "i controlli 1g, poi 2g, 3g, 5g e così via."
        )

    lines.append("")
    lines.append("## Come leggerlo")
    lines.append("")
    lines.append("- **CALIBRABILE** = modulo reale sul quale, con dati maturi, si può valutare una modifica di peso.")
    lines.append("- **DIAGNOSTICO** = resta misurato, ma è già incluso in una famiglia e il suo peso separato deve restare 0.")
    lines.append("- **BENCHMARK** = risultato complessivo del Global; serve per confrontare l'aggregato, non è un peso interno.")
    lines.append("- **Controlli** = segnali non neutrali già verificati su quell'orizzonte.")
    lines.append("- **Accuratezza direzione** = quante volte un segnale positivo ha avuto return positivo o un segnale negativo ha avuto return negativo.")
    lines.append("- **Return medio** = rendimento reale medio dell'asset su quell'orizzonte.")
    lines.append("- **Return corretto direzione** = return visto dal lato del modulo: se il modulo era ribassista, un calo conta positivo.")
    lines.append("- **Drawdown medio** = peggior discesa media durante l'orizzonte.")
    lines.append("- **Max gain medio** = massimo rialzo medio durante l'orizzonte.")
    lines.append("")
    lines.append("Regole operative:")
    lines.append("")
    lines.append("- Sotto **30 controlli**: solo osservazione, nessuna modifica ai pesi.")
    lines.append("- Da **30 controlli**: possibile calibrazione leggera.")
    lines.append("- Da **60 controlli**: lettura più utile.")
    lines.append("- Da **100+ controlli**: possibile revisione più seria dei pesi.")
    lines.append("")
    lines.append(
        "Questo report non cambia ancora automaticamente i pesi del Global Confluence. "
        "Produce però i metadati `calibratable` e `calibration_role`, così il report di calibrazione "
        "può escludere Scanner e Market dalle proposte di peso separate."
    )
    lines.append("")
    lines.append(
        "Nota tecnica: le colonne data sono forzate come testo, quindi non deve più apparire "
        "l'errore `Invalid value 'YYYY-MM-DD' for dtype 'float64'`."
    )

    return "\n".join(lines).rstrip() + "\n"


def save_metrics(metrics: pd.DataFrame) -> None:
    METRICS_CSV_PATH.parent.mkdir(parents=True, exist_ok=True)

    if metrics.empty:
        metrics = pd.DataFrame(
            columns=[
                "generated_utc",
                "asset",
                "horizon_days",
                "horizon",
                "horizon_family",
                "module_key",
                "module",
                "calibration_role",
                "calibratable",
                "parent_family",
                "controls",
                "correct",
                "accuracy_direction_pct",
                "avg_return_pct",
                "avg_direction_adjusted_return_pct",
                "avg_drawdown_pct",
                "avg_max_gain_pct",
                "status",
            ]
        )

    metrics.to_csv(METRICS_CSV_PATH, index=False)


def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    global_rows = read_global_metrics_rows()
    price_data = download_price_data()

    history = load_history()
    history, backfilled_rows = backfill_prudent_statistical_family(history)

    new_rows = build_signal_rows(global_rows, price_data)
    history = upsert_today_signals(history, new_rows)
    history = update_checks(history, price_data)
    history = ensure_history_columns(history)

    HISTORY_CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    history.to_csv(HISTORY_CSV_PATH, index=False)

    metrics = build_metrics(history)
    save_metrics(metrics)

    report_md = build_report(history, metrics, backfilled_rows_this_run=backfilled_rows)

    write_text(REPORT_PATH, report_md)
    write_text(SHORT_REPORT_PATH, report_md)

    latest_text = read_text(LATEST_REPORT_PATH)
    if latest_text:
        updated = replace_or_insert_block(latest_text, report_md)
        write_text(LATEST_REPORT_PATH, updated)
    else:
        write_text(LATEST_REPORT_PATH, f"{START_MARKER}\n{report_md}{END_MARKER}\n")

    print(f"Module signal tracker report scritto in: {REPORT_PATH}")
    print(f"Module signal tracker short report scritto in: {SHORT_REPORT_PATH}")
    print(f"History scritto in: {HISTORY_CSV_PATH}")
    print(f"Metrics scritto in: {METRICS_CSV_PATH}")
    print(f"Backfill prudente Famiglia statistica: {backfilled_rows} righe aggiornate")


if __name__ == "__main__":
    main()
