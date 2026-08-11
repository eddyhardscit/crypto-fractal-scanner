# Block 3 — Shadow Exit Engine

Generato: 2026-08-11T05:09:56+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **249**
- Scenari virtuali ancora attivi: **10769**
- Gruppi in attesa dell'uscita originale: **234**
- Gruppi con originale chiuso ma Shadow ancora attive: **15**
- Confronti completati: **125676**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 3333 | 3399 | +€8,78 | 51,5% | 940 | 13 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 3333 | 3399 | +€7,38 | 50,6% | 928 | 47 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 3333 | 3399 | +€6,55 | 43,3% | 726 | 93 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 3333 | 3399 | +€6,12 | 49,0% | 926 | 98 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 3333 | 3399 | +€5,00 | 33,4% | 428 | 386 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 3333 | 3399 | +€4,80 | 42,9% | 690 | 143 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 3333 | 3399 | +€4,58 | 48,7% | 1043 | 12 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 3333 | 3399 | +€4,36 | 41,3% | 794 | 91 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 3333 | 3399 | +€4,11 | 41,9% | 604 | 235 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 3333 | 3399 | +€3,84 | 35,9% | 203 | 627 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 3318 | 3384 | +€4,67 | 49,2% | 868 | 143 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 3318 | 3384 | +€2,40 | 40,3% | 520 | 380 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 3318 | 3384 | €-0,19 | 31,9% | 370 | 702 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 3318 | 3384 | €-0,87 | 29,2% | 313 | 840 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 3318 | 3384 | €-0,90 | 40,0% | 403 | 740 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 3318 | 3384 | €-1,28 | 45,8% | 674 | 502 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 3318 | 3384 | €-3,57 | 33,2% | 558 | 718 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 3318 | 3384 | €-4,31 | 32,2% | 190 | 1009 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 3318 | 3384 | €-5,13 | 27,7% | 262 | 918 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 3318 | 3384 | €-8,39 | 23,1% | 262 | 1051 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
