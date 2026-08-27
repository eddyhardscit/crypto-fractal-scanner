# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-27T05:05:50+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **42**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **711.49 R**
- Profitto virtuale mancato: **1016.95 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 247 | 0 | 36570.86 |
| DOWN_20 | 247 | 0 | 73141.73 |
| DOWN_30 | 247 | 4 | 109754.78 |
| DOWN_40 | 247 | 92 | 136083.14 |
| UP_10 | 80 | 0 | 4716.14 |
| UP_20 | 80 | 0 | 9432.27 |
| UP_30 | 80 | 0 | 14148.41 |
| UP_40 | 80 | 25 | 18217.80 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
