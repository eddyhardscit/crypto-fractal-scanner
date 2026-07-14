# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-14 09:21:54 CEST**  
UTC: **2026-07-14 07:21:54 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 59.127 $ | 68.463 $ | +33,33% | +15,79% | rimbalzo poco frequente | 68.463 $ | 59.127 $ | +13,04% | -13,64% | spike storicamente più resistente |
| SOL | 71,12 $ | 82,35 $ | +14,29% | +15,79% | rimbalzo poco frequente | 82,35 $ | 71,12 $ | +18,75% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06826 $ | 0,07904 $ | +11,11% | +15,79% | rimbalzo poco frequente | 0,07904 $ | 0,06826 $ | +60,00% | -13,64% | attenzione a prendere profitto |

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

- BTC: su 40 casi simili, 21 prima sono scesi a -5,00%. Tra quei 21, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +33,33% (7/21). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- BTC: su 40 casi simili, 23 prima sono saliti a +10,00%. Tra quei 23, 3 poi sono scaricati a -5,00%. Percentuale: +13,04% (3/23). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 59.127 $ | 21/40 | +52,50% | +5,00% | 65.351 $ | 9/21 | +42,86% | +10,53% | BASSA | 9,7 | 22,1 |
| -5,00% | 59.127 $ | 21/40 | +52,50% | +10,00% | 68.463 $ | 7/21 | +33,33% | +15,79% | DEBOLE | 9,7 | 24,9 |
| -5,00% | 59.127 $ | 21/40 | +52,50% | +15,00% | 71.575 $ | 4/21 | +19,05% | +21,05% | DEBOLE | 9,7 | 27,8 |
| -5,00% | 59.127 $ | 21/40 | +52,50% | +20,00% | 74.687 $ | 3/21 | +14,29% | +26,32% | DEBOLE | 9,7 | 28,0 |
| -8,00% | 57.260 $ | 16/40 | +40,00% | +5,00% | 65.351 $ | 4/16 | +25,00% | +14,13% | DEBOLE | 13,2 | 23,2 |
| -8,00% | 57.260 $ | 16/40 | +40,00% | +10,00% | 68.463 $ | 2/16 | +12,50% | +19,57% | DEBOLE | 13,2 | 22,0 |
| -8,00% | 57.260 $ | 16/40 | +40,00% | +15,00% | 71.575 $ | 1/16 | +6,25% | +25,00% | DEBOLE | 13,2 | 26,0 |
| -8,00% | 57.260 $ | 16/40 | +40,00% | +20,00% | 74.687 $ | 1/16 | +6,25% | +30,43% | DEBOLE | 13,2 | 26,0 |
| -10,00% | 56.015 $ | 13/40 | +32,50% | +5,00% | 65.351 $ | 3/13 | +23,08% | +16,67% | DEBOLE | 13,0 | 22,3 |
| -10,00% | 56.015 $ | 13/40 | +32,50% | +10,00% | 68.463 $ | 2/13 | +15,38% | +22,22% | DEBOLE | 13,0 | 22,0 |
| -10,00% | 56.015 $ | 13/40 | +32,50% | +15,00% | 71.575 $ | 1/13 | +7,69% | +27,78% | DEBOLE | 13,0 | 26,0 |
| -10,00% | 56.015 $ | 13/40 | +32,50% | +20,00% | 74.687 $ | 1/13 | +7,69% | +33,33% | DEBOLE | 13,0 | 26,0 |
| -15,00% | 52.903 $ | 8/40 | +20,00% | +5,00% | 65.351 $ | 0/8 | 0,00% | +23,53% | DEBOLE | 17,4 | n/d |
| -15,00% | 52.903 $ | 8/40 | +20,00% | +10,00% | 68.463 $ | 0/8 | 0,00% | +29,41% | DEBOLE | 17,4 | n/d |
| -15,00% | 52.903 $ | 8/40 | +20,00% | +15,00% | 71.575 $ | 0/8 | 0,00% | +35,29% | DEBOLE | 17,4 | n/d |
| -15,00% | 52.903 $ | 8/40 | +20,00% | +20,00% | 74.687 $ | 0/8 | 0,00% | +41,18% | DEBOLE | 17,4 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 65.351 $ | 34/40 | +85,00% | prezzo iniziale | 62.239 $ | 22/34 | +64,71% | -4,76% | MEDIA | 4,9 | 13,0 |
| +5,00% | 65.351 $ | 34/40 | +85,00% | -5,00% | 59.127 $ | 14/34 | +41,18% | -9,52% | BASSA | 4,9 | 15,1 |
| +5,00% | 65.351 $ | 34/40 | +85,00% | -8,00% | 57.260 $ | 9/34 | +26,47% | -12,38% | DEBOLE | 4,9 | 16,8 |
| +5,00% | 65.351 $ | 34/40 | +85,00% | -10,00% | 56.015 $ | 7/34 | +20,59% | -14,29% | DEBOLE | 4,9 | 16,4 |
| +5,00% | 65.351 $ | 34/40 | +85,00% | -15,00% | 52.903 $ | 4/34 | +11,76% | -19,05% | DEBOLE | 4,9 | 23,0 |
| +10,00% | 68.463 $ | 23/40 | +57,50% | prezzo iniziale | 62.239 $ | 5/23 | +21,74% | -9,09% | DEBOLE | 11,9 | 12,6 |
| +10,00% | 68.463 $ | 23/40 | +57,50% | -5,00% | 59.127 $ | 3/23 | +13,04% | -13,64% | DEBOLE | 11,9 | 11,7 |
| +10,00% | 68.463 $ | 23/40 | +57,50% | -8,00% | 57.260 $ | 2/23 | +8,70% | -16,36% | DEBOLE | 11,9 | 17,0 |
| +10,00% | 68.463 $ | 23/40 | +57,50% | -10,00% | 56.015 $ | 2/23 | +8,70% | -18,18% | DEBOLE | 11,9 | 17,0 |
| +10,00% | 68.463 $ | 23/40 | +57,50% | -15,00% | 52.903 $ | 0/23 | 0,00% | -22,73% | DEBOLE | 11,9 | n/d |
| +15,00% | 71.575 $ | 18/40 | +45,00% | prezzo iniziale | 62.239 $ | 2/18 | +11,11% | -13,04% | DEBOLE | 12,9 | 18,5 |
| +15,00% | 71.575 $ | 18/40 | +45,00% | -5,00% | 59.127 $ | 0/18 | 0,00% | -17,39% | DEBOLE | 12,9 | n/d |
| +15,00% | 71.575 $ | 18/40 | +45,00% | -8,00% | 57.260 $ | 0/18 | 0,00% | -20,00% | DEBOLE | 12,9 | n/d |
| +15,00% | 71.575 $ | 18/40 | +45,00% | -10,00% | 56.015 $ | 0/18 | 0,00% | -21,74% | DEBOLE | 12,9 | n/d |
| +15,00% | 71.575 $ | 18/40 | +45,00% | -15,00% | 52.903 $ | 0/18 | 0,00% | -26,09% | DEBOLE | 12,9 | n/d |
| +20,00% | 74.687 $ | 14/40 | +35,00% | prezzo iniziale | 62.239 $ | 0/14 | 0,00% | -16,67% | DEBOLE | 14,5 | n/d |
| +20,00% | 74.687 $ | 14/40 | +35,00% | -5,00% | 59.127 $ | 0/14 | 0,00% | -20,83% | DEBOLE | 14,5 | n/d |
| +20,00% | 74.687 $ | 14/40 | +35,00% | -8,00% | 57.260 $ | 0/14 | 0,00% | -23,33% | DEBOLE | 14,5 | n/d |
| +20,00% | 74.687 $ | 14/40 | +35,00% | -10,00% | 56.015 $ | 0/14 | 0,00% | -25,00% | DEBOLE | 14,5 | n/d |
| +20,00% | 74.687 $ | 14/40 | +35,00% | -15,00% | 52.903 $ | 0/14 | 0,00% | -29,17% | DEBOLE | 14,5 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 28 prima sono scesi a -5,00%. Tra quei 28, 4 poi sono rimbalzati fino a +10,00%. Percentuale: +14,29% (4/28). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 16 prima sono saliti a +10,00%. Tra quei 16, 3 poi sono scaricati a -5,00%. Percentuale: +18,75% (3/16). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 71,12 $ | 28/40 | +70,00% | +5,00% | 78,60 $ | 7/28 | +25,00% | +10,53% | DEBOLE | 6,6 | 22,6 |
| -5,00% | 71,12 $ | 28/40 | +70,00% | +10,00% | 82,35 $ | 4/28 | +14,29% | +15,79% | DEBOLE | 6,6 | 20,5 |
| -5,00% | 71,12 $ | 28/40 | +70,00% | +15,00% | 86,09 $ | 3/28 | +10,71% | +21,05% | DEBOLE | 6,6 | 24,3 |
| -5,00% | 71,12 $ | 28/40 | +70,00% | +20,00% | 89,83 $ | 2/28 | +7,14% | +26,32% | DEBOLE | 6,6 | 23,0 |
| -8,00% | 68,87 $ | 25/40 | +62,50% | +5,00% | 78,60 $ | 4/25 | +16,00% | +14,13% | DEBOLE | 9,3 | 22,0 |
| -8,00% | 68,87 $ | 25/40 | +62,50% | +10,00% | 82,35 $ | 3/25 | +12,00% | +19,57% | DEBOLE | 9,3 | 20,7 |
| -8,00% | 68,87 $ | 25/40 | +62,50% | +15,00% | 86,09 $ | 2/25 | +8,00% | +25,00% | DEBOLE | 9,3 | 22,0 |
| -8,00% | 68,87 $ | 25/40 | +62,50% | +20,00% | 89,83 $ | 2/25 | +8,00% | +30,43% | DEBOLE | 9,3 | 23,0 |
| -10,00% | 67,38 $ | 19/40 | +47,50% | +5,00% | 78,60 $ | 2/19 | +10,53% | +16,67% | DEBOLE | 10,1 | 23,5 |
| -10,00% | 67,38 $ | 19/40 | +47,50% | +10,00% | 82,35 $ | 1/19 | +5,26% | +22,22% | DEBOLE | 10,1 | 18,0 |
| -10,00% | 67,38 $ | 19/40 | +47,50% | +15,00% | 86,09 $ | 0/19 | 0,00% | +27,78% | DEBOLE | 10,1 | n/d |
| -10,00% | 67,38 $ | 19/40 | +47,50% | +20,00% | 89,83 $ | 0/19 | 0,00% | +33,33% | DEBOLE | 10,1 | n/d |
| -15,00% | 63,63 $ | 12/40 | +30,00% | +5,00% | 78,60 $ | 0/12 | 0,00% | +23,53% | DEBOLE | 10,4 | n/d |
| -15,00% | 63,63 $ | 12/40 | +30,00% | +10,00% | 82,35 $ | 0/12 | 0,00% | +29,41% | DEBOLE | 10,4 | n/d |
| -15,00% | 63,63 $ | 12/40 | +30,00% | +15,00% | 86,09 $ | 0/12 | 0,00% | +35,29% | DEBOLE | 10,4 | n/d |
| -15,00% | 63,63 $ | 12/40 | +30,00% | +20,00% | 89,83 $ | 0/12 | 0,00% | +41,18% | DEBOLE | 10,4 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 78,60 $ | 24/40 | +60,00% | prezzo iniziale | 74,86 $ | 12/24 | +50,00% | -4,76% | MEDIA | 6,5 | 9,8 |
| +5,00% | 78,60 $ | 24/40 | +60,00% | -5,00% | 71,12 $ | 10/24 | +41,67% | -9,52% | BASSA | 6,5 | 11,0 |
| +5,00% | 78,60 $ | 24/40 | +60,00% | -8,00% | 68,87 $ | 9/24 | +37,50% | -12,38% | BASSA | 6,5 | 14,8 |
| +5,00% | 78,60 $ | 24/40 | +60,00% | -10,00% | 67,38 $ | 6/24 | +25,00% | -14,29% | DEBOLE | 6,5 | 17,0 |
| +5,00% | 78,60 $ | 24/40 | +60,00% | -15,00% | 63,63 $ | 3/24 | +12,50% | -19,05% | DEBOLE | 6,5 | 21,0 |
| +10,00% | 82,35 $ | 16/40 | +40,00% | prezzo iniziale | 74,86 $ | 3/16 | +18,75% | -9,09% | DEBOLE | 11,2 | 8,3 |
| +10,00% | 82,35 $ | 16/40 | +40,00% | -5,00% | 71,12 $ | 3/16 | +18,75% | -13,64% | DEBOLE | 11,2 | 10,0 |
| +10,00% | 82,35 $ | 16/40 | +40,00% | -8,00% | 68,87 $ | 3/16 | +18,75% | -16,36% | DEBOLE | 11,2 | 12,7 |
| +10,00% | 82,35 $ | 16/40 | +40,00% | -10,00% | 67,38 $ | 2/16 | +12,50% | -18,18% | DEBOLE | 11,2 | 13,5 |
| +10,00% | 82,35 $ | 16/40 | +40,00% | -15,00% | 63,63 $ | 0/16 | 0,00% | -22,73% | DEBOLE | 11,2 | n/d |
| +15,00% | 86,09 $ | 13/40 | +32,50% | prezzo iniziale | 74,86 $ | 0/13 | 0,00% | -13,04% | DEBOLE | 12,2 | n/d |
| +15,00% | 86,09 $ | 13/40 | +32,50% | -5,00% | 71,12 $ | 0/13 | 0,00% | -17,39% | DEBOLE | 12,2 | n/d |
| +15,00% | 86,09 $ | 13/40 | +32,50% | -8,00% | 68,87 $ | 0/13 | 0,00% | -20,00% | DEBOLE | 12,2 | n/d |
| +15,00% | 86,09 $ | 13/40 | +32,50% | -10,00% | 67,38 $ | 0/13 | 0,00% | -21,74% | DEBOLE | 12,2 | n/d |
| +15,00% | 86,09 $ | 13/40 | +32,50% | -15,00% | 63,63 $ | 0/13 | 0,00% | -26,09% | DEBOLE | 12,2 | n/d |
| +20,00% | 89,83 $ | 10/40 | +25,00% | prezzo iniziale | 74,86 $ | 0/10 | 0,00% | -16,67% | DEBOLE | 12,5 | n/d |
| +20,00% | 89,83 $ | 10/40 | +25,00% | -5,00% | 71,12 $ | 0/10 | 0,00% | -20,83% | DEBOLE | 12,5 | n/d |
| +20,00% | 89,83 $ | 10/40 | +25,00% | -8,00% | 68,87 $ | 0/10 | 0,00% | -23,33% | DEBOLE | 12,5 | n/d |
| +20,00% | 89,83 $ | 10/40 | +25,00% | -10,00% | 67,38 $ | 0/10 | 0,00% | -25,00% | DEBOLE | 12,5 | n/d |
| +20,00% | 89,83 $ | 10/40 | +25,00% | -15,00% | 63,63 $ | 0/10 | 0,00% | -29,17% | DEBOLE | 12,5 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 36 prima sono scesi a -5,00%. Tra quei 36, 4 poi sono rimbalzati fino a +10,00%. Percentuale: +11,11% (4/36). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 15 prima sono saliti a +10,00%. Tra quei 15, 9 poi sono scaricati a -5,00%. Percentuale: +60,00% (9/15). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06826 $ | 36/40 | +90,00% | +5,00% | 0,07544 $ | 5/36 | +13,89% | +10,53% | DEBOLE | 6,4 | 14,8 |
| -5,00% | 0,06826 $ | 36/40 | +90,00% | +10,00% | 0,07904 $ | 4/36 | +11,11% | +15,79% | DEBOLE | 6,4 | 12,5 |
| -5,00% | 0,06826 $ | 36/40 | +90,00% | +15,00% | 0,08263 $ | 2/36 | +5,56% | +21,05% | DEBOLE | 6,4 | 9,0 |
| -5,00% | 0,06826 $ | 36/40 | +90,00% | +20,00% | 0,08622 $ | 2/36 | +5,56% | +26,32% | DEBOLE | 6,4 | 11,0 |
| -8,00% | 0,06610 $ | 35/40 | +87,50% | +5,00% | 0,07544 $ | 5/35 | +14,29% | +14,13% | DEBOLE | 7,6 | 14,8 |
| -8,00% | 0,06610 $ | 35/40 | +87,50% | +10,00% | 0,07904 $ | 4/35 | +11,43% | +19,57% | DEBOLE | 7,6 | 12,5 |
| -8,00% | 0,06610 $ | 35/40 | +87,50% | +15,00% | 0,08263 $ | 2/35 | +5,71% | +25,00% | DEBOLE | 7,6 | 9,0 |
| -8,00% | 0,06610 $ | 35/40 | +87,50% | +20,00% | 0,08622 $ | 2/35 | +5,71% | +30,43% | DEBOLE | 7,6 | 11,0 |
| -10,00% | 0,06467 $ | 32/40 | +80,00% | +5,00% | 0,07544 $ | 2/32 | +6,25% | +16,67% | DEBOLE | 8,3 | 18,0 |
| -10,00% | 0,06467 $ | 32/40 | +80,00% | +10,00% | 0,07904 $ | 2/32 | +6,25% | +22,22% | DEBOLE | 8,3 | 18,5 |
| -10,00% | 0,06467 $ | 32/40 | +80,00% | +15,00% | 0,08263 $ | 0/32 | 0,00% | +27,78% | DEBOLE | 8,3 | n/d |
| -10,00% | 0,06467 $ | 32/40 | +80,00% | +20,00% | 0,08622 $ | 0/32 | 0,00% | +33,33% | DEBOLE | 8,3 | n/d |
| -15,00% | 0,06107 $ | 29/40 | +72,50% | +5,00% | 0,07544 $ | 2/29 | +6,90% | +23,53% | DEBOLE | 8,1 | 18,0 |
| -15,00% | 0,06107 $ | 29/40 | +72,50% | +10,00% | 0,07904 $ | 2/29 | +6,90% | +29,41% | DEBOLE | 8,1 | 18,5 |
| -15,00% | 0,06107 $ | 29/40 | +72,50% | +15,00% | 0,08263 $ | 0/29 | 0,00% | +35,29% | DEBOLE | 8,1 | n/d |
| -15,00% | 0,06107 $ | 29/40 | +72,50% | +20,00% | 0,08622 $ | 0/29 | 0,00% | +41,18% | DEBOLE | 8,1 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07544 $ | 20/40 | +50,00% | prezzo iniziale | 0,07185 $ | 18/20 | +90,00% | -4,76% | ALTA | 2,8 | 8,6 |
| +5,00% | 0,07544 $ | 20/40 | +50,00% | -5,00% | 0,06826 $ | 15/20 | +75,00% | -9,52% | ALTA | 2,8 | 9,8 |
| +5,00% | 0,07544 $ | 20/40 | +50,00% | -8,00% | 0,06610 $ | 15/20 | +75,00% | -12,38% | ALTA | 2,8 | 10,8 |
| +5,00% | 0,07544 $ | 20/40 | +50,00% | -10,00% | 0,06467 $ | 13/20 | +65,00% | -14,29% | ALTA | 2,8 | 11,9 |
| +5,00% | 0,07544 $ | 20/40 | +50,00% | -15,00% | 0,06107 $ | 11/20 | +55,00% | -19,05% | MEDIA | 2,8 | 10,1 |
| +10,00% | 0,07904 $ | 15/40 | +37,50% | prezzo iniziale | 0,07185 $ | 13/15 | +86,67% | -9,09% | ALTA | 6,9 | 12,7 |
| +10,00% | 0,07904 $ | 15/40 | +37,50% | -5,00% | 0,06826 $ | 9/15 | +60,00% | -13,64% | MEDIA | 6,9 | 12,3 |
| +10,00% | 0,07904 $ | 15/40 | +37,50% | -8,00% | 0,06610 $ | 9/15 | +60,00% | -16,36% | MEDIA | 6,9 | 13,2 |
| +10,00% | 0,07904 $ | 15/40 | +37,50% | -10,00% | 0,06467 $ | 8/15 | +53,33% | -18,18% | MEDIA | 6,9 | 14,5 |
| +10,00% | 0,07904 $ | 15/40 | +37,50% | -15,00% | 0,06107 $ | 6/15 | +40,00% | -22,73% | BASSA | 6,9 | 12,0 |
| +15,00% | 0,08263 $ | 9/40 | +22,50% | prezzo iniziale | 0,07185 $ | 6/9 | +66,67% | -13,04% | ALTA | 8,3 | 17,2 |
| +15,00% | 0,08263 $ | 9/40 | +22,50% | -5,00% | 0,06826 $ | 4/9 | +44,44% | -17,39% | BASSA | 8,3 | 18,0 |
| +15,00% | 0,08263 $ | 9/40 | +22,50% | -8,00% | 0,06610 $ | 3/9 | +33,33% | -20,00% | DEBOLE | 8,3 | 15,0 |
| +15,00% | 0,08263 $ | 9/40 | +22,50% | -10,00% | 0,06467 $ | 3/9 | +33,33% | -21,74% | DEBOLE | 8,3 | 15,3 |
| +15,00% | 0,08263 $ | 9/40 | +22,50% | -15,00% | 0,06107 $ | 3/9 | +33,33% | -26,09% | DEBOLE | 8,3 | 15,7 |
| +20,00% | 0,08622 $ | 6/40 | +15,00% | prezzo iniziale | 0,07185 $ | 3/6 | +50,00% | -16,67% | MEDIA | 8,0 | 11,3 |
| +20,00% | 0,08622 $ | 6/40 | +15,00% | -5,00% | 0,06826 $ | 3/6 | +50,00% | -20,83% | MEDIA | 8,0 | 15,3 |
| +20,00% | 0,08622 $ | 6/40 | +15,00% | -8,00% | 0,06610 $ | 2/6 | +33,33% | -23,33% | DEBOLE | 8,0 | 9,5 |
| +20,00% | 0,08622 $ | 6/40 | +15,00% | -10,00% | 0,06467 $ | 2/6 | +33,33% | -25,00% | DEBOLE | 8,0 | 10,0 |
| +20,00% | 0,08622 $ | 6/40 | +15,00% | -15,00% | 0,06107 $ | 2/6 | +33,33% | -29,17% | DEBOLE | 8,0 | 10,5 |

---
