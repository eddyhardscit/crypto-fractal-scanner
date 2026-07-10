import csv
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf


REPORTS_DIR = Path("reports")
LATEST_REPORT_PATH = REPORTS_DIR / "latest_report.md"

REPORT_PATH = REPORTS_DIR / "extreme_cases_path_report.md"
METRICS_CSV_PATH = REPORTS_DIR / "extreme_cases_path_metrics.csv"
PATHS_CSV_PATH = REPORTS_DIR / "extreme_cases_path_points.csv"

START_MARKER = "<!-- EXTREME_CASES_PATH_START -->"
END_MARKER = "<!-- EXTREME_CASES_PATH_END -->"

ASSETS = ["BTC", "SOL", "DOGE"]

ASSET_NAMES = {
    "BTC": "Bitcoin",
    "SOL": "Solana",
    "DOGE": "Dogecoin",
}

TARGET_TICKERS = {
    "BTC": "BTC-USD",
    "SOL": "SOL-USD",
    "DOGE": "DOGE-USD",
}

TICKER_TO_ASSET = {
    "BTC-USD": "BTC",
    "SOL-USD": "SOL",
    "DOGE-USD": "DOGE",
}

MATCH_CSV_CANDIDATES = [
    REPORTS_DIR / "latest_scanner_matches.csv",
    REPORTS_DIR / "scanner_matches.csv",
    REPORTS_DIR / "fractal_matches.csv",
    REPORTS_DIR / "latest_matches.csv",
    REPORTS_DIR / "scanner_results.csv",
]

EXTREME_THRESHOLD = 80.0
DAYS_FORWARD = 30
DOWNLOAD_PADDING_DAYS = 60


def now_utc_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def now_utc_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


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

    scanner_forecast_end = "<!-- SCANNER_FORECAST_TRACKER_END -->"
    if scanner_forecast_end in text:
        return text.replace(scanner_forecast_end, scanner_forecast_end + "\n\n" + full_block, 1)

    bounce_end = "<!-- BOUNCE_AFTER_DRAWDOWN_END -->"
    if bounce_end in text:
        return text.replace(bounce_end, bounce_end + "\n\n" + full_block, 1)

    daily_change_end = "<!-- DAILY_CHANGE_END -->"
    if daily_change_end in text:
        return text.replace(daily_change_end, daily_change_end + "\n\n" + full_block, 1)

    return text.rstrip() + "\n\n" + full_block + "\n"


def safe_str(value, default="") -> str:
    if value is None:
        return default

    try:
        if pd.isna(value):
            return default
    except Exception:
        pass

    return str(value)


def safe_float(value, default=np.nan):
    try:
        if value is None:
            return default

        if isinstance(value, str):
            s = value.strip()
            if not s or s.lower() in {"nan", "none", "n/a", "null", "-"}:
                return default

            s = s.replace("%", "")
            s = s.replace("$", "")
            s = s.replace(" ", "")

            if "," in s:
                s = s.replace(".", "")
                s = s.replace(",", ".")

            return float(s)

        if pd.isna(value):
            return default

        return float(value)

    except Exception:
        return default


def fmt_pct(value, decimals: int = 2) -> str:
    if value is None or pd.isna(value):
        return "n/a"
    return f"{float(value):+.{decimals}f}%".replace(".", ",")


def fmt_pct_plain(value, decimals: int = 2) -> str:
    if value is None or pd.isna(value):
        return "n/a"
    return f"{float(value):.{decimals}f}%".replace(".", ",")


def fmt_int(value) -> str:
    if value is None or pd.isna(value):
        return "0"
    return str(int(value))


def md_table(headers, rows) -> str:
    out = []
    out.append("| " + " | ".join(headers) + " |")
    out.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for row in rows:
        out.append("| " + " | ".join(str(x) for x in row) + " |")
    return "\n".join(out)


def normalize_asset(value: str) -> str:
    s = safe_str(value).upper().strip()

    if s in ASSETS:
        return s

    if s in TICKER_TO_ASSET:
        return TICKER_TO_ASSET[s]

    if "BTC" in s:
        return "BTC"
    if "SOL" in s:
        return "SOL"
    if "DOGE" in s:
        return "DOGE"

    return s


