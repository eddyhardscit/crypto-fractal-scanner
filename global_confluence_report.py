import csv
import re
from datetime import datetime, timezone
from pathlib import Path


REPORTS_DIR = Path("reports")
LATEST_REPORT_PATH = REPORTS_DIR / "latest_report.md"
REPORT_PATH = REPORTS_DIR / "global_confluence_report.md"
METRICS_CSV_PATH = REPORTS_DIR / "global_confluence_metrics.csv"

CLASSIC_TECH_METRICS_PATH = REPORTS_DIR / "classic_technical_confirmation_metrics.csv"

START_MARKER = "<!-- GLOBAL_CONFLUENCE_START -->"
END_MARKER = "<!-- GLOBAL_CONFLUENCE_END -->"

ASSETS = ["BTC", "SOL", "DOGE"]

ASSET_NAMES = {
    "BTC": "Bitcoin",
    "SOL": "Solana",
    "DOGE": "Dogecoin",
}

ASSET_TICKERS = {
    "BTC": "BTC-USD",
    "SOL": "SOL-USD",
    "DOGE": "DOGE-USD",
}

SOURCE_EXCLUDE_MARKERS = [
    "DECISION_REPORT",
    "GLOBAL_CONFLUENCE",
    "MODULE_ACCURACY",
    "GLOBAL_WEIGHT_CALIBRATION",
    "RISK_CALIBRATION",
    "SOL_BTC_FRACTAL_HISTORY",
]


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def now_utc_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def remove_marker_block(text: str, marker_name: str) -> str:
    start = f"<!-- {marker_name}_START -->"
    end = f"<!-- {marker_name}_END -->"

    pattern = re.compile(
        re.escape(start) + r".*?" + re.escape(end),
        flags=re.DOTALL,
    )
    return pattern.sub("", text)


def clean_source_text(text: str) -> str:
    out = text
    for marker in SOURCE_EXCLUDE_MARKERS:
        out = remove_marker_block(out, marker)
    return out


def extract_marker_block(text: str, marker_name: str) -> str:
    start = f"<!-- {marker_name}_START -->"
    end = f"<!-- {marker_name}_END -->"

    pattern = re.compile(
        re.escape(start) + r"(.*?)" + re.escape(end),
        flags=re.DOTALL,
    )
    match = pattern.search(text)
    if not match:
        return ""
    return match.group(1).strip()


def replace_block(text: str, block: str) -> str:
    full_block = f"{START_MARKER}\n{block.rstrip()}\n{END_MARKER}"

    if START_MARKER in text and END_MARKER in text:
        pattern = re.compile(
            re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
            flags=re.DOTALL,
        )
        return pattern.sub(full_block, text)

    decision_end = "<!-- DECISION_REPORT_END -->"
    if decision_end in text:
        return text.replace(decision_end, decision_end + "\n\n" + full_block, 1)

    return full_block + "\n\n" + text


def parse_number(value):
    if value is None:
        return None

    s = str(value)
    s = s.replace("\xa0", " ").strip()

    if not s or s.lower() in {"n/a", "nan", "none", "-"}:
        return None

    match = re.search(r"[-+]?\d[\d\s.,]*", s)
    if not match:
        return None

    token = match.group(0).replace(" ", "")

    if "," in token:
        token = token.replace(".", "")
        token = token.replace(",", ".")
    elif "." in token:
        parts = token.split(".")
        if (
            len(parts) == 2
            and len(parts[1]) == 3
            and parts[0] != "0"
            and len(parts[0]) <= 3
        ):
            token = parts[0] + parts[1]

    try:
        return float(token)
    except ValueError:
        return None


def parse_int(value, default=0):
    n = parse_number(value)
    if n is None:
        return default
    return int(n)


def clean_cell(value: str) -> str:
    if value is None:
        return ""
    s = str(value).strip()
    s = s.replace("**", "")
    s = s.replace("`", "")
    return s.strip()


def split_md_row(line: str):
    line = line.strip()
    if not line.startswith("|") or not line.endswith("|"):
        return None

    cells = [clean_cell(c) for c in line.strip("|").split("|")]

    if not cells:
        return None

    if all(set(c.replace(":", "").strip()) <= {"-"} for c in cells if c.strip()):
        return None

    return cells


def fmt_signed_int(value) -> str:
    if value is None:
        return "0"
    value = int(value)
    if value > 0:
        return f"+{value}"
    return str(value)


def fmt_pct(value, decimals: int = 2) -> str:
    if value is None:
        return "n/a"
    s = f"{value:+.{decimals}f}%"
    return s.replace(".", ",")


def fmt_pct_plain(value, decimals: int = 2) -> str:
    if value is None:
        return "n/a"
    s = f"{value:.{decimals}f}%"
    return s.replace(".", ",")


def fmt_price(asset: str, value) -> str:
    if value is None:
        return "n/a"

    v = float(value)

    if asset == "BTC":
        s = f"{v:,.0f}"
        s = s.replace(",", ".")
        return s

    if asset == "DOGE":
        return f"{v:.5f}"

    s = f"{v:,.2f}"
    s = s.replace(",", "X").replace(".", ",").replace("X", ".")
    return s


def fmt_money(asset: str, value) -> str:
    if value is None:
        return "n/a"

    if asset == "DOGE":
        return f"{fmt_price(asset, value)} $"

    return f"{fmt_price(asset, value)} $"


def md_table(headers, rows) -> str:
    out = []
    out.append("| " + " | ".join(headers) + " |")
    out.append("| " + " | ".join(["---"] * len(headers)) + " |")

    for row in rows:
        out.append("| " + " | ".join(str(x) for x in row) + " |")

    return "\n".join(out)


def extract_section_after(text: str, start_pattern: str, end_pattern: str = r"\n#{1,3}\s+"):
    match = re.search(start_pattern, text, flags=re.IGNORECASE)
    if not match:
        return ""

    start = match.start()
    rest = text[start + 1 :]

    end_match = re.search(end_pattern, rest, flags=re.IGNORECASE)
    if not end_match:
        return text[start:]

    end = start + 1 + end_match.start()
    return text[start:end]


def extract_heading_block(text: str, heading_regex: str) -> str:
    match = re.search(heading_regex, text, flags=re.IGNORECASE)
    if not match:
        return ""

    start = match.start()
    rest = text[match.end() :]

    end_match = re.search(r"\n##\s+", rest)
    if not end_match:
        return text[start:]

    end = match.end() + end_match.start()
    return text[start:end]


