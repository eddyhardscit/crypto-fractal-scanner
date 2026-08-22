# Analisi uscite paper trading a leva

Generato: 2026-08-22T05:11:40+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **7921**
- Trade con percorso cronologico utilizzabile: **7867**
- Trade che hanno raggiunto almeno +€50: **3096**
- Di questi, chiusi poi in perdita: **606**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€35.260,17 | +€39.536,25 |
| 2 | Protegge +€30 dopo +€50 | +€7.570,68 | +€11.846,76 |
| 3 | Protegge +€20 dopo +€50 | +€3.279,62 | +€7.555,70 |
| 4 | TP +€50 / SL -€50 | +€3.262,22 | +€7.538,30 |
| 5 | Pareggio dopo +€50 | -€3.944,38 | +€331,70 |
| 6 | Trailing 20% dopo +€50 | -€4.133,34 | +€142,73 |
| 7 | Strategia attuale | -€4.276,08 | €0,00 |
| 8 | Take profit fisso +€200 | -€4.276,08 | €0,00 |
| 9 | Take profit fisso +€150 | -€4.286,27 | -€10,19 |
| 10 | Chiude 50% a +€50 | -€4.564,03 | -€287,95 |
| 11 | Take profit fisso +€100 | -€6.052,43 | -€1.776,36 |
| 12 | Take profit fisso +€75 | -€19.263,69 | -€14.987,62 |
| 13 | Take profit fisso +€50 | -€35.270,27 | -€30.994,20 |
| 14 | Take profit fisso +€25 | -€43.690,09 | -€39.414,01 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
