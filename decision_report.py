import csv
import re
from datetime import datetime, timezone
from pathlib import Path


REPORTS_DIR = Path("reports")

LATEST_REPORT_PATH = REPORTS_DIR / "latest_report.md"
REPORT_PATH = REPORTS_DIR / "decision_report.md"
METRICS_CSV_PATH = REPORTS_DIR / "decision_report_metrics.csv"

GLOBAL_CONFLUENCE_METRICS_PATH = REPORTS_DIR / "global_confluence_metrics.csv"
RISK_CALIBRATION_METRICS_PATH = REPORTS_DIR / "risk_calibration_metrics.csv"
MARKET_SNAPSHOT_CSV_PATH = REPORTS_DIR / "latest_market_snapshot.csv"

BTC_LONG_CONFIRMATION_PRICE = 67248.0

START_MARKER = "<!-- DECISION_REPORT_START -->"
END_MARKER = "<!-- DECISION_REPORT_END -->"

ASSETS = ["BTC", "SOL", "DOGE"]


def now_utc_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


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

    text = str(value).strip()
    text = text.replace("**", "")
    text = text.replace("`", "")
    text = text.replace("\xa0", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def parse_number(value, default=None):
    if value is None:
        return default

    text = str(value).strip()

    if not text or text.lower() in {"n/a", "nan", "none", "null", "-"}:
        return default

    match = re.search(r"[-+]?\d[\d\s.,]*", text)
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
    except (TypeError, ValueError):
        return default


def fmt_score(value) -> str:
    try:
        number = int(value)
    except (TypeError, ValueError):
        number = 0

    if number > 0:
        return f"+{number}"

    return str(number)


def fmt_btc_level(value: float) -> str:
    return f"{value:,.0f}".replace(",", ".")


def split_md_row(line: str):
    line = line.strip()

    if not line.startswith("|") or not line.endswith("|"):
        return None

    cells = [clean_cell(cell) for cell in line.strip("|").split("|")]

    if not cells:
        return None

    non_empty = [cell for cell in cells if cell.strip()]
    if non_empty and all(set(cell.replace(":", "").strip()) <= {"-"} for cell in non_empty):
        return None

    return cells


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


def replace_or_prepend_decision_block(latest_text: str, report_text: str) -> str:
    full_block = f"{START_MARKER}\n\n{report_text.rstrip()}\n\n{END_MARKER}"

    if START_MARKER in latest_text and END_MARKER in latest_text:
        pattern = re.compile(
            re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
            flags=re.DOTALL,
        )
        return pattern.sub(full_block, latest_text)

    return full_block + "\n\n" + latest_text.lstrip()


def read_csv_rows(path: Path):
    if not path.exists():
        return []

    try:
        with path.open("r", encoding="utf-8", newline="") as file:
            return list(csv.DictReader(file))
    except Exception:
        return []


def read_snapshot_prices():
    rows = read_csv_rows(MARKET_SNAPSHOT_CSV_PATH)
    prices = {}

    for row in rows:
        asset = clean_cell(row.get("asset") or row.get("Asset")).upper()
        if asset not in ASSETS:
            continue

        price = parse_number(
            row.get("price")
            or row.get("close")
            or row.get("current_price"),
            None,
        )

        if price is not None:
            prices[asset] = float(price)

    return prices


def empty_global_row(asset: str) -> dict:
    return {
        "asset": asset,
        "score": 0,
        "confluence": "",
        "bias": "",
        "reliability": "",
        "action": "",
        "confirmations": "",
        "invalidations": "",
        "scanner_score": 0,
        "market_score": 0,
        "technical_score_component": 0,
        "sol_fractal_score": 0,
        "fractal_path_score": 0,
        "rsi_score": 0,
        "lifecycle_score_component": 0,
        "lifecycle_raw_score": None,
        "lifecycle_ema200": None,
        "lifecycle_upside": None,
        "futures_score": 0,
        "daily_change_score": 0,
    }


def read_global_from_csv():
    rows = read_csv_rows(GLOBAL_CONFLUENCE_METRICS_PATH)
    output = {}

    for row in rows:
        asset = clean_cell(row.get("asset") or row.get("Asset")).upper()
        if asset not in ASSETS:
            continue

        score = parse_number(
            row.get("global_score")
            or row.get("score")
            or row.get("total_score")
            or row.get("Punteggio"),
            0,
        )

        item = empty_global_row(asset)
        item.update(
            {
                "score": int(score or 0),
                "confluence": clean_cell(row.get("confluence") or row.get("Confluenza")),
                "bias": clean_cell(row.get("bias") or row.get("Bias")),
                "reliability": clean_cell(
                    row.get("reliability") or row.get("AffidabilitÃ ")
                ),
                "action": clean_cell(row.get("action") or row.get("Azione coerente")),
                "confirmations": clean_cell(
                    row.get("confirmations") or row.get("Conferme")
                ),
                "invalidations": clean_cell(
                    row.get("invalidations") or row.get("Invalidazioni")
                ),
                "scanner_score": int(parse_number(row.get("scanner_score"), 0) or 0),
                "market_score": int(parse_number(row.get("market_score"), 0) or 0),
                "technical_score_component": int(
                    parse_number(row.get("technical_score_component"), 0) or 0
                ),
                "sol_fractal_score": int(
                    parse_number(row.get("sol_fractal_score"), 0) or 0
                ),
                "fractal_path_score": int(
                    parse_number(row.get("fractal_path_score"), 0) or 0
                ),
                "rsi_score": int(parse_number(row.get("rsi_score"), 0) or 0),
                "lifecycle_score_component": int(
                    parse_number(row.get("lifecycle_score_component"), 0) or 0
                ),
                "lifecycle_raw_score": parse_number(
                    row.get("lifecycle_raw_score"), None
                ),
                "lifecycle_ema200": parse_number(
                    row.get("lifecycle_ema200"), None
                ),
                "lifecycle_upside": parse_number(
                    row.get("lifecycle_upside"), None
                ),
                "futures_score": int(
                    parse_number(row.get("futures_score"), 0) or 0
                ),
                "daily_change_score": int(
                    parse_number(row.get("daily_change_score"), 0) or 0
                ),
            }
        )

        output[asset] = item

    return output


def read_global_from_latest(latest_text: str):
    block = extract_marker_block(latest_text, "GLOBAL_CONFLUENCE")
    output = {}

    if not block:
        return output

    in_summary = False

    for line in block.splitlines():
        stripped = line.strip()

        if stripped.startswith("## Sintesi operativa"):
            in_summary = True
            continue

        if in_summary and stripped.startswith("## "):
            break

        if not in_summary:
            continue

        cells = split_md_row(line)

        if not cells or len(cells) < 8:
            continue

        if cells[0] == "Asset":
            continue

        asset = clean_cell(cells[0]).upper()
        if asset not in ASSETS:
            continue

        item = empty_global_row(asset)
        item.update(
            {
                "score": int(parse_number(cells[1], 0) or 0),
                "confluence": cells[2],
                "bias": cells[3],
                "reliability": cells[4],
                "action": cells[5],
                "confirmations": cells[6],
                "invalidations": cells[7],
            }
        )
        output[asset] = item

    return output


def read_global_data(latest_text: str):
    """
    Il CSV strutturato Ã¨ la fonte principale.
    Il blocco Markdown viene usato soltanto per completare eventuali asset mancanti.
    """
    csv_data = read_global_from_csv()
    markdown_data = read_global_from_latest(latest_text)

    merged = {}

    for asset in ASSETS:
        if asset in csv_data:
            merged[asset] = csv_data[asset]
        elif asset in markdown_data:
            merged[asset] = markdown_data[asset]

    return merged


def read_risk_calibration():
    rows = read_csv_rows(RISK_CALIBRATION_METRICS_PATH)
    output = {}

    for row in rows:
        asset = clean_cell(row.get("asset") or row.get("Asset")).upper()
        if asset not in ASSETS:
            continue

        output[asset] = {
            "spot_risk": clean_cell(
                row.get("spot_risk")
                or row.get("Rischio spot")
                or row.get("risk_spot")
            ),
            "leverage_risk": clean_cell(
                row.get("leverage_risk")
                or row.get("Rischio leva")
                or row.get("risk_leverage")
            ),
            "note": clean_cell(row.get("note") or row.get("Nota leva")),
        }

    return output


def risk_from_global(asset: str, score: int, risk_data: dict) -> str:
    calibrated = risk_data.get(asset, {})
    leverage_risk = clean_cell(calibrated.get("leverage_risk"))

    if leverage_risk:
        return leverage_risk.upper()

    if asset == "BTC":
        if score >= 3:
            return "MEDIO"
        if score >= 0:
            return "MEDIO / ALTO"
        return "ALTO"

    if asset in {"SOL", "DOGE"}:
        return "MOLTO ALTO"

    return "MEDIO"


def direction_from_global(asset: str, score: int, global_row: dict) -> str:
    confluence = clean_cell(global_row.get("confluence")).upper()
    bias = clean_cell(global_row.get("bias")).upper()

    if asset == "BTC":
        if score >= 3:
            return "BULLISH"
        if score >= 0:
            return "NEUTRALE / COSTRUTTIVO"
        if score >= -3:
            return "LEGGERMENTE BEARISH"
        return "BEARISH"

    if asset == "SOL":
        if score >= 7:
            return "BULLISH"
        if score >= 3:
            return "NEUTRALE / COSTRUTTIVO"
        if score >= 0:
            return "NEUTRALE / INCERTO"
        if score >= -3:
            return "LEGGERMENTE BEARISH"
        return "BEARISH"

    if asset == "DOGE":
        if score >= 3:
            return "NEUTRALE / COSTRUTTIVO"
        if score >= 0:
            return "NEUTRALE / INCERTO"
        if score >= -3:
            return "LEGGERMENTE BEARISH"
        return "BEARISH"

    if "POSITIVA" in confluence or "COSTRUTTIVO" in bias:
        return "NEUTRALE / COSTRUTTIVO"

    if "NEGATIVA" in confluence or "RIBASSISTA" in bias:
        return "BEARISH"

    return "NEUTRALE / INCERTO"


def fallback_spot_action(asset: str, score: int) -> str:
    """
    Viene usato soltanto se Global Confluence non ha scritto l'azione.
    La regola normale Ã¨ copiare direttamente `action` dal Global.
    """
    if asset == "BTC":
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


def spot_action(asset: str, score: int, global_row: dict) -> str:
    """
    Allineamento definitivo:
    l'azione spot del Decision Report Ã¨ la stessa azione prodotta dal
    Global Confluence. Non viene piÃ¹ ricalcolata con una seconda mappatura.
    """
    global_action = clean_cell(global_row.get("action"))

    if global_action:
        return global_action

    return fallback_spot_action(asset, score)


def long_action(asset: str, score: int, risk: str, current_price=None) -> str:
    risk_upper = clean_cell(risk).upper()

    if asset == "BTC":
        price = parse_number(current_price, None)

        if price is None:
            return "NO LONG A LEVA / SNAPSHOT NON DISPONIBILE"

        if price < BTC_LONG_CONFIRMATION_PRICE:
            level = fmt_btc_level(BTC_LONG_CONFIRMATION_PRICE)
            return f"NO LONG A LEVA / ATTENDI SOPRA {level} $"

        if score >= 3 and "MOLTO ALTO" not in risk_upper:
            return "LONG PRUDENTE"

        return "NO LONG A LEVA"

    if asset == "SOL":
        if score >= 7 and risk_upper not in {"MOLTO ALTO", "ALTO"}:
            return "LONG SOLO SU CONFERMA"
        return "NO LONG A LEVA"

    if asset == "DOGE":
        return "NO LONG A LEVA"

    return "NO LONG A LEVA"


def short_action(asset: str, score: int) -> str:
    if asset in {"BTC", "SOL"}:
        if score <= -4:
            return "SHORT SOLO DOPO ROTTURA"
        return "NO SHORT"

    if asset == "DOGE":
        if score < 0:
            return "SHORT SOLO DOPO SPIKE"
        return "NO SHORT"

    return "NO SHORT"


def max_long(asset: str, score: int, long_signal: str, risk: str) -> str:
    risk_upper = clean_cell(risk).upper()

    if "NO LONG" in long_signal:
        return "nessuna"

    if asset == "BTC":
        if score >= 3 and "ALTO" not in risk_upper:
            return "max 2x isolated"
        return "nessuna"

    if asset == "SOL":
        if score >= 7 and risk_upper not in {"ALTO", "MOLTO ALTO"}:
            return "max 2x isolated"
        return "nessuna"

    return "nessuna"


def max_short(asset: str, short_signal: str) -> str:
    if short_signal == "NO SHORT":
        return "nessuna"

    if asset in {"BTC", "SOL", "DOGE"}:
        return "max 1x-2x isolated"

    return "nessuna"


def lifecycle_note(global_data: dict) -> str:
    sol = global_data.get("SOL", {})
    raw_score = sol.get("lifecycle_raw_score")
    ema200 = sol.get("lifecycle_ema200")
    upside = sol.get("lifecycle_upside")

    if raw_score is None and ema200 is None:
        return (
            "**Lifecycle EMA200** = resta come contesto per SOL, ma pesa 0 nel "
            "Global Confluence. Non autorizza leva e non aggiunge punti automatici."
        )

    parts = ["**Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0"]

    if raw_score is not None:
        parts.append(f"score interno {int(raw_score)}")

    if ema200 is not None:
        formatted_ema = f"{ema200:.2f}".replace(".", ",")
        parts.append(f"EMA200 circa {formatted_ema} $")

    if upside is not None:
        formatted_upside = f"{upside:+.2f}%".replace(".", ",")
        parts.append(f"upside verso EMA200 {formatted_upside}")

    return (
        "; ".join(parts)
        + ". Non autorizza leva e non aggiunge punti automatici."
    )


def build_decisions(global_data: dict, risk_data: dict):
    rows = []
    details = {}
    snapshot_prices = read_snapshot_prices()

    for asset in ASSETS:
        global_row = global_data.get(asset, empty_global_row(asset))
        score = int(parse_number(global_row.get("score"), 0) or 0)

        direction = direction_from_global(asset, score, global_row)
        risk = risk_from_global(asset, score, risk_data)

        # Copia diretta dal Global Confluence.
        spot = spot_action(asset, score, global_row)

        # Leva e short restano decisioni separate e piÃ¹ prudenti.
        long_signal = long_action(
            asset,
            score,
            risk,
            snapshot_prices.get(asset),
        )
        short_signal = short_action(asset, score)

        row = {
            "asset": asset,
            "score": score,
            "direction": direction,
            "spot": spot,
            "long": long_signal,
            "short": short_signal,
            "max_long": max_long(asset, score, long_signal, risk),
            "max_short": max_short(asset, short_signal),
            "risk": risk,
            "global_action": clean_cell(global_row.get("action")),
            "confluence": clean_cell(global_row.get("confluence")),
            "bias": clean_cell(global_row.get("bias")),
            "confirmations": clean_cell(global_row.get("confirmations")),
            "invalidations": clean_cell(global_row.get("invalidations")),
        }

        rows.append(row)
        details[asset] = row

    return rows, details


def md_table(headers, rows) -> str:
    output = []
    output.append("| " + " | ".join(headers) + " |")
    output.append("| " + " | ".join(["---"] * len(headers)) + " |")

    for row in rows:
        output.append("| " + " | ".join(str(value) for value in row) + " |")

    return "\n".join(output)


def build_report(decision_rows, details, global_data) -> str:
    generated = now_utc_str()

    table_rows = []

    for row in decision_rows:
        table_rows.append(
            [
                row["asset"],
                fmt_score(row["score"]),
                row["direction"],
                row["spot"],
                row["long"],
                row["short"],
                row["max_long"],
                row["max_short"],
                row["risk"],
            ]
        )

    lines = []

    lines.append("# Decisione operativa sintetica")
    lines.append("")
    lines.append(f"Generato: {generated}")
    lines.append("")
    lines.append("Report separato completo: [decision_report.md](decision_report.md)")
    lines.append("")
    lines.append(
        "Sintesi automatica dello scanner: l'azione spot viene copiata direttamente "
        "dal Global Confluence; long, short e rischio restano filtri separati e piÃ¹ prudenti."
    )
    lines.append("")
    lines.append(
        md_table(
            [
                "Asset",
                "Global",
                "Direzione",
                "Spot",
                "Long leva",
                "Short leva",
                "Max long",
                "Max short",
                "Rischio",
            ],
            table_rows,
        )
    )
    lines.append("")
    lines.append("## Lettura immediata")
    lines.append("")

    for asset in ASSETS:
        detail = details[asset]
        lines.append(
            f"- **{asset}**: Global = **{fmt_score(detail['score'])}**, "
            f"spot = **{detail['spot']}**, "
            f"long = **{detail['long']}**, "
            f"short = **{detail['short']}**, "
            f"rischio = **{detail['risk']}**."
        )

    lines.append("")
    lines.append("## Dettaglio logica")
    lines.append("")

    for asset in ASSETS:
        detail = details[asset]

        lines.append(f"### {asset}")
        lines.append("")
        lines.append(f"- Global Confluence: **{fmt_score(detail['score'])}**")
        lines.append(f"- Confluenza: **{detail['confluence'] or 'n/a'}**")
        lines.append(f"- Bias Global: **{detail['bias'] or 'n/a'}**")
        lines.append(f"- Direzione decisionale: **{detail['direction']}**")
        lines.append(f"- Azione spot dal Global: **{detail['spot']}**")
        lines.append(f"- Long leva: **{detail['long']}**")
        lines.append(f"- Short leva: **{detail['short']}**")
        lines.append(f"- Rischio: **{detail['risk']}**")

        if detail["confirmations"]:
            lines.append(f"- Conferme: {detail['confirmations']}")

        if detail["invalidations"]:
            lines.append(f"- Invalidazioni: {detail['invalidations']}")

        lines.append("")

    btc_level = fmt_btc_level(BTC_LONG_CONFIRMATION_PRICE)

    lines.append("## Nota semplice")
    lines.append("")
    lines.append(
        "- **Spot** = usa la stessa azione del Global Confluence, senza una seconda "
        "mappatura che possa produrre frasi diverse."
    )
    lines.append(
        "- **Zona alta storica** = zona dove non inseguire troppo; puÃ² essere zona "
        "da prendere profitto."
    )
    lines.append(
        "- **Zona bassa storica** = zona di rischio; con leva la liquidazione non "
        "dovrebbe stare lÃ¬ vicino."
    )
    lines.append(
        f"- **BTC leva** = nessun long a leva finchÃ© il prezzo snapshot non supera "
        f"**{btc_level} $**; sotto quella soglia resta solo l'azione spot indicata dal Global."
    )
    lines.append(f"- {lifecycle_note(global_data)}")
    lines.append(
        "- **NO LONG** non significa automaticamente **SHORT**. Lo short ha senso "
        "solo se il quadro Ã¨ bearish o se lo spike viene spesso scaricato."
    )
    lines.append(
        "- Per SOL, se il Global Ã¨ da **+3 in su**, la decisione non deve diventare "
        "bearish solo perchÃ© lo scanner grezzo a 30 giorni Ã¨ incerto."
    )
    lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def write_metrics_csv(decision_rows) -> None:
    METRICS_CSV_PATH.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "generated_utc",
        "asset",
        "global_score",
        "direction",
        "spot",
        "long",
        "short",
        "max_long",
        "max_short",
        "risk",
        "confluence",
        "bias",
        "global_action",
        "confirmations",
        "invalidations",
    ]

    generated = datetime.now(timezone.utc).isoformat()

    with METRICS_CSV_PATH.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for row in decision_rows:
            writer.writerow(
                {
                    "generated_utc": generated,
                    "asset": row["asset"],
                    "global_score": row["score"],
                    "direction": row["direction"],
                    "spot": row["spot"],
                    "long": row["long"],
                    "short": row["short"],
                    "max_long": row["max_long"],
                    "max_short": row["max_short"],
                    "risk": row["risk"],
                    "confluence": row["confluence"],
                    "bias": row["bias"],
                    "global_action": row["global_action"],
                    "confirmations": row["confirmations"],
                    "invalidations": row["invalidations"],
                }
            )


