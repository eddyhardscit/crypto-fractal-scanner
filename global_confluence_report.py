from pathlib import Path
from datetime import datetime
import re

import numpy as np
import pandas as pd


REPORTS_DIR = Path("reports")

LATEST_REPORT = REPORTS_DIR / "latest_report.md"
OUTPUT_REPORT = REPORTS_DIR / "global_confluence_report.md"
OUTPUT_METRICS = REPORTS_DIR / "global_confluence_metrics.csv"

TECHNICAL_METRICS = REPORTS_DIR / "technical_structure_metrics.csv"
MARKET_REGIME_SUMMARY = REPORTS_DIR / "market_regime_match_summary.csv"

SCANNER_PATH_METRICS = REPORTS_DIR / "scanner_forecast_path_accuracy_metrics.csv"
FRACTAL_PATH_METRICS = REPORTS_DIR / "fractal_path_accuracy_metrics.csv"

MAJOR_ALT_LIFECYCLE_REPORT = REPORTS_DIR / "major_alt_lifecycle_squeeze_report.md"

START_MARKER = "<!-- GLOBAL_CONFLUENCE_START -->"
END_MARKER = "<!-- GLOBAL_CONFLUENCE_END -->"

ASSETS = ["BTC", "SOL", "DOGE"]

ASSET_NAMES = {
    "BTC": "Bitcoin",
    "SOL": "Solana",
    "DOGE": "Dogecoin",
}


LABELS_IT = {
    "BULLISH_TECNICO": "rialzista tecnico",
    "COSTRUTTIVO_MA_NON_CONFERMATO": "costruttivo ma non confermato",
    "NEUTRALE_MISTO": "neutrale / misto",
    "DEBOLE": "debole",
    "BEARISH_TECNICO": "ribassista tecnico",

    "BULLISH_TREND": "trend rialzista",
    "BEARISH_TREND": "trend ribassista",
    "MIXED_TREND": "trend misto",

    "MOMENTUM_IMPROVING": "momentum in miglioramento",
    "MOMENTUM_WEAK": "momentum debole",
    "MOMENTUM_MIXED": "momentum misto",

    "ACCUMULATION_VOLUME": "volume da accumulazione",
    "DISTRIBUTION_VOLUME": "volume da distribuzione",
    "NEUTRAL_VOLUME": "volume neutrale",

    "HH_HL_UPSTRUCTURE": "struttura rialzista con massimi e minimi crescenti",
    "LH_LL_DOWNSTRUCTURE": "struttura ribassista con massimi e minimi decrescenti",
    "COMPRESSION_TRIANGLE": "compressione / triangolo",
    "EXPANDING_VOLATILITY": "volatilità in espansione",
    "UNKNOWN": "sconosciuto",

    "BULLISH_RSI_DIVERGENCE": "divergenza rialzista RSI",
    "BEARISH_RSI_DIVERGENCE": "divergenza ribassista RSI",
    "HIDDEN_BULLISH_RSI_DIVERGENCE": "divergenza rialzista nascosta RSI",
    "HIDDEN_BEARISH_RSI_DIVERGENCE": "divergenza ribassista nascosta RSI",
    "NONE": "nessuna",

    "ACCUMULATION_CANDIDATE": "possibile accumulazione",
    "DISTRIBUTION_CANDIDATE": "possibile distribuzione",
    "MARKUP": "markup / fase rialzista",
    "MARKDOWN": "markdown / fase ribassista",
    "RANGE_OR_UNKNOWN": "range / fase non chiara",
}


def it_label(value):
    if value is None:
        return "n/a"

    try:
        if pd.isna(value):
            return "n/a"
    except Exception:
        pass

    s = str(value).strip()

    if not s:
        return "n/a"

    if "," in s:
        parts = [p.strip() for p in s.split(",")]
        return ", ".join(LABELS_IT.get(p, p.lower()) for p in parts)

    return LABELS_IT.get(s, s.lower())


def safe_float(x):
    try:
        if pd.isna(x):
            return np.nan
        return float(x)
    except Exception:
        return np.nan


def parse_pct(value):
    if value is None:
        return np.nan

    s = str(value).strip()

    if not s or s.lower() == "nan":
        return np.nan

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


def clamp(value, low, high):
    return int(max(low, min(high, value)))


def fmt_score(x):
    try:
        x = int(x)

        if x > 0:
            return f"+{x}"

        return str(x)

    except Exception:
        return "0"


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


def fmt_price(asset, x):
    x = safe_float(x)

    if pd.isna(x):
        return "n/a"

    if asset == "DOGE":
        return f"{x:.5f}"

    if x >= 1000:
        return f"{x:,.0f}".replace(",", ".")

    return f"{x:.2f}".replace(".", ",")


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


def load_csv(path):
    if not path.exists():
        return pd.DataFrame()

    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


def clean_markdown_text(value):
    if value is None:
        return ""

    s = str(value)

    s = s.replace("**", "")
    s = s.replace("__", "")
    s = s.replace("*", "")
    s = s.replace("`", "")
    s = s.replace("\r", "")
    s = s.strip()

    s = re.sub(r"^[\-\s:|]+", "", s)
    s = re.sub(r"[\s|]+$", "", s)

    return s.strip()


def first_pct_from_text(text):
    if not text:
        return np.nan

    m = re.search(r"([+\-]?[0-9]+(?:[,.][0-9]+)?)\s*%", text)

    if not m:
        return np.nan

    return parse_pct(m.group(1))


def first_price_from_text(text):
    if not text:
        return np.nan

    m = re.search(r"([0-9]+(?:[.,][0-9]+)?)\s*\$", text)

    if not m:
        return np.nan

    return parse_number(m.group(1))


def markdown_line_value(section, label):
    label_low = label.lower()

    for line in section.splitlines():
        clean = clean_markdown_text(line)

        if label_low not in clean.lower():
            continue

        idx = clean.lower().find(label_low)
        value = clean[idx + len(label):]
        value = re.sub(r"^[\s:：\-]+", "", value)
        value = clean_markdown_text(value)

        return value

    return ""


