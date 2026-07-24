# Analisi uscite paper trading a leva

Generato: 2026-07-24T05:08:52+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **1066**
- Trade con percorso cronologico utilizzabile: **1012**
- Trade che hanno raggiunto almeno +€50: **464**
- Di questi, chiusi poi in perdita: **103**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€82,38 | +€2.279,48 |
| 2 | Chiude 50% a +€50 | -€1.488,12 | +€708,98 |
| 3 | Take profit fisso +€100 | -€2.106,85 | +€90,24 |
| 4 | Protegge +€30 dopo +€50 | -€2.186,72 | +€10,38 |
| 5 | Strategia attuale | -€2.197,09 | €0,00 |
| 6 | Take profit fisso +€150 | -€2.197,09 | €0,00 |
| 7 | Take profit fisso +€200 | -€2.197,09 | €0,00 |
| 8 | Protegge +€20 dopo +€50 | -€2.362,68 | -€165,59 |
| 9 | Take profit fisso +€75 | -€3.012,70 | -€815,61 |
| 10 | Pareggio dopo +€50 | -€3.102,48 | -€905,38 |
| 11 | Trailing 20% dopo +€50 | -€3.134,52 | -€937,42 |
| 12 | TP +€50 / SL -€50 | -€4.387,25 | -€2.190,15 |
| 13 | Take profit fisso +€50 | -€6.682,72 | -€4.485,62 |
| 14 | Take profit fisso +€25 | -€6.900,03 | -€4.702,94 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
