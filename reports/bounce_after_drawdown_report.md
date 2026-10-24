# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-10-24 07:32:47 CEST**  
UTC: **2026-10-24 05:32:47 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 76.628 $ | 88.727 $ | +50,00% | +15,79% | rimbalzo possibile | 88.727 $ | 76.628 $ | +12,00% | -13,64% | spike storicamente più resistente |
| SOL | 97,06 $ | 112,39 $ | +46,67% | +15,79% | rimbalzo debole | 112,39 $ | 97,06 $ | +8,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07438 $ | 0,08612 $ | +57,14% | +15,79% | rimbalzo possibile | 0,08612 $ | 0,07438 $ | +6,90% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 30 prima sono scesi a -5,00%. Tra quei 30, 15 poi sono rimbalzati fino a +10,00%. Percentuale: +50,00% (15/30). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.
- BTC: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 3 poi sono scaricati a -5,00%. Percentuale: +12,00% (3/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 76.628 $ | 30/40 | +75,00% | +5,00% | 84.694 $ | 15/30 | +50,00% | +10,53% | MEDIA | 6,1 | 18,0 |
| -5,00% | 76.628 $ | 30/40 | +75,00% | +10,00% | 88.727 $ | 15/30 | +50,00% | +15,79% | MEDIA | 6,1 | 19,3 |
| -5,00% | 76.628 $ | 30/40 | +75,00% | +15,00% | 92.760 $ | 11/30 | +36,67% | +21,05% | BASSA | 6,1 | 20,9 |
| -5,00% | 76.628 $ | 30/40 | +75,00% | +20,00% | 96.794 $ | 5/30 | +16,67% | +26,32% | DEBOLE | 6,1 | 22,2 |
| -8,00% | 74.208 $ | 24/40 | +60,00% | +5,00% | 84.694 $ | 10/24 | +41,67% | +14,13% | BASSA | 7,0 | 20,0 |
| -8,00% | 74.208 $ | 24/40 | +60,00% | +10,00% | 88.727 $ | 9/24 | +37,50% | +19,57% | BASSA | 7,0 | 20,4 |
| -8,00% | 74.208 $ | 24/40 | +60,00% | +15,00% | 92.760 $ | 8/24 | +33,33% | +25,00% | DEBOLE | 7,0 | 22,1 |
| -8,00% | 74.208 $ | 24/40 | +60,00% | +20,00% | 96.794 $ | 4/24 | +16,67% | +30,43% | DEBOLE | 7,0 | 23,2 |
| -10,00% | 72.595 $ | 20/40 | +50,00% | +5,00% | 84.694 $ | 6/20 | +30,00% | +16,67% | DEBOLE | 8,5 | 22,2 |
| -10,00% | 72.595 $ | 20/40 | +50,00% | +10,00% | 88.727 $ | 5/20 | +25,00% | +22,22% | DEBOLE | 8,5 | 22,2 |
| -10,00% | 72.595 $ | 20/40 | +50,00% | +15,00% | 92.760 $ | 5/20 | +25,00% | +27,78% | DEBOLE | 8,5 | 22,4 |
| -10,00% | 72.595 $ | 20/40 | +50,00% | +20,00% | 96.794 $ | 2/20 | +10,00% | +33,33% | DEBOLE | 8,5 | 28,0 |
| -15,00% | 68.562 $ | 12/40 | +30,00% | +5,00% | 84.694 $ | 2/12 | +16,67% | +23,53% | DEBOLE | 15,7 | 24,0 |
| -15,00% | 68.562 $ | 12/40 | +30,00% | +10,00% | 88.727 $ | 1/12 | +8,33% | +29,41% | DEBOLE | 15,7 | 23,0 |
| -15,00% | 68.562 $ | 12/40 | +30,00% | +15,00% | 92.760 $ | 1/12 | +8,33% | +35,29% | DEBOLE | 15,7 | 23,0 |
| -15,00% | 68.562 $ | 12/40 | +30,00% | +20,00% | 96.794 $ | 0/12 | 0,00% | +41,18% | DEBOLE | 15,7 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 84.694 $ | 27/40 | +67,50% | prezzo iniziale | 80.661 $ | 11/27 | +40,74% | -4,76% | BASSA | 11,3 | 16,1 |
| +5,00% | 84.694 $ | 27/40 | +67,50% | -5,00% | 76.628 $ | 6/27 | +22,22% | -9,52% | DEBOLE | 11,3 | 14,2 |
| +5,00% | 84.694 $ | 27/40 | +67,50% | -8,00% | 74.208 $ | 3/27 | +11,11% | -12,38% | DEBOLE | 11,3 | 13,3 |
| +5,00% | 84.694 $ | 27/40 | +67,50% | -10,00% | 72.595 $ | 3/27 | +11,11% | -14,29% | DEBOLE | 11,3 | 14,0 |
| +5,00% | 84.694 $ | 27/40 | +67,50% | -15,00% | 68.562 $ | 3/27 | +11,11% | -19,05% | DEBOLE | 11,3 | 19,7 |
| +10,00% | 88.727 $ | 25/40 | +62,50% | prezzo iniziale | 80.661 $ | 8/25 | +32,00% | -9,09% | DEBOLE | 15,4 | 20,4 |
| +10,00% | 88.727 $ | 25/40 | +62,50% | -5,00% | 76.628 $ | 3/25 | +12,00% | -13,64% | DEBOLE | 15,4 | 16,0 |
| +10,00% | 88.727 $ | 25/40 | +62,50% | -8,00% | 74.208 $ | 2/25 | +8,00% | -16,36% | DEBOLE | 15,4 | 16,5 |
| +10,00% | 88.727 $ | 25/40 | +62,50% | -10,00% | 72.595 $ | 2/25 | +8,00% | -18,18% | DEBOLE | 15,4 | 16,5 |
| +10,00% | 88.727 $ | 25/40 | +62,50% | -15,00% | 68.562 $ | 2/25 | +8,00% | -22,73% | DEBOLE | 15,4 | 17,5 |
| +15,00% | 92.760 $ | 19/40 | +47,50% | prezzo iniziale | 80.661 $ | 4/19 | +21,05% | -13,04% | DEBOLE | 17,8 | 24,2 |
| +15,00% | 92.760 $ | 19/40 | +47,50% | -5,00% | 76.628 $ | 1/19 | +5,26% | -17,39% | DEBOLE | 17,8 | 14,0 |
| +15,00% | 92.760 $ | 19/40 | +47,50% | -8,00% | 74.208 $ | 1/19 | +5,26% | -20,00% | DEBOLE | 17,8 | 20,0 |
| +15,00% | 92.760 $ | 19/40 | +47,50% | -10,00% | 72.595 $ | 1/19 | +5,26% | -21,74% | DEBOLE | 17,8 | 20,0 |
| +15,00% | 92.760 $ | 19/40 | +47,50% | -15,00% | 68.562 $ | 1/19 | +5,26% | -26,09% | DEBOLE | 17,8 | 22,0 |
| +20,00% | 96.794 $ | 12/40 | +30,00% | prezzo iniziale | 80.661 $ | 1/12 | +8,33% | -16,67% | DEBOLE | 18,5 | 28,0 |
| +20,00% | 96.794 $ | 12/40 | +30,00% | -5,00% | 76.628 $ | 0/12 | 0,00% | -20,83% | DEBOLE | 18,5 | n/d |
| +20,00% | 96.794 $ | 12/40 | +30,00% | -8,00% | 74.208 $ | 0/12 | 0,00% | -23,33% | DEBOLE | 18,5 | n/d |
| +20,00% | 96.794 $ | 12/40 | +30,00% | -10,00% | 72.595 $ | 0/12 | 0,00% | -25,00% | DEBOLE | 18,5 | n/d |
| +20,00% | 96.794 $ | 12/40 | +30,00% | -15,00% | 68.562 $ | 0/12 | 0,00% | -29,17% | DEBOLE | 18,5 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 30 prima sono scesi a -5,00%. Tra quei 30, 14 poi sono rimbalzati fino a +10,00%. Percentuale: +46,67% (14/30). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- SOL: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 2 poi sono scaricati a -5,00%. Percentuale: +8,00% (2/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 97,06 $ | 30/40 | +75,00% | +5,00% | 107,28 $ | 15/30 | +50,00% | +10,53% | MEDIA | 5,5 | 17,5 |
| -5,00% | 97,06 $ | 30/40 | +75,00% | +10,00% | 112,39 $ | 14/30 | +46,67% | +15,79% | BASSA | 5,5 | 18,9 |
| -5,00% | 97,06 $ | 30/40 | +75,00% | +15,00% | 117,50 $ | 9/30 | +30,00% | +21,05% | DEBOLE | 5,5 | 21,3 |
| -5,00% | 97,06 $ | 30/40 | +75,00% | +20,00% | 122,60 $ | 3/30 | +10,00% | +26,32% | DEBOLE | 5,5 | 27,0 |
| -8,00% | 94,00 $ | 24/40 | +60,00% | +5,00% | 107,28 $ | 9/24 | +37,50% | +14,13% | BASSA | 7,4 | 20,4 |
| -8,00% | 94,00 $ | 24/40 | +60,00% | +10,00% | 112,39 $ | 8/24 | +33,33% | +19,57% | DEBOLE | 7,4 | 20,1 |
| -8,00% | 94,00 $ | 24/40 | +60,00% | +15,00% | 117,50 $ | 7/24 | +29,17% | +25,00% | DEBOLE | 7,4 | 23,4 |
| -8,00% | 94,00 $ | 24/40 | +60,00% | +20,00% | 122,60 $ | 3/24 | +12,50% | +30,43% | DEBOLE | 7,4 | 27,0 |
| -10,00% | 91,95 $ | 21/40 | +52,50% | +5,00% | 107,28 $ | 7/21 | +33,33% | +16,67% | DEBOLE | 7,5 | 23,6 |
| -10,00% | 91,95 $ | 21/40 | +52,50% | +10,00% | 112,39 $ | 6/21 | +28,57% | +22,22% | DEBOLE | 7,5 | 23,7 |
| -10,00% | 91,95 $ | 21/40 | +52,50% | +15,00% | 117,50 $ | 6/21 | +28,57% | +27,78% | DEBOLE | 7,5 | 23,8 |
| -10,00% | 91,95 $ | 21/40 | +52,50% | +20,00% | 122,60 $ | 2/21 | +9,52% | +33,33% | DEBOLE | 7,5 | 27,5 |
| -15,00% | 86,84 $ | 12/40 | +30,00% | +5,00% | 107,28 $ | 3/12 | +25,00% | +23,53% | DEBOLE | 11,0 | 25,7 |
| -15,00% | 86,84 $ | 12/40 | +30,00% | +10,00% | 112,39 $ | 2/12 | +16,67% | +29,41% | DEBOLE | 11,0 | 26,0 |
| -15,00% | 86,84 $ | 12/40 | +30,00% | +15,00% | 117,50 $ | 2/12 | +16,67% | +35,29% | DEBOLE | 11,0 | 26,0 |
| -15,00% | 86,84 $ | 12/40 | +30,00% | +20,00% | 122,60 $ | 0/12 | 0,00% | +41,18% | DEBOLE | 11,0 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 107,28 $ | 28/40 | +70,00% | prezzo iniziale | 102,17 $ | 16/28 | +57,14% | -4,76% | MEDIA | 9,4 | 16,3 |
| +5,00% | 107,28 $ | 28/40 | +70,00% | -5,00% | 97,06 $ | 7/28 | +25,00% | -9,52% | DEBOLE | 9,4 | 12,9 |
| +5,00% | 107,28 $ | 28/40 | +70,00% | -8,00% | 94,00 $ | 5/28 | +17,86% | -12,38% | DEBOLE | 9,4 | 11,6 |
| +5,00% | 107,28 $ | 28/40 | +70,00% | -10,00% | 91,95 $ | 5/28 | +17,86% | -14,29% | DEBOLE | 9,4 | 13,8 |
| +5,00% | 107,28 $ | 28/40 | +70,00% | -15,00% | 86,84 $ | 3/28 | +10,71% | -19,05% | DEBOLE | 9,4 | 18,7 |
| +10,00% | 112,39 $ | 25/40 | +62,50% | prezzo iniziale | 102,17 $ | 10/25 | +40,00% | -9,09% | BASSA | 15,3 | 21,3 |
| +10,00% | 112,39 $ | 25/40 | +62,50% | -5,00% | 97,06 $ | 2/25 | +8,00% | -13,64% | DEBOLE | 15,3 | 10,5 |
| +10,00% | 112,39 $ | 25/40 | +62,50% | -8,00% | 94,00 $ | 2/25 | +8,00% | -16,36% | DEBOLE | 15,3 | 11,5 |
| +10,00% | 112,39 $ | 25/40 | +62,50% | -10,00% | 91,95 $ | 2/25 | +8,00% | -18,18% | DEBOLE | 15,3 | 11,5 |
| +10,00% | 112,39 $ | 25/40 | +62,50% | -15,00% | 86,84 $ | 2/25 | +8,00% | -22,73% | DEBOLE | 15,3 | 19,5 |
| +15,00% | 117,50 $ | 18/40 | +45,00% | prezzo iniziale | 102,17 $ | 5/18 | +27,78% | -13,04% | DEBOLE | 17,9 | 25,4 |
| +15,00% | 117,50 $ | 18/40 | +45,00% | -5,00% | 97,06 $ | 0/18 | 0,00% | -17,39% | DEBOLE | 17,9 | n/d |
| +15,00% | 117,50 $ | 18/40 | +45,00% | -8,00% | 94,00 $ | 0/18 | 0,00% | -20,00% | DEBOLE | 17,9 | n/d |
| +15,00% | 117,50 $ | 18/40 | +45,00% | -10,00% | 91,95 $ | 0/18 | 0,00% | -21,74% | DEBOLE | 17,9 | n/d |
| +15,00% | 117,50 $ | 18/40 | +45,00% | -15,00% | 86,84 $ | 0/18 | 0,00% | -26,09% | DEBOLE | 17,9 | n/d |
| +20,00% | 122,60 $ | 11/40 | +27,50% | prezzo iniziale | 102,17 $ | 1/11 | +9,09% | -16,67% | DEBOLE | 19,5 | 28,0 |
| +20,00% | 122,60 $ | 11/40 | +27,50% | -5,00% | 97,06 $ | 0/11 | 0,00% | -20,83% | DEBOLE | 19,5 | n/d |
| +20,00% | 122,60 $ | 11/40 | +27,50% | -8,00% | 94,00 $ | 0/11 | 0,00% | -23,33% | DEBOLE | 19,5 | n/d |
| +20,00% | 122,60 $ | 11/40 | +27,50% | -10,00% | 91,95 $ | 0/11 | 0,00% | -25,00% | DEBOLE | 19,5 | n/d |
| +20,00% | 122,60 $ | 11/40 | +27,50% | -15,00% | 86,84 $ | 0/11 | 0,00% | -29,17% | DEBOLE | 19,5 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 28 prima sono scesi a -5,00%. Tra quei 28, 16 poi sono rimbalzati fino a +10,00%. Percentuale: +57,14% (16/28). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.
- DOGE: su 40 casi simili, 29 prima sono saliti a +10,00%. Tra quei 29, 2 poi sono scaricati a -5,00%. Percentuale: +6,90% (2/29). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,07438 $ | 28/40 | +70,00% | +5,00% | 0,08220 $ | 19/28 | +67,86% | +10,53% | ALTA | 4,2 | 19,6 |
| -5,00% | 0,07438 $ | 28/40 | +70,00% | +10,00% | 0,08612 $ | 16/28 | +57,14% | +15,79% | MEDIA | 4,2 | 20,1 |
| -5,00% | 0,07438 $ | 28/40 | +70,00% | +15,00% | 0,09003 $ | 11/28 | +39,29% | +21,05% | BASSA | 4,2 | 21,1 |
| -5,00% | 0,07438 $ | 28/40 | +70,00% | +20,00% | 0,09395 $ | 4/28 | +14,29% | +26,32% | DEBOLE | 4,2 | 22,5 |
| -8,00% | 0,07203 $ | 20/40 | +50,00% | +5,00% | 0,08220 $ | 11/20 | +55,00% | +14,13% | MEDIA | 6,8 | 22,8 |
| -8,00% | 0,07203 $ | 20/40 | +50,00% | +10,00% | 0,08612 $ | 8/20 | +40,00% | +19,57% | BASSA | 6,8 | 21,6 |
| -8,00% | 0,07203 $ | 20/40 | +50,00% | +15,00% | 0,09003 $ | 7/20 | +35,00% | +25,00% | BASSA | 6,8 | 23,3 |
| -8,00% | 0,07203 $ | 20/40 | +50,00% | +20,00% | 0,09395 $ | 3/20 | +15,00% | +30,43% | DEBOLE | 6,8 | 26,0 |
| -10,00% | 0,07046 $ | 15/40 | +37,50% | +5,00% | 0,08220 $ | 7/15 | +46,67% | +16,67% | BASSA | 6,5 | 23,7 |
| -10,00% | 0,07046 $ | 15/40 | +37,50% | +10,00% | 0,08612 $ | 5/15 | +33,33% | +22,22% | DEBOLE | 6,5 | 22,6 |
| -10,00% | 0,07046 $ | 15/40 | +37,50% | +15,00% | 0,09003 $ | 5/15 | +33,33% | +27,78% | DEBOLE | 6,5 | 22,8 |
| -10,00% | 0,07046 $ | 15/40 | +37,50% | +20,00% | 0,09395 $ | 2/15 | +13,33% | +33,33% | DEBOLE | 6,5 | 27,5 |
| -15,00% | 0,06655 $ | 7/40 | +17,50% | +5,00% | 0,08220 $ | 3/7 | +42,86% | +23,53% | BASSA | 6,6 | 26,0 |
| -15,00% | 0,06655 $ | 7/40 | +17,50% | +10,00% | 0,08612 $ | 1/7 | +14,29% | +29,41% | DEBOLE | 6,6 | 23,0 |
| -15,00% | 0,06655 $ | 7/40 | +17,50% | +15,00% | 0,09003 $ | 1/7 | +14,29% | +35,29% | DEBOLE | 6,6 | 23,0 |
| -15,00% | 0,06655 $ | 7/40 | +17,50% | +20,00% | 0,09395 $ | 0/7 | 0,00% | +41,18% | DEBOLE | 6,6 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,08220 $ | 32/40 | +80,00% | prezzo iniziale | 0,07829 $ | 15/32 | +46,88% | -4,76% | BASSA | 11,7 | 17,0 |
| +5,00% | 0,08220 $ | 32/40 | +80,00% | -5,00% | 0,07438 $ | 6/32 | +18,75% | -9,52% | DEBOLE | 11,7 | 9,5 |
| +5,00% | 0,08220 $ | 32/40 | +80,00% | -8,00% | 0,07203 $ | 3/32 | +9,38% | -12,38% | DEBOLE | 11,7 | 13,0 |
| +5,00% | 0,08220 $ | 32/40 | +80,00% | -10,00% | 0,07046 $ | 3/32 | +9,38% | -14,29% | DEBOLE | 11,7 | 13,3 |
| +5,00% | 0,08220 $ | 32/40 | +80,00% | -15,00% | 0,06655 $ | 2/32 | +6,25% | -19,05% | DEBOLE | 11,7 | 17,0 |
| +10,00% | 0,08612 $ | 29/40 | +72,50% | prezzo iniziale | 0,07829 $ | 8/29 | +27,59% | -9,09% | DEBOLE | 15,9 | 21,4 |
| +10,00% | 0,08612 $ | 29/40 | +72,50% | -5,00% | 0,07438 $ | 2/29 | +6,90% | -13,64% | DEBOLE | 15,9 | 9,0 |
| +10,00% | 0,08612 $ | 29/40 | +72,50% | -8,00% | 0,07203 $ | 2/29 | +6,90% | -16,36% | DEBOLE | 15,9 | 12,0 |
| +10,00% | 0,08612 $ | 29/40 | +72,50% | -10,00% | 0,07046 $ | 2/29 | +6,90% | -18,18% | DEBOLE | 15,9 | 12,0 |
| +10,00% | 0,08612 $ | 29/40 | +72,50% | -15,00% | 0,06655 $ | 2/29 | +6,90% | -22,73% | DEBOLE | 15,9 | 17,0 |
| +15,00% | 0,09003 $ | 22/40 | +55,00% | prezzo iniziale | 0,07829 $ | 5/22 | +22,73% | -13,04% | DEBOLE | 17,5 | 25,4 |
| +15,00% | 0,09003 $ | 22/40 | +55,00% | -5,00% | 0,07438 $ | 0/22 | 0,00% | -17,39% | DEBOLE | 17,5 | n/d |
| +15,00% | 0,09003 $ | 22/40 | +55,00% | -8,00% | 0,07203 $ | 0/22 | 0,00% | -20,00% | DEBOLE | 17,5 | n/d |
| +15,00% | 0,09003 $ | 22/40 | +55,00% | -10,00% | 0,07046 $ | 0/22 | 0,00% | -21,74% | DEBOLE | 17,5 | n/d |
| +15,00% | 0,09003 $ | 22/40 | +55,00% | -15,00% | 0,06655 $ | 0/22 | 0,00% | -26,09% | DEBOLE | 17,5 | n/d |
| +20,00% | 0,09395 $ | 14/40 | +35,00% | prezzo iniziale | 0,07829 $ | 1/14 | +7,14% | -16,67% | DEBOLE | 18,1 | 28,0 |
| +20,00% | 0,09395 $ | 14/40 | +35,00% | -5,00% | 0,07438 $ | 0/14 | 0,00% | -20,83% | DEBOLE | 18,1 | n/d |
| +20,00% | 0,09395 $ | 14/40 | +35,00% | -8,00% | 0,07203 $ | 0/14 | 0,00% | -23,33% | DEBOLE | 18,1 | n/d |
| +20,00% | 0,09395 $ | 14/40 | +35,00% | -10,00% | 0,07046 $ | 0/14 | 0,00% | -25,00% | DEBOLE | 18,1 | n/d |
| +20,00% | 0,09395 $ | 14/40 | +35,00% | -15,00% | 0,06655 $ | 0/14 | 0,00% | -29,17% | DEBOLE | 18,1 | n/d |

---
