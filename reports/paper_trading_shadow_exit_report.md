# Block 3 — Shadow Exit Engine

Generato: 2026-08-14T10:08:03+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **630**
- Scenari virtuali ancora attivi: **11887**
- Gruppi in attesa dell'uscita originale: **403**
- Gruppi con originale chiuso ma Shadow ancora attive: **227**
- Confronti completati: **188477**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 4609 | 4675 | +€8,35 | 51,3% | 1201 | 13 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 4609 | 4675 | +€7,37 | 50,3% | 1193 | 58 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 4609 | 4675 | +€4,65 | 48,4% | 1339 | 12 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 4609 | 4675 | €-0,33 | 46,8% | 852 | 669 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 4608 | 4674 | +€6,07 | 48,5% | 1207 | 119 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 4607 | 4673 | +€4,71 | 48,9% | 1135 | 176 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 4602 | 4668 | €-0,55 | 41,1% | 487 | 957 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 4602 | 4668 | €-4,66 | 32,9% | 212 | 1329 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 4601 | 4667 | +€7,08 | 43,9% | 936 | 102 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 4601 | 4667 | +€5,55 | 43,3% | 901 | 173 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 4601 | 4667 | +€4,89 | 41,8% | 1044 | 98 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 4596 | 4662 | +€5,64 | 34,0% | 561 | 456 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 4594 | 4660 | +€4,70 | 42,4% | 799 | 284 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 4593 | 4659 | +€2,92 | 41,2% | 677 | 476 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 4585 | 4651 | +€5,58 | 37,6% | 264 | 715 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 4576 | 4642 | +€1,24 | 35,0% | 484 | 833 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 4576 | 4642 | +€0,38 | 32,9% | 350 | 1049 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 4565 | 4631 | €-4,11 | 29,8% | 297 | 1205 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 4529 | 4595 | €-3,67 | 34,2% | 672 | 962 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 4494 | 4560 | €-8,42 | 24,8% | 291 | 1365 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
