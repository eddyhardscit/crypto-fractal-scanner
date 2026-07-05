import os
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
import yfinance as yf


REPORT_DIR = "reports"
MAIN_REPORT_PATH = "reports/latest_report.md"

REPORT_PATH = "reports/btc_2022_vs_sol_2026_report.md"
CSV_PATH = "reports/btc_2022_vs_sol_2026_metrics.csv"

BTC_TICKER = "BTC-USD"
SOL_TICKER = "SOL-USD"

BTC_BOTTOM_SEARCH_START = "2022-11-01"
BTC_BOTTOM_SEARCH_END = "2023-01-31"

SOL_BOTTOM_SEARCH_START = "2026-06-01"

FORECAST_DAYS = [7, 14, 30, 60, 90, 120, 180, 365]


def safe_float(value):
    try:
        if pd.isna(value):
            return None

        value = float(value)

        if np.isnan(value) or np.isinf(value):
            return None

        return value
    except Exception:
        return None


def fmt_number(value, decimals=2):
    value = safe_float(value)

    if value is None:
        return "n/d"

    s = f"{value:,.{decimals}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def fmt_pct(value, decimals=2):
    value = safe_float(value)

    if value is None:
        return "n/d"

    sign = "+" if value > 0 else ""
    return f"{sign}{fmt_number(value, decimals)}%"


def fmt_price(value):
    value = safe_float(value)

    if value is None:
        return "n/d"

    if abs(value) >= 1000:
        return f"{fmt_number(value, 0)} $"

    if abs(value) >= 1:
        return f"{fmt_number(value, 2)} $"

    return f"{fmt_number(value, 5)} $"


def md_table(headers, rows):
    def clean(x):
        return str(x).replace("|", "\\|").replace("\n", " ")

    lines = []
    lines.append("| " + " | ".join(clean(h) for h in headers) + " |")
    lines.append("| " + " | ".join("---" for _ in headers) + " |")

    for row in rows:
        lines.append("| " + " | ".join(clean(cell) for cell in row) + " |")

    return "\n".join(lines)


def download_close(ticker, start):
    df = yf.download(
        ticker,
        start=start,
        interval="1d",
        auto_adjust=True,
        progress=False,
        threads=False,
    )

    if df.empty:
        return pd.DataFrame()

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [c[0] for c in df.columns]

    if "Close" not in df.columns:
        return pd.DataFrame()

    df = df[["Close"]].dropna().copy()
    df.index = pd.to_datetime(df.index)

    if getattr(df.index, "tz", None) is not None:
        df.index = df.index.tz_convert(None)

    df.index = df.index.normalize()

    return df


def rsi(close, period=14):
    close = pd.to_numeric(close, errors="coerce")
    delta = close.diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.ewm(alpha=1 / period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / period, adjust=False).mean()

    rs = avg_gain / avg_loss.replace(0, np.nan)
    out = 100 - (100 / (1 + rs))

    return out


def add_features(df):
    df = df.copy()

    df["rsi_14"] = rsi(df["Close"], 14)

    for ma in [20, 50, 100, 200]:
        df[f"ma_{ma}"] = df["Close"].rolling(ma).mean()
        df[f"dist_ma_{ma}"] = (df["Close"] / df[f"ma_{ma}"] - 1) * 100

    df["log_return"] = np.log(df["Close"] / df["Close"].shift(1))

    return df


def find_low_anchor(df, start, end=None):
    if df.empty:
        return None, None

    if end is None:
        period = df.loc[pd.to_datetime(start):].copy()
    else:
        period = df.loc[pd.to_datetime(start):pd.to_datetime(end)].copy()

    if period.empty:
        period = df.tail(90).copy()

    low_date = period["Close"].idxmin()
    low_price = safe_float(period.loc[low_date, "Close"])

    return low_date, low_price


def normalize_path(df, anchor_date, anchor_price):
    path = df[df.index >= anchor_date].copy()

    if path.empty or anchor_price is None or anchor_price <= 0:
        return pd.DataFrame()

    path["norm"] = path["Close"] / anchor_price * 100
    path["pct_from_anchor"] = (path["Close"] / anchor_price - 1) * 100

    return path


