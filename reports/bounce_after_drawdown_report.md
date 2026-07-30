# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-30 07:13:54 CEST**  
UTC: **2026-07-30 05:13:54 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 60.691 $ | 70.273 $ | +25,00% | +15,79% | rimbalzo poco frequente | 70.273 $ | 60.691 $ | +4,00% | -13,64% | spike storicamente più resistente |
| SOL | 69,76 $ | 80,77 $ | +23,81% | +15,79% | rimbalzo poco frequente | 80,77 $ | 69,76 $ | 0,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06615 $ | 0,07659 $ | +33,33% | +15,79% | rimbalzo poco frequente | 0,07659 $ | 0,06615 $ | +41,38% | -13,64% | scarico possibile |

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

- BTC: su 40 casi simili, 20 prima sono scesi a -5,00%. Tra quei 20, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +25,00% (5/20). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- BTC: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 1 poi sono scaricati a -5,00%. Percentuale: +4,00% (1/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 60.691 $ | 20/40 | +50,00% | +5,00% | 67.079 $ | 7/20 | +35,00% | +10,53% | BASSA | 6,0 | 20,4 |
| -5,00% | 60.691 $ | 20/40 | +50,00% | +10,00% | 70.273 $ | 5/20 | +25,00% | +15,79% | DEBOLE | 6,0 | 20,4 |
| -5,00% | 60.691 $ | 20/40 | +50,00% | +15,00% | 73.468 $ | 5/20 | +25,00% | +21,05% | DEBOLE | 6,0 | 22,8 |
| -5,00% | 60.691 $ | 20/40 | +50,00% | +20,00% | 76.662 $ | 4/20 | +20,00% | +26,32% | DEBOLE | 6,0 | 24,8 |
| -8,00% | 58.774 $ | 17/40 | +42,50% | +5,00% | 67.079 $ | 4/17 | +23,53% | +14,13% | DEBOLE | 8,5 | 25,5 |
| -8,00% | 58.774 $ | 17/40 | +42,50% | +10,00% | 70.273 $ | 2/17 | +11,76% | +19,57% | DEBOLE | 8,5 | 23,5 |
| -8,00% | 58.774 $ | 17/40 | +42,50% | +15,00% | 73.468 $ | 2/17 | +11,76% | +25,00% | DEBOLE | 8,5 | 27,5 |
| -8,00% | 58.774 $ | 17/40 | +42,50% | +20,00% | 76.662 $ | 2/17 | +11,76% | +30,43% | DEBOLE | 8,5 | 28,5 |
| -10,00% | 57.496 $ | 15/40 | +37,50% | +5,00% | 67.079 $ | 3/15 | +20,00% | +16,67% | DEBOLE | 8,3 | 28,3 |
| -10,00% | 57.496 $ | 15/40 | +37,50% | +10,00% | 70.273 $ | 1/15 | +6,67% | +22,22% | DEBOLE | 8,3 | 30,0 |
| -10,00% | 57.496 $ | 15/40 | +37,50% | +15,00% | 73.468 $ | 1/15 | +6,67% | +27,78% | DEBOLE | 8,3 | 30,0 |
| -10,00% | 57.496 $ | 15/40 | +37,50% | +20,00% | 76.662 $ | 1/15 | +6,67% | +33,33% | DEBOLE | 8,3 | 30,0 |
| -15,00% | 54.302 $ | 11/40 | +27,50% | +5,00% | 67.079 $ | 1/11 | +9,09% | +23,53% | DEBOLE | 9,9 | 29,0 |
| -15,00% | 54.302 $ | 11/40 | +27,50% | +10,00% | 70.273 $ | 1/11 | +9,09% | +29,41% | DEBOLE | 9,9 | 30,0 |
| -15,00% | 54.302 $ | 11/40 | +27,50% | +15,00% | 73.468 $ | 1/11 | +9,09% | +35,29% | DEBOLE | 9,9 | 30,0 |
| -15,00% | 54.302 $ | 11/40 | +27,50% | +20,00% | 76.662 $ | 1/11 | +9,09% | +41,18% | DEBOLE | 9,9 | 30,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 67.079 $ | 28/40 | +70,00% | prezzo iniziale | 63.885 $ | 5/28 | +17,86% | -4,76% | DEBOLE | 10,1 | 12,0 |
| +5,00% | 67.079 $ | 28/40 | +70,00% | -5,00% | 60.691 $ | 2/28 | +7,14% | -9,52% | DEBOLE | 10,1 | 7,5 |
| +5,00% | 67.079 $ | 28/40 | +70,00% | -8,00% | 58.774 $ | 2/28 | +7,14% | -12,38% | DEBOLE | 10,1 | 9,0 |
| +5,00% | 67.079 $ | 28/40 | +70,00% | -10,00% | 57.496 $ | 1/28 | +3,57% | -14,29% | DEBOLE | 10,1 | 12,0 |
| +5,00% | 67.079 $ | 28/40 | +70,00% | -15,00% | 54.302 $ | 1/28 | +3,57% | -19,05% | DEBOLE | 10,1 | 12,0 |
| +10,00% | 70.273 $ | 25/40 | +62,50% | prezzo iniziale | 63.885 $ | 3/25 | +12,00% | -9,09% | DEBOLE | 13,6 | 16,7 |
| +10,00% | 70.273 $ | 25/40 | +62,50% | -5,00% | 60.691 $ | 1/25 | +4,00% | -13,64% | DEBOLE | 13,6 | 10,0 |
| +10,00% | 70.273 $ | 25/40 | +62,50% | -8,00% | 58.774 $ | 1/25 | +4,00% | -16,36% | DEBOLE | 13,6 | 12,0 |
| +10,00% | 70.273 $ | 25/40 | +62,50% | -10,00% | 57.496 $ | 1/25 | +4,00% | -18,18% | DEBOLE | 13,6 | 12,0 |
| +10,00% | 70.273 $ | 25/40 | +62,50% | -15,00% | 54.302 $ | 1/25 | +4,00% | -22,73% | DEBOLE | 13,6 | 12,0 |
| +15,00% | 73.468 $ | 22/40 | +55,00% | prezzo iniziale | 63.885 $ | 2/22 | +9,09% | -13,04% | DEBOLE | 15,6 | 18,5 |
| +15,00% | 73.468 $ | 22/40 | +55,00% | -5,00% | 60.691 $ | 1/22 | +4,55% | -17,39% | DEBOLE | 15,6 | 10,0 |
| +15,00% | 73.468 $ | 22/40 | +55,00% | -8,00% | 58.774 $ | 1/22 | +4,55% | -20,00% | DEBOLE | 15,6 | 12,0 |
| +15,00% | 73.468 $ | 22/40 | +55,00% | -10,00% | 57.496 $ | 1/22 | +4,55% | -21,74% | DEBOLE | 15,6 | 12,0 |
| +15,00% | 73.468 $ | 22/40 | +55,00% | -15,00% | 54.302 $ | 1/22 | +4,55% | -26,09% | DEBOLE | 15,6 | 12,0 |
| +20,00% | 76.662 $ | 17/40 | +42,50% | prezzo iniziale | 63.885 $ | 0/17 | 0,00% | -16,67% | DEBOLE | 17,9 | n/d |
| +20,00% | 76.662 $ | 17/40 | +42,50% | -5,00% | 60.691 $ | 0/17 | 0,00% | -20,83% | DEBOLE | 17,9 | n/d |
| +20,00% | 76.662 $ | 17/40 | +42,50% | -8,00% | 58.774 $ | 0/17 | 0,00% | -23,33% | DEBOLE | 17,9 | n/d |
| +20,00% | 76.662 $ | 17/40 | +42,50% | -10,00% | 57.496 $ | 0/17 | 0,00% | -25,00% | DEBOLE | 17,9 | n/d |
| +20,00% | 76.662 $ | 17/40 | +42,50% | -15,00% | 54.302 $ | 0/17 | 0,00% | -29,17% | DEBOLE | 17,9 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 21 prima sono scesi a -5,00%. Tra quei 21, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +23,81% (5/21). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 22 prima sono saliti a +10,00%. Tra quei 22, 0 poi sono scaricati a -5,00%. Percentuale: 0,00% (0/22). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 69,76 $ | 21/40 | +52,50% | +5,00% | 77,10 $ | 7/21 | +33,33% | +10,53% | DEBOLE | 7,7 | 18,4 |
| -5,00% | 69,76 $ | 21/40 | +52,50% | +10,00% | 80,77 $ | 5/21 | +23,81% | +15,79% | DEBOLE | 7,7 | 19,2 |
| -5,00% | 69,76 $ | 21/40 | +52,50% | +15,00% | 84,44 $ | 4/21 | +19,05% | +21,05% | DEBOLE | 7,7 | 18,0 |
| -5,00% | 69,76 $ | 21/40 | +52,50% | +20,00% | 88,12 $ | 3/21 | +14,29% | +26,32% | DEBOLE | 7,7 | 20,3 |
| -8,00% | 67,56 $ | 17/40 | +42,50% | +5,00% | 77,10 $ | 3/17 | +17,65% | +14,13% | DEBOLE | 9,9 | 23,0 |
| -8,00% | 67,56 $ | 17/40 | +42,50% | +10,00% | 80,77 $ | 2/17 | +11,76% | +19,57% | DEBOLE | 9,9 | 26,0 |
| -8,00% | 67,56 $ | 17/40 | +42,50% | +15,00% | 84,44 $ | 1/17 | +5,88% | +25,00% | DEBOLE | 9,9 | 23,0 |
| -8,00% | 67,56 $ | 17/40 | +42,50% | +20,00% | 88,12 $ | 1/17 | +5,88% | +30,43% | DEBOLE | 9,9 | 23,0 |
| -10,00% | 66,09 $ | 17/40 | +42,50% | +5,00% | 77,10 $ | 3/17 | +17,65% | +16,67% | DEBOLE | 11,1 | 23,0 |
| -10,00% | 66,09 $ | 17/40 | +42,50% | +10,00% | 80,77 $ | 2/17 | +11,76% | +22,22% | DEBOLE | 11,1 | 26,0 |
| -10,00% | 66,09 $ | 17/40 | +42,50% | +15,00% | 84,44 $ | 1/17 | +5,88% | +27,78% | DEBOLE | 11,1 | 23,0 |
| -10,00% | 66,09 $ | 17/40 | +42,50% | +20,00% | 88,12 $ | 1/17 | +5,88% | +33,33% | DEBOLE | 11,1 | 23,0 |
| -15,00% | 62,42 $ | 8/40 | +20,00% | +5,00% | 77,10 $ | 0/8 | 0,00% | +23,53% | DEBOLE | 15,4 | n/d |
| -15,00% | 62,42 $ | 8/40 | +20,00% | +10,00% | 80,77 $ | 0/8 | 0,00% | +29,41% | DEBOLE | 15,4 | n/d |
| -15,00% | 62,42 $ | 8/40 | +20,00% | +15,00% | 84,44 $ | 0/8 | 0,00% | +35,29% | DEBOLE | 15,4 | n/d |
| -15,00% | 62,42 $ | 8/40 | +20,00% | +20,00% | 88,12 $ | 0/8 | 0,00% | +41,18% | DEBOLE | 15,4 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 77,10 $ | 28/40 | +70,00% | prezzo iniziale | 73,43 $ | 8/28 | +28,57% | -4,76% | DEBOLE | 8,6 | 10,4 |
| +5,00% | 77,10 $ | 28/40 | +70,00% | -5,00% | 69,76 $ | 4/28 | +14,29% | -9,52% | DEBOLE | 8,6 | 10,5 |
| +5,00% | 77,10 $ | 28/40 | +70,00% | -8,00% | 67,56 $ | 2/28 | +7,14% | -12,38% | DEBOLE | 8,6 | 14,5 |
| +5,00% | 77,10 $ | 28/40 | +70,00% | -10,00% | 66,09 $ | 2/28 | +7,14% | -14,29% | DEBOLE | 8,6 | 16,5 |
| +5,00% | 77,10 $ | 28/40 | +70,00% | -15,00% | 62,42 $ | 0/28 | 0,00% | -19,05% | DEBOLE | 8,6 | n/d |
| +10,00% | 80,77 $ | 22/40 | +55,00% | prezzo iniziale | 73,43 $ | 2/22 | +9,09% | -9,09% | DEBOLE | 12,3 | 17,5 |
| +10,00% | 80,77 $ | 22/40 | +55,00% | -5,00% | 69,76 $ | 0/22 | 0,00% | -13,64% | DEBOLE | 12,3 | n/d |
| +10,00% | 80,77 $ | 22/40 | +55,00% | -8,00% | 67,56 $ | 0/22 | 0,00% | -16,36% | DEBOLE | 12,3 | n/d |
| +10,00% | 80,77 $ | 22/40 | +55,00% | -10,00% | 66,09 $ | 0/22 | 0,00% | -18,18% | DEBOLE | 12,3 | n/d |
| +10,00% | 80,77 $ | 22/40 | +55,00% | -15,00% | 62,42 $ | 0/22 | 0,00% | -22,73% | DEBOLE | 12,3 | n/d |
| +15,00% | 84,44 $ | 18/40 | +45,00% | prezzo iniziale | 73,43 $ | 1/18 | +5,56% | -13,04% | DEBOLE | 13,3 | 22,0 |
| +15,00% | 84,44 $ | 18/40 | +45,00% | -5,00% | 69,76 $ | 0/18 | 0,00% | -17,39% | DEBOLE | 13,3 | n/d |
| +15,00% | 84,44 $ | 18/40 | +45,00% | -8,00% | 67,56 $ | 0/18 | 0,00% | -20,00% | DEBOLE | 13,3 | n/d |
| +15,00% | 84,44 $ | 18/40 | +45,00% | -10,00% | 66,09 $ | 0/18 | 0,00% | -21,74% | DEBOLE | 13,3 | n/d |
| +15,00% | 84,44 $ | 18/40 | +45,00% | -15,00% | 62,42 $ | 0/18 | 0,00% | -26,09% | DEBOLE | 13,3 | n/d |
| +20,00% | 88,12 $ | 15/40 | +37,50% | prezzo iniziale | 73,43 $ | 0/15 | 0,00% | -16,67% | DEBOLE | 15,7 | n/d |
| +20,00% | 88,12 $ | 15/40 | +37,50% | -5,00% | 69,76 $ | 0/15 | 0,00% | -20,83% | DEBOLE | 15,7 | n/d |
| +20,00% | 88,12 $ | 15/40 | +37,50% | -8,00% | 67,56 $ | 0/15 | 0,00% | -23,33% | DEBOLE | 15,7 | n/d |
| +20,00% | 88,12 $ | 15/40 | +37,50% | -10,00% | 66,09 $ | 0/15 | 0,00% | -25,00% | DEBOLE | 15,7 | n/d |
| +20,00% | 88,12 $ | 15/40 | +37,50% | -15,00% | 62,42 $ | 0/15 | 0,00% | -29,17% | DEBOLE | 15,7 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 27 prima sono scesi a -5,00%. Tra quei 27, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +33,33% (9/27). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 29 prima sono saliti a +10,00%. Tra quei 29, 12 poi sono scaricati a -5,00%. Percentuale: +41,38% (12/29). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06615 $ | 27/40 | +67,50% | +5,00% | 0,07311 $ | 12/27 | +44,44% | +10,53% | BASSA | 10,3 | 23,2 |
| -5,00% | 0,06615 $ | 27/40 | +67,50% | +10,00% | 0,07659 $ | 9/27 | +33,33% | +15,79% | DEBOLE | 10,3 | 24,8 |
| -5,00% | 0,06615 $ | 27/40 | +67,50% | +15,00% | 0,08007 $ | 5/27 | +18,52% | +21,05% | DEBOLE | 10,3 | 22,4 |
| -5,00% | 0,06615 $ | 27/40 | +67,50% | +20,00% | 0,08356 $ | 3/27 | +11,11% | +26,32% | DEBOLE | 10,3 | 18,3 |
| -8,00% | 0,06406 $ | 24/40 | +60,00% | +5,00% | 0,07311 $ | 10/24 | +41,67% | +14,13% | BASSA | 12,5 | 24,4 |
| -8,00% | 0,06406 $ | 24/40 | +60,00% | +10,00% | 0,07659 $ | 7/24 | +29,17% | +19,57% | DEBOLE | 12,5 | 25,0 |
| -8,00% | 0,06406 $ | 24/40 | +60,00% | +15,00% | 0,08007 $ | 3/24 | +12,50% | +25,00% | DEBOLE | 12,5 | 21,3 |
| -8,00% | 0,06406 $ | 24/40 | +60,00% | +20,00% | 0,08356 $ | 2/24 | +8,33% | +30,43% | DEBOLE | 12,5 | 17,5 |
| -10,00% | 0,06267 $ | 20/40 | +50,00% | +5,00% | 0,07311 $ | 6/20 | +30,00% | +16,67% | DEBOLE | 11,9 | 22,0 |
| -10,00% | 0,06267 $ | 20/40 | +50,00% | +10,00% | 0,07659 $ | 3/20 | +15,00% | +22,22% | DEBOLE | 11,9 | 20,3 |
| -10,00% | 0,06267 $ | 20/40 | +50,00% | +15,00% | 0,08007 $ | 2/20 | +10,00% | +27,78% | DEBOLE | 11,9 | 18,0 |
| -10,00% | 0,06267 $ | 20/40 | +50,00% | +20,00% | 0,08356 $ | 1/20 | +5,00% | +33,33% | DEBOLE | 11,9 | 7,0 |
| -15,00% | 0,05919 $ | 13/40 | +32,50% | +5,00% | 0,07311 $ | 0/13 | 0,00% | +23,53% | DEBOLE | 15,0 | n/d |
| -15,00% | 0,05919 $ | 13/40 | +32,50% | +10,00% | 0,07659 $ | 0/13 | 0,00% | +29,41% | DEBOLE | 15,0 | n/d |
| -15,00% | 0,05919 $ | 13/40 | +32,50% | +15,00% | 0,08007 $ | 0/13 | 0,00% | +35,29% | DEBOLE | 15,0 | n/d |
| -15,00% | 0,05919 $ | 13/40 | +32,50% | +20,00% | 0,08356 $ | 0/13 | 0,00% | +41,18% | DEBOLE | 15,0 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07311 $ | 34/40 | +85,00% | prezzo iniziale | 0,06963 $ | 26/34 | +76,47% | -4,76% | ALTA | 5,3 | 9,9 |
| +5,00% | 0,07311 $ | 34/40 | +85,00% | -5,00% | 0,06615 $ | 19/34 | +55,88% | -9,52% | MEDIA | 5,3 | 12,5 |
| +5,00% | 0,07311 $ | 34/40 | +85,00% | -8,00% | 0,06406 $ | 16/34 | +47,06% | -12,38% | BASSA | 5,3 | 13,9 |
| +5,00% | 0,07311 $ | 34/40 | +85,00% | -10,00% | 0,06267 $ | 12/34 | +35,29% | -14,29% | BASSA | 5,3 | 12,9 |
| +5,00% | 0,07311 $ | 34/40 | +85,00% | -15,00% | 0,05919 $ | 7/34 | +20,59% | -19,05% | DEBOLE | 5,3 | 17,4 |
| +10,00% | 0,07659 $ | 29/40 | +72,50% | prezzo iniziale | 0,06963 $ | 18/29 | +62,07% | -9,09% | MEDIA | 9,6 | 12,4 |
| +10,00% | 0,07659 $ | 29/40 | +72,50% | -5,00% | 0,06615 $ | 12/29 | +41,38% | -13,64% | BASSA | 9,6 | 15,3 |
| +10,00% | 0,07659 $ | 29/40 | +72,50% | -8,00% | 0,06406 $ | 9/29 | +31,03% | -16,36% | DEBOLE | 9,6 | 16,6 |
| +10,00% | 0,07659 $ | 29/40 | +72,50% | -10,00% | 0,06267 $ | 6/29 | +20,69% | -18,18% | DEBOLE | 9,6 | 13,8 |
| +10,00% | 0,07659 $ | 29/40 | +72,50% | -15,00% | 0,05919 $ | 6/29 | +20,69% | -22,73% | DEBOLE | 9,6 | 16,5 |
| +15,00% | 0,08007 $ | 20/40 | +50,00% | prezzo iniziale | 0,06963 $ | 7/20 | +35,00% | -13,04% | BASSA | 13,9 | 15,0 |
| +15,00% | 0,08007 $ | 20/40 | +50,00% | -5,00% | 0,06615 $ | 4/20 | +20,00% | -17,39% | DEBOLE | 13,9 | 16,8 |
| +15,00% | 0,08007 $ | 20/40 | +50,00% | -8,00% | 0,06406 $ | 3/20 | +15,00% | -20,00% | DEBOLE | 13,9 | 17,3 |
| +15,00% | 0,08007 $ | 20/40 | +50,00% | -10,00% | 0,06267 $ | 2/20 | +10,00% | -21,74% | DEBOLE | 13,9 | 14,5 |
| +15,00% | 0,08007 $ | 20/40 | +50,00% | -15,00% | 0,05919 $ | 2/20 | +10,00% | -26,09% | DEBOLE | 13,9 | 17,0 |
| +20,00% | 0,08356 $ | 14/40 | +35,00% | prezzo iniziale | 0,06963 $ | 3/14 | +21,43% | -16,67% | DEBOLE | 14,4 | 19,7 |
| +20,00% | 0,08356 $ | 14/40 | +35,00% | -5,00% | 0,06615 $ | 1/14 | +7,14% | -20,83% | DEBOLE | 14,4 | 26,0 |
| +20,00% | 0,08356 $ | 14/40 | +35,00% | -8,00% | 0,06406 $ | 0/14 | 0,00% | -23,33% | DEBOLE | 14,4 | n/d |
| +20,00% | 0,08356 $ | 14/40 | +35,00% | -10,00% | 0,06267 $ | 0/14 | 0,00% | -25,00% | DEBOLE | 14,4 | n/d |
| +20,00% | 0,08356 $ | 14/40 | +35,00% | -15,00% | 0,05919 $ | 0/14 | 0,00% | -29,17% | DEBOLE | 14,4 | n/d |

---
