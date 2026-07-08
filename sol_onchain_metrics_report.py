import csv
import json
import os
import re
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from zoneinfo import ZoneInfo


REPORT_DIR = "reports"
MAIN_REPORT_PATH = "reports/latest_report.md"

REPORT_PATH = "reports/sol_onchain_metrics_report.md"
HISTORY_CSV_PATH = "reports/sol_onchain_metrics_history.csv"
LATEST_JSON_PATH = "reports/sol_onchain_metrics_latest.json"

START_MARKER = "<!-- SOL_ONCHAIN_METRICS_START -->"
END_MARKER = "<!-- SOL_ONCHAIN_METRICS_END -->"

RSI_END = "<!-- RSI_TOP_CYCLE_END -->"
BTC_SOL_END = "<!-- BTC_SOL_FRACTAL_END -->"
GLOBAL_END = "<!-- GLOBAL_CONFLUENCE_END -->"

SOLANA_RPC_URL = os.getenv("SOLANA_RPC_URL", "https://api.mainnet-beta.solana.com")
LAMPORTS_PER_SOL = 1_000_000_000.0

# Metriche opzionali da provider esterni o inserimento manuale.
# Se non le hai, lasciale vuote: il report funziona comunque.
OPTIONAL_ENV_FIELDS = {
    "sol_realized_price_usd": "SOL_REALIZED_PRICE_USD",
    "sol_mvrv": "SOL_MVRV",
    "sol_holder_profit_pct": "SOL_HOLDER_PROFIT_PCT",
    "sol_holder_loss_pct": "SOL_HOLDER_LOSS_PCT",
    "sol_exchange_netflow_24h_usd": "SOL_EXCHANGE_NETFLOW_24H_USD",
}


COLUMNS = [
    "date",
    "generated_at_utc",

    "sol_price_usd",
    "sol_market_cap_usd",
    "sol_volume_24h_usd",
    "sol_24h_change_pct",

    "chain_tvl_usd",
    "chain_tvl_change_1d_pct",
    "chain_tvl_change_7d_pct",
    "chain_tvl_change_30d_pct",

    "dex_volume_24h_usd",
    "dex_volume_7d_usd",
    "dex_volume_30d_usd",
    "dex_volume_change_1d_pct",
    "dex_volume_change_7d_pct",

    "fees_24h_usd",
    "fees_7d_usd",
    "fees_30d_usd",
    "fees_change_1d_pct",
    "fees_change_7d_pct",

    "stablecoins_usd",
    "stablecoins_change_7d_pct",
    "stablecoins_change_30d_pct",

    "sol_total_supply",
    "sol_circulating_supply",
    "sol_non_circulating_supply",
    "sol_activated_stake",
    "sol_stake_ratio_total_pct",
    "sol_stake_ratio_circulating_pct",
    "sol_delinquent_stake",
    "sol_delinquent_stake_ratio_pct",
    "sol_current_validators",
    "sol_delinquent_validators",
    "sol_inflation_rate_pct",

    "sol_realized_price_usd",
    "sol_mvrv",
    "sol_holder_profit_pct",
    "sol_holder_loss_pct",
    "sol_exchange_netflow_24h_usd",

    "onchain_score",
    "onchain_bias",
    "onchain_action",
    "missing_important_metrics",
]


def now_utc():
    return datetime.now(timezone.utc)


def today_str():
    return now_utc().strftime("%Y-%m-%d")


def utc_str():
    return now_utc().strftime("%Y-%m-%d %H:%M:%S UTC")


def clean_text(value):
    if value is None:
        return ""
    return str(value).replace("\xa0", " ").strip()


def parse_number(value):
    if value is None:
        return None

    text = clean_text(value)
    if text == "":
        return None

    text = text.replace("$", "")
    text = text.replace("%", "")
    text = text.replace("€", "")
    text = text.replace(" ", "")

    match = re.search(r"[-+]?\d[\d\.,]*", text)
    if not match:
        return None

    number = match.group(0)

    if "," in number:
        number = number.replace(".", "")
        number = number.replace(",", ".")
    else:
        if number.count(".") > 1:
            number = number.replace(".", "")

    try:
        return float(number)
    except Exception:
        return None


def safe_float(value):
    try:
        if value is None:
            return None
        return float(value)
    except Exception:
        return parse_number(value)


def lamports_to_sol(value):
    value = safe_float(value)
    if value is None:
        return None

    # I valori RPC di Solana sono normalmente in lamports.
    # Se però in futuro un provider restituisse già SOL, non dividiamo valori piccoli.
    if value > 10_000_000_000:
        return value / LAMPORTS_PER_SOL

    return value


def pct_change(new, old):
    new = safe_float(new)
    old = safe_float(old)

    if new is None or old is None or old == 0:
        return None

    return (new / old - 1.0) * 100.0


def fmt_number(value, decimals=2):
    value = safe_float(value)

    if value is None:
        return "n/a"

    formatted = f"{value:,.{decimals}f}"
    return formatted.replace(",", "X").replace(".", ",").replace("X", ".")


def fmt_usd(value, decimals=2):
    value = safe_float(value)

    if value is None:
        return "n/a"

    abs_value = abs(value)

    if abs_value >= 1_000_000_000:
        return f"{fmt_number(value / 1_000_000_000, 2)} mld $"

    if abs_value >= 1_000_000:
        return f"{fmt_number(value / 1_000_000, 2)} mln $"

    if abs_value >= 1_000:
        return f"{fmt_number(value, 0)} $"

    return f"{fmt_number(value, decimals)} $"


