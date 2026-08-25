# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-25T05:05:46+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **84**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **695.04 R**
- Profitto virtuale mancato: **1003.90 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 217 | 3 | 15089.68 |
| DOWN_20 | 217 | 3 | 29704.41 |
| DOWN_30 | 217 | 3 | 44319.14 |
| DOWN_40 | 217 | 78 | 54925.19 |
| UP_10 | 53 | 0 | 3399.78 |
| UP_20 | 53 | 0 | 6799.56 |
| UP_30 | 53 | 0 | 10199.34 |
| UP_40 | 53 | 11 | 13114.13 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
