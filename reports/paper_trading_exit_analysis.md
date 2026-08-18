# Analisi uscite paper trading a leva

Generato: 2026-08-18T05:08:58+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **6101**
- Trade con percorso cronologico utilizzabile: **6047**
- Trade che hanno raggiunto almeno +€50: **2270**
- Di questi, chiusi poi in perdita: **474**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | -€3.071,33 | +€29.670,87 |
| 2 | TP +€50 / SL -€50 | -€17.443,19 | +€15.299,02 |
| 3 | Protegge +€30 dopo +€50 | -€24.714,70 | +€8.027,50 |
| 4 | Chiude 50% a +€50 | -€27.147,21 | +€5.594,99 |
| 5 | Protegge +€20 dopo +€50 | -€28.063,17 | +€4.679,04 |
| 6 | Strategia attuale | -€32.742,20 | €0,00 |
| 7 | Take profit fisso +€200 | -€32.742,20 | €0,00 |
| 8 | Take profit fisso +€150 | -€32.746,52 | -€4,32 |
| 9 | Trailing 20% dopo +€50 | -€32.992,63 | -€250,43 |
| 10 | Take profit fisso +€100 | -€33.140,02 | -€397,82 |
| 11 | Pareggio dopo +€50 | -€34.034,18 | -€1.291,98 |
| 12 | Take profit fisso +€75 | -€38.559,01 | -€5.816,81 |
| 13 | Take profit fisso +€50 | -€46.154,10 | -€13.411,90 |
| 14 | Take profit fisso +€25 | -€50.819,87 | -€18.077,67 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
