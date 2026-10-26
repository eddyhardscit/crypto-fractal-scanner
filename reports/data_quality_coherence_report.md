# Data quality / coherence check

Generato: 2026-10-26 06:34 UTC

Questo controllo non modifica punteggi o decisioni. Verifica che tutti i moduli usino lo stesso prezzo corrente e che le nuove regole Technical/Classic Visual siano integre.

## Stato finale: **WARN**

## Avvisi

- Calibrazione rischio in quarantena; moduli sospesi esclusi dalla verifica prezzi correnti. Consultare lab_reduction_status.md.
- 3 campi prezzo superano la tolleranza specifica del modulo.

## Prezzo unico per modulo

| Modulo                  | Asset   | Campo         | Stato   | Prezzo snapshot   | Prezzo modulo   | Differenza   |
|:------------------------|:--------|:--------------|:--------|:------------------|:----------------|:-------------|
| Scanner                 | BTC     | current_price | OK      | 79.856 $          | 79.856 $        | +0,0000%     |
| Scanner                 | DOGE    | current_price | OK      | 0.07658 $         | 0.07658 $       | +0,0000%     |
| Scanner                 | SOL     | current_price | OK      | 100,60 $          | 100,60 $        | +0,0000%     |
| Scanner Forecast        | BTC     | current_price | OK      | 79.856 $          | 79.856 $        | +0,0000%     |
| Scanner Forecast        | SOL     | current_price | OK      | 100,60 $          | 100,60 $        | +0,0000%     |
| Scanner Forecast        | DOGE    | current_price | OK      | 0.07658 $         | 0.07658 $       | +0,0000%     |
| Technical Structure     | BTC     | price         | OK      | 79.856 $          | 79.856 $        | +0,0000%     |
| Technical Structure     | SOL     | price         | OK      | 100,60 $          | 100,60 $        | +0,0000%     |
| Technical Structure     | DOGE    | price         | OK      | 0.07658 $         | 0.07658 $       | +0,0000%     |
| Classic Technical       | BTC     | price         | OK      | 79.856 $          | 79.856 $        | +0,0000%     |
| Classic Technical       | SOL     | price         | OK      | 100,60 $          | 100,60 $        | +0,0000%     |
| Classic Technical       | DOGE    | price         | OK      | 0.07658 $         | 0.07658 $       | +0,0000%     |
| Classic Visual          | BTC     | price         | OK      | 79.856 $          | 79.856 $        | +0,0000%     |
| Classic Visual          | SOL     | price         | OK      | 100,60 $          | 100,60 $        | +0,0000%     |
| Classic Visual          | DOGE    | price         | OK      | 0.07658 $         | 0.07658 $       | +0,0000%     |
| Exchange Microstructure | BTC     | price         | WARN    | 79.856 $          | 80.106 $        | +0,3132%     |
| Exchange Microstructure | SOL     | price         | WARN    | 100,60 $          | 101,14 $        | +0,5348%     |
| Exchange Microstructure | DOGE    | price         | WARN    | 0.07658 $         | 0.07702 $       | +0,5746%     |

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
