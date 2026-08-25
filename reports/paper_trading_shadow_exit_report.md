# Block 3 — Shadow Exit Engine

Generato: 2026-08-25T05:08:29+00:00

> Motore esclusivamente osservativo e Paper-only. Non modifica le uscite reali. I confronti escludono il funding sia dall'uscita originale sia dalle varianti.

## Stato operativo

- Gruppi di trade ancora monitorati: **1109**
- Scenari virtuali ancora attivi: **15925**
- Gruppi in attesa dell'uscita originale: **269**
- Gruppi con originale chiuso ma Shadow ancora attive: **840**
- Confronti completati: **364286**

## Classifica osservativa complessiva

| Scenario | Campione completo | Campione totale | Δ medio vs originale | Migliora | Troppo presto | Troppo tardi | Stato dati |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GB20_R050 | 8206 | 8279 | +€6,55 | 49,9% | 2697 | 15 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R050 | 8206 | 8279 | +€5,96 | 49,6% | 2645 | 76 | READY_FOR_BLOCK4_EVALUATION |
| TP_R050 | 8206 | 8279 | +€3,01 | 47,0% | 2944 | 12 | READY_FOR_BLOCK4_EVALUATION |
| TP_R100 | 8203 | 8276 | +€4,66 | 42,8% | 2496 | 106 | READY_FOR_BLOCK4_EVALUATION |
| GB20_R100 | 8201 | 8274 | +€7,91 | 46,2% | 2171 | 126 | READY_FOR_BLOCK4_EVALUATION |
| GB30_R100 | 8201 | 8274 | +€6,98 | 46,5% | 2036 | 242 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R050 | 8199 | 8272 | +€5,37 | 48,8% | 2609 | 173 | READY_FOR_BLOCK4_EVALUATION |
| TIME_6H | 8193 | 8266 | +€1,51 | 48,2% | 2063 | 909 | READY_FOR_BLOCK4_EVALUATION |
| TIME_12H | 8179 | 8252 | +€4,00 | 46,6% | 1316 | 1339 | READY_FOR_BLOCK4_EVALUATION |
| GB40_R100 | 8174 | 8247 | +€7,23 | 46,3% | 1822 | 431 | READY_FOR_BLOCK4_EVALUATION |
| ATR15_R100 | 8169 | 8242 | +€4,29 | 42,7% | 1216 | 1176 | READY_FOR_BLOCK4_EVALUATION |
| ATR20_R100 | 8165 | 8238 | +€4,16 | 40,3% | 994 | 1581 | READY_FOR_BLOCK4_EVALUATION |
| ATR30_R100 | 8160 | 8233 | +€2,97 | 38,1% | 828 | 1864 | READY_FOR_BLOCK4_EVALUATION |
| TP_R150 | 8156 | 8229 | +€5,70 | 36,2% | 1632 | 581 | READY_FOR_BLOCK4_EVALUATION |
| TIME_24H | 8148 | 8221 | +€5,53 | 41,6% | 773 | 1883 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R050 | 8146 | 8219 | +€4,78 | 48,5% | 2476 | 296 | READY_FOR_BLOCK4_EVALUATION |
| GB50_R100 | 8105 | 8178 | +€6,64 | 45,0% | 1591 | 747 | READY_FOR_BLOCK4_EVALUATION |
| TP_R200 | 8098 | 8171 | +€7,06 | 41,6% | 803 | 911 | READY_FOR_BLOCK4_EVALUATION |
| BE_R050 | 7751 | 7824 | €-1,98 | 36,2% | 1645 | 1418 | READY_FOR_BLOCK4_EVALUATION |
| BE_R100 | 7604 | 7677 | €-4,12 | 29,9% | 786 | 2157 | READY_FOR_BLOCK4_EVALUATION |

## Come leggere il controllo

- **EARLIER_BETTER**: la variante è uscita prima e ha conservato più profitto.
- **TOO_EARLY**: la variante è uscita prima ma ha tagliato un movimento migliore.
- **LATER_BETTER**: la variante ha continuato dopo l'uscita originale e ha guadagnato di più.
- **TOO_LATE**: la variante è rimasta aperta più a lungo e ha peggiorato il risultato.

## Limiti e protezioni

Le regole Shadow mantengono entrata, quantità, commissioni, stop protettivo iniziale e liquidazione. Le ambiguità all'interno della stessa candela vengono risolte scegliendo l'esito peggiore. Le posizioni già aperte al momento dell'installazione sono marcate come campione parziale e non saranno utilizzate dal futuro Blocco 4 come prova piena.
