# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-24T05:05:47+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **86**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **697.85 R**
- Profitto virtuale mancato: **956.56 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 226 | 0 | 12515.92 |
| DOWN_20 | 226 | 0 | 25031.84 |
| DOWN_30 | 226 | 8 | 37737.81 |
| DOWN_40 | 226 | 83 | 46757.58 |
| UP_10 | 18 | 0 | 1391.87 |
| UP_20 | 18 | 0 | 2783.73 |
| UP_30 | 18 | 0 | 4175.60 |
| UP_40 | 18 | 0 | 5567.47 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