def correlation_similarity(a, b):
    a = pd.to_numeric(pd.Series(a), errors="coerce")
    b = pd.to_numeric(pd.Series(b), errors="coerce")

    valid = pd.concat([a, b], axis=1).dropna()

    if len(valid) < 5:
        return None

    x = valid.iloc[:, 0].values
    y = valid.iloc[:, 1].values

    if np.std(x) == 0 or np.std(y) == 0:
        return None

    corr = np.corrcoef(x, y)[0, 1]

    if np.isnan(corr):
        return None

    return max(0, min(100, (corr + 1) / 2 * 100))


def error_similarity(a, b, tolerance=0.35):
    a = pd.to_numeric(pd.Series(a), errors="coerce")
    b = pd.to_numeric(pd.Series(b), errors="coerce")

    valid = pd.concat([a, b], axis=1).dropna()

    if len(valid) < 5:
        return None

    diff = valid.iloc[:, 0].values - valid.iloc[:, 1].values
    rms = float(np.sqrt(np.mean(diff ** 2)))

    return max(0, min(100, 100 * (1 - rms / tolerance)))


def mean_abs_similarity(a, b, scale):
    a = pd.to_numeric(pd.Series(a), errors="coerce")
    b = pd.to_numeric(pd.Series(b), errors="coerce")

    valid = pd.concat([a, b], axis=1).dropna()

    if len(valid) < 5:
        return None

    mean_abs = float(np.mean(np.abs(valid.iloc[:, 0].values - valid.iloc[:, 1].values)))

    return max(0, min(100, 100 - mean_abs * scale))


def combine_scores(items):
    total_weight = 0
    total_score = 0

    for score, weight in items:
        score = safe_float(score)

        if score is None:
            continue

        total_score += score * weight
        total_weight += weight

    if total_weight == 0:
        return None

    return total_score / total_weight


def quality_label(score):
    score = safe_float(score)

    if score is None:
        return "n/d"

    if score >= 80:
        return "ALTA"
    if score >= 65:
        return "MEDIA"
    if score >= 50:
        return "BASSA / DA CONTROLLARE"

    return "DEBOLE"


def quality_translation(score):
    score = safe_float(score)

    if score is None:
        return "Dati insufficienti."

    if score >= 80:
        return "Il frattale è molto simile: la proiezione BTC 2022 merita attenzione."
    if score >= 65:
        return "Il frattale è abbastanza simile: utile come scenario, ma non come certezza."
    if score >= 50:
        return "Il frattale ha qualche somiglianza, ma va usato con prudenza."
    return "Il frattale non è abbastanza simile: la proiezione è debole."


def compute_similarity(btc_path, sol_path):
    compare_len = min(len(btc_path), len(sol_path))

    if compare_len < 15:
        return {
            "compare_len": compare_len,
            "price_similarity": None,
            "rsi_similarity": None,
            "ma_similarity": None,
            "total_similarity": None,
        }

    btc = btc_path.iloc[:compare_len].copy()
    sol = sol_path.iloc[:compare_len].copy()

    btc_log_norm = np.log(btc["norm"] / 100)
    sol_log_norm = np.log(sol["norm"] / 100)

    price_corr_sim = correlation_similarity(btc_log_norm, sol_log_norm)
    price_error_sim = error_similarity(btc_log_norm, sol_log_norm, tolerance=0.45)

    price_similarity = combine_scores(
        [
            (price_corr_sim, 0.65),
            (price_error_sim, 0.35),
        ]
    )

    rsi_similarity = mean_abs_similarity(
        btc["rsi_14"],
        sol["rsi_14"],
        scale=2.0,
    )

    ma_scores = []

    for ma in [20, 50, 100]:
        col = f"dist_ma_{ma}"

        if col in btc.columns and col in sol.columns:
            ma_scores.append(
                mean_abs_similarity(
                    btc[col],
                    sol[col],
                    scale=2.8,
                )
            )

    ma_similarity = combine_scores([(s, 1) for s in ma_scores])

    total_similarity = combine_scores(
        [
            (price_similarity, 0.60),
            (rsi_similarity, 0.25),
            (ma_similarity, 0.15),
        ]
    )

    return {
        "compare_len": compare_len,
        "price_similarity": price_similarity,
        "rsi_similarity": rsi_similarity,
        "ma_similarity": ma_similarity,
        "total_similarity": total_similarity,
    }