def extract_between(text, start_marker, end_marker):
    if start_marker not in text or end_marker not in text:
        return ""

    start = text.find(start_marker)
    end = text.find(end_marker)

    if start == -1 or end == -1 or end <= start:
        return ""

    start = start + len(start_marker)

    return text[start:end]


def extract_section_from_heading(text, heading, stop_headings=None):
    if stop_headings is None:
        stop_headings = ["\n# ", "\n<!-- "]

    idx = text.find(heading)

    if idx == -1:
        return ""

    rest = text[idx:]

    stop_positions = []

    for stop in stop_headings:
        pos = rest.find(stop, len(heading))

        if pos != -1:
            stop_positions.append(pos)

    if not stop_positions:
        return rest

    return rest[:min(stop_positions)]


def extract_asset_block(text, asset):
    name = ASSET_NAMES.get(asset, asset)

    patterns = [
        rf"^##\s+{re.escape(name)}\s*$\n(.*?)(?=^##\s+|^#\s+|\Z)",
        rf"^#\s+{re.escape(name)}[^\n]*\n(.*?)(?=^#\s+|\Z)",
    ]

    for pat in patterns:
        m = re.search(pat, text, flags=re.DOTALL | re.MULTILINE)

        if m:
            return m.group(1)

    return ""


def load_technical_metrics():
    df = load_csv(TECHNICAL_METRICS)

    if df.empty:
        return {}

    out = {}

    for _, row in df.iterrows():
        asset = str(row.get("asset", row.get("ticker", ""))).upper()
        asset = asset.replace("-USD", "").strip()

        if asset in ASSETS:
            out[asset] = row.to_dict()

    return out


def get_market_row(asset, market_df):
    if market_df is None or market_df.empty:
        return None

    target = f"{asset}-USD"

    if "target" not in market_df.columns or "group" not in market_df.columns:
        return None

    df = market_df.copy()
    df["target"] = df["target"].astype(str)
    df["group"] = df["group"].astype(str)

    asset_df = df[df["target"].str.upper() == target.upper()].copy()

    if asset_df.empty:
        return None

    preferred_groups = [
        "SAME_BTC_AND_ASSET_REGIME",
        "SAME_BTC_REGIME",
        "SAME_ASSET_REGIME",
        "ALL_MATCHES",
    ]

    for group in preferred_groups:
        g = asset_df[asset_df["group"] == group]

        if not g.empty:
            return g.iloc[0].to_dict()

    return asset_df.iloc[0].to_dict()


def extract_positive_negative_and_return(block):
    positive = np.nan
    negative = np.nan
    return_30d = np.nan

    for line in block.splitlines():
        clean = clean_markdown_text(line)
        low = clean.lower()

        if "casi positivi" in low or "probabilità storica di salita" in low:
            pct = first_pct_from_text(clean)

            if not pd.isna(pct):
                positive = pct

        if "casi negativi" in low or "probabilità storica di discesa" in low:
            pct = first_pct_from_text(clean)

            if not pd.isna(pct):
                negative = pct

        if "return normale fra 30 giorni" in low:
            pct = first_pct_from_text(clean)

            if not pd.isna(pct):
                return_30d = pct

    if pd.isna(return_30d):
        m = re.search(
            r"Percentile 50%.*?([+\-0-9,.]+)\s*%\s*→",
            block,
            flags=re.IGNORECASE | re.DOTALL,
        )

        if m:
            return_30d = parse_pct(m.group(1))

    return positive, negative, return_30d


def component_scanner(asset, latest_text):
    fast_section = extract_section_from_heading(
        latest_text,
        "# Lettura velocissima",
        stop_headings=[
            "\n---\n\n# Mappa",
            "\n# Mappa",
            "\n# Controllo",
            "\n<!-- CALIBRATION",
            "\n<!-- LIQUIDATION",
            "\n<!-- MARKET",
            "\n<!-- TECHNICAL",
        ],
    )

    block = ""

    if fast_section:
        block = extract_asset_block(fast_section, asset)

    if not block:
        full_name = ASSET_NAMES.get(asset, asset)
        detailed_heading = f"# {full_name}"
        detailed_section = extract_section_from_heading(
            latest_text,
            detailed_heading,
            stop_headings=["\n---\n\n# Approfondimento", "\n---\n\n# ", "\n# Controllo", "\n<!-- "],
        )
        block = detailed_section

    if not block:
        block = extract_asset_block(latest_text, asset)

    if not block:
        return {
            "score": 0,
            "summary": "Dati scanner non trovati.",
            "positive_rate": np.nan,
            "negative_rate": np.nan,
            "return_30d": np.nan,
        }

    positive, negative, return_30d = extract_positive_negative_and_return(block)

    score = 0

    if not pd.isna(positive):
        if positive >= 60:
            score += 2
        elif positive >= 52:
            score += 1
        elif positive <= 40:
            score -= 2
        elif positive < 48:
            score -= 1

    if not pd.isna(return_30d):
        if return_30d >= 5:
            score += 1
        elif return_30d <= -5:
            score -= 1

    score = clamp(score, -3, 3)

    if pd.isna(positive):
        summary = "Scanner principale non leggibile."
    else:
        summary = f"Casi positivi {fmt_pct(positive)}, return centrale 30g {fmt_pct(return_30d)}."

    return {
        "score": score,
        "summary": summary,
        "positive_rate": positive,
        "negative_rate": negative,
        "return_30d": return_30d,
    }