def extract_quick_asset_section(text: str, asset: str) -> str:
    name = ASSET_NAMES[asset]

    anchor = text.find("# Lettura velocissima")
    if anchor < 0:
        anchor = 0

    sub = text[anchor:]

    pattern = rf"##\s+{re.escape(name)}\b"
    match = re.search(pattern, sub, flags=re.IGNORECASE)
    if not match:
        return ""

    start = match.start()
    rest = sub[start + 1 :]

    end_match = re.search(r"\n##\s+", rest)
    if not end_match:
        return sub[start:]

    end = start + 1 + end_match.start()
    return sub[start:end]


def extract_detailed_asset_section(text: str, asset: str) -> str:
    name = ASSET_NAMES[asset]
    pattern = rf"#\s+Approfondimento tecnico\s+—\s+{re.escape(name)}"
    return extract_section_after(text, pattern, r"\n---\n|\n#\s+Approfondimento tecnico|\n<!--")


def component_template(score=0, detail="n/a", data=None):
    return {
        "score": int(score),
        "detail": detail,
        "data": data or {},
    }


def read_csv_rows(path: Path):
    if not path.exists():
        return []

    try:
        with path.open("r", encoding="utf-8", newline="") as f:
            return list(csv.DictReader(f))
    except Exception:
        return []


def _parse_scanner_component_markdown_fallback(text: str, asset: str):
    quick = extract_quick_asset_section(text, asset)
    detailed = extract_detailed_asset_section(text, asset)
    source = quick + "\n" + detailed

    direction = None
    positive_rate = None
    negative_rate = None
    return_p50 = None
    price = None

    m = re.search(
        r"Direzione più probabile a 30 giorni:\s*\*\*([^*]+)\*\*",
        source,
        flags=re.IGNORECASE,
    )
    if m:
        direction = clean_cell(m.group(1)).upper()

    m = re.search(
        r"Casi positivi.*?:\s*\*\*([+\-]?\d[\d.,]*)%",
        source,
        flags=re.IGNORECASE,
    )
    if m:
        positive_rate = parse_number(m.group(1))

    m = re.search(
        r"Casi negativi.*?:\s*\*\*([+\-]?\d[\d.,]*)%",
        source,
        flags=re.IGNORECASE,
    )
    if m:
        negative_rate = parse_number(m.group(1))

    m = re.search(
        r"Return normale fra 30 giorni:\s*\*\*.*?\*\*\s*$begin:math:text$\(\[\+\\\-\]\?\\d\[\\d\.\,\]\*\)\%$end:math:text$",
        source,
        flags=re.IGNORECASE,
    )
    if m:
        return_p50 = parse_number(m.group(1))

    if return_p50 is None:
        m = re.search(
            r"Rendimento centrale dopo 30 giorni:\s*\*\*([+\-]?\d[\d.,]*)%",
            source,
            flags=re.IGNORECASE,
        )
        if m:
            return_p50 = parse_number(m.group(1))

    m = re.search(
        r"Prezzo attuale:\s*\*\*([^\n*]+)\*\*",
        source,
        flags=re.IGNORECASE,
    )
    if m:
        price = parse_number(m.group(1))

    score = 0

    if positive_rate is not None and return_p50 is not None:
        if positive_rate >= 65 and return_p50 > 0:
            score = 3
        elif positive_rate >= 58 and return_p50 >= 0:
            score = 2
        elif positive_rate >= 52 and return_p50 >= 0:
            score = 1
        elif positive_rate <= 20 and return_p50 < 0:
            score = -3
        elif positive_rate <= 35 and return_p50 < 0:
            score = -2
        elif positive_rate < 48 and return_p50 < 0:
            score = -1
        else:
            score = 0
    elif positive_rate is not None:
        if positive_rate >= 65:
            score = 1
        elif positive_rate <= 20:
            score = -3
        elif positive_rate <= 35:
            score = -2
        elif positive_rate < 48:
            score = -1

    detail = (
        f"Casi positivi {fmt_pct_plain(positive_rate)}, "
        f"return centrale 30g {fmt_pct(return_p50)}. "
        f"Direzione scanner: {direction or 'n/a'}."
    )

    return component_template(
        score=score,
        detail=detail,
        data={
            "direction": direction,
            "positive_rate": positive_rate,
            "negative_rate": negative_rate,
            "return_p50": return_p50,
            "price": price,
        },
    )


# STRUCTURED_SCANNER_PATCH_V1
# Prima usa il riepilogo strutturato prodotto da scanner.py; il vecchio parser
# Markdown resta disponibile come fallback per non interrompere il workflow.
def parse_scanner_component(text: str, asset: str):
    structured = None
    try:
        from scanner_signal_reader import scanner_signal
        candidate = scanner_signal(asset)
        if candidate and candidate.get("available"):
            structured = candidate
    except Exception:
        structured = None

    if not structured:
        return _parse_scanner_component_markdown_fallback(text, asset)

    direction = clean_cell(structured.get("direction_30d") or "").upper() or None
    positive_rate = parse_number(structured.get("positive_cases_30d"))
    negative_rate = parse_number(structured.get("negative_cases_30d"))
    return_p50 = parse_number(structured.get("return_p50_pct"))
    price = parse_number(structured.get("current_price"))

    # Se il file strutturato esiste ma la riga è incompleta, non inventa dati:
    # torna al parser precedente.
    if positive_rate is None:
        return _parse_scanner_component_markdown_fallback(text, asset)

    if negative_rate is None:
        negative_rate = 100.0 - positive_rate

    score = 0
    if positive_rate is not None and return_p50 is not None:
        if positive_rate >= 65 and return_p50 > 0:
            score = 3
        elif positive_rate >= 58 and return_p50 >= 0:
            score = 2
        elif positive_rate >= 52 and return_p50 >= 0:
            score = 1
        elif positive_rate <= 20 and return_p50 < 0:
            score = -3
        elif positive_rate <= 35 and return_p50 < 0:
            score = -2
        elif positive_rate < 48 and return_p50 < 0:
            score = -1
    elif positive_rate is not None:
        if positive_rate >= 65:
            score = 1
        elif positive_rate <= 20:
            score = -3
        elif positive_rate <= 35:
            score = -2
        elif positive_rate < 48:
            score = -1

    detail = (
        f"Casi positivi {fmt_pct_plain(positive_rate)}, "
        f"return centrale 30g {fmt_pct(return_p50)}. "
        f"Direzione scanner: {direction or 'n/a'}. "
        "Fonte: latest_scanner_summary strutturato."
    )

    return component_template(
        score=score,
        detail=detail,
        data={
            "direction": direction,
            "positive_rate": positive_rate,
            "negative_rate": negative_rate,
            "return_p50": return_p50,
            "price": price,
            "structured_source": True,
        },
    )

