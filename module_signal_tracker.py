from pathlib import Path
from datetime import datetime, timezone
import re

import numpy as np
import pandas as pd
import yfinance as yf


REPORTS_DIR = Path("reports")
LATEST_REPORT = REPORTS_DIR / "latest_report.md"

SIGNAL_LOG = REPORTS_DIR / "module_signal_log.csv"
ACCURACY_METRICS = REPORTS_DIR / "module_accuracy_metrics.csv"
ACCURACY_REPORT = REPORTS_DIR / "module_accuracy_report.md"

GLOBAL_CONFLUENCE_METRICS = REPORTS_DIR / "global_confluence_metrics.csv"
TECHNICAL_METRICS = REPORTS_DIR / "technical_structure_metrics.csv"
MARKET_REGIME_SUMMARY = REPORTS_DIR / "market_regime_match_summary.csv"

START_MARKER = "<!-- MODULE_ACCURACY_START -->"
END_MARKER = "<!-- MODULE_ACCURACY_END -->"

ASSETS = ["BTC", "SOL", "DOGE"]

TICKERS = {
    "BTC": "BTC-USD",
    "SOL": "SOL-USD",
    "DOGE": "DOGE-USD",
}

HORIZONS = [1, 3, 7, 14, 30, 60]


def utc_now():
    return datetime.now(timezone.utc)


def today_str():
    return utc_now().strftime("%Y-%m-%d")


def safe_float(x):
    try:
        if pd.isna(x):
            return np.nan
        return float(x)
    except Exception:
        return np.nan


def parse_number(value):
    if value is None:
        return np.nan

    s = str(value).strip()

    if not s or s.lower() == "nan":
        return np.nan

    s = s.replace("$", "")
    s = s.replace("€", "")
    s = s.replace("+", "")
    s = s.replace("−", "-")
    s = s.replace(" ", "")

    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".")
    elif "," in s:
        s = s.replace(",", ".")

    s = re.sub(r"[^0-9.\-]", "", s)

    if not s or s in ["-", ".", "-."]:
        return np.nan

    try:
        return float(s)
    except Exception:
        return np.nan


def fmt_pct(x):
    x = safe_float(x)

    if pd.isna(x):
        return "n/a"

    return f"{x:.2f}%".replace(".", ",")


def fmt_num(x, digits=2):
    x = safe_float(x)

    if pd.isna(x):
        return "n/a"

    return f"{x:.{digits}f}".replace(".", ",")


def fmt_score(x):
    try:
        x = int(float(x))

        if x > 0:
            return f"+{x}"

        return str(x)

    except Exception:
        return "0"


def df_to_markdown(df):
    if df is None or df.empty:
        return "_Nessun dato disponibile._"

    try:
        return df.to_markdown(index=False)
    except Exception:
        return "```csv\n" + df.to_csv(index=False) + "\n```"


def read_text(path):
    if not path.exists():
        return ""

    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def normalize_ohlcv(df):
    if df is None or df.empty:
        return pd.DataFrame()

    out = df.copy()

    if isinstance(out.columns, pd.MultiIndex):
        level0 = list(out.columns.get_level_values(0))
        level1 = list(out.columns.get_level_values(1))
        fields = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]

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

    needed = ["Open", "High", "Low", "Close", "Volume"]

    for col in needed:
        if col not in out.columns:
            if col in ["Open", "High", "Low"] and "Close" in out.columns:
                out[col] = out["Close"]
            elif col == "Volume":
                out[col] = np.nan
            else:
                return pd.DataFrame()

    out = out[needed].copy()
    out.index = pd.to_datetime(out.index)

    try:
        if out.index.tz is not None:
            out.index = out.index.tz_convert(None)
    except Exception:
        pass

    out.index = out.index.normalize()
    out = out[~out.index.duplicated(keep="last")]
    out = out.sort_index()
    out = out.dropna(subset=["Close"])

    return out


