# Analisi uscite paper trading a leva

Generato: 2026-07-19T05:08:34+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **237**
- Trade con percorso cronologico utilizzabile: **183**
- Trade che hanno raggiunto almeno +€50: **102**
- Di questi, chiusi poi in perdita: **18**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Protegge +€30 dopo +€50 | +€2.040,22 | +€234,80 |
| 2 | Protegge +€20 dopo +€50 | +€1.947,95 | +€142,53 |
| 3 | Stop loss fisso -€50 | +€1.923,48 | +€118,06 |
| 4 | Pareggio dopo +€50 | +€1.860,06 | +€54,64 |
| 5 | Strategia attuale | +€1.805,42 | €0,00 |
| 6 | Take profit fisso +€150 | +€1.805,42 | €0,00 |
| 7 | Take profit fisso +€200 | +€1.805,42 | €0,00 |
| 8 | Take profit fisso +€100 | +€1.773,39 | -€32,03 |
| 9 | Chiude 50% a +€50 | +€1.467,87 | -€337,55 |
| 10 | Trailing 20% dopo +€50 | +€1.351,14 | -€454,28 |
| 11 | Take profit fisso +€75 | +€1.132,13 | -€673,29 |
| 12 | TP +€50 / SL -€50 | +€358,03 | -€1.447,39 |
| 13 | Take profit fisso +€50 | +€223,98 | -€1.581,44 |
| 14 | Take profit fisso +€25 | -€392,04 | -€2.197,46 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