def parse_scanner_path_component(block: str, asset: str):
    accuracy_block = extract_heading_block(
        block,
        r"##\s+Accuratezza percorso scanner\b",
    )

    max_controls = 0

    for line in accuracy_block.splitlines():
        cells = split_md_row(line)
        if not cells or len(cells) < 3:
            continue

        if cells[0].upper() != asset:
            continue

        if not re.fullmatch(r"\d+g", cells[1].strip().lower()):
            continue

        controls = parse_number(cells[2])
        if controls is not None:
            max_controls = max(max_controls, int(controls))

    if max_controls < 5:
        detail = (
            f"Raccolta dati. Controlli disponibili {max_controls}. "
            "Servono almeno 5 controlli prima di pesare il cono previsionale."
        )
        return component_template(0, detail, {"controls": max_controls})

    detail = (
        f"Controlli disponibili {max_controls}. "
        "Il cono previsionale inizia a essere valutabile, ma resta secondario."
    )
    return component_template(0, detail, {"controls": max_controls})


def parse_market_component(block: str, asset: str):
    ticker = ASSET_TICKERS[asset]

    matches = None
    positive_30d = None
    return_p50 = None

    for line in block.splitlines():
        cells = split_md_row(line)
        if not cells or len(cells) < 6:
            continue

        if cells[0] == ticker and cells[1] == "SAME_BTC_AND_ASSET_REGIME":
            matches = parse_number(cells[2])
            positive_30d = parse_number(cells[3])
            return_p50 = parse_number(cells[4])
            break

    score = 0

    if matches is not None and matches >= 5 and positive_30d is not None and return_p50 is not None:
        if positive_30d >= 85 and return_p50 > 0:
            score = 3
        elif positive_30d >= 60 and return_p50 >= 0:
            score = 2
        elif positive_30d >= 55 and return_p50 >= 0:
            score = 1
        elif positive_30d <= 20 and return_p50 < 0:
            score = -3
        elif positive_30d <= 35 and return_p50 < 0:
            score = -2
        elif positive_30d < 45 and return_p50 < 0:
            score = -1

    detail = (
        f"Gruppo SAME_BTC_AND_ASSET_REGIME, match {int(matches) if matches is not None else 'n/a'}, "
        f"positivi 30g {fmt_pct_plain(positive_30d)}, return p50 {fmt_pct(return_p50)}."
    )

    return component_template(
        score,
        detail,
        {
            "matches": matches,
            "positive_30d": positive_30d,
            "return_p50": return_p50,
        },
    )


def parse_technical_component(block: str, asset: str):
    tech_score = None
    verdict = None
    trend = None
    structure = None
    divergence = None
    wyckoff = None
    support = None
    resistance = None
    price = None

    for line in block.splitlines():
        cells = split_md_row(line)
        if not cells or len(cells) < 10:
            continue

        if cells[0].upper() != asset:
            continue

        price = parse_number(cells[1])
        tech_score = parse_number(cells[2])
        verdict = clean_cell(cells[3])
        trend = clean_cell(cells[4])
        structure = clean_cell(cells[6])
        divergence = clean_cell(cells[7])
        wyckoff = clean_cell(cells[8])
        support = parse_number(cells[9])
        resistance = parse_number(cells[10]) if len(cells) > 10 else None
        break

    if tech_score is None:
        detail_section = extract_section_after(
            block,
            rf"###\s+{asset}\b",
            r"\n###\s+|\n##\s+",
        )

        m = re.search(r"Punteggio tecnico:\s*\*\*([+\-]?\d+)", detail_section, flags=re.IGNORECASE)
        if m:
            tech_score = parse_number(m.group(1))

        m = re.search(r"Verdetto:\s*\*\*([^*]+)\*\*", detail_section, flags=re.IGNORECASE)
        if m:
            verdict = clean_cell(m.group(1))

        m = re.search(r"Trend:\s*\*\*([^*]+)\*\*", detail_section, flags=re.IGNORECASE)
        if m:
            trend = clean_cell(m.group(1))

        m = re.search(r"Struttura:\s*\*\*([^*]+)\*\*", detail_section, flags=re.IGNORECASE)
        if m:
            structure = clean_cell(m.group(1))

        m = re.search(r"Divergenza:\s*\*\*([^*]+)\*\*", detail_section, flags=re.IGNORECASE)
        if m:
            divergence = clean_cell(m.group(1))

        m = re.search(r"Fase Wyckoff candidata:\s*\*\*([^*]+)\*\*", detail_section, flags=re.IGNORECASE)
        if m:
            wyckoff = clean_cell(m.group(1))

        m = re.search(r"Supporto più vicino:\s*\*\*([^*]+)\*\*", detail_section, flags=re.IGNORECASE)
        if m:
            support = parse_number(m.group(1))

        m = re.search(r"Resistenza più vicina:\s*\*\*([^*]+)\*\*", detail_section, flags=re.IGNORECASE)
        if m:
            resistance = parse_number(m.group(1))

    score = 0

    if tech_score is not None:
        if tech_score >= 7:
            score = 3
        elif tech_score >= 3:
            score = 2
        elif tech_score >= 1:
            score = 1
        elif tech_score <= -7:
            score = -3
        elif tech_score <= -3:
            score = -2
        elif tech_score <= -1:
            score = -1

    detail = (
        f"Score tecnico {int(tech_score) if tech_score is not None else 'n/a'}/12, "
        f"verdetto {(verdict or 'n/a').lower()}, "
        f"trend {(trend or 'n/a').lower()}, "
        f"struttura {(structure or 'n/a').lower()}, "
        f"divergenza {(divergence or 'n/a').lower()}, "
        f"Wyckoff {(wyckoff or 'n/a').lower()}."
    )

    return component_template(
        score,
        detail,
        {
            "technical_score": tech_score,
            "verdict": verdict,
            "trend": trend,
            "structure": structure,
            "divergence": divergence,
            "wyckoff": wyckoff,
            "support": support,
            "resistance": resistance,
            "price": price,
        },
    )


