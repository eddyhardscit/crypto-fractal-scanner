# Block 3 — Shadow Exit Engine

Generato: 2026-07-26T05:08:47+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **656**
- Scenari virtuali ancora attivi: **11763**
- Gruppi in attesa dell'uscita originale: **399**
- Gruppi con originale chiuso ma Shadow ancora attive: **257**
- Confronti completati: **28648**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 1295 | 1360 | +€1,65 | 47,8% | 439 | 2 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 1295 | 1360 | €-0,17 | 45,8% | 456 | 16 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 1295 | 1360 | €-2,48 | 44,8% | 485 | 1 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 1282 | 1347 | €-2,22 | 45,1% | 442 | 28 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 1277 | 1342 | €-5,17 | 46,1% | 356 | 192 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 1272 | 1337 | +€3,37 | 43,7% | 358 | 28 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 1272 | 1337 | +€1,49 | 43,3% | 341 | 50 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 1272 | 1337 | +€0,67 | 39,7% | 413 | 26 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 1270 | 1335 | €-3,57 | 44,4% | 424 | 50 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 1244 | 1309 | €-0,09 | 42,8% | 284 | 89 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 1243 | 1308 | +€1,21 | 29,9% | 199 | 143 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 1230 | 1295 | €-3,42 | 41,7% | 191 | 294 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 1229 | 1294 | €-0,93 | 39,3% | 244 | 169 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 1217 | 1282 | +€2,46 | 38,8% | 101 | 214 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 1208 | 1273 | €-3,78 | 36,1% | 87 | 376 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 1190 | 1255 | €-4,45 | 35,1% | 151 | 255 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 1178 | 1243 | €-16,30 | 29,5% | 268 | 235 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 1172 | 1237 | €-8,67 | 29,6% | 132 | 322 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 1168 | 1233 | €-13,60 | 26,9% | 96 | 365 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 1073 | 1138 | €-20,49 | 22,1% | 95 | 348 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
