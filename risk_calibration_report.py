from pathlib import Path
from datetime import datetime, timezone
import re

import numpy as np
import pandas as pd
import yfinance as yf


REPORTS_DIR = Path("reports")
LATEST_REPORT = REPORTS_DIR / "latest_report.md"

OUTPUT_REPORT = REPORTS_DIR / "risk_calibration_report.md"
OUTPUT_METRICS = REPORTS_DIR / "risk_calibration_metrics.csv"
RISK_LOG = REPORTS_DIR / "risk_calibration_log.csv"

START_MARKER = "<!-- RISK_CALIBRATION_START -->"
END_MARKER = "<!-- RISK_CALIBRATION_END -->"

HORIZON_DAYS = 30

MIN_OBSERVATION_CHECKS = 30
MIN_LIGHT_CALIBRATION_CHECKS = 60
MIN_STRONG_CALIBRATION_CHECKS = 100

ASSETS = {
    "BTC": {
        "ticker": "BTC-USD",
        "name": "Bitcoin",
    },
    "SOL": {
        "ticker": "SOL-USD",
        "name": "Solana",
    },
    "DOGE": {
        "ticker": "DOGE-USD",
        "name": "Dogecoin",
    },
}


def utc_now():
    return datetime.now(timezone.utc)


def today_str():
    return utc_now().strftime("%Y-%m-%d")


def read_text(path):
    if not path.exists():
        return ""

    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


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

    if not s or s.lower() in ["nan", "none", "null", "n/a", "n/d", "nd"]:
        return np.nan

    s = s.replace("$", "")
    s = s.replace("€", "")
    s = s.replace("%", "")
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


def first_price(text):
    if not text:
        return np.nan

    s = str(text)

    m = re.search(r"([0-9]+(?:[.,][0-9]+)?)\s*\$", s)

    if m:
        return parse_number(m.group(1))

    return np.nan


def first_pct(text):
    if not text:
        return np.nan

    s = str(text)

    matches = re.findall(r"([+\-−]?[0-9]+(?:[.,][0-9]+)?)\s*%", s)

    if not matches:
        return np.nan

    # Evita di prendere il "10%" di "Percentile 10%" quando possibile.
    for m in matches:
        x = parse_number(m)
        if not pd.isna(x) and (x < 0 or x > 0):
            return x

    return parse_number(matches[0])


def clean_text(value):
    if value is None:
        return ""

    s = str(value)
    s = s.replace("**", "")
    s = s.replace("__", "")
    s = s.replace("`", "")
    s = s.replace("|", " ")
    s = re.sub(r"\s+", " ", s)

    return s.strip()


def fmt_price(x, asset=None):
    x = safe_float(x)

    if pd.isna(x):
        return "n/a"

    if asset == "DOGE":
        return f"{x:.5f} $"

    if asset == "BTC":
        return f"{x:,.2f} $".replace(",", "X").replace(".", ",").replace("X", ".")

    return f"{x:.2f} $".replace(".", ",")


def fmt_pct(x):
    x = safe_float(x)

    if pd.isna(x):
        return "n/a"

    return f"{x:.2f}%".replace(".", ",")


def fmt_num(x, decimals=2):
    x = safe_float(x)

    if pd.isna(x):
        return "n/a"

    return f"{x:.{decimals}f}".replace(".", ",")


def fmt_int(x):
    try:
        return str(int(x))
    except Exception:
        return "0"


def df_to_markdown(df):
    if df is None or df.empty:
        return "_Nessun dato disponibile._"

    try:
        return df.to_markdown(index=False)
    except Exception:
        return "```csv\n" + df.to_csv(index=False) + "\n```"


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
            "interval": "1d",
            "progress": False,
            "auto_adjust": False,
            "actions": False,
            "threads": False,
        }

        if start:
            kwargs["start"] = start
        else:
            kwargs["period"] = "max"

        raw = yf.download(**kwargs)

        return normalize_ohlcv(raw)

    except Exception as e:
        print(f"Download prezzi fallito per {ticker}: {e}")
        return pd.DataFrame()


def actual_close_on_or_after(df, date):
    if df.empty:
        return np.nan

    date = pd.to_datetime(date).normalize()
    d = df[df.index >= date]

    if d.empty:
        return np.nan

    return safe_float(d.iloc[0]["Close"])


def extract_section(text, start_marker, end_marker):
    if not text:
        return ""

    if start_marker not in text or end_marker not in text:
        return ""

    start = text.find(start_marker)
    end = text.find(end_marker)

    if start == -1 or end == -1 or end <= start:
        return ""

    return text[start:end]