def parse_classic_technical_component(block: str, asset: str):
    """
    Nuovo modulo:
    Classic technical confirmation.

    Importante: pesa poco nel Global, perché si sovrappone in parte al vecchio
    Technical Structure. Lo usiamo come filtro di conferma classica, non come
    motore principale.
    """

    rows = read_csv_rows(CLASSIC_TECH_METRICS_PATH)

    data = {}

    for row in rows:
        row_asset = clean_cell(row.get("asset")).upper()
        if row_asset == asset:
            data = row
            break

    raw_score = None
    verdict = None
    action = None
    risk = None
    stage = None
    structure = None
    wyckoff = None
    price_confirmation_score = None
    support = None
    resistance = None

    if data:
        raw_score = parse_number(data.get("score"))
        verdict = clean_cell(data.get("verdict"))
        action = clean_cell(data.get("action"))
        risk = clean_cell(data.get("risk"))
        stage = clean_cell(data.get("stage"))
        structure = clean_cell(data.get("structure"))
        wyckoff = clean_cell(data.get("wyckoff_phase"))
        price_confirmation_score = parse_number(data.get("price_confirmation_score"))
        support = parse_number(data.get("support"))
        resistance = parse_number(data.get("resistance"))

    if raw_score is None and block:
        asset_section = extract_section_after(
            block,
            rf"###\s+{asset}\b",
            r"\n###\s+|\n##\s+",
        )

        m = re.search(r"Score classico:\s*\*\*([+\-]?\d+)", asset_section, flags=re.IGNORECASE)
        if m:
            raw_score = parse_number(m.group(1))

        m = re.search(r"Verdetto:\s*\*\*([^*]+)\*\*", asset_section, flags=re.IGNORECASE)
        if m:
            verdict = clean_cell(m.group(1))

        m = re.search(r"Azione coerente:\s*\*\*([^*]+)\*\*", asset_section, flags=re.IGNORECASE)
        if m:
            action = clean_cell(m.group(1))

        m = re.search(r"(?:Rischio|Volatilità tecnica locale|Volatilità locale):\s*\*\*([^*]+)\*\*", asset_section, flags=re.IGNORECASE)
        if m:
            risk = clean_cell(m.group(1))

        m = re.search(r"Stage weekly:\s*\*\*([^*]+)\*\*", asset_section, flags=re.IGNORECASE)
        if m:
            stage = clean_cell(m.group(1))

        m = re.search(r"Struttura:\s*\*\*[^*]+\*\*\s*—\s*([^\n]+)", asset_section, flags=re.IGNORECASE)
        if m:
            structure = clean_cell(m.group(1))

        m = re.search(r"Wyckoff:\s*\*\*[^*]+\*\*\s*—\s*([^.\n]+)", asset_section, flags=re.IGNORECASE)
        if m:
            wyckoff = clean_cell(m.group(1))

    if raw_score is None:
        return component_template(
            0,
            "Modulo Classic Technical non disponibile o non ancora eseguito.",
            {},
        )

    raw_score = int(raw_score)

    score = 0

    verdict_u = (verdict or "").upper()

    if raw_score >= 8 or "CONFERMATO RIALZISTA" in verdict_u:
        score = 1
    elif raw_score >= 5:
        score = 1
    elif raw_score <= -8 or "CONFERMATO RIBASSISTA" in verdict_u:
        score = -1
    elif raw_score <= -5:
        score = -1
    else:
        score = 0

    detail = (
        f"Score classico {raw_score}/12, "
        f"verdetto {verdict or 'n/a'}, "
        f"stage {stage or 'n/a'}, "
        f"struttura {structure or 'n/a'}, "
        f"Wyckoff {wyckoff or 'n/a'}, "
        f"volatilità locale {risk or 'n/a'}. "
        "Peso Global limitato a ±1 perché è un filtro di conferma."
    )

    return component_template(
        score,
        detail,
        {
            "classic_raw_score": raw_score,
            "classic_verdict": verdict,
            "classic_action": action,
            "classic_risk": risk,
            "classic_stage": stage,
            "classic_structure": structure,
            "classic_wyckoff": wyckoff,
            "classic_price_confirmation_score": price_confirmation_score,
            "classic_support": support,
            "classic_resistance": resistance,
        },
    )


def parse_sol_fractal_component(block: str):
    if not block:
        return component_template(0, "Frattale SOL/BTC non disponibile.")

    verdict = None
    phase = None
    similarity = None
    reliability = None
    risk = None
    tracking = None

    m = re.search(r"##\s+Verdetto:\s*([^\n]+)", block, flags=re.IGNORECASE)
    if m:
        verdict = clean_cell(m.group(1)).upper()

    m = re.search(r"Fase attuale:\*\*\s*([^\n*]+)", block, flags=re.IGNORECASE)
    if m:
        phase = clean_cell(m.group(1)).upper()

    m = re.search(r"Somiglianza totale:\*\*\s*([+\-]?\d[\d.,]*)%", block, flags=re.IGNORECASE)
    if m:
        similarity = parse_number(m.group(1))

    m = re.search(r"Affidabilita:\*\*\s*([^\n*]+)", block, flags=re.IGNORECASE)
    if m:
        reliability = clean_cell(m.group(1)).upper()

    m = re.search(r"Rischio fase:\*\*\s*([^\n*]+)", block, flags=re.IGNORECASE)
    if m:
        risk = clean_cell(m.group(1)).upper()

    m = re.search(r"Trend tracking:\*\*\s*([^\n*]+)", block, flags=re.IGNORECASE)
    if m:
        tracking = clean_cell(m.group(1)).upper()

    first_confirmation = None
    second_confirmation = None
    soft_invalidation = None
    strong_invalidation = None

    for line in block.splitlines():
        cells = split_md_row(line)
        if not cells or len(cells) < 2:
            continue

        label = cells[0].lower()

        if "prima conferma" in label:
            first_confirmation = parse_number(cells[1])
        elif "seconda conferma" in label:
            second_confirmation = parse_number(cells[1])
        elif "invalidazione soft" in label:
            soft_invalidation = parse_number(cells[1])
        elif "invalidazione forte" in label:
            strong_invalidation = parse_number(cells[1])

    score = 0

    verdict_u = verdict or ""
    tracking_u = tracking or ""

    if "ROTTO" in verdict_u or "NO" == verdict_u:
        score = -2
    elif "PARZIALMENTE" in verdict_u:
        if similarity is not None and similarity >= 78 and "STABILE" in tracking_u:
            score = 2
        elif similarity is not None and similarity >= 70 and "STABILE" in tracking_u:
            score = 1
        elif similarity is not None and similarity >= 65:
            score = 0
    elif "SI" in verdict_u:
        if similarity is not None and similarity >= 80:
            score = 3
        elif similarity is not None and similarity >= 72:
            score = 2
        else:
            score = 1

    detail = (
        f"Verdetto {verdict or 'n/a'}, "
        f"somiglianza {fmt_pct(similarity)}, "
        f"tracking {tracking or 'n/a'}, "
        f"fase {phase or 'n/a'}, "
        f"rischio {risk or 'n/a'}."
    )

    return component_template(
        score,
        detail,
        {
            "verdict": verdict,
            "similarity": similarity,
            "tracking": tracking,
            "phase": phase,
            "risk": risk,
            "reliability": reliability,
            "first_confirmation": first_confirmation,
            "second_confirmation": second_confirmation,
            "soft_invalidation": soft_invalidation,
            "strong_invalidation": strong_invalidation,
        },
    )