def component_market_regime(asset, market_df):
    row = get_market_row(asset, market_df)

    if row is None:
        return {
            "score": 0,
            "summary": "Dati market regime non trovati.",
            "group": "",
        }

    group = str(row.get("group", ""))
    matches = parse_number(row.get("matches", np.nan))
    positive = parse_pct(row.get("positive_30d_rate", np.nan))
    return_p50 = parse_pct(row.get("return_30d_p50", np.nan))

    score = 0

    if not pd.isna(matches) and matches >= 5:
        if not pd.isna(positive):
            if positive >= 60:
                score += 2
            elif positive >= 52:
                score += 1
            elif positive <= 40:
                score -= 2
            elif positive < 48:
                score -= 1

        if not pd.isna(return_p50):
            if return_p50 >= 5:
                score += 1
            elif return_p50 <= -5:
                score -= 1
    else:
        score = 0

    score = clamp(score, -3, 3)

    summary = (
        f"Gruppo {group}, match {int(matches) if not pd.isna(matches) else 'n/a'}, "
        f"positivi 30g {fmt_pct(positive)}, return p50 {fmt_pct(return_p50)}."
    )

    return {
        "score": score,
        "summary": summary,
        "group": group,
        "matches": matches,
        "positive_rate": positive,
        "return_p50": return_p50,
    }


def component_technical(asset, technical):
    row = technical.get(asset)

    if not row:
        return {
            "score": 0,
            "summary": "Report tecnico non trovato.",
            "technical_score": np.nan,
        }

    tech_score = safe_float(row.get("technical_score", np.nan))
    verdict = str(row.get("verdict", ""))
    trend = str(row.get("trend", ""))
    structure = str(row.get("structure", ""))
    divergence = str(row.get("divergence", ""))
    wyckoff = str(row.get("wyckoff", ""))

    score = 0

    if not pd.isna(tech_score):
        if tech_score >= 7:
            score = 3
        elif tech_score >= 3:
            score = 2
        elif tech_score >= 0:
            score = 1
        elif tech_score >= -2:
            score = 0
        elif tech_score >= -6:
            score = -2
        else:
            score = -3

    score = clamp(score, -3, 3)

    summary = (
        f"Score tecnico {int(tech_score) if not pd.isna(tech_score) else 'n/a'}/12, "
        f"verdetto {it_label(verdict)}, trend {it_label(trend)}, "
        f"struttura {it_label(structure)}, divergenza {it_label(divergence)}, "
        f"Wyckoff {it_label(wyckoff)}."
    )

    return {
        "score": score,
        "summary": summary,
        "technical_score": tech_score,
        "verdict": verdict,
        "trend": trend,
        "structure": structure,
        "divergence": divergence,
        "wyckoff": wyckoff,
    }


def parse_sol_fractal(latest_text):
    section = extract_between(
        latest_text,
        "<!-- BTC_SOL_FRACTAL_START -->",
        "<!-- BTC_SOL_FRACTAL_END -->",
    )

    if not section:
        section = read_text(REPORTS_DIR / "btc_2022_vs_sol_2026_report.md")

    data = {
        "found": False,
        "score": 0,
        "summary": "Frattale SOL/BTC non trovato.",
        "similarity": np.nan,
        "tracking": "",
        "phase": "",
        "risk": "",
        "verdict": "",
        "first_confirmation": np.nan,
        "second_confirmation": np.nan,
        "soft_invalidation": np.nan,
        "strong_invalidation": np.nan,
    }

    if not section:
        return data

    data["found"] = True

    verdict_line = ""

    for line in section.splitlines():
        clean = clean_markdown_text(line)

        if clean.lower().startswith("# frattale"):
            continue

        if "verdetto:" in clean.lower():
            verdict_line = clean
            break

    if verdict_line:
        data["verdict"] = clean_markdown_text(verdict_line.split(":", 1)[-1])

    similarity_value = markdown_line_value(section, "Somiglianza totale")

    if similarity_value:
        data["similarity"] = first_pct_from_text(similarity_value)

    if pd.isna(data["similarity"]):
        m = re.search(
            r"Somiglianza totale.*?([0-9]+(?:[,.][0-9]+)?)\s*%",
            section,
            flags=re.IGNORECASE | re.DOTALL,
        )

        if m:
            data["similarity"] = parse_pct(m.group(1))

    data["tracking"] = markdown_line_value(section, "Trend tracking")
    data["phase"] = markdown_line_value(section, "Fase attuale")
    data["risk"] = markdown_line_value(section, "Rischio fase")

    def price_after_label(label):
        for line in section.splitlines():
            clean = clean_markdown_text(line)

            if label.lower() not in clean.lower():
                continue

            price = first_price_from_text(clean)

            if not pd.isna(price):
                return price

        pat = rf"{label}.*?([0-9]+(?:[,.][0-9]+)?)\s*\$"
        mm = re.search(pat, section, flags=re.IGNORECASE | re.DOTALL)

        if mm:
            return parse_number(mm.group(1))

        return np.nan

    data["first_confirmation"] = price_after_label("Prima conferma")
    data["second_confirmation"] = price_after_label("Seconda conferma")
    data["soft_invalidation"] = price_after_label("Invalidazione soft")
    data["strong_invalidation"] = price_after_label("Invalidazione forte")

    score = 0

    if "SI" in data["verdict"].upper():
        score += 1

    if not pd.isna(data["similarity"]):
        if data["similarity"] >= 78:
            score += 2
        elif data["similarity"] >= 70:
            score += 1
        elif data["similarity"] < 60:
            score -= 1

    if "STABILE" in data["tracking"].upper():
        score += 1
    elif "ROTTO" in data["tracking"].upper() or "INSTABILE" in data["tracking"].upper():
        score -= 2

    if "ALTO" in data["risk"].upper():
        score -= 1

    score = clamp(score, -3, 3)
    data["score"] = score

    data["summary"] = (
        f"Verdetto {data['verdict'] or 'n/a'}, somiglianza {fmt_pct(data['similarity'])}, "
        f"tracking {data['tracking'] or 'n/a'}, fase {data['phase'] or 'n/a'}, "
        f"rischio {data['risk'] or 'n/a'}."
    )

    return data


def component_fractal(asset, latest_text):
    if asset != "SOL":
        return {
            "score": 0,
            "summary": "Non applicabile a questo asset.",
        }

    return parse_sol_fractal(latest_text)


