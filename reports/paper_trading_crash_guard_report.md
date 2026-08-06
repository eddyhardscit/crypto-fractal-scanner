# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-06T05:08:55+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **0**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **196.29 R**
- Profitto virtuale mancato: **312.09 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 5 | 2 | 420.44 |
| DOWN_20 | 5 | 2 | 780.88 |
| DOWN_30 | 5 | 3 | 892.43 |
| DOWN_40 | 5 | 4 | 1002.20 |
| UP_10 | 9 | 0 | 640.45 |
| UP_20 | 9 | 0 | 1280.89 |
| UP_30 | 9 | 0 | 1921.34 |
| UP_40 | 9 | 3 | 2336.25 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