def parse_fractal_path_component(block: str):
    if not block:
        return component_template(0, "Fractal path tracker non disponibile.")

    accuracy_block = extract_heading_block(
        block,
        r"##\s+Accuratezza storica della proiezione futura\b",
    )

    max_controls = 0

    for line in accuracy_block.splitlines():
        cells = split_md_row(line)
        if not cells or len(cells) < 2:
            continue

        first = cells[0].strip().lower()
        if re.fullmatch(r"\d+g", first):
            controls = parse_number(cells[1])
            if controls is not None:
                max_controls = max(max_controls, int(controls))

    if max_controls <= 0:
        detail = (
            "Tracking operativo, ma nessuna milestone settimanale ancora verificata. "
            "Il modulo non pesa finché non maturano abbastanza controlli."
        )
        return component_template(0, detail, {"controls": max_controls})

    if max_controls < 5:
        detail = (
            f"Raccolta dati. Controlli disponibili {max_controls}. "
            "Servono almeno 5 controlli prima di pesare il percorso frattale."
        )
        return component_template(0, detail, {"controls": max_controls})

    detail = (
        f"Controlli disponibili {max_controls}. "
        "Il percorso frattale inizia a essere valutabile, ma resta secondario."
    )
    return component_template(0, detail, {"controls": max_controls})


def parse_rsi_component(block: str, asset: str):
    if asset != "SOL":
        return component_template(0, "Non applicabile a questo asset.")

    risk = None
    for line in block.splitlines():
        cells = split_md_row(line)
        if not cells or len(cells) < 2:
            continue
        if "Rischio top-cycle RSI" in cells[0]:
            risk = clean_cell(cells[1]).upper()
            break

    # Questo modulo misura il rischio di top, non la forza rialzista.
    # Un rischio BASSO o MEDIO non deve aggiungere punti al Global.
    score_by_risk = {
        "BASSO": 0,
        "MEDIO": 0,
        "ALTO": -1,
        "MOLTO ALTO": -2,
    }
    score = score_by_risk.get(risk, 0)

    return component_template(
        score,
        f"Rischio top-cycle RSI: {risk or 'n/a'}.",
        {"risk": risk},
    )


def parse_lifecycle_component(block: str, asset: str):
    if asset != "SOL":
        return component_template(0, "Non applicabile a questo asset.")

    values = {}

    for line in block.splitlines():
        cells = split_md_row(line)
        if not cells or len(cells) < 2:
            continue

        key = clean_cell(cells[0])
        value = clean_cell(cells[1])
        values[key] = value

    lifecycle_score = parse_number(values.get("Lifecycle squeeze score"))
    bias = values.get("Bias")
    ema200 = parse_number(values.get("EMA200 weekly target"))
    upside = parse_number(values.get("Upside verso EMA200"))
    gap = parse_number(values.get("Gap EMA50/EMA200"))
    hit = parse_number(values.get("Hit EMA200 12w analoghi"))
    trend = values.get("Trend squeeze")

    detail = (
        "Contesto non pesato nel Global. "
        f"Lifecycle score {int(lifecycle_score) if lifecycle_score is not None else 'n/a'}, "
        f"bias {bias or 'n/a'}, "
        f"EMA200 {fmt_money('SOL', ema200)}, "
        f"upside EMA200 {fmt_pct(upside)}, "
        f"gap EMA50/EMA200 {fmt_pct(gap)}, "
        f"hit EMA200 12w {fmt_pct(hit)}, "
        f"trend {trend or 'n/a'}. "
        "Peso Global forzato a 0."
    )

    return component_template(
        0,
        detail,
        {
            "lifecycle_score": lifecycle_score,
            "bias": bias,
            "ema200": ema200,
            "upside": upside,
            "gap": gap,
            "hit_ema200_12w": hit,
            "trend": trend,
            "forced_weight": 0,
        },
    )


def parse_futures_component(block: str, asset: str):
    reading = None
    strength = None

    for line in block.splitlines():
        cells = split_md_row(line)
        if not cells or len(cells) < 6:
            continue

        if cells[0].upper() != asset:
            continue

        reading = clean_cell(cells[5])
        strength = clean_cell(cells[6]) if len(cells) > 6 else None
        break

    detail = f"Lettura futures {reading or 'n/a'}, forza {strength or 'n/a'}."

    return component_template(
        0,
        detail,
        {
            "reading": reading,
            "strength": strength,
        },
    )


def parse_daily_change_component(block: str, asset: str):
    change = None
    tone = None
    today_verdict = None

    for line in block.splitlines():
        cells = split_md_row(line)
        if not cells or len(cells) < 5:
            continue

        if cells[0].upper() != asset:
            continue

        change = clean_cell(cells[1]).upper()
        tone = clean_cell(cells[2]).lower()
        today_verdict = clean_cell(cells[3]).upper()
        break

    score = 0

    if change and "NESSUN" not in change:
        if "miglioramento" in (tone or ""):
            score = 1
        elif "peggioramento" in (tone or ""):
            score = -1

    detail = (
        f"{asset}: "
        f"{(change or 'nessun dato').lower()} "
        f"in {tone or 'n/a'} rispetto a ieri."
    )

    return component_template(
        score,
        detail,
        {
            "change": change,
            "tone": tone,
            "today_verdict": today_verdict,
        },
    )


def build_components(source_text: str):
    scanner_forecast_block = extract_marker_block(source_text, "SCANNER_FORECAST_TRACKER")
    market_block = extract_marker_block(source_text, "MARKET_REGIME_MATCH")
    technical_block = extract_marker_block(source_text, "TECHNICAL_STRUCTURE")
    classic_technical_block = extract_marker_block(source_text, "CLASSIC_TECHNICAL_CONFIRMATION")
    sol_fractal_block = extract_marker_block(source_text, "BTC_SOL_FRACTAL")
    fractal_path_block = extract_marker_block(source_text, "FRACTAL_PATH_TRACKER")
    rsi_block = extract_marker_block(source_text, "RSI_TOP_CYCLE")
    lifecycle_block = extract_marker_block(source_text, "MAJOR_ALT_LIFECYCLE_SQUEEZE")
    futures_block = extract_marker_block(source_text, "LIQUIDATION_SUMMARY")
    daily_block = extract_marker_block(source_text, "DAILY_CHANGE")

    components = {}

    for asset in ASSETS:
        components[asset] = {
            "Scanner": parse_scanner_component(source_text, asset),
            "Scanner path": parse_scanner_path_component(scanner_forecast_block, asset),
            "Market regime": parse_market_component(market_block, asset),
            "Tecnico": parse_technical_component(technical_block, asset),
            "Classic technical": parse_classic_technical_component(classic_technical_block, asset),
            "Frattale SOL": (
                parse_sol_fractal_component(sol_fractal_block)
                if asset == "SOL"
                else component_template(0, "Non applicabile a questo asset.")
            ),
            "Fractal path": (
                parse_fractal_path_component(fractal_path_block)
                if asset == "SOL"
                else component_template(0, "Non applicabile a questo asset.")
            ),
            "RSI top-cycle": parse_rsi_component(rsi_block, asset),
            "Lifecycle EMA": parse_lifecycle_component(lifecycle_block, asset),
            "Futures": parse_futures_component(futures_block, asset),
            "Daily change": parse_daily_change_component(daily_block, asset),
        }

    return components


