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


MOJIBAKE_REPLACEMENTS = {
    "\u00c3\u00a0": "\u00e0",
    "\u00c3\u00a8": "\u00e8",
    "\u00c3\u00a9": "\u00e9",
    "\u00c3\u00ac": "\u00ec",
    "\u00c3\u00b2": "\u00f2",
    "\u00c3\u00b9": "\u00f9",
    "\u00c3\u0080": "\u00c0",
    "\u00c3\u0088": "\u00c8",
    "\u00c3\u0089": "\u00c9",
    "\u00c3\u008c": "\u00cc",
    "\u00c3\u0092": "\u00d2",
    "\u00c3\u0099": "\u00d9",
    "\u00c2\u00b1": "\u00b1",
    "\u00e2\u0080\u0093": "\u2013",
    "\u00e2\u0080\u0094": "\u2014",
    "\u00e2\u0080\u0098": "\u2018",
    "\u00e2\u0080\u0099": "\u2019",
    "\u00e2\u0080\u009c": "\u201c",
    "\u00e2\u0080\u009d": "\u201d",
}


def repair_mojibake(value):
    if value is None:
        return value

    out = str(value)

    for broken, fixed in MOJIBAKE_REPLACEMENTS.items():
        out = out.replace(broken, fixed)

    return out


