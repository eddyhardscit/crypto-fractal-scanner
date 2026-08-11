# Analisi uscite paper trading a leva

Generato: 2026-08-11T05:15:54+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **3678**
- Trade con percorso cronologico utilizzabile: **3624**
- Trade che hanno raggiunto almeno +€50: **1425**
- Di questi, chiusi poi in perdita: **291**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€5.583,81 | +€12.333,21 |
| 2 | Chiude 50% a +€50 | -€3.824,46 | +€2.924,93 |
| 3 | Protegge +€30 dopo +€50 | -€4.978,58 | +€1.770,81 |
| 4 | TP +€50 / SL -€50 | -€5.764,50 | +€984,90 |
| 5 | Protegge +€20 dopo +€50 | -€5.914,87 | +€834,52 |
| 6 | Trailing 20% dopo +€50 | -€6.595,23 | +€154,16 |
| 7 | Strategia attuale | -€6.749,39 | €0,00 |
| 8 | Take profit fisso +€200 | -€6.749,39 | €0,00 |
| 9 | Take profit fisso +€150 | -€6.753,71 | -€4,32 |
| 10 | Take profit fisso +€100 | -€6.980,83 | -€231,44 |
| 11 | Pareggio dopo +€50 | -€7.871,38 | -€1.121,99 |
| 12 | Take profit fisso +€75 | -€10.514,30 | -€3.764,91 |
| 13 | Take profit fisso +€50 | -€17.958,65 | -€11.209,26 |
| 14 | Take profit fisso +€25 | -€18.240,38 | -€11.490,98 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
