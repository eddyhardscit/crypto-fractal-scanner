# Data quality / coherence check

Generato: 2026-09-27 05:33 UTC

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **OK**

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 84.377 $          | 84.377 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.09591 $         | 0.09591 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 120,68 $          | 120,68 $        | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 84.377 $          | 84.377 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 120,68 $          | 120,68 $        | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.09591 $         | 0.09591 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 84.377 $          | 84.377 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 120,68 $          | 120,68 $        | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.09591 $         | 0.09591 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 84.377 $          | 84.377 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 120,68 $          | 120,68 $        | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.09591 $         | 0.09591 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 84.377 $          | 84.377 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 120,68 $          | 120,68 $        | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.09591 $         | 0.09591 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 84.377 $          | 84.360 $        | -0,0203%     |
| Exchange Microstructure | SOL     | price             | OK      | 120,68 $          | 120,44 $        | -0,1947%     |
| Exchange Microstructure | DOGE    | price             | OK      | 0.09591 $         | 0.09583 $       | -0,0847%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 120,68 $          | 120,68 $        | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 120,68 $          | 120,68 $        | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 120,68 $          | 120,68 $        | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 120,68 $          | 120,68 $        | +0,0000%     |

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
