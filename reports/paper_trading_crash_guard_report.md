# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-28T07:05:47+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **59**
- Simulazioni completate nel ciclo: **3**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **628.54 R**
- Profitto virtuale mancato: **1101.45 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 224 | 0 | 15575.96 |
| DOWN_20 | 224 | 0 | 31151.91 |
| DOWN_30 | 224 | 0 | 46727.87 |
| DOWN_40 | 224 | 65 | 59484.98 |
| UP_10 | 64 | 0 | 3453.50 |
| UP_20 | 64 | 0 | 6906.99 |
| UP_30 | 64 | 0 | 10360.49 |
| UP_40 | 64 | 20 | 13221.41 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
