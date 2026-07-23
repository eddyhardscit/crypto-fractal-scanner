# Block 3 — Shadow Exit Engine

Generato: 2026-07-23T07:35:04+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **271**
- Scenari virtuali ancora attivi: **2361**
- Gruppi in attesa dell'uscita originale: **154**
- Gruppi con originale chiuso ma Shadow ancora attive: **117**
- Confronti completati: **10661**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 488 | 549 | +€8,17 | 46,8% | 124 | 0 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 488 | 549 | +€6,42 | 45,7% | 124 | 7 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 488 | 549 | +€4,45 | 45,0% | 125 | 10 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 488 | 549 | +€3,64 | 45,4% | 133 | 0 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 488 | 549 | +€2,52 | 44,3% | 120 | 19 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 488 | 549 | +€0,04 | 51,4% | 110 | 60 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 487 | 548 | +€1,82 | 43,1% | 41 | 119 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 481 | 542 | +€4,76 | 37,5% | 106 | 17 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 481 | 542 | +€3,35 | 36,9% | 97 | 29 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 481 | 542 | +€2,52 | 36,2% | 113 | 17 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 481 | 542 | +€1,99 | 36,9% | 76 | 48 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 481 | 542 | +€1,09 | 34,5% | 51 | 87 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 481 | 542 | €-3,56 | 28,4% | 34 | 121 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 472 | 533 | €-4,98 | 24,8% | 40 | 127 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 468 | 529 | €-3,68 | 29,5% | 22 | 149 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 460 | 521 | €-8,25 | 21,7% | 36 | 124 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 455 | 516 | +€1,49 | 27,7% | 48 | 53 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 447 | 508 | €-7,44 | 26,4% | 87 | 64 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 429 | 490 | €-0,58 | 30,2% | 20 | 81 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 410 | 470 | €-13,64 | 17,0% | 35 | 105 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
