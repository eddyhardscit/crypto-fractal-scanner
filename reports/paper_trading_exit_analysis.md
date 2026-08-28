# Analisi uscite paper trading a leva

Generato: 2026-08-28T07:14:30+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **9426**
- Trade con percorso cronologico utilizzabile: **9372**
- Trade che hanno raggiunto almeno +€50: **3583**
- Di questi, chiusi poi in perdita: **717**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€26.127,82 | +€43.813,88 |
| 2 | Protegge +€30 dopo +€50 | -€3.290,89 | +€14.395,17 |
| 3 | TP +€50 / SL -€50 | -€5.460,51 | +€12.225,55 |
| 4 | Protegge +€20 dopo +€50 | -€8.365,59 | +€9.320,47 |
| 5 | Chiude 50% a +€50 | -€14.309,00 | +€3.377,06 |
| 6 | Trailing 20% dopo +€50 | -€16.494,71 | +€1.191,35 |
| 7 | Pareggio dopo +€50 | -€16.654,67 | +€1.031,39 |
| 8 | Strategia attuale | -€17.686,06 | €0,00 |
| 9 | Take profit fisso +€200 | -€17.686,06 | €0,00 |
| 10 | Take profit fisso +€150 | -€17.696,25 | -€10,19 |
| 11 | Take profit fisso +€100 | -€19.552,72 | -€1.866,66 |
| 12 | Take profit fisso +€75 | -€31.333,74 | -€13.647,68 |
| 13 | Take profit fisso +€50 | -€48.129,51 | -€30.443,45 |
| 14 | Take profit fisso +€25 | -€55.815,03 | -€38.128,97 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