def volatility_beta(btc_path, sol_path, compare_len):
    btc_ret = btc_path["log_return"].iloc[:compare_len].dropna()
    sol_ret = sol_path["log_return"].iloc[:compare_len].dropna()

    if len(btc_ret) < 10 or len(sol_ret) < 10:
        return 1.0

    btc_vol = float(btc_ret.std())
    sol_vol = float(sol_ret.std())

    if btc_vol <= 0:
        return 1.0

    ratio = sol_vol / btc_vol

    return max(0.60, min(2.00, ratio))


def projection_from_btc(btc_path, sol_current_price, sol_elapsed_days, beta_ratio):
    rows = []

    if btc_path.empty or sol_current_price is None:
        return rows

    btc_current_idx = min(sol_elapsed_days, len(btc_path) - 1)
    btc_current_norm = safe_float(btc_path["norm"].iloc[btc_current_idx])

    if btc_current_norm is None or btc_current_norm <= 0:
        return rows

    for horizon in FORECAST_DAYS:
        future_idx = btc_current_idx + horizon

        if future_idx >= len(btc_path):
            continue

        btc_future_norm = safe_float(btc_path["norm"].iloc[future_idx])

        if btc_future_norm is None:
            continue

        future_slice = btc_path["norm"].iloc[btc_current_idx:future_idx + 1]
        relative_slice = future_slice / btc_current_norm

        btc_move_pct = (btc_future_norm / btc_current_norm - 1) * 100

        base_price = sol_current_price * (btc_future_norm / btc_current_norm)

        beta_price = sol_current_price * np.exp(
            np.log(btc_future_norm / btc_current_norm) * beta_ratio
        )

        low_base_price = sol_current_price * relative_slice.min()
        high_base_price = sol_current_price * relative_slice.max()

        low_base_pct = (low_base_price / sol_current_price - 1) * 100
        high_base_pct = (high_base_price / sol_current_price - 1) * 100

        rows.append(
            {
                "horizon_days": horizon,
                "btc_equivalent_future_date": str(btc_path.index[future_idx].date()),
                "btc_move_from_equivalent_today_pct": btc_move_pct,
                "sol_projection_base_price": base_price,
                "sol_projection_beta_price": beta_price,
                "sol_path_low_base_price": low_base_price,
                "sol_path_low_base_pct": low_base_pct,
                "sol_path_high_base_price": high_base_price,
                "sol_path_high_base_pct": high_base_pct,
            }
        )

    return rows


def build_projection_table(projections):
    rows = []

    for p in projections:
        rows.append(
            [
                f"{p['horizon_days']} giorni",
                p["btc_equivalent_future_date"],
                fmt_pct(p["btc_move_from_equivalent_today_pct"]),
                fmt_price(p["sol_projection_base_price"]),
                fmt_price(p["sol_projection_beta_price"]),
                fmt_price(p["sol_path_low_base_price"]),
                fmt_pct(p["sol_path_low_base_pct"]),
                fmt_price(p["sol_path_high_base_price"]),
                fmt_pct(p["sol_path_high_base_pct"]),
            ]
        )

    return md_table(
        [
            "Orizzonte",
            "Data BTC equivalente",
            "BTC fece",
            "SOL base",
            "SOL beta",
            "Min percorso",
            "Min %",
            "Max percorso",
            "Max %",
        ],
        rows,
    )


