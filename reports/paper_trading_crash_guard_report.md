# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-14T10:07:22+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **113**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **545.69 R**
- Profitto virtuale mancato: **522.27 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 209 | 0 | 19266.88 |
| DOWN_20 | 209 | 0 | 38533.75 |
| DOWN_30 | 209 | 0 | 57800.63 |
| DOWN_40 | 209 | 56 | 74263.43 |
| UP_10 | 153 | 0 | 32079.73 |
| UP_20 | 153 | 0 | 64159.46 |
| UP_30 | 153 | 0 | 96239.20 |
| UP_40 | 153 | 63 | 117273.68 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