def component_rsi_top_cycle(asset, latest_text):
    if asset != "SOL":
        return {
            "score": 0,
            "summary": "Non applicabile a questo asset.",
        }

    section = extract_between(
        latest_text,
        "<!-- RSI_TOP_CYCLE_START -->",
        "<!-- RSI_TOP_CYCLE_END -->",
    )

    if not section:
        section = read_text(REPORTS_DIR / "rsi_top_cycle_report.md")

    if not section:
        return {
            "score": 0,
            "summary": "RSI top-cycle non trovato.",
        }

    risk = ""

    for line in section.splitlines():
        clean = clean_markdown_text(line)

        if "Rischio top-cycle RSI" in clean:
            parts = [p.strip() for p in clean.split("|") if p.strip()]

            if len(parts) >= 2:
                risk = parts[1]
            else:
                risk = clean.split(":", 1)[-1].strip() if ":" in clean else ""

            break

    score = 0

    if "BASSO" in risk.upper():
        score = 1
    elif "MEDIO" in risk.upper():
        score = 0
    elif "ALTO" in risk.upper():
        score = -2

    summary = f"Rischio top-cycle RSI: {risk or 'n/a'}."

    return {
        "score": score,
        "summary": summary,
        "risk": risk,
    }


def component_lifecycle_squeeze(asset, latest_text):
    if asset != "SOL":
        return {
            "score": 0,
            "summary": "Non applicabile a questo asset.",
            "found": False,
            "raw_score": np.nan,
            "suggested_weight": 0,
            "bias": "",
            "action": "",
            "trend": "",
            "trend_score": np.nan,
            "ema200_target": np.nan,
            "upside_ema200": np.nan,
            "distance_ema200": np.nan,
            "ema_gap": np.nan,
            "cross_status": "",
            "hit_ema200_12w": np.nan,
            "max_gain_median_12w": np.nan,
            "drawdown_median_12w": np.nan,
        }

    section = extract_between(
        latest_text,
        "<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_START -->",
        "<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->",
    )

    if not section:
        section = read_text(MAJOR_ALT_LIFECYCLE_REPORT)

    if not section:
        return {
            "score": 0,
            "summary": "Major alt lifecycle squeeze / EMA200 non trovato.",
            "found": False,
            "raw_score": np.nan,
            "suggested_weight": 0,
            "bias": "",
            "action": "",
            "trend": "",
            "trend_score": np.nan,
            "ema200_target": np.nan,
            "upside_ema200": np.nan,
            "distance_ema200": np.nan,
            "ema_gap": np.nan,
            "cross_status": "",
            "hit_ema200_12w": np.nan,
            "max_gain_median_12w": np.nan,
            "drawdown_median_12w": np.nan,
        }

    raw_score = parse_number(markdown_line_value(section, "Lifecycle squeeze score"))
    bias = markdown_line_value(section, "Bias")
    action = markdown_line_value(section, "Azione coerente")

    suggested_weight = parse_number(markdown_line_value(section, "Peso suggerito Global"))

    if pd.isna(suggested_weight):
        suggested_weight = parse_number(markdown_line_value(section, "Peso suggerito nel Global"))

    trend = markdown_line_value(section, "Trend squeeze")
    trend_score = parse_number(markdown_line_value(section, "Trend squeeze score"))

    ema200_target = first_price_from_text(markdown_line_value(section, "EMA200 weekly target"))

    if pd.isna(ema200_target):
        ema200_target = first_price_from_text(markdown_line_value(section, "Target tecnico naturale"))

    if pd.isna(ema200_target):
        ema200_target = first_price_from_text(markdown_line_value(section, "EMA200"))

    upside_ema200 = first_pct_from_text(markdown_line_value(section, "Upside verso EMA200"))
    distance_ema200 = first_pct_from_text(markdown_line_value(section, "Distanza prezzo da EMA200"))
    ema_gap = first_pct_from_text(markdown_line_value(section, "Gap EMA50/EMA200"))

    cross_status = markdown_line_value(section, "Stato cross")

    if not cross_status:
        cross_status = markdown_line_value(section, "Stato incrocio")

    if not cross_status:
        cross_status = markdown_line_value(section, "Stato EMA50/EMA200")

    hit_ema200_12w = first_pct_from_text(markdown_line_value(section, "Hit EMA200 12w analoghi"))

    if pd.isna(hit_ema200_12w):
        hit_ema200_12w = first_pct_from_text(markdown_line_value(section, "Probabilità storica hit EMA200 12w"))

    max_gain_median_12w = first_pct_from_text(markdown_line_value(section, "Max gain mediano 12w"))
    drawdown_median_12w = first_pct_from_text(markdown_line_value(section, "Drawdown mediano 12w"))

    if not pd.isna(suggested_weight):
        score = int(round(suggested_weight))
    else:
        score = 0

        if not pd.isna(raw_score):
            if raw_score >= 5:
                score = 1
            elif raw_score <= -3:
                score = -1

        if "SETUP FORTE" in bias.upper():
            score = max(score, 1)

        if "PEGGIORA" in trend.upper() or "INDEBOL" in trend.upper():
            score -= 1

    score = clamp(score, -1, 1)

    summary_parts = []

    if not pd.isna(raw_score):
        summary_parts.append(f"Lifecycle score {int(raw_score)}")

    summary_parts.append(f"peso Global {fmt_score(score)}")

    if bias:
        summary_parts.append(f"bias {bias}")

    if not pd.isna(ema200_target):
        summary_parts.append(f"EMA200 {fmt_price(asset, ema200_target)} $")

    if not pd.isna(upside_ema200):
        summary_parts.append(f"upside EMA200 {fmt_pct(upside_ema200)}")

    if cross_status:
        summary_parts.append(f"stato {cross_status}")

    if not pd.isna(hit_ema200_12w):
        summary_parts.append(f"hit EMA200 12w {fmt_pct(hit_ema200_12w)}")

    if trend:
        summary_parts.append(f"trend {trend}")

    summary = ", ".join(summary_parts) + "."

    return {
        "score": score,
        "summary": summary,
        "found": True,
        "raw_score": raw_score,
        "suggested_weight": suggested_weight,
        "bias": bias,
        "action": action,
        "trend": trend,
        "trend_score": trend_score,
        "ema200_target": ema200_target,
        "upside_ema200": upside_ema200,
        "distance_ema200": distance_ema200,
        "ema_gap": ema_gap,
        "cross_status": cross_status,
        "hit_ema200_12w": hit_ema200_12w,
        "max_gain_median_12w": max_gain_median_12w,
        "drawdown_median_12w": drawdown_median_12w,
    }