def fmt_price(value):
    return fmt_usd(value, 2)


def fmt_pct(value, decimals=2, force_sign=True):
    value = safe_float(value)

    if value is None:
        return "n/a"

    sign = "+" if force_sign and value > 0 else ""
    return f"{sign}{fmt_number(value, decimals)}%"


def md_table(headers, rows):
    def cell(value):
        value = "" if value is None else str(value)
        return value.replace("|", "\\|").replace("\n", " ")

    lines = []
    lines.append("| " + " | ".join(cell(h) for h in headers) + " |")
    lines.append("| " + " | ".join("---" for _ in headers) + " |")

    for row in rows:
        lines.append("| " + " | ".join(cell(v) for v in row) + " |")

    return "\n".join(lines)


def http_json(url, method="GET", payload=None, timeout=25):
    headers = {
        "User-Agent": "crypto-fractal-scanner/1.0",
        "Accept": "application/json",
    }

    data = None

    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"

    request = urllib.request.Request(
        url=url,
        data=data,
        headers=headers,
        method=method,
    )

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
            return json.loads(raw)
    except Exception as exc:
        return {
            "_error": str(exc),
            "_url": url,
        }


def rpc_call(method, params=None):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
    }

    if params is not None:
        payload["params"] = params

    data = http_json(SOLANA_RPC_URL, method="POST", payload=payload)

    if isinstance(data, dict) and "result" in data:
        return data["result"]

    return None


def get_nested(data, *keys):
    current = data

    for key in keys:
        if not isinstance(current, dict):
            return None
        current = current.get(key)

    return current