def total_score(asset_components: dict) -> int:
    return int(sum(c["score"] for c in asset_components.values()))


def confluence_label(score: int) -> str:
    if score >= 7:
        return "POSITIVA FORTE"
    if score >= 3:
        return "MODERATAMENTE POSITIVA"
    if score >= 0:
        return "MISTA / PARZIALE"
    if score >= -3:
        return "DEBOLE / FRAGILE"
    return "NEGATIVA"


def bias_label(score: int) -> str:
    if score >= 7:
        return "Rialzista"
    if score >= 3:
        return "Costruttivo prudente"
    if score >= 0:
        return "Neutrale / misto"
    if score >= -3:
        return "Fragile"
    return "Ribassista"


def reliability_label(score: int) -> str:
    abs_score = abs(score)

    if abs_score >= 7:
        return "MEDIA / ALTA"
    if abs_score >= 3:
        return "MEDIA"
    return "BASSA / RACCOLTA DATI"


def coherent_action(asset: str, score: int) -> str:
    if asset == "BTC":
        if score >= 7:
            return "ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA"
        if score >= 3:
            return "ACCUMULA SU PULLBACK / NO SHORT"
        if score >= 0:
            return "HOLD / ATTESA CONFERME"
        if score >= -3:
            return "NON INSEGUIRE / RIDUCI RISCHIO"
        return "STAI FUORI / SHORT SOLO DOPO ROTTURA"

    if asset == "SOL":
        if score >= 7:
            return "HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA"
        if score >= 3:
            return "HOLD / TRANCHE PICCOLE, NO LEVA"
        if score >= 0:
            return "HOLD LEGGERO / ATTESA CONFERME"
        if score >= -3:
            return "TAKE PROFIT SU SPIKE / NON INSEGUIRE"
        return "STAI FUORI / VENDI PARZIALE"

    if asset == "DOGE":
        if score >= 3:
            return "SOLO TRANCHE PICCOLE / NO LEVA"
        if score >= 0:
            return "STAI ALLA FINESTRA"
        if score >= -3:
            return "EVITA LONG / SOLO RIMBALZI VELOCI"
        return "STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE"

    return "n/a"


def build_confirmations(asset: str, components: dict) -> str:
    technical = components[asset]["Tecnico"]["data"]
    sol_fractal = components[asset]["Frattale SOL"]["data"]

    resistance = technical.get("resistance")

    if asset == "BTC":
        if resistance is not None:
            return (
                f"Sopra {fmt_price(asset, resistance)} migliora; "
                "sopra la neckline tecnica successiva il recupero diventa più credibile."
            )
        return "Serve recupero delle resistenze tecniche principali."

    if asset == "SOL":
        levels = []

        if resistance is not None:
            levels.append(fmt_price(asset, resistance))

        first_confirmation = sol_fractal.get("first_confirmation")
        second_confirmation = sol_fractal.get("second_confirmation")

        if first_confirmation is not None:
            levels.append(fmt_price(asset, first_confirmation))

        if second_confirmation is not None:
            levels.append(fmt_price(asset, second_confirmation))

        if levels:
            return "Conferme sopra " + " / ".join(levels) + "."

        return "Serve recupero delle resistenze tecniche e frattali."

    if asset == "DOGE":
        if resistance is not None:
            return (
                f"Sopra {fmt_price(asset, resistance)} migliora, "
                "ma resta asset debole finché scanner e struttura non girano."
            )
        return "Serve recupero delle resistenze tecniche principali."

    return "n/a"


def build_invalidations(asset: str, components: dict) -> str:
    technical = components[asset]["Tecnico"]["data"]
    sol_fractal = components[asset]["Frattale SOL"]["data"]

    support = technical.get("support")

    if asset == "BTC":
        if support is not None:
            return f"Sotto {fmt_price(asset, support)} il quadro tecnico peggiora."
        return "Sotto i supporti tecnici principali il quadro peggiora."

    if asset == "SOL":
        levels = []

        soft_invalidation = sol_fractal.get("soft_invalidation")
        strong_invalidation = sol_fractal.get("strong_invalidation")

        if soft_invalidation is not None:
            levels.append(fmt_price(asset, soft_invalidation))

        if support is not None:
            levels.append(fmt_price(asset, support))

        if strong_invalidation is not None:
            levels.append(fmt_price(asset, strong_invalidation))

        if levels:
            return "Allarmi sotto " + " / ".join(levels) + "."

        return "Sotto supporti tecnici e invalidazioni frattali il setup peggiora."

    if asset == "DOGE":
        if support is not None:
            return f"Sotto {fmt_price(asset, support)} il rischio ribassista aumenta."
        return "Sotto i supporti tecnici principali il rischio aumenta."

    return "n/a"


def asset_commentary(asset: str, score: int) -> str:
    if asset == "BTC":
        if score >= 7:
            return (
                "BTC ha una confluenza positiva forte. Resta comunque necessario evitare leva eccessiva: "
                "la conferma deve arrivare da prezzo e resistenze, non solo dallo score."
            )
        if score >= 3:
            return (
                "BTC è l'asset messo meglio nel breve. La struttura macro non è ancora "
                "pienamente rialzista, ma scanner, regime e segnali interni sono abbastanza "
                "coerenti per un recupero prudente."
            )
        if score >= 0:
            return (
                "BTC è in fase mista. Non è abbastanza debole da autorizzare short semplici, "
                "ma non ha ancora una conferma piena."
            )
        return (
            "BTC si è indebolito. In questo caso conta più proteggere il rischio che inseguire "
            "un recupero non confermato."
        )

    if asset == "SOL":
        if score >= 7:
            return (
                "SOL ha una confluenza molto interessante, ma resta più rischiosa di BTC. "
                "Le conferme tecniche e frattali devono comunque reggere prima di usare leva."
            )
        if score >= 3:
            return (
                "SOL ha una confluenza costruttiva, ma va ancora trattato come setup anticipato. "
                "La conferma vera arriva solo sopra le resistenze tecniche e frattali. "
                "Il modulo lifecycle/EMA200 resta utile come contesto, ma non viene più usato "
                "per aumentare il punteggio Global."
            )
        if score >= 0:
            return (
                "SOL è ancora in zona mista. Il frattale resta vivo, ma serve conferma di prezzo. "
                "Meglio evitare leva e ragionare solo a tranche piccole."
            )
        return (
            "SOL è fragile nel breve. Il frattale da solo non basta: se non recupera le conferme, "
            "il rischio è di inseguire uno spike scaricato."
        )

    if asset == "DOGE":
        if score <= -4:
            return (
                "DOGE resta l'asset più debole. Anche se può fare rimbalzi o spike, "
                "la confluenza generale resta negativa rispetto a BTC e SOL."
            )
        return (
            "DOGE non ha ancora una confluenza pulita. Serve conferma tecnica prima di trattarlo "
            "come asset forte."
        )

    return ""


