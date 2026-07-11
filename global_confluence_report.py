import csv
import re
from datetime import datetime, timezone
from pathlib import Path


REPORTS_DIR = Path("reports")
LATEST_REPORT_PATH = REPORTS_DIR / "latest_report.md"
REPORT_PATH = REPORTS_DIR / "global_confluence_report.md"
METRICS_CSV_PATH = REPORTS_DIR / "global_confluence_metrics.csv"

TECHNICAL_METRICS_PATH = REPORTS_DIR / "technical_structure_metrics.csv"
CLASSIC_TECH_METRICS_PATH = REPORTS_DIR / "classic_technical_confirmation_metrics.csv"
EXCHANGE_MICROSTRUCTURE_METRICS_PATH = REPORTS_DIR / "exchange_microstructure_metrics.csv"
# EXCHANGE_MICROSTRUCTURE_GLOBAL_PATCH_V2_1

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

# Scanner e Market Regime derivano dagli stessi analoghi storici.
# Vengono quindi fusi in una sola famiglia statistica, con massimo ±4.
STATISTICAL_FAMILY_MAX_ABS = 4
MARKET_MIN_MATCHES = 5
MARKET_CONFIRM_MIN_MATCHES = 10


WEIGHTED_COMPONENTS = [
    "Famiglia statistica",
    "Scanner path",
    "Tecnico",
    "Classic technical",
    "Frattale SOL",
    "Fractal path",
    "RSI top-cycle",
    "Lifecycle EMA",
    "Exchange flow",
    "Daily change",
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

    if not s or s.lower() in {"n/a", "nan", "none", "-", "n/d"}:
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


def sign_int(value: int) -> int:
    if value > 0:
        return 1
    if value < 0:
        return -1
    return 0


def clamp_int(value: int, minimum: int, maximum: int) -> int:
    return max(minimum, min(maximum, int(value)))


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
        r"Return normale fra 30 giorni:\s*\*\*.*?\*\*\s*\(([+\-]?\d[\d.,]*)%\)",
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

    if matches is not None and matches >= MARKET_MIN_MATCHES and positive_30d is not None and return_p50 is not None:
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


def combine_scanner_market_components(scanner_component: dict, market_component: dict):
    """
    Unisce Scanner e Market Regime senza doppio conteggio.

    Regole:
    - Scanner è il punteggio principale.
    - Market Regime può aggiungere al massimo 1 punto di conferma se ha almeno
      10 match e concorda col segno dello Scanner.
    - Se i due moduli sono discordanti, il punteggio viene ridotto o azzerato.
    - Se Scanner è neutro, Market Regime da solo vale al massimo ±1.
    - Limite assoluto della famiglia: ±4.
    """

    scanner_score = int(scanner_component.get("score", 0) or 0)
    market_score = int(market_component.get("score", 0) or 0)
    matches = parse_number(market_component.get("data", {}).get("matches"))
    matches_int = int(matches) if matches is not None else 0

    rule = ""

    if scanner_score == 0:
        if matches_int >= MARKET_CONFIRM_MIN_MATCHES and market_score != 0:
            family_score = sign_int(market_score)
            rule = "Scanner neutro: il regime da solo vale al massimo ±1."
        else:
            family_score = 0
            rule = "Scanner neutro e regime non abbastanza forte o non abbastanza popolato."

    elif market_score == 0 or matches_int < MARKET_MIN_MATCHES:
        family_score = scanner_score
        if matches_int < MARKET_MIN_MATCHES:
            rule = "Regime ignorato: meno di 5 match utili."
        else:
            rule = "Regime neutro: resta il punteggio Scanner."

    elif sign_int(scanner_score) == sign_int(market_score):
        if matches_int >= MARKET_CONFIRM_MIN_MATCHES:
            family_score = scanner_score + sign_int(scanner_score)
            rule = "Scanner e regime concordi con almeno 10 match: bonus massimo di 1 punto."
        else:
            family_score = scanner_score
            rule = "Scanner e regime concordi, ma i match sono meno di 10: nessun bonus."

    else:
        if matches_int >= MARKET_CONFIRM_MIN_MATCHES and abs(market_score) >= abs(scanner_score):
            family_score = 0
            rule = "Scanner e regime fortemente discordanti: famiglia neutralizzata."
        else:
            family_score = scanner_score - sign_int(scanner_score)
            rule = "Scanner e regime discordanti: punteggio Scanner ridotto di 1."

    family_score = clamp_int(
        family_score,
        -STATISTICAL_FAMILY_MAX_ABS,
        STATISTICAL_FAMILY_MAX_ABS,
    )

    detail = (
        f"Scanner grezzo {fmt_signed_int(scanner_score)}, "
        f"Market Regime grezzo {fmt_signed_int(market_score)}, "
        f"match regime {matches_int}. {rule} "
        f"Punteggio contato nel Global: {fmt_signed_int(family_score)}."
    )

    return component_template(
        family_score,
        detail,
        {
            "scanner_raw_score": scanner_score,
            "market_raw_score": market_score,
            "market_matches": matches_int,
            "rule": rule,
            "max_abs": STATISTICAL_FAMILY_MAX_ABS,
        },
    )


def parse_technical_component(block: str, asset: str):
    """
    Legge prima il CSV strutturato prodotto da technical_structure_report.py.

    Il Markdown resta soltanto come fallback. In questo modo l'aggiunta o lo
    spostamento di colonne nella tabella del report non può più trasformare il
    pattern score in divergenza, il pattern dominante in Wyckoff o il supporto
    in resistenza.
    """

    rows = read_csv_rows(TECHNICAL_METRICS_PATH)
    data = {}

    for row in rows:
        row_asset = clean_cell(row.get("asset")).upper()
        if row_asset == asset:
            data = row
            break

    def pattern_prefix(name):
        n = clean_cell(name).lower()

        if "doppio minimo" in n:
            return "double_bottom"
        if "triplo minimo" in n:
            return "triple_bottom"
        if "bottom" in n:
            return "adam_eve_bottom"
        if "doppio massimo" in n:
            return "double_top"
        if "triplo massimo" in n:
            return "triple_top"
        if "top" in n:
            return "adam_eve_top"

        return ""

    def row_number(key):
        return parse_number(data.get(key)) if data else None

    def row_text(key):
        return clean_cell(data.get(key)) if data else ""

    def technical_label(value):
        mapping = {
            "BULLISH_TECNICO": "RIALZISTA TECNICO",
            "COSTRUTTIVO_MA_NON_CONFERMATO": "COSTRUTTIVO MA NON CONFERMATO",
            "NEUTRALE_MISTO": "NEUTRALE / MISTO",
            "DEBOLE": "DEBOLE",
            "BEARISH_TECNICO": "RIBASSISTA TECNICO",
            "BULLISH_TREND": "rialzista",
            "BEARISH_TREND": "ribassista",
            "MIXED_TREND": "misto",
            "HH_HL_UPSTRUCTURE": "rialzista con massimi e minimi crescenti",
            "LH_LL_DOWNSTRUCTURE": "ribassista con massimi e minimi decrescenti",
            "COMPRESSION_TRIANGLE": "Compressione / triangolo",
            "EXPANDING_VOLATILITY": "Volatilità in espansione",
            "BULLISH_RSI_DIVERGENCE": "rialzista RSI",
            "BEARISH_RSI_DIVERGENCE": "ribassista RSI",
            "HIDDEN_BULLISH_RSI_DIVERGENCE": "rialzista nascosta RSI",
            "HIDDEN_BEARISH_RSI_DIVERGENCE": "ribassista nascosta RSI",
            "NONE": "Nessuna",
            "ACCUMULATION_CANDIDATE": "Possibile accumulazione",
            "DISTRIBUTION_CANDIDATE": "Possibile distribuzione",
            "MARKUP": "Markup / fase rialzista",
            "MARKDOWN": "Markdown / fase ribassista",
            "RANGE_OR_UNKNOWN": "Range / fase non chiara",
        }

        raw = clean_cell(value)
        if not raw:
            return "n/a"

        if "," in raw:
            return ", ".join(mapping.get(part.strip(), part.strip()) for part in raw.split(","))

        return mapping.get(raw, raw.replace("_", " "))

    tech_score = None
    verdict = ""
    trend = ""
    structure = ""
    divergence = ""
    wyckoff = ""
    support = None
    resistance = None
    price = None
    pattern_score = None
    dominant_bullish_pattern = ""
    dominant_bullish_status = ""
    dominant_bullish_score = None
    dominant_bearish_pattern = ""
    dominant_bearish_status = ""
    dominant_bearish_score = None
    bullish_neckline = None
    bullish_target = None
    bullish_invalidation = None
    bullish_relation = ""
    bearish_neckline = None
    bearish_target = None
    bearish_invalidation = None
    bearish_relation = ""
    source = ""

    if data:
        source = TECHNICAL_METRICS_PATH.name
        price = row_number("price")
        tech_score = row_number("technical_score")
        verdict = row_text("verdict")
        trend = row_text("trend")
        structure = row_text("structure")
        divergence = row_text("divergence")
        wyckoff = row_text("wyckoff")
        support = row_number("support")
        resistance = row_number("resistance")
        pattern_score = row_number("pattern_score")

        dominant_bullish_pattern = row_text("dominant_bullish_pattern")
        dominant_bullish_status = row_text("dominant_bullish_status")
        dominant_bullish_score = row_number("dominant_bullish_score")
        dominant_bearish_pattern = row_text("dominant_bearish_pattern")
        dominant_bearish_status = row_text("dominant_bearish_status")
        dominant_bearish_score = row_number("dominant_bearish_score")

        bull_prefix = pattern_prefix(dominant_bullish_pattern)
        bear_prefix = pattern_prefix(dominant_bearish_pattern)

        if bull_prefix:
            bullish_neckline = row_number(f"{bull_prefix}_neckline")
            bullish_target = row_number(f"{bull_prefix}_target")
            bullish_invalidation = row_number(f"{bull_prefix}_invalidation_level")
            bullish_relation = row_text(f"{bull_prefix}_current_relation")

        if bear_prefix:
            bearish_neckline = row_number(f"{bear_prefix}_neckline")
            bearish_target = row_number(f"{bear_prefix}_target")
            bearish_invalidation = row_number(f"{bear_prefix}_invalidation_level")
            bearish_relation = row_text(f"{bear_prefix}_current_relation")

    if not data:
        source = "TECHNICAL_STRUCTURE markdown fallback"

        for line in block.splitlines():
            cells = split_md_row(line)
            if not cells or len(cells) < 12:
                continue

            if cells[0].upper() != asset:
                continue

            price = parse_number(cells[1])
            tech_score = parse_number(cells[2])
            verdict = clean_cell(cells[3])
            trend = clean_cell(cells[4])
            structure = clean_cell(cells[6])
            pattern_score = parse_number(cells[7])

            bull_cell = clean_cell(cells[8])
            bear_cell = clean_cell(cells[9])

            if " / " in bull_cell:
                dominant_bullish_pattern, dominant_bullish_status = bull_cell.rsplit(" / ", 1)
            elif bull_cell.lower() != "nessuno":
                dominant_bullish_pattern = bull_cell

            if " / " in bear_cell:
                dominant_bearish_pattern, dominant_bearish_status = bear_cell.rsplit(" / ", 1)
            elif bear_cell.lower() != "nessuno":
                dominant_bearish_pattern = bear_cell

            support = parse_number(cells[10])
            resistance = parse_number(cells[11])
            break

        detail_section = extract_section_after(
            block,
            rf"###\s+{asset}\b",
            r"\n###\s+|\n##\s+",
        )

        if tech_score is None:
            m = re.search(r"Punteggio tecnico:\s*\*\*([+\-]?\d+)", detail_section, flags=re.IGNORECASE)
            if m:
                tech_score = parse_number(m.group(1))

        if not verdict:
            m = re.search(r"Verdetto:\s*\*\*([^*]+)\*\*", detail_section, flags=re.IGNORECASE)
            if m:
                verdict = clean_cell(m.group(1))

        if not trend:
            m = re.search(r"Trend:\s*\*\*([^*]+)\*\*", detail_section, flags=re.IGNORECASE)
            if m:
                trend = clean_cell(m.group(1))

        if not structure:
            m = re.search(r"Struttura:\s*\*\*([^*]+)\*\*", detail_section, flags=re.IGNORECASE)
            if m:
                structure = clean_cell(m.group(1))

        m = re.search(r"Divergenza:\s*\*\*([^*]+)\*\*", detail_section, flags=re.IGNORECASE)
        if m:
            divergence = clean_cell(m.group(1))

        m = re.search(r"Fase Wyckoff candidata:\s*\*\*([^*]+)\*\*", detail_section, flags=re.IGNORECASE)
        if m:
            wyckoff = clean_cell(m.group(1))

        if support is None:
            m = re.search(r"Supporto più vicino:\s*\*\*([^*]+)\*\*", detail_section, flags=re.IGNORECASE)
            if m:
                support = parse_number(m.group(1))

        if resistance is None:
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

    pattern_bits = []

    if dominant_bullish_pattern:
        pattern_bits.append(
            f"rialzista {dominant_bullish_pattern} / {(dominant_bullish_status or 'n/a').replace('_', ' ')}"
        )

    if dominant_bearish_pattern:
        pattern_bits.append(
            f"ribassista {dominant_bearish_pattern} / {(dominant_bearish_status or 'n/a').replace('_', ' ')}"
        )

    pattern_text = "; ".join(pattern_bits) if pattern_bits else "nessun dominante"
    pattern_score_text = (
        fmt_signed_int(int(pattern_score)) if pattern_score is not None else "n/a"
    )

    detail = (
        f"Score tecnico {int(tech_score) if tech_score is not None else 'n/a'}/12, "
        f"verdetto {technical_label(verdict).lower()}, "
        f"trend {technical_label(trend).lower()}, "
        f"struttura {technical_label(structure).lower()}, "
        f"divergenza {technical_label(divergence).lower()}, "
        f"Wyckoff {technical_label(wyckoff).lower()}, "
        f"pattern score {pattern_score_text} ({pattern_text}). "
        f"Fonte: {source}."
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
            "pattern_score": pattern_score,
            "dominant_bullish_pattern": dominant_bullish_pattern,
            "dominant_bullish_status": dominant_bullish_status,
            "dominant_bullish_score": dominant_bullish_score,
            "dominant_bearish_pattern": dominant_bearish_pattern,
            "dominant_bearish_status": dominant_bearish_status,
            "dominant_bearish_score": dominant_bearish_score,
            "bullish_neckline": bullish_neckline,
            "bullish_target": bullish_target,
            "bullish_invalidation": bullish_invalidation,
            "bullish_relation": bullish_relation,
            "bearish_neckline": bearish_neckline,
            "bearish_target": bearish_target,
            "bearish_invalidation": bearish_invalidation,
            "bearish_relation": bearish_relation,
            "source": source,
        },
    )