def component_futures(asset, latest_text):
    section = extract_between(
        latest_text,
        "<!-- LIQUIDATION_SUMMARY_START -->",
        "<!-- LIQUIDATION_SUMMARY_END -->",
    )

    if not section:
        section = read_text(REPORTS_DIR / "liquidation_report.md")

    if not section:
        return {
            "score": 0,
            "summary": "Futures/liquidazioni non trovati.",
        }

    row = None

    for line in section.splitlines():
        line = line.strip()

        if not line.startswith("|"):
            continue

        cells = [c.strip() for c in line.strip("|").split("|")]

        if not cells:
            continue

        if cells[0].upper() == asset:
            row = cells
            break

    if not row:
        return {
            "score": 0,
            "summary": "Riga futures non trovata.",
        }

    reading = ""
    force = ""

    if len(row) >= 7:
        reading = row[5]
        force = row[6]

    force_num = np.nan
    m = re.search(r"([0-9]+)\s*/\s*5", force)

    if m:
        force_num = parse_number(m.group(1))

    score = 0
    r = reading.lower()

    if not pd.isna(force_num) and force_num >= 4:
        if "ribass" in r or ("long" in r and "rischio" in r):
            score = -1
        elif "rialz" in r or ("short" in r and "rischio" in r):
            score = 1

    if "misto" in r:
        score = 0

    summary = f"Lettura futures {reading or 'n/a'}, forza {force or 'n/a'}."

    return {
        "score": score,
        "summary": summary,
        "reading": reading,
        "force": force,
    }


def component_daily_change(asset, latest_text):
    section = extract_between(
        latest_text,
        "<!-- DAILY_CHANGE_START -->",
        "<!-- DAILY_CHANGE_END -->",
    )

    if not section:
        return {
            "score": 0,
            "summary": "Mini report cambiamenti non trovato.",
        }

    line_found = ""

    for line in section.splitlines():
        if line.strip().startswith(f"- {asset}:"):
            line_found = clean_markdown_text(line.strip())
            break

    score = 0
    low = line_found.lower()

    if "nessun cambiamento forte" in low:
        score = 0
    elif "miglioramento" in low and "cambiamento" in low:
        score = 1
    elif "peggioramento" in low and "cambiamento" in low:
        score = -1

    summary = line_found if line_found else "Nessun cambiamento forte rilevato."

    return {
        "score": score,
        "summary": summary,
    }


def get_best_metric_row(df, asset, horizon_col):
    if df is None or df.empty:
        return None

    if "asset" not in df.columns:
        return None

    d = df[df["asset"].astype(str).str.upper() == asset.upper()].copy()

    if d.empty:
        return None

    if "checked_predictions" not in d.columns:
        return None

    d["checked_predictions_num"] = pd.to_numeric(d["checked_predictions"], errors="coerce").fillna(0)

    d = d.sort_values("checked_predictions_num", ascending=False)

    if d.empty:
        return None

    return d.iloc[0].to_dict()


def score_accuracy_component(n, wide_rate, mid_rate, avg_abs_error, mode="scanner"):
    n = safe_float(n)
    wide_rate = safe_float(wide_rate)
    mid_rate = safe_float(mid_rate)
    avg_abs_error = safe_float(avg_abs_error)

    if pd.isna(n) or n < 5:
        return 0, "RACCOLTA DATI"

    if n < 30:
        if not pd.isna(wide_rate) and not pd.isna(avg_abs_error):
            if wide_rate >= 75 and avg_abs_error <= 12:
                return 1, "CONFERMA LEGGERA"
            if wide_rate < 45 or avg_abs_error > 25:
                return -1, "ALLARME LEGGERO"

        return 0, "RACCOLTA DATI AVANZATA"

    if not pd.isna(wide_rate) and not pd.isna(mid_rate) and not pd.isna(avg_abs_error):
        if wide_rate >= 80 and mid_rate >= 50 and avg_abs_error <= 10:
            return 2, "CONFERMA FORTE"
        if wide_rate >= 65 and avg_abs_error <= 16:
            return 1, "CONFERMA MODERATA"
        if wide_rate < 35 or avg_abs_error > 30:
            return -2, "ALLARME FORTE"
        if wide_rate < 50 or avg_abs_error > 22:
            return -1, "ALLARME MODERATO"

    return 0, "NEUTRALE"


def component_scanner_path(asset):
    df = load_csv(SCANNER_PATH_METRICS)

    if df.empty:
        return {
            "score": 0,
            "summary": "Scanner path non ancora disponibile.",
            "status": "NON DISPONIBILE",
            "checked_predictions": 0,
        }

    row = get_best_metric_row(df, asset, "day_index")

    if row is None:
        return {
            "score": 0,
            "summary": "Scanner path non ancora disponibile per questo asset.",
            "status": "NON DISPONIBILE",
            "checked_predictions": 0,
        }

    n = safe_float(row.get("checked_predictions", 0))
    day = safe_float(row.get("day_index", np.nan))
    wide = safe_float(row.get("inside_p10_p90_rate", np.nan))
    mid = safe_float(row.get("inside_p25_p75_rate", np.nan))
    err = safe_float(row.get("avg_abs_error_vs_p50", np.nan))

    score, status = score_accuracy_component(n, wide, mid, err, mode="scanner")

    if n < 5:
        summary = (
            f"Raccolta dati. Controlli disponibili {int(n) if not pd.isna(n) else 0}. "
            f"Servono almeno 5 controlli prima di pesare il cono previsionale."
        )
    else:
        summary = (
            f"Stato {status}, orizzonte migliore {int(day) if not pd.isna(day) else 'n/a'}g, "
            f"controlli {int(n)}, dentro p10-p90 {fmt_pct(wide)}, "
            f"dentro p25-p75 {fmt_pct(mid)}, errore medio abs vs p50 {fmt_pct(err)}."
        )

    return {
        "score": score,
        "summary": summary,
        "status": status,
        "checked_predictions": n,
        "day_index": day,
        "inside_p10_p90_rate": wide,
        "inside_p25_p75_rate": mid,
        "avg_abs_error_vs_p50": err,
    }


