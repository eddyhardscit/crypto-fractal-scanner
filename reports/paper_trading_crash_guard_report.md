# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-09-11T05:06:28+00:00

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
| DOWN_10 | 234 | 0 | 13846.79 |
| DOWN_20 | 234 | 0 | 27693.59 |
| DOWN_30 | 234 | 2 | 41569.52 |
| DOWN_40 | 234 | 57 | 52883.70 |
| UP_10 | 184 | 0 | 14374.42 |
| UP_20 | 184 | 0 | 28748.84 |
| UP_30 | 184 | 9 | 43680.95 |
| UP_40 | 184 | 97 | 50961.34 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
