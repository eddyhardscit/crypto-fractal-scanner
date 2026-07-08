# Storico frattale SOL/BTC

Generato: **2026-07-08 19:09:40 CEST**  
UTC: **2026-07-08 17:09:40 UTC**

Questo file salva giorno per giorno la lettura del frattale **BTC novembre 2022 vs SOL giugno 2026**.

Serve per vedere se SOL sta seguendo il percorso BTC-scalato, se si sta avvicinando, se si sta staccando sopra, oppure se sta perdendo aderenza.

Il CSV completo è: `sol_btc_fractal_history.csv`.

## Stato archivio

| Voce | Valore |
| --- | --- |
| Prima rilevazione salvata | 2026-11-05 |
| Ultima rilevazione salvata | 2026-11-05 |
| Righe salvate | 1 |

## Ultima lettura

| Voce | Valore |
| --- | --- |
| Data | 2026-11-05 |
| Prezzo SOL | 76,01 $ |
| BTC scalato | 140,04 $ |
| Gap SOL vs BTC-scalato | n/a |
| Somiglianza totale | +73,97% |
| Fase | FASE ANTICIPATA |
| Tracking | FRATTALE STABILE |
| Errore medio da inizio programma | +22,48% |
| Errore ultimo giorno | n/a |
| Conferma 1 | 104,63 $ |
| Conferma 2 | 114,06 $ |
| Invalidazione soft | 73,30 $ |
| Invalidazione forte | 62,19 $ |
| Target ciclo base da oggi | 573,07 $ |

## Storico compatto giorno per giorno

| Data | SOL | BTC scalato | Gap | Somiglianza | Fase | Tracking | Errore live medio | Errore ultimo | Base 30g | Base 60g | Soft invalid. | Conferma 1 | Target ciclo oggi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-11-05 | 76,01 $ | 140,04 $ | n/a | +73,97% | FASE ANTICIPATA | FRATTALE STABILE | +22,48% | n/a | 104,37 $ | 112,25 $ | 73,30 $ | 104,63 $ | 573,07 $ |

## Aderenza prima e dopo inizio programma

| Data | Aderenza pre | Errore pre | Stato pre | Aderenza live | Errore live | Stato live | Aderenza totale | Errore totale | Stato totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-11-05 | +87,95% | +6,02% | ABBASTANZA ALLINEATO | +55,04% | +22,48% | STACCATO / MOLTO IN ANTICIPO | +81,97% | +9,02% | ABBASTANZA ALLINEATO |

## Storico proiezioni frattali

| Data | Base 7g | Base 14g | Base 30g | Base 60g | Base 90g | Base 120g | Min 30g | Max 30g | Target ciclo oggi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-11-05 | 76,27 $ | 77,87 $ | 104,37 $ | 112,25 $ | 130,16 $ | 127,78 $ | 76,01 $ | 104,63 $ | 573,07 $ |

## Come leggerlo

- **Gap**: quanto SOL è sopra o sotto la linea BTC-scalata.
- **Gap 0-5%**: frattale molto pulito.
- **Gap 5-10%**: frattale buono.
- **Gap 10-15%**: ancora accettabile, ma SOL è in anticipo.
- **Gap 15-25%**: frattale valido, ma meno preciso per prevedere ritracciamenti e date.
- **Gap oltre 25%**: SOL troppo accelerata rispetto al frattale.
- **Errore live medio**: la parte più importante, perché misura da quando abbiamo iniziato a monitorarlo davvero.
- **Base 30g / 60g**: dove dovrebbe andare SOL se segue il percorso BTC equivalente.
- **Soft invalidation**: primo livello dove il frattale si sporca.
- **Invalidazione forte**: sotto il bottom SOL usato, il frattale è quasi rotto.

Nota: se il workflow gira più volte nello stesso giorno, viene tenuta solo l'ultima lettura del giorno.
