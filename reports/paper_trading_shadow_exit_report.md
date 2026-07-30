# Block 3 — Shadow Exit Engine

Generato: 2026-07-30T05:08:47+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **471**
- Scenari virtuali ancora attivi: **6570**
- Gruppi in attesa dell'uscita originale: **126**
- Gruppi con originale chiuso ma Shadow ancora attive: **345**
- Confronti completati: **110793**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TIME_12H | 3073 | 3138 | €-1,29 | 40,2% | 388 | 720 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 3073 | 3138 | €-1,69 | 46,6% | 656 | 477 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 3073 | 3138 | €-4,80 | 32,7% | 176 | 980 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R050 | 3061 | 3126 | +€8,88 | 51,7% | 889 | 2 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 3061 | 3126 | +€7,22 | 50,7% | 891 | 21 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 3061 | 3126 | +€4,75 | 48,6% | 988 | 1 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 3053 | 3118 | +€5,17 | 49,3% | 898 | 57 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 3051 | 3116 | +€3,68 | 49,0% | 843 | 123 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 3045 | 3110 | +€6,39 | 44,1% | 695 | 82 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 3045 | 3110 | +€4,52 | 43,7% | 672 | 117 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 3045 | 3110 | +€4,39 | 41,9% | 762 | 80 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 3044 | 3109 | +€2,94 | 43,0% | 587 | 194 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 3041 | 3106 | +€1,16 | 40,9% | 509 | 356 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 3036 | 3101 | €-1,66 | 32,2% | 365 | 662 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 3014 | 3079 | €-2,05 | 29,6% | 308 | 777 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 3002 | 3067 | +€4,72 | 33,1% | 410 | 357 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 2942 | 3007 | +€4,09 | 36,5% | 198 | 540 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 2933 | 2998 | €-6,16 | 27,7% | 257 | 804 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 2879 | 2944 | €-6,39 | 33,4% | 539 | 588 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 2832 | 2897 | €-11,73 | 22,5% | 256 | 879 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
