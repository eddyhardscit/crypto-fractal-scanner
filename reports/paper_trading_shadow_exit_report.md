# Block 3 — Shadow Exit Engine

Generato: 2026-08-26T05:08:33+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **898**
- Scenari virtuali ancora attivi: **12474**
- Gruppi in attesa dell'uscita originale: **222**
- Gruppi con originale chiuso ma Shadow ancora attive: **676**
- Confronti completati: **375588**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 8401 | 8474 | +€6,90 | 50,0% | 2725 | 15 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 8401 | 8474 | +€6,30 | 49,7% | 2668 | 76 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 8401 | 8474 | +€3,43 | 47,2% | 2972 | 12 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 8401 | 8474 | +€1,74 | 48,3% | 2088 | 920 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 8399 | 8472 | +€7,76 | 45,4% | 2179 | 127 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 8399 | 8472 | +€6,83 | 45,7% | 2044 | 248 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 8399 | 8472 | +€4,57 | 42,0% | 2516 | 107 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 8397 | 8470 | +€6,09 | 48,9% | 2631 | 178 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 8397 | 8470 | +€4,20 | 46,5% | 1323 | 1381 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 8383 | 8456 | +€5,46 | 41,6% | 779 | 1933 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 8381 | 8454 | +€5,46 | 35,4% | 1634 | 618 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 8380 | 8453 | +€7,47 | 45,5% | 1824 | 452 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 8373 | 8446 | +€4,19 | 41,9% | 1222 | 1193 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 8373 | 8446 | +€3,99 | 39,4% | 1002 | 1619 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 8370 | 8443 | +€6,82 | 48,8% | 2497 | 306 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 8366 | 8439 | +€2,77 | 37,2% | 834 | 1902 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 8350 | 8423 | +€6,54 | 40,6% | 803 | 986 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 8339 | 8412 | +€8,41 | 44,3% | 1593 | 772 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 8027 | 8100 | +€4,14 | 36,9% | 1658 | 1452 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 7879 | 7952 | +€1,82 | 29,7% | 792 | 2194 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
