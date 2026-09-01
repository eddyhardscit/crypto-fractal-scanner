# Analisi uscite paper trading a leva

Generato: 2026-09-01T05:16:22+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **10241**
- Trade con percorso cronologico utilizzabile: **10187**
- Trade che hanno raggiunto almeno +€50: **3817**
- Di questi, chiusi poi in perdita: **788**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€17.668,35 | +€44.573,84 |
| 2 | Protegge +€30 dopo +€50 | -€11.968,90 | +€14.936,58 |
| 3 | TP +€50 / SL -€50 | -€14.193,29 | +€12.712,20 |
| 4 | Protegge +€20 dopo +€50 | -€17.800,74 | +€9.104,75 |
| 5 | Chiude 50% a +€50 | -€21.787,56 | +€5.117,93 |
| 6 | Trailing 20% dopo +€50 | -€25.748,43 | +€1.157,06 |
| 7 | Strategia attuale | -€26.905,49 | €0,00 |
| 8 | Take profit fisso +€200 | -€26.905,49 | €0,00 |
| 9 | Take profit fisso +€150 | -€26.915,67 | -€10,19 |
| 10 | Pareggio dopo +€50 | -€27.195,82 | -€290,33 |
| 11 | Take profit fisso +€100 | -€28.829,48 | -€1.923,99 |
| 12 | Take profit fisso +€75 | -€41.257,39 | -€14.351,90 |
| 13 | Take profit fisso +€50 | -€57.613,34 | -€30.707,85 |
| 14 | Take profit fisso +€25 | -€64.926,70 | -€38.021,21 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
