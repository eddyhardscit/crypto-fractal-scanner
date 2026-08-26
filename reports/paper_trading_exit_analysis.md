# Analisi uscite paper trading a leva

Generato: 2026-08-26T05:12:45+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **8753**
- Trade con percorso cronologico utilizzabile: **8699**
- Trade che hanno raggiunto almeno +€50: **3294**
- Di questi, chiusi poi in perdita: **673**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€22.210,51 | +€43.248,05 |
| 2 | Protegge +€30 dopo +€50 | -€6.692,82 | +€14.344,72 |
| 3 | TP +€50 / SL -€50 | -€6.746,04 | +€14.291,51 |
| 4 | Protegge +€20 dopo +€50 | -€11.636,76 | +€9.400,78 |
| 5 | Chiude 50% a +€50 | -€18.222,91 | +€2.814,63 |
| 6 | Pareggio dopo +€50 | -€19.649,33 | +€1.388,22 |
| 7 | Trailing 20% dopo +€50 | -€20.082,88 | +€954,67 |
| 8 | Strategia attuale | -€21.037,55 | €0,00 |
| 9 | Take profit fisso +€200 | -€21.037,55 | €0,00 |
| 10 | Take profit fisso +€150 | -€21.047,74 | -€10,19 |
| 11 | Take profit fisso +€100 | -€22.741,26 | -€1.703,72 |
| 12 | Take profit fisso +€75 | -€34.820,50 | -€13.782,95 |
| 13 | Take profit fisso +€50 | -€48.856,56 | -€27.819,01 |
| 14 | Take profit fisso +€25 | -€56.426,59 | -€35.389,04 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