def download_prices(ticker, start=None):
    try:
        kwargs = {
            "tickers": ticker,
            "period": "max",
            "interval": "1d",
            "progress": False,
            "auto_adjust": False,
            "actions": False,
            "threads": False,
        }

        if start:
            kwargs.pop("period", None)
            kwargs["start"] = start

        raw = yf.download(**kwargs)

        return normalize_ohlcv(raw)

    except Exception as e:
        print(f"Download fallito per {ticker}: {e}")
        return pd.DataFrame()


def load_csv(path):
    if not path.exists():
        return pd.DataFrame()

    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


def current_price(asset):
    ticker = TICKERS[asset]
    df = download_prices(ticker, start="2020-01-01")

    if df.empty:
        return np.nan

    return safe_float(df["Close"].iloc[-1])


def row_for_asset(df, asset):
    if df is None or df.empty:
        return {}

    if "asset" in df.columns:
        m = df[df["asset"].astype(str).str.upper() == asset.upper()]

        if not m.empty:
            return m.iloc[0].to_dict()

    if "target" in df.columns:
        target = f"{asset}-USD"
        m = df[df["target"].astype(str).str.upper() == target.upper()]

        if not m.empty:
            return m.iloc[0].to_dict()

    return {}


def market_regime_row(asset, df):
    if df is None or df.empty:
        return {}

    if "target" not in df.columns or "group" not in df.columns:
        return {}

    target = f"{asset}-USD"
    d = df[df["target"].astype(str).str.upper() == target.upper()].copy()

    if d.empty:
        return {}

    preferred_groups = [
        "SAME_BTC_AND_ASSET_REGIME",
        "SAME_BTC_REGIME",
        "SAME_ASSET_REGIME",
        "ALL_MATCHES",
    ]

    for group in preferred_groups:
        g = d[d["group"].astype(str) == group]

        if not g.empty:
            return g.iloc[0].to_dict()

    return d.iloc[0].to_dict()


def parse_percent_value(value):
    if value is None:
        return np.nan

    s = str(value).strip()
    s = s.replace("%", "")
    s = s.replace("+", "")
    s = s.replace("−", "-")
    s = s.replace(",", ".")
    s = re.sub(r"[^0-9.\-]", "", s)

    if not s or s in ["-", ".", "-."]:
        return np.nan

    try:
        return float(s)
    except Exception:
        return np.nan


def parse_global_confluence():
    df = load_csv(GLOBAL_CONFLUENCE_METRICS)

    out = {}

    for asset in ASSETS:
        row = row_for_asset(df, asset)

        out[asset] = {
            "global_confluence_score": safe_float(row.get("confluence_score", np.nan)),
            "global_confluence_label": row.get("confluence", ""),
            "global_bias": row.get("bias", ""),
            "global_action": row.get("action", ""),

            "scanner_score": safe_float(row.get("scanner_score", np.nan)),
            "market_regime_score": safe_float(row.get("market_regime_score", np.nan)),
            "technical_component_score": safe_float(row.get("technical_score_component", np.nan)),
            "fractal_score": safe_float(row.get("fractal_score", np.nan)),
            "rsi_top_cycle_score": safe_float(row.get("rsi_top_cycle_score", np.nan)),
            "futures_score": safe_float(row.get("futures_score", np.nan)),
            "daily_change_score": safe_float(row.get("daily_change_score", np.nan)),

            "confirmation": row.get("confirmation", ""),
            "invalidation": row.get("invalidation", ""),
        }

    return out


def parse_technical():
    df = load_csv(TECHNICAL_METRICS)

    out = {}

    for asset in ASSETS:
        row = row_for_asset(df, asset)

        out[asset] = {
            "technical_raw_score": safe_float(row.get("technical_score", np.nan)),
            "technical_verdict": row.get("verdict", ""),
            "technical_trend": row.get("trend", ""),
            "technical_structure": row.get("structure", ""),
            "technical_support": safe_float(row.get("support", np.nan)),
            "technical_resistance": safe_float(row.get("resistance", np.nan)),
        }

    return out


