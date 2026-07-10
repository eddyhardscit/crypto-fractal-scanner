from datetime import datetime, timezone
from pathlib import Path
import math

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf


REPORTS = Path("reports")
MATCHES = REPORTS / "latest_scanner_matches.csv"
LATEST = REPORTS / "latest_report.md"
REPORT = REPORTS / "extreme_cases_path_report.md"
METRICS = REPORTS / "extreme_cases_path_metrics.csv"
CASES = REPORTS / "extreme_cases_path_cases.csv"

START = "<!-- EXTREME_CASES_PATH_START -->"
END = "<!-- EXTREME_CASES_PATH_END -->"

THRESHOLD = 80.0
HORIZON = 30
ASSETS = ["BTC", "SOL", "DOGE"]


def sf(x):
    try:
        x = float(x)
        return x if np.isfinite(x) else np.nan
    except Exception:
        return np.nan


def fp(x):
    x = sf(x)
    return "n/a" if np.isnan(x) else f"{x:+.2f}%".replace(".", ",")


def fm(x, d=0):
    x = sf(x)
    return "n/a" if np.isnan(x) else f"{x:.{d}f}".replace(".", ",")


def md(df):
    return "_Nessun dato._" if df.empty else df.to_markdown(index=False)


def read_matches():
    if not MATCHES.exists():
        return pd.DataFrame()

    df = pd.read_csv(MATCHES)

    for c in [
        "similarity",
        "return_30d",
        "drawdown_30d",
        "max_gain_30d",
        "match_rank",
    ]:
        if c in df:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    df["target_asset"] = (
        df["target_asset"]
        .astype(str)
        .str.upper()
        .str.replace("-USD", "", regex=False)
    )

    df["similar_asset"] = df["similar_asset"].astype(str).str.upper()
    df["start_date"] = pd.to_datetime(df["start_date"], errors="coerce")
    df["end_date"] = pd.to_datetime(df["end_date"], errors="coerce")

    return df.dropna(
        subset=[
            "target_asset",
            "similar_asset",
            "end_date",
            "return_30d",
        ]
    ).copy()


def trigger_info(g):
    if g.empty:
        return "NESSUNO", False, np.nan, "Nessun match"

    pos = (g["return_30d"] > 0).mean() * 100
    neg = (g["return_30d"] < 0).mean() * 100

    if pos >= THRESHOLD:
        return (
            "POSITIVO / RIALZISTA",
            True,
            pos,
            f"Casi positivi {pos:.2f}% >= {THRESHOLD:.0f}%",
        )

    if neg >= THRESHOLD:
        return (
            "NEGATIVO / RIBASSISTA",
            True,
            neg,
            f"Casi negativi {neg:.2f}% >= {THRESHOLD:.0f}%",
        )

    return (
        "NESSUNO",
        False,
        max(pos, neg),
        "Nessun lato sopra soglia estrema",
    )


def norm(df):
    if df is None or df.empty:
        return pd.DataFrame()

    out = df.copy()

    if isinstance(out.columns, pd.MultiIndex):
        out.columns = [c[0] for c in out.columns]

    if "Close" not in out:
        return pd.DataFrame()

    out.index = pd.to_datetime(out.index)

    try:
        out.index = out.index.tz_localize(None)
    except TypeError:
        pass

    return out[
        ~out.index.duplicated(keep="last")
    ].sort_index()


def load_prices(tickers, start, end):
    prices = {}

    for t in sorted(set(tickers)):
        try:
            df = yf.download(
                t,
                start=(
                    pd.Timestamp(start) - pd.Timedelta(days=7)
                ).strftime("%Y-%m-%d"),
                end=(
                    pd.Timestamp(end)
                    + pd.Timedelta(days=HORIZON + 10)
                ).strftime("%Y-%m-%d"),
                interval="1d",
                auto_adjust=False,
                progress=False,
                threads=False,
            )

            df = norm(df)

            if not df.empty:
                prices[t] = df

        except Exception:
            pass

    return prices


