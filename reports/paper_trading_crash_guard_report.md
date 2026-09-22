# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-09-17T17:33:27+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **31**
- Simulazioni completate nel ciclo: **13**
- Liquidazioni virtuali evitate totali: **2**
- Valore cumulato del filtro: **773.35 R**
- Profitto virtuale mancato: **1889.97 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 70 | 0 | 6015.46 |
| DOWN_20 | 70 | 0 | 12030.92 |
| DOWN_30 | 70 | 0 | 18046.38 |
| DOWN_40 | 70 | 27 | 22347.18 |
| UP_10 | 33 | 6 | 1193.93 |
| UP_20 | 33 | 9 | 2207.87 |
| UP_30 | 33 | 13 | 3144.15 |
| UP_40 | 33 | 22 | 4054.64 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
