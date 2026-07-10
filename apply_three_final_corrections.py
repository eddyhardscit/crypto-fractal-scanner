# -*- coding: utf-8 -*-
"""Applica tre correzioni finali allo scanner, in modo idempotente.

1. Scanner Forecast usa direttamente il prezzo dello snapshot condiviso.
2. Price coherence non confonde la colonna-score "Prezzo" del Classic Technical
   con un prezzo di mercato; inoltre sincronizza e controlla Scanner Forecast.
3. Classic Visual mostra correttamente Fibonacci 23,6% invece di 0,2%.

Il file non modifica punteggi, soglie operative, target o storici congelati.
"""

from __future__ import annotations

import py_compile
import re
import shutil
from pathlib import Path


FORECAST_PATH = Path("scanner_forecast_tracker.py")
SYNC_PATH = Path("price_coherence_sync.py")
VISUAL_PATH = Path("classic_technical_visual_report.py")
QUALITY_PATH = Path("data_quality_coherence_report.py")

FILES = (FORECAST_PATH, SYNC_PATH, VISUAL_PATH, QUALITY_PATH)


def read(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"File mancante: {path}")
    return path.read_text(encoding="utf-8")


def write_with_backup(path: Path, old: str, new: str) -> bool:
    if new == old:
        print(f"{path}: già corretto.")
        return False
    backup = path.with_suffix(path.suffix + ".bak_three_final_corrections")
    if not backup.exists():
        shutil.copy2(path, backup)
    path.write_text(new, encoding="utf-8", newline="\n")
    print(f"{path}: corretto; backup {backup.name}")
    return True


def replace_one(text: str, pattern: str, replacement: str, label: str, flags: int = 0) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=flags)
    if count != 1:
        raise RuntimeError(f"Patch non applicata a {label}: blocco atteso non trovato.")
    return updated


def patch_forecast() -> bool:
    old = read(FORECAST_PATH)
    new = old

    import_line = "from shared_market_snapshot import snapshot_price"
    if import_line not in new:
        new = replace_one(
            new,
            r"(import yfinance as yf\s*\n)",
            r"\1\nfrom shared_market_snapshot import snapshot_price\n",
            "import snapshot condiviso Scanner Forecast",
        )

    desired = '''# SHARED_SNAPSHOT_PRICE_PATCH_V1\ndef current_price_for_target(target, data):
    """Usa lo stesso prezzo corrente di tutti gli altri moduli.

    Il close scaricato da Yahoo resta soltanto un fallback. In questo modo il
    cono, i percentili in dollari, il CSV latest e il report sono tutti ancorati
    allo snapshot creato a inizio workflow.
    """
    asset = asset_short(target)
    shared = pd.to_numeric(snapshot_price(asset, np.nan), errors="coerce")
    if not pd.isna(shared) and float(shared) > 0:
        return float(shared)
    if target in data and not data[target].empty:
        return float(data[target]["Close"].iloc[-1])
    return np.nan


'''

    if "SHARED_SNAPSHOT_PRICE_PATCH_V1" not in new:
        new = replace_one(
            new,
            r"def current_price_for_target\(target, data\):.*?(?=def build_path_matrix\()",
            desired,
            "current_price_for_target Scanner Forecast",
            flags=re.DOTALL,
        )

    return write_with_backup(FORECAST_PATH, old, new)


def patch_sync() -> bool:
    old = read(SYNC_PATH)
    new = old

    if '"scanner_forecast_latest.csv"' not in new:
        scanner_spec = '''    "scanner_forecast_latest.csv": {
        "asset_columns": ("asset", "target_ticker"),
        "price_columns": ("current_price",),
    },
'''
        anchor_pattern = (
            r'(    "latest_scanner_summary\.csv": \{\s*'
            r'"asset_columns": \("asset", "ticker", "target"\),\s*'
            r'"price_columns": \("current_price", "price"\),\s*'
            r'\},\s*)'
        )
        new = replace_one(
            new,
            anchor_pattern,
            r"\1" + scanner_spec,
            "CSV Scanner Forecast in price coherence",
            flags=re.DOTALL,
        )

    for header in ("prezzo iniziale", "initial price", "start price", "start_price"):
        if f'"{header}"' not in new:
            new = new.replace(
                '    "prezzo attuale",\n',
                f'    "prezzo attuale",\n    "{header}",\n',
                1,
            )

    if "PRICE_SCORE_TABLE_GUARD_V1" not in new:
        anchor = (
            "            price_indexes = [idx for idx, name in enumerate(norm_header) "
            "if name in PRICE_HEADERS]\n"
        )
        if anchor not in new:
            raise RuntimeError("Punto di inserimento price_indexes non trovato in price_coherence_sync.py")
        guard = '''            # PRICE_SCORE_TABLE_GUARD_V1
            # Nel Classic Technical la colonna chiamata "Prezzo" è lo score
            # della conferma prezzo, non il prezzo di mercato. Non va riscritta.
            score_area_headers = {
                "trend", "struttura", "momentum", "volume",
                "candela", "wyckoff", "totale",
            }
            if score_area_headers.issubset(set(norm_header)):
                price_indexes = [
                    idx for idx in price_indexes
                    if norm_header[idx] not in {"prezzo", "price"}
                ]
'''
        new = new.replace(anchor, anchor + guard, 1)

    return write_with_backup(SYNC_PATH, old, new)


