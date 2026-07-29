# Block 3 — Shadow Exit Engine

Generato: 2026-07-29T05:08:46+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **621**
- Scenari virtuali ancora attivi: **9488**
- Gruppi in attesa dell'uscita originale: **193**
- Gruppi con originale chiuso ma Shadow ancora attive: **428**
- Confronti completati: **106699**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 2997 | 3062 | +€8,71 | 51,6% | 870 | 2 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 2997 | 3062 | +€7,04 | 50,7% | 872 | 21 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 2997 | 3062 | +€4,49 | 48,5% | 969 | 1 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 2990 | 3055 | +€4,98 | 49,2% | 879 | 57 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 2988 | 3053 | +€3,50 | 48,9% | 824 | 123 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 2988 | 3053 | €-1,82 | 46,9% | 636 | 459 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 2965 | 3030 | +€6,35 | 44,3% | 693 | 80 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 2965 | 3030 | +€4,47 | 43,9% | 670 | 115 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 2965 | 3030 | +€4,30 | 42,1% | 762 | 78 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 2965 | 3030 | +€2,90 | 43,3% | 583 | 192 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 2963 | 3028 | +€1,13 | 41,2% | 505 | 354 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 2952 | 3017 | €-2,19 | 39,0% | 371 | 720 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 2933 | 2998 | €-1,67 | 32,9% | 361 | 628 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 2922 | 2987 | €-4,96 | 32,8% | 169 | 917 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 2892 | 2957 | €-2,27 | 30,1% | 306 | 727 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 2888 | 2953 | +€4,79 | 33,1% | 410 | 330 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 2836 | 2901 | +€4,22 | 36,8% | 198 | 511 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 2828 | 2893 | €-6,33 | 28,1% | 255 | 768 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 2773 | 2838 | €-5,98 | 33,8% | 518 | 539 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 2698 | 2763 | €-12,05 | 23,0% | 254 | 812 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