def normalize_ticker(value: str) -> str:
    s = safe_str(value).upper().strip()

    if not s:
        return ""

    if s in ASSETS:
        return TARGET_TICKERS.get(s, s)

    if "-" not in s and s not in ASSETS:
        return f"{s}-USD"

    return s


def clean_header(value: str) -> str:
    s = safe_str(value).strip().lower()
    s = s.replace(" ", "_")
    s = s.replace("-", "_")
    s = s.replace(".", "")
    s = s.replace("%", "pct")
    return s


def is_separator_row(cells) -> bool:
    joined = "".join(cells)
    joined = joined.replace(":", "").replace("-", "").replace("|", "").strip()
    return joined == ""


def split_md_row(line: str):
    line = line.strip()
    if not line.startswith("|"):
        return []
    parts = [p.strip() for p in line.strip("|").split("|")]
    return parts


def extract_asset_technical_section(text: str, asset: str) -> str:
    asset_name = ASSET_NAMES[asset]
    ticker = TARGET_TICKERS[asset]

    pattern = re.compile(
        rf"# Approfondimento tecnico — {re.escape(asset_name)} \({re.escape(ticker)}\)(.*?)(?=\n---\n# Approfondimento tecnico|\n---\n\n# Approfondimento tecnico|\n<!--|\Z)",
        flags=re.DOTALL,
    )

    m = pattern.search(text)
    if m:
        return m.group(1)

    pattern2 = re.compile(
        rf"# {re.escape(asset_name)} .*?(.*?)(?=\n---|\n<!--|\Z)",
        flags=re.DOTALL,
    )

    m2 = pattern2.search(text)
    if m2:
        return m2.group(1)

    return ""


def parse_positive_negative_rates(text: str, asset: str):
    section = extract_asset_technical_section(text, asset)

    if not section:
        section = text

    positive_patterns = [
        r"Casi positivi dopo 30 giorni:\s*\*\*([+\-]?\d+(?:[,.]\d+)?)%\*\*",
        r"Casi positivi / salita storica:\s*\*\*([+\-]?\d+(?:[,.]\d+)?)%\*\*",
        r"Probabilità storica di salita:\s*\*\*([+\-]?\d+(?:[,.]\d+)?)%\*\*",
    ]

    negative_patterns = [
        r"Casi negativi dopo 30 giorni:\s*\*\*([+\-]?\d+(?:[,.]\d+)?)%\*\*",
        r"Casi negativi / discesa storica:\s*\*\*([+\-]?\d+(?:[,.]\d+)?)%\*\*",
        r"Probabilità storica di discesa:\s*\*\*([+\-]?\d+(?:[,.]\d+)?)%\*\*",
    ]

    positive = np.nan
    negative = np.nan

    for p in positive_patterns:
        m = re.search(p, section, flags=re.IGNORECASE)
        if m:
            positive = safe_float(m.group(1))
            break

    for p in negative_patterns:
        m = re.search(p, section, flags=re.IGNORECASE)
        if m:
            negative = safe_float(m.group(1))
            break

    return positive, negative


def parse_matches_from_latest_report(text: str):
    rows = []

    for asset in ASSETS:
        section = extract_asset_technical_section(text, asset)
        if not section:
            continue

        lines = section.splitlines()

        table_lines = []
        inside_match_table = False

        for line in lines:
            if "similar_asset" in line and "return_30d" in line:
                inside_match_table = True
                table_lines.append(line)
                continue

            if inside_match_table:
                if line.strip().startswith("|"):
                    table_lines.append(line)
                else:
                    if table_lines:
                        break

        if len(table_lines) < 3:
            continue

        header = split_md_row(table_lines[0])
        headers = [clean_header(h) for h in header]

        for line in table_lines[1:]:
            cells = split_md_row(line)
            if not cells:
                continue
            if is_separator_row(cells):
                continue
            if len(cells) != len(headers):
                continue

            row = dict(zip(headers, cells))

            similar_asset = normalize_ticker(row.get("similar_asset", ""))
            start_date = safe_str(row.get("start_date"))
            end_date = safe_str(row.get("end_date"))

            if not similar_asset or not end_date:
                continue

            rows.append(
                {
                    "source": "latest_report_fallback_top_table",
                    "target_asset": asset,
                    "similar_asset": similar_asset,
                    "start_date": start_date,
                    "end_date": end_date,
                    "similarity": safe_float(row.get("similarity")),
                    "return_30d": safe_float(row.get("return_30d")),
                    "drawdown_30d": safe_float(row.get("drawdown_30d")),
                    "max_gain_30d": safe_float(row.get("max_gain_30d")),
                }
            )

    return pd.DataFrame(rows)


