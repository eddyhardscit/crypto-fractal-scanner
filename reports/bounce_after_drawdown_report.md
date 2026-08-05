# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-08-05 07:14:30 CEST**  
UTC: **2026-08-05 05:14:30 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 61.046 $ | 70.684 $ | +27,78% | +15,79% | rimbalzo poco frequente | 70.684 $ | 61.046 $ | +7,69% | -13,64% | spike storicamente più resistente |
| SOL | 70,21 $ | 81,30 $ | +21,43% | +15,79% | rimbalzo poco frequente | 81,30 $ | 70,21 $ | 0,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06642 $ | 0,07691 $ | +33,33% | +15,79% | rimbalzo poco frequente | 0,07691 $ | 0,06642 $ | +22,73% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 18 prima sono scesi a -5,00%. Tra quei 18, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +27,78% (5/18). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- BTC: su 40 casi simili, 26 prima sono saliti a +10,00%. Tra quei 26, 2 poi sono scaricati a -5,00%. Percentuale: +7,69% (2/26). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 61.046 $ | 18/40 | +45,00% | +5,00% | 67.471 $ | 9/18 | +50,00% | +10,53% | MEDIA | 8,7 | 18,6 |
| -5,00% | 61.046 $ | 18/40 | +45,00% | +10,00% | 70.684 $ | 5/18 | +27,78% | +15,79% | DEBOLE | 8,7 | 19,0 |
| -5,00% | 61.046 $ | 18/40 | +45,00% | +15,00% | 73.897 $ | 4/18 | +22,22% | +21,05% | DEBOLE | 8,7 | 18,2 |
| -5,00% | 61.046 $ | 18/40 | +45,00% | +20,00% | 77.110 $ | 4/18 | +22,22% | +26,32% | DEBOLE | 8,7 | 19,0 |
| -8,00% | 59.118 $ | 14/40 | +35,00% | +5,00% | 67.471 $ | 4/14 | +28,57% | +14,13% | DEBOLE | 10,1 | 24,8 |
| -8,00% | 59.118 $ | 14/40 | +35,00% | +10,00% | 70.684 $ | 2/14 | +14,29% | +19,57% | DEBOLE | 10,1 | 26,5 |
| -8,00% | 59.118 $ | 14/40 | +35,00% | +15,00% | 73.897 $ | 1/14 | +7,14% | +25,00% | DEBOLE | 10,1 | 28,0 |
| -8,00% | 59.118 $ | 14/40 | +35,00% | +20,00% | 77.110 $ | 1/14 | +7,14% | +30,43% | DEBOLE | 10,1 | 30,0 |
| -10,00% | 57.833 $ | 13/40 | +32,50% | +5,00% | 67.471 $ | 3/13 | +23,08% | +16,67% | DEBOLE | 11,1 | 26,3 |
| -10,00% | 57.833 $ | 13/40 | +32,50% | +10,00% | 70.684 $ | 1/13 | +7,69% | +22,22% | DEBOLE | 11,1 | 26,0 |
| -10,00% | 57.833 $ | 13/40 | +32,50% | +15,00% | 73.897 $ | 0/13 | 0,00% | +27,78% | DEBOLE | 11,1 | n/d |
| -10,00% | 57.833 $ | 13/40 | +32,50% | +20,00% | 77.110 $ | 0/13 | 0,00% | +33,33% | DEBOLE | 11,1 | n/d |
| -15,00% | 54.620 $ | 6/40 | +15,00% | +5,00% | 67.471 $ | 0/6 | 0,00% | +23,53% | DEBOLE | 10,5 | n/d |
| -15,00% | 54.620 $ | 6/40 | +15,00% | +10,00% | 70.684 $ | 0/6 | 0,00% | +29,41% | DEBOLE | 10,5 | n/d |
| -15,00% | 54.620 $ | 6/40 | +15,00% | +15,00% | 73.897 $ | 0/6 | 0,00% | +35,29% | DEBOLE | 10,5 | n/d |
| -15,00% | 54.620 $ | 6/40 | +15,00% | +20,00% | 77.110 $ | 0/6 | 0,00% | +41,18% | DEBOLE | 10,5 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 67.471 $ | 35/40 | +87,50% | prezzo iniziale | 64.258 $ | 10/35 | +28,57% | -4,76% | DEBOLE | 9,2 | 11,6 |
| +5,00% | 67.471 $ | 35/40 | +87,50% | -5,00% | 61.046 $ | 7/35 | +20,00% | -9,52% | DEBOLE | 9,2 | 13,7 |
| +5,00% | 67.471 $ | 35/40 | +87,50% | -8,00% | 59.118 $ | 6/35 | +17,14% | -12,38% | DEBOLE | 9,2 | 15,0 |
| +5,00% | 67.471 $ | 35/40 | +87,50% | -10,00% | 57.833 $ | 6/35 | +17,14% | -14,29% | DEBOLE | 9,2 | 15,7 |
| +5,00% | 67.471 $ | 35/40 | +87,50% | -15,00% | 54.620 $ | 3/35 | +8,57% | -19,05% | DEBOLE | 9,2 | 9,7 |
| +10,00% | 70.684 $ | 26/40 | +65,00% | prezzo iniziale | 64.258 $ | 2/26 | +7,69% | -9,09% | DEBOLE | 14,6 | 11,5 |
| +10,00% | 70.684 $ | 26/40 | +65,00% | -5,00% | 61.046 $ | 2/26 | +7,69% | -13,64% | DEBOLE | 14,6 | 16,0 |
| +10,00% | 70.684 $ | 26/40 | +65,00% | -8,00% | 59.118 $ | 2/26 | +7,69% | -16,36% | DEBOLE | 14,6 | 16,5 |
| +10,00% | 70.684 $ | 26/40 | +65,00% | -10,00% | 57.833 $ | 2/26 | +7,69% | -18,18% | DEBOLE | 14,6 | 17,0 |
| +10,00% | 70.684 $ | 26/40 | +65,00% | -15,00% | 54.620 $ | 1/26 | +3,85% | -22,73% | DEBOLE | 14,6 | 10,0 |
| +15,00% | 73.897 $ | 19/40 | +47,50% | prezzo iniziale | 64.258 $ | 1/19 | +5,26% | -13,04% | DEBOLE | 14,5 | 6,0 |
| +15,00% | 73.897 $ | 19/40 | +47,50% | -5,00% | 61.046 $ | 1/19 | +5,26% | -17,39% | DEBOLE | 14,5 | 7,0 |
| +15,00% | 73.897 $ | 19/40 | +47,50% | -8,00% | 59.118 $ | 1/19 | +5,26% | -20,00% | DEBOLE | 14,5 | 7,0 |
| +15,00% | 73.897 $ | 19/40 | +47,50% | -10,00% | 57.833 $ | 1/19 | +5,26% | -21,74% | DEBOLE | 14,5 | 7,0 |
| +15,00% | 73.897 $ | 19/40 | +47,50% | -15,00% | 54.620 $ | 1/19 | +5,26% | -26,09% | DEBOLE | 14,5 | 10,0 |
| +20,00% | 77.110 $ | 15/40 | +37,50% | prezzo iniziale | 64.258 $ | 1/15 | +6,67% | -16,67% | DEBOLE | 15,7 | 6,0 |
| +20,00% | 77.110 $ | 15/40 | +37,50% | -5,00% | 61.046 $ | 1/15 | +6,67% | -20,83% | DEBOLE | 15,7 | 7,0 |
| +20,00% | 77.110 $ | 15/40 | +37,50% | -8,00% | 59.118 $ | 1/15 | +6,67% | -23,33% | DEBOLE | 15,7 | 7,0 |
| +20,00% | 77.110 $ | 15/40 | +37,50% | -10,00% | 57.833 $ | 1/15 | +6,67% | -25,00% | DEBOLE | 15,7 | 7,0 |
| +20,00% | 77.110 $ | 15/40 | +37,50% | -15,00% | 54.620 $ | 1/15 | +6,67% | -29,17% | DEBOLE | 15,7 | 10,0 |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 14 prima sono scesi a -5,00%. Tra quei 14, 3 poi sono rimbalzati fino a +10,00%. Percentuale: +21,43% (3/14). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 24 prima sono saliti a +10,00%. Tra quei 24, 0 poi sono scaricati a -5,00%. Percentuale: 0,00% (0/24). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 70,21 $ | 14/40 | +35,00% | +5,00% | 77,61 $ | 5/14 | +35,71% | +10,53% | BASSA | 5,9 | 21,2 |
| -5,00% | 70,21 $ | 14/40 | +35,00% | +10,00% | 81,30 $ | 3/14 | +21,43% | +15,79% | DEBOLE | 5,9 | 26,7 |
| -5,00% | 70,21 $ | 14/40 | +35,00% | +15,00% | 85,00 $ | 1/14 | +7,14% | +21,05% | DEBOLE | 5,9 | 25,0 |
| -5,00% | 70,21 $ | 14/40 | +35,00% | +20,00% | 88,69 $ | 1/14 | +7,14% | +26,32% | DEBOLE | 5,9 | 25,0 |
| -8,00% | 68,00 $ | 12/40 | +30,00% | +5,00% | 77,61 $ | 3/12 | +25,00% | +14,13% | DEBOLE | 7,9 | 28,7 |
| -8,00% | 68,00 $ | 12/40 | +30,00% | +10,00% | 81,30 $ | 2/12 | +16,67% | +19,57% | DEBOLE | 7,9 | 30,0 |
| -8,00% | 68,00 $ | 12/40 | +30,00% | +15,00% | 85,00 $ | 0/12 | 0,00% | +25,00% | DEBOLE | 7,9 | n/d |
| -8,00% | 68,00 $ | 12/40 | +30,00% | +20,00% | 88,69 $ | 0/12 | 0,00% | +30,43% | DEBOLE | 7,9 | n/d |
| -10,00% | 66,52 $ | 12/40 | +30,00% | +5,00% | 77,61 $ | 3/12 | +25,00% | +16,67% | DEBOLE | 8,7 | 28,7 |
| -10,00% | 66,52 $ | 12/40 | +30,00% | +10,00% | 81,30 $ | 2/12 | +16,67% | +22,22% | DEBOLE | 8,7 | 30,0 |
| -10,00% | 66,52 $ | 12/40 | +30,00% | +15,00% | 85,00 $ | 0/12 | 0,00% | +27,78% | DEBOLE | 8,7 | n/d |
| -10,00% | 66,52 $ | 12/40 | +30,00% | +20,00% | 88,69 $ | 0/12 | 0,00% | +33,33% | DEBOLE | 8,7 | n/d |
| -15,00% | 62,82 $ | 8/40 | +20,00% | +5,00% | 77,61 $ | 1/8 | +12,50% | +23,53% | DEBOLE | 9,6 | 28,0 |
| -15,00% | 62,82 $ | 8/40 | +20,00% | +10,00% | 81,30 $ | 1/8 | +12,50% | +29,41% | DEBOLE | 9,6 | 30,0 |
| -15,00% | 62,82 $ | 8/40 | +20,00% | +15,00% | 85,00 $ | 0/8 | 0,00% | +35,29% | DEBOLE | 9,6 | n/d |
| -15,00% | 62,82 $ | 8/40 | +20,00% | +20,00% | 88,69 $ | 0/8 | 0,00% | +41,18% | DEBOLE | 9,6 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 77,61 $ | 29/40 | +72,50% | prezzo iniziale | 73,91 $ | 5/29 | +17,24% | -4,76% | DEBOLE | 8,8 | 10,2 |
| +5,00% | 77,61 $ | 29/40 | +72,50% | -5,00% | 70,21 $ | 1/29 | +3,45% | -9,52% | DEBOLE | 8,8 | 10,0 |
| +5,00% | 77,61 $ | 29/40 | +72,50% | -8,00% | 68,00 $ | 0/29 | 0,00% | -12,38% | DEBOLE | 8,8 | n/d |
| +5,00% | 77,61 $ | 29/40 | +72,50% | -10,00% | 66,52 $ | 0/29 | 0,00% | -14,29% | DEBOLE | 8,8 | n/d |
| +5,00% | 77,61 $ | 29/40 | +72,50% | -15,00% | 62,82 $ | 0/29 | 0,00% | -19,05% | DEBOLE | 8,8 | n/d |
| +10,00% | 81,30 $ | 24/40 | +60,00% | prezzo iniziale | 73,91 $ | 0/24 | 0,00% | -9,09% | DEBOLE | 13,1 | n/d |
| +10,00% | 81,30 $ | 24/40 | +60,00% | -5,00% | 70,21 $ | 0/24 | 0,00% | -13,64% | DEBOLE | 13,1 | n/d |
| +10,00% | 81,30 $ | 24/40 | +60,00% | -8,00% | 68,00 $ | 0/24 | 0,00% | -16,36% | DEBOLE | 13,1 | n/d |
| +10,00% | 81,30 $ | 24/40 | +60,00% | -10,00% | 66,52 $ | 0/24 | 0,00% | -18,18% | DEBOLE | 13,1 | n/d |
| +10,00% | 81,30 $ | 24/40 | +60,00% | -15,00% | 62,82 $ | 0/24 | 0,00% | -22,73% | DEBOLE | 13,1 | n/d |
| +15,00% | 85,00 $ | 17/40 | +42,50% | prezzo iniziale | 73,91 $ | 0/17 | 0,00% | -13,04% | DEBOLE | 13,3 | n/d |
| +15,00% | 85,00 $ | 17/40 | +42,50% | -5,00% | 70,21 $ | 0/17 | 0,00% | -17,39% | DEBOLE | 13,3 | n/d |
| +15,00% | 85,00 $ | 17/40 | +42,50% | -8,00% | 68,00 $ | 0/17 | 0,00% | -20,00% | DEBOLE | 13,3 | n/d |
| +15,00% | 85,00 $ | 17/40 | +42,50% | -10,00% | 66,52 $ | 0/17 | 0,00% | -21,74% | DEBOLE | 13,3 | n/d |
| +15,00% | 85,00 $ | 17/40 | +42,50% | -15,00% | 62,82 $ | 0/17 | 0,00% | -26,09% | DEBOLE | 13,3 | n/d |
| +20,00% | 88,69 $ | 14/40 | +35,00% | prezzo iniziale | 73,91 $ | 0/14 | 0,00% | -16,67% | DEBOLE | 16,9 | n/d |
| +20,00% | 88,69 $ | 14/40 | +35,00% | -5,00% | 70,21 $ | 0/14 | 0,00% | -20,83% | DEBOLE | 16,9 | n/d |
| +20,00% | 88,69 $ | 14/40 | +35,00% | -8,00% | 68,00 $ | 0/14 | 0,00% | -23,33% | DEBOLE | 16,9 | n/d |
| +20,00% | 88,69 $ | 14/40 | +35,00% | -10,00% | 66,52 $ | 0/14 | 0,00% | -25,00% | DEBOLE | 16,9 | n/d |
| +20,00% | 88,69 $ | 14/40 | +35,00% | -15,00% | 62,82 $ | 0/14 | 0,00% | -29,17% | DEBOLE | 16,9 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 33 prima sono scesi a -5,00%. Tra quei 33, 11 poi sono rimbalzati fino a +10,00%. Percentuale: +33,33% (11/33). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 22 prima sono saliti a +10,00%. Tra quei 22, 5 poi sono scaricati a -5,00%. Percentuale: +22,73% (5/22). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06642 $ | 33/40 | +82,50% | +5,00% | 0,07342 $ | 16/33 | +48,48% | +10,53% | BASSA | 5,4 | 20,2 |
| -5,00% | 0,06642 $ | 33/40 | +82,50% | +10,00% | 0,07691 $ | 11/33 | +33,33% | +15,79% | DEBOLE | 5,4 | 21,3 |
| -5,00% | 0,06642 $ | 33/40 | +82,50% | +15,00% | 0,08041 $ | 10/33 | +30,30% | +21,05% | DEBOLE | 5,4 | 21,9 |
| -5,00% | 0,06642 $ | 33/40 | +82,50% | +20,00% | 0,08390 $ | 5/33 | +15,15% | +26,32% | DEBOLE | 5,4 | 20,6 |
| -8,00% | 0,06433 $ | 29/40 | +72,50% | +5,00% | 0,07342 $ | 12/29 | +41,38% | +14,13% | BASSA | 6,5 | 20,2 |
| -8,00% | 0,06433 $ | 29/40 | +72,50% | +10,00% | 0,07691 $ | 8/29 | +27,59% | +19,57% | DEBOLE | 6,5 | 21,0 |
| -8,00% | 0,06433 $ | 29/40 | +72,50% | +15,00% | 0,08041 $ | 7/29 | +24,14% | +25,00% | DEBOLE | 6,5 | 20,1 |
| -8,00% | 0,06433 $ | 29/40 | +72,50% | +20,00% | 0,08390 $ | 5/29 | +17,24% | +30,43% | DEBOLE | 6,5 | 20,6 |
| -10,00% | 0,06293 $ | 26/40 | +65,00% | +5,00% | 0,07342 $ | 9/26 | +34,62% | +16,67% | DEBOLE | 8,2 | 23,2 |
| -10,00% | 0,06293 $ | 26/40 | +65,00% | +10,00% | 0,07691 $ | 5/26 | +19,23% | +22,22% | DEBOLE | 8,2 | 24,4 |
| -10,00% | 0,06293 $ | 26/40 | +65,00% | +15,00% | 0,08041 $ | 4/26 | +15,38% | +27,78% | DEBOLE | 8,2 | 23,8 |
| -10,00% | 0,06293 $ | 26/40 | +65,00% | +20,00% | 0,08390 $ | 2/26 | +7,69% | +33,33% | DEBOLE | 8,2 | 25,0 |
| -15,00% | 0,05943 $ | 19/40 | +47,50% | +5,00% | 0,07342 $ | 4/19 | +21,05% | +23,53% | DEBOLE | 11,2 | 24,5 |
| -15,00% | 0,05943 $ | 19/40 | +47,50% | +10,00% | 0,07691 $ | 3/19 | +15,79% | +29,41% | DEBOLE | 11,2 | 25,3 |
| -15,00% | 0,05943 $ | 19/40 | +47,50% | +15,00% | 0,08041 $ | 2/19 | +10,53% | +35,29% | DEBOLE | 11,2 | 23,5 |
| -15,00% | 0,05943 $ | 19/40 | +47,50% | +20,00% | 0,08390 $ | 2/19 | +10,53% | +41,18% | DEBOLE | 11,2 | 25,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07342 $ | 28/40 | +70,00% | prezzo iniziale | 0,06992 $ | 18/28 | +64,29% | -4,76% | MEDIA | 10,5 | 15,6 |
| +5,00% | 0,07342 $ | 28/40 | +70,00% | -5,00% | 0,06642 $ | 11/28 | +39,29% | -9,52% | BASSA | 10,5 | 14,1 |
| +5,00% | 0,07342 $ | 28/40 | +70,00% | -8,00% | 0,06433 $ | 9/28 | +32,14% | -12,38% | DEBOLE | 10,5 | 14,6 |
| +5,00% | 0,07342 $ | 28/40 | +70,00% | -10,00% | 0,06293 $ | 7/28 | +25,00% | -14,29% | DEBOLE | 10,5 | 14,7 |
| +5,00% | 0,07342 $ | 28/40 | +70,00% | -15,00% | 0,05943 $ | 4/28 | +14,29% | -19,05% | DEBOLE | 10,5 | 14,2 |
| +10,00% | 0,07691 $ | 22/40 | +55,00% | prezzo iniziale | 0,06992 $ | 9/22 | +40,91% | -9,09% | BASSA | 13,1 | 17,0 |
| +10,00% | 0,07691 $ | 22/40 | +55,00% | -5,00% | 0,06642 $ | 5/22 | +22,73% | -13,64% | DEBOLE | 13,1 | 16,2 |
| +10,00% | 0,07691 $ | 22/40 | +55,00% | -8,00% | 0,06433 $ | 4/22 | +18,18% | -16,36% | DEBOLE | 13,1 | 16,2 |
| +10,00% | 0,07691 $ | 22/40 | +55,00% | -10,00% | 0,06293 $ | 4/22 | +18,18% | -18,18% | DEBOLE | 13,1 | 16,8 |
| +10,00% | 0,07691 $ | 22/40 | +55,00% | -15,00% | 0,05943 $ | 3/22 | +13,64% | -22,73% | DEBOLE | 13,1 | 16,0 |
| +15,00% | 0,08041 $ | 18/40 | +45,00% | prezzo iniziale | 0,06992 $ | 5/18 | +27,78% | -13,04% | DEBOLE | 14,4 | 15,6 |
| +15,00% | 0,08041 $ | 18/40 | +45,00% | -5,00% | 0,06642 $ | 3/18 | +16,67% | -17,39% | DEBOLE | 14,4 | 14,3 |
| +15,00% | 0,08041 $ | 18/40 | +45,00% | -8,00% | 0,06433 $ | 2/18 | +11,11% | -20,00% | DEBOLE | 14,4 | 13,5 |
| +15,00% | 0,08041 $ | 18/40 | +45,00% | -10,00% | 0,06293 $ | 2/18 | +11,11% | -21,74% | DEBOLE | 14,4 | 13,5 |
| +15,00% | 0,08041 $ | 18/40 | +45,00% | -15,00% | 0,05943 $ | 2/18 | +11,11% | -26,09% | DEBOLE | 14,4 | 18,0 |
| +20,00% | 0,08390 $ | 12/40 | +30,00% | prezzo iniziale | 0,06992 $ | 2/12 | +16,67% | -16,67% | DEBOLE | 16,2 | 23,5 |
| +20,00% | 0,08390 $ | 12/40 | +30,00% | -5,00% | 0,06642 $ | 1/12 | +8,33% | -20,83% | DEBOLE | 16,2 | 17,0 |
| +20,00% | 0,08390 $ | 12/40 | +30,00% | -8,00% | 0,06433 $ | 0/12 | 0,00% | -23,33% | DEBOLE | 16,2 | n/d |
| +20,00% | 0,08390 $ | 12/40 | +30,00% | -10,00% | 0,06293 $ | 0/12 | 0,00% | -25,00% | DEBOLE | 16,2 | n/d |
| +20,00% | 0,08390 $ | 12/40 | +30,00% | -15,00% | 0,05943 $ | 0/12 | 0,00% | -29,17% | DEBOLE | 16,2 | n/d |

---