def extract_asset_map_section(latest_text, asset_name):
    if not latest_text:
        return ""

    heading = f"# {asset_name} — mappa semplice"
    start = latest_text.find(heading)

    if start == -1:
        heading_alt = f"# {asset_name}"
        start = latest_text.find(heading_alt)

    if start == -1:
        return ""

    rest = latest_text[start + 1:]
    m = re.search(r"\n# [^\n]+", rest)

    if m:
        end = start + 1 + m.start()
        return latest_text[start:end]

    return latest_text[start:]


def extract_decision_risks(latest_text):
    risks = {}

    section = extract_section(
        latest_text,
        "<!-- DECISION_REPORT_START -->",
        "<!-- DECISION_REPORT_END -->",
    )

    if not section:
        return risks

    for line in section.splitlines():
        raw = line.strip()

        if not raw.startswith("|"):
            continue

        cells = [clean_text(c) for c in raw.strip("|").split("|")]

        if len(cells) < 8:
            continue

        asset = cells[0].upper()

        if asset in ASSETS:
            risks[asset] = {
                "decision_direction": cells[1],
                "decision_spot": cells[2],
                "decision_long": cells[3],
                "decision_short": cells[4],
                "decision_max_long": cells[5],
                "decision_max_short": cells[6],
                "decision_risk": cells[7],
            }

    return risks


def find_line_with_label(section, labels):
    if not section:
        return ""

    if isinstance(labels, str):
        labels = [labels]

    labels_low = [str(x).lower() for x in labels]

    for line in section.splitlines():
        low = line.lower()

        if any(label in low for label in labels_low):
            return line

    return ""


def parse_price_pct_from_labels(section, labels):
    line = find_line_with_label(section, labels)

    if not line:
        return np.nan, np.nan

    return first_price(line), first_pct(line)


def risk_label_from_drawdowns(normal_dd_pct, bad_dd_pct, mode):
    normal_dd_pct = safe_float(normal_dd_pct)
    bad_dd_pct = safe_float(bad_dd_pct)

    if pd.isna(normal_dd_pct) and pd.isna(bad_dd_pct):
        return "n/a"

    n = abs(normal_dd_pct) if not pd.isna(normal_dd_pct) else np.nan
    b = abs(bad_dd_pct) if not pd.isna(bad_dd_pct) else np.nan

    if mode == "spot":
        if (not pd.isna(b) and b >= 35) or (not pd.isna(n) and n >= 20):
            return "MOLTO ALTO"
        if (not pd.isna(b) and b >= 22) or (not pd.isna(n) and n >= 12):
            return "ALTO"
        if (not pd.isna(b) and b >= 14) or (not pd.isna(n) and n >= 7):
            return "MEDIO"
        return "BASSO"

    if mode == "leverage":
        if (not pd.isna(b) and b >= 15) or (not pd.isna(n) and n >= 8):
            return "MOLTO ALTO"
        if (not pd.isna(b) and b >= 10) or (not pd.isna(n) and n >= 5):
            return "ALTO"
        if (not pd.isna(b) and b >= 6) or (not pd.isna(n) and n >= 3):
            return "MEDIO"
        return "BASSO"

    if mode == "drawdown":
        if (not pd.isna(b) and b >= 30) or (not pd.isna(n) and n >= 18):
            return "MOLTO ALTO"
        if (not pd.isna(b) and b >= 20) or (not pd.isna(n) and n >= 10):
            return "ALTO"
        if (not pd.isna(b) and b >= 12) or (not pd.isna(n) and n >= 6):
            return "MEDIO"
        return "BASSO"

    return "n/a"


def leverage_note(normal_dd_pct, bad_dd_pct, very_bad_dd_pct):
    normal_dd_pct = safe_float(normal_dd_pct)
    bad_dd_pct = safe_float(bad_dd_pct)
    very_bad_dd_pct = safe_float(very_bad_dd_pct)

    values = [
        abs(x)
        for x in [normal_dd_pct, bad_dd_pct, very_bad_dd_pct]
        if not pd.isna(x)
    ]

    if not values:
        return "n/a"

    worst = max(values)

    if worst >= 30:
        return "spot preferibile; leva molto pericolosa anche 2x/3x senza margine largo"

    if worst >= 22:
        return "spot/tranche; se proprio leva, massimo 2x con margine molto largo"

    if worst >= 15:
        return "leva da limitare; 2x/3x solo con invalidazione chiara"

    if worst >= 10:
        return "leva moderata possibile solo con stop e margine"

    return "rischio leva relativamente più gestibile, ma non nullo"