def read_matches_from_csv_candidate(path: Path):
    if not path.exists():
        return pd.DataFrame()

    try:
        df = pd.read_csv(path)
    except Exception:
        return pd.DataFrame()

    if df.empty:
        return pd.DataFrame()

    cols = {clean_header(c): c for c in df.columns}

    similar_col = cols.get("similar_asset") or cols.get("matched_asset") or cols.get("asset_match")
    end_col = cols.get("end_date") or cols.get("match_end_date")
    start_col = cols.get("start_date") or cols.get("match_start_date")
    target_col = cols.get("target_asset") or cols.get("target") or cols.get("asset") or cols.get("target_ticker")
    similarity_col = cols.get("similarity")
    return_col = cols.get("return_30d") or cols.get("future_return_30d")
    drawdown_col = cols.get("drawdown_30d") or cols.get("future_drawdown_30d")
    max_gain_col = cols.get("max_gain_30d") or cols.get("future_max_gain_30d")

    required = [similar_col, end_col, target_col, return_col]
    if any(c is None for c in required):
        return pd.DataFrame()

    rows = []

    for _, r in df.iterrows():
        target_asset = normalize_asset(r.get(target_col))
        similar_asset = normalize_ticker(r.get(similar_col))
        end_date = safe_str(r.get(end_col))
        start_date = safe_str(r.get(start_col)) if start_col else ""

        if target_asset not in ASSETS:
            continue

        if not similar_asset or not end_date:
            continue

        rows.append(
            {
                "source": path.name,
                "target_asset": target_asset,
                "similar_asset": similar_asset,
                "start_date": start_date,
                "end_date": end_date,
                "similarity": safe_float(r.get(similarity_col)) if similarity_col else np.nan,
                "return_30d": safe_float(r.get(return_col)),
                "drawdown_30d": safe_float(r.get(drawdown_col)) if drawdown_col else np.nan,
                "max_gain_30d": safe_float(r.get(max_gain_col)) if max_gain_col else np.nan,
            }
        )

    return pd.DataFrame(rows)


def load_matches(latest_text: str):
    for path in MATCH_CSV_CANDIDATES:
        df = read_matches_from_csv_candidate(path)
        if not df.empty:
            return df, f"CSV completo: {path.name}"

    fallback = parse_matches_from_latest_report(latest_text)
    if not fallback.empty:
        return fallback, "Fallback latest_report.md: usa solo i match mostrati nel report"

    return pd.DataFrame(), "Nessun match trovato"


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


_PRICE_CACHE = {}


def download_ticker_window(ticker: str, start_date: str, end_date: str):
    ticker = normalize_ticker(ticker)

    key = (ticker, start_date, end_date)
    if key in _PRICE_CACHE:
        return _PRICE_CACHE[key]

    try:
        df = yf.download(
            ticker,
            start=start_date,
            end=end_date,
            interval="1d",
            auto_adjust=False,
            progress=False,
            threads=False,
        )
        out = normalize_yfinance_df(df)
    except Exception:
        out = pd.DataFrame()

    _PRICE_CACHE[key] = out
    return out


