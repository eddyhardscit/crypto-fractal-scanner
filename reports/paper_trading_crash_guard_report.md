# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-17T05:06:04+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **131**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **566.13 R**
- Profitto virtuale mancato: **903.98 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 259 | 0 | 33513.63 |
| DOWN_20 | 259 | 0 | 67027.26 |
| DOWN_30 | 259 | 0 | 100540.88 |
| DOWN_40 | 259 | 95 | 125792.36 |
| UP_10 | 203 | 0 | 18527.86 |
| UP_20 | 203 | 0 | 37055.72 |
| UP_30 | 203 | 0 | 55583.58 |
| UP_40 | 203 | 64 | 69638.32 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
