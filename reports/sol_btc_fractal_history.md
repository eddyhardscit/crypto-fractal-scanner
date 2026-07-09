# Storico frattale SOL/BTC

Generato: **2026-07-09 17:58:48 CEST**  
UTC: **2026-07-09 15:58:48 UTC**

Questo file salva giorno per giorno la lettura del frattale **BTC novembre 2022 vs SOL giugno 2026**.

Serve per vedere se SOL sta seguendo il percorso BTC-scalato, se si sta avvicinando, se si sta staccando sopra, oppure se sta perdendo aderenza.

Il CSV completo è: `sol_btc_fractal_history.csv`.

## Stato archivio

| Voce | Valore |
| --- | --- |
| Prima rilevazione salvata | 2026-07-08 |
| Ultima rilevazione salvata | 2026-07-09 |
| Righe salvate | 4 |

## Ultima lettura

| Voce | Valore |
| --- | --- |
| Data lettura | 2026-07-09 |
| Prezzo SOL | 77,46 $ |
| BTC scalato | 66,37 $ |
| Gap SOL vs BTC-scalato | +16,71% |
| Somiglianza totale | +73,81% |
| Fase | FASE ANTICIPATA |
| Tracking | n/a |
| Errore medio da inizio programma | +21,79% |
| Errore ultimo giorno | +16,71% |
| Conferma 1 | 105,44 $ |
| Conferma 2 | 114,16 $ |
| Invalidazione soft | 73,59 $ |
| Invalidazione forte | 62,19 $ |
| Target ciclo base da oggi | 573,57 $ |

## Storico compatto giorno per giorno

| Data | SOL | BTC scalato | Gap | Somiglianza | Fase | Tracking | Errore live medio | Errore ultimo | Base 30g | Base 60g | Soft invalid. | Conferma 1 | Target ciclo oggi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-08 | 77,45 $ | 66,17 $ | +17,05% | +73,94% | FASE ANTICIPATA | FRATTALE STABILE | +22,55% | +17,05% | 104,76 $ | 112,67 $ | 73,58 $ | 105,03 $ | 575,23 $ |
| 2026-07-09 | 77,46 $ | 66,37 $ | +16,71% | +73,81% | FASE ANTICIPATA | n/a | +21,79% | +16,71% | 105,44 $ | 111,21 $ | 73,59 $ | 105,44 $ | 573,57 $ |
| nan | 77,58 $ | 70,55 $ | +9,96% | +73,80% | nan | nan | +21,83% | +9,96% | 105,65 $ | 111,43 $ | 73,73 $ | 105,65 $ | 574,68 $ |
| nan | 77,58 $ | 70,55 $ | +9,96% | +73,79% | nan | nan | +21,83% | +9,96% | 105,70 $ | 111,48 $ | 73,77 $ | 105,70 $ | 574,97 $ |

## Aderenza prima e dopo inizio programma

| Data | Aderenza pre | Errore pre | Stato pre | Aderenza live | Errore live | Stato live | Aderenza totale | Errore totale | Stato totale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-08 | +87,95% | +6,02% | ABBASTANZA ALLINEATO | +54,89% | +22,55% | STACCATO / MOLTO IN ANTICIPO | +81,94% | +9,03% | ABBASTANZA ALLINEATO |
| 2026-07-09 | +87,95% | +6,02% | ABBASTANZA ALLINEATO | +56,41% | +21,79% | STACCATO / MOLTO IN ANTICIPO | +81,46% | +9,27% | ABBASTANZA ALLINEATO |
| nan | +87,95% | +6,02% | ABBASTANZA ALLINEATO | +56,35% | +21,83% | STACCATO / MOLTO IN ANTICIPO | +81,44% | +9,28% | ABBASTANZA ALLINEATO |
| nan | +87,95% | +6,02% | ABBASTANZA ALLINEATO | +56,33% | +21,83% | STACCATO / MOLTO IN ANTICIPO | +81,44% | +9,28% | ABBASTANZA ALLINEATO |

## Storico proiezioni frattali

| Data | Base 7g | Base 14g | Base 30g | Base 60g | Base 90g | Base 120g | Min 30g | Max 30g | Target ciclo oggi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07-08 | 76,55 $ | 78,16 $ | 104,76 $ | 112,67 $ | 130,65 $ | 128,27 $ | 76,30 $ | 105,03 $ | 575,23 $ |
| 2026-07-09 | 76,08 $ | 77,95 $ | 105,44 $ | 111,21 $ | 126,40 $ | 126,86 $ | 76,08 $ | 105,44 $ | 573,57 $ |
| nan | 76,23 $ | 78,10 $ | 105,65 $ | 111,43 $ | 126,65 $ | 127,10 $ | 76,23 $ | 105,65 $ | 574,68 $ |
| nan | 76,27 $ | 78,14 $ | 105,70 $ | 111,48 $ | 126,71 $ | 127,17 $ | 76,27 $ | 105,70 $ | 574,97 $ |

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
