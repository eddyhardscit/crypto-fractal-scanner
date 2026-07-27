# Analisi uscite paper trading a leva

Generato: 2026-07-27T05:09:29+00:00

> Analisi osservativa: non modifica ingressi, uscite o rischio del paper trading.

## Verifica del target +€50

- Trade chiusi: **2106**
- Trade con percorso cronologico utilizzabile: **2052**
- Trade che hanno raggiunto almeno +€50: **928**
- Di questi, chiusi poi in perdita: **193**

## Confronto simulazioni

| Posizione | Regola di uscita | P&L simulato | Differenza dall'attuale |
| ---: | --- | ---: | ---: |
| 1 | Stop loss fisso -€50 | +€6.227,91 | +€8.937,89 |
| 2 | Chiude 50% a +€50 | -€1.229,98 | +€1.479,99 |
| 3 | Protegge +€30 dopo +€50 | -€1.886,03 | +€823,94 |
| 4 | TP +€50 / SL -€50 | -€2.178,74 | +€531,24 |
| 5 | Protegge +€20 dopo +€50 | -€2.328,79 | +€381,19 |
| 6 | Strategia attuale | -€2.709,98 | €0,00 |
| 7 | Take profit fisso +€200 | -€2.709,98 | €0,00 |
| 8 | Take profit fisso +€150 | -€2.710,72 | -€0,74 |
| 9 | Take profit fisso +€100 | -€2.769,63 | -€59,65 |
| 10 | Trailing 20% dopo +€50 | -€2.861,50 | -€151,52 |
| 11 | Pareggio dopo +€50 | -€3.552,84 | -€842,87 |
| 12 | Take profit fisso +€75 | -€5.796,32 | -€3.086,34 |
| 13 | Take profit fisso +€50 | -€10.978,49 | -€8.268,51 |
| 14 | Take profit fisso +€25 | -€15.077,03 | -€12.367,06 |

## Limiti metodologici

Le simulazioni usano i campioni cronologici salvati a ogni ciclo. Non presumono l'ordine interno dei movimenti tra due campioni. Le decisioni operative restano invariate finché il campione non sarà sufficiente.
