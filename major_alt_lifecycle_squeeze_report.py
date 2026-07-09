import os
from datetime import datetime, timezone

import numpy as np
import pandas as pd
import yfinance as yf
from tabulate import tabulate


REPORT_DIR = "reports"
MAIN_REPORT_PATH = os.path.join(REPORT_DIR, "latest_report.md")
REPORT_PATH = os.path.join(REPORT_DIR, "major_alt_lifecycle_squeeze_report.md")
HISTORY_CSV_PATH = os.path.join(REPORT_DIR, "major_alt_lifecycle_squeeze_history.csv")
METRICS_CSV_PATH = os.path.join(REPORT_DIR, "major_alt_lifecycle_squeeze_metrics.csv")

START_MARKER = "<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_START -->"
END_MARKER = "<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->"

TARGET_TICKER = "SOL-USD"
TARGET_NAME = "SOL"

# Importante:
# Questo modulo resta utile come contesto EMA200 / lifecycle,
# ma NON deve più dare punti al Global Confluence.
GLOBAL_WEIGHT_FORCED = 0

UNIVERSE = [
    "BTC-USD", "ETH-USD", "BNB-USD", "SOL-USD", "XRP-USD", "ADA-USD",
    "DOGE-USD", "TRX-USD", "LINK-USD", "AVAX-USD", "DOT-USD", "MATIC-USD",
    "LTC-USD", "BCH-USD", "UNI-USD", "ATOM-USD", "ETC-USD", "XLM-USD",
    "FIL-USD", "HBAR-USD", "APT-USD", "NEAR-USD", "ICP-USD", "VET-USD",
    "ALGO-USD", "SAND-USD", "MANA-USD", "AAVE-USD", "MKR-USD", "GRT-USD",
    "EGLD-USD", "THETA-USD", "XTZ-USD", "EOS-USD", "KSM-USD", "ZEC-USD",
    "DASH-USD", "COMP-USD", "SNX-USD", "YFI-USD", "ENJ-USD", "CHZ-USD",
    "BAT-USD", "ZIL-USD", "1INCH-USD", "OMG-USD", "LRC-USD", "QTUM-USD",
    "NEO-USD", "WAVES-USD", "CRV-USD", "RUNE-USD", "FTM-USD", "ONE-USD",
    "CAKE-USD",
]

MAX_ANALOGS = 30
MAX_ANALOGS_PER_ASSET = 3


def now_utc():
    return datetime.now(timezone.utc)