def build_report(components: dict):
    generated = now_utc_str()

    summary_rows = []
    score_rows = []

    component_order = [
        "Scanner",
        "Scanner path",
        "Market regime",
        "Tecnico",
        "Classic technical",
        "Frattale SOL",
        "Fractal path",
        "RSI top-cycle",
        "Lifecycle EMA",
        "Futures",
        "Daily change",
    ]

    results = {}

    for asset in ASSETS:
        score = total_score(components[asset])
        results[asset] = {
            "score": score,
            "confluence": confluence_label(score),
            "bias": bias_label(score),
            "reliability": reliability_label(score),
            "action": coherent_action(asset, score),
            "confirmations": build_confirmations(asset, components),
            "invalidations": build_invalidations(asset, components),
        }

        summary_rows.append(
            [
                asset,
                fmt_signed_int(score),
                results[asset]["confluence"],
                results[asset]["bias"],
                results[asset]["reliability"],
                results[asset]["action"],
                results[asset]["confirmations"],
                results[asset]["invalidations"],
            ]
        )

        score_rows.append(
            [
                asset,
                fmt_signed_int(components[asset]["Scanner"]["score"]),
                fmt_signed_int(components[asset]["Scanner path"]["score"]),
                fmt_signed_int(components[asset]["Market regime"]["score"]),
                fmt_signed_int(components[asset]["Tecnico"]["score"]),
                fmt_signed_int(components[asset]["Classic technical"]["score"]),
                fmt_signed_int(components[asset]["Frattale SOL"]["score"]),
                fmt_signed_int(components[asset]["Fractal path"]["score"]),
                fmt_signed_int(components[asset]["RSI top-cycle"]["score"]),
                fmt_signed_int(components[asset]["Lifecycle EMA"]["score"]),
                fmt_signed_int(components[asset]["Futures"]["score"]),
                fmt_signed_int(components[asset]["Daily change"]["score"]),
                fmt_signed_int(score),
            ]
        )

    lines = []

    lines.append("# Sintesi finale di confluenza")
    lines.append("")
    lines.append(f"Generato: {generated}")
    lines.append("")
    lines.append("Questo report mette insieme i moduli principali dello scanner e controlla se si confermano o si contraddicono.")
    lines.append("")
    lines.append("Moduli letti:")
    lines.append("")
    lines.append("- Scanner frattale/statistico a 30 giorni")
    lines.append("- Scanner path / cono previsionale")
    lines.append("- Market regime match")
    lines.append("- Struttura tecnica classica precedente")
    lines.append("- Classic technical confirmation, nuovo filtro tecnico completo")
    lines.append("- Frattale BTC 2022 vs SOL 2026, solo per SOL")
    lines.append("- Fractal path tracker, solo per SOL")
    lines.append("- RSI top-cycle, soprattutto per SOL")
    lines.append("- Major alt lifecycle squeeze / EMA200 weekly, solo per SOL")
    lines.append("- Futures / liquidazioni")
    lines.append("- Cambiamento giornaliero")
    lines.append("")
    lines.append(
        "Nota importante: **Lifecycle EMA200 viene letto e mostrato, ma ora vale sempre 0 punti nel Global Confluence**. "
        "Serve come contesto, non come conferma operativa."
    )
    lines.append("")
    lines.append(
        "Nota nuovo modulo: **Classic technical confirmation pesa massimo ±1** perché è un filtro di conferma "
        "e in parte si sovrappone alla struttura tecnica già esistente."
    )
    lines.append("")
    lines.append("## Sintesi operativa")
    lines.append("")
    lines.append(
        md_table(
            [
                "Asset",
                "Punteggio",
                "Confluenza",
                "Bias",
                "Affidabilità",
                "Azione coerente",
                "Conferme",
                "Invalidazioni",
            ],
            summary_rows,
        )
    )
    lines.append("")
    lines.append("## Punteggi per modulo")
    lines.append("")
    lines.append(
        md_table(
            [
                "Asset",
                "Scanner",
                "Scanner path",
                "Market regime",
                "Tecnico",
                "Classic tech",
                "Frattale SOL",
                "Fractal path",
                "RSI top-cycle",
                "Lifecycle EMA",
                "Futures",
                "Daily change",
                "Totale",
            ],
            score_rows,
        )
    )
    lines.append("")
    lines.append("## Lettura asset per asset")

    for asset in ASSETS:
        r = results[asset]
        lines.append("")
        lines.append(f"### {asset}")
        lines.append("")
        lines.append(f"- Confluenza: **{r['confluence']}**")
        lines.append(f"- Bias: **{r['bias']}**")
        lines.append(f"- Punteggio finale: **{fmt_signed_int(r['score'])}**")
        lines.append(f"- Affidabilità: **{r['reliability']}**")
        lines.append(f"- Azione coerente: **{r['action']}**")
        lines.append("")
        lines.append(asset_commentary(asset, r["score"]))
        lines.append("")
        lines.append("Dettaglio moduli:")
        lines.append("")

        for component_name in component_order:
            comp = components[asset][component_name]
            lines.append(
                f"- {component_name}: **{fmt_signed_int(comp['score'])}** — {comp['detail']}"
            )

        lines.append("")
        lines.append(f"Conferme: {r['confirmations']}")
        lines.append("")
        lines.append(f"Invalidazioni: {r['invalidations']}")

    lines.append("")
    lines.append("")
    lines.append("## Come leggere il punteggio")
    lines.append("")
    lines.append("- +7 o più: confluenza positiva forte.")
    lines.append("- Da +3 a +6: confluenza moderatamente positiva.")
    lines.append("- Da 0 a +2: confluenza parziale o mista.")
    lines.append("- Da -1 a -3: confluenza debole o fragile.")
    lines.append("- -4 o meno: confluenza negativa.")
    lines.append("")
    lines.append(
        "Nota: Scanner path e Fractal path sono già integrati, ma finché hanno pochi controlli restano quasi sempre a punteggio 0."
    )
    lines.append(
        "Servono almeno 5 controlli prima di influire leggermente, e 30+ controlli prima di pesare davvero."
    )
    lines.append("")
    lines.append(
        "Nota lifecycle EMA200: il modulo Major alt lifecycle squeeze resta nel report, ma pesa **0** nel Global "
        "perché EMA50/EMA200 e target EMA200 sono contesto, non conferme dirette di prezzo."
    )
    lines.append("")
    lines.append(
        "Nota Classic technical: il nuovo modulo è utile per capire se il setup è confermato davvero, "
        "ma il suo peso resta prudente per evitare doppio conteggio con il modulo tecnico già presente."
    )

    return "\n".join(lines).rstrip() + "\n", results


