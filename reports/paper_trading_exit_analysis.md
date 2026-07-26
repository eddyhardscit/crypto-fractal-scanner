# Analisi uscite paper trading a leva

Generato: 2026-07-26T05:09:09+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **1641**
- Trade con percorso cronologico utilizzabile: **1587**
- Trade che hanno raggiunto almeno +€50: **789**
- Di questi, chiusi poi in perdita: **168**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€9.465,12 | +€4.331,22 |
| 2 | Chiude 50% a +€50 | +€5.461,15 | +€327,25 |
| 3 | Protegge +€20 dopo +€50 | +€5.178,25 | +€44,35 |
| 4 | Strategia attuale | +€5.133,90 | €0,00 |
| 5 | Take profit fisso +€200 | +€5.133,90 | €0,00 |
| 6 | Take profit fisso +€150 | +€5.133,16 | -€0,74 |
| 7 | Protegge +€30 dopo +€50 | +€5.112,59 | -€21,30 |
| 8 | Take profit fisso +€100 | +€5.069,55 | -€64,35 |
| 9 | Pareggio dopo +€50 | +€4.253,06 | -€880,84 |
| 10 | Trailing 20% dopo +€50 | +€3.541,53 | -€1.592,37 |
| 11 | Take profit fisso +€75 | +€2.250,14 | -€2.883,76 |
| 12 | TP +€50 / SL -€50 | +€88,65 | -€5.045,24 |
| 13 | Take profit fisso +€50 | -€4.104,43 | -€9.238,33 |
| 14 | Take profit fisso +€25 | -€7.625,44 | -€12.759,34 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