def build_summary_rows(btc_anchor_date, btc_anchor_price, sol_anchor_date, sol_anchor_price, sol_current_price, sol_elapsed_days, similarity, beta_ratio):
    return [
        ["BTC bottom usato", str(btc_anchor_date.date()), fmt_price(btc_anchor_price)],
        ["SOL bottom usato", str(sol_anchor_date.date()), fmt_price(sol_anchor_price)],
        ["Prezzo SOL attuale", "-", fmt_price(sol_current_price)],
        ["Giorni SOL dal bottom", "-", sol_elapsed_days],
        ["Giorni confrontati", "-", similarity.get("compare_len")],
        ["Somiglianza prezzo", "-", fmt_pct(similarity.get("price_similarity"))],
        ["Somiglianza RSI", "-", fmt_pct(similarity.get("rsi_similarity"))],
        ["Somiglianza medie", "-", fmt_pct(similarity.get("ma_similarity"))],
        ["Somiglianza totale", "-", fmt_pct(similarity.get("total_similarity"))],
        ["Qualità frattale", "-", quality_label(similarity.get("total_similarity"))],
        ["Beta volatilità SOL/BTC", "-", fmt_number(beta_ratio, 2)],
    ]


def build_report(btc_anchor_date, btc_anchor_price, sol_anchor_date, sol_anchor_price, sol_current_price, sol_elapsed_days, btc_equiv_date, similarity, beta_ratio, projections):
    rome_now = datetime.now(ZoneInfo("Europe/Rome")).strftime("%Y-%m-%d %H:%M:%S %Z")
    utc_now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    score = similarity.get("total_similarity")

    lines = []

    lines.append("# Frattale mirato: BTC novembre 2022 vs SOL giugno 2026")
    lines.append("")
    lines.append(f"Generato: **{rome_now}**  ")
    lines.append(f"UTC: **{utc_now}**")
    lines.append("")
    lines.append("Questo report confronta una sola ipotesi:")
    lines.append("")
    lines.append("> SOL sta seguendo il frattale di Bitcoin dopo il bottom di novembre 2022?")
    lines.append("")
    lines.append("Il report non cerca 40 casi storici. Confronta proprio:")
    lines.append("")
    lines.append("- **BTC dal bottom novembre 2022**")
    lines.append("- **SOL dal bottom giugno 2026**")
    lines.append("")
    lines.append("## Risposta veloce")
    lines.append("")
    lines.append(f"- **Somiglianza totale:** {fmt_pct(score)}")
    lines.append(f"- **Qualità frattale:** {quality_label(score)}")
    lines.append(f"- **Lettura:** {quality_translation(score)}")
    lines.append("")
    lines.append(f"SOL oggi è circa al giorno **{sol_elapsed_days}** dal suo bottom. Nel frattale BTC, il giorno equivalente era circa **{btc_equiv_date.date()}**.")
    lines.append("")
    lines.append("## Dati base")
    lines.append("")
    lines.append(
        md_table(
            ["Voce", "Data", "Valore"],
            build_summary_rows(
                btc_anchor_date,
                btc_anchor_price,
                sol_anchor_date,
                sol_anchor_price,
                sol_current_price,
                sol_elapsed_days,
                similarity,
                beta_ratio,
            ),
        )
    )
    lines.append("")
    lines.append("## Proiezione SOL se continua a seguire BTC 2022")
    lines.append("")
    lines.append("Ci sono due prezzi:")
    lines.append("")
    lines.append("- **SOL base**: SOL replica la percentuale di BTC.")
    lines.append("- **SOL beta**: SOL replica BTC ma con volatilità SOL/BTC. È più aggressivo se SOL si muove più forte di BTC.")
    lines.append("")
    lines.append(build_projection_table(projections))
    lines.append("")
    lines.append("## Come leggerlo semplice")
    lines.append("")
    lines.append("- Se la somiglianza è alta, la proiezione merita attenzione.")
    lines.append("- Se la somiglianza è media, la proiezione è uno scenario possibile, non una guida cieca.")
    lines.append("- Se la somiglianza è bassa, il frattale BTC non sta descrivendo bene SOL.")
    lines.append("")
    lines.append("La colonna **Min percorso** è importante: dice quanto potrebbe scendere prima di arrivare al prezzo proiettato.")
    lines.append("")
    lines.append("La colonna **Max percorso** dice quale zona alta BTC avrebbe raggiunto nello stesso tratto temporale.")
    lines.append("")
    lines.append("## Nota pratica")
    lines.append("")
    lines.append("Questo report serve soprattutto per la tua ipotesi:")
    lines.append("")
    lines.append("> comprare SOL su retest e tenerlo se sta davvero seguendo il cambio trend di BTC post-bottom 2022.")
    lines.append("")
    lines.append("Se il frattale resta simile e SOL tiene le zone basse, allora le proiezioni diventano più interessanti.")
    lines.append("")
    lines.append("Se invece la somiglianza crolla nei prossimi giorni, il paragone con BTC 2022 perde valore.")
    lines.append("")

    return "\n".join(lines)