def main() -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    latest_text = read_text(LATEST_REPORT_PATH)
    global_data = read_global_data(latest_text)

    missing_assets = [asset for asset in ASSETS if asset not in global_data]

    if missing_assets:
        missing = ", ".join(missing_assets)
        raise RuntimeError(
            "Decision Report: dati Global Confluence mancanti per "
            f"{missing}. Esegui prima global_confluence_report.py."
        )

    risk_data = read_risk_calibration()

    decision_rows, details = build_decisions(global_data, risk_data)
    report_text = build_report(decision_rows, details, global_data)

    write_text(REPORT_PATH, report_text)
    write_metrics_csv(decision_rows)

    updated_latest = replace_or_prepend_decision_block(latest_text, report_text)
    write_text(LATEST_REPORT_PATH, updated_latest)

    print(f"Decision report scritto in: {REPORT_PATH}")
    print(f"Metriche Decision report scritte in: {METRICS_CSV_PATH}")
    print(f"Latest report aggiornato: {LATEST_REPORT_PATH}")

    for row in decision_rows:
        print(
            f"{row['asset']}: Global {fmt_score(row['score'])} | "
            f"{row['direction']} | Spot {row['spot']} | "
            f"Long {row['long']} | Short {row['short']}"
        )


if __name__ == "__main__":
    main()
