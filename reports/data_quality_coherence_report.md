# Data quality / coherence check

Generato: 2026-10-13 12:36 UTC

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- Calibrazione rischio in quarantena; moduli sospesi esclusi dalla verifica prezzi correnti. Consultare lab_reduction_status.md.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo         | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:--------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price | OK      | 83.631 $          | 83.631 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price | OK      | 0.08469 $         | 0.08469 $       | -0,0000%     |
| Scanner                 | SOL     | current_price | OK      | 108,21 $          | 108,21 $        | +0,0000%     |
| Scanner Forecast        | BTC     | current_price | OK      | 83.631 $          | 83.631 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price | OK      | 108,21 $          | 108,21 $        | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price | OK      | 0.08469 $         | 0.08469 $       | -0,0000%     |
| Technical Structure     | BTC     | price         | OK      | 83.631 $          | 83.631 $        | +0,0000%     |
| Technical Structure     | SOL     | price         | OK      | 108,21 $          | 108,21 $        | +0,0000%     |
| Technical Structure     | DOGE    | price         | OK      | 0.08469 $         | 0.08469 $       | -0,0000%     |
| Classic Technical       | BTC     | price         | OK      | 83.631 $          | 83.631 $        | +0,0000%     |
| Classic Technical       | SOL     | price         | OK      | 108,21 $          | 108,21 $        | +0,0000%     |
| Classic Technical       | DOGE    | price         | OK      | 0.08469 $         | 0.08469 $       | -0,0000%     |
| Classic Visual          | BTC     | price         | OK      | 83.631 $          | 83.631 $        | +0,0000%     |
| Classic Visual          | SOL     | price         | OK      | 108,21 $          | 108,21 $        | +0,0000%     |
| Classic Visual          | DOGE    | price         | OK      | 0.08469 $         | 0.08469 $       | -0,0000%     |
| Exchange Microstructure | BTC     | price         | OK      | 83.631 $          | 83.469 $        | -0,1941%     |
| Exchange Microstructure | SOL     | price         | OK      | 108,21 $          | 108,16 $        | -0,0434%     |
| Exchange Microstructure | DOGE    | price         | OK      | 0.08469 $         | 0.08465 $       | -0,0472%     |

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