def load_history():
    if not os.path.exists(HISTORY_CSV_PATH):
        return []

    rows = []

    try:
        with open(HISTORY_CSV_PATH, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(dict(row))
    except Exception:
        return []

    return rows


def save_history(rows):
    os.makedirs(REPORT_DIR, exist_ok=True)

    with open(HISTORY_CSV_PATH, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()

        for row in rows:
            clean_row = {col: row.get(col) for col in COLUMNS}
            writer.writerow(clean_row)


def latest_previous_row(rows, date_value):
    filtered = []

    for row in rows:
        d = row.get("date")
        if d and d < date_value:
            filtered.append(row)

    if not filtered:
        return None

    filtered.sort(key=lambda r: r.get("date", ""))
    return filtered[-1]


def get_defillama_price():
    result = {
        "sol_price_usd": None,
        "sol_market_cap_usd": None,
        "sol_volume_24h_usd": None,
        "sol_24h_change_pct": None,
    }

    params = urllib.parse.urlencode(
        {
            "ids": "solana",
            "vs_currencies": "usd",
            "include_market_cap": "true",
            "include_24hr_vol": "true",
            "include_24hr_change": "true",
            "include_last_updated_at": "true",
        }
    )
    cg_url = f"https://api.coingecko.com/api/v3/simple/price?{params}"
    cg = http_json(cg_url)

    sol = get_nested(cg, "solana")

    if isinstance(sol, dict):
        result["sol_price_usd"] = safe_float(sol.get("usd"))
        result["sol_market_cap_usd"] = safe_float(sol.get("usd_market_cap"))
        result["sol_volume_24h_usd"] = safe_float(sol.get("usd_24h_vol"))
        result["sol_24h_change_pct"] = safe_float(sol.get("usd_24h_change"))

    if result["sol_price_usd"] is None:
        llama = http_json("https://coins.llama.fi/prices/current/coingecko:solana")
        coin = get_nested(llama, "coins", "coingecko:solana")
        if isinstance(coin, dict):
            result["sol_price_usd"] = safe_float(coin.get("price"))

    return result


def get_chain_tvl():
    result = {
        "chain_tvl_usd": None,
        "chain_tvl_change_1d_pct": None,
        "chain_tvl_change_7d_pct": None,
        "chain_tvl_change_30d_pct": None,
    }

    chains = http_json("https://api.llama.fi/v2/chains")

    if isinstance(chains, list):
        for item in chains:
            if str(item.get("name") or item.get("chain") or "").lower() == "solana":
                result["chain_tvl_usd"] = safe_float(item.get("tvl"))
                result["chain_tvl_change_1d_pct"] = safe_float(item.get("change_1d"))
                result["chain_tvl_change_7d_pct"] = safe_float(item.get("change_7d"))
                result["chain_tvl_change_30d_pct"] = safe_float(item.get("change_1m"))
                break

    hist = http_json("https://api.llama.fi/v2/historicalChainTvl/Solana")

    if isinstance(hist, list) and hist:
        clean = []
        for item in hist:
            value = safe_float(item.get("tvl"))
            date_value = safe_float(item.get("date"))
            if value is not None and date_value is not None:
                clean.append({"date": date_value, "tvl": value})

        clean.sort(key=lambda x: x["date"])

        if clean:
            latest = clean[-1]
            result["chain_tvl_usd"] = result["chain_tvl_usd"] or latest["tvl"]

            if result["chain_tvl_change_7d_pct"] is None and len(clean) > 8:
                result["chain_tvl_change_7d_pct"] = pct_change(latest["tvl"], clean[-8]["tvl"])

            if result["chain_tvl_change_30d_pct"] is None and len(clean) > 31:
                result["chain_tvl_change_30d_pct"] = pct_change(latest["tvl"], clean[-31]["tvl"])

    return result


def get_overview_metrics(kind):
    if kind == "dexs":
        url = "https://api.llama.fi/overview/dexs/Solana"
    else:
        url = "https://api.llama.fi/overview/fees/Solana"

    data = http_json(url)

    result = {}

    if not isinstance(data, dict):
        return result

    result["total24h"] = safe_float(
        data.get("total24h")
        or data.get("total24hUSD")
        or data.get("dailyVolume")
        or data.get("dailyFees")
    )

    result["total7d"] = safe_float(
        data.get("total7d")
        or data.get("total7dUSD")
        or data.get("weeklyVolume")
        or data.get("weeklyFees")
    )

    result["total30d"] = safe_float(
        data.get("total30d")
        or data.get("total30dUSD")
        or data.get("monthlyVolume")
        or data.get("monthlyFees")
    )

    result["change_1d"] = safe_float(data.get("change_1d"))
    result["change_7d"] = safe_float(data.get("change_7d"))

    chart = data.get("totalDataChart") or data.get("totalDataChartBreakdown")

    if isinstance(chart, list):
        values = []
        for item in chart:
            if isinstance(item, list) and len(item) >= 2:
                value = None

                if isinstance(item[1], dict):
                    total = 0.0
                    found = False
                    for v in item[1].values():
                        v = safe_float(v)
                        if v is not None:
                            total += v
                            found = True
                    value = total if found else None
                else:
                    value = safe_float(item[1])

                if value is not None:
                    values.append(value)

        if values:
            result["total24h"] = result.get("total24h") or values[-1]

            if result.get("change_7d") is None and len(values) > 8:
                result["change_7d"] = pct_change(values[-1], values[-8])

            if result.get("change_1d") is None and len(values) > 2:
                result["change_1d"] = pct_change(values[-1], values[-2])

    return result


def extract_stablecoin_value(item):
    if not isinstance(item, dict):
        return None

    candidates = [
        item.get("totalCirculatingUSD"),
        item.get("currentCirculatingUSD"),
        item.get("mcap"),
        item.get("totalCirculating"),
        item.get("circulating"),
    ]

    for candidate in candidates:
        if isinstance(candidate, dict):
            if safe_float(candidate.get("peggedUSD")) is not None:
                return safe_float(candidate.get("peggedUSD"))

            total = 0.0
            found = False
            for value in candidate.values():
                value = safe_float(value)
                if value is not None:
                    total += value
                    found = True
            if found:
                return total

        value = safe_float(candidate)
        if value is not None:
            return value

    return None


def get_stablecoins():
    result = {
        "stablecoins_usd": None,
        "stablecoins_change_7d_pct": None,
        "stablecoins_change_30d_pct": None,
    }

    hist = http_json("https://stablecoins.llama.fi/stablecoincharts/Solana")

    values = []

    if isinstance(hist, list):
        for item in hist:
            value = extract_stablecoin_value(item)
            if value is not None:
                values.append(value)

    elif isinstance(hist, dict):
        chart = hist.get("data") or hist.get("chainCirculating") or hist.get("peggedAssets")
        if isinstance(chart, list):
            for item in chart:
                value = extract_stablecoin_value(item)
                if value is not None:
                    values.append(value)

    if values:
        result["stablecoins_usd"] = values[-1]

        if len(values) > 8:
            result["stablecoins_change_7d_pct"] = pct_change(values[-1], values[-8])

        if len(values) > 31:
            result["stablecoins_change_30d_pct"] = pct_change(values[-1], values[-31])

    if result["stablecoins_usd"] is None:
        chains = http_json("https://stablecoins.llama.fi/stablecoinchains")
        items = []

        if isinstance(chains, dict):
            if isinstance(chains.get("chains"), list):
                items = chains.get("chains")
            elif isinstance(chains.get("data"), list):
                items = chains.get("data")
        elif isinstance(chains, list):
            items = chains

        for item in items:
            chain_name = str(item.get("name") or item.get("chain") or "").lower()
            if chain_name == "solana":
                result["stablecoins_usd"] = extract_stablecoin_value(item)
                break

    return result


def get_solana_rpc_metrics():
    result = {
        "sol_total_supply": None,
        "sol_circulating_supply": None,
        "sol_non_circulating_supply": None,
        "sol_activated_stake": None,
        "sol_stake_ratio_total_pct": None,
        "sol_stake_ratio_circulating_pct": None,
        "sol_delinquent_stake": None,
        "sol_delinquent_stake_ratio_pct": None,
        "sol_current_validators": None,
        "sol_delinquent_validators": None,
        "sol_inflation_rate_pct": None,
    }

    if os.getenv("SOL_ONCHAIN_DISABLE_RPC", "0") == "1":
        return result

    supply = rpc_call(
        "getSupply",
        [
            {
                "commitment": "finalized",
                "excludeNonCirculatingAccountsList": True,
            }
        ],
    )

    if isinstance(supply, dict):
        value = supply.get("value", supply)
        if isinstance(value, dict):
            result["sol_total_supply"] = lamports_to_sol(value.get("total"))
            result["sol_circulating_supply"] = lamports_to_sol(value.get("circulating"))
            result["sol_non_circulating_supply"] = lamports_to_sol(value.get("nonCirculating"))

    vote_accounts = rpc_call(
        "getVoteAccounts",
        [
            {
                "commitment": "finalized",
                "keepUnstakedDelinquents": False,
            }
        ],
    )

    if isinstance(vote_accounts, dict):
        current = vote_accounts.get("current") or []
        delinquent = vote_accounts.get("delinquent") or []

        current_stake_lamports = 0.0
        delinquent_stake_lamports = 0.0

        for account in current:
            current_stake_lamports += safe_float(account.get("activatedStake")) or 0.0

        for account in delinquent:
            delinquent_stake_lamports += safe_float(account.get("activatedStake")) or 0.0

        activated_stake_sol = current_stake_lamports / LAMPORTS_PER_SOL
        delinquent_stake_sol = delinquent_stake_lamports / LAMPORTS_PER_SOL
        total_stake_sol = activated_stake_sol + delinquent_stake_sol

        result["sol_current_validators"] = len(current)
        result["sol_delinquent_validators"] = len(delinquent)

        if total_stake_sol > 0:
            result["sol_activated_stake"] = total_stake_sol
            result["sol_delinquent_stake"] = delinquent_stake_sol

            total_supply_sol = safe_float(result["sol_total_supply"])
            circulating_supply_sol = safe_float(result["sol_circulating_supply"])

            if total_supply_sol and total_supply_sol > 0:
                result["sol_stake_ratio_total_pct"] = total_stake_sol / total_supply_sol * 100.0

            if circulating_supply_sol and circulating_supply_sol > 0:
                result["sol_stake_ratio_circulating_pct"] = total_stake_sol / circulating_supply_sol * 100.0

            result["sol_delinquent_stake_ratio_pct"] = delinquent_stake_sol / total_stake_sol * 100.0

    inflation = rpc_call("getInflationRate")

    if isinstance(inflation, dict):
        total = safe_float(inflation.get("total"))
        if total is not None:
            result["sol_inflation_rate_pct"] = total * 100.0

    return result


def get_optional_external_metrics():
    result = {}

    for key, env_name in OPTIONAL_ENV_FIELDS.items():
        result[key] = parse_number(os.getenv(env_name))

    return result


def get_all_metrics():
    row = {col: None for col in COLUMNS}
    row["date"] = today_str()
    row["generated_at_utc"] = utc_str()

    dex_metrics = get_overview_metrics("dexs")
    fees_metrics = get_overview_metrics("fees")

    sources = [
        get_defillama_price(),
        get_chain_tvl(),
        {
            "dex_volume_24h_usd": dex_metrics.get("total24h"),
            "dex_volume_7d_usd": dex_metrics.get("total7d"),
            "dex_volume_30d_usd": dex_metrics.get("total30d"),
            "dex_volume_change_1d_pct": dex_metrics.get("change_1d"),
            "dex_volume_change_7d_pct": dex_metrics.get("change_7d"),
        },
        {
            "fees_24h_usd": fees_metrics.get("total24h"),
            "fees_7d_usd": fees_metrics.get("total7d"),
            "fees_30d_usd": fees_metrics.get("total30d"),
            "fees_change_1d_pct": fees_metrics.get("change_1d"),
            "fees_change_7d_pct": fees_metrics.get("change_7d"),
        },
        get_stablecoins(),
        get_solana_rpc_metrics(),
        get_optional_external_metrics(),
    ]

    for source in sources:
        for key, value in source.items():
            if key in row and value is not None:
                row[key] = value

    return row


def add_component(components, score, name, value, points, reason):
    components.append(
        {
            "name": name,
            "value": value,
            "points": points,
            "reason": reason,
        }
    )
    return score + points


def compute_score(row, previous_row=None):
    score = 0
    components = []

    price = safe_float(row.get("sol_price_usd"))
    market_cap = safe_float(row.get("sol_market_cap_usd"))

    realized_price = safe_float(row.get("sol_realized_price_usd"))
    mvrv = safe_float(row.get("sol_mvrv"))
    holder_profit = safe_float(row.get("sol_holder_profit_pct"))
    exchange_netflow = safe_float(row.get("sol_exchange_netflow_24h_usd"))

    tvl_change = safe_float(row.get("chain_tvl_change_7d_pct"))
    dex_change = safe_float(row.get("dex_volume_change_7d_pct"))
    fees_change = safe_float(row.get("fees_change_7d_pct"))
    stable_change = safe_float(row.get("stablecoins_change_7d_pct"))
    stake_ratio = safe_float(row.get("sol_stake_ratio_total_pct"))
    delinquent_ratio = safe_float(row.get("sol_delinquent_stake_ratio_pct"))

    if tvl_change is not None:
        if tvl_change > 5:
            score = add_component(components, score, "TVL 7g", fmt_pct(tvl_change), 1, "TVL in crescita: rete più forte.")
        elif tvl_change < -5:
            score = add_component(components, score, "TVL 7g", fmt_pct(tvl_change), -1, "TVL in calo: liquidità DeFi in uscita.")
        else:
            score = add_component(components, score, "TVL 7g", fmt_pct(tvl_change), 0, "TVL stabile.")

    if dex_change is not None:
        if dex_change > 10:
            score = add_component(components, score, "DEX volume 7g", fmt_pct(dex_change), 1, "Volume DEX in aumento: attività reale più forte.")
        elif dex_change < -10:
            score = add_component(components, score, "DEX volume 7g", fmt_pct(dex_change), -1, "Volume DEX in calo: attività più debole.")
        else:
            score = add_component(components, score, "DEX volume 7g", fmt_pct(dex_change), 0, "Volume DEX stabile.")

    if fees_change is not None:
        if fees_change > 10:
            score = add_component(components, score, "Fees 7g", fmt_pct(fees_change), 1, "Fee in crescita: uso della rete in miglioramento.")
        elif fees_change < -10:
            score = add_component(components, score, "Fees 7g", fmt_pct(fees_change), -1, "Fee in calo: uso della rete più debole.")
        else:
            score = add_component(components, score, "Fees 7g", fmt_pct(fees_change), 0, "Fee stabili.")

    if stable_change is not None:
        if stable_change > 2:
            score = add_component(components, score, "Stablecoin liquidity 7g", fmt_pct(stable_change), 1, "Stablecoin su Solana in aumento: liquidità disponibile migliore.")
        elif stable_change < -2:
            score = add_component(components, score, "Stablecoin liquidity 7g", fmt_pct(stable_change), -1, "Stablecoin su Solana in calo: liquidità in uscita.")
        else:
            score = add_component(components, score, "Stablecoin liquidity 7g", fmt_pct(stable_change), 0, "Stablecoin stabili.")

    if stake_ratio is not None:
        if stake_ratio <= 0.01:
            score = add_component(
                components,
                score,
                "Stake ratio",
                fmt_pct(stake_ratio, force_sign=False),
                0,
                "Dato stake non affidabile o non letto correttamente: non viene penalizzato.",
            )
        elif stake_ratio >= 55:
            score = add_component(components, score, "Stake ratio", fmt_pct(stake_ratio, force_sign=False), 1, "Quota staked alta: supply liquida più contenuta.")
        elif stake_ratio < 40:
            score = add_component(components, score, "Stake ratio", fmt_pct(stake_ratio, force_sign=False), -1, "Quota staked bassa: supply più liquida.")
        else:
            score = add_component(components, score, "Stake ratio", fmt_pct(stake_ratio, force_sign=False), 0, "Quota staked normale.")

    if delinquent_ratio is not None:
        if delinquent_ratio > 2:
            score = add_component(components, score, "Stake delinquent", fmt_pct(delinquent_ratio, force_sign=False), -1, "Quota delinquent alta: qualità validatori da monitorare.")
        else:
            score = add_component(components, score, "Stake delinquent", fmt_pct(delinquent_ratio, force_sign=False), 0, "Delinquent stake basso.")

    if realized_price is not None and price is not None and realized_price > 0:
        price_to_realized = price / realized_price

        if price_to_realized < 1.1:
            score = add_component(components, score, "Prezzo / realized price", f"{fmt_number(price_to_realized, 2)}x", 2, "Prezzo vicino/sotto costo medio stimato: zona potenzialmente interessante.")
        elif price_to_realized < 1.6:
            score = add_component(components, score, "Prezzo / realized price", f"{fmt_number(price_to_realized, 2)}x", 1, "Prezzo sopra realized price ma non troppo esteso.")
        elif price_to_realized > 3.0:
            score = add_component(components, score, "Prezzo / realized price", f"{fmt_number(price_to_realized, 2)}x", -2, "Prezzo molto esteso sopra realized price: rischio prese profitto.")
        elif price_to_realized > 2.2:
            score = add_component(components, score, "Prezzo / realized price", f"{fmt_number(price_to_realized, 2)}x", -1, "Prezzo abbastanza esteso sopra realized price.")
        else:
            score = add_component(components, score, "Prezzo / realized price", f"{fmt_number(price_to_realized, 2)}x", 0, "Prezzo in zona media rispetto al realized price.")

    if mvrv is not None:
        if mvrv <= 1.0:
            score = add_component(components, score, "MVRV", fmt_number(mvrv, 2), 2, "MVRV vicino/sotto 1: mercato poco in profitto, potenziale accumulo.")
        elif mvrv <= 1.5:
            score = add_component(components, score, "MVRV", fmt_number(mvrv, 2), 1, "MVRV sano, non troppo esteso.")
        elif mvrv >= 3.5:
            score = add_component(components, score, "MVRV", fmt_number(mvrv, 2), -2, "MVRV molto alto: rischio surriscaldamento.")
        elif mvrv >= 2.5:
            score = add_component(components, score, "MVRV", fmt_number(mvrv, 2), -1, "MVRV elevato: attenzione a profit taking.")
        else:
            score = add_component(components, score, "MVRV", fmt_number(mvrv, 2), 0, "MVRV intermedio.")

    if holder_profit is not None:
        if holder_profit < 50:
            score = add_component(components, score, "Holder in profit", fmt_pct(holder_profit, force_sign=False), 1, "Pochi holder in profit: pressione take profit più bassa.")
        elif holder_profit > 85:
            score = add_component(components, score, "Holder in profit", fmt_pct(holder_profit, force_sign=False), -2, "Troppi holder in profit: rischio prese profitto.")
        elif holder_profit > 75:
            score = add_component(components, score, "Holder in profit", fmt_pct(holder_profit, force_sign=False), -1, "Molti holder in profit: attenzione agli spike.")
        else:
            score = add_component(components, score, "Holder in profit", fmt_pct(holder_profit, force_sign=False), 0, "Holder in profit in zona media.")

    if exchange_netflow is not None:
        if market_cap:
            flow_ratio = exchange_netflow / market_cap * 100.0
            value_text = f"{fmt_usd(exchange_netflow)} / {fmt_pct(flow_ratio)} mcap"

            if flow_ratio > 0.15:
                score = add_component(components, score, "Exchange netflow", value_text, -2, "Forte inflow verso exchange: possibile pressione vendita.")
            elif flow_ratio > 0.05:
                score = add_component(components, score, "Exchange netflow", value_text, -1, "Inflow verso exchange: prudenza.")
            elif flow_ratio < -0.15:
                score = add_component(components, score, "Exchange netflow", value_text, 2, "Forte outflow da exchange: possibile accumulo.")
            elif flow_ratio < -0.05:
                score = add_component(components, score, "Exchange netflow", value_text, 1, "Outflow da exchange: segnale costruttivo.")
            else:
                score = add_component(components, score, "Exchange netflow", value_text, 0, "Netflow contenuto.")
        else:
            value_text = fmt_usd(exchange_netflow)

            if exchange_netflow > 100_000_000:
                score = add_component(components, score, "Exchange netflow", value_text, -2, "Forte inflow verso exchange.")
            elif exchange_netflow > 25_000_000:
                score = add_component(components, score, "Exchange netflow", value_text, -1, "Inflow verso exchange.")
            elif exchange_netflow < -100_000_000:
                score = add_component(components, score, "Exchange netflow", value_text, 2, "Forte outflow da exchange.")
            elif exchange_netflow < -25_000_000:
                score = add_component(components, score, "Exchange netflow", value_text, 1, "Outflow da exchange.")
            else:
                score = add_component(components, score, "Exchange netflow", value_text, 0, "Netflow contenuto.")

    score = max(-8, min(8, score))

    if score >= 5:
        bias = "POSITIVA FORTE"
        action = "ON-CHAIN SANO / RAFFORZA IL FRATTALE"
    elif score >= 2:
        bias = "POSITIVA"
        action = "CONFERMA MODERATA / BUONO SE IL FRATTALE REGGE"
    elif score >= -1:
        bias = "NEUTRALE / MISTA"
        action = "NESSUNA CONFERMA FORTE / LEGGERE INSIEME AL FRATTALE"
    elif score >= -4:
        bias = "NEGATIVA"
        action = "PRUDENZA / POSSIBILE PRESSIONE"
    else:
        bias = "NEGATIVA FORTE"
        action = "RISCHIO ALTO / FRATTALE MENO AFFIDABILE"

    missing = []
    for key in [
        "sol_realized_price_usd",
        "sol_mvrv",
        "sol_holder_profit_pct",
        "sol_exchange_netflow_24h_usd",
    ]:
        if row.get(key) is None:
            missing.append(key)

    row["onchain_score"] = score
    row["onchain_bias"] = bias
    row["onchain_action"] = action
    row["missing_important_metrics"] = ", ".join(missing) if missing else "nessuna"

    return row, components


def update_history(row):
    rows = load_history()
    date_value = row.get("date")

    rows = [r for r in rows if r.get("date") != date_value]
    rows.append(row)
    rows.sort(key=lambda r: r.get("date", ""))

    save_history(rows)
    return rows


def build_metric_table(row):
    return md_table(
        ["Metrica", "Valore", "Lettura"],
        [
            ["Prezzo SOL", fmt_price(row.get("sol_price_usd")), "Prezzo spot usato per il report."],
            ["Market cap", fmt_usd(row.get("sol_market_cap_usd")), "Grandezza complessiva di mercato."],
            ["Volume 24h", fmt_usd(row.get("sol_volume_24h_usd")), "Liquidità di trading spot aggregata."],
            ["TVL Solana", fmt_usd(row.get("chain_tvl_usd")), "Capitale in DeFi su Solana."],
            ["TVL 7g", fmt_pct(row.get("chain_tvl_change_7d_pct")), "Crescita/calo DeFi a 7 giorni."],
            ["DEX volume 24h", fmt_usd(row.get("dex_volume_24h_usd")), "Attività di scambio on-chain."],
            ["DEX volume 7g", fmt_usd(row.get("dex_volume_7d_usd")), "Volume settimanale DEX."],
            ["DEX change 7g", fmt_pct(row.get("dex_volume_change_7d_pct")), "Accelerazione o rallentamento DEX."],
            ["Fees 24h", fmt_usd(row.get("fees_24h_usd")), "Fee generate dalla chain/protocolli monitorati."],
            ["Fees 7g", fmt_usd(row.get("fees_7d_usd")), "Fee settimanali."],
            ["Fees change 7g", fmt_pct(row.get("fees_change_7d_pct")), "Uso rete in crescita/calo."],
            ["Stablecoin su Solana", fmt_usd(row.get("stablecoins_usd")), "Liquidità stabile disponibile su chain."],
            ["Stablecoin 7g", fmt_pct(row.get("stablecoins_change_7d_pct")), "Entrata/uscita liquidità stabile."],
            ["Supply totale", fmt_number(row.get("sol_total_supply"), 0), "Supply totale convertita da lamports a SOL."],
            ["Supply circolante", fmt_number(row.get("sol_circulating_supply"), 0), "Supply circolante convertita da lamports a SOL."],
            ["SOL in stake", fmt_number(row.get("sol_activated_stake"), 0), "Stake attivo stimato da vote accounts."],
            ["Stake / supply totale", fmt_pct(row.get("sol_stake_ratio_total_pct"), force_sign=False), "Quota supply totale in staking."],
            ["Stake / supply circolante", fmt_pct(row.get("sol_stake_ratio_circulating_pct"), force_sign=False), "Quota supply circolante in staking."],
            ["Stake delinquent", fmt_pct(row.get("sol_delinquent_stake_ratio_pct"), force_sign=False), "Quota stake su validatori delinquent."],
            ["Validatori attivi", fmt_number(row.get("sol_current_validators"), 0), "Validatori correnti letti da RPC."],
            ["Validatori delinquent", fmt_number(row.get("sol_delinquent_validators"), 0), "Validatori delinquent letti da RPC."],
            ["Inflazione stimata", fmt_pct(row.get("sol_inflation_rate_pct"), force_sign=False), "Inflation rate da RPC."],
        ],
    )


def build_optional_table(row):
    return md_table(
        ["Metrica opzionale", "Valore", "Come interpretarla"],
        [
            ["Realized price SOL", fmt_price(row.get("sol_realized_price_usd")), "Costo medio stimato degli holder. Richiede provider esterno."],
            ["MVRV SOL", fmt_number(row.get("sol_mvrv"), 2), "Prezzo rispetto al costo medio. Alto = rischio profit taking."],
            ["Holder in profit", fmt_pct(row.get("sol_holder_profit_pct"), force_sign=False), "Troppi holder in profit possono aumentare prese profitto."],
            ["Holder in loss", fmt_pct(row.get("sol_holder_loss_pct"), force_sign=False), "Molti holder in loss possono indicare fase depressa/accumulo."],
            ["Exchange netflow 24h", fmt_usd(row.get("sol_exchange_netflow_24h_usd")), "Positivo = SOL entra su exchange, negativo = SOL esce dagli exchange."],
        ],
    )


def build_score_table(components):
    if not components:
        return "Nessun componente disponibile."

    rows = []

    for c in components:
        points = c.get("points")
        if points is None:
            points_text = "0"
        elif points > 0:
            points_text = f"+{points}"
        else:
            points_text = str(points)

        rows.append(
            [
                c.get("name"),
                c.get("value"),
                points_text,
                c.get("reason"),
            ]
        )

    return md_table(["Componente", "Valore", "Punti", "Lettura"], rows)


def build_history_table(rows):
    if not rows:
        return "Nessuno storico salvato."

    last_rows = rows[-30:]

    table_rows = []

    for r in last_rows:
        table_rows.append(
            [
                r.get("date"),
                fmt_price(r.get("sol_price_usd")),
                fmt_usd(r.get("chain_tvl_usd")),
                fmt_pct(r.get("chain_tvl_change_7d_pct")),
                fmt_usd(r.get("dex_volume_24h_usd")),
                fmt_pct(r.get("dex_volume_change_7d_pct")),
                fmt_usd(r.get("stablecoins_usd")),
                fmt_pct(r.get("sol_stake_ratio_total_pct"), force_sign=False),
                r.get("onchain_score"),
                r.get("onchain_bias"),
            ]
        )

    return md_table(
        [
            "Data",
            "Prezzo",
            "TVL",
            "TVL 7g",
            "DEX 24h",
            "DEX 7g",
            "Stablecoin",
            "Stake ratio",
            "Score",
            "Bias",
        ],
        table_rows,
    )


def build_markdown_report(row, components, rows):
    rome_now = datetime.now(ZoneInfo("Europe/Rome")).strftime("%Y-%m-%d %H:%M:%S %Z")

    score = row.get("onchain_score")
    bias = row.get("onchain_bias")
    action = row.get("onchain_action")

    lines = []
    lines.append("# SOL on-chain metrics report")
    lines.append("")
    lines.append(f"Generato: **{rome_now}**  ")
    lines.append(f"UTC: **{row.get('generated_at_utc')}**")
    lines.append("")
    lines.append("Questo report aggiunge una lettura on-chain/fondamentale di Solana.")
    lines.append("")
    lines.append("Non sostituisce il frattale SOL/BTC. Serve a capire se dietro il movimento ci sono segnali di rete sani oppure pressione/speculazione.")
    lines.append("")
    lines.append("## Sintesi")
    lines.append("")
    lines.append(
        md_table(
            ["Voce", "Valore"],
            [
                ["Score on-chain", score],
                ["Bias", bias],
                ["Azione coerente", action],
                ["Metriche importanti mancanti", row.get("missing_important_metrics")],
            ],
        )
    )
    lines.append("")
    lines.append("## Componenti del punteggio")
    lines.append("")
    lines.append(build_score_table(components))
    lines.append("")
    lines.append("## Metriche disponibili")
    lines.append("")
    lines.append(build_metric_table(row))
    lines.append("")
    lines.append("## Metriche opzionali: realized price / MVRV / holder profit / exchange flow")
    lines.append("")
    lines.append("Queste metriche sono molto utili, ma spesso richiedono provider esterni. Il file le supporta tramite variabili d'ambiente.")
    lines.append("")
    lines.append(build_optional_table(row))
    lines.append("")
    lines.append("## Variabili opzionali supportate")
    lines.append("")
    lines.append(
        md_table(
            ["Variabile", "Significato"],
            [
                ["SOL_REALIZED_PRICE_USD", "Realized price stimato di SOL."],
                ["SOL_MVRV", "MVRV di SOL."],
                ["SOL_HOLDER_PROFIT_PCT", "% holder/supply in profit."],
                ["SOL_HOLDER_LOSS_PCT", "% holder/supply in loss."],
                ["SOL_EXCHANGE_NETFLOW_24H_USD", "Netflow exchange 24h in USD. Positivo = entra su exchange; negativo = esce."],
                ["SOLANA_RPC_URL", "RPC Solana custom, se non vuoi usare quello pubblico."],
                ["SOL_ONCHAIN_DISABLE_RPC=1", "Disattiva letture Solana RPC."],
            ],
        )
    )
    lines.append("")
    lines.append("## Storico ultimi 30 salvataggi")
    lines.append("")
    lines.append(build_history_table(rows))
    lines.append("")
    lines.append("## Come usarlo insieme al frattale SOL/BTC")
    lines.append("")
    lines.append("- **Frattale positivo + score on-chain positivo**: setup più credibile.")
    lines.append("- **Frattale positivo + on-chain neutrale**: setup ancora valido, ma non confermato dai fondamentali.")
    lines.append("- **Frattale positivo + on-chain negativo**: attenzione, il prezzo può seguire la forma ma avere pressione sotto.")
    lines.append("- **Exchange inflow alto**: rischio prese profitto.")
    lines.append("- **Stablecoin, TVL, fee e DEX volume in crescita**: attività reale più sana.")
    lines.append("- **Stake ratio alto e delinquent basso**: supply liquida più contenuta e rete più stabile.")
    lines.append("")
    lines.append("## Nota importante")
    lines.append("")
    lines.append("Solana non ha un costo di mining come Bitcoin, perché non è Proof-of-Work. Per SOL è più utile guardare staking, attività di rete, liquidità DeFi, stablecoin, DEX volume, fee, MVRV e holder profit/loss.")
    lines.append("")

    return "\n".join(lines)


def build_main_report_block(row):
    return "\n".join(
        [
            START_MARKER,
            "",
            "---",
            "",
            "# SOL on-chain metrics",
            "",
            "Report separato completo: **[sol_onchain_metrics_report.md](sol_onchain_metrics_report.md)**",
            "",
            md_table(
                ["Voce", "Valore"],
                [
                    ["Score on-chain", row.get("onchain_score")],
                    ["Bias", row.get("onchain_bias")],
                    ["Azione coerente", row.get("onchain_action")],
                    ["Prezzo SOL", fmt_price(row.get("sol_price_usd"))],
                    ["TVL Solana", fmt_usd(row.get("chain_tvl_usd"))],
                    ["TVL 7g", fmt_pct(row.get("chain_tvl_change_7d_pct"))],
                    ["DEX volume 24h", fmt_usd(row.get("dex_volume_24h_usd"))],
                    ["Fees 24h", fmt_usd(row.get("fees_24h_usd"))],
                    ["Stablecoin su Solana", fmt_usd(row.get("stablecoins_usd"))],
                    ["Stake ratio", fmt_pct(row.get("sol_stake_ratio_total_pct"), force_sign=False)],
                    ["Metriche mancanti", row.get("missing_important_metrics")],
                ],
            ),
            "",
            "Lettura semplice:",
            "",
            f"**{row.get('onchain_action')}**",
            "",
            "Questo blocco non sostituisce il frattale SOL/BTC: serve come filtro per capire se il movimento è sostenuto anche da attività on-chain.",
            "",
            END_MARKER,
        ]
    )


def inject_into_main_report(row):
    if not os.path.exists(MAIN_REPORT_PATH):
        return

    with open(MAIN_REPORT_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    if START_MARKER in text and END_MARKER in text:
        before = text.split(START_MARKER)[0].rstrip()
        after = text.split(END_MARKER, 1)[1].lstrip()
        text = before + "\n\n" + after

    block = build_main_report_block(row).strip()

    if RSI_END in text:
        pos = text.find(RSI_END) + len(RSI_END)
        new_text = text[:pos].rstrip() + "\n\n" + block + "\n\n" + text[pos:].lstrip()
    elif BTC_SOL_END in text:
        pos = text.find(BTC_SOL_END) + len(BTC_SOL_END)
        new_text = text[:pos].rstrip() + "\n\n" + block + "\n\n" + text[pos:].lstrip()
    elif GLOBAL_END in text:
        pos = text.find(GLOBAL_END) + len(GLOBAL_END)
        new_text = text[:pos].rstrip() + "\n\n" + block + "\n\n" + text[pos:].lstrip()
    else:
        new_text = text.rstrip() + "\n\n" + block + "\n"

    with open(MAIN_REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(new_text.rstrip() + "\n")


def main():
    os.makedirs(REPORT_DIR, exist_ok=True)

    old_rows = load_history()
    row = get_all_metrics()

    previous = latest_previous_row(old_rows, row.get("date"))
    row, components = compute_score(row, previous)

    rows = update_history(row)

    with open(LATEST_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(row, f, indent=2, ensure_ascii=False)

    markdown = build_markdown_report(row, components, rows)

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(markdown)

    inject_into_main_report(row)

    print(f"Wrote {REPORT_PATH}")
    print(f"Wrote {HISTORY_CSV_PATH}")
    print(f"Wrote {LATEST_JSON_PATH}")
    print(f"Updated {MAIN_REPORT_PATH}")
    print(f"SOL on-chain score: {row.get('onchain_score')} / {row.get('onchain_bias')}")


if __name__ == "__main__":
    main()
