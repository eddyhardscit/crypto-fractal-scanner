# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-10-19 07:32:47 CEST**  
UTC: **2026-10-19 05:32:47 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 78.492 $ | 90.886 $ | +40,74% | +15,79% | rimbalzo debole | 90.886 $ | 78.492 $ | +16,00% | -13,64% | spike storicamente più resistente |
| SOL | 100,34 $ | 116,18 $ | +28,00% | +15,79% | rimbalzo poco frequente | 116,18 $ | 100,34 $ | +4,35% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07548 $ | 0,08739 $ | +40,00% | +15,79% | rimbalzo debole | 0,08739 $ | 0,07548 $ | +6,67% | -13,64% | spike storicamente più resistente |

## Spiegazione semplice delle percentuali

Queste percentuali sono **condizionate**.

Vuol dire che il report controlla sempre due passaggi, in ordine:

1. Prima deve succedere la prima cosa.
2. Solo dopo si controlla se succede la seconda cosa.

### Esempio rimbalzo

`Se scende a -5% → poi +10% = 24%`

Vuol dire:

- Lo scanner prende i 40 casi storici più simili.
- Prima guarda quanti sono scesi almeno a -5% dal prezzo iniziale.
- Poi, solo tra quelli che sono scesi, guarda quanti sono arrivati a +10% dal prezzo iniziale.
- Se il risultato è 24%, vuol dire circa 1 caso su 4.

Esempio con prezzo iniziale 100 $:

- -5% = 95 $
- +10% = 110 $
- il movimento reale da 95 $ a 110 $ non è +10%, ma circa +15,79%.

Quindi `poi +10%` non significa +10% dal minimo. Significa +10% dal prezzo iniziale.

### Esempio dump dopo spike

`Se sale a +10% → poi dump -5% = 62%`

Vuol dire:

- Prima il prezzo deve salire almeno a +10% dal prezzo iniziale.
- Poi si controlla se, dopo quello spike, scende fino a -5% dal prezzo iniziale.
- Se il risultato è 62%, vuol dire che questo scarico è successo più di metà delle volte.

Esempio con prezzo iniziale 100 $:

- +10% = 110 $
- -5% = 95 $
- il movimento reale da 110 $ a 95 $ non è -5%, ma circa -13,64%.

Quindi `dump -5%` non significa -5% dallo spike. Significa che torna fino a 5% sotto il prezzo iniziale.

### Soglie controllate

Nel report principale vedi solo la lettura più semplice:

- discesa -5% → rimbalzo +10%
- spike +10% → dump -5%

Nel report dettagliato invece lo scanner controlla anche soglie intermedie:

- discese: -5%, -8%, -10%, -15%
- rimbalzi: +5%, +10%, +15%, +20%
- spike: +5%, +10%, +15%, +20%
- dump: 0%, -5%, -8%, -10%, -15%

---

# Bitcoin — BTC

## Lettura semplice

