# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-09-05T08:07:03+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **43**
- Simulazioni bloccate attive: **115**
- Simulazioni completate nel ciclo: **49**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **615.56 R**
- Profitto virtuale mancato: **1576.31 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 315 | 0 | 17567.63 |
| DOWN_20 | 315 | 0 | 35135.26 |
| DOWN_30 | 315 | 0 | 52702.90 |
| DOWN_40 | 315 | 94 | 66229.27 |
| UP_10 | 131 | 0 | 10580.58 |
| UP_20 | 131 | 0 | 21161.17 |
| UP_30 | 131 | 0 | 31741.75 |
| UP_40 | 131 | 60 | 38786.19 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
