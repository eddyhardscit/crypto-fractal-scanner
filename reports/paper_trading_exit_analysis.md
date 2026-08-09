# Analisi uscite paper trading a leva

Generato: 2026-08-09T05:12:20+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **3634**
- Trade con percorso cronologico utilizzabile: **3580**
- Trade che hanno raggiunto almeno +€50: **1409**
- Di questi, chiusi poi in perdita: **291**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€5.182,47 | +€12.055,56 |
| 2 | Chiude 50% a +€50 | -€3.605,54 | +€3.267,56 |
| 3 | Protegge +€30 dopo +€50 | -€5.102,28 | +€1.770,81 |
| 4 | TP +€50 / SL -€50 | -€5.436,07 | +€1.437,03 |
| 5 | Protegge +€20 dopo +€50 | -€6.038,57 | +€834,52 |
| 6 | Trailing 20% dopo +€50 | -€6.718,93 | +€154,16 |
| 7 | Strategia attuale | -€6.873,09 | €0,00 |
| 8 | Take profit fisso +€200 | -€6.873,09 | €0,00 |
| 9 | Take profit fisso +€150 | -€6.877,41 | -€4,32 |
| 10 | Take profit fisso +€100 | -€7.088,33 | -€215,24 |
| 11 | Pareggio dopo +€50 | -€7.995,08 | -€1.121,99 |
| 12 | Take profit fisso +€75 | -€10.283,23 | -€3.410,13 |
| 13 | Take profit fisso +€25 | -€17.278,83 | -€10.405,73 |
| 14 | Take profit fisso +€50 | -€17.352,58 | -€10.479,49 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
