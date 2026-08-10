# Analisi uscite paper trading a leva

Generato: 2026-08-10T05:11:51+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **3641**
- Trade con percorso cronologico utilizzabile: **3587**
- Trade che hanno raggiunto almeno +€50: **1409**
- Di questi, chiusi poi in perdita: **291**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€5.148,57 | +€12.055,56 |
| 2 | Chiude 50% a +€50 | -€3.639,44 | +€3.267,56 |
| 3 | Protegge +€30 dopo +€50 | -€5.136,18 | +€1.770,81 |
| 4 | TP +€50 / SL -€50 | -€5.469,97 | +€1.437,03 |
| 5 | Protegge +€20 dopo +€50 | -€6.072,48 | +€834,52 |
| 6 | Trailing 20% dopo +€50 | -€6.752,83 | +€154,16 |
| 7 | Strategia attuale | -€6.907,00 | €0,00 |
| 8 | Take profit fisso +€200 | -€6.907,00 | €0,00 |
| 9 | Take profit fisso +€150 | -€6.911,32 | -€4,32 |
| 10 | Take profit fisso +€100 | -€7.122,24 | -€215,24 |
| 11 | Pareggio dopo +€50 | -€8.028,99 | -€1.121,99 |
| 12 | Take profit fisso +€75 | -€10.317,13 | -€3.410,13 |
| 13 | Take profit fisso +€25 | -€17.312,73 | -€10.405,73 |
| 14 | Take profit fisso +€50 | -€17.386,49 | -€10.479,49 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