def component_fractal_path(asset):
    if asset != "SOL":
        return {
            "score": 0,
            "summary": "Non applicabile a questo asset.",
            "status": "NON APPLICABILE",
            "checked_predictions": 0,
        }

    df = load_csv(FRACTAL_PATH_METRICS)

    if df.empty:
        return {
            "score": 0,
            "summary": "Fractal path non ancora disponibile.",
            "status": "NON DISPONIBILE",
            "checked_predictions": 0,
        }

    row = get_best_metric_row(df, "SOL", "horizon_days")

    if row is None:
        return {
            "score": 0,
            "summary": "Fractal path non ancora disponibile per SOL.",
            "status": "NON DISPONIBILE",
            "checked_predictions": 0,
        }

    n = safe_float(row.get("checked_predictions", 0))
    horizon = safe_float(row.get("horizon_days", np.nan))
    inside = safe_float(row.get("inside_band_rate", np.nan))
    err = safe_float(row.get("avg_abs_error_pct", np.nan))
    avg_error = safe_float(row.get("avg_error_pct", np.nan))

    score, status = score_accuracy_component(
        n=n,
        wide_rate=inside,
        mid_rate=inside,
        avg_abs_error=err,
        mode="fractal",
    )

    if n < 5:
        summary = (
            f"Raccolta dati. Controlli disponibili {int(n) if not pd.isna(n) else 0}. "
            f"Servono almeno 5 controlli prima di pesare il percorso frattale."
        )
    else:
        summary = (
            f"Stato {status}, orizzonte migliore {int(horizon) if not pd.isna(horizon) else 'n/a'}g, "
            f"controlli {int(n)}, dentro banda {fmt_pct(inside)}, "
            f"errore medio abs {fmt_pct(err)}, errore medio {fmt_pct(avg_error)}."
        )

    return {
        "score": score,
        "summary": summary,
        "status": status,
        "checked_predictions": n,
        "horizon_days": horizon,
        "inside_band_rate": inside,
        "avg_abs_error_pct": err,
        "avg_error_pct": avg_error,
    }


def get_technical_level(asset, technical, field):
    row = technical.get(asset)

    if not row:
        return np.nan

    return safe_float(row.get(field, np.nan))


def build_levels(asset, technical, fractal_data):
    support = get_technical_level(asset, technical, "support")
    resistance = get_technical_level(asset, technical, "resistance")

    if asset == "BTC":
        return {
            "confirmation": f"Sopra {fmt_price(asset, resistance)} migliora; sopra la neckline tecnica successiva il recupero diventa più credibile.",
            "invalidation": f"Sotto {fmt_price(asset, support)} il quadro tecnico peggiora.",
        }

    if asset == "SOL":
        first = fractal_data.get("first_confirmation", np.nan)
        second = fractal_data.get("second_confirmation", np.nan)
        soft = fractal_data.get("soft_invalidation", np.nan)
        strong = fractal_data.get("strong_invalidation", np.nan)

        confirmations = []

        if not pd.isna(resistance):
            confirmations.append(fmt_price(asset, resistance))

        if not pd.isna(first):
            confirmations.append(fmt_price(asset, first))

        if not pd.isna(second):
            confirmations.append(fmt_price(asset, second))

        invalidations = []

        if not pd.isna(soft):
            invalidations.append(fmt_price(asset, soft))

        if not pd.isna(support):
            invalidations.append(fmt_price(asset, support))

        if not pd.isna(strong):
            invalidations.append(fmt_price(asset, strong))

        return {
            "confirmation": "Conferme sopra " + " / ".join(confirmations) + ".",
            "invalidation": "Allarmi sotto " + " / ".join(invalidations) + ".",
        }

    if asset == "DOGE":
        return {
            "confirmation": f"Sopra {fmt_price(asset, resistance)} migliora, ma resta asset debole finché scanner e struttura non girano.",
            "invalidation": f"Sotto {fmt_price(asset, support)} il rischio ribassista aumenta.",
        }

    return {
        "confirmation": "n/a",
        "invalidation": "n/a",
    }


def confluence_label(score):
    if score >= 7:
        return "POSITIVA"
    if score >= 3:
        return "MODERATAMENTE POSITIVA"
    if score >= 0:
        return "PARZIALE / MISTA"
    if score >= -3:
        return "DEBOLE / MISTA"
    return "NEGATIVA"


def bias_label(asset, score):
    if score >= 7:
        return "Rialzista"
    if score >= 3:
        return "Costruttivo prudente"
    if score >= 0:
        if asset == "SOL":
            return "Interessante ma non confermato"
        return "Neutrale / attesa"
    if score >= -3:
        return "Fragile / prudenza"
    return "Ribassista"


def reliability_label(component_scores):
    positives = sum(1 for x in component_scores if x > 0)
    negatives = sum(1 for x in component_scores if x < 0)
    nonzero = positives + negatives
    total = sum(component_scores)

    if nonzero == 0:
        return "BASSA"

    if positives > 0 and negatives > 0:
        if abs(total) <= 2:
            return "BASSA / MEDIA"
        return "MEDIA"

    if abs(total) >= 5:
        return "MEDIA / ALTA"

    return "MEDIA"


def action_label(asset, score):
    if asset == "BTC":
        if score >= 3:
            return "ACCUMULA SU PULLBACK / NO SHORT"
        if score >= 0:
            return "HOLD / ACCUMULO MOLTO SELETTIVO"
        return "PRUDENZA / NIENTE LEVA"

    if asset == "SOL":
        if score >= 7:
            return "SPOT OK, AGGIUNTE SU CONFERMA / LEVA ANCORA PRUDENTE"
        if score >= 3:
            return "HOLD / TRANCHE PICCOLE, NO LEVA"
        if score >= 0:
            return "HOLD / SOLO ANTICIPO A TRANCHE, NO LEVA"
        return "ASPETTA / NO LEVA"

    if asset == "DOGE":
        if score >= 3:
            return "SOLO TRADING TATTICO, RISCHIO ALTO"
        return "STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE"

    return "n/a"