def get_path_for_match(row):
    ticker = normalize_ticker(row["similar_asset"])

    try:
        end_date = pd.to_datetime(row["end_date"]).date()
    except Exception:
        return None

    start_download = (end_date - timedelta(days=5)).isoformat()
    end_download = (end_date + timedelta(days=DOWNLOAD_PADDING_DAYS)).isoformat()

    df = download_ticker_window(ticker, start_download, end_download)

    if df.empty:
        return None

    match_ts = pd.Timestamp(end_date)
    candidates = df.index[df.index >= match_ts]

    if len(candidates) == 0:
        return None

    day0_idx = candidates[0]
    loc = df.index.get_loc(day0_idx)

    future = df.iloc[loc : loc + DAYS_FORWARD + 1].copy()

    if len(future) < 8:
        return None

    base_price = float(future["Close"].iloc[0])

    if base_price <= 0:
        return None

    path = []

    for i, (_, r) in enumerate(future.iterrows()):
        if i > DAYS_FORWARD:
            break

        close = float(r["Close"])
        high = float(r["High"])
        low = float(r["Low"])

        path.append(
            {
                "day": i,
                "date": future.index[i].strftime("%Y-%m-%d"),
                "close_return_pct": (close / base_price - 1) * 100,
                "high_return_pct": (high / base_price - 1) * 100,
                "low_return_pct": (low / base_price - 1) * 100,
            }
        )

    if len(path) < 8:
        return None

    return {
        "ticker": ticker,
        "match_end_date": day0_idx.strftime("%Y-%m-%d"),
        "base_price": base_price,
        "path": path,
    }


def build_paths_for_asset(asset: str, direction: str, matches: pd.DataFrame):
    asset_matches = matches[matches["target_asset"] == asset].copy()

    if asset_matches.empty:
        return [], pd.DataFrame()

    if direction == "positive":
        selected = asset_matches[asset_matches["return_30d"] > 0].copy()
    else:
        selected = asset_matches[asset_matches["return_30d"] < 0].copy()

    selected = selected.sort_values("similarity", ascending=False)

    paths = []
    path_points = []

    for match_id, (_, row) in enumerate(selected.iterrows(), start=1):
        result = get_path_for_match(row)

        if result is None:
            continue

        ticker = result["ticker"]

        final_return = np.nan
        if result["path"]:
            final_return = result["path"][-1]["close_return_pct"]

        match_info = {
            "match_id": match_id,
            "target_asset": asset,
            "direction": direction,
            "similar_asset": ticker,
            "start_date": safe_str(row.get("start_date")),
            "end_date": safe_str(row.get("end_date")),
            "match_end_date_used": result["match_end_date"],
            "similarity": safe_float(row.get("similarity")),
            "return_30d_report": safe_float(row.get("return_30d")),
            "drawdown_30d_report": safe_float(row.get("drawdown_30d")),
            "max_gain_30d_report": safe_float(row.get("max_gain_30d")),
            "final_return_path": final_return,
            "base_price": result["base_price"],
        }

        paths.append(
            {
                "info": match_info,
                "path": result["path"],
            }
        )

        for p in result["path"]:
            point = dict(match_info)
            point.update(p)
            path_points.append(point)

    return paths, pd.DataFrame(path_points)


def paths_to_matrix(paths):
    if not paths:
        return pd.DataFrame()

    data = {}

    for p in paths:
        label = f"{p['info']['similar_asset']} {p['info']['end_date']}"
        series = {}
        for point in p["path"]:
            series[int(point["day"])] = float(point["close_return_pct"])
        data[label] = series

    matrix = pd.DataFrame(data).sort_index()
    matrix = matrix.reindex(range(0, DAYS_FORWARD + 1))

    return matrix


