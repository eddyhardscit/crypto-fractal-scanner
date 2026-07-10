# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-10 03:34:16 CEST**  
UTC: **2026-07-10 01:34:16 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 60.132 $ | 69.626 $ | +12,50% | +15,79% | rimbalzo poco frequente | 69.626 $ | 60.132 $ | +16,00% | -13,64% | spike storicamente più resistente |
| SOL | 74,41 $ | 86,16 $ | +11,11% | +15,79% | rimbalzo poco frequente | 86,16 $ | 74,41 $ | +26,32% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06952 $ | 0,08050 $ | +8,33% | +15,79% | rimbalzo poco frequente | 0,08050 $ | 0,06952 $ | +69,23% | -13,64% | spike spesso scaricato |

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

- BTC: su 40 casi simili, 16 prima sono scesi a -5,00%. Tra quei 16, 2 poi sono rimbalzati fino a +10,00%. Percentuale: +12,50% (2/16). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- BTC: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 4 poi sono scaricati a -5,00%. Percentuale: +16,00% (4/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 60.132 $ | 16/40 | +40,00% | +5,00% | 66.461 $ | 3/16 | +18,75% | +10,53% | DEBOLE | 14,2 | 16,0 |
| -5,00% | 60.132 $ | 16/40 | +40,00% | +10,00% | 69.626 $ | 2/16 | +12,50% | +15,79% | DEBOLE | 14,2 | 9,5 |
| -5,00% | 60.132 $ | 16/40 | +40,00% | +15,00% | 72.791 $ | 2/16 | +12,50% | +21,05% | DEBOLE | 14,2 | 9,5 |
| -5,00% | 60.132 $ | 16/40 | +40,00% | +20,00% | 75.956 $ | 2/16 | +12,50% | +26,32% | DEBOLE | 14,2 | 10,5 |
| -8,00% | 58.233 $ | 13/40 | +32,50% | +5,00% | 66.461 $ | 3/13 | +23,08% | +14,13% | DEBOLE | 15,2 | 16,0 |
| -8,00% | 58.233 $ | 13/40 | +32,50% | +10,00% | 69.626 $ | 2/13 | +15,38% | +19,57% | DEBOLE | 15,2 | 9,5 |
| -8,00% | 58.233 $ | 13/40 | +32,50% | +15,00% | 72.791 $ | 2/13 | +15,38% | +25,00% | DEBOLE | 15,2 | 9,5 |
| -8,00% | 58.233 $ | 13/40 | +32,50% | +20,00% | 75.956 $ | 2/13 | +15,38% | +30,43% | DEBOLE | 15,2 | 10,5 |
| -10,00% | 56.967 $ | 9/40 | +22,50% | +5,00% | 66.461 $ | 1/9 | +11,11% | +16,67% | DEBOLE | 17,2 | 30,0 |
| -10,00% | 56.967 $ | 9/40 | +22,50% | +10,00% | 69.626 $ | 0/9 | 0,00% | +22,22% | DEBOLE | 17,2 | n/d |
| -10,00% | 56.967 $ | 9/40 | +22,50% | +15,00% | 72.791 $ | 0/9 | 0,00% | +27,78% | DEBOLE | 17,2 | n/d |
| -10,00% | 56.967 $ | 9/40 | +22,50% | +20,00% | 75.956 $ | 0/9 | 0,00% | +33,33% | DEBOLE | 17,2 | n/d |
| -15,00% | 53.802 $ | 5/40 | +12,50% | +5,00% | 66.461 $ | 0/5 | 0,00% | +23,53% | DEBOLE | 16,2 | n/d |
| -15,00% | 53.802 $ | 5/40 | +12,50% | +10,00% | 69.626 $ | 0/5 | 0,00% | +29,41% | DEBOLE | 16,2 | n/d |
| -15,00% | 53.802 $ | 5/40 | +12,50% | +15,00% | 72.791 $ | 0/5 | 0,00% | +35,29% | DEBOLE | 16,2 | n/d |
| -15,00% | 53.802 $ | 5/40 | +12,50% | +20,00% | 75.956 $ | 0/5 | 0,00% | +41,18% | DEBOLE | 16,2 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 66.461 $ | 36/40 | +90,00% | prezzo iniziale | 63.296 $ | 18/36 | +50,00% | -4,76% | MEDIA | 4,4 | 12,5 |
| +5,00% | 66.461 $ | 36/40 | +90,00% | -5,00% | 60.132 $ | 11/36 | +30,56% | -9,52% | DEBOLE | 4,4 | 16,6 |
| +5,00% | 66.461 $ | 36/40 | +90,00% | -8,00% | 58.233 $ | 9/36 | +25,00% | -12,38% | DEBOLE | 4,4 | 17,2 |
| +5,00% | 66.461 $ | 36/40 | +90,00% | -10,00% | 56.967 $ | 6/36 | +16,67% | -14,29% | DEBOLE | 4,4 | 21,7 |
| +5,00% | 66.461 $ | 36/40 | +90,00% | -15,00% | 53.802 $ | 3/36 | +8,33% | -19,05% | DEBOLE | 4,4 | 21,0 |
| +10,00% | 69.626 $ | 25/40 | +62,50% | prezzo iniziale | 63.296 $ | 5/25 | +20,00% | -9,09% | DEBOLE | 6,0 | 11,8 |
| +10,00% | 69.626 $ | 25/40 | +62,50% | -5,00% | 60.132 $ | 4/25 | +16,00% | -13,64% | DEBOLE | 6,0 | 15,2 |
| +10,00% | 69.626 $ | 25/40 | +62,50% | -8,00% | 58.233 $ | 3/25 | +12,00% | -16,36% | DEBOLE | 6,0 | 16,0 |
| +10,00% | 69.626 $ | 25/40 | +62,50% | -10,00% | 56.967 $ | 2/25 | +8,00% | -18,18% | DEBOLE | 6,0 | 22,0 |
| +10,00% | 69.626 $ | 25/40 | +62,50% | -15,00% | 53.802 $ | 1/25 | +4,00% | -22,73% | DEBOLE | 6,0 | 24,0 |
| +15,00% | 72.791 $ | 22/40 | +55,00% | prezzo iniziale | 63.296 $ | 3/22 | +13,64% | -13,04% | DEBOLE | 9,5 | 13,3 |
| +15,00% | 72.791 $ | 22/40 | +55,00% | -5,00% | 60.132 $ | 2/22 | +9,09% | -17,39% | DEBOLE | 9,5 | 24,0 |
| +15,00% | 72.791 $ | 22/40 | +55,00% | -8,00% | 58.233 $ | 1/22 | +4,55% | -20,00% | DEBOLE | 9,5 | 21,0 |
| +15,00% | 72.791 $ | 22/40 | +55,00% | -10,00% | 56.967 $ | 1/22 | +4,55% | -21,74% | DEBOLE | 9,5 | 21,0 |
| +15,00% | 72.791 $ | 22/40 | +55,00% | -15,00% | 53.802 $ | 0/22 | 0,00% | -26,09% | DEBOLE | 9,5 | n/d |
| +20,00% | 75.956 $ | 18/40 | +45,00% | prezzo iniziale | 63.296 $ | 1/18 | +5,56% | -16,67% | DEBOLE | 11,3 | 16,0 |
| +20,00% | 75.956 $ | 18/40 | +45,00% | -5,00% | 60.132 $ | 1/18 | +5,56% | -20,83% | DEBOLE | 11,3 | 28,0 |
| +20,00% | 75.956 $ | 18/40 | +45,00% | -8,00% | 58.233 $ | 0/18 | 0,00% | -23,33% | DEBOLE | 11,3 | n/d |
| +20,00% | 75.956 $ | 18/40 | +45,00% | -10,00% | 56.967 $ | 0/18 | 0,00% | -25,00% | DEBOLE | 11,3 | n/d |
| +20,00% | 75.956 $ | 18/40 | +45,00% | -15,00% | 53.802 $ | 0/18 | 0,00% | -29,17% | DEBOLE | 11,3 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 27 prima sono scesi a -5,00%. Tra quei 27, 3 poi sono rimbalzati fino a +10,00%. Percentuale: +11,11% (3/27). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 19 prima sono saliti a +10,00%. Tra quei 19, 5 poi sono scaricati a -5,00%. Percentuale: +26,32% (5/19). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 74,41 $ | 27/40 | +67,50% | +5,00% | 82,25 $ | 5/27 | +18,52% | +10,53% | DEBOLE | 8,0 | 13,4 |
| -5,00% | 74,41 $ | 27/40 | +67,50% | +10,00% | 86,16 $ | 3/27 | +11,11% | +15,79% | DEBOLE | 8,0 | 10,0 |
| -5,00% | 74,41 $ | 27/40 | +67,50% | +15,00% | 90,08 $ | 1/27 | +3,70% | +21,05% | DEBOLE | 8,0 | 8,0 |
| -5,00% | 74,41 $ | 27/40 | +67,50% | +20,00% | 94,00 $ | 1/27 | +3,70% | +26,32% | DEBOLE | 8,0 | 10,0 |
| -8,00% | 72,06 $ | 22/40 | +55,00% | +5,00% | 82,25 $ | 3/22 | +13,64% | +14,13% | DEBOLE | 10,5 | 21,0 |
| -8,00% | 72,06 $ | 22/40 | +55,00% | +10,00% | 86,16 $ | 2/22 | +9,09% | +19,57% | DEBOLE | 10,5 | 16,5 |
| -8,00% | 72,06 $ | 22/40 | +55,00% | +15,00% | 90,08 $ | 0/22 | 0,00% | +25,00% | DEBOLE | 10,5 | n/d |
| -8,00% | 72,06 $ | 22/40 | +55,00% | +20,00% | 94,00 $ | 0/22 | 0,00% | +30,43% | DEBOLE | 10,5 | n/d |
| -10,00% | 70,50 $ | 21/40 | +52,50% | +5,00% | 82,25 $ | 2/21 | +9,52% | +16,67% | DEBOLE | 11,5 | 16,5 |
| -10,00% | 70,50 $ | 21/40 | +52,50% | +10,00% | 86,16 $ | 2/21 | +9,52% | +22,22% | DEBOLE | 11,5 | 16,5 |
| -10,00% | 70,50 $ | 21/40 | +52,50% | +15,00% | 90,08 $ | 0/21 | 0,00% | +27,78% | DEBOLE | 11,5 | n/d |
| -10,00% | 70,50 $ | 21/40 | +52,50% | +20,00% | 94,00 $ | 0/21 | 0,00% | +33,33% | DEBOLE | 11,5 | n/d |
| -15,00% | 66,58 $ | 14/40 | +35,00% | +5,00% | 82,25 $ | 1/14 | +7,14% | +23,53% | DEBOLE | 12,4 | 15,0 |
| -15,00% | 66,58 $ | 14/40 | +35,00% | +10,00% | 86,16 $ | 1/14 | +7,14% | +29,41% | DEBOLE | 12,4 | 15,0 |
| -15,00% | 66,58 $ | 14/40 | +35,00% | +15,00% | 90,08 $ | 0/14 | 0,00% | +35,29% | DEBOLE | 12,4 | n/d |
| -15,00% | 66,58 $ | 14/40 | +35,00% | +20,00% | 94,00 $ | 0/14 | 0,00% | +41,18% | DEBOLE | 12,4 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 82,25 $ | 25/40 | +62,50% | prezzo iniziale | 78,33 $ | 13/25 | +52,00% | -4,76% | MEDIA | 3,5 | 11,0 |
| +5,00% | 82,25 $ | 25/40 | +62,50% | -5,00% | 74,41 $ | 11/25 | +44,00% | -9,52% | BASSA | 3,5 | 13,5 |
| +5,00% | 82,25 $ | 25/40 | +62,50% | -8,00% | 72,06 $ | 9/25 | +36,00% | -12,38% | BASSA | 3,5 | 15,0 |
| +5,00% | 82,25 $ | 25/40 | +62,50% | -10,00% | 70,50 $ | 8/25 | +32,00% | -14,29% | DEBOLE | 3,5 | 15,5 |
| +5,00% | 82,25 $ | 25/40 | +62,50% | -15,00% | 66,58 $ | 3/25 | +12,00% | -19,05% | DEBOLE | 3,5 | 15,3 |
| +10,00% | 86,16 $ | 19/40 | +47,50% | prezzo iniziale | 78,33 $ | 6/19 | +31,58% | -9,09% | DEBOLE | 7,2 | 12,7 |
| +10,00% | 86,16 $ | 19/40 | +47,50% | -5,00% | 74,41 $ | 5/19 | +26,32% | -13,64% | DEBOLE | 7,2 | 15,2 |
| +10,00% | 86,16 $ | 19/40 | +47,50% | -8,00% | 72,06 $ | 4/19 | +21,05% | -16,36% | DEBOLE | 7,2 | 15,2 |
| +10,00% | 86,16 $ | 19/40 | +47,50% | -10,00% | 70,50 $ | 3/19 | +15,79% | -18,18% | DEBOLE | 7,2 | 15,0 |
| +10,00% | 86,16 $ | 19/40 | +47,50% | -15,00% | 66,58 $ | 2/19 | +10,53% | -22,73% | DEBOLE | 7,2 | 16,0 |
| +15,00% | 90,08 $ | 14/40 | +35,00% | prezzo iniziale | 78,33 $ | 2/14 | +14,29% | -13,04% | DEBOLE | 11,4 | 14,0 |
| +15,00% | 90,08 $ | 14/40 | +35,00% | -5,00% | 74,41 $ | 1/14 | +7,14% | -17,39% | DEBOLE | 11,4 | 17,0 |
| +15,00% | 90,08 $ | 14/40 | +35,00% | -8,00% | 72,06 $ | 1/14 | +7,14% | -20,00% | DEBOLE | 11,4 | 17,0 |
| +15,00% | 90,08 $ | 14/40 | +35,00% | -10,00% | 70,50 $ | 0/14 | 0,00% | -21,74% | DEBOLE | 11,4 | n/d |
| +15,00% | 90,08 $ | 14/40 | +35,00% | -15,00% | 66,58 $ | 0/14 | 0,00% | -26,09% | DEBOLE | 11,4 | n/d |
| +20,00% | 94,00 $ | 12/40 | +30,00% | prezzo iniziale | 78,33 $ | 0/12 | 0,00% | -16,67% | DEBOLE | 14,0 | n/d |
| +20,00% | 94,00 $ | 12/40 | +30,00% | -5,00% | 74,41 $ | 0/12 | 0,00% | -20,83% | DEBOLE | 14,0 | n/d |
| +20,00% | 94,00 $ | 12/40 | +30,00% | -8,00% | 72,06 $ | 0/12 | 0,00% | -23,33% | DEBOLE | 14,0 | n/d |
| +20,00% | 94,00 $ | 12/40 | +30,00% | -10,00% | 70,50 $ | 0/12 | 0,00% | -25,00% | DEBOLE | 14,0 | n/d |
| +20,00% | 94,00 $ | 12/40 | +30,00% | -15,00% | 66,58 $ | 0/12 | 0,00% | -29,17% | DEBOLE | 14,0 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 36 prima sono scesi a -5,00%. Tra quei 36, 3 poi sono rimbalzati fino a +10,00%. Percentuale: +8,33% (3/36). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 13 prima sono saliti a +10,00%. Tra quei 13, 9 poi sono scaricati a -5,00%. Percentuale: +69,23% (9/13). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike spesso scaricato.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06952 $ | 36/40 | +90,00% | +5,00% | 0,07684 $ | 6/36 | +16,67% | +10,53% | DEBOLE | 6,8 | 15,7 |
| -5,00% | 0,06952 $ | 36/40 | +90,00% | +10,00% | 0,08050 $ | 3/36 | +8,33% | +15,79% | DEBOLE | 6,8 | 9,7 |
| -5,00% | 0,06952 $ | 36/40 | +90,00% | +15,00% | 0,08416 $ | 3/36 | +8,33% | +21,05% | DEBOLE | 6,8 | 13,3 |
| -5,00% | 0,06952 $ | 36/40 | +90,00% | +20,00% | 0,08782 $ | 3/36 | +8,33% | +26,32% | DEBOLE | 6,8 | 14,3 |
| -8,00% | 0,06733 $ | 34/40 | +85,00% | +5,00% | 0,07684 $ | 4/34 | +11,76% | +14,13% | DEBOLE | 8,8 | 19,8 |
| -8,00% | 0,06733 $ | 34/40 | +85,00% | +10,00% | 0,08050 $ | 1/34 | +2,94% | +19,57% | DEBOLE | 8,8 | 12,0 |
| -8,00% | 0,06733 $ | 34/40 | +85,00% | +15,00% | 0,08416 $ | 1/34 | +2,94% | +25,00% | DEBOLE | 8,8 | 21,0 |
| -8,00% | 0,06733 $ | 34/40 | +85,00% | +20,00% | 0,08782 $ | 1/34 | +2,94% | +30,43% | DEBOLE | 8,8 | 22,0 |
| -10,00% | 0,06586 $ | 32/40 | +80,00% | +5,00% | 0,07684 $ | 3/32 | +9,38% | +16,67% | DEBOLE | 9,4 | 22,3 |
| -10,00% | 0,06586 $ | 32/40 | +80,00% | +10,00% | 0,08050 $ | 0/32 | 0,00% | +22,22% | DEBOLE | 9,4 | n/d |
| -10,00% | 0,06586 $ | 32/40 | +80,00% | +15,00% | 0,08416 $ | 0/32 | 0,00% | +27,78% | DEBOLE | 9,4 | n/d |
| -10,00% | 0,06586 $ | 32/40 | +80,00% | +20,00% | 0,08782 $ | 0/32 | 0,00% | +33,33% | DEBOLE | 9,4 | n/d |
| -15,00% | 0,06220 $ | 29/40 | +72,50% | +5,00% | 0,07684 $ | 2/29 | +6,90% | +23,53% | DEBOLE | 11,2 | 21,0 |
| -15,00% | 0,06220 $ | 29/40 | +72,50% | +10,00% | 0,08050 $ | 0/29 | 0,00% | +29,41% | DEBOLE | 11,2 | n/d |
| -15,00% | 0,06220 $ | 29/40 | +72,50% | +15,00% | 0,08416 $ | 0/29 | 0,00% | +35,29% | DEBOLE | 11,2 | n/d |
| -15,00% | 0,06220 $ | 29/40 | +72,50% | +20,00% | 0,08782 $ | 0/29 | 0,00% | +41,18% | DEBOLE | 11,2 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07684 $ | 20/40 | +50,00% | prezzo iniziale | 0,07318 $ | 17/20 | +85,00% | -4,76% | ALTA | 7,0 | 11,7 |
| +5,00% | 0,07684 $ | 20/40 | +50,00% | -5,00% | 0,06952 $ | 15/20 | +75,00% | -9,52% | ALTA | 7,0 | 15,7 |
| +5,00% | 0,07684 $ | 20/40 | +50,00% | -8,00% | 0,06733 $ | 13/20 | +65,00% | -12,38% | ALTA | 7,0 | 15,5 |
| +5,00% | 0,07684 $ | 20/40 | +50,00% | -10,00% | 0,06586 $ | 11/20 | +55,00% | -14,29% | MEDIA | 7,0 | 16,0 |
| +5,00% | 0,07684 $ | 20/40 | +50,00% | -15,00% | 0,06220 $ | 9/20 | +45,00% | -19,05% | BASSA | 7,0 | 14,3 |
| +10,00% | 0,08050 $ | 13/40 | +32,50% | prezzo iniziale | 0,07318 $ | 9/13 | +69,23% | -9,09% | ALTA | 6,8 | 11,4 |
| +10,00% | 0,08050 $ | 13/40 | +32,50% | -5,00% | 0,06952 $ | 9/13 | +69,23% | -13,64% | ALTA | 6,8 | 14,0 |
| +10,00% | 0,08050 $ | 13/40 | +32,50% | -8,00% | 0,06733 $ | 8/13 | +61,54% | -16,36% | MEDIA | 6,8 | 14,5 |
| +10,00% | 0,08050 $ | 13/40 | +32,50% | -10,00% | 0,06586 $ | 7/13 | +53,85% | -18,18% | MEDIA | 6,8 | 15,7 |
| +10,00% | 0,08050 $ | 13/40 | +32,50% | -15,00% | 0,06220 $ | 6/13 | +46,15% | -22,73% | BASSA | 6,8 | 14,7 |
| +15,00% | 0,08416 $ | 7/40 | +17,50% | prezzo iniziale | 0,07318 $ | 3/7 | +42,86% | -13,04% | BASSA | 9,3 | 10,7 |
| +15,00% | 0,08416 $ | 7/40 | +17,50% | -5,00% | 0,06952 $ | 3/7 | +42,86% | -17,39% | BASSA | 9,3 | 10,7 |
| +15,00% | 0,08416 $ | 7/40 | +17,50% | -8,00% | 0,06733 $ | 3/7 | +42,86% | -20,00% | BASSA | 9,3 | 11,0 |
| +15,00% | 0,08416 $ | 7/40 | +17,50% | -10,00% | 0,06586 $ | 2/7 | +28,57% | -21,74% | DEBOLE | 9,3 | 12,5 |
| +15,00% | 0,08416 $ | 7/40 | +17,50% | -15,00% | 0,06220 $ | 2/7 | +28,57% | -26,09% | DEBOLE | 9,3 | 13,0 |
| +20,00% | 0,08782 $ | 5/40 | +12,50% | prezzo iniziale | 0,07318 $ | 3/5 | +60,00% | -16,67% | MEDIA | 11,6 | 16,7 |
| +20,00% | 0,08782 $ | 5/40 | +12,50% | -5,00% | 0,06952 $ | 2/5 | +40,00% | -20,83% | BASSA | 11,6 | 11,5 |
| +20,00% | 0,08782 $ | 5/40 | +12,50% | -8,00% | 0,06733 $ | 2/5 | +40,00% | -23,33% | BASSA | 11,6 | 12,0 |
| +20,00% | 0,08782 $ | 5/40 | +12,50% | -10,00% | 0,06586 $ | 2/5 | +40,00% | -25,00% | BASSA | 11,6 | 12,5 |
| +20,00% | 0,08782 $ | 5/40 | +12,50% | -15,00% | 0,06220 $ | 2/5 | +40,00% | -29,17% | BASSA | 11,6 | 13,0 |

---
