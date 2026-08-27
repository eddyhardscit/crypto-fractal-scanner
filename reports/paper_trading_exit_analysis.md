# Analisi uscite paper trading a leva

Generato: 2026-08-27T05:14:16+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **8971**
- Trade con percorso cronologico utilizzabile: **8917**
- Trade che hanno raggiunto almeno +€50: **3376**
- Di questi, chiusi poi in perdita: **699**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€20.681,32 | +€43.486,17 |
| 2 | Protegge +€30 dopo +€50 | -€8.372,79 | +€14.432,06 |
| 3 | TP +€50 / SL -€50 | -€8.676,39 | +€14.128,46 |
| 4 | Protegge +€20 dopo +€50 | -€13.389,93 | +€9.414,92 |
| 5 | Chiude 50% a +€50 | -€19.169,61 | +€3.635,24 |
| 6 | Pareggio dopo +€50 | -€21.416,63 | +€1.388,22 |
| 7 | Trailing 20% dopo +€50 | -€21.463,88 | +€1.340,97 |
| 8 | Strategia attuale | -€22.804,85 | €0,00 |
| 9 | Take profit fisso +€200 | -€22.804,85 | €0,00 |
| 10 | Take profit fisso +€150 | -€22.815,04 | -€10,19 |
| 11 | Take profit fisso +€100 | -€24.504,59 | -€1.699,74 |
| 12 | Take profit fisso +€75 | -€36.760,54 | -€13.955,70 |
| 13 | Take profit fisso +€50 | -€51.025,02 | -€28.220,17 |
| 14 | Take profit fisso +€25 | -€55.686,21 | -€32.881,36 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
