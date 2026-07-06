import os
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
import yfinance as yf

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    CHARTS_AVAILABLE = True
except Exception:
    CHARTS_AVAILABLE = False

REPORT_DIR = "reports"
MAIN_REPORT_PATH = "reports/latest_report.md"
REPORT_PATH = "reports/rsi_top_cycle_report.md"
CSV_PATH = "reports/rsi_top_cycle_metrics.csv"
BTC_SOL_METRICS_PATH = "reports/btc_2022_vs_sol_2026_metrics.csv"

WEEKLY_CHART_PATH = "reports/rsi_top_cycle_SOL_weekly.png"
MONTHLY_CHART_PATH = "reports/rsi_top_cycle_SOL_monthly.png"
WEEKLY_CHART_FILE = "rsi_top_cycle_SOL_weekly.png"
MONTHLY_CHART_FILE = "rsi_top_cycle_SOL_monthly.png"

TICKER = "SOL-USD"
ASSET_NAME = "SOL"
DOWNLOAD_START = "2020-01-01"
RSI_PERIOD = 14

# Use recent macro-cycle RSI highs, not the old 2020 SOL spike.
WEEKLY_ANCHOR_START_DATE = "2023-01-01"
MONTHLY_ANCHOR_START_DATE = "2023-01-01"
START_MARKER = "<!-- RSI_TOP_CYCLE_START -->"
END_MARKER = "<!-- RSI_TOP_CYCLE_END -->"


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


def fmt_date(value):
    try:
        return pd.to_datetime(value).strftime("%Y-%m-%d")
    except Exception:
        return "n/d"


def fmt_date_it(value):
    try:
        dt = pd.to_datetime(value)
        months = {
            1: "gennaio", 2: "febbraio", 3: "marzo", 4: "aprile",
            5: "maggio", 6: "giugno", 7: "luglio", 8: "agosto",
            9: "settembre", 10: "ottobre", 11: "novembre", 12: "dicembre",
        }
        return f"{dt.day} {months[dt.month]} {dt.year}"
    except Exception:
        return "n/d"


def md_table(headers, rows):
    def clean(x):
        return str(x).replace("|", "\\|").replace("\n", " ")
    out = []
    out.append("| " + " | ".join(clean(h) for h in headers) + " |")
    out.append("| " + " | ".join("---" for _ in headers) + " |")
    for row in rows:
        out.append("| " + " | ".join(clean(c) for c in row) + " |")
    return "\n".join(out)


def rsi(close, period=14):
    close = pd.to_numeric(close, errors="coerce")
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1 / period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / period, adjust=False).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs))


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


def resample_close(df, mode):
    if df.empty:
        return pd.DataFrame()
    if mode == "weekly":
        out = df["Close"].resample("W").last().dropna().to_frame("Close")
    else:
        out = df["Close"].resample("ME").last().dropna().to_frame("Close")
    out["rsi"] = rsi(out["Close"], RSI_PERIOD)
    return out.dropna().copy()