def parse_market():
    df = load_csv(MARKET_REGIME_SUMMARY)

    out = {}

    for asset in ASSETS:
        row = market_regime_row(asset, df)

        out[asset] = {
            "market_group": row.get("group", ""),
            "market_matches": safe_float(row.get("matches", np.nan)),
            "market_positive_30d": parse_percent_value(row.get("positive_30d_rate", np.nan)),
            "market_return_30d_p50": parse_percent_value(row.get("return_30d_p50", np.nan)),
            "market_positive_60d": parse_percent_value(row.get("positive_60d_rate", np.nan)),
            "market_return_60d_p50": parse_percent_value(row.get("return_60d_p50", np.nan)),
        }

    return out


def extract_fractal_from_latest(asset):
    if asset != "SOL":
        return {
            "fractal_similarity": np.nan,
            "fractal_tracking": "",
            "fractal_phase": "",
            "fractal_risk": "",
        }

    text = read_text(LATEST_REPORT)

    if not text:
        return {
            "fractal_similarity": np.nan,
            "fractal_tracking": "",
            "fractal_phase": "",
            "fractal_risk": "",
        }

    start = text.find("<!-- BTC_SOL_FRACTAL_START -->")
    end = text.find("<!-- BTC_SOL_FRACTAL_END -->")

    if start != -1 and end != -1 and end > start:
        section = text[start:end]
    else:
        section = text

    def line_value(label):
        for line in section.splitlines():
            clean = line.replace("*", "").replace("|", "").strip()

            if label.lower() in clean.lower():
                val = clean.split(":", 1)[-1].strip() if ":" in clean else clean
                return val

        return ""

    sim = np.nan
    sim_line = line_value("Somiglianza totale")
    m = re.search(r"([0-9]+(?:[,.][0-9]+)?)\s*%", sim_line)

    if m:
        sim = safe_float(m.group(1).replace(",", "."))

    return {
        "fractal_similarity": sim,
        "fractal_tracking": line_value("Trend tracking"),
        "fractal_phase": line_value("Fase attuale"),
        "fractal_risk": line_value("Rischio fase"),
    }


def build_today_rows():
    global_data = parse_global_confluence()
    technical_data = parse_technical()
    market_data = parse_market()

    rows = []
    now = utc_now().strftime("%Y-%m-%d %H:%M:%S UTC")
    date = today_str()

    for asset in ASSETS:
        price = current_price(asset)

        g = global_data.get(asset, {})
        t = technical_data.get(asset, {})
        m = market_data.get(asset, {})
        f = extract_fractal_from_latest(asset)

        row = {
            "prediction_date": date,
            "created_at_utc": now,
            "asset": asset,
            "ticker": TICKERS[asset],
            "start_price": price,

            **g,
            **t,
            **m,
            **f,
        }

        for h in HORIZONS:
            row[f"checked_{h}d"] = False
            row[f"end_price_{h}d"] = np.nan
            row[f"return_{h}d"] = np.nan
            row[f"drawdown_{h}d"] = np.nan
            row[f"max_gain_{h}d"] = np.nan

            row[f"direction_correct_global_{h}d"] = np.nan
            row[f"direction_correct_scanner_{h}d"] = np.nan
            row[f"direction_correct_market_{h}d"] = np.nan
            row[f"direction_correct_technical_{h}d"] = np.nan
            row[f"direction_correct_fractal_{h}d"] = np.nan

        rows.append(row)

    return pd.DataFrame(rows)


def append_today_log():
    today_rows = build_today_rows()

    if SIGNAL_LOG.exists():
        old = load_csv(SIGNAL_LOG)
    else:
        old = pd.DataFrame()

    if not old.empty and "prediction_date" in old.columns and "asset" in old.columns:
        old = old[
            ~(
                old["prediction_date"].astype(str).isin(today_rows["prediction_date"].astype(str))
                & old["asset"].astype(str).isin(today_rows["asset"].astype(str))
            )
        ]

        combined = pd.concat([old, today_rows], ignore_index=True)
    else:
        combined = today_rows

    combined.to_csv(SIGNAL_LOG, index=False)

    return combined