def now_utc_str():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def clean_cell(value) -> str:
    if value is None:
        return ""

    s = repair_mojibake(value)
    s = s.strip()
    s = s.replace("**", "")
    s = s.replace("`", "")
    s = s.replace("\xa0", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def parse_number(value, default=None):
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


def fmt_score(value):
    try:
        value = int(value)
    except Exception:
        value = 0

    if value > 0:
        return f"+{value}"

    return str(value)


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
        return pattern.sub(lambda _: full_block, latest_text)

    return full_block + "\n\n" + latest_text.lstrip()


def read_csv_rows(path: Path):
    if not path.exists():
        return []

    try:
        with path.open("r", encoding="utf-8", newline="") as f:
            return list(csv.DictReader(f))
    except Exception:
        return []


def read_snapshot_prices():
    rows = read_csv_rows(MARKET_SNAPSHOT_CSV_PATH)
    out = {}

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
            out[asset] = float(price)

    return out


def read_global_from_csv():
    rows = read_csv_rows(GLOBAL_CONFLUENCE_METRICS_PATH)
    out = {}

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

        out[asset] = {
            "asset": asset,
            "score": int(score or 0),
            "confluence": clean_cell(row.get("confluence") or row.get("Confluenza")),
            "bias": clean_cell(row.get("bias") or row.get("Bias")),
            "reliability": clean_cell(
                row.get("reliability")
                or row.get("Affidabilit\u00e0")
                or row.get("Affidabilita")
            ),
            "action": clean_cell(row.get("action") or row.get("Azione coerente")),
            "confirmations": clean_cell(row.get("confirmations") or row.get("Conferme")),
            "invalidations": clean_cell(row.get("invalidations") or row.get("Invalidazioni")),
            "scanner_score": int(parse_number(row.get("scanner_score"), 0) or 0),
            "market_score": int(parse_number(row.get("market_score"), 0) or 0),
            "statistical_family_score": int(
                parse_number(row.get("statistical_family_score"), 0) or 0
            ),
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
            "lifecycle_ema200": parse_number(row.get("lifecycle_ema200"), None),
            "lifecycle_upside": parse_number(row.get("lifecycle_upside"), None),
            "futures_score": int(parse_number(row.get("futures_score"), 0) or 0),
            "daily_change_score": int(
                parse_number(row.get("daily_change_score"), 0) or 0
            ),
        }

    return out


def read_global_from_latest(latest_text: str):
    block = extract_marker_block(latest_text, "GLOBAL_CONFLUENCE")
    out = {}

    if not block:
        return out

    in_summary = False

    for line in block.splitlines():
        if line.strip().startswith("## Sintesi operativa"):
            in_summary = True
            continue

        if in_summary and line.strip().startswith("## "):
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

        score = parse_number(cells[1], 0)

        out[asset] = {
            "asset": asset,
            "score": int(score or 0),
            "confluence": cells[2],
            "bias": cells[3],
            "reliability": cells[4],
            "action": cells[5],
            "confirmations": cells[6],
            "invalidations": cells[7],
            "scanner_score": 0,
            "market_score": 0,
            "statistical_family_score": 0,
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

    return out


def read_global_data(latest_text: str):
    data = read_global_from_csv()

    if data:
        return data

    return read_global_from_latest(latest_text)


def read_risk_calibration():
    rows = read_csv_rows(RISK_CALIBRATION_METRICS_PATH)
    out = {}

    for row in rows:
        asset = clean_cell(row.get("asset") or row.get("Asset")).upper()

        if asset not in ASSETS:
            continue

        out[asset] = {
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

    return out


def risk_from_global(asset: str, score: int, global_row: dict, risk_data: dict):
    csv_risk = risk_data.get(asset, {})
    leverage_risk = clean_cell(csv_risk.get("leverage_risk"))

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


def direction_from_global(asset: str, score: int, global_row: dict):
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


def fallback_spot_action(asset: str, score: int):
    if asset == "BTC":
        if score >= 7:
            return "COMPRA / ACCUMULA"
        if score >= 3:
            return "ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE"
        if score >= 0:
            return "HOLD / ACCUMULA SOLO SU PULLBACK"
        if score >= -3:
            return "RIDUCI RISCHIO / NON INSEGUIRE"
        return "STAI FUORI / VENDI PARZIALE"

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


def spot_action(asset: str, score: int, direction: str, global_row: dict):
    del direction

    global_action = clean_cell(global_row.get("action"))

    if global_action:
        return global_action.upper()

    return fallback_spot_action(asset, score)


def long_action(asset: str, score: int, direction: str, risk: str, current_price=None):
    del direction

    risk_u = clean_cell(risk).upper()

    if asset == "BTC":
        price = parse_number(current_price, None)

        if price is None:
            return "NO LONG A LEVA / SNAPSHOT NON DISPONIBILE"

        if price < BTC_LONG_CONFIRMATION_PRICE:
            return "NO LONG A LEVA / ATTENDI SOPRA 67.248 $"

        if score >= 3 and "MOLTO ALTO" not in risk_u:
            return "LONG PRUDENTE"

        return "NO LONG A LEVA"

    if asset == "SOL":
        if score >= 7 and risk_u not in {"MOLTO ALTO", "ALTO"}:
            return "LONG SOLO SU CONFERMA"
        return "NO LONG A LEVA"

    return "NO LONG A LEVA"


def short_action(asset: str, score: int, direction: str):
    del direction

    if asset == "BTC":
        if score <= -4:
            return "SHORT SOLO DOPO ROTTURA"
        return "NO SHORT"

    if asset == "SOL":
        if score <= -4:
            return "SHORT SOLO DOPO ROTTURA"
        return "NO SHORT"

    if asset == "DOGE":
        if score < 0:
            return "SHORT SOLO DOPO SPIKE"
        return "NO SHORT"

    return "NO SHORT"


def max_long(asset: str, score: int, long_signal: str, risk: str):
    risk_u = clean_cell(risk).upper()

    if "NO LONG" in long_signal:
        return "nessuna"

    if asset == "BTC":
        if score >= 3 and "ALTO" not in risk_u:
            return "max 2x isolated"
        return "nessuna"

    if asset == "SOL":
        if score >= 7 and risk_u not in {"ALTO", "MOLTO ALTO"}:
            return "max 2x isolated"
        return "nessuna"

    return "nessuna"


def max_short(asset: str, score: int, short_signal: str):
    del score

    if short_signal == "NO SHORT":
        return "nessuna"

    if asset in {"BTC", "SOL", "DOGE"}:
        return "max 1x-2x isolated"

    return "nessuna"


def lifecycle_note(global_data: dict):
    sol = global_data.get("SOL", {})
    raw_score = sol.get("lifecycle_raw_score")
    ema200 = sol.get("lifecycle_ema200")
    upside = sol.get("lifecycle_upside")

    if raw_score is None and ema200 is None:
        return (
            "**Lifecycle EMA200** = resta come contesto per SOL, ma ora pesa 0 "
            "nel Global Confluence. Non autorizza leva e non aggiunge punti automatici."
        )

    parts = ["**Lifecycle EMA200** = per SOL resta solo contesto, peso Global 0"]

    if raw_score is not None:
        parts.append(f"score interno {int(raw_score)}")

    if ema200 is not None:
        parts.append(f"EMA200 circa {ema200:.2f} $".replace(".", ","))

    if upside is not None:
        parts.append(
            f"upside verso EMA200 {upside:+.2f}%".replace(".", ",")
        )

    return (
        "; ".join(parts)
        + ". Non autorizza leva e non aggiunge punti automatici."
    )


def build_decisions(global_data: dict, risk_data: dict):
    rows = []
    details = {}
    snapshot_prices = read_snapshot_prices()

    for asset in ASSETS:
        g = global_data.get(asset, {})
        score = int(parse_number(g.get("score"), 0) or 0)

        direction = direction_from_global(asset, score, g)
        risk = risk_from_global(asset, score, g, risk_data)
        spot = spot_action(asset, score, direction, g)
        long_sig = long_action(
            asset,
            score,
            direction,
            risk,
            snapshot_prices.get(asset),
        )
        short_sig = short_action(asset, score, direction)
        max_l = max_long(asset, score, long_sig, risk)
        max_s = max_short(asset, score, short_sig)

        row = {
            "asset": asset,
            "score": score,
            "direction": direction,
            "spot": spot,
            "long": long_sig,
            "short": short_sig,
            "max_long": max_l,
            "max_short": max_s,
            "risk": risk,
            "global_action": g.get("action", ""),
            "confluence": g.get("confluence", ""),
            "bias": g.get("bias", ""),
            "confirmations": g.get("confirmations", ""),
            "invalidations": g.get("invalidations", ""),
        }

        rows.append(row)
        details[asset] = row

    return rows, details


def md_table(headers, rows):
    out = []
    out.append("| " + " | ".join(headers) + " |")
    out.append("| " + " | ".join(["---"] * len(headers)) + " |")

    for row in rows:
        out.append("| " + " | ".join(str(x) for x in row) + " |")

    return "\n".join(out)


def build_report(decision_rows, details, global_data):
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
        "dal Global Confluence; long, short e rischio restano filtri separati e "
        "pi\u00f9 prudenti."
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
        d = details[asset]
        lines.append(
            f"- **{asset}**: Global = **{fmt_score(d['score'])}**, "
            f"spot = **{d['spot']}**, "
            f"long = **{d['long']}**, "
            f"short = **{d['short']}**, "
            f"rischio = **{d['risk']}**."
        )

    lines.append("")
    lines.append("## Dettaglio logica")
    lines.append("")

    for asset in ASSETS:
        d = details[asset]
        lines.append(f"### {asset}")
        lines.append("")
        lines.append(f"- Global Confluence: **{fmt_score(d['score'])}**")
        lines.append(f"- Confluenza: **{d['confluence'] or 'n/a'}**")
        lines.append(f"- Bias Global: **{d['bias'] or 'n/a'}**")
        lines.append(f"- Direzione decisionale: **{d['direction']}**")
        lines.append(f"- Azione spot dal Global: **{d['spot']}**")
        lines.append(f"- Long leva: **{d['long']}**")
        lines.append(f"- Short leva: **{d['short']}**")
        lines.append(f"- Rischio: **{d['risk']}**")

        if d["confirmations"]:
            lines.append(f"- Conferme: {d['confirmations']}")

        if d["invalidations"]:
            lines.append(f"- Invalidazioni: {d['invalidations']}")

        lines.append("")

    lines.append("## Nota semplice")
    lines.append("")
    lines.append(
        "- **Spot** = usa la stessa azione del Global Confluence, senza una "
        "seconda mappatura che possa produrre frasi diverse."
    )
    lines.append(
        "- **Zona alta storica** = zona dove non inseguire troppo; "
        "pu\u00f2 essere zona da prendere profitto."
    )
    lines.append(
        "- **Zona bassa storica** = zona di rischio; con leva la liquidazione "
        "non dovrebbe stare l\u00ec vicino."
    )
    lines.append(
        "- **BTC leva** = nessun long a leva finch\u00e9 il prezzo snapshot non "
        "supera **67.248 $**; sotto quella soglia resta solo l'azione spot "
        "indicata dal Global."
    )
    lines.append(f"- {lifecycle_note(global_data)}")
    lines.append(
        "- **NO LONG** non significa automaticamente **SHORT**. Lo short ha "
        "senso solo se il quadro \u00e8 bearish o se lo spike viene spesso scaricato."
    )
    lines.append(
        "- Per SOL, se il Global \u00e8 da **+3 in su**, la decisione non deve "
        "diventare bearish solo perch\u00e9 lo scanner grezzo a 30 giorni \u00e8 incerto."
    )
    lines.append("")

    report = "\n".join(lines).rstrip() + "\n"
    return repair_mojibake(report)


def write_metrics_csv(decision_rows):
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

    with METRICS_CSV_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
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


def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    latest_text = read_text(LATEST_REPORT_PATH)
    global_data = read_global_data(latest_text)

    if not global_data:
        raise RuntimeError(
            "Decision Report: impossibile leggere Global Confluence. "
            "Esegui prima global_confluence_report.py."
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