def build_case(row, prices):
    t = row["similar_asset"]

    if t not in prices:
        return None, None

    df = prices[t]
    end_date = pd.Timestamp(row["end_date"]).normalize()

    eligible = df.index[df.index <= end_date]

    if len(eligible) == 0:
        return None, None

    anchor = eligible[-1]
    pos = df.index.get_loc(anchor)

    if not isinstance(pos, (int, np.integer)):
        return None, None

    close = pd.to_numeric(
        df.iloc[pos:pos + HORIZON + 1]["Close"],
        errors="coerce",
    ).dropna()

    if len(close) < 2:
        return None, None

    base = sf(close.iloc[0])

    if np.isnan(base) or base <= 0:
        return None, None

    r = ((close / base) - 1) * 100

    path = pd.Series(
        index=range(HORIZON + 1),
        dtype=float,
    )

    path.iloc[:len(r)] = r.values
    path = path.interpolate(limit_direction="forward")

    max_gain = sf(path.max())
    max_day = int(path.idxmax())

    min_ret = sf(path.min())
    min_day = int(path.idxmin())

    final_ret = sf(path.iloc[-1])

    # Massimo rialzo raggiunto prima del minimo principale.
    before_low = path.loc[:min_day]
    spike = sf(before_low.max())
    spike_day = int(before_low.idxmax())

    # Minimo successivo allo spike.
    after_peak = path.loc[spike_day:]
    post_low = sf(after_peak.min())
    post_low_day = int(after_peak.idxmin())

    # Calo reale dal picco al minimo successivo.
    peak_factor = 1 + spike / 100
    low_factor = 1 + post_low / 100

    dump_from_peak = (
        (low_factor / peak_factor - 1) * 100
        if peak_factor > 0
        else np.nan
    )

    if (
        spike >= 8
        and min_ret <= -10
        and spike_day < min_day
    ):
        sequence = "SPIKE PRIMA DEL DUMP"

    elif (
        spike >= 3
        and min_ret <= -10
        and spike_day < min_day
    ):
        sequence = "RIALZO MODESTO PRIMA DEL DUMP"

    elif min_day <= 5 and spike < 3:
        sequence = "DISCESA QUASI IMMEDIATA"

    elif final_ret < 0:
        sequence = "PERCORSO RIBASSISTA MISTO"

    else:
        sequence = "ECCEZIONE POSITIVA"

    rec = {
        "target_asset": row["target_asset"],
        "similar_asset": t,
        "end_date": end_date.date().isoformat(),
        "similarity": sf(row.get("similarity")),
        "return_30d": final_ret,
        "drawdown_30d": min_ret,
        "max_gain_30d": max_gain,
        "spike_before_low_pct": spike,
        "spike_day": spike_day,
        "low_day": min_day,
        "post_peak_low_pct": post_low,
        "post_peak_low_day": post_low_day,
        "dump_from_peak_pct": dump_from_peak,
        "sequence": sequence,
    }

    return rec, path.to_numpy(dtype=float)


def plot_bands(asset, matrix, out):
    x = np.arange(matrix.shape[1])

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.fill_between(
        x,
        np.nanpercentile(matrix, 10, axis=0),
        np.nanpercentile(matrix, 90, axis=0),
        alpha=.18,
        label="p10-p90",
    )

    ax.fill_between(
        x,
        np.nanpercentile(matrix, 25, axis=0),
        np.nanpercentile(matrix, 75, axis=0),
        alpha=.30,
        label="p25-p75",
    )

    ax.plot(
        x,
        np.nanmedian(matrix, axis=0),
        linewidth=3,
        label="Mediana",
    )

    ax.plot(
        x,
        np.nanmean(matrix, axis=0),
        linewidth=2,
        linestyle="--",
        label="Media",
    )

    ax.axhline(
        0,
        linewidth=1,
        linestyle=":",
    )

    for d in [7, 14, 30]:
        ax.axvline(
            d,
            linewidth=.8,
            linestyle=":",
        )

    ax.set_title(
        f"{asset} — percorso pulito dei casi estremi"
    )

    ax.set_xlabel("Giorni dopo il match")
    ax.set_ylabel("Return dal giorno 0 (%)")
    ax.grid(alpha=.2)
    ax.legend()

    fig.tight_layout()
    fig.savefig(out, dpi=160)
    plt.close(fig)


