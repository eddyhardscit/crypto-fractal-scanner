# Analisi uscite paper trading a leva

Generato: 2026-09-11T05:10:48+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **12801**
- Trade con percorso cronologico utilizzabile: **12747**
- Trade che hanno raggiunto almeno +€50: **4502**
- Di questi, chiusi poi in perdita: **858**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€23.045,04 | +€47.008,02 |
| 2 | Protegge +€30 dopo +€50 | -€10.212,13 | +€13.750,85 |
| 3 | Protegge +€20 dopo +€50 | -€16.965,46 | +€6.997,53 |
| 4 | TP +€50 / SL -€50 | -€19.690,89 | +€4.272,09 |
| 5 | Chiude 50% a +€50 | -€20.511,76 | +€3.451,22 |
| 6 | Strategia attuale | -€23.962,98 | €0,00 |
| 7 | Take profit fisso +€200 | -€23.962,98 | €0,00 |
| 8 | Take profit fisso +€150 | -€23.973,17 | -€10,19 |
| 9 | Trailing 20% dopo +€50 | -€25.709,98 | -€1.747,00 |
| 10 | Take profit fisso +€100 | -€26.774,97 | -€2.811,99 |
| 11 | Pareggio dopo +€50 | -€27.097,41 | -€3.134,43 |
| 12 | Take profit fisso +€75 | -€42.423,62 | -€18.460,63 |
| 13 | Take profit fisso +€50 | -€65.539,51 | -€41.576,53 |
| 14 | Take profit fisso +€25 | -€79.426,54 | -€55.463,55 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
