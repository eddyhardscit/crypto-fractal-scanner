# Data quality / coherence check

Generato: 2026-09-08 05:33 UTC

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **OK**

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 78.780 $          | 78.780 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.09000 $         | 0.09000 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 103,29 $          | 103,29 $        | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 78.780 $          | 78.780 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 103,29 $          | 103,29 $        | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.09000 $         | 0.09000 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 78.780 $          | 78.780 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 103,29 $          | 103,29 $        | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.09000 $         | 0.09000 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 78.780 $          | 78.780 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 103,29 $          | 103,29 $        | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.09000 $         | 0.09000 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 78.780 $          | 78.780 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 103,29 $          | 103,29 $        | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.09000 $         | 0.09000 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 78.780 $          | 78.729 $        | -0,0653%     |
| Exchange Microstructure | SOL     | price             | OK      | 103,29 $          | 103,18 $        | -0,1026%     |
| Exchange Microstructure | DOGE    | price             | OK      | 0.09000 $         | 0.08985 $       | -0,1667%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 103,29 $          | 103,29 $        | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 103,29 $          | 103,29 $        | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 103,29 $          | 103,29 $        | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 103,29 $          | 103,29 $        | +0,0000%     |

## Integrità Technical / Classic Visual

- Fibonacci strutturato: **OK**
- Candidati senza falso progresso target: **OK**
- Classic Visual allineato al lifecycle Technical: **OK**

## Controllo codifica UTF-8

Nessun indicatore comune di mojibake trovato.

## File strutturati

- Snapshot condiviso completo: **OK**
- Scanner summary: **OK**
- Price coherence sync: **OK**
- Dati exchange / microstruttura: **OK**

Il workflow è tecnicamente coerente nei controlli disponibili.
