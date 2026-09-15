# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-09-15T05:06:49+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **67**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **680.56 R**
- Profitto virtuale mancato: **1786.34 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 250 | 0 | 13581.70 |
| DOWN_20 | 250 | 0 | 27163.39 |
| DOWN_30 | 250 | 2 | 40769.19 |
| DOWN_40 | 250 | 67 | 51690.82 |
| UP_10 | 153 | 0 | 10460.17 |
| UP_20 | 153 | 0 | 20920.34 |
| UP_30 | 153 | 0 | 31380.50 |
| UP_40 | 153 | 80 | 37429.11 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