def plot_paths(asset: str, direction: str, paths):
    matrix = paths_to_matrix(paths)

    if matrix.empty:
        return None

    image_path = REPORTS_DIR / f"extreme_cases_{asset}_{direction}_paths.png"

    days = matrix.index.values

    p10 = matrix.quantile(0.10, axis=1)
    p25 = matrix.quantile(0.25, axis=1)
    p50 = matrix.quantile(0.50, axis=1)
    p75 = matrix.quantile(0.75, axis=1)
    p90 = matrix.quantile(0.90, axis=1)
    mean = matrix.mean(axis=1)

    fig, ax = plt.subplots(figsize=(13, 7))

    for col in matrix.columns:
        ax.plot(days, matrix[col].values, linewidth=0.8, alpha=0.25)

    ax.fill_between(days, p10.values, p90.values, alpha=0.12, label="Banda p10-p90")
    ax.fill_between(days, p25.values, p75.values, alpha=0.20, label="Banda p25-p75")

    ax.plot(days, p50.values, linewidth=2.4, label="Mediana p50")
    ax.plot(days, mean.values, linewidth=1.8, linestyle="--", label="Media")

    ax.axhline(0, linewidth=1.0, linestyle=":")
    ax.axvline(7, linewidth=0.8, linestyle=":")
    ax.axvline(14, linewidth=0.8, linestyle=":")
    ax.axvline(30, linewidth=0.8, linestyle=":")

    direction_label = "rialzisti" if direction == "positive" else "ribassisti"

    ax.set_title(f"{asset} — percorso dei casi storici {direction_label} simili")
    ax.set_xlabel("Giorni dopo il match")
    ax.set_ylabel("Return dal giorno 0")
    ax.grid(True, alpha=0.25)
    ax.legend(loc="best")

    plt.tight_layout()
    fig.savefig(image_path, dpi=160, bbox_inches="tight")
    plt.close(fig)

    return image_path


def plot_distribution(asset: str, direction: str, paths):
    if not paths:
        return None

    finals = []

    for p in paths:
        if p["path"]:
            finals.append(float(p["path"][-1]["close_return_pct"]))

    finals = [x for x in finals if not pd.isna(x)]

    if not finals:
        return None

    image_path = REPORTS_DIR / f"extreme_cases_{asset}_{direction}_distribution.png"

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.hist(finals, bins=min(12, max(5, len(finals))), alpha=0.75)
    ax.axvline(np.median(finals), linewidth=2.0, linestyle="--", label="Mediana")
    ax.axvline(np.mean(finals), linewidth=2.0, linestyle=":", label="Media")
    ax.axvline(0, linewidth=1.0, linestyle="-")

    direction_label = "rialzisti" if direction == "positive" else "ribassisti"

    ax.set_title(f"{asset} — distribuzione return 30g dei casi {direction_label}")
    ax.set_xlabel("Return 30 giorni")
    ax.set_ylabel("Numero casi")
    ax.grid(True, alpha=0.25)
    ax.legend(loc="best")

    plt.tight_layout()
    fig.savefig(image_path, dpi=160, bbox_inches="tight")
    plt.close(fig)

    return image_path


def summarize_paths(paths):
    if not paths:
        return {
            "cases_used": 0,
            "median_7d": np.nan,
            "median_14d": np.nan,
            "median_30d": np.nan,
            "mean_30d": np.nan,
            "p10_30d": np.nan,
            "p25_30d": np.nan,
            "p75_30d": np.nan,
            "p90_30d": np.nan,
            "median_drawdown": np.nan,
            "median_max_gain": np.nan,
        }

    matrix = paths_to_matrix(paths)

    if matrix.empty:
        return {
            "cases_used": 0,
            "median_7d": np.nan,
            "median_14d": np.nan,
            "median_30d": np.nan,
            "mean_30d": np.nan,
            "p10_30d": np.nan,
            "p25_30d": np.nan,
            "p75_30d": np.nan,
            "p90_30d": np.nan,
            "median_drawdown": np.nan,
            "median_max_gain": np.nan,
        }

    day_7 = matrix.loc[7].dropna() if 7 in matrix.index else pd.Series(dtype=float)
    day_14 = matrix.loc[14].dropna() if 14 in matrix.index else pd.Series(dtype=float)
    day_30 = matrix.loc[30].dropna() if 30 in matrix.index else matrix.iloc[-1].dropna()

    drawdowns = []
    max_gains = []

    for col in matrix.columns:
        s = matrix[col].dropna()
        if s.empty:
            continue
        drawdowns.append(float(s.min()))
        max_gains.append(float(s.max()))

    return {
        "cases_used": int(len(matrix.columns)),
        "median_7d": float(day_7.median()) if not day_7.empty else np.nan,
        "median_14d": float(day_14.median()) if not day_14.empty else np.nan,
        "median_30d": float(day_30.median()) if not day_30.empty else np.nan,
        "mean_30d": float(day_30.mean()) if not day_30.empty else np.nan,
        "p10_30d": float(day_30.quantile(0.10)) if not day_30.empty else np.nan,
        "p25_30d": float(day_30.quantile(0.25)) if not day_30.empty else np.nan,
        "p75_30d": float(day_30.quantile(0.75)) if not day_30.empty else np.nan,
        "p90_30d": float(day_30.quantile(0.90)) if not day_30.empty else np.nan,
        "median_drawdown": float(np.median(drawdowns)) if drawdowns else np.nan,
        "median_max_gain": float(np.median(max_gains)) if max_gains else np.nan,
    }


