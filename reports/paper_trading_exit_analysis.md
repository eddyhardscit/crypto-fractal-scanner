# Analisi uscite paper trading a leva

Generato: 2026-07-20T05:10:22+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **319**
- Trade con percorso cronologico utilizzabile: **265**
- Trade che hanno raggiunto almeno +€50: **139**
- Di questi, chiusi poi in perdita: **33**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Protegge +€30 dopo +€50 | +€1.939,50 | +€329,21 |
| 2 | Stop loss fisso -€50 | +€1.842,57 | +€232,29 |
| 3 | Protegge +€20 dopo +€50 | +€1.777,22 | +€166,93 |
| 4 | Take profit fisso +€100 | +€1.682,68 | +€72,39 |
| 5 | Pareggio dopo +€50 | +€1.666,36 | +€56,07 |
| 6 | Strategia attuale | +€1.610,29 | €0,00 |
| 7 | Take profit fisso +€150 | +€1.610,29 | €0,00 |
| 8 | Take profit fisso +€200 | +€1.610,29 | €0,00 |
| 9 | Chiude 50% a +€50 | +€1.439,94 | -€170,35 |
| 10 | Trailing 20% dopo +€50 | +€1.050,00 | -€560,29 |
| 11 | Take profit fisso +€75 | +€825,22 | -€785,07 |
| 12 | TP +€50 / SL -€50 | -€98,90 | -€1.709,18 |
| 13 | Take profit fisso +€50 | -€347,17 | -€1.957,46 |
| 14 | Take profit fisso +€25 | -€742,30 | -€2.352,59 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
