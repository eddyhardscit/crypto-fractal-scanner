# Blocco 4.5 — Crash Cascade Guard

Generato: 2026-07-28T05:08:38+00:00

> Paper-only. In mercato NORMAL/WATCH non riduce i segnali. Le limitazioni iniziano soltanto in STRESS, RECOVERY, CRASH, EXTREME o con dati non affidabili.

## Stato corrente

- Livello: **NORMAL**
- Direzione: **NONE**
- Segnali bloccati nel ciclo: **0**
- Simulazioni bloccate attive: **41**
- Simulazioni completate nel ciclo: **0**
- Liquidazioni virtuali evitate totali: **0**
- Valore cumulato del filtro: **163.54 R**
- Profitto virtuale mancato: **260.98 R**

## Stress test portafogli Paper

| Scenario | Posizioni interessate | Liquidazioni stimate | Perdita stimata EUR |
| --- | ---: | ---: | ---: |
| DOWN_10 | 103 | 0 | 10370.17 |
| DOWN_20 | 103 | 0 | 20740.34 |
| DOWN_30 | 103 | 7 | 31208.53 |
| DOWN_40 | 103 | 18 | 39960.50 |
| UP_10 | 255 | 0 | 36673.16 |
| UP_20 | 255 | 0 | 73346.32 |
| UP_30 | 255 | 0 | 110019.49 |
| UP_40 | 255 | 145 | 129820.40 |

## Modello di esecuzione

Se una candela di cascata attraversa nello stesso intervallo sia lo stop sia il prezzo di liquidazione, il Paper usa il caso peggiore e registra una liquidazione intrabar. Gli stop in gap o in regime di stress ricevono slippage aggiuntivo.

## Requisiti prima del live futures

- modalità ISOLATED obbligatoria;
- stop nativo sull'exchange;
- conferma dello stop prima di accettare la posizione;
- cross margin vietato.
