# Analisi uscite paper trading a leva

Generato: 2026-08-24T05:12:39+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **8365**
- Trade con percorso cronologico utilizzabile: **8311**
- Trade che hanno raggiunto almeno +€50: **3211**
- Di questi, chiusi poi in perdita: **646**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€28.605,73 | +€42.771,96 |
| 2 | Protegge +€30 dopo +€50 | +€35,05 | +€14.201,28 |
| 3 | TP +€50 / SL -€50 | -€353,69 | +€13.812,54 |
| 4 | Protegge +€20 dopo +€50 | -€4.808,02 | +€9.358,21 |
| 5 | Chiude 50% a +€50 | -€12.287,85 | +€1.878,38 |
| 6 | Pareggio dopo +€50 | -€12.765,87 | +€1.400,36 |
| 7 | Trailing 20% dopo +€50 | -€13.335,40 | +€830,82 |
| 8 | Strategia attuale | -€14.166,23 | €0,00 |
| 9 | Take profit fisso +€200 | -€14.166,23 | €0,00 |
| 10 | Take profit fisso +€150 | -€14.176,42 | -€10,19 |
| 11 | Take profit fisso +€100 | -€15.869,94 | -€1.703,72 |
| 12 | Take profit fisso +€75 | -€27.903,48 | -€13.737,25 |
| 13 | Take profit fisso +€50 | -€41.988,11 | -€27.821,88 |
| 14 | Take profit fisso +€25 | -€50.946,93 | -€36.780,70 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
