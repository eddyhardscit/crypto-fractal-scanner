# Block 3 — Shadow Exit Engine

Generato: 2026-08-02T05:08:56+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **257**
- Scenari virtuali ancora attivi: **3873**
- Gruppi in attesa dell'uscita originale: **27**
- Gruppi con originale chiuso ma Shadow ancora attive: **230**
- Confronti completati: **115669**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TIME_6H | 3189 | 3255 | €-1,49 | 45,8% | 664 | 484 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 3180 | 3246 | €-1,19 | 39,4% | 396 | 729 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 3180 | 3246 | €-4,68 | 31,6% | 184 | 989 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R050 | 3171 | 3237 | +€8,84 | 51,8% | 899 | 8 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 3171 | 3237 | +€7,21 | 50,9% | 901 | 27 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 3171 | 3237 | +€5,19 | 49,3% | 904 | 69 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 3171 | 3237 | +€4,86 | 48,8% | 998 | 7 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 3159 | 3225 | +€3,72 | 49,1% | 847 | 129 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 3149 | 3215 | +€6,30 | 43,3% | 696 | 88 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 3149 | 3215 | +€4,47 | 42,9% | 673 | 123 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 3149 | 3215 | +€4,37 | 41,3% | 762 | 86 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 3149 | 3215 | +€2,92 | 42,0% | 591 | 206 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 3143 | 3209 | +€4,83 | 33,0% | 410 | 378 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 3137 | 3203 | +€1,20 | 40,1% | 509 | 362 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 3127 | 3193 | €-1,62 | 31,4% | 365 | 671 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 3127 | 3193 | €-2,20 | 28,6% | 309 | 807 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 3122 | 3188 | +€3,71 | 35,7% | 198 | 600 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 3117 | 3183 | €-6,70 | 26,8% | 258 | 885 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 3018 | 3084 | €-7,01 | 32,6% | 544 | 634 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 3002 | 3068 | €-12,52 | 21,4% | 257 | 963 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
