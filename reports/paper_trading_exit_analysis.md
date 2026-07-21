# Analisi uscite paper trading a leva

Generato: 2026-07-21T05:08:41+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **416**
- Trade con percorso cronologico utilizzabile: **362**
- Trade che hanno raggiunto almeno +€50: **178**
- Di questi, chiusi poi in perdita: **45**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Protegge +€30 dopo +€50 | +€976,85 | +€506,54 |
| 2 | Stop loss fisso -€50 | +€859,61 | +€389,30 |
| 3 | Protegge +€20 dopo +€50 | +€766,27 | +€295,96 |
| 4 | Chiude 50% a +€50 | +€604,99 | +€134,68 |
| 5 | Pareggio dopo +€50 | +€536,92 | +€66,61 |
| 6 | Take profit fisso +€100 | +€493,45 | +€23,14 |
| 7 | Strategia attuale | +€470,31 | €0,00 |
| 8 | Take profit fisso +€150 | +€470,31 | €0,00 |
| 9 | Take profit fisso +€200 | +€470,31 | €0,00 |
| 10 | Trailing 20% dopo +€50 | +€204,83 | -€265,48 |
| 11 | Take profit fisso +€75 | -€278,05 | -€748,36 |
| 12 | TP +€50 / SL -€50 | -€1.172,53 | -€1.642,84 |
| 13 | Take profit fisso +€50 | -€1.577,82 | -€2.048,13 |
| 14 | Take profit fisso +€25 | -€1.839,49 | -€2.309,80 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