def build_today_snapshot():
    latest = read_text(LATEST_REPORT)

    if not latest:
        return pd.DataFrame()

    decision_risks = extract_decision_risks(latest)
    rows = []

    for asset, info in ASSETS.items():
        section = extract_asset_map_section(latest, info["name"])

        if not section:
            continue

        current_line = find_line_with_label(section, "Prezzo attuale")
        current_price = first_price(current_line)

        direction_line = find_line_with_label(section, "Direzione più probabile a 30 giorni")
        direction = ""

        if direction_line:
            m = re.search(r"\*\*([^*]+)\*\*", direction_line)
            if m:
                direction = clean_text(m.group(1))
            else:
                direction = clean_text(direction_line.split(":", 1)[-1])

        positive_line = find_line_with_label(section, "Probabilità storica di salita")
        negative_line = find_line_with_label(section, "Probabilità storica di discesa")

        positive_rate = first_pct(positive_line)
        negative_rate = first_pct(negative_line)

        normal_dd_price, normal_dd_pct = parse_price_pct_from_labels(
            section,
            ["Discesa normale", "Drawdown normale durante il mese"],
        )

        bad_dd_price, bad_dd_pct = parse_price_pct_from_labels(
            section,
            ["Discesa brutta", "Drawdown brutto da rispettare"],
        )

        very_bad_dd_price, very_bad_dd_pct = parse_price_pct_from_labels(
            section,
            ["Discesa molto brutta", "Drawdown molto brutto"],
        )

        normal_gain_price, normal_gain_pct = parse_price_pct_from_labels(
            section,
            ["Rialzo normale", "Max gain normale durante il mese"],
        )

        good_gain_price, good_gain_pct = parse_price_pct_from_labels(
            section,
            ["Rialzo buono", "Max gain buono / take profit ottimistico"],
        )

        very_good_gain_price, very_good_gain_pct = parse_price_pct_from_labels(
            section,
            ["Rialzo molto forte", "Max gain molto forte"],
        )

        if pd.isna(current_price):
            continue

        # Se qualche percentuale manca, la ricostruisce dal prezzo.
        if pd.isna(normal_dd_pct) and not pd.isna(normal_dd_price) and current_price != 0:
            normal_dd_pct = (normal_dd_price / current_price - 1) * 100

        if pd.isna(bad_dd_pct) and not pd.isna(bad_dd_price) and current_price != 0:
            bad_dd_pct = (bad_dd_price / current_price - 1) * 100

        if pd.isna(very_bad_dd_pct) and not pd.isna(very_bad_dd_price) and current_price != 0:
            very_bad_dd_pct = (very_bad_dd_price / current_price - 1) * 100

        if pd.isna(normal_gain_pct) and not pd.isna(normal_gain_price) and current_price != 0:
            normal_gain_pct = (normal_gain_price / current_price - 1) * 100

        if pd.isna(good_gain_pct) and not pd.isna(good_gain_price) and current_price != 0:
            good_gain_pct = (good_gain_price / current_price - 1) * 100

        if pd.isna(very_good_gain_pct) and not pd.isna(very_good_gain_price) and current_price != 0:
            very_good_gain_pct = (very_good_gain_price / current_price - 1) * 100

        spot_risk = risk_label_from_drawdowns(normal_dd_pct, bad_dd_pct, "spot")
        leverage_risk = risk_label_from_drawdowns(normal_dd_pct, bad_dd_pct, "leverage")
        drawdown_risk = risk_label_from_drawdowns(normal_dd_pct, bad_dd_pct, "drawdown")

        decision = decision_risks.get(asset, {})

        rows.append({
            "forecast_date": today_str(),
            "created_at_utc": utc_now().strftime("%Y-%m-%d %H:%M:%S UTC"),
            "asset": asset,
            "ticker": info["ticker"],
            "horizon_days": HORIZON_DAYS,
            "target_date": (pd.to_datetime(today_str()) + pd.Timedelta(days=HORIZON_DAYS)).strftime("%Y-%m-%d"),
            "current_price": current_price,
            "scanner_direction": direction,
            "positive_rate_pct": positive_rate,
            "negative_rate_pct": negative_rate,
            "normal_drawdown_price": normal_dd_price,
            "normal_drawdown_pct": normal_dd_pct,
            "bad_drawdown_price": bad_dd_price,
            "bad_drawdown_pct": bad_dd_pct,
            "very_bad_drawdown_price": very_bad_dd_price,
            "very_bad_drawdown_pct": very_bad_dd_pct,
            "normal_max_gain_price": normal_gain_price,
            "normal_max_gain_pct": normal_gain_pct,
            "good_max_gain_price": good_gain_price,
            "good_max_gain_pct": good_gain_pct,
            "very_good_max_gain_price": very_good_gain_price,
            "very_good_max_gain_pct": very_good_gain_pct,
            "spot_risk_label": spot_risk,
            "leverage_risk_label": leverage_risk,
            "drawdown_risk_label": drawdown_risk,
            "leverage_note": leverage_note(normal_dd_pct, bad_dd_pct, very_bad_dd_pct),
            "decision_direction": decision.get("decision_direction", ""),
            "decision_spot": decision.get("decision_spot", ""),
            "decision_long": decision.get("decision_long", ""),
            "decision_short": decision.get("decision_short", ""),
            "decision_max_long": decision.get("decision_max_long", ""),
            "decision_max_short": decision.get("decision_max_short", ""),
            "decision_risk": decision.get("decision_risk", ""),
            "checked_30d": 0.0,
            "actual_end_price": np.nan,
            "actual_min_low": np.nan,
            "actual_max_high": np.nan,
            "actual_return_30d_pct": np.nan,
            "actual_drawdown_pct": np.nan,
            "actual_max_gain_pct": np.nan,
            "normal_drawdown_hit": np.nan,
            "bad_drawdown_hit": np.nan,
            "very_bad_drawdown_hit": np.nan,
            "normal_max_gain_hit": np.nan,
            "good_max_gain_hit": np.nan,
            "very_good_max_gain_hit": np.nan,
            "risk_result": "",
        })

    return pd.DataFrame(rows)


