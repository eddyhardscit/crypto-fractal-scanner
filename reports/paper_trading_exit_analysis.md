# Analisi uscite paper trading a leva

Generato: 2026-08-29T05:14:40+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **9609**
- Trade con percorso cronologico utilizzabile: **9555**
- Trade che hanno raggiunto almeno +€50: **3622**
- Di questi, chiusi poi in perdita: **744**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€22.395,26 | +€43.942,98 |
| 2 | Protegge +€30 dopo +€50 | -€6.987,69 | +€14.560,04 |
| 3 | TP +€50 / SL -€50 | -€9.213,62 | +€12.334,10 |
| 4 | Protegge +€20 dopo +€50 | -€12.086,73 | +€9.461,00 |
| 5 | Chiude 50% a +€50 | -€17.210,19 | +€4.337,54 |
| 6 | Trailing 20% dopo +€50 | -€20.107,63 | +€1.440,10 |
| 7 | Pareggio dopo +€50 | -€20.415,81 | +€1.131,91 |
| 8 | Strategia attuale | -€21.547,73 | €0,00 |
| 9 | Take profit fisso +€200 | -€21.547,73 | €0,00 |
| 10 | Take profit fisso +€150 | -€21.557,91 | -€10,19 |
| 11 | Take profit fisso +€100 | -€23.414,39 | -€1.866,66 |
| 12 | Take profit fisso +€75 | -€35.219,60 | -€13.671,87 |
| 13 | Take profit fisso +€50 | -€52.011,17 | -€30.463,44 |
| 14 | Take profit fisso +€25 | -€57.159,96 | -€35.612,23 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