def plain_interpretation(asset, score):
    if asset == "BTC":
        if score >= 3:
            return (
                "BTC è l'asset messo meglio nel breve. La struttura macro non è ancora pienamente rialzista, "
                "ma scanner, regime e segnali tecnici interni sono abbastanza coerenti per un recupero prudente."
            )

        return (
            "BTC resta il più solido del gruppo, ma la confluenza non è ancora abbastanza forte da inseguire il prezzo."
        )

    if asset == "SOL":
        if score >= 3:
            return (
                "SOL ha una confluenza costruttiva, ma va ancora trattato come setup anticipato. "
                "La conferma vera arriva solo sopra le resistenze tecniche, frattali e verso la zona EMA200 weekly. "
                "Il modulo lifecycle/EMA200 aggiunge una lettura positiva da squeeze, ma non sostituisce le conferme di prezzo."
            )

        if score >= 0:
            return (
                "SOL è interessante ma non confermato. Il frattale, il lifecycle/EMA200 e alcuni filtri aiutano, "
                "ma scanner e struttura tecnica non danno ancora una conferma pulita."
            )

        return (
            "SOL resta fragile: può avere una base, ma la struttura tecnica non ha ancora girato. "
            "Meglio evitare leva e aspettare conferme sopra le resistenze."
        )

    if asset == "DOGE":
        return (
            "DOGE resta l'asset più debole. Anche se può fare rimbalzi o spike, la confluenza generale "
            "resta negativa rispetto a BTC e SOL."
        )

    return ""


def build_global_confluence():
    latest_text = read_text(LATEST_REPORT)
    technical = load_technical_metrics()
    market_df = load_csv(MARKET_REGIME_SUMMARY)

    sol_fractal_data = parse_sol_fractal(latest_text)

    rows = []
    details = {}

    for asset in ASSETS:
        scanner = component_scanner(asset, latest_text)
        scanner_path = component_scanner_path(asset)
        market = component_market_regime(asset, market_df)
        technical_component = component_technical(asset, technical)
        fractal = component_fractal(asset, latest_text)
        fractal_path = component_fractal_path(asset)
        rsi_top = component_rsi_top_cycle(asset, latest_text)
        lifecycle = component_lifecycle_squeeze(asset, latest_text)
        futures = component_futures(asset, latest_text)
        daily = component_daily_change(asset, latest_text)

        component_scores = [
            scanner["score"],
            scanner_path["score"],
            market["score"],
            technical_component["score"],
            fractal["score"],
            fractal_path["score"],
            rsi_top["score"],
            lifecycle["score"],
            futures["score"],
            daily["score"],
        ]

        total_score = int(sum(component_scores))

        levels = build_levels(asset, technical, sol_fractal_data)

        row = {
            "asset": asset,
            "confluence_score": total_score,
            "confluence": confluence_label(total_score),
            "bias": bias_label(asset, total_score),
            "reliability": reliability_label(component_scores),
            "action": action_label(asset, total_score),

            "scanner_score": scanner["score"],
            "scanner_path_score": scanner_path["score"],
            "market_regime_score": market["score"],
            "technical_score_component": technical_component["score"],
            "fractal_score": fractal["score"],
            "fractal_path_score": fractal_path["score"],
            "rsi_top_cycle_score": rsi_top["score"],
            "lifecycle_squeeze_score": lifecycle["score"],
            "futures_score": futures["score"],
            "daily_change_score": daily["score"],

            "lifecycle_raw_score": lifecycle.get("raw_score", np.nan),
            "lifecycle_suggested_weight": lifecycle.get("suggested_weight", np.nan),
            "lifecycle_bias": lifecycle.get("bias", ""),
            "lifecycle_action": lifecycle.get("action", ""),
            "lifecycle_trend": lifecycle.get("trend", ""),
            "lifecycle_trend_score": lifecycle.get("trend_score", np.nan),
            "lifecycle_ema200_target": lifecycle.get("ema200_target", np.nan),
            "lifecycle_upside_ema200": lifecycle.get("upside_ema200", np.nan),
            "lifecycle_distance_ema200": lifecycle.get("distance_ema200", np.nan),
            "lifecycle_ema_gap": lifecycle.get("ema_gap", np.nan),
            "lifecycle_cross_status": lifecycle.get("cross_status", ""),
            "lifecycle_hit_ema200_12w": lifecycle.get("hit_ema200_12w", np.nan),
            "lifecycle_max_gain_median_12w": lifecycle.get("max_gain_median_12w", np.nan),
            "lifecycle_drawdown_median_12w": lifecycle.get("drawdown_median_12w", np.nan),

            "confirmation": levels["confirmation"],
            "invalidation": levels["invalidation"],
        }

        rows.append(row)

        details[asset] = {
            "scanner": scanner,
            "scanner_path": scanner_path,
            "market": market,
            "technical": technical_component,
            "fractal": fractal,
            "fractal_path": fractal_path,
            "rsi_top": rsi_top,
            "lifecycle": lifecycle,
            "futures": futures,
            "daily": daily,
            "levels": levels,
            "interpretation": plain_interpretation(asset, total_score),
        }

    metrics = pd.DataFrame(rows)

    return metrics, details