def append_today_snapshot(today_df):
    if today_df is None or today_df.empty:
        if RISK_LOG.exists():
            try:
                return pd.read_csv(RISK_LOG)
            except Exception:
                return pd.DataFrame()

        return pd.DataFrame()

    if RISK_LOG.exists():
        try:
            old = pd.read_csv(RISK_LOG)
        except Exception:
            old = pd.DataFrame()
    else:
        old = pd.DataFrame()

    if old.empty:
        combined = today_df.copy()
    else:
        keys = ["forecast_date", "asset", "horizon_days"]

        for k in keys:
            if k not in old.columns:
                old[k] = np.nan

        old_marker = old[keys].astype(str).agg("|".join, axis=1)
        today_marker = today_df[keys].astype(str).agg("|".join, axis=1)

        old = old[~old_marker.isin(set(today_marker))]
        combined = pd.concat([old, today_df], ignore_index=True)

    combined.to_csv(RISK_LOG, index=False)

    return combined


def classify_risk_result(row):
    normal_hit = safe_float(row.get("normal_drawdown_hit", np.nan))
    bad_hit = safe_float(row.get("bad_drawdown_hit", np.nan))
    very_bad_hit = safe_float(row.get("very_bad_drawdown_hit", np.nan))

    actual_drawdown = safe_float(row.get("actual_drawdown_pct", np.nan))
    normal_dd = safe_float(row.get("normal_drawdown_pct", np.nan))
    bad_dd = safe_float(row.get("bad_drawdown_pct", np.nan))

    if pd.isna(actual_drawdown):
        return ""

    if not pd.isna(very_bad_hit) and very_bad_hit >= 1:
        return "TAIL RISK TOCCATO"

    if not pd.isna(bad_hit) and bad_hit >= 1:
        return "RISCHIO ALTO CONFERMATO"

    if not pd.isna(normal_hit) and normal_hit >= 1:
        return "RISCHIO NORMALE CONFERMATO"

    if not pd.isna(normal_hit) and normal_hit == 0:
        return "RISCHIO STIMATO SEVERO"

    if not pd.isna(normal_dd) and actual_drawdown < normal_dd:
        return "RISCHIO NORMALE SUPERATO"

    if not pd.isna(bad_dd) and actual_drawdown < bad_dd:
        return "RISCHIO BRUTTO SUPERATO"

    return "n/a"


