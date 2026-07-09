import os
import re
from datetime import datetime, timezone

import numpy as np
import pandas as pd
from tabulate import tabulate


REPORT_DIR = "reports"
MAIN_REPORT_PATH = os.path.join(REPORT_DIR, "latest_report.md")
REPORT_PATH = os.path.join(REPORT_DIR, "global_confluence_report.md")
CSV_PATH = os.path.join(REPORT_DIR, "global_confluence_metrics.csv")

START_MARKER = "<!-- GLOBAL_CONFLUENCE_START -->"
END_MARKER = "<!-- GLOBAL_CONFLUENCE_END -->"

ASSETS = ["BTC", "SOL", "DOGE"]

SECTION_MARKERS = {
    "daily_change": ("<!-- DAILY_CHANGE_START -->", "<!-- DAILY_CHANGE_END -->"),
    "scanner_forecast": ("<!-- SCANNER_FORECAST_TRACKER_START -->", "<!-- SCANNER_FORECAST_TRACKER_END -->"),
    "btc_sol_fractal": ("<!-- BTC_SOL_FRACTAL_START -->", "<!-- BTC_SOL_FRACTAL_END -->"),
    "rsi_top_cycle": ("<!-- RSI_TOP_CYCLE_START -->", "<!-- RSI_TOP_CYCLE_END -->"),
    "lifecycle": ("<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_START -->", "<!-- MAJOR_ALT_LIFECYCLE_SQUEEZE_END -->"),
    "liquidations": ("<!-- LIQUIDATION_SUMMARY_START -->", "<!-- LIQUIDATION_SUMMARY_END -->"),
    "fractal_path": ("<!-- FRACTAL_PATH_TRACKER_START -->", "<!-- FRACTAL_PATH_TRACKER_END -->"),
    "market_regime": ("<!-- MARKET_REGIME_MATCH_START -->", "<!-- MARKET_REGIME_MATCH_END -->"),
    "technical": ("<!-- TECHNICAL_STRUCTURE_START -->", "<!-- TECHNICAL_STRUCTURE_END -->"),
}


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

            s = re.sub(r"[^0-9.\-]", "", s)

            if not s or s in ["-", ".", "-."]:
                return default

            return float(s)

        if pd.isna(v):
            return default

        return float(v)

    except Exception:
        return default


def fmt_pct(v, decimals=2, signed=False):
    v = safe_float(v)

    if pd.isna(v):
        return "n/a"

    sign = "+" if signed and v > 0 else ""
    return f"{sign}{v:.{decimals}f}%".replace(".", ",")


def fmt_score(v):
    try:
        v = int(v)
    except Exception:
        return "0"

    if v > 0:
        return f"+{v}"

    return str(v)


def fmt_price_level(v, decimals=2):
    v = safe_float(v)

    if pd.isna(v):
        return "n/a"

    if abs(v) >= 1000:
        s = f"{v:,.0f}".replace(",", ".")
        return s

    if abs(v) >= 1:
        return f"{v:.2f}".replace(".", ",")

    return f"{v:.5f}"


def section(text, name):
    start, end = SECTION_MARKERS[name]

    if start in text and end in text:
        s = text.index(start)
        e = text.index(end) + len(end)
        return text[s:e]

    return ""


def clean_cell(cell):
    cell = str(cell).strip()
    cell = cell.replace("**", "")
    cell = cell.replace("`", "")
    cell = cell.replace("<br>", " ")
    cell = re.sub(r"\s+", " ", cell)
    return cell.strip()


def parse_markdown_table_rows(text):
    rows = []

    for line in text.splitlines():
        if "|" not in line:
            continue

        stripped = line.strip()

        if not stripped.startswith("|") and "|" not in stripped:
            continue

        cells = [clean_cell(c) for c in stripped.strip("|").split("|")]

        if len(cells) < 2:
            continue

        joined = "".join(cells).replace(":", "").replace("-", "").strip()
        if not joined:
            continue

        # Salta righe separatore tipo | --- | --- |
        if all(re.fullmatch(r":?-{2,}:?", c.replace(" ", "")) for c in cells if c):
            continue

        rows.append(cells)

    return rows


