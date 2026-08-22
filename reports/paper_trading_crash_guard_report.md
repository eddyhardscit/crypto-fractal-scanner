# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-08-22T05:07:22+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **38**
- Simulazioni completate nel ciclo: **3**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **706.82 R**
- Profitto virtuale mancato: **914.92 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 243 | 0 | 18299.64 |
| DOWN_20 | 243 | 0 | 36599.27 |
| DOWN_30 | 243 | 0 | 54898.91 |
| DOWN_40 | 243 | 85 | 67729.11 |
| UP_10 | 32 | 0 | 2257.85 |
| UP_20 | 32 | 0 | 4515.70 |
| UP_30 | 32 | 0 | 6773.55 |
| UP_40 | 32 | 5 | 8697.12 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