def update_risk_checks(log_df):
    if log_df is None or log_df.empty:
        return pd.DataFrame()

    out = log_df.copy()
    today = pd.to_datetime(today_str()).normalize()

    for col in [
        "checked_30d",
        "actual_end_price",
        "actual_min_low",
        "actual_max_high",
        "actual_return_30d_pct",
        "actual_drawdown_pct",
        "actual_max_gain_pct",
        "normal_drawdown_hit",
        "bad_drawdown_hit",
        "very_bad_drawdown_hit",
        "normal_max_gain_hit",
        "good_max_gain_hit",
        "very_good_max_gain_hit",
        "risk_result",
    ]:
        if col not in out.columns:
            out[col] = np.nan if col != "risk_result" else ""

    for asset, asset_df in out.groupby("asset"):
        asset = str(asset).upper()

        if asset not in ASSETS:
            continue

        forecast_dates = pd.to_datetime(asset_df["forecast_date"], errors="coerce").dropna()

        if forecast_dates.empty:
            continue

        min_date = forecast_dates.min()
        start = (min_date - pd.Timedelta(days=3)).strftime("%Y-%m-%d")

        prices = download_prices(ASSETS[asset]["ticker"], start=start)

        if prices.empty:
            continue

        for idx, row in asset_df.iterrows():
            checked = safe_float(row.get("checked_30d", 0.0))

            if not pd.isna(checked) and checked >= 1:
                continue

            forecast_date = pd.to_datetime(row.get("forecast_date", ""), errors="coerce")
            horizon_days = int(safe_float(row.get("horizon_days", HORIZON_DAYS)) or HORIZON_DAYS)

            if pd.isna(forecast_date):
                continue

            target_date = forecast_date.normalize() + pd.Timedelta(days=horizon_days)

            if target_date > today:
                continue

            window = prices[
                (prices.index >= forecast_date.normalize()) &
                (prices.index <= target_date.normalize())
            ].copy()

            if window.empty:
                continue

            current_price = safe_float(row.get("current_price", np.nan))
            end_price = actual_close_on_or_after(prices, target_date)
            min_low = safe_float(window["Low"].min())
            max_high = safe_float(window["High"].max())

            if pd.isna(current_price) or current_price == 0:
                continue

            actual_return = np.nan
            actual_drawdown = np.nan
            actual_max_gain = np.nan

            if not pd.isna(end_price):
                actual_return = (end_price / current_price - 1) * 100

            if not pd.isna(min_low):
                actual_drawdown = (min_low / current_price - 1) * 100

            if not pd.isna(max_high):
                actual_max_gain = (max_high / current_price - 1) * 100

            def hit_down(price_col):
                threshold = safe_float(row.get(price_col, np.nan))

                if pd.isna(threshold) or pd.isna(min_low):
                    return np.nan

                return 1.0 if min_low <= threshold else 0.0

            def hit_up(price_col):
                threshold = safe_float(row.get(price_col, np.nan))

                if pd.isna(threshold) or pd.isna(max_high):
                    return np.nan

                return 1.0 if max_high >= threshold else 0.0

            out.at[idx, "checked_30d"] = 1.0
            out.at[idx, "actual_end_price"] = end_price
            out.at[idx, "actual_min_low"] = min_low
            out.at[idx, "actual_max_high"] = max_high
            out.at[idx, "actual_return_30d_pct"] = actual_return
            out.at[idx, "actual_drawdown_pct"] = actual_drawdown
            out.at[idx, "actual_max_gain_pct"] = actual_max_gain
            out.at[idx, "normal_drawdown_hit"] = hit_down("normal_drawdown_price")
            out.at[idx, "bad_drawdown_hit"] = hit_down("bad_drawdown_price")
            out.at[idx, "very_bad_drawdown_hit"] = hit_down("very_bad_drawdown_price")
            out.at[idx, "normal_max_gain_hit"] = hit_up("normal_max_gain_price")
            out.at[idx, "good_max_gain_hit"] = hit_up("good_max_gain_price")
            out.at[idx, "very_good_max_gain_hit"] = hit_up("very_good_max_gain_price")

            temp_row = out.loc[idx].to_dict()
            out.at[idx, "risk_result"] = classify_risk_result(temp_row)

    out.to_csv(RISK_LOG, index=False)

    return out


def hit_rate(series):
    values = pd.to_numeric(series, errors="coerce").dropna()

    if values.empty:
        return np.nan

    return values.mean() * 100


def stage_from_checks(checked):
    checked = int(checked or 0)

    if checked < MIN_OBSERVATION_CHECKS:
        return "RACCOLTA DATI"

    if checked < MIN_LIGHT_CALIBRATION_CHECKS:
        return "OSSERVAZIONE 30+"

    if checked < MIN_STRONG_CALIBRATION_CHECKS:
        return "CALIBRAZIONE LEGGERA"

    return "CALIBRAZIONE MATURA"


def stage_note(stage):
    if stage == "RACCOLTA DATI":
        return "non applicare correzioni"

    if stage == "OSSERVAZIONE 30+":
        return "osserva, ma non modificare ancora il modello"

    if stage == "CALIBRAZIONE LEGGERA":
        return "può suggerire correzioni prudenti al rischio"

    if stage == "CALIBRAZIONE MATURA":
        return "può diventare una calibrazione utile per spot/leva"

    return ""


def calibration_bias_from_rates(normal_hit, bad_hit, very_bad_hit):
    normal_hit = safe_float(normal_hit)
    bad_hit = safe_float(bad_hit)
    very_bad_hit = safe_float(very_bad_hit)

    if pd.isna(normal_hit):
        return "n/a"

    if not pd.isna(very_bad_hit) and very_bad_hit >= 15:
        return "RISCHIO SOTTOVALUTATO"

    if not pd.isna(bad_hit) and bad_hit >= 35:
        return "RISCHIO ALTO CONFERMATO"

    if normal_hit < 25 and (pd.isna(bad_hit) or bad_hit < 10):
        return "RISCHIO FORSE TROPPO SEVERO"

    if normal_hit >= 40:
        return "RISCHIO NORMALE CONFERMATO"

    return "RISCHIO IN LINEA / DA OSSERVARE"