def write_metrics_csv(components: dict, results: dict) -> None:
    METRICS_CSV_PATH.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "generated_utc",
        "asset",
        "score",
        "global_score",
        "confluence",
        "bias",
        "reliability",
        "action",
        "confirmations",
        "invalidations",
        "scanner_score",
        "scanner_direction",
        "scanner_positive_rate",
        "scanner_return_p50",
        "scanner_path_score",
        "scanner_path_controls",
        "market_score",
        "market_matches",
        "market_positive_30d",
        "market_return_p50",
        "technical_score_component",
        "technical_raw_score",
        "technical_verdict",
        "technical_support",
        "technical_resistance",
        "classic_technical_score_component",
        "classic_technical_raw_score",
        "classic_technical_verdict",
        "classic_technical_action",
        "classic_technical_risk",
        "classic_technical_stage",
        "classic_technical_structure",
        "classic_technical_wyckoff",
        "classic_technical_price_confirmation_score",
        "classic_technical_support",
        "classic_technical_resistance",
        "sol_fractal_score",
        "sol_fractal_verdict",
        "sol_fractal_similarity",
        "sol_fractal_tracking",
        "sol_fractal_phase",
        "sol_fractal_risk",
        "fractal_path_score",
        "fractal_path_controls",
        "rsi_score",
        "rsi_risk",
        "lifecycle_score_component",
        "lifecycle_raw_score",
        "lifecycle_bias",
        "lifecycle_ema200",
        "lifecycle_upside",
        "futures_score",
        "futures_reading",
        "daily_change_score",
        "daily_change",
        "daily_tone",
    ]

    generated = datetime.now(timezone.utc).isoformat()

    rows = []

    for asset in ASSETS:
        c = components[asset]
        r = results[asset]

        row = {
            "generated_utc": generated,
            "asset": asset,
            "score": r["score"],
            "global_score": r["score"],
            "confluence": r["confluence"],
            "bias": r["bias"],
            "reliability": r["reliability"],
            "action": r["action"],
            "confirmations": r["confirmations"],
            "invalidations": r["invalidations"],
            "scanner_score": c["Scanner"]["score"],
            "scanner_direction": c["Scanner"]["data"].get("direction"),
            "scanner_positive_rate": c["Scanner"]["data"].get("positive_rate"),
            "scanner_return_p50": c["Scanner"]["data"].get("return_p50"),
            "scanner_path_score": c["Scanner path"]["score"],
            "scanner_path_controls": c["Scanner path"]["data"].get("controls"),
            "market_score": c["Market regime"]["score"],
            "market_matches": c["Market regime"]["data"].get("matches"),
            "market_positive_30d": c["Market regime"]["data"].get("positive_30d"),
            "market_return_p50": c["Market regime"]["data"].get("return_p50"),
            "technical_score_component": c["Tecnico"]["score"],
            "technical_raw_score": c["Tecnico"]["data"].get("technical_score"),
            "technical_verdict": c["Tecnico"]["data"].get("verdict"),
            "technical_support": c["Tecnico"]["data"].get("support"),
            "technical_resistance": c["Tecnico"]["data"].get("resistance"),
            "classic_technical_score_component": c["Classic technical"]["score"],
            "classic_technical_raw_score": c["Classic technical"]["data"].get("classic_raw_score"),
            "classic_technical_verdict": c["Classic technical"]["data"].get("classic_verdict"),
            "classic_technical_action": c["Classic technical"]["data"].get("classic_action"),
            "classic_technical_risk": c["Classic technical"]["data"].get("classic_risk"),
            "classic_technical_stage": c["Classic technical"]["data"].get("classic_stage"),
            "classic_technical_structure": c["Classic technical"]["data"].get("classic_structure"),
            "classic_technical_wyckoff": c["Classic technical"]["data"].get("classic_wyckoff"),
            "classic_technical_price_confirmation_score": c["Classic technical"]["data"].get("classic_price_confirmation_score"),
            "classic_technical_support": c["Classic technical"]["data"].get("classic_support"),
            "classic_technical_resistance": c["Classic technical"]["data"].get("classic_resistance"),
            "sol_fractal_score": c["Frattale SOL"]["score"],
            "sol_fractal_verdict": c["Frattale SOL"]["data"].get("verdict"),
            "sol_fractal_similarity": c["Frattale SOL"]["data"].get("similarity"),
            "sol_fractal_tracking": c["Frattale SOL"]["data"].get("tracking"),
            "sol_fractal_phase": c["Frattale SOL"]["data"].get("phase"),
            "sol_fractal_risk": c["Frattale SOL"]["data"].get("risk"),
            "fractal_path_score": c["Fractal path"]["score"],
            "fractal_path_controls": c["Fractal path"]["data"].get("controls"),
            "rsi_score": c["RSI top-cycle"]["score"],
            "rsi_risk": c["RSI top-cycle"]["data"].get("risk"),
            "lifecycle_score_component": c["Lifecycle EMA"]["score"],
            "lifecycle_raw_score": c["Lifecycle EMA"]["data"].get("lifecycle_score"),
            "lifecycle_bias": c["Lifecycle EMA"]["data"].get("bias"),
            "lifecycle_ema200": c["Lifecycle EMA"]["data"].get("ema200"),
            "lifecycle_upside": c["Lifecycle EMA"]["data"].get("upside"),
            "futures_score": c["Futures"]["score"],
            "futures_reading": c["Futures"]["data"].get("reading"),
            "daily_change_score": c["Daily change"]["score"],
            "daily_change": c["Daily change"]["data"].get("change"),
            "daily_tone": c["Daily change"]["data"].get("tone"),
        }

        rows.append(row)

    with METRICS_CSV_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    latest_text = read_text(LATEST_REPORT_PATH)
    source_text = clean_source_text(latest_text)

    components = build_components(source_text)
    report_md, results = build_report(components)

    write_text(REPORT_PATH, report_md)
    write_metrics_csv(components, results)

    if latest_text:
        updated_latest = replace_block(latest_text, report_md)
        write_text(LATEST_REPORT_PATH, updated_latest)
    else:
        write_text(LATEST_REPORT_PATH, f"{START_MARKER}\n{report_md}{END_MARKER}\n")

    print(f"Global Confluence report scritto in: {REPORT_PATH}")
    print(f"Metriche Global Confluence scritte in: {METRICS_CSV_PATH}")


if __name__ == "__main__":
    main()
