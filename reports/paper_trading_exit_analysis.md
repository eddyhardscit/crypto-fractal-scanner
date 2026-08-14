# Analisi uscite paper trading a leva

Generato: 2026-08-14T10:13:20+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **4954**
- Trade con percorso cronologico utilizzabile: **4900**
- Trade che hanno raggiunto almeno +€50: **1851**
- Di questi, chiusi poi in perdita: **362**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | -€6.108,55 | +€19.046,04 |
| 2 | TP +€50 / SL -€50 | -€17.871,43 | +€7.283,16 |
| 3 | Protegge +€30 dopo +€50 | -€20.177,14 | +€4.977,45 |
| 4 | Chiude 50% a +€50 | -€20.765,25 | +€4.389,34 |
| 5 | Protegge +€20 dopo +€50 | -€22.594,32 | +€2.560,27 |
| 6 | Trailing 20% dopo +€50 | -€25.123,00 | +€31,59 |
| 7 | Strategia attuale | -€25.154,59 | €0,00 |
| 8 | Take profit fisso +€200 | -€25.154,59 | €0,00 |
| 9 | Take profit fisso +€150 | -€25.158,91 | -€4,32 |
| 10 | Take profit fisso +€100 | -€25.673,51 | -€518,92 |
| 11 | Pareggio dopo +€50 | -€26.553,62 | -€1.399,03 |
| 12 | Take profit fisso +€75 | -€30.169,33 | -€5.014,74 |
| 13 | Take profit fisso +€50 | -€36.724,75 | -€11.570,16 |
| 14 | Take profit fisso +€25 | -€41.607,36 | -€16.452,77 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