def plot_asset_lines(asset, cases, matrix, out):
    tmp = cases.reset_index(drop=True).copy()
    medians = {}

    for t, g in tmp.groupby("similar_asset"):
        medians[t] = np.nanmedian(
            matrix[g.index.to_list()],
            axis=0,
        )

    ranked = sorted(
        medians,
        key=lambda t: (
            tmp[tmp["similar_asset"] == t].shape[0],
            tmp.loc[
                tmp["similar_asset"] == t,
                "similarity",
            ].max(),
        ),
        reverse=True,
    )

    keep = ranked[:18]
    rest = ranked[18:]

    fig, ax = plt.subplots(figsize=(12, 7))

    for t in keep:
        ax.plot(
            range(HORIZON + 1),
            medians[t],
            linewidth=1.7,
            label=t.replace("-USD", ""),
        )

    if rest:
        other = np.nanmedian(
            np.vstack([medians[t] for t in rest]),
            axis=0,
        )

        ax.plot(
            range(HORIZON + 1),
            other,
            linewidth=2.6,
            linestyle="--",
            label="ALTRI aggregati",
        )

    ax.plot(
        range(HORIZON + 1),
        np.nanmedian(matrix, axis=0),
        linewidth=3.4,
        label="MEDIANA totale",
    )

    ax.axhline(
        0,
        linewidth=1,
        linestyle=":",
    )

    for d in [7, 14, 30]:
        ax.axvline(
            d,
            linewidth=.8,
            linestyle=":",
        )

    ax.set_title(
        f"{asset} — linee colorate per asset storico"
    )

    ax.set_xlabel("Giorni dopo il match")
    ax.set_ylabel("Return dal giorno 0 (%)")
    ax.grid(alpha=.2)

    ax.legend(
        bbox_to_anchor=(1.02, 1),
        loc="upper left",
        fontsize=8,
    )

    fig.tight_layout()
    fig.savefig(
        out,
        dpi=160,
        bbox_inches="tight",
    )

    plt.close(fig)


def plot_spikes(asset, cases, out):
    g = cases.sort_values(
        [
            "spike_before_low_pct",
            "similarity",
        ],
        ascending=[
            False,
            False,
        ],
    ).copy()

    labels = [
        f"{r.similar_asset.replace('-USD', '')}\n{r.end_date}"
        for r in g.itertuples()
    ]

    vals = g["spike_before_low_pct"].to_numpy()

    fig, ax = plt.subplots(
        figsize=(
            max(12, len(g) * .36),
            6.5,
        )
    )

    bars = ax.bar(
        range(len(vals)),
        vals,
    )

    for bar, day, val in zip(
        bars,
        g["spike_day"],
        vals,
    ):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            val + .25,
            f"g{int(day)}",
            ha="center",
            va="bottom",
            fontsize=7,
            rotation=90,
        )

    ax.axhline(
        5,
        linestyle=":",
        linewidth=1.2,
        label="+5%",
    )

    ax.axhline(
        10,
        linestyle="--",
        linewidth=1.2,
        label="+10%",
    )

    ax.set_xticks(range(len(labels)))

    ax.set_xticklabels(
        labels,
        rotation=75,
        ha="right",
        fontsize=7,
    )

    ax.set_ylabel(
        "Massimo rialzo prima del minimo (%)"
    )

    ax.set_title(
        f"{asset} — spike massimo prima della discesa principale"
    )

    ax.grid(
        axis="y",
        alpha=.2,
    )

    ax.legend()

    fig.tight_layout()

    fig.savefig(
        out,
        dpi=160,
        bbox_inches="tight",
    )

    plt.close(fig)


def plot_spike_vs_low(asset, cases, out):
    fig, ax = plt.subplots(
        figsize=(9.5, 6.5)
    )

    ax.scatter(
        cases["spike_before_low_pct"],
        cases["drawdown_30d"],
        s=60,
        alpha=.8,
    )

    for r in cases.itertuples():
        ax.annotate(
            r.similar_asset.replace("-USD", ""),
            (
                r.spike_before_low_pct,
                r.drawdown_30d,
            ),
            fontsize=7,
            xytext=(3, 3),
            textcoords="offset points",
        )

    ax.axvline(
        5,
        linestyle=":",
        linewidth=1,
    )

    ax.axvline(
        10,
        linestyle="--",
        linewidth=1,
    )

    ax.axhline(
        -10,
        linestyle=":",
        linewidth=1,
    )

    ax.axhline(
        -20,
        linestyle="--",
        linewidth=1,
    )

    ax.set_xlabel(
        "Rialzo massimo prima del minimo (%)"
    )

    ax.set_ylabel(
        "Minimo raggiunto nei 30 giorni (%)"
    )

    ax.set_title(
        f"{asset} — quanto è salito prima e quanto è sceso dopo"
    )

    ax.grid(alpha=.2)

    fig.tight_layout()
    fig.savefig(out, dpi=160)
    plt.close(fig)