def parse_classic_technical_component(block: str, asset: str):
    """
    Classic technical confirmation.

    Pesa poco nel Global, perché si sovrappone in parte al vecchio Technical
    Structure. È un filtro di conferma, non il motore principale.
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
    structural_similarity = None
    live_adherence = None
    live_error = None
    current_gap = None
    operational_weight = None
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

    m = re.search(r"Somiglianza strutturale:\*\*\s*([+\-]?\d[\d.,]*)%", block, flags=re.IGNORECASE)
    if m:
        structural_similarity = parse_number(m.group(1))

    if structural_similarity is None:
        structural_similarity = similarity

    m = re.search(r"Aderenza prezzo live:\*\*\s*([+\-]?\d[\d.,]*)%", block, flags=re.IGNORECASE)
    if m:
        live_adherence = parse_number(m.group(1))

    m = re.search(r"Errore medio live:\*\*\s*([+\-]?\d[\d.,]*)%", block, flags=re.IGNORECASE)
    if m:
        live_error = parse_number(m.group(1))

    m = re.search(r"Gap prezzo corrente:\*\*\s*([+\-]?\d[\d.,]*)%", block, flags=re.IGNORECASE)
    if m:
        current_gap = parse_number(m.group(1))

    m = re.search(r"Peso operativo suggerito:\*\*\s*([+\-]?\d[\d.,]*)", block, flags=re.IGNORECASE)
    if m:
        operational_weight = parse_number(m.group(1))

    m = re.search(r"Affidabilit[àa]:\*\*\s*([^\n*]+)", block, flags=re.IGNORECASE)
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

        if "milestone analogica breve" in label or "prima conferma" in label:
            first_confirmation = parse_number(cells[1])
        elif "milestone analogica estesa" in label or "seconda conferma" in label:
            second_confirmation = parse_number(cells[1])
        elif "invalidazione soft" in label:
            soft_invalidation = parse_number(cells[1])
        elif "invalidazione forte" in label:
            strong_invalidation = parse_number(cells[1])

    if operational_weight is not None:
        score = clamp_int(round(operational_weight), -2, 3)
    else:
        # Fallback prudente per vecchi report: niente ricerca generica della
        # sottostringa "SI", che poteva produrre falsi positivi.
        verdict_u = verdict or ""
        tracking_u = tracking or ""

        if "ROTTO" in verdict_u or verdict_u.startswith("NO,") or verdict_u == "NO":
            score = -2
        elif verdict_u.startswith("SI,"):
            if structural_similarity is not None and structural_similarity >= 80:
                score = 3
            elif structural_similarity is not None and structural_similarity >= 72:
                score = 2
            else:
                score = 1
        elif "PARZIALMENTE SI" in verdict_u:
            if (
                structural_similarity is not None
                and structural_similarity >= 78
                and "STABILE" in tracking_u
                and (live_error is None or live_error <= 12)
                and (current_gap is None or abs(current_gap) <= 12)
            ):
                score = 2
            elif (
                structural_similarity is not None
                and structural_similarity >= 70
                and "STABILE" in tracking_u
                and (live_error is None or live_error <= 15)
                and (current_gap is None or abs(current_gap) <= 15)
            ):
                score = 1
            else:
                score = 0
        else:
            score = 0

    detail = (
        f"Verdetto {verdict or 'n/a'}, "
        f"somiglianza strutturale {fmt_pct(structural_similarity)}, "
        f"aderenza live {fmt_pct(live_adherence)}, "
        f"errore live {fmt_pct(live_error)}, "
        f"gap corrente {fmt_pct(current_gap)}, "
        f"peso operativo {fmt_signed_int(score)}, "
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
            "structural_similarity": structural_similarity,
            "live_adherence": live_adherence,
            "live_error": live_error,
            "current_gap": current_gap,
            "operational_weight": operational_weight,
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

    current_gap = None
    gap_ma7 = None
    abs_error_ma7 = None
    live_error = None

    patterns = {
        "current_gap": r"Ultimo gap firmato:\s*\*\*([+\-]?\d[\d.,]*)%",
        "gap_ma7": r"Gap firmato medio 7g:\s*\*\*([+\-]?\d[\d.,]*)%",
        "abs_error_ma7": r"Errore assoluto medio 7g:\s*\*\*([+\-]?\d[\d.,]*)%",
        "live_error": r"Errore assoluto medio da inizio programma:\s*\*\*([+\-]?\d[\d.,]*)%",
    }

    for key, pattern in patterns.items():
        m = re.search(pattern, block, flags=re.IGNORECASE)
        if not m:
            continue
        value = parse_number(m.group(1))
        if key == "current_gap":
            current_gap = value
        elif key == "gap_ma7":
            gap_ma7 = value
        elif key == "abs_error_ma7":
            abs_error_ma7 = value
        elif key == "live_error":
            live_error = value

    data = {
        "controls": max_controls,
        "current_gap": current_gap,
        "gap_ma7": gap_ma7,
        "abs_error_ma7": abs_error_ma7,
        "live_error": live_error,
    }

    if max_controls <= 0:
        detail = (
            "Tracking operativo, ma nessuna milestone settimanale ancora verificata. "
            f"Gap corrente {fmt_pct(current_gap)}, errore live {fmt_pct(live_error)}. "
            "Il modulo non pesa finché non maturano abbastanza controlli."
        )
        return component_template(0, detail, data)

    if max_controls < 5:
        detail = (
            f"Raccolta dati. Controlli disponibili {max_controls}, "
            f"gap corrente {fmt_pct(current_gap)}, errore live {fmt_pct(live_error)}. "
            "Servono almeno 5 controlli prima di pesare il percorso frattale."
        )
        return component_template(0, detail, data)

    # Anche dopo 5 controlli, il modulo resta neutro se il percorso ancorato
    # è troppo distante. Evita che l'accuratezza dello scenario riancorato
    # venga scambiata per conferma del frattale originale.
    if (
        current_gap is not None
        and abs(current_gap) > 12
    ) or (
        live_error is not None
        and live_error > 12
    ):
        detail = (
            f"Controlli disponibili {max_controls}, ma percorso ancorato non aderente: "
            f"gap {fmt_pct(current_gap)}, errore live {fmt_pct(live_error)}. Peso 0."
        )
        return component_template(0, detail, data)

    detail = (
        f"Controlli disponibili {max_controls}, gap {fmt_pct(current_gap)}, "
        f"errore live {fmt_pct(live_error)}. Il percorso è valutabile ma resta secondario."
    )
    return component_template(0, detail, data)


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



def parse_exchange_microstructure_component(asset: str):
    """Read structured exchange metrics; Global score is already calibration-gated."""
    if not EXCHANGE_MICROSTRUCTURE_METRICS_PATH.exists():
        return component_template(
            0,
            "Dati exchange non disponibili; modulo neutrale.",
            {"raw_score": None, "candidate_score": 0, "confidence": "MANCANTE", "bias": "n/a", "data_coverage": 0},
        )

    try:
        with EXCHANGE_MICROSTRUCTURE_METRICS_PATH.open("r", encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
    except Exception as exc:
        return component_template(
            0,
            f"Metriche exchange non leggibili: {type(exc).__name__}.",
            {"raw_score": None, "candidate_score": 0, "confidence": "ERRORE", "bias": "n/a", "data_coverage": 0},
        )

    row = next((item for item in rows if clean_cell(item.get("asset", "")).upper() == asset), None)
    if row is None:
        return component_template(
            0,
            f"Riga exchange {asset} mancante; modulo neutrale.",
            {"raw_score": None, "candidate_score": 0, "confidence": "MANCANTE", "bias": "n/a", "data_coverage": 0},
        )

    raw_score = parse_number(row.get("raw_score"))
    candidate_score = max(-1, min(1, parse_int(row.get("candidate_global_score"), 0)))
    reported_score = max(-1, min(1, parse_int(row.get("global_score"), 0)))
    score = reported_score
    confidence = clean_cell(row.get("confidence", "")) or "n/a"
    bias = clean_cell(row.get("bias", "")) or "n/a"
    activation = clean_cell(row.get("global_activation_status", "")) or "n/a"
    coverage = parse_number(row.get("data_coverage"))
    exchange_count = parse_int(row.get("exchange_count"), 0)
    kucoin_available = clean_cell(row.get("kucoin_available", "")).lower() in {"true", "1", "yes", "si", "sì"}
    flow = parse_number(row.get("flow_score"))
    derivatives = parse_number(row.get("derivatives_score"))
    crowding = parse_number(row.get("crowding_score"))
    technical_confirmation = parse_number(row.get("technical_confirmation_score"))
    detail_text = clean_cell(row.get("detail", ""))
    if not detail_text:
        detail_text = (
            f"Raw {raw_score if raw_score is not None else 'n/a'}, candidato {candidate_score:+d}, "
            f"flow {flow if flow is not None else 'n/a'}, derivati {derivatives if derivatives is not None else 'n/a'}, "
            f"affollamento {crowding if crowding is not None else 'n/a'}, "
            f"conferme tecniche {technical_confirmation if technical_confirmation is not None else 'n/a'}."
        )
    detail = (
        f"{detail_text} Bias {bias}; confidenza {confidence}; fonti {exchange_count}/3; "
        f"KuCoin {'OK' if kucoin_available else 'mancante'}; "
        f"copertura {fmt_pct_plain(coverage * 100 if coverage is not None and coverage <= 1.0 else coverage)}. "
        f"Attivazione: {activation}. Il Global usa {score:+d}; il candidato {candidate_score:+d} resta misurato separatamente."
    )
    return component_template(
        score,
        detail,
        {
            "raw_score": raw_score,
            "candidate_score": candidate_score,
            "reported_score": reported_score,
            "confidence": confidence,
            "bias": bias,
            "activation_status": activation,
            "data_coverage": coverage,
            "exchange_count": exchange_count,
            "kucoin_available": kucoin_available,
            "flow_score": flow,
            "derivatives_score": derivatives,
            "crowding_score": crowding,
            "technical_confirmation_score": technical_confirmation,
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
        scanner_component = parse_scanner_component(source_text, asset)
        market_component = parse_market_component(market_block, asset)
        statistical_family = combine_scanner_market_components(
            scanner_component,
            market_component,
        )

        components[asset] = {
            "Famiglia statistica": statistical_family,
            "Scanner": scanner_component,
            "Scanner path": parse_scanner_path_component(scanner_forecast_block, asset),
            "Market regime": market_component,
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
            "Exchange flow": parse_exchange_microstructure_component(asset),
            "Futures": parse_futures_component(futures_block, asset),
            "Daily change": parse_daily_change_component(daily_block, asset),
        }

    return components


def total_score(asset_components: dict) -> int:
    return int(
        sum(
            asset_components[name]["score"]
            for name in WEIGHTED_COMPONENTS
            if name in asset_components
        )
    )


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
            return "ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE"
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

    price = technical.get("price")
    resistance = technical.get("resistance")
    bullish_neckline = technical.get("bullish_neckline")
    bullish_pattern = technical.get("dominant_bullish_pattern")
    bullish_status = technical.get("dominant_bullish_status")
    bearish_invalidation = technical.get("bearish_invalidation")

    if asset == "BTC":
        parts = []

        if resistance is not None:
            parts.append(f"prima resistenza sopra {fmt_price(asset, resistance)}")

        if bullish_neckline is not None:
            pattern_name = bullish_pattern or "pattern rialzista"
            parts.append(
                f"conferma del {pattern_name.lower()} sopra {fmt_price(asset, bullish_neckline)}"
            )

        if parts:
            return "; ".join(parts).capitalize() + "."

        return "Serve recupero delle resistenze tecniche principali."

    if asset == "SOL":
        parts = []

        if bullish_neckline is not None:
            if price is not None and price >= bullish_neckline:
                parts.append(
                    f"{(bullish_pattern or 'Pattern rialzista')} "
                    f"{(bullish_status or '').lower().replace('_', ' ')} finché mantiene "
                    f"{fmt_price(asset, bullish_neckline)}"
                )
            else:
                parts.append(
                    f"conferma del {(bullish_pattern or 'pattern rialzista').lower()} "
                    f"sopra {fmt_price(asset, bullish_neckline)}"
                )

        if resistance is not None:
            parts.append(f"nuova conferma tecnica sopra {fmt_price(asset, resistance)}")

        milestones = []
        first_confirmation = sol_fractal.get("first_confirmation")
        second_confirmation = sol_fractal.get("second_confirmation")

        if first_confirmation is not None:
            milestones.append(fmt_price(asset, first_confirmation))

        if second_confirmation is not None:
            milestones.append(fmt_price(asset, second_confirmation))

        if milestones:
            parts.append(
                "milestone analogiche "
                + " / ".join(milestones)
                + ", valide soltanto se rientra anche il gap frattale"
            )

        if parts:
            return "; ".join(parts) + "."

        return "Serve recupero delle resistenze tecniche e rientro del gap frattale."

    if asset == "DOGE":
        parts = []

        if resistance is not None:
            parts.append(f"sopra {fmt_price(asset, resistance)} migliora")

        if bearish_invalidation is not None:
            parts.append(
                f"sopra {fmt_price(asset, bearish_invalidation)} viene invalidato "
                "il pattern ribassista dominante"
            )

        if parts:
            return "; ".join(parts).capitalize() + "."

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
                "BTC è l'asset messo meglio nel breve, ma lo score statistico ora conta Scanner e Market Regime "
                "una sola volta. La struttura macro resta debole: ha più senso accumulare a tranche sui pullback "
                "che inseguire il prezzo vicino alle resistenze."
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
                "La conferma vera arriva solo sopra le resistenze tecniche e con rientro del gap frattale. "
                "Il modulo lifecycle/EMA200 resta utile come contesto, ma non aumenta il punteggio Global."
            )
        if score >= 0:
            return (
                "SOL è ancora in zona mista. Il frattale resta soltanto uno scenario contestuale: "
                "non è confermato dal prezzo e vale 0 punti operativi finché il gap non rientra. "
                "Meglio evitare leva e ragionare solo a tranche piccole."
            )
        return (
            "SOL è fragile nel breve. Il frattale da solo non basta: se non recupera le conferme e il gap "
            "non rientra, il rischio è di inseguire uno spike scaricato."
        )

    if asset == "DOGE":
        if score <= -4:
            return (
                "DOGE resta l'asset più debole. Anche senza contare due volte Scanner e Market Regime, "
                "la confluenza generale resta chiaramente negativa rispetto a BTC e SOL."
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
        "Famiglia statistica",
        "Scanner",
        "Market regime",
        "Scanner path",
        "Tecnico",
        "Classic technical",
        "Frattale SOL",
        "Fractal path",
        "RSI top-cycle",
        "Lifecycle EMA",
        "Exchange flow",
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
                fmt_signed_int(components[asset]["Market regime"]["score"]),
                fmt_signed_int(components[asset]["Famiglia statistica"]["score"]),
                fmt_signed_int(components[asset]["Scanner path"]["score"]),
                fmt_signed_int(components[asset]["Tecnico"]["score"]),
                fmt_signed_int(components[asset]["Classic technical"]["score"]),
                fmt_signed_int(components[asset]["Frattale SOL"]["score"]),
                fmt_signed_int(components[asset]["Fractal path"]["score"]),
                fmt_signed_int(components[asset]["RSI top-cycle"]["score"]),
                fmt_signed_int(components[asset]["Lifecycle EMA"]["score"]),
                fmt_signed_int(components[asset]["Exchange flow"]["score"]),
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
    lines.append("- Famiglia statistica Scanner + Market Regime, conteggiata una sola volta")
    lines.append("- Scanner path / cono previsionale")
    lines.append("- Struttura tecnica classica precedente")
    lines.append("- Classic technical confirmation, filtro tecnico completo")
    lines.append("- Frattale BTC 2022 vs SOL 2026, solo per SOL")
    lines.append("- Fractal path tracker, solo per SOL")
    lines.append("- RSI top-cycle, soprattutto per SOL")
    lines.append("- Major alt lifecycle squeeze / EMA200 weekly, solo per SOL")
    lines.append("- Exchange microstructure: OI, funding, taker flow, order book e liquidazioni campionate")
    lines.append("- Futures / liquidazioni precedente, mantenuto come diagnostica")
    lines.append("- Cambiamento giornaliero")
    lines.append("")
    lines.append(
        "Nota statistica: **Scanner e Market Regime non vengono più sommati come due prove indipendenti**. "
        "Lo Scanner è il punteggio principale; il Market Regime può aggiungere al massimo 1 punto di conferma "
        "con almeno 10 match. La famiglia statistica è limitata a ±4."
    )
    lines.append("")
    lines.append(
        "Nota importante: **Lifecycle EMA200 viene letto e mostrato, ma vale sempre 0 punti nel Global Confluence**. "
        "Serve come contesto, non come conferma operativa."
    )
    lines.append("")
    lines.append(
        "Nota Classic technical: **pesa massimo ±1** perché è un filtro di conferma "
        "e in parte si sovrappone alla struttura tecnica già esistente."
    )
    lines.append("")
    lines.append(
        "Nota exchange: **candidato massimo ±1, peso iniziale 0** e più conferme indipendenti. "
        "Order book, funding o una singola liquidazione non bastano da soli."
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
                "Scanner grezzo",
                "Market grezzo",
                "Famiglia statistica",
                "Scanner path",
                "Tecnico",
                "Classic tech",
                "Frattale SOL",
                "Fractal path",
                "RSI top-cycle",
                "Lifecycle EMA",
                "Exchange flow",
                "Futures",
                "Daily change",
                "Totale",
            ],
            score_rows,
        )
    )
    lines.append("")
    lines.append(
        "Le colonne **Scanner grezzo** e **Market grezzo** sono diagnostiche: nel totale entra soltanto "
        "la colonna **Famiglia statistica**."
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
            suffix = ""
            if component_name in {"Scanner", "Market regime"}:
                suffix = " (diagnostico, già incluso nella Famiglia statistica)"
            lines.append(
                f"- {component_name}{suffix}: **{fmt_signed_int(comp['score'])}** — {comp['detail']}"
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
        "Nota Classic technical: il modulo è utile per capire se il setup è confermato davvero, "
        "ma il suo peso resta prudente per evitare doppio conteggio con il modulo tecnico già presente."
    )
    lines.append("")
    lines.append(
        "Nota exchange: il modulo salva OI, funding, taker flow, order book e liquidazioni campionate. "
        "Il candidato è limitato a ±1; il peso Global resta 0 finché il gate storico a 7 giorni non matura."
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
        "statistical_family_score",
        "statistical_family_detail",
        "statistical_family_rule",
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
        "technical_source",
        "technical_pattern_score",
        "technical_dominant_bullish_pattern",
        "technical_dominant_bullish_status",
        "technical_bullish_neckline",
        "technical_dominant_bearish_pattern",
        "technical_dominant_bearish_status",
        "technical_bearish_invalidation",
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
        "sol_fractal_structural_similarity",
        "sol_fractal_live_adherence",
        "sol_fractal_live_error",
        "sol_fractal_current_gap",
        "sol_fractal_operational_weight",
        "sol_fractal_tracking",
        "sol_fractal_phase",
        "sol_fractal_risk",
        "fractal_path_score",
        "fractal_path_controls",
        "fractal_path_current_gap",
        "fractal_path_live_error",
        "rsi_score",
        "rsi_risk",
        "lifecycle_score_component",
        "lifecycle_raw_score",
        "lifecycle_bias",
        "lifecycle_ema200",
        "lifecycle_upside",
        "exchange_flow_score_component",
        "exchange_candidate_score_component",
        "exchange_global_activation_status",
        "exchange_count",
        "exchange_kucoin_available",
        "exchange_raw_score",
        "exchange_confidence",
        "exchange_bias",
        "exchange_data_coverage",
        "exchange_flow_score",
        "exchange_derivatives_score",
        "exchange_crowding_score",
        "exchange_technical_confirmation_score",
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
            "statistical_family_score": c["Famiglia statistica"]["score"],
            "statistical_family_detail": c["Famiglia statistica"]["detail"],
            "statistical_family_rule": c["Famiglia statistica"]["data"].get("rule"),
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
            "technical_source": c["Tecnico"]["data"].get("source"),
            "technical_pattern_score": c["Tecnico"]["data"].get("pattern_score"),
            "technical_dominant_bullish_pattern": c["Tecnico"]["data"].get("dominant_bullish_pattern"),
            "technical_dominant_bullish_status": c["Tecnico"]["data"].get("dominant_bullish_status"),
            "technical_bullish_neckline": c["Tecnico"]["data"].get("bullish_neckline"),
            "technical_dominant_bearish_pattern": c["Tecnico"]["data"].get("dominant_bearish_pattern"),
            "technical_dominant_bearish_status": c["Tecnico"]["data"].get("dominant_bearish_status"),
            "technical_bearish_invalidation": c["Tecnico"]["data"].get("bearish_invalidation"),
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
            "sol_fractal_structural_similarity": c["Frattale SOL"]["data"].get("structural_similarity"),
            "sol_fractal_live_adherence": c["Frattale SOL"]["data"].get("live_adherence"),
            "sol_fractal_live_error": c["Frattale SOL"]["data"].get("live_error"),
            "sol_fractal_current_gap": c["Frattale SOL"]["data"].get("current_gap"),
            "sol_fractal_operational_weight": c["Frattale SOL"]["data"].get("operational_weight"),
            "sol_fractal_tracking": c["Frattale SOL"]["data"].get("tracking"),
            "sol_fractal_phase": c["Frattale SOL"]["data"].get("phase"),
            "sol_fractal_risk": c["Frattale SOL"]["data"].get("risk"),
            "fractal_path_score": c["Fractal path"]["score"],
            "fractal_path_controls": c["Fractal path"]["data"].get("controls"),
            "fractal_path_current_gap": c["Fractal path"]["data"].get("current_gap"),
            "fractal_path_live_error": c["Fractal path"]["data"].get("live_error"),
            "rsi_score": c["RSI top-cycle"]["score"],
            "rsi_risk": c["RSI top-cycle"]["data"].get("risk"),
            "lifecycle_score_component": c["Lifecycle EMA"]["score"],
            "lifecycle_raw_score": c["Lifecycle EMA"]["data"].get("lifecycle_score"),
            "lifecycle_bias": c["Lifecycle EMA"]["data"].get("bias"),
            "lifecycle_ema200": c["Lifecycle EMA"]["data"].get("ema200"),
            "lifecycle_upside": c["Lifecycle EMA"]["data"].get("upside"),
            "exchange_flow_score_component": c["Exchange flow"]["score"],
            "exchange_candidate_score_component": c["Exchange flow"]["data"].get("candidate_score"),
            "exchange_global_activation_status": c["Exchange flow"]["data"].get("activation_status"),
            "exchange_count": c["Exchange flow"]["data"].get("exchange_count"),
            "exchange_kucoin_available": c["Exchange flow"]["data"].get("kucoin_available"),
            "exchange_raw_score": c["Exchange flow"]["data"].get("raw_score"),
            "exchange_confidence": c["Exchange flow"]["data"].get("confidence"),
            "exchange_bias": c["Exchange flow"]["data"].get("bias"),
            "exchange_data_coverage": c["Exchange flow"]["data"].get("data_coverage"),
            "exchange_flow_score": c["Exchange flow"]["data"].get("flow_score"),
            "exchange_derivatives_score": c["Exchange flow"]["data"].get("derivatives_score"),
            "exchange_crowding_score": c["Exchange flow"]["data"].get("crowding_score"),
            "exchange_technical_confirmation_score": c["Exchange flow"]["data"].get("technical_confirmation_score"),
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