def determine_triggers(latest_text: str, matches: pd.DataFrame):
    triggers = []

    for asset in ASSETS:
        positive_rate, negative_rate = parse_positive_negative_rates(latest_text, asset)

        asset_matches = matches[matches["target_asset"] == asset].copy()

        if pd.isna(positive_rate) and not asset_matches.empty:
            total = len(asset_matches)
            if total > 0:
                positive_rate = (asset_matches["return_30d"] > 0).sum() / total * 100

        if pd.isna(negative_rate) and not asset_matches.empty:
            total = len(asset_matches)
            if total > 0:
                negative_rate = (asset_matches["return_30d"] < 0).sum() / total * 100

        if not pd.isna(positive_rate) and positive_rate >= EXTREME_THRESHOLD:
            triggers.append(
                {
                    "asset": asset,
                    "direction": "positive",
                    "rate": positive_rate,
                    "opposite_rate": negative_rate,
                    "trigger": True,
                    "reason": f"Casi positivi {fmt_pct_plain(positive_rate)} >= {EXTREME_THRESHOLD:.0f}%",
                }
            )

        if not pd.isna(negative_rate) and negative_rate >= EXTREME_THRESHOLD:
            triggers.append(
                {
                    "asset": asset,
                    "direction": "negative",
                    "rate": negative_rate,
                    "opposite_rate": positive_rate,
                    "trigger": True,
                    "reason": f"Casi negativi {fmt_pct_plain(negative_rate)} >= {EXTREME_THRESHOLD:.0f}%",
                }
            )

        if (
            (pd.isna(positive_rate) or positive_rate < EXTREME_THRESHOLD)
            and (pd.isna(negative_rate) or negative_rate < EXTREME_THRESHOLD)
        ):
            triggers.append(
                {
                    "asset": asset,
                    "direction": "none",
                    "rate": max(
                        positive_rate if not pd.isna(positive_rate) else -999,
                        negative_rate if not pd.isna(negative_rate) else -999,
                    ),
                    "opposite_rate": np.nan,
                    "trigger": False,
                    "reason": "Nessun lato sopra soglia estrema",
                }
            )

    return triggers


def analyze(latest_text: str):
    matches, source_label = load_matches(latest_text)

    triggers = determine_triggers(latest_text, matches)

    results = []
    all_path_points = []

    for trig in triggers:
        asset = trig["asset"]
        direction = trig["direction"]

        if not trig["trigger"]:
            results.append(
                {
                    **trig,
                    "source_label": source_label,
                    "matches_available": int(len(matches[matches["target_asset"] == asset])) if not matches.empty else 0,
                    "cases_used": 0,
                    "path_image": "",
                    "distribution_image": "",
                    "summary": summarize_paths([]),
                    "paths": [],
                }
            )
            continue

        paths, path_points = build_paths_for_asset(asset, direction, matches)

        path_image = plot_paths(asset, direction, paths)
        distribution_image = plot_distribution(asset, direction, paths)

        summary = summarize_paths(paths)

        if not path_points.empty:
            all_path_points.append(path_points)

        results.append(
            {
                **trig,
                "source_label": source_label,
                "matches_available": int(len(matches[matches["target_asset"] == asset])) if not matches.empty else 0,
                "cases_used": summary["cases_used"],
                "path_image": path_image.name if path_image else "",
                "distribution_image": distribution_image.name if distribution_image else "",
                "summary": summary,
                "paths": paths,
            }
        )

    if all_path_points:
        points_df = pd.concat(all_path_points, ignore_index=True)
    else:
        points_df = pd.DataFrame()

    return results, matches, points_df, source_label


