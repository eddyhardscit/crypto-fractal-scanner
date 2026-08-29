# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-29T05:06:00+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **50**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **631.64 R**
- Profitto virtuale mancato: **1101.45 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 203 | 0 | 11818.54 |
| DOWN_20 | 203 | 0 | 23637.08 |
| DOWN_30 | 203 | 2 | 35457.75 |
| DOWN_40 | 203 | 58 | 45015.27 |
| UP_10 | 117 | 0 | 12606.81 |
| UP_20 | 117 | 0 | 25213.62 |
| UP_30 | 117 | 0 | 37820.44 |
| UP_40 | 117 | 58 | 45036.90 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
