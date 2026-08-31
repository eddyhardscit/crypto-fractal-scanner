# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-31T05:06:20+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **30**
- Simulazioni bloccate attive: **38**
- Simulazioni completate nel ciclo: **33**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **651.89 R**
- Profitto virtuale mancato: **1224.73 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 173 | 2 | 11407.85 |
| DOWN_20 | 173 | 5 | 22862.38 |
| DOWN_30 | 173 | 9 | 34084.12 |
| DOWN_40 | 173 | 58 | 42803.77 |
| UP_10 | 123 | 0 | 13659.52 |
| UP_20 | 123 | 0 | 27319.04 |
| UP_30 | 123 | 0 | 40978.57 |
| UP_40 | 123 | 49 | 50003.33 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