def build_main_report_block(similarity, sol_elapsed_days, btc_equiv_date, projections):
    score = similarity.get("total_similarity")

    quick_rows = []

    for p in projections:
        if p["horizon_days"] in [30, 60, 90, 120, 180]:
            quick_rows.append(
                [
                    f"{p['horizon_days']} giorni",
                    fmt_pct(p["btc_move_from_equivalent_today_pct"]),
                    fmt_price(p["sol_projection_base_price"]),
                    fmt_price(p["sol_projection_beta_price"]),
                    fmt_price(p["sol_path_low_base_price"]),
                    fmt_price(p["sol_path_high_base_price"]),
                ]
            )

    return "\n".join(
        [
            "<!-- BTC_SOL_FRACTAL_START -->",
            "",
            "---",
            "",
            "# Frattale mirato: BTC 2022 vs SOL 2026",
            "",
            "Report separato completo: [btc_2022_vs_sol_2026_report.md](btc_2022_vs_sol_2026_report.md)",
            "",
            f"- **Somiglianza totale:** {fmt_pct(score)}",
            f"- **Qualità:** {quality_label(score)}",
            f"- **Lettura:** {quality_translation(score)}",
            f"- **SOL è al giorno:** {sol_elapsed_days} dal bottom usato.",
            f"- **Giorno BTC equivalente:** {btc_equiv_date.date()}",
            "",
            "## Proiezione veloce se SOL segue BTC 2022",
            "",
            md_table(
                [
                    "Orizzonte",
                    "BTC fece",
                    "SOL base",
                    "SOL beta",
                    "Min percorso",
                    "Max percorso",
                ],
                quick_rows,
            ),
            "",
            "Nota: questa è una proiezione analogica, non una certezza. Serve a vedere se l'idea 75–77 → 100–105 ha coerenza col frattale BTC post-bottom.",
            "",
            "<!-- BTC_SOL_FRACTAL_END -->",
        ]
    )


