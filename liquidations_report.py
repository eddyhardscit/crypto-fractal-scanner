import os
import csv
import json
import math
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from zoneinfo import ZoneInfo


REPORT_DIR = "reports"
LIQ_REPORT_PATH = "reports/liquidation_report.md"
LIQ_CSV_PATH = "reports/liquidation_metrics.csv"
MAIN_REPORT_PATH = "reports/latest_report.md"

BINANCE_BASE = "https://fapi.binance.com"
COINGLASS_BASE = "https://open-api-v4.coinglass.com"

SYMBOLS = [
    {
        "asset": "BTC",
        "name": "Bitcoin",
        "binance_symbol": "BTCUSDT",
        "coinglass_symbol": "BTCUSDT",
        "coinglass_coin": "BTC",
    },
    {
        "asset": "SOL",
        "name": "Solana",
        "binance_symbol": "SOLUSDT",
        "coinglass_symbol": "SOLUSDT",
        "coinglass_coin": "SOL",
    },
    {
        "asset": "DOGE",
        "name": "Dogecoin",
        "binance_symbol": "DOGEUSDT",
        "coinglass_symbol": "DOGEUSDT",
        "coinglass_coin": "DOGE",
    },
]


def get_json(base_url, path, params=None, headers=None, timeout=20):
    params = params or {}
    headers = headers or {}

    query = urllib.parse.urlencode(params)
    url = f"{base_url}{path}"
    if query:
        url = f"{url}?{query}"

    final_headers = {
        "Accept": "application/json",
        "User-Agent": "crypto-fractal-scanner/1.0",
    }
    final_headers.update(headers)

    request = urllib.request.Request(url, headers=final_headers)

    with urllib.request.urlopen(request, timeout=timeout) as response:
        text = response.read().decode("utf-8")

    return json.loads(text)


def safe_float(value):
    try:
        if value is None:
            return None
        value = float(value)
        if math.isnan(value) or math.isinf(value):
            return None
        return value
    except Exception:
        return None


def pct_change(first, last):
    first = safe_float(first)
    last = safe_float(last)

    if first is None or last is None or first == 0:
        return None

    return ((last - first) / first) * 100


def fmt_price(value):
    value = safe_float(value)

    if value is None:
        return "n/d"

    if abs(value) >= 1000:
        return f"${value:,.0f}"

    if abs(value) >= 1:
        return f"${value:,.2f}"

    return f"${value:.5f}"


def fmt_pct(value, decimals=2):
    value = safe_float(value)

    if value is None:
        return "n/d"

    return f"{value:+.{decimals}f}%"


def fmt_number(value, decimals=2):
    value = safe_float(value)

    if value is None:
        return "n/d"

    return f"{value:,.{decimals}f}"


def fmt_usd(value):
    value = safe_float(value)

    if value is None:
        return "n/d"

    if abs(value) >= 1_000_000_000:
        return f"${value / 1_000_000_000:,.2f}B"

    if abs(value) >= 1_000_000:
        return f"${value / 1_000_000:,.2f}M"

    if abs(value) >= 1_000:
        return f"${value / 1_000:,.2f}K"

    return f"${value:,.2f}"


def timestamp_ms_to_rome(ms):
    value = safe_float(ms)

    if value is None:
        return "n/d"

    dt = datetime.fromtimestamp(value / 1000, tz=timezone.utc)
    return dt.astimezone(ZoneInfo("Europe/Rome")).strftime("%Y-%m-%d %H:%M")


def md_table(headers, rows):
    def clean(x):
        return str(x).replace("|", "\\|").replace("\n", " ")

    lines = []
    lines.append("| " + " | ".join(clean(h) for h in headers) + " |")
    lines.append("| " + " | ".join("---" for _ in headers) + " |")

    for row in rows:
        lines.append("| " + " | ".join(clean(cell) for cell in row) + " |")

    return "\n".join(lines)


def latest_item(items):
    if isinstance(items, list) and items:
        return items[-1]
    return {}


