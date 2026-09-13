# Analisi uscite paper trading a leva

Generato: 2026-09-13T05:18:14+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **13036**
- Trade con percorso cronologico utilizzabile: **12982**
- Trade che hanno raggiunto almeno +€50: **4534**
- Di questi, chiusi poi in perdita: **862**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€21.089,05 | +€47.316,45 |
| 2 | Protegge +€30 dopo +€50 | -€12.383,13 | +€13.844,27 |
| 3 | Protegge +€20 dopo +€50 | -€19.165,50 | +€7.061,91 |
| 4 | TP +€50 / SL -€50 | -€22.060,21 | +€4.167,20 |
| 5 | Chiude 50% a +€50 | -€22.791,83 | +€3.435,58 |
| 6 | Strategia attuale | -€26.227,40 | €0,00 |
| 7 | Take profit fisso +€200 | -€26.227,40 | €0,00 |
| 8 | Take profit fisso +€150 | -€26.237,59 | -€10,19 |
| 9 | Trailing 20% dopo +€50 | -€27.815,04 | -€1.587,63 |
| 10 | Take profit fisso +€100 | -€29.099,52 | -€2.872,12 |
| 11 | Pareggio dopo +€50 | -€29.317,45 | -€3.090,05 |
| 12 | Take profit fisso +€75 | -€44.719,34 | -€18.491,93 |
| 13 | Take profit fisso +€50 | -€68.217,26 | -€41.989,85 |
| 14 | Take profit fisso +€25 | -€82.702,69 | -€56.475,29 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
