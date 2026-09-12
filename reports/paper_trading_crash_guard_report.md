# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-09-12T05:05:51+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **5**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **576.00 R**
- Profitto virtuale mancato: **1740.39 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 233 | 0 | 12816.46 |
| DOWN_20 | 233 | 0 | 25632.92 |
| DOWN_30 | 233 | 4 | 38498.67 |
| DOWN_40 | 233 | 57 | 49232.12 |
| UP_10 | 147 | 0 | 9914.19 |
| UP_20 | 147 | 0 | 19828.38 |
| UP_30 | 147 | 9 | 30300.25 |
| UP_40 | 147 | 72 | 35500.53 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
