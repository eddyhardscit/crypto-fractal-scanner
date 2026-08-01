# Analisi uscite paper trading a leva

Generato: 2026-08-01T05:10:26+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **3505**
- Trade con percorso cronologico utilizzabile: **3451**
- Trade che hanno raggiunto almeno +€50: **1402**
- Di questi, chiusi poi in perdita: **287**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€5.344,22 | +€11.994,48 |
| 2 | Chiude 50% a +€50 | -€3.533,39 | +€3.116,87 |
| 3 | Protegge +€30 dopo +€50 | -€4.994,08 | +€1.656,18 |
| 4 | TP +€50 / SL -€50 | -€5.475,16 | +€1.175,10 |
| 5 | Protegge +€20 dopo +€50 | -€5.890,37 | +€759,89 |
| 6 | Trailing 20% dopo +€50 | -€6.573,19 | +€77,07 |
| 7 | Strategia attuale | -€6.650,26 | €0,00 |
| 8 | Take profit fisso +€200 | -€6.650,26 | €0,00 |
| 9 | Take profit fisso +€150 | -€6.654,58 | -€4,32 |
| 10 | Take profit fisso +€100 | -€6.865,50 | -€215,24 |
| 11 | Pareggio dopo +€50 | -€7.766,88 | -€1.116,62 |
| 12 | Take profit fisso +€75 | -€10.183,04 | -€3.532,78 |
| 13 | Take profit fisso +€50 | -€17.330,59 | -€10.680,33 |
| 14 | Take profit fisso +€25 | -€17.389,55 | -€10.739,29 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