def summarize_metrics(log_df):
    if log_df is None or log_df.empty:
        return pd.DataFrame()

    rows = []

    for asset, d in log_df.groupby("asset"):
        asset = str(asset).upper()
        total = len(d)
        checked = d[pd.to_numeric(d["checked_30d"], errors="coerce").fillna(0) >= 1].copy()
        n = len(checked)
        pending = total - n

        normal_dd_hit = hit_rate(checked["normal_drawdown_hit"]) if n else np.nan
        bad_dd_hit = hit_rate(checked["bad_drawdown_hit"]) if n else np.nan
        very_bad_dd_hit = hit_rate(checked["very_bad_drawdown_hit"]) if n else np.nan

        normal_gain_hit = hit_rate(checked["normal_max_gain_hit"]) if n else np.nan
        good_gain_hit = hit_rate(checked["good_max_gain_hit"]) if n else np.nan
        very_good_gain_hit = hit_rate(checked["very_good_max_gain_hit"]) if n else np.nan

        avg_actual_drawdown = pd.to_numeric(checked["actual_drawdown_pct"], errors="coerce").mean() if n else np.nan
        avg_actual_max_gain = pd.to_numeric(checked["actual_max_gain_pct"], errors="coerce").mean() if n else np.nan
        avg_actual_return = pd.to_numeric(checked["actual_return_30d_pct"], errors="coerce").mean() if n else np.nan

        stage = stage_from_checks(n)
        bias = calibration_bias_from_rates(normal_dd_hit, bad_dd_hit, very_bad_dd_hit)

        rows.append({
            "asset": asset,
            "snapshots_saved": total,
            "checked_30d": n,
            "pending": pending,
            "calibration_stage": stage,
            "stage_note": stage_note(stage),
            "normal_drawdown_hit_rate_pct": normal_dd_hit,
            "bad_drawdown_hit_rate_pct": bad_dd_hit,
            "very_bad_drawdown_hit_rate_pct": very_bad_dd_hit,
            "normal_max_gain_hit_rate_pct": normal_gain_hit,
            "good_max_gain_hit_rate_pct": good_gain_hit,
            "very_good_max_gain_hit_rate_pct": very_good_gain_hit,
            "avg_actual_return_30d_pct": avg_actual_return,
            "avg_actual_drawdown_pct": avg_actual_drawdown,
            "avg_actual_max_gain_pct": avg_actual_max_gain,
            "risk_calibration_bias": bias,
            "can_influence_decision": n >= MIN_LIGHT_CALIBRATION_CHECKS,
            "can_strongly_influence_decision": n >= MIN_STRONG_CALIBRATION_CHECKS,
        })

    metrics = pd.DataFrame(rows)

    if metrics.empty:
        return metrics

    order = {"BTC": 0, "SOL": 1, "DOGE": 2}
    metrics["_order"] = metrics["asset"].map(order).fillna(9)

    metrics = metrics.sort_values("_order").drop(columns=["_order"])

    return metrics


def latest_snapshot(log_df):
    if log_df is None or log_df.empty:
        return pd.DataFrame()

    d = log_df.copy()
    d["forecast_date_dt"] = pd.to_datetime(d["forecast_date"], errors="coerce")
    max_date = d["forecast_date_dt"].max()

    if pd.isna(max_date):
        return pd.DataFrame()

    out = d[d["forecast_date_dt"] == max_date].copy()

    order = {"BTC": 0, "SOL": 1, "DOGE": 2}
    out["_order"] = out["asset"].map(order).fillna(9)

    return out.sort_values("_order").drop(columns=["_order"])


def build_latest_table(log_df):
    latest = latest_snapshot(log_df)

    if latest.empty:
        return pd.DataFrame()

    rows = []

    for _, r in latest.iterrows():
        asset = r["asset"]

        rows.append({
            "Asset": asset,
            "Prezzo": fmt_price(r.get("current_price", np.nan), asset),
            "Direzione scanner": r.get("scanner_direction", "n/a"),
            "Drawdown normale": f"{fmt_price(r.get('normal_drawdown_price', np.nan), asset)} / {fmt_pct(r.get('normal_drawdown_pct', np.nan))}",
            "Drawdown brutto": f"{fmt_price(r.get('bad_drawdown_price', np.nan), asset)} / {fmt_pct(r.get('bad_drawdown_pct', np.nan))}",
            "Max gain normale": f"{fmt_price(r.get('normal_max_gain_price', np.nan), asset)} / {fmt_pct(r.get('normal_max_gain_pct', np.nan))}",
            "Rischio spot": r.get("spot_risk_label", "n/a"),
            "Rischio leva": r.get("leverage_risk_label", "n/a"),
        })

    return pd.DataFrame(rows)


