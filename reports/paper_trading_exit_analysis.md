# Analisi uscite paper trading a leva

Generato: 2026-09-02T05:16:40+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **10478**
- Trade con percorso cronologico utilizzabile: **10424**
- Trade che hanno raggiunto almeno +€50: **3885**
- Di questi, chiusi poi in perdita: **804**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€15.759,27 | +€45.093,44 |
| 2 | Protegge +€30 dopo +€50 | -€15.014,12 | +€14.320,05 |
| 3 | TP +€50 / SL -€50 | -€17.234,20 | +€12.099,97 |
| 4 | Protegge +€20 dopo +€50 | -€20.975,95 | +€8.358,22 |
| 5 | Chiude 50% a +€50 | -€24.185,01 | +€5.149,16 |
| 6 | Trailing 20% dopo +€50 | -€29.207,61 | +€126,56 |
| 7 | Strategia attuale | -€29.334,17 | €0,00 |
| 8 | Take profit fisso +€200 | -€29.334,17 | €0,00 |
| 9 | Take profit fisso +€150 | -€29.344,36 | -€10,19 |
| 10 | Pareggio dopo +€50 | -€30.631,03 | -€1.296,86 |
| 11 | Take profit fisso +€100 | -€31.371,68 | -€2.037,51 |
| 12 | Take profit fisso +€75 | -€44.042,25 | -€14.708,08 |
| 13 | Take profit fisso +€50 | -€61.173,85 | -€31.839,68 |
| 14 | Take profit fisso +€25 | -€69.092,45 | -€39.758,28 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
