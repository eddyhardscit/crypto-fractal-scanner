# Data quality / coherence check

Generato: 2026-09-06 05:33 UTC

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- 2 campi prezzo superano la tolleranza specifica del modulo.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo             | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:------------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price     | OK      | 79.859 $          | 79.859 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price     | OK      | 0.09084 $         | 0.09084 $       | -0,0000%     |
| Scanner                 | SOL     | current_price     | OK      | 106,09 $          | 106,09 $        | +0,0000%     |
| Scanner Forecast        | BTC     | current_price     | OK      | 79.859 $          | 79.859 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price     | OK      | 106,09 $          | 106,09 $        | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price     | OK      | 0.09084 $         | 0.09084 $       | -0,0000%     |
| Technical Structure     | BTC     | price             | OK      | 79.859 $          | 79.859 $        | +0,0000%     |
| Technical Structure     | SOL     | price             | OK      | 106,09 $          | 106,09 $        | +0,0000%     |
| Technical Structure     | DOGE    | price             | OK      | 0.09084 $         | 0.09084 $       | -0,0000%     |
| Classic Technical       | BTC     | price             | OK      | 79.859 $          | 79.859 $        | +0,0000%     |
| Classic Technical       | SOL     | price             | OK      | 106,09 $          | 106,09 $        | +0,0000%     |
| Classic Technical       | DOGE    | price             | OK      | 0.09084 $         | 0.09084 $       | -0,0000%     |
| Classic Visual          | BTC     | price             | OK      | 79.859 $          | 79.859 $        | +0,0000%     |
| Classic Visual          | SOL     | price             | OK      | 106,09 $          | 106,09 $        | +0,0000%     |
| Classic Visual          | DOGE    | price             | OK      | 0.09084 $         | 0.09084 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price             | OK      | 79.859 $          | 79.834 $        | -0,0311%     |
| Exchange Microstructure | SOL     | price             | WARN    | 106,09 $          | 105,78 $        | -0,2931%     |
| Exchange Microstructure | DOGE    | price             | WARN    | 0.09084 $         | 0.09052 $       | -0,3523%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 106,09 $          | 106,09 $        | +0,0000%     |
| RSI top-cycle           | SOL     | current_price     | OK      | 106,09 $          | 106,09 $        | +0,0000%     |
| Frattale BTC/SOL        | SOL     | sol_current_price | OK      | 106,09 $          | 106,09 $        | +0,0000%     |
| Fractal path            | SOL     | current_price     | OK      | 106,09 $          | 106,09 $        | +0,0000%     |

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

Il workflow può continuare, ma gli avvisi sopra vanno verificati.
