# Block 3 — Shadow Exit Engine

Generato: 2026-07-28T05:08:47+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **671**
- Scenari virtuali ancora attivi: **14242**
- Gruppi in attesa dell'uscita originale: **363**
- Gruppi con originale chiuso ma Shadow ancora attive: **308**
- Confronti completati: **81630**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 2445 | 2510 | +€8,85 | 50,0% | 743 | 2 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 2445 | 2510 | +€4,19 | 46,5% | 835 | 1 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 2442 | 2507 | €-2,37 | 44,4% | 530 | 428 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 2433 | 2498 | +€7,12 | 48,6% | 750 | 17 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 2429 | 2494 | +€5,02 | 47,4% | 755 | 40 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 2419 | 2484 | €-2,31 | 39,3% | 290 | 626 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 2418 | 2483 | +€7,31 | 44,5% | 589 | 67 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 2418 | 2483 | +€4,63 | 41,8% | 660 | 65 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 2418 | 2483 | +€3,50 | 47,1% | 712 | 90 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 2402 | 2467 | +€5,40 | 44,1% | 565 | 95 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 2402 | 2467 | +€3,92 | 43,9% | 477 | 159 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 2390 | 2455 | +€2,18 | 41,6% | 403 | 302 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 2382 | 2447 | +€5,91 | 33,8% | 342 | 269 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 2370 | 2435 | €-1,83 | 32,9% | 291 | 532 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 2361 | 2426 | +€5,72 | 38,6% | 169 | 428 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 2325 | 2390 | €-6,50 | 32,2% | 160 | 739 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 2323 | 2388 | €-2,92 | 30,3% | 256 | 590 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 2302 | 2367 | €-8,42 | 31,2% | 456 | 482 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 2284 | 2349 | €-7,44 | 28,3% | 209 | 634 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 2220 | 2285 | €-14,31 | 22,1% | 208 | 726 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