def compute_outcome(asset, start_date, horizon):
    ticker = TICKERS[asset]

    start_dt = pd.to_datetime(start_date)
    end_dt = start_dt + pd.Timedelta(days=horizon)

    dl_start = (start_dt - pd.Timedelta(days=3)).strftime("%Y-%m-%d")

    df = download_prices(ticker, start=dl_start)

    if df.empty:
        return None

    df = df.copy()
    df.index = pd.to_datetime(df.index).normalize()

    after_start = df[df.index >= start_dt.normalize()]

    if after_start.empty:
        return None

    start_price = safe_float(after_start.iloc[0]["Close"])

    after_end = df[df.index >= end_dt.normalize()]

    if after_end.empty:
        return None

    end_index = after_end.index[0]
    end_price = safe_float(after_end.iloc[0]["Close"])

    window = df[(df.index >= start_dt.normalize()) & (df.index <= end_index)]

    if window.empty or pd.isna(start_price) or start_price == 0:
        return None

    min_low = safe_float(window["Low"].min())
    max_high = safe_float(window["High"].max())

    real_return = (end_price / start_price - 1) * 100 if not pd.isna(end_price) else np.nan
    drawdown = (min_low / start_price - 1) * 100 if not pd.isna(min_low) else np.nan
    max_gain = (max_high / start_price - 1) * 100 if not pd.isna(max_high) else np.nan

    return {
        "end_price": end_price,
        "return": real_return,
        "drawdown": drawdown,
        "max_gain": max_gain,
    }


def sign_from_score(score):
    score = safe_float(score)

    if pd.isna(score):
        return 0

    if score > 0:
        return 1

    if score < 0:
        return -1

    return 0


def direction_correct(score, real_return):
    direction = sign_from_score(score)

    if direction == 0 or pd.isna(real_return):
        return np.nan

    if direction > 0:
        return bool(real_return > 0)

    return bool(real_return < 0)


def update_checks(log_df):
    if log_df.empty:
        return log_df

    today = pd.to_datetime(today_str())

    for idx, row in log_df.iterrows():
        asset = str(row.get("asset", ""))

        if asset not in ASSETS:
            continue

        try:
            pred_date = pd.to_datetime(row.get("prediction_date", ""))
        except Exception:
            continue

        if pd.isna(pred_date):
            continue

        for h in HORIZONS:
            checked_col = f"checked_{h}d"

            already_checked = str(row.get(checked_col, "False")).lower() == "true"

            if already_checked:
                continue

            if pred_date + pd.Timedelta(days=h) > today:
                continue

            outcome = compute_outcome(asset, pred_date.strftime("%Y-%m-%d"), h)

            if outcome is None:
                continue

            log_df.at[idx, checked_col] = True
            log_df.at[idx, f"end_price_{h}d"] = outcome["end_price"]
            log_df.at[idx, f"return_{h}d"] = outcome["return"]
            log_df.at[idx, f"drawdown_{h}d"] = outcome["drawdown"]
            log_df.at[idx, f"max_gain_{h}d"] = outcome["max_gain"]

            log_df.at[idx, f"direction_correct_global_{h}d"] = direction_correct(
                row.get("global_confluence_score", np.nan),
                outcome["return"],
            )

            log_df.at[idx, f"direction_correct_scanner_{h}d"] = direction_correct(
                row.get("scanner_score", np.nan),
                outcome["return"],
            )

            log_df.at[idx, f"direction_correct_market_{h}d"] = direction_correct(
                row.get("market_regime_score", np.nan),
                outcome["return"],
            )

            log_df.at[idx, f"direction_correct_technical_{h}d"] = direction_correct(
                row.get("technical_component_score", np.nan),
                outcome["return"],
            )

            log_df.at[idx, f"direction_correct_fractal_{h}d"] = direction_correct(
                row.get("fractal_score", np.nan),
                outcome["return"],
            )

    log_df.to_csv(SIGNAL_LOG, index=False)

    return log_df


