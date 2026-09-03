# Analisi uscite paper trading a leva

Generato: 2026-09-03T05:17:11+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **10759**
- Trade con percorso cronologico utilizzabile: **10705**
- Trade che hanno raggiunto almeno +€50: **3961**
- Di questi, chiusi poi in perdita: **807**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€14.319,43 | +€45.324,65 |
| 2 | Protegge +€30 dopo +€50 | -€16.635,69 | +€14.369,53 |
| 3 | TP +€50 / SL -€50 | -€19.691,70 | +€11.313,51 |
| 4 | Protegge +€20 dopo +€50 | -€22.635,78 | +€8.369,44 |
| 5 | Chiude 50% a +€50 | -€26.010,02 | +€4.995,20 |
| 6 | Trailing 20% dopo +€50 | -€30.747,92 | +€257,30 |
| 7 | Strategia attuale | -€31.005,22 | €0,00 |
| 8 | Take profit fisso +€200 | -€31.005,22 | €0,00 |
| 9 | Take profit fisso +€150 | -€31.015,40 | -€10,19 |
| 10 | Pareggio dopo +€50 | -€32.302,08 | -€1.296,86 |
| 11 | Take profit fisso +€100 | -€33.003,31 | -€1.998,09 |
| 12 | Take profit fisso +€75 | -€45.926,50 | -€14.921,28 |
| 13 | Take profit fisso +€50 | -€63.862,57 | -€32.857,35 |
| 14 | Take profit fisso +€25 | -€72.455,36 | -€41.450,14 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
