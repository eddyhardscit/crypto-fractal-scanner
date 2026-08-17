# Block 3 — Shadow Exit Engine

Generato: 2026-08-17T05:06:14+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **806**
- Scenari virtuali ancora attivi: **15529**
- Gruppi in attesa dell'uscita originale: **470**
- Gruppi con originale chiuso ma Shadow ancora attive: **336**
- Confronti completati: **219750**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 5256 | 5325 | +€8,56 | 51,4% | 1442 | 13 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 5256 | 5325 | +€7,59 | 50,7% | 1425 | 58 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 5256 | 5325 | +€5,08 | 48,8% | 1589 | 12 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 5255 | 5324 | +€6,25 | 49,2% | 1438 | 120 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 5254 | 5323 | +€4,83 | 49,3% | 1369 | 182 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 5249 | 5322 | +€0,31 | 47,0% | 1102 | 708 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 5246 | 5319 | +€0,68 | 42,9% | 636 | 1025 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 5222 | 5295 | €-3,91 | 34,4% | 341 | 1438 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 5214 | 5283 | +€5,90 | 42,9% | 1261 | 98 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 5209 | 5278 | +€7,95 | 44,9% | 1140 | 104 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 5200 | 5269 | +€6,69 | 44,7% | 1080 | 173 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 5199 | 5268 | +€2,66 | 37,7% | 593 | 905 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 5197 | 5266 | +€5,60 | 44,0% | 979 | 285 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 5196 | 5265 | +€1,93 | 35,4% | 461 | 1137 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 5187 | 5256 | +€3,71 | 42,4% | 852 | 501 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 5178 | 5247 | +€5,89 | 35,1% | 695 | 493 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 5169 | 5238 | €-4,36 | 35,1% | 859 | 1043 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 5162 | 5231 | €-2,47 | 32,6% | 399 | 1291 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 5137 | 5203 | +€6,19 | 39,2% | 338 | 757 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 5009 | 5078 | €-7,80 | 27,3% | 363 | 1469 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
