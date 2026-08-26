# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-26T05:05:47+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **65**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **694.19 R**
- Profitto virtuale mancato: **1016.95 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 112 | 0 | 7793.73 |
| DOWN_20 | 112 | 0 | 15587.46 |
| DOWN_30 | 112 | 1 | 23382.07 |
| DOWN_40 | 112 | 45 | 28976.68 |
| UP_10 | 105 | 0 | 8691.58 |
| UP_20 | 105 | 0 | 17383.17 |
| UP_30 | 105 | 0 | 26074.75 |
| UP_40 | 105 | 42 | 32340.25 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
