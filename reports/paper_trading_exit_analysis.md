# Analisi uscite paper trading a leva

Generato: 2026-09-07T05:16:31+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **12115**
- Trade con percorso cronologico utilizzabile: **12061**
- Trade che hanno raggiunto almeno +€50: **4364**
- Di questi, chiusi poi in perdita: **835**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€27.198,34 | +€46.474,61 |
| 2 | Protegge +€30 dopo +€50 | -€6.249,05 | +€13.027,22 |
| 3 | Protegge +€20 dopo +€50 | -€12.790,61 | +€6.485,66 |
| 4 | TP +€50 / SL -€50 | -€15.466,20 | +€3.810,08 |
| 5 | Chiude 50% a +€50 | -€16.613,81 | +€2.662,47 |
| 6 | Strategia attuale | -€19.276,27 | €0,00 |
| 7 | Take profit fisso +€200 | -€19.276,27 | €0,00 |
| 8 | Take profit fisso +€150 | -€19.286,46 | -€10,19 |
| 9 | Trailing 20% dopo +€50 | -€21.582,33 | -€2.306,05 |
| 10 | Take profit fisso +€100 | -€22.049,45 | -€2.773,17 |
| 11 | Pareggio dopo +€50 | -€22.773,36 | -€3.497,09 |
| 12 | Take profit fisso +€75 | -€37.531,07 | -€18.254,80 |
| 13 | Take profit fisso +€50 | -€60.787,03 | -€41.510,75 |
| 14 | Take profit fisso +€25 | -€73.649,14 | -€54.372,86 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