def build_metrics_table(metrics):
    if metrics is None or metrics.empty:
        return pd.DataFrame()

    rows = []

    for _, r in metrics.iterrows():
        rows.append({
            "Asset": r["asset"],
            "Snapshot": int(r["snapshots_saved"]),
            "Controlli 30g": int(r["checked_30d"]),
            "In attesa": int(r["pending"]),
            "Stato": r["calibration_stage"],
            "DD normale hit": fmt_pct(r["normal_drawdown_hit_rate_pct"]),
            "DD brutto hit": fmt_pct(r["bad_drawdown_hit_rate_pct"]),
            "DD molto brutto hit": fmt_pct(r["very_bad_drawdown_hit_rate_pct"]),
            "Bias rischio": r["risk_calibration_bias"],
        })

    return pd.DataFrame(rows)


def build_checked_examples_table(log_df, max_rows=12):
    if log_df is None or log_df.empty:
        return pd.DataFrame()

    checked = log_df[pd.to_numeric(log_df["checked_30d"], errors="coerce").fillna(0) >= 1].copy()

    if checked.empty:
        return pd.DataFrame()

    checked["forecast_date_dt"] = pd.to_datetime(checked["forecast_date"], errors="coerce")
    checked = checked.sort_values("forecast_date_dt", ascending=False).head(max_rows)

    rows = []

    for _, r in checked.iterrows():
        asset = r.get("asset", "")

        rows.append({
            "Data previsione": r.get("forecast_date", ""),
            "Asset": asset,
            "Prezzo iniziale": fmt_price(r.get("current_price", np.nan), asset),
            "Min reale": fmt_price(r.get("actual_min_low", np.nan), asset),
            "Max reale": fmt_price(r.get("actual_max_high", np.nan), asset),
            "Drawdown reale": fmt_pct(r.get("actual_drawdown_pct", np.nan)),
            "Max gain reale": fmt_pct(r.get("actual_max_gain_pct", np.nan)),
            "Risultato rischio": r.get("risk_result", ""),
        })

    return pd.DataFrame(rows)


def render_report(log_df, metrics):
    now = utc_now().strftime("%Y-%m-%d %H:%M UTC")

    lines = []

    lines.append("# Calibrazione rischio spot / leva")
    lines.append("")
    lines.append(f"Generato: **{now}**")
    lines.append("")
    lines.append("Questo report controlla se le zone di rischio previste dallo scanner vengono davvero toccate nei 30 giorni successivi.")
    lines.append("")
    lines.append("L'obiettivo è separare meglio:")
    lines.append("")
    lines.append("- rischio spot")
    lines.append("- rischio leva")
    lines.append("- rischio drawdown")
    lines.append("- rischio di liquidazione")
    lines.append("")
    lines.append("Questo file **non modifica ancora il Decision Report**. Per ora salva dati e misura. Le correzioni automatiche verranno considerate solo dopo abbastanza controlli.")
    lines.append("")

    lines.append("## Regola prudente")
    lines.append("")
    lines.append(f"- Sotto **{MIN_OBSERVATION_CHECKS}** controlli: solo raccolta dati.")
    lines.append(f"- Da **{MIN_OBSERVATION_CHECKS}** a **{MIN_LIGHT_CALIBRATION_CHECKS - 1}** controlli: osservazione, senza modificare il modello.")
    lines.append(f"- Da **{MIN_LIGHT_CALIBRATION_CHECKS}** a **{MIN_STRONG_CALIBRATION_CHECKS - 1}** controlli: può suggerire correzioni leggere.")
    lines.append(f"- Da **{MIN_STRONG_CALIBRATION_CHECKS}+** controlli: può diventare utile per correggere rischio spot/leva nel Decision Report.")
    lines.append("")

    lines.append("## Ultima lettura rischio salvata")
    lines.append("")
    latest_table = build_latest_table(log_df)
    lines.append(df_to_markdown(latest_table))
    lines.append("")

    lines.append("## Stato calibrazione rischio")
    lines.append("")
    lines.append(df_to_markdown(build_metrics_table(metrics)))
    lines.append("")

    checked_examples = build_checked_examples_table(log_df)

    if not checked_examples.empty:
        lines.append("## Ultimi controlli completati")
        lines.append("")
        lines.append(df_to_markdown(checked_examples))
        lines.append("")

    lines.append("## Come leggerlo")
    lines.append("")
    lines.append("- **Drawdown normale hit**: quante volte il prezzo ha toccato la discesa normale prevista.")
    lines.append("- **Drawdown brutto hit**: quante volte il prezzo ha toccato la zona brutta prevista.")
    lines.append("- **Drawdown molto brutto hit**: quante volte è stato toccato il rischio estremo.")
    lines.append("- Se il drawdown brutto viene toccato spesso, il rischio alto era giustificato.")
    lines.append("- Se il drawdown normale non viene quasi mai toccato, il rischio potrebbe essere troppo severo.")
    lines.append("- Se il drawdown molto brutto viene toccato spesso, il modello stava forse sottovalutando il rischio.")
    lines.append("")
    lines.append("## Traduzione pratica")
    lines.append("")
    lines.append("- Per spot, un drawdown profondo è dolore e rischio di timing, ma non liquidazione.")
    lines.append("- Per leva, lo stesso drawdown può chiudere la posizione anche se poi il prezzo recupera.")
    lines.append("- Per questo il report separa rischio spot e rischio leva.")
    lines.append("")

    return "\n".join(lines) + "\n"


