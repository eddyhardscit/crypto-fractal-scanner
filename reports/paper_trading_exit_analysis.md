# Analisi uscite paper trading a leva

Generato: 2026-08-25T05:12:37+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **8564**
- Trade con percorso cronologico utilizzabile: **8510**
- Trade che hanno raggiunto almeno +€50: **3266**
- Di questi, chiusi poi in perdita: **671**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€26.244,41 | +€42.998,90 |
| 2 | Protegge +€30 dopo +€50 | -€2.428,56 | +€14.325,94 |
| 3 | TP +€50 / SL -€50 | -€2.556,90 | +€14.197,60 |
| 4 | Protegge +€20 dopo +€50 | -€7.361,57 | +€9.392,92 |
| 5 | Chiude 50% a +€50 | -€13.981,05 | +€2.773,44 |
| 6 | Pareggio dopo +€50 | -€15.354,14 | +€1.400,36 |
| 7 | Trailing 20% dopo +€50 | -€15.910,49 | +€844,00 |
| 8 | Strategia attuale | -€16.754,50 | €0,00 |
| 9 | Take profit fisso +€200 | -€16.754,50 | €0,00 |
| 10 | Take profit fisso +€150 | -€16.764,68 | -€10,19 |
| 11 | Take profit fisso +€100 | -€18.458,21 | -€1.703,72 |
| 12 | Take profit fisso +€75 | -€30.537,45 | -€13.782,95 |
| 13 | Take profit fisso +€50 | -€44.418,27 | -€27.663,77 |
| 14 | Take profit fisso +€25 | -€53.106,24 | -€36.351,75 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