def read_text(path):
    if not os.path.exists(path):
        return ""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_text(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def safe_float(v, default=np.nan):
    try:
        if v is None:
            return default

        if isinstance(v, str):
            s = v.strip()
            if not s or s.lower() in ["nan", "none", "null", "n/a", "na"]:
                return default

            s = s.replace("%", "")
            s = s.replace("$", "")
            s = s.replace("€", "")
            s = s.replace("+", "")
            s = s.replace("−", "-")
            s = s.replace(" ", "")

            if "," in s and "." in s:
                s = s.replace(".", "").replace(",", ".")
            elif "," in s:
                s = s.replace(",", ".")

            return float(s)

        if pd.isna(v):
            return default

        return float(v)

    except Exception:
        return default


def fmt_price(v, decimals=2):
    v = safe_float(v)
    if pd.isna(v):
        return "n/a"

    s = f"{v:,.{decimals}f}"
    s = s.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{s} $"


def fmt_pct(v, decimals=2, signed=True):
    v = safe_float(v)
    if pd.isna(v):
        return "n/a"

    sign = "+" if signed and v > 0 else ""
    return f"{sign}{v:.{decimals}f}%".replace(".", ",")


def fmt_number(v, decimals=2):
    v = safe_float(v)
    if pd.isna(v):
        return "n/a"

    return f"{v:.{decimals}f}".replace(".", ",")


def normalize_ohlcv(df):
    if df is None or df.empty:
        return pd.DataFrame()

    out = df.copy()

    if isinstance(out.columns, pd.MultiIndex):
        fields = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
        level0 = list(out.columns.get_level_values(0))
        level1 = list(out.columns.get_level_values(1))

        if any(f in level0 for f in fields):
            tmp = {}
            for field in fields:
                if field in level0:
                    part = out.xs(field, axis=1, level=0)
                    tmp[field] = part.iloc[:, 0]
            out = pd.DataFrame(tmp)

        elif any(f in level1 for f in fields):
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


def download_weekly(ticker):
    try:
        raw = yf.download(
            ticker,
            period="max",
            interval="1wk",
            progress=False,
            auto_adjust=False,
            actions=False,
            threads=False,
        )
        return normalize_ohlcv(raw)
    except Exception as e:
        print(f"Download weekly fallito per {ticker}: {e}")
        return pd.DataFrame()


def ema(series, span):
    return series.ewm(span=span, adjust=False).mean()


def rsi(series, period=14):
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.ewm(alpha=1 / period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / period, adjust=False).mean()

    rs = avg_gain / avg_loss.replace(0, np.nan)
    out = 100 - (100 / (1 + rs))
    return out


def prepare_weekly_indicators(df):
    out = df.copy()
    out["ema50"] = ema(out["Close"], 50)
    out["ema200"] = ema(out["Close"], 200)
    out["rsi14"] = rsi(out["Close"], 14)
    return out


def get_asset_age_years(df, date):
    if df is None or df.empty or pd.isna(date):
        return np.nan

    first_date = df.index.min()
    return (date - first_date).days / 365.25


def classify_cross_state(gap_pct):
    gap_pct = safe_float(gap_pct)

    if pd.isna(gap_pct):
        return "n/a"

    if abs(gap_pct) <= 2:
        return "EMA50/EMA200 SOVRAPPOSTE / INCROCIO IN CORSO"

    if gap_pct > 2:
        return "EMA50 SOPRA EMA200"

    return "EMA50 SOTTO EMA200"


def compute_lifecycle_score(row):
    price = safe_float(row.get("price"))
    ema50_v = safe_float(row.get("ema50"))
    ema200_v = safe_float(row.get("ema200"))
    rsi_v = safe_float(row.get("rsi14"))
    age_years = safe_float(row.get("age_years"))

    if pd.isna(price) or pd.isna(ema200_v) or ema200_v == 0:
        return 0

    distance_pct = (price / ema200_v - 1) * 100
    gap_pct = (ema50_v / ema200_v - 1) * 100 if not pd.isna(ema50_v) and ema200_v else np.nan

    score = 0

    if not pd.isna(age_years) and age_years >= 3:
        score += 1

    if -45 <= distance_pct <= -15:
        score += 2
    elif -60 <= distance_pct < -45:
        score += 1
    elif -15 < distance_pct < 5:
        score += 1

    if not pd.isna(gap_pct) and abs(gap_pct) <= 2:
        score += 1

    if not pd.isna(rsi_v) and 35 <= rsi_v <= 55:
        score += 1

    return int(max(0, min(score, 5)))


def classify_bias(score):
    score = int(score)

    if score >= 5:
        return "SQUEEZE SETUP FORTE"

    if score >= 3:
        return "SQUEEZE SETUP MODERATO"

    if score >= 1:
        return "CONTESTO DA OSSERVARE"

    return "NESSUN SETUP EMA200"


def classify_action(score):
    score = int(score)

    if score >= 5:
        return "CONTESTO BUONO VERSO EMA200, MA NON PESA NEL GLOBAL"

    if score >= 3:
        return "CONTESTO INTERESSANTE, SERVONO CONFERME DI PREZZO"

    if score >= 1:
        return "SOLO OSSERVAZIONE"

    return "NESSUNA CONFLUENZA OPERATIVA"


def classify_trend(current_score, previous_score):
    if previous_score is None or pd.isna(previous_score):
        return "STABILE / DA CONFERMARE", 0

    current_score = safe_float(current_score)
    previous_score = safe_float(previous_score)

    diff = current_score - previous_score

    if diff >= 2:
        return "MIGLIORAMENTO FORTE", 1

    if diff >= 1:
        return "MIGLIORAMENTO", 1

    if diff <= -2:
        return "PEGGIORAMENTO FORTE", -1

    if diff <= -1:
        return "PEGGIORAMENTO", -1

    return "STABILE / DA CONFERMARE", 0


def load_previous_score():
    if not os.path.exists(HISTORY_CSV_PATH):
        return None, None

    try:
        hist = pd.read_csv(HISTORY_CSV_PATH)
    except Exception:
        return None, None

    if hist.empty or "date" not in hist.columns or "lifecycle_score" not in hist.columns:
        return None, None

    hist = hist.dropna(subset=["date"]).copy()
    hist = hist.sort_values("date")

    if hist.empty:
        return None, None

    last = hist.iloc[-1]
    return last.get("date"), safe_float(last.get("lifecycle_score"))


def build_target_snapshot():
    df = download_weekly(TARGET_TICKER)

    if df.empty:
        raise RuntimeError("Impossibile scaricare dati weekly SOL da Yahoo Finance.")

    ind = prepare_weekly_indicators(df)
    ind = ind.dropna(subset=["Close", "ema50", "ema200", "rsi14"]).copy()

    if ind.empty:
        raise RuntimeError("Dati insufficienti per calcolare EMA50/EMA200 weekly SOL.")

    last = ind.iloc[-1]
    last_date = ind.index[-1]

    price = safe_float(last["Close"])
    ema50_v = safe_float(last["ema50"])
    ema200_v = safe_float(last["ema200"])
    rsi_v = safe_float(last["rsi14"])

    distance_pct = (price / ema200_v - 1) * 100 if ema200_v else np.nan
    upside_pct = (ema200_v / price - 1) * 100 if price else np.nan
    gap_pct = (ema50_v / ema200_v - 1) * 100 if ema200_v else np.nan
    age_years = get_asset_age_years(df, last_date)

    row = {
        "date": last_date.strftime("%Y-%m-%d"),
        "asset": TARGET_NAME,
        "ticker": TARGET_TICKER,
        "price": price,
        "ema50": ema50_v,
        "ema200": ema200_v,
        "distance_pct": distance_pct,
        "upside_pct": upside_pct,
        "ema50_ema200_gap_pct": gap_pct,
        "cross_state": classify_cross_state(gap_pct),
        "rsi14": rsi_v,
        "age_years": age_years,
    }

    row["lifecycle_score"] = compute_lifecycle_score(row)
    row["bias"] = classify_bias(row["lifecycle_score"])
    row["action"] = classify_action(row["lifecycle_score"])
    row["global_weight"] = GLOBAL_WEIGHT_FORCED

    return row, ind


def find_analogs(target_row):
    analog_rows = []

    target_age = safe_float(target_row.get("age_years"))
    target_distance = safe_float(target_row.get("distance_pct"))
    target_gap = safe_float(target_row.get("ema50_ema200_gap_pct"))
    target_rsi = safe_float(target_row.get("rsi14"))

    for ticker in UNIVERSE:
        df = download_weekly(ticker)

        if df.empty or len(df) < 230:
            continue

        ind = prepare_weekly_indicators(df)
        ind = ind.dropna(subset=["Close", "High", "Low", "ema50", "ema200", "rsi14"]).copy()

        if len(ind) < 230:
            continue

        rows_for_asset = []

        for i in range(200, len(ind) - 13):
            snap = ind.iloc[i]
            snap_date = ind.index[i]

            price = safe_float(snap["Close"])
            ema50_v = safe_float(snap["ema50"])
            ema200_v = safe_float(snap["ema200"])
            rsi_v = safe_float(snap["rsi14"])

            if pd.isna(price) or pd.isna(ema50_v) or pd.isna(ema200_v) or ema200_v == 0:
                continue

            distance = (price / ema200_v - 1) * 100
            gap = (ema50_v / ema200_v - 1) * 100
            age = get_asset_age_years(df, snap_date)

            if pd.isna(age) or pd.isna(target_age):
                continue

            future = ind.iloc[i + 1: i + 13].copy()

            if future.empty:
                continue

            max_high = safe_float(future["High"].max())
            min_low = safe_float(future["Low"].min())

            max_gain_12w = (max_high / price - 1) * 100 if price else np.nan
            drawdown_12w = (min_low / price - 1) * 100 if price else np.nan
            hit_ema200_12w = bool(max_high >= ema200_v)

            dist_score = abs(distance - target_distance)
            gap_score = abs(gap - target_gap)
            rsi_score = abs(rsi_v - target_rsi)
            age_score = abs(age - target_age)

            similarity_distance = (
                dist_score * 1.8
                + gap_score * 2.5
                + rsi_score * 0.8
                + age_score * 2.0
            )

            # Filtro morbido per non prendere analoghi troppo lontani.
            if dist_score > 35:
                continue

            if gap_score > 12:
                continue

            if rsi_score > 25:
                continue

            rows_for_asset.append({
                "similar_asset": ticker,
                "date": snap_date.strftime("%Y-%m-%d"),
                "price": price,
                "distance_pct": distance,
                "gap_pct": gap,
                "rsi14": rsi_v,
                "age_years": age,
                "similarity_distance": similarity_distance,
                "hit_ema200_12w": hit_ema200_12w,
                "max_gain_12w": max_gain_12w,
                "drawdown_12w": drawdown_12w,
            })

        if rows_for_asset:
            asset_df = pd.DataFrame(rows_for_asset)
            asset_df = asset_df.sort_values("similarity_distance").head(MAX_ANALOGS_PER_ASSET)
            analog_rows.extend(asset_df.to_dict("records"))

    if not analog_rows:
        return pd.DataFrame()

    analogs = pd.DataFrame(analog_rows)
    analogs = analogs.sort_values("similarity_distance").head(MAX_ANALOGS).reset_index(drop=True)

    return analogs


def summarize_analogs(analogs):
    if analogs is None or analogs.empty:
        return {
            "analog_count": 0,
            "hit_ema200_12w_rate": np.nan,
            "median_max_gain_12w": np.nan,
            "median_drawdown_12w": np.nan,
        }

    return {
        "analog_count": int(len(analogs)),
        "hit_ema200_12w_rate": float(analogs["hit_ema200_12w"].astype(bool).mean() * 100),
        "median_max_gain_12w": safe_float(analogs["max_gain_12w"].median()),
        "median_drawdown_12w": safe_float(analogs["drawdown_12w"].median()),
    }


def save_history(row, analog_summary, previous_date):
    out = row.copy()
    out.update(analog_summary)
    out["generated_at"] = now_utc().strftime("%Y-%m-%d %H:%M:%S UTC")

    new_df = pd.DataFrame([out])

    if os.path.exists(HISTORY_CSV_PATH):
        try:
            hist = pd.read_csv(HISTORY_CSV_PATH)
        except Exception:
            hist = pd.DataFrame()
    else:
        hist = pd.DataFrame()

    if not hist.empty and "date" in hist.columns:
        hist = hist[hist["date"].astype(str) != str(row["date"])].copy()

    hist = pd.concat([hist, new_df], ignore_index=True)
    hist = hist.sort_values("date").reset_index(drop=True)
    hist.to_csv(HISTORY_CSV_PATH, index=False)

    metrics = pd.DataFrame([{
        "asset": TARGET_NAME,
        "ticker": TARGET_TICKER,
        "date": row["date"],
        "price": row["price"],
        "ema200": row["ema200"],
        "upside_pct": row["upside_pct"],
        "distance_pct": row["distance_pct"],
        "ema50_ema200_gap_pct": row["ema50_ema200_gap_pct"],
        "cross_state": row["cross_state"],
        "rsi14": row["rsi14"],
        "age_years": row["age_years"],
        "lifecycle_score": row["lifecycle_score"],
        "bias": row["bias"],
        "action": row["action"],
        "global_weight": GLOBAL_WEIGHT_FORCED,
        "analog_count": analog_summary["analog_count"],
        "hit_ema200_12w_rate": analog_summary["hit_ema200_12w_rate"],
        "median_max_gain_12w": analog_summary["median_max_gain_12w"],
        "median_drawdown_12w": analog_summary["median_drawdown_12w"],
    }])

    metrics.to_csv(METRICS_CSV_PATH, index=False)


def df_to_markdown(df):
    if df is None or df.empty:
        return "_Nessun dato disponibile._"

    return tabulate(df, headers="keys", tablefmt="pipe", showindex=False)


def build_report(row, analog_summary, previous_date, previous_score, trend_label, trend_score):
    generated = now_utc().strftime("%Y-%m-%d %H:%M UTC")

    table = pd.DataFrame([
        {"Voce": "Lifecycle squeeze score", "Valore": int(row["lifecycle_score"])},
        {"Voce": "Bias", "Valore": row["bias"]},
        {"Voce": "Azione coerente", "Valore": row["action"]},
        {"Voce": "Peso suggerito Global", "Valore": GLOBAL_WEIGHT_FORCED},
        {"Voce": "Trend squeeze", "Valore": trend_label},
        {"Voce": "Trend squeeze score", "Valore": trend_score},
        {"Voce": "Confronto precedente", "Valore": previous_date if previous_date else "n/a"},
        {"Voce": "Fonte prezzi", "Valore": "Yahoo Finance SOL-USD weekly"},
        {"Voce": "Prezzo SOL", "Valore": fmt_price(row["price"])},
        {"Voce": "EMA200 weekly target", "Valore": fmt_price(row["ema200"])},
        {"Voce": "Upside verso EMA200", "Valore": fmt_pct(row["upside_pct"])},
        {"Voce": "Distanza prezzo da EMA200", "Valore": fmt_pct(row["distance_pct"])},
        {"Voce": "Gap EMA50/EMA200", "Valore": fmt_pct(row["ema50_ema200_gap_pct"])},
        {"Voce": "Stato cross", "Valore": row["cross_state"]},
        {"Voce": "RSI weekly", "Valore": fmt_number(row["rsi14"])},
        {"Voce": "Età SOL", "Valore": f"{fmt_number(row['age_years'], 1)} anni"},
        {"Voce": "Analoghi storici usati", "Valore": analog_summary["analog_count"]},
        {"Voce": "Max analoghi per asset", "Valore": MAX_ANALOGS_PER_ASSET},
        {"Voce": "Hit EMA200 12w analoghi", "Valore": fmt_pct(analog_summary["hit_ema200_12w_rate"])},
        {"Voce": "Max gain mediano 12w", "Valore": fmt_pct(analog_summary["median_max_gain_12w"])},
        {"Voce": "Drawdown mediano 12w", "Valore": fmt_pct(analog_summary["median_drawdown_12w"])},
    ])

    report = f"""{START_MARKER}

---

# Major alt lifecycle squeeze - SOL

Report separato completo: **[major_alt_lifecycle_squeeze_report.md](major_alt_lifecycle_squeeze_report.md)**

{df_to_markdown(table)}

Lettura semplice:

**{row["action"]}**

Autocontrollo: **{trend_label}**.

Questo modulo confronta SOL con altre crypto in fasi simili di età, distanza da EMA200, EMA50/EMA200 e RSI. Non usa stock market.

Nota importante: **questo modulo ora NON pesa più nel Global Confluence**. Resta solo come contesto di ciclo e come mappa verso EMA200 weekly. Il punteggio Global resta guidato da prezzo, scanner, regime, struttura tecnica, frattale, RSI e conferme reali.

Nota: se EMA50/EMA200 sono dentro ±2%, il modulo parla di medie sovrapposte / incrocio in corso, perché exchange diversi possono mostrare il cross leggermente prima o dopo.

<!-- Generato: {generated} -->
{END_MARKER}
"""
    return report


def replace_section_in_latest_report(section_text):
    if not os.path.exists(MAIN_REPORT_PATH):
        write_text(MAIN_REPORT_PATH, section_text)
        return

    content = read_text(MAIN_REPORT_PATH)

    if START_MARKER in content and END_MARKER in content:
        start_idx = content.index(START_MARKER)
        end_idx = content.index(END_MARKER) + len(END_MARKER)
        new_content = content[:start_idx] + section_text + content[end_idx:]
    else:
        insert_before = "# Report giornaliero BTC / SOL / DOGE"
        if insert_before in content:
            idx = content.index(insert_before)
            new_content = content[:idx] + section_text + "\n" + content[idx:]
        else:
            if not content.endswith("\n"):
                content += "\n"
            new_content = content + "\n" + section_text

    write_text(MAIN_REPORT_PATH, new_content)


def main():
    os.makedirs(REPORT_DIR, exist_ok=True)

    row, _ = build_target_snapshot()

    previous_date, previous_score = load_previous_score()
    trend_label, trend_score = classify_trend(row["lifecycle_score"], previous_score)

    analogs = find_analogs(row)
    analog_summary = summarize_analogs(analogs)

    save_history(row, analog_summary, previous_date)

    report_text = build_report(
        row=row,
        analog_summary=analog_summary,
        previous_date=previous_date,
        previous_score=previous_score,
        trend_label=trend_label,
        trend_score=trend_score,
    )

    write_text(REPORT_PATH, report_text)
    replace_section_in_latest_report(report_text)

    print(f"Report scritto in: {REPORT_PATH}")
    print(f"Latest report aggiornato: {MAIN_REPORT_PATH}")
    print(f"History scritto in: {HISTORY_CSV_PATH}")
    print(f"Metrics scritto in: {METRICS_CSV_PATH}")
    print(f"Lifecycle score: {row['lifecycle_score']}")
    print(f"Peso Global forzato: {GLOBAL_WEIGHT_FORCED}")


if __name__ == "__main__":
    main()
