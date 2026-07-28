# Analisi uscite paper trading a leva

Generato: 2026-07-28T05:09:48+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **2807**
- Trade con percorso cronologico utilizzabile: **2753**
- Trade che hanno raggiunto almeno +€50: **1200**
- Di questi, chiusi poi in perdita: **240**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€7.771,71 | +€10.914,30 |
| 2 | Chiude 50% a +€50 | -€1.311,36 | +€1.831,24 |
| 3 | Protegge +€30 dopo +€50 | -€1.328,79 | +€1.813,81 |
| 4 | Protegge +€20 dopo +€50 | -€2.486,72 | +€655,88 |
| 5 | TP +€50 / SL -€50 | -€2.536,04 | +€606,56 |
| 6 | Trailing 20% dopo +€50 | -€2.792,71 | +€349,89 |
| 7 | Strategia attuale | -€3.142,60 | €0,00 |
| 8 | Take profit fisso +€200 | -€3.142,60 | €0,00 |
| 9 | Take profit fisso +€150 | -€3.146,91 | -€4,32 |
| 10 | Take profit fisso +€100 | -€3.177,45 | -€34,86 |
| 11 | Pareggio dopo +€50 | -€3.715,50 | -€572,91 |
| 12 | Take profit fisso +€75 | -€6.894,77 | -€3.752,17 |
| 13 | Take profit fisso +€50 | -€13.312,21 | -€10.169,62 |
| 14 | Take profit fisso +€25 | -€14.575,36 | -€11.432,76 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
