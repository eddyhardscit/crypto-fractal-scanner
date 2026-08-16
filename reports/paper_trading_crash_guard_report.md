# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-16T05:06:14+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **177**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **493.18 R**
- Profitto virtuale mancato: **895.04 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 238 | 0 | 28896.80 |
| DOWN_20 | 238 | 0 | 57793.59 |
| DOWN_30 | 238 | 2 | 86720.13 |
| DOWN_40 | 238 | 73 | 109820.33 |
| UP_10 | 183 | 0 | 19967.04 |
| UP_20 | 183 | 6 | 40272.83 |
| UP_30 | 183 | 14 | 60163.15 |
| UP_40 | 183 | 76 | 74790.69 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
