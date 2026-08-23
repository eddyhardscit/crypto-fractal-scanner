# Block 3 — Shadow Exit Engine

Generato: 2026-08-23T05:06:05+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **1163**
- Scenari virtuali ancora attivi: **16814**
- Gruppi in attesa dell'uscita originale: **233**
- Gruppi con originale chiuso ma Shadow ancora attive: **930**
- Confronti completati: **345173**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TIME_12H | 7846 | 7919 | +€4,21 | 47,3% | 1237 | 1311 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 7846 | 7919 | +€1,48 | 48,5% | 1983 | 883 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R050 | 7828 | 7901 | +€6,68 | 50,2% | 2606 | 15 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 7828 | 7901 | +€6,08 | 49,8% | 2561 | 76 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 7828 | 7901 | +€5,90 | 42,3% | 726 | 1828 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 7828 | 7901 | +€2,88 | 47,2% | 2844 | 12 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 7820 | 7893 | +€5,48 | 48,9% | 2528 | 173 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 7818 | 7891 | +€4,62 | 42,7% | 2443 | 106 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 7816 | 7889 | +€8,00 | 46,3% | 2130 | 124 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 7816 | 7889 | +€7,05 | 46,6% | 2004 | 232 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 7808 | 7881 | +€4,69 | 43,7% | 1156 | 1150 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 7808 | 7881 | +€4,61 | 41,6% | 951 | 1509 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 7806 | 7879 | +€5,67 | 36,2% | 1607 | 568 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 7806 | 7879 | +€3,43 | 39,4% | 787 | 1787 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 7788 | 7861 | +€7,40 | 46,4% | 1796 | 413 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 7788 | 7861 | +€7,01 | 42,0% | 784 | 898 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 7770 | 7843 | +€4,91 | 48,7% | 2393 | 291 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 7700 | 7773 | +€5,78 | 44,9% | 1565 | 728 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 7348 | 7421 | €-4,09 | 36,7% | 1557 | 1369 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 7195 | 7268 | €-6,49 | 30,4% | 745 | 2072 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
