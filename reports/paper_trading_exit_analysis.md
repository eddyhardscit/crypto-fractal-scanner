# Analisi uscite paper trading a leva

Generato: 2026-09-05T08:19:02+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **11482**
- Trade con percorso cronologico utilizzabile: **11428**
- Trade che hanno raggiunto almeno +€50: **4239**
- Di questi, chiusi poi in perdita: **823**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€26.011,84 | +€46.069,96 |
| 2 | Protegge +€30 dopo +€50 | -€6.718,88 | +€13.339,24 |
| 3 | Protegge +€20 dopo +€50 | -€13.154,73 | +€6.903,39 |
| 4 | TP +€50 / SL -€50 | -€14.312,57 | +€5.745,55 |
| 5 | Chiude 50% a +€50 | -€16.865,95 | +€3.192,17 |
| 6 | Strategia attuale | -€20.058,12 | €0,00 |
| 7 | Take profit fisso +€200 | -€20.058,12 | €0,00 |
| 8 | Take profit fisso +€150 | -€20.068,31 | -€10,19 |
| 9 | Trailing 20% dopo +€50 | -€22.098,78 | -€2.040,66 |
| 10 | Take profit fisso +€100 | -€22.953,10 | -€2.894,98 |
| 11 | Pareggio dopo +€50 | -€23.275,74 | -€3.217,62 |
| 12 | Take profit fisso +€75 | -€37.721,64 | -€17.663,52 |
| 13 | Take profit fisso +€50 | -€59.228,74 | -€39.170,62 |
| 14 | Take profit fisso +€25 | -€70.478,26 | -€50.420,15 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
