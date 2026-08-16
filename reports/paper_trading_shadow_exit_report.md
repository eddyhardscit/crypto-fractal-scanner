# Block 3 — Shadow Exit Engine

Generato: 2026-08-16T05:06:30+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **714**
- Scenari virtuali ancora attivi: **14921**
- Gruppi in attesa dell'uscita originale: **412**
- Gruppi con originale chiuso ma Shadow ancora attive: **302**
- Confronti completati: **209302**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 5035 | 5104 | +€8,32 | 50,6% | 1420 | 13 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 5035 | 5104 | +€7,37 | 49,9% | 1403 | 58 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 5035 | 5104 | +€4,77 | 48,0% | 1558 | 12 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 5034 | 5103 | +€6,03 | 48,3% | 1417 | 119 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 5033 | 5102 | +€4,61 | 48,6% | 1340 | 181 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 5030 | 5103 | +€0,10 | 46,7% | 1044 | 703 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 5018 | 5087 | +€7,80 | 44,4% | 1125 | 102 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 5018 | 5087 | +€6,51 | 44,2% | 1072 | 173 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 5018 | 5087 | +€5,73 | 42,3% | 1239 | 98 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 5017 | 5086 | +€2,52 | 36,9% | 585 | 903 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 5015 | 5084 | +€5,43 | 43,4% | 972 | 284 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 5005 | 5074 | +€3,51 | 41,9% | 837 | 500 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 5002 | 5075 | +€0,64 | 42,3% | 613 | 1000 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 4996 | 5066 | €-3,97 | 34,1% | 333 | 1386 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 4994 | 5060 | +€1,31 | 34,6% | 453 | 1116 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 4971 | 5040 | +€6,20 | 34,9% | 681 | 456 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 4956 | 5022 | €-3,30 | 31,6% | 394 | 1268 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 4951 | 5017 | €-4,65 | 34,6% | 838 | 1025 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 4927 | 4993 | +€6,55 | 39,0% | 334 | 716 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 4831 | 4897 | €-8,22 | 26,4% | 358 | 1450 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