def plot_ranked(asset, cases, out):
    g = cases.sort_values("return_30d")

    labels = [
        f"{r.similar_asset.replace('-USD', '')}\n{r.end_date}"
        for r in g.itertuples()
    ]

    vals = g["return_30d"].to_numpy()

    fig, ax = plt.subplots(
        figsize=(
            max(12, len(g) * .34),
            6.5,
        )
    )

    ax.bar(
        range(len(vals)),
        vals,
    )

    ax.axhline(
        np.nanmedian(vals),
        linestyle="--",
        label="Mediana",
    )

    ax.axhline(
        np.nanmean(vals),
        linestyle=":",
        label="Media",
    )

    ax.set_xticks(range(len(labels)))

    ax.set_xticklabels(
        labels,
        rotation=75,
        ha="right",
        fontsize=7,
    )

    ax.set_ylabel(
        "Return 30 giorni (%)"
    )

    ax.set_title(
        f"{asset} — return 30g ordinato"
    )

    ax.grid(
        axis="y",
        alpha=.2,
    )

    ax.legend()

    fig.tight_layout()

    fig.savefig(
        out,
        dpi=160,
        bbox_inches="tight",
    )

    plt.close(fig)


def inject(section):
    if not LATEST.exists():
        return

    old = LATEST.read_text(
        encoding="utf-8"
    )

    block = (
        START
        + "\n"
        + section.strip()
        + "\n"
        + END
    )

    if START in old and END in old:
        a = old.find(START)
        b = old.find(END) + len(END)

        new = (
            old[:a]
            + block
            + old[b:]
        )

    else:
        anchor = (
            "<!-- SCANNER_FORECAST_TRACKER_END -->"
        )

        if anchor in old:
            p = (
                old.find(anchor)
                + len(anchor)
            )

            new = (
                old[:p]
                + "\n\n"
                + block
                + old[p:]
            )

        else:
            new = (
                old.rstrip()
                + "\n\n"
                + block
                + "\n"
            )

    LATEST.write_text(
        new,
        encoding="utf-8",
    )