def summarize_accuracy(log_df):
    rows = []

    modules = [
        ("Global confluence", "global_confluence_score", "direction_correct_global"),
        ("Scanner", "scanner_score", "direction_correct_scanner"),
        ("Market regime", "market_regime_score", "direction_correct_market"),
        ("Tecnico", "technical_component_score", "direction_correct_technical"),
        ("Frattale SOL", "fractal_score", "direction_correct_fractal"),
    ]

    if log_df.empty:
        return pd.DataFrame()

    for asset in ASSETS:
        asset_df = log_df[log_df["asset"].astype(str) == asset].copy()

        for horizon in HORIZONS:
            checked_col = f"checked_{horizon}d"

            if checked_col not in asset_df.columns:
                continue

            checked = asset_df[asset_df[checked_col].astype(str).str.lower() == "true"].copy()

            for module_name, score_col, correct_prefix in modules:
                if score_col not in checked.columns:
                    continue

                if module_name == "Frattale SOL" and asset != "SOL":
                    continue

                d = checked.copy()
                d[score_col] = pd.to_numeric(d[score_col], errors="coerce")
                d = d[d[score_col].notna()]
                d = d[d[score_col] != 0]

                correct_col = f"{correct_prefix}_{horizon}d"

                if correct_col not in d.columns:
                    continue

                c = d[d[correct_col].notna()].copy()

                n = len(c)

                if n == 0:
                    accuracy = np.nan
                    avg_return = np.nan
                    avg_drawdown = np.nan
                    avg_max_gain = np.nan
                else:
                    correct_bool = c[correct_col].astype(str).str.lower().isin(["true", "1", "1.0"])
                    accuracy = correct_bool.mean() * 100
                    avg_return = pd.to_numeric(c[f"return_{horizon}d"], errors="coerce").mean()
                    avg_drawdown = pd.to_numeric(c[f"drawdown_{horizon}d"], errors="coerce").mean()
                    avg_max_gain = pd.to_numeric(c[f"max_gain_{horizon}d"], errors="coerce").mean()

                rows.append({
                    "asset": asset,
                    "horizon_days": horizon,
                    "module": module_name,
                    "checked_predictions": n,
                    "direction_accuracy": accuracy,
                    "avg_return": avg_return,
                    "avg_drawdown": avg_drawdown,
                    "avg_max_gain": avg_max_gain,
                })

    return pd.DataFrame(rows)


def calibration_status(n):
    if n < 30:
        return "RACCOLTA DATI"

    if n < 60:
        return "CALIBRAZIONE LEGGERA"

    if n < 100:
        return "CALIBRAZIONE MEDIA"

    return "CALIBRAZIONE PIÙ SOLIDA"


