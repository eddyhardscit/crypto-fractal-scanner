# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-05T05:08:53+00:00

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
| DOWN_10 | 2 | 0 | 111.55 |
| DOWN_20 | 2 | 0 | 223.09 |
| DOWN_30 | 2 | 0 | 334.64 |
| DOWN_40 | 2 | 1 | 444.41 |
| UP_10 | 12 | 2 | 803.20 |
| UP_20 | 12 | 3 | 1546.39 |
| UP_30 | 12 | 3 | 2186.84 |
| UP_40 | 12 | 6 | 2601.75 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
