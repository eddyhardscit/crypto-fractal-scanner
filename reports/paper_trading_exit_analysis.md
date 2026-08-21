# Analisi uscite paper trading a leva

Generato: 2026-08-21T05:09:19+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **7162**
- Trade con percorso cronologico utilizzabile: **7108**
- Trade che hanno raggiunto almeno +€50: **2703**
- Di questi, chiusi poi in perdita: **578**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€6.091,16 | +€40.419,21 |
| 2 | TP +€50 / SL -€50 | -€14.532,02 | +€19.796,02 |
| 3 | Protegge +€30 dopo +€50 | -€22.848,76 | +€11.479,29 |
| 4 | Protegge +€20 dopo +€50 | -€26.842,59 | +€7.485,45 |
| 5 | Chiude 50% a +€50 | -€29.211,14 | +€5.116,90 |
| 6 | Trailing 20% dopo +€50 | -€33.066,43 | +€1.261,61 |
| 7 | Pareggio dopo +€50 | -€33.966,32 | +€361,72 |
| 8 | Strategia attuale | -€34.328,04 | €0,00 |
| 9 | Take profit fisso +€200 | -€34.328,04 | €0,00 |
| 10 | Take profit fisso +€150 | -€34.332,36 | -€4,32 |
| 11 | Take profit fisso +€100 | -€34.764,49 | -€436,45 |
| 12 | Take profit fisso +€75 | -€43.549,09 | -€9.221,05 |
| 13 | Take profit fisso +€25 | -€53.156,44 | -€18.828,39 |
| 14 | Take profit fisso +€50 | -€53.482,77 | -€19.154,72 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