def render_report(log_df, metrics):
    now = utc_now().strftime("%Y-%m-%d %H:%M UTC")

    lines = []

    lines.append("# Accuratezza moduli / autocalibrazione allargata")
    lines.append("")
    lines.append(f"Generato: {now}")
    lines.append("")
    lines.append("Questo report salva ogni giorno i segnali dei moduli e controlla, dopo vari orizzonti, quali moduli stanno davvero aiutando.")
    lines.append("")
    lines.append("Moduli controllati:")
    lines.append("")
    lines.append("- Global Confluence")
    lines.append("- Scanner grezzo")
    lines.append("- Market regime")
    lines.append("- Struttura tecnica")
    lines.append("- Frattale SOL/BTC, solo per SOL")
    lines.append("")
    lines.append("Orizzonti controllati: 1, 3, 7, 14, 30 e 60 giorni.")
    lines.append("")

    if log_df.empty:
        lines.append("_Nessun segnale salvato._")
        return "\n".join(lines) + "\n"

    total_signals = len(log_df)
    lines.append(f"Segnali totali salvati: **{total_signals}**.")
    lines.append("")

    latest_rows = log_df.sort_values(["prediction_date", "asset"]).tail(len(ASSETS))

    lines.append("## Ultimi segnali salvati")
    lines.append("")

    latest_table = []

    for _, r in latest_rows.iterrows():
        asset = r.get("asset", "")
        digits = 5 if asset == "DOGE" else 2

        latest_table.append({
            "Data": r.get("prediction_date", ""),
            "Asset": asset,
            "Prezzo": fmt_num(r.get("start_price", np.nan), digits),
            "Global": fmt_score(r.get("global_confluence_score", 0)),
            "Scanner": fmt_score(r.get("scanner_score", 0)),
            "Market": fmt_score(r.get("market_regime_score", 0)),
            "Tecnico": fmt_score(r.get("technical_component_score", 0)),
            "Frattale": fmt_score(r.get("fractal_score", 0)),
            "Azione": r.get("global_action", ""),
        })

    lines.append(df_to_markdown(pd.DataFrame(latest_table)))
    lines.append("")

    lines.append("## Stato controlli")
    lines.append("")

    status_rows = []

    for asset in ASSETS:
        d = log_df[log_df["asset"].astype(str) == asset]

        row = {
            "Asset": asset,
            "Segnali salvati": len(d),
        }

        for h in HORIZONS:
            checked_col = f"checked_{h}d"

            if checked_col in d.columns:
                checked = d[d[checked_col].astype(str).str.lower() == "true"]
                row[f"{h}g controllati"] = len(checked)
            else:
                row[f"{h}g controllati"] = 0

        status_rows.append(row)

    lines.append(df_to_markdown(pd.DataFrame(status_rows)))
    lines.append("")

    lines.append("## Accuratezza direzionale per modulo")
    lines.append("")

    if metrics.empty:
        lines.append("_Dati insufficienti._")
    else:
        view = metrics.copy()
        view = view.sort_values(["asset", "horizon_days", "module"])

        table_rows = []

        for _, r in view.iterrows():
            n = int(r["checked_predictions"]) if not pd.isna(r["checked_predictions"]) else 0

            table_rows.append({
                "Asset": r["asset"],
                "Orizzonte": f"{int(r['horizon_days'])}g",
                "Modulo": r["module"],
                "Controlli": n,
                "Accuratezza direzione": fmt_pct(r["direction_accuracy"]),
                "Return medio": fmt_pct(r["avg_return"]),
                "Drawdown medio": fmt_pct(r["avg_drawdown"]),
                "Max gain medio": fmt_pct(r["avg_max_gain"]),
                "Stato": calibration_status(n),
            })

        lines.append(df_to_markdown(pd.DataFrame(table_rows)))

    lines.append("")

    lines.append("## Come leggerlo")
    lines.append("")
    lines.append("- Prima di 30 controlli per asset/modulo, è solo raccolta dati.")
    lines.append("- Dopo 30 controlli, il modulo può iniziare a dare una calibrazione leggera.")
    lines.append("- Dopo 60 controlli, la lettura diventa più utile.")
    lines.append("- Dopo 100+ controlli, i pesi dei moduli possono essere regolati con più fiducia.")
    lines.append("")
    lines.append("Questo report non cambia ancora automaticamente i pesi del Global Confluence. Serve prima a capire quali moduli funzionano davvero.")
    lines.append("")

    return "\n".join(lines) + "\n"


def inject_into_latest_report(section_md):
    if not LATEST_REPORT.exists():
        return

    old = read_text(LATEST_REPORT)

    if not old:
        return

    clean = section_md.strip()
    new_section = START_MARKER + "\n" + clean + "\n" + END_MARKER

    if START_MARKER in old and END_MARKER in old:
        start = old.find(START_MARKER)
        end = old.find(END_MARKER)

        if start != -1 and end != -1 and end > start:
            end = end + len(END_MARKER)
            new = old[:start] + new_section + old[end:]
        else:
            new = old.rstrip() + "\n\n" + new_section + "\n"
    else:
        calib_marker = "<!-- CALIBRATION_READABLE_END -->"

        if calib_marker in old:
            idx = old.find(calib_marker) + len(calib_marker)
            new = old[:idx] + "\n\n" + new_section + old[idx:]
        else:
            new = old.rstrip() + "\n\n" + new_section + "\n"

    LATEST_REPORT.write_text(new, encoding="utf-8")


def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    log_df = append_today_log()
    log_df = update_checks(log_df)

    metrics = summarize_accuracy(log_df)
    metrics.to_csv(ACCURACY_METRICS, index=False)

    md = render_report(log_df, metrics)
    ACCURACY_REPORT.write_text(md, encoding="utf-8")
    inject_into_latest_report(md)

    print(f"Creato/aggiornato {SIGNAL_LOG}")
    print(f"Creato {ACCURACY_METRICS}")
    print(f"Creato {ACCURACY_REPORT}")


if __name__ == "__main__":
    main()
