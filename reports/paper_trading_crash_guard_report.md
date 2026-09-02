# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-09-02T05:06:50+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **9**
- Simulazioni bloccate attive: **14**
- Simulazioni completate nel ciclo: **20**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **692.23 R**
- Profitto virtuale mancato: **1341.00 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 296 | 0 | 20190.78 |
| DOWN_20 | 296 | 0 | 40381.56 |
| DOWN_30 | 296 | 5 | 60621.25 |
| DOWN_40 | 296 | 103 | 75294.75 |
| UP_10 | 118 | 0 | 11819.11 |
| UP_20 | 118 | 0 | 23638.22 |
| UP_30 | 118 | 0 | 35457.33 |
| UP_40 | 118 | 43 | 43122.28 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
