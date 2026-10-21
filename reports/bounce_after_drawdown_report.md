# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-10-21 07:32:47 CEST**  
UTC: **2026-10-21 05:32:47 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 78.672 $ | 91.094 $ | +30,77% | +15,79% | rimbalzo poco frequente | 91.094 $ | 78.672 $ | +12,50% | -13,64% | spike storicamente più resistente |
| SOL | 100,67 $ | 116,57 $ | +37,50% | +15,79% | rimbalzo debole | 116,57 $ | 100,67 $ | +4,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07761 $ | 0,08986 $ | +47,62% | +15,79% | rimbalzo debole | 0,08986 $ | 0,07761 $ | +6,67% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 26 prima sono scesi a -5,00%. Tra quei 26, 8 poi sono rimbalzati fino a +10,00%. Percentuale: +30,77% (8/26). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- BTC: su 40 casi simili, 24 prima sono saliti a +10,00%. Tra quei 24, 3 poi sono scaricati a -5,00%. Percentuale: +12,50% (3/24). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 78.672 $ | 26/40 | +65,00% | +5,00% | 86.953 $ | 10/26 | +38,46% | +10,53% | BASSA | 7,9 | 17,9 |
| -5,00% | 78.672 $ | 26/40 | +65,00% | +10,00% | 91.094 $ | 8/26 | +30,77% | +15,79% | DEBOLE | 7,9 | 19,0 |
| -5,00% | 78.672 $ | 26/40 | +65,00% | +15,00% | 95.234 $ | 5/26 | +19,23% | +21,05% | DEBOLE | 7,9 | 20,0 |
| -5,00% | 78.672 $ | 26/40 | +65,00% | +20,00% | 99.375 $ | 5/26 | +19,23% | +26,32% | DEBOLE | 7,9 | 21,2 |
| -8,00% | 76.187 $ | 24/40 | +60,00% | +5,00% | 86.953 $ | 8/24 | +33,33% | +14,13% | DEBOLE | 10,1 | 18,5 |
| -8,00% | 76.187 $ | 24/40 | +60,00% | +10,00% | 91.094 $ | 6/24 | +25,00% | +19,57% | DEBOLE | 10,1 | 19,2 |
| -8,00% | 76.187 $ | 24/40 | +60,00% | +15,00% | 95.234 $ | 3/24 | +12,50% | +25,00% | DEBOLE | 10,1 | 20,3 |
| -8,00% | 76.187 $ | 24/40 | +60,00% | +20,00% | 99.375 $ | 3/24 | +12,50% | +30,43% | DEBOLE | 10,1 | 22,0 |
| -10,00% | 74.531 $ | 19/40 | +47,50% | +5,00% | 86.953 $ | 4/19 | +21,05% | +16,67% | DEBOLE | 11,7 | 27,0 |
| -10,00% | 74.531 $ | 19/40 | +47,50% | +10,00% | 91.094 $ | 3/19 | +15,79% | +22,22% | DEBOLE | 11,7 | 27,7 |
| -10,00% | 74.531 $ | 19/40 | +47,50% | +15,00% | 95.234 $ | 1/19 | +5,26% | +27,78% | DEBOLE | 11,7 | 30,0 |
| -10,00% | 74.531 $ | 19/40 | +47,50% | +20,00% | 99.375 $ | 1/19 | +5,26% | +33,33% | DEBOLE | 11,7 | 30,0 |
| -15,00% | 70.391 $ | 14/40 | +35,00% | +5,00% | 86.953 $ | 2/14 | +14,29% | +23,53% | DEBOLE | 19,1 | 27,0 |
| -15,00% | 70.391 $ | 14/40 | +35,00% | +10,00% | 91.094 $ | 2/14 | +14,29% | +29,41% | DEBOLE | 19,1 | 27,0 |
| -15,00% | 70.391 $ | 14/40 | +35,00% | +15,00% | 95.234 $ | 0/14 | 0,00% | +35,29% | DEBOLE | 19,1 | n/d |
| -15,00% | 70.391 $ | 14/40 | +35,00% | +20,00% | 99.375 $ | 0/14 | 0,00% | +41,18% | DEBOLE | 19,1 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 86.953 $ | 28/40 | +70,00% | prezzo iniziale | 82.812 $ | 17/28 | +60,71% | -4,76% | MEDIA | 7,1 | 12,6 |
| +5,00% | 86.953 $ | 28/40 | +70,00% | -5,00% | 78.672 $ | 10/28 | +35,71% | -9,52% | BASSA | 7,1 | 14,5 |
| +5,00% | 86.953 $ | 28/40 | +70,00% | -8,00% | 76.187 $ | 8/28 | +28,57% | -12,38% | DEBOLE | 7,1 | 17,4 |
| +5,00% | 86.953 $ | 28/40 | +70,00% | -10,00% | 74.531 $ | 7/28 | +25,00% | -14,29% | DEBOLE | 7,1 | 18,0 |
| +5,00% | 86.953 $ | 28/40 | +70,00% | -15,00% | 70.391 $ | 5/28 | +17,86% | -19,05% | DEBOLE | 7,1 | 22,4 |
| +10,00% | 91.094 $ | 24/40 | +60,00% | prezzo iniziale | 82.812 $ | 10/24 | +41,67% | -9,09% | BASSA | 11,9 | 15,9 |
| +10,00% | 91.094 $ | 24/40 | +60,00% | -5,00% | 78.672 $ | 3/24 | +12,50% | -13,64% | DEBOLE | 11,9 | 17,7 |
| +10,00% | 91.094 $ | 24/40 | +60,00% | -8,00% | 76.187 $ | 3/24 | +12,50% | -16,36% | DEBOLE | 11,9 | 20,3 |
| +10,00% | 91.094 $ | 24/40 | +60,00% | -10,00% | 74.531 $ | 3/24 | +12,50% | -18,18% | DEBOLE | 11,9 | 20,7 |
| +10,00% | 91.094 $ | 24/40 | +60,00% | -15,00% | 70.391 $ | 2/24 | +8,33% | -22,73% | DEBOLE | 11,9 | 24,5 |
| +15,00% | 95.234 $ | 18/40 | +45,00% | prezzo iniziale | 82.812 $ | 3/18 | +16,67% | -13,04% | DEBOLE | 16,3 | 15,0 |
| +15,00% | 95.234 $ | 18/40 | +45,00% | -5,00% | 78.672 $ | 2/18 | +11,11% | -17,39% | DEBOLE | 16,3 | 21,5 |
| +15,00% | 95.234 $ | 18/40 | +45,00% | -8,00% | 76.187 $ | 2/18 | +11,11% | -20,00% | DEBOLE | 16,3 | 24,5 |
| +15,00% | 95.234 $ | 18/40 | +45,00% | -10,00% | 74.531 $ | 2/18 | +11,11% | -21,74% | DEBOLE | 16,3 | 25,0 |
| +15,00% | 95.234 $ | 18/40 | +45,00% | -15,00% | 70.391 $ | 1/18 | +5,56% | -26,09% | DEBOLE | 16,3 | 22,0 |
| +20,00% | 99.375 $ | 15/40 | +37,50% | prezzo iniziale | 82.812 $ | 0/15 | 0,00% | -16,67% | DEBOLE | 21,5 | n/d |
| +20,00% | 99.375 $ | 15/40 | +37,50% | -5,00% | 78.672 $ | 0/15 | 0,00% | -20,83% | DEBOLE | 21,5 | n/d |
| +20,00% | 99.375 $ | 15/40 | +37,50% | -8,00% | 76.187 $ | 0/15 | 0,00% | -23,33% | DEBOLE | 21,5 | n/d |
| +20,00% | 99.375 $ | 15/40 | +37,50% | -10,00% | 74.531 $ | 0/15 | 0,00% | -25,00% | DEBOLE | 21,5 | n/d |
| +20,00% | 99.375 $ | 15/40 | +37,50% | -15,00% | 70.391 $ | 0/15 | 0,00% | -29,17% | DEBOLE | 21,5 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 24 prima sono scesi a -5,00%. Tra quei 24, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +37,50% (9/24). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- SOL: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 1 poi sono scaricati a -5,00%. Percentuale: +4,00% (1/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 100,67 $ | 24/40 | +60,00% | +5,00% | 111,27 $ | 11/24 | +45,83% | +10,53% | BASSA | 8,2 | 19,2 |
| -5,00% | 100,67 $ | 24/40 | +60,00% | +10,00% | 116,57 $ | 9/24 | +37,50% | +15,79% | BASSA | 8,2 | 20,8 |
| -5,00% | 100,67 $ | 24/40 | +60,00% | +15,00% | 121,87 $ | 6/24 | +25,00% | +21,05% | DEBOLE | 8,2 | 22,5 |
| -5,00% | 100,67 $ | 24/40 | +60,00% | +20,00% | 127,16 $ | 4/24 | +16,67% | +26,32% | DEBOLE | 8,2 | 22,0 |
| -8,00% | 97,49 $ | 22/40 | +55,00% | +5,00% | 111,27 $ | 9/22 | +40,91% | +14,13% | BASSA | 9,1 | 19,1 |
| -8,00% | 97,49 $ | 22/40 | +55,00% | +10,00% | 116,57 $ | 7/22 | +31,82% | +19,57% | DEBOLE | 9,1 | 19,9 |
| -8,00% | 97,49 $ | 22/40 | +55,00% | +15,00% | 121,87 $ | 5/22 | +22,73% | +25,00% | DEBOLE | 9,1 | 22,6 |
| -8,00% | 97,49 $ | 22/40 | +55,00% | +20,00% | 127,16 $ | 3/22 | +13,64% | +30,43% | DEBOLE | 9,1 | 22,0 |
| -10,00% | 95,37 $ | 16/40 | +40,00% | +5,00% | 111,27 $ | 5/16 | +31,25% | +16,67% | DEBOLE | 9,2 | 26,4 |
| -10,00% | 95,37 $ | 16/40 | +40,00% | +10,00% | 116,57 $ | 4/16 | +25,00% | +22,22% | DEBOLE | 9,2 | 26,8 |
| -10,00% | 95,37 $ | 16/40 | +40,00% | +15,00% | 121,87 $ | 3/16 | +18,75% | +27,78% | DEBOLE | 9,2 | 27,3 |
| -10,00% | 95,37 $ | 16/40 | +40,00% | +20,00% | 127,16 $ | 1/16 | +6,25% | +33,33% | DEBOLE | 9,2 | 30,0 |
| -15,00% | 90,07 $ | 14/40 | +35,00% | +5,00% | 111,27 $ | 3/14 | +21,43% | +23,53% | DEBOLE | 13,0 | 26,0 |
| -15,00% | 90,07 $ | 14/40 | +35,00% | +10,00% | 116,57 $ | 3/14 | +21,43% | +29,41% | DEBOLE | 13,0 | 26,0 |
| -15,00% | 90,07 $ | 14/40 | +35,00% | +15,00% | 121,87 $ | 2/14 | +14,29% | +35,29% | DEBOLE | 13,0 | 26,0 |
| -15,00% | 90,07 $ | 14/40 | +35,00% | +20,00% | 127,16 $ | 0/14 | 0,00% | +41,18% | DEBOLE | 13,0 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 111,27 $ | 31/40 | +77,50% | prezzo iniziale | 105,97 $ | 19/31 | +61,29% | -4,76% | MEDIA | 6,3 | 10,2 |
| +5,00% | 111,27 $ | 31/40 | +77,50% | -5,00% | 100,67 $ | 9/31 | +29,03% | -9,52% | DEBOLE | 6,3 | 13,1 |
| +5,00% | 111,27 $ | 31/40 | +77,50% | -8,00% | 97,49 $ | 7/31 | +22,58% | -12,38% | DEBOLE | 6,3 | 14,0 |
| +5,00% | 111,27 $ | 31/40 | +77,50% | -10,00% | 95,37 $ | 6/31 | +19,35% | -14,29% | DEBOLE | 6,3 | 16,0 |
| +5,00% | 111,27 $ | 31/40 | +77,50% | -15,00% | 90,07 $ | 5/31 | +16,13% | -19,05% | DEBOLE | 6,3 | 20,4 |
| +10,00% | 116,57 $ | 25/40 | +62,50% | prezzo iniziale | 105,97 $ | 6/25 | +24,00% | -9,09% | DEBOLE | 15,0 | 16,2 |
| +10,00% | 116,57 $ | 25/40 | +62,50% | -5,00% | 100,67 $ | 1/25 | +4,00% | -13,64% | DEBOLE | 15,0 | 14,0 |
| +10,00% | 116,57 $ | 25/40 | +62,50% | -8,00% | 97,49 $ | 1/25 | +4,00% | -16,36% | DEBOLE | 15,0 | 20,0 |
| +10,00% | 116,57 $ | 25/40 | +62,50% | -10,00% | 95,37 $ | 1/25 | +4,00% | -18,18% | DEBOLE | 15,0 | 20,0 |
| +10,00% | 116,57 $ | 25/40 | +62,50% | -15,00% | 90,07 $ | 1/25 | +4,00% | -22,73% | DEBOLE | 15,0 | 22,0 |
| +15,00% | 121,87 $ | 18/40 | +45,00% | prezzo iniziale | 105,97 $ | 2/18 | +11,11% | -13,04% | DEBOLE | 16,3 | 16,0 |
| +15,00% | 121,87 $ | 18/40 | +45,00% | -5,00% | 100,67 $ | 1/18 | +5,56% | -17,39% | DEBOLE | 16,3 | 14,0 |
| +15,00% | 121,87 $ | 18/40 | +45,00% | -8,00% | 97,49 $ | 1/18 | +5,56% | -20,00% | DEBOLE | 16,3 | 20,0 |
| +15,00% | 121,87 $ | 18/40 | +45,00% | -10,00% | 95,37 $ | 1/18 | +5,56% | -21,74% | DEBOLE | 16,3 | 20,0 |
| +15,00% | 121,87 $ | 18/40 | +45,00% | -15,00% | 90,07 $ | 1/18 | +5,56% | -26,09% | DEBOLE | 16,3 | 22,0 |
| +20,00% | 127,16 $ | 14/40 | +35,00% | prezzo iniziale | 105,97 $ | 0/14 | 0,00% | -16,67% | DEBOLE | 18,0 | n/d |
| +20,00% | 127,16 $ | 14/40 | +35,00% | -5,00% | 100,67 $ | 0/14 | 0,00% | -20,83% | DEBOLE | 18,0 | n/d |
| +20,00% | 127,16 $ | 14/40 | +35,00% | -8,00% | 97,49 $ | 0/14 | 0,00% | -23,33% | DEBOLE | 18,0 | n/d |
| +20,00% | 127,16 $ | 14/40 | +35,00% | -10,00% | 95,37 $ | 0/14 | 0,00% | -25,00% | DEBOLE | 18,0 | n/d |
| +20,00% | 127,16 $ | 14/40 | +35,00% | -15,00% | 90,07 $ | 0/14 | 0,00% | -29,17% | DEBOLE | 18,0 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 21 prima sono scesi a -5,00%. Tra quei 21, 10 poi sono rimbalzati fino a +10,00%. Percentuale: +47,62% (10/21). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- DOGE: su 40 casi simili, 30 prima sono saliti a +10,00%. Tra quei 30, 2 poi sono scaricati a -5,00%. Percentuale: +6,67% (2/30). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,07761 $ | 21/40 | +52,50% | +5,00% | 0,08577 $ | 12/21 | +57,14% | +10,53% | MEDIA | 6,4 | 20,2 |
| -5,00% | 0,07761 $ | 21/40 | +52,50% | +10,00% | 0,08986 $ | 10/21 | +47,62% | +15,79% | BASSA | 6,4 | 25,2 |
| -5,00% | 0,07761 $ | 21/40 | +52,50% | +15,00% | 0,09394 $ | 7/21 | +33,33% | +21,05% | DEBOLE | 6,4 | 26,4 |
| -5,00% | 0,07761 $ | 21/40 | +52,50% | +20,00% | 0,09803 $ | 4/21 | +19,05% | +26,32% | DEBOLE | 6,4 | 26,2 |
| -8,00% | 0,07515 $ | 16/40 | +40,00% | +5,00% | 0,08577 $ | 7/16 | +43,75% | +14,13% | BASSA | 8,1 | 21,7 |
| -8,00% | 0,07515 $ | 16/40 | +40,00% | +10,00% | 0,08986 $ | 6/16 | +37,50% | +19,57% | BASSA | 8,1 | 24,2 |
| -8,00% | 0,07515 $ | 16/40 | +40,00% | +15,00% | 0,09394 $ | 4/16 | +25,00% | +25,00% | DEBOLE | 8,1 | 25,8 |
| -8,00% | 0,07515 $ | 16/40 | +40,00% | +20,00% | 0,09803 $ | 3/16 | +18,75% | +30,43% | DEBOLE | 8,1 | 27,7 |
| -10,00% | 0,07352 $ | 13/40 | +32,50% | +5,00% | 0,08577 $ | 4/13 | +30,77% | +16,67% | DEBOLE | 9,8 | 26,2 |
| -10,00% | 0,07352 $ | 13/40 | +32,50% | +10,00% | 0,08986 $ | 4/13 | +30,77% | +22,22% | DEBOLE | 9,8 | 26,5 |
| -10,00% | 0,07352 $ | 13/40 | +32,50% | +15,00% | 0,09394 $ | 3/13 | +23,08% | +27,78% | DEBOLE | 9,8 | 27,3 |
| -10,00% | 0,07352 $ | 13/40 | +32,50% | +20,00% | 0,09803 $ | 2/13 | +15,38% | +33,33% | DEBOLE | 9,8 | 30,0 |
| -15,00% | 0,06944 $ | 9/40 | +22,50% | +5,00% | 0,08577 $ | 2/9 | +22,22% | +23,53% | DEBOLE | 15,1 | 24,5 |
| -15,00% | 0,06944 $ | 9/40 | +22,50% | +10,00% | 0,08986 $ | 2/9 | +22,22% | +29,41% | DEBOLE | 15,1 | 24,5 |
| -15,00% | 0,06944 $ | 9/40 | +22,50% | +15,00% | 0,09394 $ | 1/9 | +11,11% | +35,29% | DEBOLE | 15,1 | 23,0 |
| -15,00% | 0,06944 $ | 9/40 | +22,50% | +20,00% | 0,09803 $ | 0/9 | 0,00% | +41,18% | DEBOLE | 15,1 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,08577 $ | 33/40 | +82,50% | prezzo iniziale | 0,08169 $ | 19/33 | +57,58% | -4,76% | MEDIA | 6,6 | 9,1 |
| +5,00% | 0,08577 $ | 33/40 | +82,50% | -5,00% | 0,07761 $ | 8/33 | +24,24% | -9,52% | DEBOLE | 6,6 | 10,5 |
| +5,00% | 0,08577 $ | 33/40 | +82,50% | -8,00% | 0,07515 $ | 4/33 | +12,12% | -12,38% | DEBOLE | 6,6 | 11,8 |
| +5,00% | 0,08577 $ | 33/40 | +82,50% | -10,00% | 0,07352 $ | 4/33 | +12,12% | -14,29% | DEBOLE | 6,6 | 14,8 |
| +5,00% | 0,08577 $ | 33/40 | +82,50% | -15,00% | 0,06944 $ | 3/33 | +9,09% | -19,05% | DEBOLE | 6,6 | 21,7 |
| +10,00% | 0,08986 $ | 30/40 | +75,00% | prezzo iniziale | 0,08169 $ | 7/30 | +23,33% | -9,09% | DEBOLE | 15,8 | 13,1 |
| +10,00% | 0,08986 $ | 30/40 | +75,00% | -5,00% | 0,07761 $ | 2/30 | +6,67% | -13,64% | DEBOLE | 15,8 | 8,5 |
| +10,00% | 0,08986 $ | 30/40 | +75,00% | -8,00% | 0,07515 $ | 2/30 | +6,67% | -16,36% | DEBOLE | 15,8 | 10,5 |
| +10,00% | 0,08986 $ | 30/40 | +75,00% | -10,00% | 0,07352 $ | 2/30 | +6,67% | -18,18% | DEBOLE | 15,8 | 10,5 |
| +10,00% | 0,08986 $ | 30/40 | +75,00% | -15,00% | 0,06944 $ | 2/30 | +6,67% | -22,73% | DEBOLE | 15,8 | 23,5 |
| +15,00% | 0,09394 $ | 20/40 | +50,00% | prezzo iniziale | 0,08169 $ | 1/20 | +5,00% | -13,04% | DEBOLE | 18,3 | 14,0 |
| +15,00% | 0,09394 $ | 20/40 | +50,00% | -5,00% | 0,07761 $ | 0/20 | 0,00% | -17,39% | DEBOLE | 18,3 | n/d |
| +15,00% | 0,09394 $ | 20/40 | +50,00% | -8,00% | 0,07515 $ | 0/20 | 0,00% | -20,00% | DEBOLE | 18,3 | n/d |
| +15,00% | 0,09394 $ | 20/40 | +50,00% | -10,00% | 0,07352 $ | 0/20 | 0,00% | -21,74% | DEBOLE | 18,3 | n/d |
| +15,00% | 0,09394 $ | 20/40 | +50,00% | -15,00% | 0,06944 $ | 0/20 | 0,00% | -26,09% | DEBOLE | 18,3 | n/d |
| +20,00% | 0,09803 $ | 15/40 | +37,50% | prezzo iniziale | 0,08169 $ | 0/15 | 0,00% | -16,67% | DEBOLE | 18,9 | n/d |
| +20,00% | 0,09803 $ | 15/40 | +37,50% | -5,00% | 0,07761 $ | 0/15 | 0,00% | -20,83% | DEBOLE | 18,9 | n/d |
| +20,00% | 0,09803 $ | 15/40 | +37,50% | -8,00% | 0,07515 $ | 0/15 | 0,00% | -23,33% | DEBOLE | 18,9 | n/d |
| +20,00% | 0,09803 $ | 15/40 | +37,50% | -10,00% | 0,07352 $ | 0/15 | 0,00% | -25,00% | DEBOLE | 18,9 | n/d |
| +20,00% | 0,09803 $ | 15/40 | +37,50% | -15,00% | 0,06944 $ | 0/15 | 0,00% | -29,17% | DEBOLE | 18,9 | n/d |

---
