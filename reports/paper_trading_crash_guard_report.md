# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-09-14T05:05:53+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **28**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **675.51 R**
- Profitto virtuale mancato: **1741.88 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 245 | 0 | 13590.71 |
| DOWN_20 | 245 | 0 | 27181.43 |
| DOWN_30 | 245 | 0 | 40772.14 |
| DOWN_40 | 245 | 65 | 51885.53 |
| UP_10 | 144 | 0 | 8753.94 |
| UP_20 | 144 | 0 | 17507.88 |
| UP_30 | 144 | 4 | 26516.62 |
| UP_40 | 144 | 72 | 31641.60 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