def fetch_binance_asset(cfg):
    symbol = cfg["binance_symbol"]
    errors = []

    def call(label, path, params):
        try:
            return get_json(BINANCE_BASE, path, params=params)
        except Exception as exc:
            errors.append(f"{label}: {exc}")
            return None

    premium = call("premiumIndex", "/fapi/v1/premiumIndex", {"symbol": symbol})
    ticker_24h = call("ticker_24hr", "/fapi/v1/ticker/24hr", {"symbol": symbol})
    open_interest = call("openInterest", "/fapi/v1/openInterest", {"symbol": symbol})

    oi_1h = call(
        "openInterestHist_1h",
        "/futures/data/openInterestHist",
        {"symbol": symbol, "period": "1h", "limit": 25},
    )

    oi_1d = call(
        "openInterestHist_1d",
        "/futures/data/openInterestHist",
        {"symbol": symbol, "period": "1d", "limit": 8},
    )

    global_long_short_1h = call(
        "globalLongShortAccountRatio_1h",
        "/futures/data/globalLongShortAccountRatio",
        {"symbol": symbol, "period": "1h", "limit": 24},
    )

    top_position_1h = call(
        "topLongShortPositionRatio_1h",
        "/futures/data/topLongShortPositionRatio",
        {"symbol": symbol, "period": "1h", "limit": 24},
    )

    taker_1h = call(
        "takerlongshortRatio_1h",
        "/futures/data/takerlongshortRatio",
        {"symbol": symbol, "period": "1h", "limit": 24},
    )

    premium = premium or {}
    ticker_24h = ticker_24h or {}
    open_interest = open_interest or {}

    last_oi_1h = latest_item(oi_1h)
    first_oi_1h = oi_1h[0] if isinstance(oi_1h, list) and oi_1h else {}

    last_oi_1d = latest_item(oi_1d)
    first_oi_1d = oi_1d[0] if isinstance(oi_1d, list) and oi_1d else {}

    last_global_ls = latest_item(global_long_short_1h)
    last_top_position = latest_item(top_position_1h)
    last_taker = latest_item(taker_1h)

    mark_price = safe_float(premium.get("markPrice"))
    if mark_price is None:
        mark_price = safe_float(ticker_24h.get("lastPrice"))

    funding_rate_pct = None
    if safe_float(premium.get("lastFundingRate")) is not None:
        funding_rate_pct = safe_float(premium.get("lastFundingRate")) * 100

    current_oi_contracts = safe_float(open_interest.get("openInterest"))
    current_oi_value = None
    if current_oi_contracts is not None and mark_price is not None:
        current_oi_value = current_oi_contracts * mark_price

    oi_value_24h_change_pct = pct_change(
        first_oi_1h.get("sumOpenInterestValue"),
        last_oi_1h.get("sumOpenInterestValue"),
    )

    oi_value_7d_change_pct = pct_change(
        first_oi_1d.get("sumOpenInterestValue"),
        last_oi_1d.get("sumOpenInterestValue"),
    )

    long_account_pct = None
    short_account_pct = None

    if safe_float(last_global_ls.get("longAccount")) is not None:
        long_account_pct = safe_float(last_global_ls.get("longAccount")) * 100

    if safe_float(last_global_ls.get("shortAccount")) is not None:
        short_account_pct = safe_float(last_global_ls.get("shortAccount")) * 100

    top_long_pct = None
    top_short_pct = None

    if safe_float(last_top_position.get("longAccount")) is not None:
        top_long_pct = safe_float(last_top_position.get("longAccount")) * 100

    if safe_float(last_top_position.get("shortAccount")) is not None:
        top_short_pct = safe_float(last_top_position.get("shortAccount")) * 100

    result = {
        "asset": cfg["asset"],
        "name": cfg["name"],
        "symbol": symbol,
        "mark_price": mark_price,
        "price_change_24h_pct": safe_float(ticker_24h.get("priceChangePercent")),
        "funding_rate_pct": funding_rate_pct,
        "next_funding_time": timestamp_ms_to_rome(premium.get("nextFundingTime")),
        "current_oi_contracts": current_oi_contracts,
        "current_oi_value": current_oi_value,
        "oi_value_24h_change_pct": oi_value_24h_change_pct,
        "oi_value_7d_change_pct": oi_value_7d_change_pct,
        "long_account_pct": long_account_pct,
        "short_account_pct": short_account_pct,
        "global_long_short_ratio": safe_float(last_global_ls.get("longShortRatio")),
        "top_long_pct": top_long_pct,
        "top_short_pct": top_short_pct,
        "top_long_short_ratio": safe_float(last_top_position.get("longShortRatio")),
        "taker_buy_sell_ratio": safe_float(last_taker.get("buySellRatio")),
        "taker_buy_vol": safe_float(last_taker.get("buyVol")),
        "taker_sell_vol": safe_float(last_taker.get("sellVol")),
        "errors": errors,
    }

    return result


