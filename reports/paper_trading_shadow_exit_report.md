# Block 3 — Shadow Exit Engine

Generato: 2026-07-31T05:08:49+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **411**
- Scenari virtuali ancora attivi: **6049**
- Gruppi in attesa dell'uscita originale: **109**
- Gruppi con originale chiuso ma Shadow ancora attive: **302**
- Confronti completati: **111431**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TIME_12H | 3090 | 3155 | €-1,29 | 40,1% | 389 | 720 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 3090 | 3155 | €-1,67 | 46,4% | 657 | 477 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 3090 | 3155 | €-4,79 | 32,6% | 177 | 980 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R050 | 3072 | 3137 | +€8,89 | 51,7% | 890 | 2 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 3072 | 3137 | +€7,24 | 50,8% | 892 | 21 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 3072 | 3137 | +€4,79 | 48,7% | 989 | 1 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 3064 | 3129 | +€5,19 | 49,4% | 899 | 57 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 3062 | 3127 | +€3,69 | 49,1% | 844 | 123 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 3048 | 3113 | +€6,38 | 44,0% | 696 | 82 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 3048 | 3113 | +€4,51 | 43,6% | 673 | 117 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 3048 | 3113 | +€4,39 | 41,9% | 762 | 80 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 3047 | 3112 | +€2,93 | 43,0% | 588 | 194 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 3044 | 3109 | +€1,16 | 40,9% | 509 | 356 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 3039 | 3104 | €-1,66 | 32,2% | 365 | 662 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 3025 | 3090 | €-2,04 | 29,5% | 308 | 784 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 3020 | 3085 | +€4,82 | 33,4% | 410 | 358 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 2994 | 3059 | €-6,36 | 27,8% | 257 | 844 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 2988 | 3053 | +€3,96 | 36,5% | 198 | 566 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 2893 | 2958 | €-6,46 | 33,3% | 540 | 591 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 2868 | 2933 | €-12,16 | 22,3% | 256 | 911 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
