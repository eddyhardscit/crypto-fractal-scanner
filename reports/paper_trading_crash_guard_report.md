# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-07-31T05:08:40+00:00

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
| DOWN_10 | 46 | 0 | 3532.23 |
| DOWN_20 | 46 | 0 | 7064.46 |
| DOWN_30 | 46 | 0 | 10596.69 |
| DOWN_40 | 46 | 20 | 13529.75 |
| UP_10 | 63 | 0 | 3645.46 |
| UP_20 | 63 | 0 | 7290.91 |
| UP_30 | 63 | 0 | 10936.37 |
| UP_40 | 63 | 14 | 13954.27 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