def score_asset(metrics):
    downside = 0
    upside = 0
    stress = 0
    reasons = []

    funding = metrics.get("funding_rate_pct")
    oi_24h = metrics.get("oi_value_24h_change_pct")
    price_24h = metrics.get("price_change_24h_pct")
    long_acc = metrics.get("long_account_pct")
    top_long = metrics.get("top_long_pct")
    taker_ratio = metrics.get("taker_buy_sell_ratio")

    if funding is not None:
        if funding >= 0.03:
            downside += 2
            reasons.append("funding molto positivo: mercato long più carico")
        elif funding >= 0.01:
            downside += 1
            reasons.append("funding positivo: leggera pressione long")
        elif funding <= -0.03:
            upside += 2
            reasons.append("funding molto negativo: mercato short più carico")
        elif funding <= -0.01:
            upside += 1
            reasons.append("funding negativo: leggera pressione short")

    if oi_24h is not None:
        if oi_24h >= 5:
            stress += 2
            reasons.append("open interest 24h in forte aumento: più leva nel sistema")
        elif oi_24h >= 2:
            stress += 1
            reasons.append("open interest 24h in aumento: leva in crescita")
        elif oi_24h <= -5:
            stress -= 1
            reasons.append("open interest 24h in calo: parte della leva è già uscita")

    if oi_24h is not None and price_24h is not None and funding is not None:
        if oi_24h >= 2 and price_24h > 0 and funding > 0:
            downside += 2
            reasons.append("prezzo su + OI su + funding positivo: rischio flush long aumentato")
        elif oi_24h >= 2 and price_24h < 0 and funding < 0:
            upside += 2
            reasons.append("prezzo giù + OI su + funding negativo: rischio short squeeze aumentato")

    if long_acc is not None:
        if long_acc >= 60:
            downside += 1
            reasons.append("troppi account long: rischio pulizia sotto")
        elif long_acc <= 40:
            upside += 1
            reasons.append("troppi account short: rischio squeeze sopra")

    if top_long is not None:
        if top_long >= 60:
            downside += 1
            reasons.append("top trader molto long: lato long affollato")
        elif top_long <= 40:
            upside += 1
            reasons.append("top trader più short: possibile squeeze sopra")

    if taker_ratio is not None:
        if taker_ratio >= 1.20:
            upside += 1
            reasons.append("taker buy più forti dei sell: pressione d'acquisto breve")
        elif taker_ratio <= 0.80:
            downside += 1
            reasons.append("taker sell più forti dei buy: pressione vendita breve")

    delta = downside - upside

    if delta >= 2:
        label = "RISCHIO FLUSH SOTTO"
        meaning = "Liquidazioni/rischio leva più orientati verso una pulizia sotto il prezzo."
    elif delta <= -2:
        label = "RISCHIO SHORT SQUEEZE SOPRA"
        meaning = "Liquidazioni/rischio leva più orientati verso uno squeeze sopra il prezzo."
    else:
        if stress >= 2:
            label = "LEVA ALTA / DIREZIONE MISTA"
            meaning = "C'è leva nel sistema, ma la direzione non è pulita."
        else:
            label = "NEUTRALE / MISTO"
            meaning = "I dati futures non danno una direzione netta."

    strength = min(5, max(1, abs(delta) + max(0, stress)))

    return {
        "label": label,
        "meaning": meaning,
        "downside_score": downside,
        "upside_score": upside,
        "stress_score": stress,
        "strength": strength,
        "reasons": reasons[:6],
    }


def theoretical_liquidation_rows(mark_price):
    rows = []

    if mark_price is None:
        return rows

    for leverage in [5, 10, 20, 50]:
        long_liq = mark_price * (1 - (1 / leverage))
        short_liq = mark_price * (1 + (1 / leverage))

        rows.append(
            [
                f"{leverage}x",
                fmt_price(long_liq),
                fmt_price(short_liq),
            ]
        )

    return rows