- BTC: su 40 casi simili, 27 prima sono scesi a -5,00%. Tra quei 27, 11 poi sono rimbalzati fino a +10,00%. Percentuale: +40,74% (11/27). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 4 poi sono scaricati a -5,00%. Percentuale: +16,00% (4/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 78.492 $ | 27/40 | +67,50% | +5,00% | 86.755 $ | 14/27 | +51,85% | +10,53% | MEDIA | 7,1 | 14,4 |
| -5,00% | 78.492 $ | 27/40 | +67,50% | +10,00% | 90.886 $ | 11/27 | +40,74% | +15,79% | BASSA | 7,1 | 17,6 |
| -5,00% | 78.492 $ | 27/40 | +67,50% | +15,00% | 95.017 $ | 8/27 | +29,63% | +21,05% | DEBOLE | 7,1 | 16,1 |
| -5,00% | 78.492 $ | 27/40 | +67,50% | +20,00% | 99.148 $ | 6/27 | +22,22% | +26,32% | DEBOLE | 7,1 | 15,8 |
| -8,00% | 76.014 $ | 23/40 | +57,50% | +5,00% | 86.755 $ | 10/23 | +43,48% | +14,13% | BASSA | 9,8 | 16,0 |
| -8,00% | 76.014 $ | 23/40 | +57,50% | +10,00% | 90.886 $ | 7/23 | +30,43% | +19,57% | DEBOLE | 9,8 | 17,4 |
| -8,00% | 76.014 $ | 23/40 | +57,50% | +15,00% | 95.017 $ | 4/23 | +17,39% | +25,00% | DEBOLE | 9,8 | 13,0 |
| -8,00% | 76.014 $ | 23/40 | +57,50% | +20,00% | 99.148 $ | 3/23 | +13,04% | +30,43% | DEBOLE | 9,8 | 15,7 |
| -10,00% | 74.361 $ | 17/40 | +42,50% | +5,00% | 86.755 $ | 6/17 | +35,29% | +16,67% | BASSA | 11,1 | 19,5 |
| -10,00% | 74.361 $ | 17/40 | +42,50% | +10,00% | 90.886 $ | 5/17 | +29,41% | +22,22% | DEBOLE | 11,1 | 19,0 |
| -10,00% | 74.361 $ | 17/40 | +42,50% | +15,00% | 95.017 $ | 3/17 | +17,65% | +27,78% | DEBOLE | 11,1 | 14,0 |
| -10,00% | 74.361 $ | 17/40 | +42,50% | +20,00% | 99.148 $ | 2/17 | +11,76% | +33,33% | DEBOLE | 11,1 | 18,5 |
| -15,00% | 70.230 $ | 9/40 | +22,50% | +5,00% | 86.755 $ | 2/9 | +22,22% | +23,53% | DEBOLE | 17,7 | 27,0 |
| -15,00% | 70.230 $ | 9/40 | +22,50% | +10,00% | 90.886 $ | 2/9 | +22,22% | +29,41% | DEBOLE | 17,7 | 27,0 |
| -15,00% | 70.230 $ | 9/40 | +22,50% | +15,00% | 95.017 $ | 0/9 | 0,00% | +35,29% | DEBOLE | 17,7 | n/d |
| -15,00% | 70.230 $ | 9/40 | +22,50% | +20,00% | 99.148 $ | 0/9 | 0,00% | +41,18% | DEBOLE | 17,7 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 86.755 $ | 32/40 | +80,00% | prezzo iniziale | 82.623 $ | 19/32 | +59,38% | -4,76% | MEDIA | 7,0 | 13,2 |
| +5,00% | 86.755 $ | 32/40 | +80,00% | -5,00% | 78.492 $ | 13/32 | +40,62% | -9,52% | BASSA | 7,0 | 13,4 |
| +5,00% | 86.755 $ | 32/40 | +80,00% | -8,00% | 76.014 $ | 10/32 | +31,25% | -12,38% | DEBOLE | 7,0 | 14,6 |
| +5,00% | 86.755 $ | 32/40 | +80,00% | -10,00% | 74.361 $ | 7/32 | +21,88% | -14,29% | DEBOLE | 7,0 | 13,6 |
| +5,00% | 86.755 $ | 32/40 | +80,00% | -15,00% | 70.230 $ | 4/32 | +12,50% | -19,05% | DEBOLE | 7,0 | 20,8 |
| +10,00% | 90.886 $ | 25/40 | +62,50% | prezzo iniziale | 82.623 $ | 9/25 | +36,00% | -9,09% | BASSA | 11,8 | 20,4 |
| +10,00% | 90.886 $ | 25/40 | +62,50% | -5,00% | 78.492 $ | 4/25 | +16,00% | -13,64% | DEBOLE | 11,8 | 22,0 |
| +10,00% | 90.886 $ | 25/40 | +62,50% | -8,00% | 76.014 $ | 2/25 | +8,00% | -16,36% | DEBOLE | 11,8 | 20,5 |
| +10,00% | 90.886 $ | 25/40 | +62,50% | -10,00% | 74.361 $ | 2/25 | +8,00% | -18,18% | DEBOLE | 11,8 | 21,0 |
| +10,00% | 90.886 $ | 25/40 | +62,50% | -15,00% | 70.230 $ | 1/25 | +4,00% | -22,73% | DEBOLE | 11,8 | 27,0 |
| +15,00% | 95.017 $ | 19/40 | +47,50% | prezzo iniziale | 82.623 $ | 3/19 | +15,79% | -13,04% | DEBOLE | 14,0 | 20,0 |
| +15,00% | 95.017 $ | 19/40 | +47,50% | -5,00% | 78.492 $ | 3/19 | +15,79% | -17,39% | DEBOLE | 14,0 | 26,0 |
| +15,00% | 95.017 $ | 19/40 | +47,50% | -8,00% | 76.014 $ | 1/19 | +5,26% | -20,00% | DEBOLE | 14,0 | 29,0 |
| +15,00% | 95.017 $ | 19/40 | +47,50% | -10,00% | 74.361 $ | 1/19 | +5,26% | -21,74% | DEBOLE | 14,0 | 30,0 |
| +15,00% | 95.017 $ | 19/40 | +47,50% | -15,00% | 70.230 $ | 0/19 | 0,00% | -26,09% | DEBOLE | 14,0 | n/d |
| +20,00% | 99.148 $ | 16/40 | +40,00% | prezzo iniziale | 82.623 $ | 1/16 | +6,25% | -16,67% | DEBOLE | 17,6 | 25,0 |
| +20,00% | 99.148 $ | 16/40 | +40,00% | -5,00% | 78.492 $ | 1/16 | +6,25% | -20,83% | DEBOLE | 17,6 | 27,0 |
| +20,00% | 99.148 $ | 16/40 | +40,00% | -8,00% | 76.014 $ | 0/16 | 0,00% | -23,33% | DEBOLE | 17,6 | n/d |
| +20,00% | 99.148 $ | 16/40 | +40,00% | -10,00% | 74.361 $ | 0/16 | 0,00% | -25,00% | DEBOLE | 17,6 | n/d |
| +20,00% | 99.148 $ | 16/40 | +40,00% | -15,00% | 70.230 $ | 0/16 | 0,00% | -29,17% | DEBOLE | 17,6 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 25 prima sono scesi a -5,00%. Tra quei 25, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +28,00% (7/25). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 23 prima sono saliti a +10,00%. Tra quei 23, 1 poi sono scaricati a -5,00%. Percentuale: +4,35% (1/23). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 100,34 $ | 25/40 | +62,50% | +5,00% | 110,90 $ | 12/25 | +48,00% | +10,53% | BASSA | 6,4 | 19,3 |
| -5,00% | 100,34 $ | 25/40 | +62,50% | +10,00% | 116,18 $ | 7/25 | +28,00% | +15,79% | DEBOLE | 6,4 | 22,7 |
| -5,00% | 100,34 $ | 25/40 | +62,50% | +15,00% | 121,46 $ | 3/25 | +12,00% | +21,05% | DEBOLE | 6,4 | 20,7 |
| -5,00% | 100,34 $ | 25/40 | +62,50% | +20,00% | 126,74 $ | 3/25 | +12,00% | +26,32% | DEBOLE | 6,4 | 20,7 |
| -8,00% | 97,17 $ | 23/40 | +57,50% | +5,00% | 110,90 $ | 10/23 | +43,48% | +14,13% | BASSA | 8,7 | 18,8 |
| -8,00% | 97,17 $ | 23/40 | +57,50% | +10,00% | 116,18 $ | 6/23 | +26,09% | +19,57% | DEBOLE | 8,7 | 22,8 |
| -8,00% | 97,17 $ | 23/40 | +57,50% | +15,00% | 121,46 $ | 2/23 | +8,70% | +25,00% | DEBOLE | 8,7 | 20,0 |
| -8,00% | 97,17 $ | 23/40 | +57,50% | +20,00% | 126,74 $ | 2/23 | +8,70% | +30,43% | DEBOLE | 8,7 | 20,0 |
| -10,00% | 95,06 $ | 19/40 | +47,50% | +5,00% | 110,90 $ | 6/19 | +31,58% | +16,67% | DEBOLE | 10,9 | 24,2 |
| -10,00% | 95,06 $ | 19/40 | +47,50% | +10,00% | 116,18 $ | 4/19 | +21,05% | +22,22% | DEBOLE | 10,9 | 27,5 |
| -10,00% | 95,06 $ | 19/40 | +47,50% | +15,00% | 121,46 $ | 1/19 | +5,26% | +27,78% | DEBOLE | 10,9 | 30,0 |
| -10,00% | 95,06 $ | 19/40 | +47,50% | +20,00% | 126,74 $ | 1/19 | +5,26% | +33,33% | DEBOLE | 10,9 | 30,0 |
| -15,00% | 89,78 $ | 12/40 | +30,00% | +5,00% | 110,90 $ | 2/12 | +16,67% | +23,53% | DEBOLE | 13,8 | 27,0 |
| -15,00% | 89,78 $ | 12/40 | +30,00% | +10,00% | 116,18 $ | 2/12 | +16,67% | +29,41% | DEBOLE | 13,8 | 27,0 |
| -15,00% | 89,78 $ | 12/40 | +30,00% | +15,00% | 121,46 $ | 0/12 | 0,00% | +35,29% | DEBOLE | 13,8 | n/d |
| -15,00% | 89,78 $ | 12/40 | +30,00% | +20,00% | 126,74 $ | 0/12 | 0,00% | +41,18% | DEBOLE | 13,8 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 110,90 $ | 30/40 | +75,00% | prezzo iniziale | 105,62 $ | 18/30 | +60,00% | -4,76% | MEDIA | 6,6 | 14,1 |
| +5,00% | 110,90 $ | 30/40 | +75,00% | -5,00% | 100,34 $ | 10/30 | +33,33% | -9,52% | DEBOLE | 6,6 | 13,2 |
| +5,00% | 110,90 $ | 30/40 | +75,00% | -8,00% | 97,17 $ | 8/30 | +26,67% | -12,38% | DEBOLE | 6,6 | 15,4 |
| +5,00% | 110,90 $ | 30/40 | +75,00% | -10,00% | 95,06 $ | 6/30 | +20,00% | -14,29% | DEBOLE | 6,6 | 17,3 |
| +5,00% | 110,90 $ | 30/40 | +75,00% | -15,00% | 89,78 $ | 4/30 | +13,33% | -19,05% | DEBOLE | 6,6 | 21,2 |
| +10,00% | 116,18 $ | 23/40 | +57,50% | prezzo iniziale | 105,62 $ | 8/23 | +34,78% | -9,09% | DEBOLE | 11,5 | 18,9 |
| +10,00% | 116,18 $ | 23/40 | +57,50% | -5,00% | 100,34 $ | 1/23 | +4,35% | -13,64% | DEBOLE | 11,5 | 13,0 |
| +10,00% | 116,18 $ | 23/40 | +57,50% | -8,00% | 97,17 $ | 1/23 | +4,35% | -16,36% | DEBOLE | 11,5 | 16,0 |
| +10,00% | 116,18 $ | 23/40 | +57,50% | -10,00% | 95,06 $ | 1/23 | +4,35% | -18,18% | DEBOLE | 11,5 | 16,0 |
| +10,00% | 116,18 $ | 23/40 | +57,50% | -15,00% | 89,78 $ | 0/23 | 0,00% | -22,73% | DEBOLE | 11,5 | n/d |
| +15,00% | 121,46 $ | 14/40 | +35,00% | prezzo iniziale | 105,62 $ | 1/14 | +7,14% | -13,04% | DEBOLE | 12,4 | 19,0 |
| +15,00% | 121,46 $ | 14/40 | +35,00% | -5,00% | 100,34 $ | 0/14 | 0,00% | -17,39% | DEBOLE | 12,4 | n/d |
| +15,00% | 121,46 $ | 14/40 | +35,00% | -8,00% | 97,17 $ | 0/14 | 0,00% | -20,00% | DEBOLE | 12,4 | n/d |
| +15,00% | 121,46 $ | 14/40 | +35,00% | -10,00% | 95,06 $ | 0/14 | 0,00% | -21,74% | DEBOLE | 12,4 | n/d |
| +15,00% | 121,46 $ | 14/40 | +35,00% | -15,00% | 89,78 $ | 0/14 | 0,00% | -26,09% | DEBOLE | 12,4 | n/d |
| +20,00% | 126,74 $ | 12/40 | +30,00% | prezzo iniziale | 105,62 $ | 0/12 | 0,00% | -16,67% | DEBOLE | 15,2 | n/d |
| +20,00% | 126,74 $ | 12/40 | +30,00% | -5,00% | 100,34 $ | 0/12 | 0,00% | -20,83% | DEBOLE | 15,2 | n/d |
| +20,00% | 126,74 $ | 12/40 | +30,00% | -8,00% | 97,17 $ | 0/12 | 0,00% | -23,33% | DEBOLE | 15,2 | n/d |
| +20,00% | 126,74 $ | 12/40 | +30,00% | -10,00% | 95,06 $ | 0/12 | 0,00% | -25,00% | DEBOLE | 15,2 | n/d |
| +20,00% | 126,74 $ | 12/40 | +30,00% | -15,00% | 89,78 $ | 0/12 | 0,00% | -29,17% | DEBOLE | 15,2 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 20 prima sono scesi a -5,00%. Tra quei 20, 8 poi sono rimbalzati fino a +10,00%. Percentuale: +40,00% (8/20). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- DOGE: su 40 casi simili, 30 prima sono saliti a +10,00%. Tra quei 30, 2 poi sono scaricati a -5,00%. Percentuale: +6,67% (2/30). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,07548 $ | 20/40 | +50,00% | +5,00% | 0,08342 $ | 11/20 | +55,00% | +10,53% | MEDIA | 6,5 | 19,7 |
| -5,00% | 0,07548 $ | 20/40 | +50,00% | +10,00% | 0,08739 $ | 8/20 | +40,00% | +15,79% | BASSA | 6,5 | 22,8 |
| -5,00% | 0,07548 $ | 20/40 | +50,00% | +15,00% | 0,09137 $ | 5/20 | +25,00% | +21,05% | DEBOLE | 6,5 | 22,6 |
| -5,00% | 0,07548 $ | 20/40 | +50,00% | +20,00% | 0,09534 $ | 4/20 | +20,00% | +26,32% | DEBOLE | 6,5 | 21,2 |
| -8,00% | 0,07309 $ | 16/40 | +40,00% | +5,00% | 0,08342 $ | 7/16 | +43,75% | +14,13% | BASSA | 9,1 | 19,7 |
| -8,00% | 0,07309 $ | 16/40 | +40,00% | +10,00% | 0,08739 $ | 6/16 | +37,50% | +19,57% | BASSA | 9,1 | 21,8 |
| -8,00% | 0,07309 $ | 16/40 | +40,00% | +15,00% | 0,09137 $ | 3/16 | +18,75% | +25,00% | DEBOLE | 9,1 | 20,3 |
| -8,00% | 0,07309 $ | 16/40 | +40,00% | +20,00% | 0,09534 $ | 3/16 | +18,75% | +30,43% | DEBOLE | 9,1 | 21,0 |
| -10,00% | 0,07150 $ | 11/40 | +27,50% | +5,00% | 0,08342 $ | 3/11 | +27,27% | +16,67% | DEBOLE | 10,5 | 27,7 |
| -10,00% | 0,07150 $ | 11/40 | +27,50% | +10,00% | 0,08739 $ | 3/11 | +27,27% | +22,22% | DEBOLE | 10,5 | 27,7 |
| -10,00% | 0,07150 $ | 11/40 | +27,50% | +15,00% | 0,09137 $ | 1/11 | +9,09% | +27,78% | DEBOLE | 10,5 | 30,0 |
| -10,00% | 0,07150 $ | 11/40 | +27,50% | +20,00% | 0,09534 $ | 1/11 | +9,09% | +33,33% | DEBOLE | 10,5 | 30,0 |
| -15,00% | 0,06753 $ | 7/40 | +17,50% | +5,00% | 0,08342 $ | 2/7 | +28,57% | +23,53% | DEBOLE | 14,9 | 27,0 |
| -15,00% | 0,06753 $ | 7/40 | +17,50% | +10,00% | 0,08739 $ | 2/7 | +28,57% | +29,41% | DEBOLE | 14,9 | 27,0 |
| -15,00% | 0,06753 $ | 7/40 | +17,50% | +15,00% | 0,09137 $ | 0/7 | 0,00% | +35,29% | DEBOLE | 14,9 | n/d |
| -15,00% | 0,06753 $ | 7/40 | +17,50% | +20,00% | 0,09534 $ | 0/7 | 0,00% | +41,18% | DEBOLE | 14,9 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,08342 $ | 34/40 | +85,00% | prezzo iniziale | 0,07945 $ | 19/34 | +55,88% | -4,76% | MEDIA | 5,8 | 11,2 |
| +5,00% | 0,08342 $ | 34/40 | +85,00% | -5,00% | 0,07548 $ | 7/34 | +20,59% | -9,52% | DEBOLE | 5,8 | 12,6 |
| +5,00% | 0,08342 $ | 34/40 | +85,00% | -8,00% | 0,07309 $ | 5/34 | +14,71% | -12,38% | DEBOLE | 5,8 | 13,8 |
| +5,00% | 0,08342 $ | 34/40 | +85,00% | -10,00% | 0,07150 $ | 4/34 | +11,76% | -14,29% | DEBOLE | 5,8 | 16,0 |
| +5,00% | 0,08342 $ | 34/40 | +85,00% | -15,00% | 0,06753 $ | 3/34 | +8,82% | -19,05% | DEBOLE | 5,8 | 23,3 |
| +10,00% | 0,08739 $ | 30/40 | +75,00% | prezzo iniziale | 0,07945 $ | 10/30 | +33,33% | -9,09% | DEBOLE | 10,6 | 14,8 |
| +10,00% | 0,08739 $ | 30/40 | +75,00% | -5,00% | 0,07548 $ | 2/30 | +6,67% | -13,64% | DEBOLE | 10,6 | 12,0 |
| +10,00% | 0,08739 $ | 30/40 | +75,00% | -8,00% | 0,07309 $ | 2/30 | +6,67% | -16,36% | DEBOLE | 10,6 | 13,0 |
| +10,00% | 0,08739 $ | 30/40 | +75,00% | -10,00% | 0,07150 $ | 2/30 | +6,67% | -18,18% | DEBOLE | 10,6 | 13,0 |
| +10,00% | 0,08739 $ | 30/40 | +75,00% | -15,00% | 0,06753 $ | 2/30 | +6,67% | -22,73% | DEBOLE | 10,6 | 26,0 |
| +15,00% | 0,09137 $ | 20/40 | +50,00% | prezzo iniziale | 0,07945 $ | 1/20 | +5,00% | -13,04% | DEBOLE | 12,4 | 14,0 |
| +15,00% | 0,09137 $ | 20/40 | +50,00% | -5,00% | 0,07548 $ | 0/20 | 0,00% | -17,39% | DEBOLE | 12,4 | n/d |
| +15,00% | 0,09137 $ | 20/40 | +50,00% | -8,00% | 0,07309 $ | 0/20 | 0,00% | -20,00% | DEBOLE | 12,4 | n/d |
| +15,00% | 0,09137 $ | 20/40 | +50,00% | -10,00% | 0,07150 $ | 0/20 | 0,00% | -21,74% | DEBOLE | 12,4 | n/d |
| +15,00% | 0,09137 $ | 20/40 | +50,00% | -15,00% | 0,06753 $ | 0/20 | 0,00% | -26,09% | DEBOLE | 12,4 | n/d |
| +20,00% | 0,09534 $ | 15/40 | +37,50% | prezzo iniziale | 0,07945 $ | 0/15 | 0,00% | -16,67% | DEBOLE | 15,1 | n/d |
| +20,00% | 0,09534 $ | 15/40 | +37,50% | -5,00% | 0,07548 $ | 0/15 | 0,00% | -20,83% | DEBOLE | 15,1 | n/d |
| +20,00% | 0,09534 $ | 15/40 | +37,50% | -8,00% | 0,07309 $ | 0/15 | 0,00% | -23,33% | DEBOLE | 15,1 | n/d |
| +20,00% | 0,09534 $ | 15/40 | +37,50% | -10,00% | 0,07150 $ | 0/15 | 0,00% | -25,00% | DEBOLE | 15,1 | n/d |
| +20,00% | 0,09534 $ | 15/40 | +37,50% | -15,00% | 0,06753 $ | 0/15 | 0,00% | -29,17% | DEBOLE | 15,1 | n/d |

---