def find_pivot_highs(df, window=7, min_rsi=55):
    if df.empty or "rsi" not in df.columns:
        return pd.DataFrame(columns=["date", "rsi", "close"])
    s = df["rsi"].dropna()
    half = max(1, int(window // 2))
    rows = []
    for i in range(half, len(s) - half):
        val = safe_float(s.iloc[i])
        if val is None or val < min_rsi:
            continue
        local = s.iloc[i - half:i + half + 1]
        if val >= safe_float(local.max()):
            date = s.index[i]
            rows.append({"date": date, "rsi": val, "close": safe_float(df.loc[date, "Close"])})
    pivots = pd.DataFrame(rows)
    if pivots.empty:
        return pd.DataFrame(columns=["date", "rsi", "close"])
    pivots = pivots.sort_values("date").reset_index(drop=True)
    cleaned = []
    min_gap_days = 45 if window >= 7 else 120
    for _, row in pivots.iterrows():
        item = row.to_dict()
        if not cleaned:
            cleaned.append(item)
            continue
        gap = (pd.to_datetime(item["date"]) - pd.to_datetime(cleaned[-1]["date"])).days
        if gap < min_gap_days:
            if safe_float(item["rsi"]) > safe_float(cleaned[-1]["rsi"]):
                cleaned[-1] = item
        else:
            cleaned.append(item)
    return pd.DataFrame(cleaned)


def choose_anchors(pivots, df):
    if pivots is not None and not pivots.empty and len(pivots) >= 2:
        pivots = pivots.copy()
        pivots["date"] = pd.to_datetime(pivots["date"])
        pivots = pivots.sort_values("date")
        first = pivots.iloc[0]
        later = pivots.iloc[1:].copy()
        lower_later = later[pd.to_numeric(later["rsi"], errors="coerce") < safe_float(first["rsi"])]
        last = lower_later.iloc[-1] if not lower_later.empty else later.iloc[-1]
        out = pd.DataFrame([first, last]).reset_index(drop=True)
        if pd.to_datetime(out.iloc[0]["date"]) != pd.to_datetime(out.iloc[1]["date"]):
            return out
    if df.empty:
        return pd.DataFrame(columns=["date", "rsi", "close"])
    c = df.dropna(subset=["rsi"]).copy()
    c = c.sort_values("rsi", ascending=False)
    chosen = []
    for date, row in c.iterrows():
        item = {"date": date, "rsi": safe_float(row["rsi"]), "close": safe_float(row["Close"])}
        if not chosen:
            chosen.append(item)
        elif abs((pd.to_datetime(date) - pd.to_datetime(chosen[0]["date"])).days) >= 120:
            chosen.append(item)
            break
    if len(chosen) < 2:
        return pd.DataFrame(columns=["date", "rsi", "close"])
    return pd.DataFrame(chosen).sort_values("date").reset_index(drop=True)


def fit_line(anchors):
    if anchors is None or anchors.empty or len(anchors) < 2:
        return None
    a = anchors.copy()
    a["date"] = pd.to_datetime(a["date"])
    x = a["date"].map(pd.Timestamp.toordinal).astype(float).values
    y = pd.to_numeric(a["rsi"], errors="coerce").astype(float).values
    if len(x) < 2 or np.std(x) == 0:
        return None
    slope, intercept = np.polyfit(x, y, 1)
    return {
        "slope": float(slope),
        "intercept": float(intercept),
        "anchor_1_date": fmt_date(a.iloc[0]["date"]),
        "anchor_1_rsi": safe_float(a.iloc[0]["rsi"]),
        "anchor_1_price": safe_float(a.iloc[0].get("close")),
        "anchor_2_date": fmt_date(a.iloc[-1]["date"]),
        "anchor_2_rsi": safe_float(a.iloc[-1]["rsi"]),
        "anchor_2_price": safe_float(a.iloc[-1].get("close")),
    }


def line_value(model, date_value):
    if not model:
        return None
    try:
        ordinal = pd.to_datetime(date_value).toordinal()
        return float(model["slope"] * ordinal + model["intercept"])
    except Exception:
        return None


def read_cycle_context():
    ctx = {
        "cycle_max_base_price": None,
        "cycle_max_base_date": None,
        "cycle_max_beta_price": None,
        "target_from_current_base": None,
        "target_from_bottom_base": None,
    }
    if not os.path.exists(BTC_SOL_METRICS_PATH):
        return ctx
    try:
        df = pd.read_csv(BTC_SOL_METRICS_PATH)
    except Exception:
        return ctx
    if df.empty or "row_type" not in df.columns:
        return ctx
    rows = df[df["row_type"].astype(str) == "cycle_summary"].copy()
    if rows.empty:
        return ctx
    row = rows.iloc[-1]
    for key in list(ctx.keys()):
        if key in row:
            ctx[key] = row.get(key)
    return ctx


def classify_distance(current_rsi, line_now, name):
    current_rsi = safe_float(current_rsi)
    line_now = safe_float(line_now)
    if current_rsi is None or line_now is None:
        return {"status": "DATI INSUFFICIENTI", "distance": None, "score": 0, "text": "Dati insufficienti."}
    distance = line_now - current_rsi
    if current_rsi < 50 and distance > 8:
        return {"status": "LONTANO DALLA TOP-LINE", "distance": distance, "score": 0, "text": f"RSI {name} e ancora basso e lontano dalla trendline di esaurimento ciclo."}
    if distance > 10:
        return {"status": "LONTANO DALLA TOP-LINE", "distance": distance, "score": 0, "text": f"RSI {name} e distante dalla trendline. Nessun segnale top-cycle attivo."}
    if distance > 5:
        return {"status": "IN AVVICINAMENTO", "distance": distance, "score": 1, "text": f"RSI {name} si sta avvicinando alla trendline, ma non la sta ancora testando."}
    if distance > 0:
        return {"status": "TEST TOP-LINE", "distance": distance, "score": 2, "text": f"RSI {name} e vicino alla trendline. Aumenta il rischio di top locale o distribuzione."}
    if distance >= -3:
        return {"status": "TOCCO / BREAKOUT LEGGERO", "distance": distance, "score": 3, "text": f"RSI {name} sta toccando o superando di poco la trendline. Qui il rischio top aumenta molto."}
    return {"status": "SOPRA TOP-LINE / MANIA", "distance": distance, "score": 4, "text": f"RSI {name} e sopra la trendline. Possibile fase di estensione estrema o mania."}


def build_period_summary(name, df, min_rsi, window, cycle_date=None):
    if df.empty:
        return {"period": name, "ok": False, "current_rsi": None, "line_now": None, "distance": None, "status": "DATI INSUFFICIENTI", "text": "Dati insufficienti.", "anchors": pd.DataFrame(), "model": None, "line_at_cycle_top": None}

    # Important:
    # The hand-drawn TradingView top-line is the recent macro RSI exhaustion line.
    # So for SOL we search trendline anchors from 2023 onward.
    # This avoids the old 2020 RSI spike, which can flatten/distort the monthly line.
    if str(name).lower() == "weekly":
        anchor_start = WEEKLY_ANCHOR_START_DATE
    elif str(name).lower() == "monthly":
        anchor_start = MONTHLY_ANCHOR_START_DATE
    else:
        anchor_start = None

    anchor_df = df.copy()
    if anchor_start is not None:
        anchor_df = anchor_df[anchor_df.index >= pd.to_datetime(anchor_start)].copy()

    if anchor_df.empty or len(anchor_df) < 8:
        anchor_df = df.copy()

    pivots = find_pivot_highs(anchor_df, window=window, min_rsi=min_rsi)
    anchors = choose_anchors(pivots, anchor_df)
    model = fit_line(anchors)

    current_date = df.index[-1]
    current_rsi = safe_float(df["rsi"].iloc[-1])
    current_close = safe_float(df["Close"].iloc[-1])
    line_now = line_value(model, current_date)
    status = classify_distance(current_rsi, line_now, name)
    line_at_cycle_top = line_value(model, cycle_date) if cycle_date is not None else None

    return {
        "period": name,
        "ok": model is not None,
        "current_date": fmt_date(current_date),
        "current_price": current_close,
        "current_rsi": current_rsi,
        "line_now": line_now,
        "distance": status.get("distance"),
        "status": status.get("status"),
        "text": status.get("text"),
        "score": status.get("score"),
        "anchors": anchors,
        "model": model,
        "line_at_cycle_top": line_at_cycle_top,
    }


def classify_confluence(weekly, monthly, current_price, ctx):
    current_price = safe_float(current_price)
    cycle_target = safe_float(ctx.get("cycle_max_base_price")) or safe_float(ctx.get("target_from_current_base"))
    weekly_score = int(weekly.get("score", 0) or 0)
    monthly_score = int(monthly.get("score", 0) or 0)
    progress = None
    if current_price is not None and cycle_target is not None and cycle_target > 0:
        progress = current_price / cycle_target * 100
    if progress is None:
        bucket = "n/d"
    elif progress < 35:
        bucket = "inizio ciclo / lontano dal target macro"
    elif progress < 60:
        bucket = "fase intermedia"
    elif progress < 80:
        bucket = "fase avanzata"
    else:
        bucket = "vicino al target ciclo"
    score = weekly_score + monthly_score
    if progress is not None and progress < 35 and score <= 2:
        label = "BASSO"
        action = "Nessun segnale top-cycle attivo. Il filtro RSI serve piu avanti, non adesso."
    elif score >= 6 and progress is not None and progress >= 80:
        label = "MOLTO ALTO"
        action = "Weekly e monthly RSI sono in zona top-line mentre il prezzo e vicino al target ciclo. Zona da distribuire, non da inseguire."
    elif score >= 4 and progress is not None and progress >= 60:
        label = "ALTO"
        action = "Rischio top importante. Ha senso prendere profitto parziale e ridurre rischio."
    elif score >= 3:
        label = "MEDIO"
        action = "RSI segnala attenzione. Non e ancora top macro certo, ma non va ignorato."
    else:
        label = "BASSO"
        action = "RSI non segnala esaurimento ciclo. Guardare prima livelli prezzo e frattale."
    return {"label": label, "action": action, "price_progress_pct": progress, "price_bucket": bucket, "cycle_target": cycle_target}


def plot_chart(name, df, summary, ctx, output_path):
    if not CHARTS_AVAILABLE:
        return False
    try:
        if df.empty or not summary.get("ok"):
            fig, ax = plt.subplots(figsize=(12, 5))
            ax.text(0.5, 0.5, "Dati insufficienti per RSI top-cycle", ha="center", va="center", fontsize=12)
            ax.set_title(f"{ASSET_NAME} RSI {name} top-cycle")
            ax.axis("off")
            fig.tight_layout()
            fig.savefig(output_path, dpi=160, bbox_inches="tight")
            plt.close(fig)
            return os.path.exists(output_path)
        model = summary.get("model")
        anchors = summary.get("anchors")
        cycle_date = ctx.get("cycle_max_base_date")
        cycle_date = pd.to_datetime(cycle_date, errors="coerce") if cycle_date is not None else None
        end_date = df.index.max()
        if cycle_date is not None and not pd.isna(cycle_date) and cycle_date > end_date:
            end_date = cycle_date
        trend_dates = pd.date_range(start=df.index.min(), end=end_date, periods=300)
        trend_values = [line_value(model, d) for d in trend_dates]
        trend_values = [np.nan if v is None else max(0, min(100, v)) for v in trend_values]
        fig, ax = plt.subplots(figsize=(13, 6))
        ax.plot(df.index, df["rsi"], linewidth=1.7, label=f"RSI {name}")
        ax.plot(trend_dates, trend_values, linestyle="--", linewidth=1.6, label="RSI top-line stimata")
        ax.axhline(70, linestyle=":", alpha=0.45)
        ax.axhline(50, linestyle=":", alpha=0.45)
        ax.axhline(30, linestyle=":", alpha=0.45)
        if anchors is not None and not anchors.empty:
            ax.scatter(pd.to_datetime(anchors["date"]), anchors["rsi"], s=55, zorder=5, label="Punti trendline")
            for _, row in anchors.iterrows():
                ax.annotate(
                    f"{fmt_date(row['date'])}\nRSI {fmt_number(row['rsi'], 1)}",
                    xy=(pd.to_datetime(row["date"]), safe_float(row["rsi"])),
                    xytext=(8, 9),
                    textcoords="offset points",
                    fontsize=8,
                    bbox=dict(boxstyle="round,pad=0.18", fc="white", alpha=0.78),
                )
        current_date = df.index[-1]
        current_rsi = safe_float(df["rsi"].iloc[-1])
        if current_rsi is not None:
            ax.scatter([current_date], [current_rsi], s=60, zorder=6)
            ax.annotate(
                f"Oggi RSI {fmt_number(current_rsi, 1)}",
                xy=(current_date, current_rsi),
                xytext=(8, 12),
                textcoords="offset points",
                fontsize=8,
                bbox=dict(boxstyle="round,pad=0.18", fc="white", alpha=0.82),
            )
        if cycle_date is not None and not pd.isna(cycle_date):
            ax.axvline(cycle_date, linestyle=":", alpha=0.45)
            ax.annotate(
                "Target ciclo",
                xy=(cycle_date, 50),
                xytext=(8, 8),
                textcoords="offset points",
                fontsize=8,
                bbox=dict(boxstyle="round,pad=0.18", fc="white", alpha=0.75),
            )
        ax.set_ylim(0, 100)
        ax.set_title(f"{ASSET_NAME} RSI {name}: top-cycle warning")
        ax.set_xlabel("Data")
        ax.set_ylabel("RSI")
        ax.grid(True, alpha=0.28)
        ax.legend(loc="upper right")
        fig.autofmt_xdate()
        fig.tight_layout()
        fig.savefig(output_path, dpi=170, bbox_inches="tight")
        plt.close(fig)
        return os.path.exists(output_path) and os.path.getsize(output_path) > 1000
    except Exception as e:
        print(f"Could not generate RSI {name} chart: {e}")
        return False


def build_report(weekly, monthly, confluence, ctx, weekly_ok, monthly_ok):
    rome_now = datetime.now(ZoneInfo("Europe/Rome")).strftime("%Y-%m-%d %H:%M:%S %Z")
    utc_now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    current_price = weekly.get("current_price") or monthly.get("current_price")
    summary_rows = [
        ["Weekly RSI", fmt_number(weekly.get("current_rsi"), 2), fmt_number(weekly.get("line_now"), 2), fmt_number(weekly.get("distance"), 2), weekly.get("status", "n/d")],
        ["Monthly RSI", fmt_number(monthly.get("current_rsi"), 2), fmt_number(monthly.get("line_now"), 2), fmt_number(monthly.get("distance"), 2), monthly.get("status", "n/d")],
    ]
    cycle_rows = [
        ["Prezzo SOL attuale", fmt_price(current_price)],
        ["Target ciclo base", fmt_price(confluence.get("cycle_target"))],
        ["Avanzamento verso target base", fmt_pct(confluence.get("price_progress_pct"))],
        ["Fase prezzo", confluence.get("price_bucket", "n/d")],
        ["Rischio top-cycle RSI", confluence.get("label", "n/d")],
    ]
    anchor_rows = []
    for period_name, item in [("Weekly", weekly), ("Monthly", monthly)]:
        model = item.get("model") or {}
        anchor_rows.append([
            period_name,
            model.get("anchor_1_date", "n/d"),
            fmt_number(model.get("anchor_1_rsi"), 2),
            fmt_price(model.get("anchor_1_price")),
            model.get("anchor_2_date", "n/d"),
            fmt_number(model.get("anchor_2_rsi"), 2),
            fmt_price(model.get("anchor_2_price")),
            fmt_number(item.get("line_at_cycle_top"), 2),
        ])
    lines = []
    lines.append("# RSI top-cycle warning - SOL")
    lines.append("")
    lines.append(f"Generato: **{rome_now}**  ")
    lines.append(f"UTC: **{utc_now}**")
    lines.append("")
    lines.append("Questo report non usa l'RSI come segnale di entrata. Lo usa come filtro di esaurimento ciclo: quando RSI weekly/monthly torna vicino alla trendline alta, il rischio di top o distribuzione aumenta.")
    lines.append("")
    lines.append("## Sintesi")
    lines.append("")
    lines.append(md_table(["Voce", "RSI attuale", "Top-line RSI stimata", "Distanza", "Stato"], summary_rows))
    lines.append("")
    lines.append("## Confluenza con target ciclo SOL")
    lines.append("")
    lines.append(md_table(["Voce", "Valore"], cycle_rows))
    lines.append("")
    lines.append(f"**Lettura:** {confluence.get('action', 'n/d')}")
    lines.append("")
    lines.append("## Come leggerlo")
    lines.append("")
    lines.append("- RSI lontano dalla top-line = nessun segnale top-cycle attivo.")
    lines.append("- RSI weekly vicino alla top-line = possibile top locale o take profit parziale.")
    lines.append("- RSI monthly vicino alla top-line = possibile top macro.")
    lines.append("- RSI weekly + monthly vicini alla top-line e prezzo vicino al target ciclo = zona da distribuire, non da inseguire.")
    lines.append("")
    lines.append("## Punti usati per stimare la trendline")
    lines.append("")
    lines.append(md_table(["Periodo", "Ancora 1 data", "Ancora 1 RSI", "Prezzo ancora 1", "Ancora 2 data", "Ancora 2 RSI", "Prezzo ancora 2", "Top-line RSI alla data ciclo"], anchor_rows))
    lines.append("")
    lines.append("Nota: la trendline RSI e stimata automaticamente sui pivot alti recenti dell'RSI, da 2023 in poi. Non e una certezza matematica; serve come filtro visivo e operativo.")
    lines.append("")
    lines.append("## Grafici")
    lines.append("")
    if weekly_ok:
        lines.append("### SOL weekly RSI top-line")
        lines.append("")
        lines.append(f"![SOL weekly RSI top-line]({WEEKLY_CHART_FILE})")
        lines.append("")
    if monthly_ok:
        lines.append("### SOL monthly RSI top-line")
        lines.append("")
        lines.append(f"![SOL monthly RSI top-line]({MONTHLY_CHART_FILE})")
        lines.append("")
    lines.append("## Stato attuale")
    lines.append("")
    lines.append(f"- **Weekly:** {weekly.get('text', 'n/d')}")
    lines.append(f"- **Monthly:** {monthly.get('text', 'n/d')}")
    lines.append(f"- **Rischio top-cycle attuale:** {confluence.get('label', 'n/d')}")
    lines.append("")
    lines.append("Traduzione pratica: questo filtro diventa molto importante piu avanti, quando SOL si avvicina ai target 211 / 500 / 600. Adesso serve soprattutto a confermare che non siamo ancora in zona top.")
    lines.append("")
    return "\n".join(lines)


def build_main_block(weekly, monthly, confluence, weekly_ok, monthly_ok):
    current_price = weekly.get("current_price") or monthly.get("current_price")
    rows = [
        ["Prezzo SOL", fmt_price(current_price), ""],
        ["Weekly RSI", f"{fmt_number(weekly.get('current_rsi'), 2)} / top-line {fmt_number(weekly.get('line_now'), 2)}", weekly.get("status", "n/d")],
        ["Monthly RSI", f"{fmt_number(monthly.get('current_rsi'), 2)} / top-line {fmt_number(monthly.get('line_now'), 2)}", monthly.get("status", "n/d")],
        ["Target ciclo base", fmt_price(confluence.get("cycle_target")), f"Avanzamento {fmt_pct(confluence.get('price_progress_pct'))}"],
        ["Rischio top-cycle RSI", confluence.get("label", "n/d"), confluence.get("action", "n/d")],
    ]
    lines = []
    lines.append(START_MARKER)
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("# RSI top-cycle warning - SOL")
    lines.append("")
    lines.append("Report separato completo: [rsi_top_cycle_report.md](rsi_top_cycle_report.md)")
    lines.append("")
    lines.append("Questo filtro controlla se RSI weekly/monthly si stanno avvicinando alla trendline alta che puo segnalare esaurimento ciclo.")
    lines.append("")
    lines.append(md_table(["Voce", "Valore", "Lettura"], rows))
    lines.append("")
    lines.append("## Lettura semplice")
    lines.append("")
    lines.append(f"- Weekly: {weekly.get('text', 'n/d')}")
    lines.append(f"- Monthly: {monthly.get('text', 'n/d')}")
    lines.append(f"- Confluenza prezzo + RSI: **{confluence.get('label', 'n/d')}**")
    lines.append("")
    lines.append("Questo non e un segnale di entrata. Serve soprattutto per riconoscere piu avanti una possibile zona top, per esempio se SOL si avvicina ai target 500/600 e RSI weekly/monthly tornano sulla top-line.")
    lines.append("")
    if weekly_ok or monthly_ok:
        lines.append("## Grafici RSI")
        lines.append("")
        if weekly_ok:
            lines.append(f"![SOL weekly RSI top-line]({WEEKLY_CHART_FILE})")
            lines.append("")
        if monthly_ok:
            lines.append(f"![SOL monthly RSI top-line]({MONTHLY_CHART_FILE})")
            lines.append("")
    lines.append(END_MARKER)
    return "\n".join(lines)


def inject_main(block):
    if not os.path.exists(MAIN_REPORT_PATH):
        return
    with open(MAIN_REPORT_PATH, "r", encoding="utf-8") as f:
        current = f.read()
    if START_MARKER in current and END_MARKER in current:
        before = current.split(START_MARKER)[0].rstrip()
        after = current.split(END_MARKER, 1)[1].lstrip()
        current = before + "\n\n" + after
    insert_after = "<!-- BTC_SOL_FRACTAL_END -->"
    if insert_after in current:
        pos = current.find(insert_after) + len(insert_after)
        new_text = current[:pos].rstrip() + "\n\n" + block.strip() + "\n\n" + current[pos:].lstrip()
    else:
        new_text = block.strip() + "\n\n" + current.lstrip()
    with open(MAIN_REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(new_text.rstrip() + "\n")


def write_csv(weekly, monthly, confluence, ctx):
    rows = []
    for item in [weekly, monthly]:
        model = item.get("model") or {}
        rows.append({
            "row_type": "period_summary",
            "period": item.get("period"),
            "current_date": item.get("current_date"),
            "current_price": item.get("current_price"),
            "current_rsi": item.get("current_rsi"),
            "line_now": item.get("line_now"),
            "distance": item.get("distance"),
            "status": item.get("status"),
            "score": item.get("score"),
            "anchor_1_date": model.get("anchor_1_date"),
            "anchor_1_rsi": model.get("anchor_1_rsi"),
            "anchor_1_price": model.get("anchor_1_price"),
            "anchor_2_date": model.get("anchor_2_date"),
            "anchor_2_rsi": model.get("anchor_2_rsi"),
            "anchor_2_price": model.get("anchor_2_price"),
            "line_at_cycle_top": item.get("line_at_cycle_top"),
        })
    rows.append({
        "row_type": "confluence",
        "risk_label": confluence.get("label"),
        "action": confluence.get("action"),
        "price_progress_pct": confluence.get("price_progress_pct"),
        "price_bucket": confluence.get("price_bucket"),
        "cycle_target": confluence.get("cycle_target"),
        "cycle_max_base_price": ctx.get("cycle_max_base_price"),
        "cycle_max_base_date": ctx.get("cycle_max_base_date"),
        "cycle_max_beta_price": ctx.get("cycle_max_beta_price"),
    })
    pd.DataFrame(rows).to_csv(CSV_PATH, index=False)


def main():
    os.makedirs(REPORT_DIR, exist_ok=True)
    daily = download_close(TICKER, DOWNLOAD_START)
    if daily.empty:
        with open(REPORT_PATH, "w", encoding="utf-8") as f:
            f.write("# RSI top-cycle warning - SOL\n\nDati insufficienti: download prezzi vuoto.\n")
        print("RSI top-cycle report: no data")
        return

    weekly_df = resample_close(daily, "weekly")
    monthly_df = resample_close(daily, "monthly")

    ctx = read_cycle_context()
    cycle_date = pd.to_datetime(ctx.get("cycle_max_base_date"), errors="coerce") if ctx.get("cycle_max_base_date") is not None else None
    if cycle_date is not None and pd.isna(cycle_date):
        cycle_date = None

    weekly = build_period_summary("weekly", weekly_df, min_rsi=55, window=7, cycle_date=cycle_date)
    monthly = build_period_summary("monthly", monthly_df, min_rsi=55, window=3, cycle_date=cycle_date)

    current_price = safe_float(daily["Close"].iloc[-1])
    confluence = classify_confluence(weekly, monthly, current_price, ctx)

    weekly_ok = plot_chart("weekly", weekly_df, weekly, ctx, WEEKLY_CHART_PATH)
    monthly_ok = plot_chart("monthly", monthly_df, monthly, ctx, MONTHLY_CHART_PATH)

    report = build_report(weekly, monthly, confluence, ctx, weekly_ok, monthly_ok)

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report.rstrip() + "\n")

    write_csv(weekly, monthly, confluence, ctx)
    inject_main(build_main_block(weekly, monthly, confluence, weekly_ok, monthly_ok))

    print("RSI top-cycle report generated")
    print(f"Weekly RSI chart ok: {weekly_ok} -> {WEEKLY_CHART_PATH}")
    print(f"Monthly RSI chart ok: {monthly_ok} -> {MONTHLY_CHART_PATH}")
    print(f"Top-cycle risk: {confluence.get('label')}")


if __name__ == "__main__":
    main()
