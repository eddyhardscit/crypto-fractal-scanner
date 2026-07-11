# -*- coding: utf-8 -*-
"""Install Exchange Microstructure V2.1.3 over an existing V2.1.1 setup."""

from __future__ import annotations

import py_compile
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('.')
WORKFLOW_TEMPLATE = ROOT / 'exchange_intraday_workflow.yml'
WORKFLOW_TARGET = ROOT / '.github/workflows/exchange_intraday.yml'
STATUS_PATH = ROOT / 'reports/exchange_v2_1_3_installation_status.md'

REQUIRED = [
    ROOT / 'alternative_exchange_sources.py',
    ROOT / 'exchange_market_data.py',
    ROOT / 'exchange_microstructure_report.py',
    ROOT / 'exchange_signal_tracker.py',
    ROOT / 'exchange_persistent_storage.py',
    ROOT / 'exchange_microstructure_selftest.py',
    ROOT / 'requirements-exchange.txt',
    ROOT / 'requirements-exchange-collector.txt',
    WORKFLOW_TEMPLATE,
]


def utc_text() -> str:
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')


def install_workflow() -> bool:
    WORKFLOW_TARGET.parent.mkdir(parents=True, exist_ok=True)
    source = WORKFLOW_TEMPLATE.read_text(encoding='utf-8')
    current = WORKFLOW_TARGET.read_text(encoding='utf-8') if WORKFLOW_TARGET.exists() else ''
    if current == source:
        print(f'{WORKFLOW_TARGET}: già aggiornato.')
        return False
    if WORKFLOW_TARGET.exists():
        backup = WORKFLOW_TARGET.with_name(WORKFLOW_TARGET.name + '.bak_v2_1_3')
        if not backup.exists():
            backup.write_text(current, encoding='utf-8', newline='\n')
    WORKFLOW_TARGET.write_text(source, encoding='utf-8', newline='\n')
    print(f'{WORKFLOW_TARGET}: aggiornato.')
    return True


def validate_files() -> None:
    missing = [str(path) for path in REQUIRED if not path.exists()]
    if missing:
        raise RuntimeError('File mancanti: ' + ', '.join(missing))
    for path in (
        ROOT / 'alternative_exchange_sources.py',
        ROOT / 'exchange_market_data.py',
        ROOT / 'exchange_microstructure_report.py',
        ROOT / 'exchange_signal_tracker.py',
        ROOT / 'exchange_persistent_storage.py',
        ROOT / 'exchange_microstructure_selftest.py',
    ):
        py_compile.compile(str(path), doraise=True)


def validate_content() -> None:
    collector = (ROOT / 'exchange_market_data.py').read_text(encoding='utf-8')
    report = (ROOT / 'exchange_microstructure_report.py').read_text(encoding='utf-8')
    workflow = WORKFLOW_TARGET.read_text(encoding='utf-8')
    checks = {
        'Kraken collector': 'probe_kraken' in collector,
        'Bitget collector': 'probe_bitget' in collector,
        'KuCoin collector': 'probe_kucoin_control' in collector,
        'Funding 8h normalization': 'normalize_funding_8h_pct' in collector,
        'OKX auxiliary': 'probe_okx' in collector,
        'Coinbase auxiliary': 'probe_coinbase' in collector,
        'No Binance in report': 'Binance' not in report,
        'No Bybit in report': 'Bybit' not in report,
        'Workflow collects every run': 'python exchange_market_data.py' in workflow,
        'Old KuCoin-only switch removed': 'EXCHANGE_ENABLED_EXCHANGES: kucoin' not in workflow,
        'Old external fallback removed': 'exchange_fallback_guard.py' not in workflow,
    }
    failed = [name for name, ok in checks.items() if not ok]
    if failed:
        raise RuntimeError('Controlli installazione falliti: ' + ', '.join(failed))


def run_selftest() -> None:
    subprocess.run([sys.executable, 'exchange_microstructure_selftest.py'], check=True)


def write_status() -> None:
    STATUS_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATUS_PATH.write_text(
        '\n'.join(
            [
                '# Exchange Microstructure V2.1.3 — stato installazione',
                '',
                f'Generato: **{utc_text()}**',
                '',
                '- Nucleo derivati: **Kraken + Bitget + KuCoin**',
                '- Fonti ausiliarie non pesate: **OKX + Coinbase spot**',
                '- Funding: **normalizzato a equivalente 8 ore**',
                '- VPS: **non necessario**',
                '- Peso Global exchange: **resta soggetto al gate storico 7g**',
                '- Overlay 30g: **resta soggetto al gate storico separato**',
                '- Storage A/B e archivi mensili: **conservati**',
                '- Self-test: **OK**',
                '',
            ]
        ),
        encoding='utf-8',
        newline='\n',
    )


def main() -> None:
    validate_files()
    changed = install_workflow()
    validate_content()
    run_selftest()
    write_status()
    print('V2.1.3 installata.' if changed else 'V2.1.3 già installata e verificata.')


if __name__ == '__main__':
    main()