def patch_visual() -> bool:
    old = read(VISUAL_PATH)
    new = old

    if "FIBONACCI_PERCENT_LABEL_PATCH_V1" not in new:
        old_line_pattern = (
            r'    return f"Fib \{float\(ratio\):\.1f\}% \{state\} '
            r'\(\{score\}\) @ \{fmt_money\(result\[\'asset\'\], level\)\}"'
        )
        replacement = '''    # FIBONACCI_PERCENT_LABEL_PATCH_V1
    ratio_value = float(ratio)
    # Nei CSV il rapporto è normalmente 0.236, 0.382, 0.500, ecc.
    # Se arriva già come 23.6 non viene moltiplicato una seconda volta.
    if abs(ratio_value) <= 1.0:
        ratio_value *= 100.0
    ratio_text = f"{ratio_value:.1f}".replace(".", ",")
    return f"Fib {ratio_text}% {state} ({score}) @ {fmt_money(result['asset'], level)}"'''
        new = replace_one(
            new,
            old_line_pattern,
            replacement,
            "formatter percentuale Fibonacci Classic Visual",
        )

    return write_with_backup(VISUAL_PATH, old, new)


def patch_quality() -> bool:
    old = read(QUALITY_PATH)
    new = old

    # Richiesta: prezzo completamente identico, non soltanto vicino entro 0,02%.
    new = re.sub(
        r"PRICE_TOLERANCE_PCT\s*=\s*0\.02\b",
        "PRICE_TOLERANCE_PCT = 0.000001",
        new,
        count=1,
    )

    if '"Scanner Forecast"' not in new:
        forecast_spec = '''    "Scanner Forecast": {
        "path": REPORTS_DIR / "scanner_forecast_latest.csv",
        "asset_columns": ("asset", "target_ticker"),
        "price_columns": ("current_price",),
    },
'''
        anchor_pattern = (
            r'(    "Scanner": \{\s*'
            r'"path": REPORTS_DIR / "latest_scanner_summary\.csv",\s*'
            r'"asset_columns": \("asset", "ticker"\),\s*'
            r'"price_columns": \("current_price", "price"\),\s*'
            r'\},\s*)'
        )
        new = replace_one(
            new,
            anchor_pattern,
            r"\1" + forecast_spec,
            "controllo prezzo Scanner Forecast",
            flags=re.DOTALL,
        )

    if "STRICT_SHARED_PRICE_CHECK_V1" not in new:
        new = new.replace(
            "PRICE_TOLERANCE_PCT = 0.000001\n",
            "# STRICT_SHARED_PRICE_CHECK_V1\nPRICE_TOLERANCE_PCT = 0.000001\n",
            1,
        )

    return write_with_backup(QUALITY_PATH, old, new)


def validate_sources() -> None:
    for path in FILES:
        py_compile.compile(str(path), doraise=True)

    forecast = read(FORECAST_PATH)
    sync = read(SYNC_PATH)
    visual = read(VISUAL_PATH)
    quality = read(QUALITY_PATH)

    required = {
        FORECAST_PATH: (
            "from shared_market_snapshot import snapshot_price",
            "SHARED_SNAPSHOT_PRICE_PATCH_V1",
            "snapshot_price(asset, np.nan)",
        ),
        SYNC_PATH: (
            '"scanner_forecast_latest.csv"',
            '"prezzo iniziale"',
            "PRICE_SCORE_TABLE_GUARD_V1",
            'norm_header[idx] not in {"prezzo", "price"}',
        ),
        VISUAL_PATH: (
            "FIBONACCI_PERCENT_LABEL_PATCH_V1",
            "ratio_value *= 100.0",
            'replace(".", ",")',
        ),
        QUALITY_PATH: (
            '"Scanner Forecast"',
            "STRICT_SHARED_PRICE_CHECK_V1",
            "PRICE_TOLERANCE_PCT = 0.000001",
        ),
    }
    texts = {
        FORECAST_PATH: forecast,
        SYNC_PATH: sync,
        VISUAL_PATH: visual,
        QUALITY_PATH: quality,
    }
    missing = []
    for path, needles in required.items():
        for needle in needles:
            if needle not in texts[path]:
                missing.append(f"{path}: {needle}")
    if missing:
        raise RuntimeError("Validazione sorgenti fallita:\n- " + "\n- ".join(missing))

    print("Compilazione e validazione sorgenti: OK")


def main() -> None:
    patch_forecast()
    patch_sync()
    patch_visual()
    patch_quality()
    validate_sources()
    print("Tre correzioni finali applicate con successo.")


if __name__ == "__main__":
    main()
