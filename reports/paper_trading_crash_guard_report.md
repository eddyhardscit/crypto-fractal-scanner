# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-07-29T05:08:37+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **1**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **196.28 R**
- Profitto virtuale mancato: **312.09 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 58 | 0 | 5302.35 |
| DOWN_20 | 58 | 0 | 10604.70 |
| DOWN_30 | 58 | 1 | 15921.33 |
| DOWN_40 | 58 | 23 | 20215.91 |
| UP_10 | 135 | 0 | 12675.53 |
| UP_20 | 135 | 0 | 25351.07 |
| UP_30 | 135 | 0 | 38026.60 |
| UP_40 | 135 | 48 | 47646.00 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