def inject_into_main_report(similarity, sol_elapsed_days, btc_equiv_date, projections):
    if not os.path.exists(MAIN_REPORT_PATH):
        return

    with open(MAIN_REPORT_PATH, "r", encoding="utf-8") as f:
        current = f.read()

    start_marker = "<!-- BTC_SOL_FRACTAL_START -->"
    end_marker = "<!-- BTC_SOL_FRACTAL_END -->"

    if start_marker in current and end_marker in current:
        before = current.split(start_marker)[0].rstrip()
        after = current.split(end_marker, 1)[1].lstrip()
        current = before + "\n\n" + after

    block = build_main_report_block(
        similarity=similarity,
        sol_elapsed_days=sol_elapsed_days,
        btc_equiv_date=btc_equiv_date,
        projections=projections,
    ).strip()

    decision_end = "<!-- DECISION_REPORT_END -->"

    if decision_end in current:
        insert_pos = current.find(decision_end) + len(decision_end)
        new_text = (
            current[:insert_pos].rstrip()
            + "\n\n"
            + block
            + "\n\n"
            + current[insert_pos:].lstrip()
        )
    else:
        new_text = block + "\n\n" + current.lstrip()

    with open(MAIN_REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(new_text.rstrip() + "\n")


def write_csv(summary_dict, projections):
    rows = []

    base = dict(summary_dict)
    base["row_type"] = "summary"
    rows.append(base)

    for p in projections:
        row = dict(p)
        row["row_type"] = "projection"
        rows.append(row)

    df = pd.DataFrame(rows)
    df.to_csv(CSV_PATH, index=False)


def main():
    os.makedirs(REPORT_DIR, exist_ok=True)

    btc = download_close(BTC_TICKER, start="2022-01-01")
    sol = download_close(SOL_TICKER, start="2026-01-01")

    if btc.empty or sol.empty:
        report = "# Frattale BTC 2022 vs SOL 2026\n\nDati insufficienti da Yahoo Finance.\n"

        with open(REPORT_PATH, "w", encoding="utf-8") as f:
            f.write(report)

        print("Insufficient data.")
        return

    btc = add_features(btc)
    sol = add_features(sol)

    btc_anchor_date, btc_anchor_price = find_low_anchor(
        btc,
        BTC_BOTTOM_SEARCH_START,
        BTC_BOTTOM_SEARCH_END,
    )

    sol_anchor_date, sol_anchor_price = find_low_anchor(
        sol,
        SOL_BOTTOM_SEARCH_START,
        None,
    )

    if btc_anchor_date is None or sol_anchor_date is None:
        report = "# Frattale BTC 2022 vs SOL 2026\n\nAnchor non trovati.\n"

        with open(REPORT_PATH, "w", encoding="utf-8") as f:
            f.write(report)

        print("Anchors not found.")
        return

    btc_path = normalize_path(btc, btc_anchor_date, btc_anchor_price)
    sol_path = normalize_path(sol, sol_anchor_date, sol_anchor_price)

    if btc_path.empty or sol_path.empty:
        report = "# Frattale BTC 2022 vs SOL 2026\n\nPercorsi non disponibili.\n"

        with open(REPORT_PATH, "w", encoding="utf-8") as f:
            f.write(report)

        print("Paths unavailable.")
        return

    sol_current_price = safe_float(sol_path["Close"].iloc[-1])
    sol_elapsed_days = len(sol_path) - 1

    btc_equiv_idx = min(sol_elapsed_days, len(btc_path) - 1)
    btc_equiv_date = btc_path.index[btc_equiv_idx]

    similarity = compute_similarity(btc_path, sol_path)
    compare_len = similarity.get("compare_len") or min(len(btc_path), len(sol_path))
    beta_ratio = volatility_beta(btc_path, sol_path, compare_len)

    projections = projection_from_btc(
        btc_path=btc_path,
        sol_current_price=sol_current_price,
        sol_elapsed_days=sol_elapsed_days,
        beta_ratio=beta_ratio,
    )

    report = build_report(
        btc_anchor_date=btc_anchor_date,
        btc_anchor_price=btc_anchor_price,
        sol_anchor_date=sol_anchor_date,
        sol_anchor_price=sol_anchor_price,
        sol_current_price=sol_current_price,
        sol_elapsed_days=sol_elapsed_days,
        btc_equiv_date=btc_equiv_date,
        similarity=similarity,
        beta_ratio=beta_ratio,
        projections=projections,
    )

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report)

    summary_dict = {
        "btc_anchor_date": str(btc_anchor_date.date()),
        "btc_anchor_price": btc_anchor_price,
        "sol_anchor_date": str(sol_anchor_date.date()),
        "sol_anchor_price": sol_anchor_price,
        "sol_current_price": sol_current_price,
        "sol_elapsed_days": sol_elapsed_days,
        "btc_equivalent_date": str(btc_equiv_date.date()),
        "price_similarity": similarity.get("price_similarity"),
        "rsi_similarity": similarity.get("rsi_similarity"),
        "ma_similarity": similarity.get("ma_similarity"),
        "total_similarity": similarity.get("total_similarity"),
        "quality_label": quality_label(similarity.get("total_similarity")),
        "beta_ratio": beta_ratio,
    }

    write_csv(summary_dict, projections)

    inject_into_main_report(
        similarity=similarity,
        sol_elapsed_days=sol_elapsed_days,
        btc_equiv_date=btc_equiv_date,
        projections=projections,
    )

    print(f"Wrote {REPORT_PATH}")
    print(f"Wrote {CSV_PATH}")
    print(f"Updated {MAIN_REPORT_PATH}")


if __name__ == "__main__":
    main()
