# Block 3 — Shadow Exit Engine

Generato: 2026-07-25T05:08:51+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **434**
- Scenari virtuali ancora attivi: **4015**
- Gruppi in attesa dell'uscita originale: **229**
- Gruppi con originale chiuso ma Shadow ancora attive: **205**
- Confronti completati: **18933**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TIME_6H | 922 | 985 | €-1,97 | 49,2% | 238 | 125 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R050 | 919 | 982 | +€5,59 | 51,1% | 262 | 1 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 919 | 982 | +€3,39 | 49,8% | 270 | 8 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 919 | 982 | +€1,06 | 48,5% | 277 | 13 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 919 | 982 | +€0,34 | 49,1% | 285 | 0 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 913 | 976 | €-0,25 | 47,3% | 269 | 27 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 911 | 974 | €-2,27 | 43,0% | 138 | 212 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 898 | 961 | +€5,02 | 45,2% | 223 | 23 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 898 | 961 | +€3,37 | 43,7% | 237 | 23 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 898 | 961 | +€3,13 | 45,2% | 211 | 35 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 897 | 960 | +€1,70 | 44,7% | 186 | 61 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 887 | 950 | +€0,92 | 42,2% | 147 | 116 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 876 | 939 | €-3,50 | 34,9% | 90 | 199 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 867 | 930 | €-5,07 | 35,2% | 80 | 256 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 863 | 926 | €-7,28 | 29,8% | 75 | 244 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 855 | 918 | +€3,32 | 34,0% | 117 | 92 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 848 | 911 | €-12,42 | 28,2% | 184 | 149 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 843 | 906 | €-11,13 | 26,6% | 70 | 243 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 837 | 900 | +€2,41 | 39,1% | 69 | 146 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 783 | 846 | €-17,73 | 21,5% | 69 | 239 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