def build_report(results, matches, source_label):
    generated = now_utc_str()

    trigger_rows = []

    for r in results:
        direction_label = {
            "positive": "POSITIVO / RIALZISTA",
            "negative": "NEGATIVO / RIBASSISTA",
            "none": "NESSUNO",
        }.get(r["direction"], r["direction"])

        trigger_rows.append(
            [
                r["asset"],
                direction_label,
                "SI" if r["trigger"] else "NO",
                fmt_pct_plain(r["rate"]) if not pd.isna(r["rate"]) and r["rate"] > -900 else "n/a",
                r["reason"],
                str(r["matches_available"]),
                str(r["cases_used"]),
            ]
        )

    lines = []

    lines.append("# Extreme cases path report")
    lines.append("")
    lines.append(f"Generato: {generated}")
    lines.append("")
    lines.append(
        "Questo report crea grafici solo quando lo scanner mostra una percentuale estrema: "
        f"casi positivi o negativi almeno pari a **{EXTREME_THRESHOLD:.0f}%**."
    )
    lines.append("")
    lines.append("Obiettivo: non guardare solo la percentuale finale, ma vedere **come si sono mossi dopo** i casi storici simili.")
    lines.append("")
    lines.append(f"Fonte match: **{source_label}**")
    lines.append("")

    if "Fallback" in source_label:
        lines.append(
            "Nota: in modalità fallback il report usa solo i match visibili nel `latest_report.md`. "
            "Per vedere davvero tutti i 40 casi serve aggiornare `scanner.py` per esportare `reports/latest_scanner_matches.csv`."
        )
        lines.append("")

    lines.append("## Trigger estremi")
    lines.append("")
    lines.append(
        md_table(
            [
                "Asset",
                "Direzione",
                "Trigger",
                "Percentuale",
                "Motivo",
                "Match disponibili",
                "Casi usati nel grafico",
            ],
            trigger_rows,
        )
    )

    for r in results:
        if not r["trigger"]:
            continue

        asset = r["asset"]
        direction = r["direction"]
        summary = r["summary"]

        direction_label = "rialzisti" if direction == "positive" else "ribassisti"

        lines.append("")
        lines.append(f"## {asset} — casi {direction_label}")
        lines.append("")
        lines.append(f"- Trigger: **{r['reason']}**")
        lines.append(f"- Casi disponibili: **{r['matches_available']}**")
        lines.append(f"- Casi usati nei grafici: **{summary['cases_used']}**")
        lines.append(f"- Return mediano 7g: **{fmt_pct(summary['median_7d'])}**")
        lines.append(f"- Return mediano 14g: **{fmt_pct(summary['median_14d'])}**")
        lines.append(f"- Return mediano 30g: **{fmt_pct(summary['median_30d'])}**")
        lines.append(f"- Return medio 30g: **{fmt_pct(summary['mean_30d'])}**")
        lines.append(f"- Drawdown mediano durante il percorso: **{fmt_pct(summary['median_drawdown'])}**")
        lines.append(f"- Max gain mediano durante il percorso: **{fmt_pct(summary['median_max_gain'])}**")
        lines.append("")
        lines.append("### Distribuzione 30 giorni")
        lines.append("")
        lines.append(
            md_table(
                ["P10", "P25", "P50", "P75", "P90"],
                [
                    [
                        fmt_pct(summary["p10_30d"]),
                        fmt_pct(summary["p25_30d"]),
                        fmt_pct(summary["median_30d"]),
                        fmt_pct(summary["p75_30d"]),
                        fmt_pct(summary["p90_30d"]),
                    ]
                ],
            )
        )

        if r["path_image"]:
            lines.append("")
            lines.append(f"![Extreme path {asset} {direction}]({r['path_image']})")

        if r["distribution_image"]:
            lines.append("")
            lines.append(f"![Extreme distribution {asset} {direction}]({r['distribution_image']})")

        if r["paths"]:
            rows = []
            for p in r["paths"][:20]:
                info = p["info"]
                rows.append(
                    [
                        info["similar_asset"],
                        info["start_date"],
                        info["end_date"],
                        fmt_pct_plain(info["similarity"]) if not pd.isna(info["similarity"]) else "n/a",
                        fmt_pct(info["return_30d_report"]),
                        fmt_pct(info["drawdown_30d_report"]),
                        fmt_pct(info["max_gain_30d_report"]),
                        fmt_pct(info["final_return_path"]),
                    ]
                )

            lines.append("")
            lines.append("### Match usati")
            lines.append("")
            lines.append(
                md_table(
                    [
                        "Asset storico",
                        "Start",
                        "End",
                        "Similarity",
                        "Return 30g report",
                        "Drawdown report",
                        "Max gain report",
                        "Return path calcolato",
                    ],
                    rows,
                )
            )

    lines.append("")
    lines.append("## Come leggerlo")
    lines.append("")
    lines.append("- Ogni linea sottile nel grafico è un vecchio caso storico simile.")
    lines.append("- Giorno 0 = giorno in cui il vecchio grafico assomigliava al grafico attuale.")
    lines.append("- Giorni 1-30 = cosa è successo dopo quel vecchio match.")
    lines.append("- La linea mediana mostra il percorso centrale.")
    lines.append("- Le bande p25-p75 e p10-p90 mostrano quanto erano dispersi i percorsi.")
    lines.append("- Per uno scenario ribassista forte, conta molto se la mediana scende subito o solo dopo uno spike.")
    lines.append("")
    lines.append(
        "Nota: questo report è visivo e diagnostico. Non modifica il Global Confluence e non autorizza leva."
    )

    return "\n".join(lines).rstrip() + "\n"