def fetch_coinglass_heatmap(cfg, mark_price):
    api_key = os.environ.get("COINGLASS_API_KEY", "").strip()

    if not api_key:
        return {
            "status": "not_configured",
            "message": "COINGLASS_API_KEY assente: heatmap vera non attiva.",
            "top_above": [],
            "top_below": [],
        }

    headers = {
        "CG-API-KEY": api_key,
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    params = {
        "exchange": "Binance",
        "symbol": cfg["coinglass_symbol"],
        "range": "3d",
    }

    try:
        raw = get_json(
            COINGLASS_BASE,
            "/api/futures/liquidation/heatmap/model1",
            params=params,
            headers=headers,
            timeout=30,
        )
    except Exception as exc:
        return {
            "status": "error",
            "message": f"Errore CoinGlass: {exc}",
            "top_above": [],
            "top_below": [],
        }

    if str(raw.get("code")) != "0":
        return {
            "status": "error",
            "message": f"CoinGlass risposta non valida: {raw.get('msg', raw)}",
            "top_above": [],
            "top_below": [],
        }

    data = raw.get("data") or {}
    y_axis = data.get("y_axis") or []
    heat_rows = data.get("liquidation_leverage_data") or []

    by_price = defaultdict(float)

    for row in heat_rows:
        try:
            y_index = int(row[1])
            value = float(row[2])
            price = float(y_axis[y_index])
            by_price[price] += value
        except Exception:
            continue

    if not by_price or mark_price is None:
        return {
            "status": "empty",
            "message": "CoinGlass attivo, ma heatmap vuota o non leggibile.",
            "top_above": [],
            "top_below": [],
        }

    above = []
    below = []

    for price, value in by_price.items():
        item = {
            "price": price,
            "distance_pct": ((price - mark_price) / mark_price) * 100,
            "value": value,
        }

        if price >= mark_price:
            above.append(item)
        else:
            below.append(item)

    above = sorted(above, key=lambda x: x["value"], reverse=True)[:5]
    below = sorted(below, key=lambda x: x["value"], reverse=True)[:5]

    return {
        "status": "active",
        "message": "CoinGlass heatmap attiva.",
        "top_above": above,
        "top_below": below,
    }


def render_heatmap_block(heatmap):
    status = heatmap.get("status")

    if status == "not_configured":
        return (
            "Heatmap vera CoinGlass: **non attiva**.\n\n"
            "Motivo: manca il secret `COINGLASS_API_KEY`.\n\n"
            "Per ora il report usa dati Binance pubblici e livelli teorici semplificati."
        )

    if status != "active":
        return f"Heatmap vera CoinGlass: **non disponibile**.\n\nMotivo: {heatmap.get('message', 'errore sconosciuto')}"

    rows_above = []
    rows_below = []

    for item in heatmap.get("top_above", []):
        rows_above.append(
            [
                fmt_price(item["price"]),
                fmt_pct(item["distance_pct"]),
                fmt_number(item["value"], 0),
            ]
        )

    for item in heatmap.get("top_below", []):
        rows_below.append(
            [
                fmt_price(item["price"]),
                fmt_pct(item["distance_pct"]),
                fmt_number(item["value"], 0),
            ]
        )

    text = "Heatmap vera CoinGlass: **attiva**.\n\n"

    text += "Zone sopra il prezzo:\n\n"
    text += md_table(["Prezzo", "Distanza", "Valore relativo"], rows_above or [["n/d", "n/d", "n/d"]])

    text += "\n\nZone sotto il prezzo:\n\n"
    text += md_table(["Prezzo", "Distanza", "Valore relativo"], rows_below or [["n/d", "n/d", "n/d"]])

    return text


def build_report(results):
    rome_now = datetime.now(ZoneInfo("Europe/Rome")).strftime("%Y-%m-%d %H:%M:%S %Z")
    utc_now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    summary_rows = []

    for item in results:
        score = item["score"]

        summary_rows.append(
            [
                item["asset"],
                fmt_price(item["mark_price"]),
                fmt_pct(item["price_change_24h_pct"]),
                fmt_pct(item["funding_rate_pct"], 4),
                fmt_pct(item["oi_value_24h_change_pct"]),
                fmt_pct(item["long_account_pct"]),
                fmt_number(item["taker_buy_sell_ratio"]),
                score["label"],
                f"{score['strength']}/5",
            ]
        )

    text = f"""# Report liquidazioni / futures BTC / SOL / DOGE

Generato: **{rome_now}**  
UTC: **{utc_now}**

Questo report legge la pressione dei futures: funding, open interest, long/short ratio, taker buy/sell e, se configurata in futuro, heatmap CoinGlass.

## Lettura velocissima

{md_table(
    [
        "Asset",
        "Prezzo",
        "Prezzo 24h",
        "Funding",
        "OI 24h",
        "Account long",
        "Taker B/S",
        "Lettura",
        "Forza",
    ],
    summary_rows,
)}

## Come leggere questo report

- **Funding positivo**: i long pagano gli short. Se diventa troppo positivo, il mercato può essere troppo long.
- **Funding negativo**: gli short pagano i long. Se diventa troppo negativo, il mercato può essere troppo short.
- **Open Interest in aumento**: entra più leva nel sistema.
- **Open Interest in calo**: parte della leva è già uscita.
- **Account long troppo alti**: rischio pulizia sotto.
- **Account short troppo alti**: rischio short squeeze sopra.
- **Taker buy/sell ratio sopra 1**: compratori aggressivi più forti dei venditori.
- **Taker buy/sell ratio sotto 1**: venditori aggressivi più forti dei compratori.

Nota importante: i livelli teorici di liquidazione sotto sono una semplificazione matematica. Non sono la vera heatmap del mercato. La vera heatmap richiede CoinGlass o fonte equivalente.

---
"""

    for item in results:
        score = item["score"]

        text += f"""

## {item["name"]} — {item["asset"]}

### Sintesi

**Lettura:** {score["label"]}  
**Forza:** {score["strength"]}/5  
**Significato:** {score["meaning"]}

### Metriche principali

{md_table(
    ["Metrica", "Valore"],
    [
        ["Prezzo mark", fmt_price(item["mark_price"])],
        ["Variazione prezzo 24h", fmt_pct(item["price_change_24h_pct"])],
        ["Funding rate ultimo", fmt_pct(item["funding_rate_pct"], 4)],
        ["Prossimo funding", item["next_funding_time"]],
        ["Open Interest stimato", fmt_usd(item["current_oi_value"])],
        ["Open Interest 24h", fmt_pct(item["oi_value_24h_change_pct"])],
        ["Open Interest 7 giorni", fmt_pct(item["oi_value_7d_change_pct"])],
        ["Account long", fmt_pct(item["long_account_pct"])],
        ["Account short", fmt_pct(item["short_account_pct"])],
        ["Long/Short ratio globale", fmt_number(item["global_long_short_ratio"])],
        ["Top trader long", fmt_pct(item["top_long_pct"])],
        ["Top trader short", fmt_pct(item["top_short_pct"])],
        ["Top trader long/short ratio", fmt_number(item["top_long_short_ratio"])],
        ["Taker buy/sell ratio", fmt_number(item["taker_buy_sell_ratio"])],
    ],
)}

### Perché lo scanner futures legge così

"""

        if score["reasons"]:
            for reason in score["reasons"]:
                text += f"- {reason}\n"
        else:
            text += "- Nessun segnale futures netto.\n"

        text += f"""

### Livelli teorici semplificati di liquidazione

Questi livelli sono calcolati come se una posizione fosse stata aperta vicino al prezzo attuale. Sono **indicativi**, non precisi, perché ogni exchange usa margine di mantenimento, fee, modalità isolated/cross e regole diverse.

{md_table(
    ["Leva", "Long circa liquidato sotto", "Short circa liquidato sopra"],
    theoretical_liquidation_rows(item["mark_price"]) or [["n/d", "n/d", "n/d"]],
)}

### Heatmap CoinGlass

{render_heatmap_block(item["heatmap"])}

"""

        if item["errors"]:
            text += "\n### Errori/parziali\n\n"
            for err in item["errors"]:
                text += f"- {err}\n"

        text += "\n---\n"

    return text


def build_main_report_summary(results):
    rows = []

    for item in results:
        score = item["score"]
        rows.append(
            [
                item["asset"],
                fmt_price(item["mark_price"]),
                fmt_pct(item["funding_rate_pct"], 4),
                fmt_pct(item["oi_value_24h_change_pct"]),
                fmt_pct(item["long_account_pct"]),
                score["label"],
                f"{score['strength']}/5",
            ]
        )

    return f"""

<!-- LIQUIDATION_SUMMARY_START -->

---

# Sintesi futures / liquidazioni

Report separato completo: [liquidation_report.md](liquidation_report.md)

{md_table(
    ["Asset", "Prezzo", "Funding", "OI 24h", "Account long", "Lettura futures", "Forza"],
    rows,
)}

## Come usarla insieme al frattale

- Se il **frattale è ribassista** e anche i **futures indicano rischio flush sotto**, il segnale di prudenza aumenta.
- Se il **frattale è ribassista** ma i **futures indicano short squeeze sopra**, il rischio è più ambiguo.
- Se il **frattale è rialzista** e i **futures indicano short squeeze sopra**, il segnale rialzista è più interessante.
- Se i due segnali sono opposti, meglio ridurre aggressività e non leggere il report come certezza.

<!-- LIQUIDATION_SUMMARY_END -->
"""


def append_summary_to_main_report(results):
    if not os.path.exists(MAIN_REPORT_PATH):
        return

    with open(MAIN_REPORT_PATH, "r", encoding="utf-8") as f:
        current = f.read()

    start_marker = "<!-- LIQUIDATION_SUMMARY_START -->"
    end_marker = "<!-- LIQUIDATION_SUMMARY_END -->"

    if start_marker in current and end_marker in current:
        before = current.split(start_marker)[0].rstrip()
        after = current.split(end_marker, 1)[1].lstrip()
        current = before + "\n\n" + after

    summary = build_main_report_summary(results)

    with open(MAIN_REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(current.rstrip() + "\n\n" + summary.strip() + "\n")


def write_csv(results):
    fieldnames = [
        "asset",
        "symbol",
        "mark_price",
        "price_change_24h_pct",
        "funding_rate_pct",
        "current_oi_value",
        "oi_value_24h_change_pct",
        "oi_value_7d_change_pct",
        "long_account_pct",
        "short_account_pct",
        "global_long_short_ratio",
        "top_long_pct",
        "top_short_pct",
        "top_long_short_ratio",
        "taker_buy_sell_ratio",
        "futures_label",
        "futures_strength",
        "downside_score",
        "upside_score",
        "stress_score",
    ]

    with open(LIQ_CSV_PATH, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for item in results:
            score = item["score"]
            writer.writerow(
                {
                    "asset": item["asset"],
                    "symbol": item["symbol"],
                    "mark_price": item["mark_price"],
                    "price_change_24h_pct": item["price_change_24h_pct"],
                    "funding_rate_pct": item["funding_rate_pct"],
                    "current_oi_value": item["current_oi_value"],
                    "oi_value_24h_change_pct": item["oi_value_24h_change_pct"],
                    "oi_value_7d_change_pct": item["oi_value_7d_change_pct"],
                    "long_account_pct": item["long_account_pct"],
                    "short_account_pct": item["short_account_pct"],
                    "global_long_short_ratio": item["global_long_short_ratio"],
                    "top_long_pct": item["top_long_pct"],
                    "top_short_pct": item["top_short_pct"],
                    "top_long_short_ratio": item["top_long_short_ratio"],
                    "taker_buy_sell_ratio": item["taker_buy_sell_ratio"],
                    "futures_label": score["label"],
                    "futures_strength": score["strength"],
                    "downside_score": score["downside_score"],
                    "upside_score": score["upside_score"],
                    "stress_score": score["stress_score"],
                }
            )


def main():
    os.makedirs(REPORT_DIR, exist_ok=True)

    results = []

    for cfg in SYMBOLS:
        metrics = fetch_binance_asset(cfg)
        metrics["score"] = score_asset(metrics)
        metrics["heatmap"] = fetch_coinglass_heatmap(cfg, metrics.get("mark_price"))
        results.append(metrics)

    report_text = build_report(results)

    with open(LIQ_REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report_text)

    write_csv(results)
    append_summary_to_main_report(results)

    print(f"Liquidation report written to {LIQ_REPORT_PATH}")
    print(f"Liquidation metrics written to {LIQ_CSV_PATH}")
    print(f"Main report updated: {MAIN_REPORT_PATH}")


if __name__ == "__main__":
    main()
