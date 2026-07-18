# Analisi uscite paper trading a leva

Generato: 2026-07-18T05:08:34+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **174**
- Trade con percorso cronologico utilizzabile: **120**
- Trade che hanno raggiunto almeno +€50: **82**
- Di questi, chiusi poi in perdita: **14**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Protegge +€30 dopo +€50 | +€2.575,71 | +€189,46 |
| 2 | Protegge +€20 dopo +€50 | +€2.503,02 | +€116,77 |
| 3 | Stop loss fisso -€50 | +€2.442,46 | +€56,20 |
| 4 | Pareggio dopo +€50 | +€2.440,15 | +€53,90 |
| 5 | Take profit fisso +€100 | +€2.439,38 | +€53,12 |
| 6 | Strategia attuale | +€2.386,26 | €0,00 |
| 7 | Take profit fisso +€150 | +€2.386,26 | €0,00 |
| 8 | Take profit fisso +€200 | +€2.386,26 | €0,00 |
| 9 | Chiude 50% a +€50 | +€2.142,59 | -€243,67 |
| 10 | Trailing 20% dopo +€50 | +€2.047,45 | -€338,80 |
| 11 | Take profit fisso +€75 | +€1.996,10 | -€390,15 |
| 12 | TP +€50 / SL -€50 | +€1.328,12 | -€1.058,14 |
| 13 | Take profit fisso +€50 | +€1.255,93 | -€1.130,33 |
| 14 | Take profit fisso +€25 | +€364,82 | -€2.021,44 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