def find_table_row(text, first_cell):
    target = first_cell.strip().upper()

    for cells in parse_markdown_table_rows(text):
        if not cells:
            continue

        if clean_cell(cells[0]).upper() == target:
            return cells

    return None


def find_row_containing(text, contains):
    contains = contains.upper()

    for cells in parse_markdown_table_rows(text):
        if cells and contains in clean_cell(cells[0]).upper():
            return cells

    return None


def extract_first(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
    m = re.search(pattern, text, flags)

    if not m:
        return None

    return clean_cell(m.group(1))


def component_scanner(asset, full_text):
    asset_title = {
        "BTC": "Bitcoin",
        "SOL": "Solana",
        "DOGE": "Dogecoin",
    }[asset]

    pattern = rf"# {asset_title} — mappa semplice.*?(?=\n---|\n# Come leggere|\n# Approfondimento|\Z)"
    m = re.search(pattern, full_text, re.IGNORECASE | re.DOTALL)

    block = m.group(0) if m else full_text

    positive_raw = extract_first(r"Probabilità storica di salita:\s*\*?\*?([+\-]?[0-9]+[,.]?[0-9]*)%?", block)
    direction = extract_first(r"Direzione più probabile a 30 giorni:\s*\*?\*?([A-ZÀ-Ú /]+)", block)
    p50_return = extract_first(r"Return normale fra 30 giorni:\s*\*?\*?[^()]*$begin:math:text$\(\[\+\\\-\]\?\[0\-9\]\+\[\,\.\]\?\[0\-9\]\*\)\%$end:math:text$", block)

    positive = safe_float(positive_raw)
    p50 = safe_float(p50_return)

    if pd.isna(positive):
        return 0, "Dati scanner non trovati."

    if positive >= 65 and p50 > 0:
        score = 3
    elif positive >= 55 and p50 > 0:
        score = 2
    elif positive >= 50:
        score = 1
    elif positive >= 40:
        score = -1
    elif positive >= 25:
        score = -2
    else:
        score = -3

    direction_text = direction if direction else "n/a"

    return score, f"Casi positivi {positive:.2f}%, return centrale 30g {fmt_pct(p50, signed=True)}. Direzione scanner: {direction_text}."


def component_scanner_path(asset, full_text):
    sec = section(full_text, "scanner_forecast")
    row = find_table_row(sec, asset)

    if not row:
        return 0, "Scanner path non disponibile."

    # Tabella accuratezza percorso:
    # Asset | Giorno | Controlli | Dentro p10-p90 | Dentro p25-p75 | ...
    rows = parse_markdown_table_rows(sec)
    controls = 0

    for cells in rows:
        if len(cells) >= 3 and cells[0].upper() == asset and cells[1].lower() == "1g":
            controls = int(safe_float(cells[2], 0))
            break

    if controls < 5:
        return 0, f"Raccolta dati. Controlli disponibili {controls}. Servono almeno 5 controlli prima di pesare il cono previsionale."

    return 0, f"Scanner path attivo con {controls} controlli, ma peso ancora neutro."


def component_market_regime(asset, full_text):
    sec = section(full_text, "market_regime")
    target = f"{asset}-USD"

    rows = parse_markdown_table_rows(sec)

    chosen = None

    for cells in rows:
        if len(cells) >= 6 and cells[0].upper() == target and cells[1] == "SAME_BTC_AND_ASSET_REGIME":
            chosen = cells
            break

    if not chosen:
        return 0, "Market regime non disponibile."

    matches = int(safe_float(chosen[2], 0))
    positive_30d = safe_float(chosen[3])
    p50 = safe_float(chosen[4])

    if matches < 5:
        return 0, f"Gruppo SAME_BTC_AND_ASSET_REGIME con pochi match ({matches}), non pesato."

    if positive_30d >= 80 and p50 > 5:
        score = 3
    elif positive_30d >= 60:
        score = 2
    elif positive_30d >= 52:
        score = 1
    elif positive_30d <= 20:
        score = -3
    elif positive_30d <= 40:
        score = -2
    else:
        score = 0

    return score, f"Gruppo SAME_BTC_AND_ASSET_REGIME, match {matches}, positivi 30g {fmt_pct(positive_30d)}, return p50 {fmt_pct(p50, signed=True)}."


def component_technical(asset, full_text):
    sec = section(full_text, "technical")
    row = find_table_row(sec, asset)

    if not row or len(row) < 10:
        return 0, "Struttura tecnica non disponibile."

    raw_score = int(safe_float(row[2], 0))
    verdict = row[3].lower()
    trend = row[4].lower()
    structure = row[6].lower()
    divergence = row[7].lower()
    wyckoff = row[8].lower()

    if raw_score >= 7:
        score = 3
    elif raw_score >= 3:
        score = 2
    elif raw_score >= 1:
        score = 1
    elif raw_score >= -2:
        score = 0
    elif raw_score >= -6:
        score = -2
    else:
        score = -3

    return score, f"Score tecnico {raw_score}/12, verdetto {verdict}, trend {trend}, struttura {structure}, divergenza {divergence}, Wyckoff {wyckoff}."


def component_sol_fractal(asset, full_text):
    if asset != "SOL":
        return 0, "Non applicabile a questo asset."

    sec = section(full_text, "btc_sol_fractal")

    verdict = extract_first(r"##\s*Verdetto:\s*([^\n]+)", sec) or "n/a"
    similarity = safe_float(extract_first(r"Somiglianza totale:\s*\+?([0-9]+[,.]?[0-9]*)", sec))
    tracking = extract_first(r"Trend tracking:\s*([^\n]+)", sec) or "n/a"
    phase = extract_first(r"Fase attuale:\s*([^\n]+)", sec) or "n/a"
    risk = extract_first(r"Rischio fase:\s*([^\n]+)", sec) or "n/a"

    verdict_u = verdict.upper()
    tracking_u = tracking.upper()

    if "SI FORTE" in verdict_u or ("PARZIALMENTE" in verdict_u and similarity >= 75):
        score = 3
    elif "PARZIALMENTE" in verdict_u and similarity >= 70:
        score = 2
    elif "PARZIALMENTE" in verdict_u:
        score = 1
    elif "NO" in verdict_u or "ROTTO" in tracking_u:
        score = -2
    else:
        score = 0

    return score, f"Verdetto {verdict}, somiglianza {fmt_pct(similarity, signed=True)}, tracking {tracking}, fase {phase}, rischio {risk}."


def component_fractal_path(asset, full_text):
    if asset != "SOL":
        return 0, "Non applicabile a questo asset."

    sec = section(full_text, "fractal_path")

    rows = parse_markdown_table_rows(sec)

    controls_total = 0

    for cells in rows:
        if len(cells) >= 2:
            first = cells[0].lower()
            if re.fullmatch(r"\d+g", first):
                controls_total += int(safe_float(cells[1], 0))

    if controls_total < 5:
        return 0, "Tracking operativo, ma nessuna milestone settimanale ancora verificata. Il modulo non pesa finché non maturano abbastanza controlli."

    return 0, f"Tracking operativo con {controls_total} controlli verificati. Peso ancora neutro finché non ci sono almeno 30+ controlli."


def component_rsi_top_cycle(asset, full_text):
    if asset != "SOL":
        return 0, "Non applicabile a questo asset."

    sec = section(full_text, "rsi_top_cycle")

    risk = extract_first(r"Rischio top-cycle RSI\s*\|\s*([^|]+)\|", sec)
    if not risk:
        risk = extract_first(r"Rischio top-cycle RSI.*?\|\s*([A-ZÀ-Ú /]+)\s*\|", sec)

    if not risk:
        risk = extract_first(r"Rischio top-cycle RSI.*?([A-ZÀ-Ú /]+)", sec) or "n/a"

    risk_u = risk.upper()

    if "BASSO" in risk_u:
        return 1, "Rischio top-cycle RSI: BASSO."

    if "ALTO" in risk_u:
        return -2, f"Rischio top-cycle RSI: {risk}."

    return 0, f"Rischio top-cycle RSI: {risk}."


def component_lifecycle(asset, full_text):
    if asset != "SOL":
        return 0, "Non applicabile a questo asset."

    sec = section(full_text, "lifecycle")

    lifecycle_score = safe_float(extract_first(r"Lifecycle squeeze score\s*\|\s*([0-9]+)", sec), 0)
    bias = extract_first(r"Bias\s*\|\s*([^|]+)", sec) or "n/a"
    action = extract_first(r"Azione coerente\s*\|\s*([^|]+)", sec) or "n/a"
    ema200 = extract_first(r"EMA200 weekly target\s*\|\s*([^|]+)", sec) or "n/a"
    upside = extract_first(r"Upside verso EMA200\s*\|\s*([^|]+)", sec) or "n/a"
    gap = extract_first(r"Gap EMA50/EMA200\s*\|\s*([^|]+)", sec) or "n/a"
    hit = extract_first(r"Hit EMA200 12w analoghi\s*\|\s*([^|]+)", sec) or "n/a"
    trend = extract_first(r"Trend squeeze\s*\|\s*([^|]+)", sec) or "n/a"

    # Scelta definitiva:
    # Lifecycle / EMA200 resta come contesto, ma NON pesa nel Global Confluence.
    score = 0

    detail = (
        f"Contesto non pesato nel Global. Lifecycle score {int(lifecycle_score)}, "
        f"bias {bias}, EMA200 {ema200}, upside EMA200 {upside}, "
        f"gap EMA50/EMA200 {gap}, hit EMA200 12w {hit}, trend {trend}. "
        f"Peso Global forzato a 0."
    )

    return score, detail


def component_futures(asset, full_text):
    sec = section(full_text, "liquidations")
    row = find_table_row(sec, asset)

    if not row or len(row) < 6:
        return 0, "Futures non disponibili."

    reading = row[5] if len(row) > 5 else "n/a"
    strength = row[6] if len(row) > 6 else "n/a"

    return 0, f"Lettura futures {reading}, forza {strength}."


def component_daily_change(asset, full_text):
    sec = section(full_text, "daily_change")
    row = find_table_row(sec, asset)

    if not row or len(row) < 4:
        return 0, "Cambiamento giornaliero non disponibile."

    change = row[1]
    tone = row[2]

    change_u = change.upper()
    tone_u = tone.upper()

    if "NESSUN" in change_u:
        score = 0
    elif "MIGLIOR" in tone_u:
        score = 1
    elif "PEGGIOR" in tone_u:
        score = -1
    else:
        score = 0

    return score, f"{asset}: {change.lower()} in {tone.lower()} rispetto a ieri."


def confluence_label(score):
    if score >= 7:
        return "POSITIVA FORTE"
    if score >= 3:
        return "MODERATAMENTE POSITIVA"
    if score >= 0:
        return "PARZIALE / MISTA"
    if score >= -3:
        return "DEBOLE / FRAGILE"
    return "NEGATIVA"


def bias_label(score):
    if score >= 7:
        return "Rialzista"
    if score >= 3:
        return "Costruttivo prudente"
    if score >= 0:
        return "Misto / da confermare"
    if score >= -3:
        return "Debole"
    return "Ribassista"


def reliability_label(score):
    if abs(score) >= 8:
        return "MEDIA / ALTA"
    if abs(score) >= 3:
        return "MEDIA"
    return "BASSA / MEDIA"


def coherent_action(asset, score):
    if asset == "BTC":
        if score >= 3:
            return "ACCUMULA SU PULLBACK / NO SHORT"
        if score >= 0:
            return "HOLD / NO LEVA"
        return "RIDUCI RISCHIO / NO LONG A LEVA"

    if asset == "SOL":
        if score >= 7:
            return "HOLD / ACCUMULA SOLO SU CONFERME, LEVA PRUDENTE"
        if score >= 3:
            return "HOLD / TRANCHE PICCOLE, NO LEVA"
        if score >= 0:
            return "HOLD LEGGERO / ASPETTA CONFERME"
        return "STAI FUORI / NO LEVA"

    if asset == "DOGE":
        if score <= -4:
            return "STAI FUORI / VENDI PARZIALE; SHORT SOLO DOPO SPIKE"
        if score < 0:
            return "STAI FUORI / NO LONG"
        return "SOLO TRADING VELOCE, NO ACCUMULO"

    return "n/a"


def parse_technical_support_resistance(asset, full_text):
    sec = section(full_text, "technical")
    row = find_table_row(sec, asset)

    if not row or len(row) < 11:
        return np.nan, np.nan

    support = safe_float(row[-2])
    resistance = safe_float(row[-1])

    return support, resistance


def parse_fractal_level(sec, label):
    rows = parse_markdown_table_rows(sec)

    for cells in rows:
        if len(cells) >= 2 and label.lower() in cells[0].lower():
            return safe_float(cells[1])

    return np.nan


def confirmations_invalidations(asset, full_text):
    if asset == "BTC":
        support, resistance = parse_technical_support_resistance(asset, full_text)
        return (
            f"Sopra {fmt_price_level(resistance)} migliora; sopra la neckline tecnica successiva il recupero diventa più credibile.",
            f"Sotto {fmt_price_level(support)} il quadro tecnico peggiora.",
        )

    if asset == "DOGE":
        support, resistance = parse_technical_support_resistance(asset, full_text)
        return (
            f"Sopra {fmt_price_level(resistance)} migliora, ma resta asset debole finché scanner e struttura non girano.",
            f"Sotto {fmt_price_level(support)} il rischio ribassista aumenta.",
        )

    if asset == "SOL":
        tech_support, tech_resistance = parse_technical_support_resistance(asset, full_text)
        sec = section(full_text, "btc_sol_fractal")

        first_conf = parse_fractal_level(sec, "Prima conferma")
        second_conf = parse_fractal_level(sec, "Seconda conferma")
        soft_inv = parse_fractal_level(sec, "Invalidazione soft")
        strong_inv = parse_fractal_level(sec, "Invalidazione forte")

        confirmations = [
            fmt_price_level(tech_resistance),
            fmt_price_level(first_conf),
            fmt_price_level(second_conf),
        ]

        invalidations = [
            fmt_price_level(soft_inv),
            fmt_price_level(tech_support),
            fmt_price_level(strong_inv),
        ]

        return (
            "Conferme sopra " + " / ".join(confirmations) + ".",
            "Allarmi sotto " + " / ".join(invalidations) + ".",
        )

    return "n/a", "n/a"


def asset_intro(asset):
    if asset == "BTC":
        return (
            "BTC è l'asset messo meglio nel breve. La struttura macro non è ancora pienamente rialzista, "
            "ma scanner, regime e segnali tecnici interni sono abbastanza coerenti per un recupero prudente."
        )

    if asset == "SOL":
        return (
            "SOL ha una confluenza costruttiva, ma va ancora trattato come setup anticipato. "
            "La conferma vera arriva solo sopra le resistenze tecniche e frattali. "
            "Il modulo lifecycle/EMA200 resta utile come contesto, ma non viene più usato per aumentare il punteggio Global."
        )

    if asset == "DOGE":
        return (
            "DOGE resta l'asset più debole. Anche se può fare rimbalzi o spike, "
            "la confluenza generale resta negativa rispetto a BTC e SOL."
        )

    return ""


def compute_asset(asset, full_text):
    components = {}

    components["Scanner"] = component_scanner(asset, full_text)
    components["Scanner path"] = component_scanner_path(asset, full_text)
    components["Market regime"] = component_market_regime(asset, full_text)
    components["Tecnico"] = component_technical(asset, full_text)
    components["Frattale SOL"] = component_sol_fractal(asset, full_text)
    components["Fractal path"] = component_fractal_path(asset, full_text)
    components["RSI top-cycle"] = component_rsi_top_cycle(asset, full_text)
    components["Lifecycle EMA"] = component_lifecycle(asset, full_text)
    components["Futures"] = component_futures(asset, full_text)
    components["Daily change"] = component_daily_change(asset, full_text)

    total = int(sum(v[0] for v in components.values()))

    confirmations, invalidations = confirmations_invalidations(asset, full_text)

    return {
        "asset": asset,
        "components": components,
        "total": total,
        "confluence": confluence_label(total),
        "bias": bias_label(total),
        "reliability": reliability_label(total),
        "action": coherent_action(asset, total),
        "confirmations": confirmations,
        "invalidations": invalidations,
    }


def df_to_markdown(df):
    if df is None or df.empty:
        return "_Nessun dato disponibile._"

    return tabulate(df, headers="keys", tablefmt="pipe", showindex=False)


def build_report(results):
    generated = now_utc().strftime("%Y-%m-%d %H:%M UTC")

    summary_rows = []
    score_rows = []
    detail_sections = []

    for res in results:
        asset = res["asset"]
        c = res["components"]

        summary_rows.append({
            "Asset": asset,
            "Punteggio": res["total"],
            "Confluenza": res["confluence"],
            "Bias": res["bias"],
            "Affidabilità": res["reliability"],
            "Azione coerente": res["action"],
            "Conferme": res["confirmations"],
            "Invalidazioni": res["invalidations"],
        })

        score_rows.append({
            "Asset": asset,
            "Scanner": fmt_score(c["Scanner"][0]),
            "Scanner path": fmt_score(c["Scanner path"][0]),
            "Market regime": fmt_score(c["Market regime"][0]),
            "Tecnico": fmt_score(c["Tecnico"][0]),
            "Frattale SOL": fmt_score(c["Frattale SOL"][0]),
            "Fractal path": fmt_score(c["Fractal path"][0]),
            "RSI top-cycle": fmt_score(c["RSI top-cycle"][0]),
            "Lifecycle EMA": fmt_score(c["Lifecycle EMA"][0]),
            "Futures": fmt_score(c["Futures"][0]),
            "Daily change": fmt_score(c["Daily change"][0]),
            "Totale": fmt_score(res["total"]),
        })

        detail_lines = []

        detail_lines.append(f"### {asset}\n")
        detail_lines.append(f"- Confluenza: **{res['confluence']}**")
        detail_lines.append(f"- Bias: **{res['bias']}**")
        detail_lines.append(f"- Punteggio finale: **{fmt_score(res['total'])}**")
        detail_lines.append(f"- Affidabilità: **{res['reliability']}**")
        detail_lines.append(f"- Azione coerente: **{res['action']}**\n")
        detail_lines.append(asset_intro(asset) + "\n")
        detail_lines.append("Dettaglio moduli:\n")

        for name, (score, desc) in c.items():
            detail_lines.append(f"- {name}: **{fmt_score(score)}** — {desc}")

        detail_lines.append("")
        detail_lines.append(f"Conferme: {res['confirmations']}")
        detail_lines.append("")
        detail_lines.append(f"Invalidazioni: {res['invalidations']}")
        detail_lines.append("")

        detail_sections.append("\n".join(detail_lines))

    summary_df = pd.DataFrame(summary_rows)
    score_df = pd.DataFrame(score_rows)

    report = f"""{START_MARKER}
# Sintesi finale di confluenza

Generato: {generated}

Questo report mette insieme i moduli principali dello scanner e controlla se si confermano o si contraddicono.

Moduli letti:

- Scanner frattale/statistico a 30 giorni
- Scanner path / cono previsionale
- Market regime match
- Struttura tecnica classica
- Frattale BTC 2022 vs SOL 2026, solo per SOL
- Fractal path tracker, solo per SOL
- RSI top-cycle, soprattutto per SOL
- Major alt lifecycle squeeze / EMA200 weekly, solo per SOL
- Futures / liquidazioni
- Cambiamento giornaliero

Nota importante: **Lifecycle EMA200 viene letto e mostrato, ma ora vale sempre 0 punti nel Global Confluence**. Serve come contesto, non come conferma operativa.

## Sintesi operativa

{df_to_markdown(summary_df)}

## Punteggi per modulo

{df_to_markdown(score_df)}

## Lettura asset per asset

{chr(10).join(detail_sections)}

## Come leggere il punteggio

- +7 o più: confluenza positiva forte.
- Da +3 a +6: confluenza moderatamente positiva.
- Da 0 a +2: confluenza parziale o mista.
- Da -1 a -3: confluenza debole o fragile.
- -4 o meno: confluenza negativa.

Nota: Scanner path e Fractal path sono già integrati, ma finché hanno pochi controlli restano quasi sempre a punteggio 0.
Servono almeno 5 controlli prima di influire leggermente, e 30+ controlli prima di pesare davvero.

Nota lifecycle EMA200: il modulo Major alt lifecycle squeeze resta nel report, ma pesa **0** nel Global perché EMA50/EMA200 e target EMA200 sono contesto, non conferme dirette di prezzo.
{END_MARKER}
"""
    return report, summary_df, score_df


def save_metrics(results):
    rows = []

    for res in results:
        c = res["components"]

        row = {
            "asset": res["asset"],
            "Asset": res["asset"],
            "total_score": res["total"],
            "Punteggio": res["total"],
            "confluence": res["confluence"],
            "Confluenza": res["confluence"],
            "bias": res["bias"],
            "Bias": res["bias"],
            "reliability": res["reliability"],
            "Affidabilità": res["reliability"],
            "action": res["action"],
            "Azione coerente": res["action"],
            "confirmations": res["confirmations"],
            "Conferme": res["confirmations"],
            "invalidations": res["invalidations"],
            "Invalidazioni": res["invalidations"],
            "scanner_score": c["Scanner"][0],
            "scanner_path_score": c["Scanner path"][0],
            "market_regime_score": c["Market regime"][0],
            "technical_score": c["Tecnico"][0],
            "sol_fractal_score": c["Frattale SOL"][0],
            "fractal_path_score": c["Fractal path"][0],
            "rsi_top_cycle_score": c["RSI top-cycle"][0],
            "lifecycle_ema_score": c["Lifecycle EMA"][0],
            "Lifecycle EMA": c["Lifecycle EMA"][0],
            "futures_score": c["Futures"][0],
            "daily_change_score": c["Daily change"][0],
        }

        rows.append(row)

    df = pd.DataFrame(rows)
    df.to_csv(CSV_PATH, index=False)


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
        if content.startswith("<!-- DECISION_REPORT_START -->"):
            decision_end = "<!-- DECISION_REPORT_END -->"
            if decision_end in content:
                idx = content.index(decision_end) + len(decision_end)
                new_content = content[:idx] + "\n\n" + section_text + "\n" + content[idx:]
            else:
                new_content = section_text + "\n\n" + content
        else:
            new_content = section_text + "\n\n" + content

    write_text(MAIN_REPORT_PATH, new_content)


def main():
    os.makedirs(REPORT_DIR, exist_ok=True)

    full_text = read_text(MAIN_REPORT_PATH)

    if not full_text:
        raise RuntimeError("latest_report.md non trovato o vuoto.")

    results = [compute_asset(asset, full_text) for asset in ASSETS]

    report_text, _, _ = build_report(results)

    write_text(REPORT_PATH, report_text)
    replace_section_in_latest_report(report_text)
    save_metrics(results)

    print(f"Report scritto in: {REPORT_PATH}")
    print(f"Latest report aggiornato: {MAIN_REPORT_PATH}")
    print(f"CSV scritto in: {CSV_PATH}")

    for res in results:
        print(f"{res['asset']}: {fmt_score(res['total'])} | Lifecycle EMA nel Global = {res['components']['Lifecycle EMA'][0]}")


if __name__ == "__main__":
    main()
