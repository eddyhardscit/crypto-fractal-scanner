# Block 3 — Shadow Exit Engine

Generato: 2026-08-15T05:06:24+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **616**
- Scenari virtuali ancora attivi: **11166**
- Gruppi in attesa dell'uscita originale: **410**
- Gruppi con originale chiuso ma Shadow ancora attive: **206**
- Confronti completati: **201259**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 4862 | 4928 | +€7,96 | 50,7% | 1338 | 13 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 4862 | 4928 | +€7,04 | 49,9% | 1323 | 58 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 4862 | 4928 | +€4,38 | 48,0% | 1476 | 12 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 4862 | 4928 | €-0,02 | 41,8% | 565 | 997 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 4862 | 4928 | €-0,32 | 47,0% | 961 | 686 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 4861 | 4927 | +€5,70 | 48,2% | 1337 | 119 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 4860 | 4926 | +€4,32 | 48,5% | 1262 | 179 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 4852 | 4918 | +€7,02 | 44,3% | 1046 | 102 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 4852 | 4918 | +€5,76 | 43,9% | 998 | 173 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 4852 | 4918 | +€4,85 | 42,1% | 1162 | 98 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 4852 | 4918 | €-4,13 | 33,7% | 288 | 1368 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 4850 | 4916 | +€4,78 | 43,1% | 897 | 284 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 4848 | 4914 | +€1,85 | 36,1% | 552 | 871 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 4845 | 4911 | +€0,93 | 34,0% | 420 | 1091 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 4844 | 4910 | +€2,80 | 41,7% | 783 | 479 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 4837 | 4903 | +€5,82 | 34,8% | 631 | 456 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 4828 | 4894 | €-3,98 | 30,8% | 361 | 1260 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 4796 | 4862 | €-5,06 | 34,0% | 777 | 1025 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 4792 | 4858 | +€5,93 | 38,4% | 306 | 716 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 4703 | 4769 | €-9,05 | 25,4% | 325 | 1442 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