def write_metrics(results):
    fieldnames = [
        "generated_utc",
        "asset",
        "direction",
        "trigger",
        "rate",
        "opposite_rate",
        "reason",
        "source_label",
        "matches_available",
        "cases_used",
        "median_7d",
        "median_14d",
        "median_30d",
        "mean_30d",
        "p10_30d",
        "p25_30d",
        "p75_30d",
        "p90_30d",
        "median_drawdown",
        "median_max_gain",
        "path_image",
        "distribution_image",
    ]

    generated = now_utc_iso()

    rows = []

    for r in results:
        s = r["summary"]
        rows.append(
            {
                "generated_utc": generated,
                "asset": r["asset"],
                "direction": r["direction"],
                "trigger": r["trigger"],
                "rate": r["rate"],
                "opposite_rate": r["opposite_rate"],
                "reason": r["reason"],
                "source_label": r["source_label"],
                "matches_available": r["matches_available"],
                "cases_used": r["cases_used"],
                "median_7d": s["median_7d"],
                "median_14d": s["median_14d"],
                "median_30d": s["median_30d"],
                "mean_30d": s["mean_30d"],
                "p10_30d": s["p10_30d"],
                "p25_30d": s["p25_30d"],
                "p75_30d": s["p75_30d"],
                "p90_30d": s["p90_30d"],
                "median_drawdown": s["median_drawdown"],
                "median_max_gain": s["median_max_gain"],
                "path_image": r["path_image"],
                "distribution_image": r["distribution_image"],
            }
        )

    with METRICS_CSV_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    latest_text = read_text(LATEST_REPORT_PATH)

    if not latest_text:
        report = "# Extreme cases path report\n\nErrore: `reports/latest_report.md` non trovato.\n"
        write_text(REPORT_PATH, report)
        return

    results, matches, points_df, source_label = analyze(latest_text)

    report_md = build_report(results, matches, source_label)

    write_text(REPORT_PATH, report_md)
    write_metrics(results)

    if not points_df.empty:
        points_df.to_csv(PATHS_CSV_PATH, index=False)
    else:
        pd.DataFrame().to_csv(PATHS_CSV_PATH, index=False)

    updated_latest = replace_or_insert_block(latest_text, report_md)
    write_text(LATEST_REPORT_PATH, updated_latest)

    print(f"Extreme cases path report scritto in: {REPORT_PATH}")
    print(f"Metriche scritte in: {METRICS_CSV_PATH}")
    print(f"Punti percorso scritti in: {PATHS_CSV_PATH}")


if __name__ == "__main__":
    main()