def main():
    REPORTS.mkdir(exist_ok=True)

    df = read_matches()

    lines = [
        "# Extreme cases path report",
        "",
        (
            "Generato: "
            + datetime.now(timezone.utc).strftime(
                "%Y-%m-%d %H:%M UTC"
            )
        ),
        "",
        (
            "Questo report si attiva quando i casi "
            f"positivi o negativi sono almeno **{THRESHOLD:.0f}%**."
        ),
        "",
        (
            "Ora misura anche il **rialzo massimo prima "
            "della discesa principale**, quindi distingue "
            "uno spike iniziale da una discesa quasi immediata."
        ),
        "",
    ]

    if df.empty:
        lines += [
            (
                "Nessun match disponibile. "
                "Esegui prima `scanner.py`."
            )
        ]

        text = "\n".join(lines)

        REPORT.write_text(
            text + "\n",
            encoding="utf-8",
        )

        inject(text)
        return

    trigger_rows = []
    info = {}

    for asset in ASSETS:
        g = df[
            df["target_asset"] == asset
        ]

        direction, active, pct, reason = trigger_info(g)

        info[asset] = (
            direction,
            active,
            pct,
            reason,
        )

        trigger_rows.append({
            "Asset": asset,
            "Direzione": direction,
            "Trigger": "SI" if active else "NO",
            "Percentuale": fp(pct),
            "Motivo": reason,
            "Match disponibili": len(g),
        })

    lines += [
        "## Trigger estremi",
        "",
        md(pd.DataFrame(trigger_rows)),
        "",
    ]

    all_cases = []
    metric_rows = []

    for asset in ASSETS:
        direction, active, pct, reason = info[asset]

        if not active:
            continue

        g = df[
            df["target_asset"] == asset
        ].copy()

        if direction.startswith("POSITIVO"):
            selected = g[
                g["return_30d"] > 0
            ]
        else:
            selected = g[
                g["return_30d"] < 0
            ]

        prices = load_prices(
            selected["similar_asset"],
            selected["end_date"].min(),
            selected["end_date"].max(),
        )

        records = []
        paths = []

        for _, row in selected.sort_values(
            "similarity",
            ascending=False,
        ).iterrows():

            rec, path = build_case(
                row,
                prices,
            )

            if rec is not None:
                records.append(rec)
                paths.append(path)

        cases = pd.DataFrame(records)

        if cases.empty:
            lines += [
                f"## {asset}",
                "",
                (
                    "Trigger presente, ma percorsi "
                    "non ricostruibili."
                ),
                "",
            ]
            continue

        matrix = np.vstack(paths)
        all_cases.append(cases)

        base = (
            "positive"
            if direction.startswith("POSITIVO")
            else "negative"
        )

        f_bands = REPORTS / (
            f"extreme_cases_{asset}_{base}_clean_bands.png"
        )

        f_lines = REPORTS / (
            f"extreme_cases_{asset}_{base}_asset_medians.png"
        )

        f_spike = REPORTS / (
            f"extreme_cases_{asset}_{base}_spike_before_dump.png"
        )

        f_scatter = REPORTS / (
            f"extreme_cases_{asset}_{base}_spike_vs_low.png"
        )

        f_ranked = REPORTS / (
            f"extreme_cases_{asset}_{base}_ranked_returns.png"
        )

        plot_bands(
            asset,
            matrix,
            f_bands,
        )

        plot_asset_lines(
            asset,
            cases,
            matrix,
            f_lines,
        )

        plot_spikes(
            asset,
            cases,
            f_spike,
        )

        plot_spike_vs_low(
            asset,
            cases,
            f_scatter,
        )

        plot_ranked(
            asset,
            cases,
            f_ranked,
        )

        med_spike = (
            cases["spike_before_low_pct"].median()
        )

        mean_spike = (
            cases["spike_before_low_pct"].mean()
        )

        p75_spike = (
            cases["spike_before_low_pct"].quantile(.75)
        )

        med_spike_day = (
            cases["spike_day"].median()
        )

        med_low_day = (
            cases["low_day"].median()
        )

        med_dump = (
            cases["dump_from_peak_pct"].median()
        )

        rate5 = (
            cases["spike_before_low_pct"] >= 5
        ).mean() * 100

        rate10 = (
            cases["spike_before_low_pct"] >= 10
        ).mean() * 100

        rate15 = (
            cases["spike_before_low_pct"] >= 15
        ).mean() * 100

        immediate = (
            (
                cases["low_day"] <= 5
            )
            &
            (
                cases["spike_before_low_pct"] < 3
            )
        ).mean() * 100

        metric_rows.append({
            "asset": asset,
            "direction": direction,
            "trigger_pct": pct,
            "cases_used": len(cases),
            "median_spike_before_low_pct": med_spike,
            "mean_spike_before_low_pct": mean_spike,
            "p75_spike_before_low_pct": p75_spike,
            "median_spike_day": med_spike_day,
            "median_low_day": med_low_day,
            "median_dump_from_peak_pct": med_dump,
            "spike_5_rate": rate5,
            "spike_10_rate": rate10,
            "spike_15_rate": rate15,
            "immediate_drop_rate": immediate,
        })

        p = np.nanpercentile(
            cases["return_30d"],
            [10, 25, 50, 75, 90],
        )

        spike_table = cases.sort_values(
            [
                "spike_before_low_pct",
                "similarity",
            ],
            ascending=[
                False,
                False,
            ],
        ).head(20)[[
            "similar_asset",
            "end_date",
            "similarity",
            "spike_before_low_pct",
            "spike_day",
            "drawdown_30d",
            "low_day",
            "dump_from_peak_pct",
            "return_30d",
            "sequence",
        ]].copy()

        spike_table.columns = [
            "Asset storico",
            "End",
            "Similarity",
            "Spike prima del minimo",
            "Giorno spike",
            "Minimo 30g",
            "Giorno minimo",
            "Dump dal picco",
            "Return 30g",
            "Sequenza",
        ]

        for c in [
            "Similarity",
            "Spike prima del minimo",
            "Minimo 30g",
            "Dump dal picco",
            "Return 30g",
        ]:
            spike_table[c] = (
                spike_table[c].map(fp)
            )

        lines += [
            (
                f"## {asset} — "
                + (
                    "casi rialzisti"
                    if direction.startswith("POSITIVO")
                    else "casi ribassisti"
                )
            ),
            "",
            f"- Trigger: **{reason}**",
            (
                "- Casi usati nei grafici: "
                f"**{len(cases)}**"
            ),
            (
                "- Return mediano 7g: "
                f"**{fp(np.nanmedian(matrix[:, 7]))}**"
            ),
            (
                "- Return mediano 14g: "
                f"**{fp(np.nanmedian(matrix[:, 14]))}**"
            ),
            (
                "- Return mediano 30g: "
                f"**{fp(np.nanmedian(matrix[:, 30]))}**"
            ),
            (
                "- Drawdown mediano: "
                f"**{fp(cases['drawdown_30d'].median())}**"
            ),
            (
                "- Max gain mediano: "
                f"**{fp(cases['max_gain_30d'].median())}**"
            ),
            "",
            "### Quanto salivano prima di scendere",
            "",
            (
                "- Spike massimo mediano prima del minimo: "
                f"**{fp(med_spike)}**"
            ),
            (
                "- Spike massimo medio prima del minimo: "
                f"**{fp(mean_spike)}**"
            ),
            (
                "- Spike p75 prima del minimo: "
                f"**{fp(p75_spike)}**"
            ),
            (
                "- Giorno mediano dello spike: "
                f"**giorno {fm(med_spike_day)}**"
            ),
            (
                "- Giorno mediano del minimo: "
                f"**giorno {fm(med_low_day)}**"
            ),
            (
                "- Scarico mediano dal picco al minimo: "
                f"**{fp(med_dump)}**"
            ),
            (
                "- Casi con almeno +5% prima del minimo: "
                f"**{fp(rate5)}**"
            ),
            (
                "- Casi con almeno +10% prima del minimo: "
                f"**{fp(rate10)}**"
            ),
            (
                "- Casi con almeno +15% prima del minimo: "
                f"**{fp(rate15)}**"
            ),
            (
                "- Discesa quasi immediata: "
                f"**{fp(immediate)}**"
            ),
            "",
            (
                "Un segnale ribassista a 30 giorni non "
                "significa necessariamente discesa immediata: "
                "alcuni casi fanno prima uno spike e poi scaricano."
            ),
            "",
            "### Distribuzione 30 giorni",
            "",
            md(pd.DataFrame([{
                "P10": fp(p[0]),
                "P25": fp(p[1]),
                "P50": fp(p[2]),
                "P75": fp(p[3]),
                "P90": fp(p[4]),
            }])),
            "",
            "### Grafico pulito: bande + mediana",
            "",
            f"![Extreme clean {asset}]({f_bands.name})",
            "",
            "### Grafico asset per asset",
            "",
            f"![Extreme asset medians {asset}]({f_lines.name})",
            "",
            "### Spike massimo prima della discesa",
            "",
            (
                "La sigla `g7` sopra una barra significa "
                "che il massimo rialzo è avvenuto al giorno 7."
            ),
            "",
            f"![Extreme spike before dump {asset}]({f_spike.name})",
            "",
            "### Spike iniziale contro minimo successivo",
            "",
            f"![Extreme spike vs low {asset}]({f_scatter.name})",
            "",
            "### Casi ordinati per risultato finale",
            "",
            f"![Extreme ranked {asset}]({f_ranked.name})",
            "",
            "### Casi con spike maggiore prima del dump",
            "",
            md(spike_table),
            "",
        ]

    lines += [
        "## Come leggerlo",
        "",
        (
            "- **Grafico pulito**: "
            "mostra il percorso centrale."
        ),
        (
            "- **Asset per asset**: "
            "mostra le differenze tra gli analoghi storici."
        ),
        (
            "- **Spike prima della discesa**: "
            "risponde a quanto poteva salire prima di scendere."
        ),
        (
            "- **Spike contro minimo**: "
            "mostra quanto rialzo iniziale è stato poi "
            "seguito da quale discesa."
        ),
        "",
        (
            "Questo report è diagnostico e "
            "non modifica il Global Confluence."
        ),
    ]

    text = "\n".join(lines).strip() + "\n"

    REPORT.write_text(
        text,
        encoding="utf-8",
    )

    inject(text)

    pd.DataFrame(
        metric_rows
    ).to_csv(
        METRICS,
        index=False,
    )

    if all_cases:
        pd.concat(
            all_cases,
            ignore_index=True,
        ).to_csv(
            CASES,
            index=False,
        )
    else:
        pd.DataFrame().to_csv(
            CASES,
            index=False,
        )

    print(f"Wrote {REPORT}")
    print(f"Wrote {METRICS}")
    print(f"Wrote {CASES}")


if __name__ == "__main__":
    main()