def render_latest_block(log_df, metrics):
    lines = []

    lines.append("# Calibrazione rischio spot / leva")
    lines.append("")
    lines.append("Report completo: [risk_calibration_report.md](risk_calibration_report.md)")
    lines.append("")
    lines.append("Questo blocco controlla se le zone di rischio previste dallo scanner vengono davvero toccate nei 30 giorni successivi.")
    lines.append("")

    if metrics is None or metrics.empty:
        lines.append("_Dati ancora non disponibili._")
        lines.append("")
        return "\n".join(lines)

    lines.append(df_to_markdown(build_metrics_table(metrics)))
    lines.append("")
    lines.append("Regola: sotto 60 controlli osserva soltanto; da 100+ controlli può diventare utile per correggere rischio spot/leva nel Decision Report.")
    lines.append("")

    latest = latest_snapshot(log_df)

    if not latest.empty:
        lines.append("## Ultima lettura rapida")
        lines.append("")
        rows = []

        for _, r in latest.iterrows():
            asset = r["asset"]

            rows.append({
                "Asset": asset,
                "Rischio spot": r.get("spot_risk_label", "n/a"),
                "Rischio leva": r.get("leverage_risk_label", "n/a"),
                "Nota leva": r.get("leverage_note", "n/a"),
            })

        lines.append(df_to_markdown(pd.DataFrame(rows)))
        lines.append("")

    return "\n".join(lines)


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
        anchors = [
            "<!-- GLOBAL_WEIGHT_CALIBRATION_END -->",
            "<!-- MODULE_ACCURACY_END -->",
            "<!-- CALIBRATION_READABLE_END -->",
            "<!-- DECISION_REPORT_END -->",
        ]

        inserted = False
        new = old

        for anchor in anchors:
            if anchor in old:
                idx = old.find(anchor) + len(anchor)
                new = old[:idx] + "\n\n" + new_section + old[idx:]
                inserted = True
                break

        if not inserted:
            new = old.rstrip() + "\n\n" + new_section + "\n"

    LATEST_REPORT.write_text(new, encoding="utf-8")


def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    today_df = build_today_snapshot()
    log_df = append_today_snapshot(today_df)
    log_df = update_risk_checks(log_df)

    metrics = summarize_metrics(log_df)

    if metrics is not None and not metrics.empty:
        metrics.to_csv(OUTPUT_METRICS, index=False)
    else:
        pd.DataFrame(columns=[
            "asset",
            "snapshots_saved",
            "checked_30d",
            "pending",
            "calibration_stage",
            "stage_note",
            "normal_drawdown_hit_rate_pct",
            "bad_drawdown_hit_rate_pct",
            "very_bad_drawdown_hit_rate_pct",
            "normal_max_gain_hit_rate_pct",
            "good_max_gain_hit_rate_pct",
            "very_good_max_gain_hit_rate_pct",
            "avg_actual_return_30d_pct",
            "avg_actual_drawdown_pct",
            "avg_actual_max_gain_pct",
            "risk_calibration_bias",
            "can_influence_decision",
            "can_strongly_influence_decision",
        ]).to_csv(OUTPUT_METRICS, index=False)

    report_md = render_report(log_df, metrics)
    OUTPUT_REPORT.write_text(report_md, encoding="utf-8")

    latest_block = render_latest_block(log_df, metrics)
    inject_into_latest_report(latest_block)

    print(f"Creato/aggiornato {RISK_LOG}")
    print(f"Creato {OUTPUT_METRICS}")
    print(f"Creato {OUTPUT_REPORT}")

    if today_df is None or today_df.empty:
        print("Attenzione: nessuna lettura rischio estratta dal latest_report.md.")
    else:
        print(f"Snapshot rischio salvati oggi: {len(today_df)}")


if __name__ == "__main__":
    main()
