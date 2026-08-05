# Analisi uscite paper trading a leva

Generato: 2026-08-05T05:11:11+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **3589**
- Trade con percorso cronologico utilizzabile: **3535**
- Trade che hanno raggiunto almeno +€50: **1407**
- Di questi, chiusi poi in perdita: **289**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€5.371,43 | +€11.995,61 |
| 2 | Chiude 50% a +€50 | -€3.432,45 | +€3.191,73 |
| 3 | Protegge +€30 dopo +€50 | -€4.884,48 | +€1.739,70 |
| 4 | TP +€50 / SL -€50 | -€5.298,22 | +€1.325,96 |
| 5 | Protegge +€20 dopo +€50 | -€5.810,77 | +€813,41 |
| 6 | Trailing 20% dopo +€50 | -€6.515,39 | +€108,79 |
| 7 | Strategia attuale | -€6.624,18 | €0,00 |
| 8 | Take profit fisso +€200 | -€6.624,18 | €0,00 |
| 9 | Take profit fisso +€150 | -€6.628,50 | -€4,32 |
| 10 | Take profit fisso +€100 | -€6.839,42 | -€215,24 |
| 11 | Pareggio dopo +€50 | -€7.747,28 | -€1.123,10 |
| 12 | Take profit fisso +€75 | -€10.034,32 | -€3.410,13 |
| 13 | Take profit fisso +€25 | -€17.131,56 | -€10.507,38 |
| 14 | Take profit fisso +€50 | -€17.154,78 | -€10.530,60 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
