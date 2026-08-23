# Analisi uscite paper trading a leva

Generato: 2026-08-23T05:10:02+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **8198**
- Trade con percorso cronologico utilizzabile: **8144**
- Trade che hanno raggiunto almeno +€50: **3156**
- Di questi, chiusi poi in perdita: **645**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€27.574,11 | +€42.633,83 |
| 2 | Protegge +€30 dopo +€50 | -€995,80 | +€14.063,93 |
| 3 | TP +€50 / SL -€50 | -€1.458,00 | +€13.601,73 |
| 4 | Protegge +€20 dopo +€50 | -€5.721,88 | +€9.337,85 |
| 5 | Chiude 50% a +€50 | -€13.385,53 | +€1.674,19 |
| 6 | Pareggio dopo +€50 | -€13.659,37 | +€1.400,36 |
| 7 | Trailing 20% dopo +€50 | -€14.814,81 | +€244,92 |
| 8 | Strategia attuale | -€15.059,72 | €0,00 |
| 9 | Take profit fisso +€200 | -€15.059,72 | €0,00 |
| 10 | Take profit fisso +€150 | -€15.069,91 | -€10,19 |
| 11 | Take profit fisso +€100 | -€16.806,64 | -€1.746,92 |
| 12 | Take profit fisso +€75 | -€28.858,63 | -€13.798,91 |
| 13 | Take profit fisso +€50 | -€42.954,29 | -€27.894,57 |
| 14 | Take profit fisso +€25 | -€50.913,85 | -€35.854,13 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