def render_report(metrics, details):
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    lines = []

    lines.append("# Sintesi finale di confluenza")
    lines.append("")
    lines.append(f"Generato: {now}")
    lines.append("")
    lines.append("Questo report mette insieme i moduli principali dello scanner e controlla se si confermano o si contraddicono.")
    lines.append("")
    lines.append("Moduli letti:")
    lines.append("")
    lines.append("- Scanner frattale/statistico a 30 giorni")
    lines.append("- Scanner path / cono previsionale")
    lines.append("- Market regime match")
    lines.append("- Struttura tecnica classica")
    lines.append("- Frattale BTC 2022 vs SOL 2026, solo per SOL")
    lines.append("- Fractal path tracker, solo per SOL")
    lines.append("- RSI top-cycle, soprattutto per SOL")
    lines.append("- Major alt lifecycle squeeze / EMA200 weekly, solo per SOL")
    lines.append("- Futures / liquidazioni")
    lines.append("- Cambiamento giornaliero")
    lines.append("")

    lines.append("## Sintesi operativa")
    lines.append("")

    summary_rows = []

    for _, r in metrics.iterrows():
        summary_rows.append({
            "Asset": r["asset"],
            "Punteggio": fmt_score(r["confluence_score"]),
            "Confluenza": r["confluence"],
            "Bias": r["bias"],
            "Affidabilità": r["reliability"],
            "Azione coerente": r["action"],
            "Conferme": r["confirmation"],
            "Invalidazioni": r["invalidation"],
        })

    lines.append(df_to_markdown(pd.DataFrame(summary_rows)))
    lines.append("")

    lines.append("## Punteggi per modulo")
    lines.append("")

    module_rows = []

    for _, r in metrics.iterrows():
        module_rows.append({
            "Asset": r["asset"],
            "Scanner": fmt_score(r["scanner_score"]),
            "Scanner path": fmt_score(r["scanner_path_score"]),
            "Market regime": fmt_score(r["market_regime_score"]),
            "Tecnico": fmt_score(r["technical_score_component"]),
            "Frattale SOL": fmt_score(r["fractal_score"]),
            "Fractal path": fmt_score(r["fractal_path_score"]),
            "RSI top-cycle": fmt_score(r["rsi_top_cycle_score"]),
            "Lifecycle EMA": fmt_score(r["lifecycle_squeeze_score"]),
            "Futures": fmt_score(r["futures_score"]),
            "Daily change": fmt_score(r["daily_change_score"]),
            "Totale": fmt_score(r["confluence_score"]),
        })

    lines.append(df_to_markdown(pd.DataFrame(module_rows)))
    lines.append("")

    lines.append("## Lettura asset per asset")
    lines.append("")

    for asset in ASSETS:
        row = metrics[metrics["asset"] == asset].iloc[0]
        d = details[asset]

        lines.append(f"### {asset}")
        lines.append("")
        lines.append(f"- Confluenza: **{row['confluence']}**")
        lines.append(f"- Bias: **{row['bias']}**")
        lines.append(f"- Punteggio finale: **{fmt_score(row['confluence_score'])}**")
        lines.append(f"- Affidabilità: **{row['reliability']}**")
        lines.append(f"- Azione coerente: **{row['action']}**")
        lines.append("")
        lines.append(d["interpretation"])
        lines.append("")

        lines.append("Dettaglio moduli:")
        lines.append("")
        lines.append(f"- Scanner 30g: **{fmt_score(d['scanner']['score'])}** — {d['scanner']['summary']}")
        lines.append(f"- Scanner path / cono: **{fmt_score(d['scanner_path']['score'])}** — {d['scanner_path']['summary']}")
        lines.append(f"- Market regime: **{fmt_score(d['market']['score'])}** — {d['market']['summary']}")
        lines.append(f"- Tecnico: **{fmt_score(d['technical']['score'])}** — {d['technical']['summary']}")
        lines.append(f"- Frattale SOL/BTC: **{fmt_score(d['fractal']['score'])}** — {d['fractal']['summary']}")
        lines.append(f"- Fractal path tracker: **{fmt_score(d['fractal_path']['score'])}** — {d['fractal_path']['summary']}")
        lines.append(f"- RSI top-cycle: **{fmt_score(d['rsi_top']['score'])}** — {d['rsi_top']['summary']}")
        lines.append(f"- Lifecycle EMA200: **{fmt_score(d['lifecycle']['score'])}** — {d['lifecycle']['summary']}")
        lines.append(f"- Futures/liquidazioni: **{fmt_score(d['futures']['score'])}** — {d['futures']['summary']}")
        lines.append(f"- Cambiamento giornaliero: **{fmt_score(d['daily']['score'])}** — {d['daily']['summary']}")
        lines.append("")
        lines.append(f"Conferme: {d['levels']['confirmation']}")
        lines.append("")
        lines.append(f"Invalidazioni: {d['levels']['invalidation']}")
        lines.append("")

    lines.append("## Come leggere il punteggio")
    lines.append("")
    lines.append("- +7 o più: confluenza positiva forte.")
    lines.append("- Da +3 a +6: confluenza moderatamente positiva.")
    lines.append("- Da 0 a +2: confluenza parziale o mista.")
    lines.append("- Da -1 a -3: confluenza debole o fragile.")
    lines.append("- -4 o meno: confluenza negativa.")
    lines.append("")
    lines.append("Nota: Scanner path e Fractal path sono già integrati, ma finché hanno pochi controlli restano quasi sempre a punteggio 0.")
    lines.append("Servono almeno 5 controlli prima di influire leggermente, e 30+ controlli prima di pesare davvero.")
    lines.append("")
    lines.append("Nota lifecycle EMA200: il modulo Major alt lifecycle squeeze pesa al massimo +1 / -1 nel Global, perché è un filtro di contesto e non una conferma diretta di prezzo.")
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
            new = new_section + "\n\n" + old
    else:
        decision_marker = "<!-- DECISION_REPORT_START -->"

        if decision_marker in old:
            idx = old.find(decision_marker)
            new = old[:idx] + new_section + "\n\n" + old[idx:]
        else:
            new = new_section + "\n\n" + old

    LATEST_REPORT.write_text(new, encoding="utf-8")


def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    metrics, details = build_global_confluence()

    metrics.to_csv(OUTPUT_METRICS, index=False)

    md = render_report(metrics, details)

    OUTPUT_REPORT.write_text(md, encoding="utf-8")
    inject_into_latest_report(md)

    print(f"Creato {OUTPUT_REPORT}")
    print(f"Creato {OUTPUT_METRICS}")


if __name__ == "__main__":
    main()
