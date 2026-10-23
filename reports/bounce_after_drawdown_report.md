# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-10-23 07:32:52 CEST**  
UTC: **2026-10-23 05:32:52 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 77.435 $ | 89.662 $ | +41,38% | +15,79% | rimbalzo debole | 89.662 $ | 77.435 $ | +12,50% | -13,64% | spike storicamente più resistente |
| SOL | 98,89 $ | 114,50 $ | +44,83% | +15,79% | rimbalzo debole | 114,50 $ | 98,89 $ | +7,69% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07561 $ | 0,08755 $ | +56,00% | +15,79% | rimbalzo possibile | 0,08755 $ | 0,07561 $ | +6,67% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 29 prima sono scesi a -5,00%. Tra quei 29, 12 poi sono rimbalzati fino a +10,00%. Percentuale: +41,38% (12/29). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 24 prima sono saliti a +10,00%. Tra quei 24, 3 poi sono scaricati a -5,00%. Percentuale: +12,50% (3/24). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 77.435 $ | 29/40 | +72,50% | +5,00% | 85.586 $ | 14/29 | +48,28% | +10,53% | BASSA | 7,2 | 18,3 |
| -5,00% | 77.435 $ | 29/40 | +72,50% | +10,00% | 89.662 $ | 12/29 | +41,38% | +15,79% | BASSA | 7,2 | 19,8 |
| -5,00% | 77.435 $ | 29/40 | +72,50% | +15,00% | 93.737 $ | 10/29 | +34,48% | +21,05% | DEBOLE | 7,2 | 19,4 |
| -5,00% | 77.435 $ | 29/40 | +72,50% | +20,00% | 97.813 $ | 8/29 | +27,59% | +26,32% | DEBOLE | 7,2 | 20,8 |
| -8,00% | 74.990 $ | 24/40 | +60,00% | +5,00% | 85.586 $ | 10/24 | +41,67% | +14,13% | BASSA | 7,6 | 19,1 |
| -8,00% | 74.990 $ | 24/40 | +60,00% | +10,00% | 89.662 $ | 8/24 | +33,33% | +19,57% | DEBOLE | 7,6 | 20,4 |
| -8,00% | 74.990 $ | 24/40 | +60,00% | +15,00% | 93.737 $ | 7/24 | +29,17% | +25,00% | DEBOLE | 7,6 | 20,3 |
| -8,00% | 74.990 $ | 24/40 | +60,00% | +20,00% | 97.813 $ | 6/24 | +25,00% | +30,43% | DEBOLE | 7,6 | 21,0 |
| -10,00% | 73.360 $ | 19/40 | +47,50% | +5,00% | 85.586 $ | 5/19 | +26,32% | +16,67% | DEBOLE | 9,9 | 24,4 |
| -10,00% | 73.360 $ | 19/40 | +47,50% | +10,00% | 89.662 $ | 4/19 | +21,05% | +22,22% | DEBOLE | 9,9 | 24,8 |
| -10,00% | 73.360 $ | 19/40 | +47,50% | +15,00% | 93.737 $ | 3/19 | +15,79% | +27,78% | DEBOLE | 9,9 | 24,7 |
| -10,00% | 73.360 $ | 19/40 | +47,50% | +20,00% | 97.813 $ | 2/19 | +10,53% | +33,33% | DEBOLE | 9,9 | 28,0 |
| -15,00% | 69.284 $ | 14/40 | +35,00% | +5,00% | 85.586 $ | 2/14 | +14,29% | +23,53% | DEBOLE | 17,1 | 24,5 |
| -15,00% | 69.284 $ | 14/40 | +35,00% | +10,00% | 89.662 $ | 2/14 | +14,29% | +29,41% | DEBOLE | 17,1 | 24,5 |
| -15,00% | 69.284 $ | 14/40 | +35,00% | +15,00% | 93.737 $ | 1/14 | +7,14% | +35,29% | DEBOLE | 17,1 | 23,0 |
| -15,00% | 69.284 $ | 14/40 | +35,00% | +20,00% | 97.813 $ | 0/14 | 0,00% | +41,18% | DEBOLE | 17,1 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 85.586 $ | 27/40 | +67,50% | prezzo iniziale | 81.511 $ | 11/27 | +40,74% | -4,76% | BASSA | 9,0 | 8,3 |
| +5,00% | 85.586 $ | 27/40 | +67,50% | -5,00% | 77.435 $ | 8/27 | +29,63% | -9,52% | DEBOLE | 9,0 | 13,4 |
| +5,00% | 85.586 $ | 27/40 | +67,50% | -8,00% | 74.990 $ | 4/27 | +14,81% | -12,38% | DEBOLE | 9,0 | 13,0 |
| +5,00% | 85.586 $ | 27/40 | +67,50% | -10,00% | 73.360 $ | 4/27 | +14,81% | -14,29% | DEBOLE | 9,0 | 16,0 |
| +5,00% | 85.586 $ | 27/40 | +67,50% | -15,00% | 69.284 $ | 4/27 | +14,81% | -19,05% | DEBOLE | 9,0 | 24,2 |
| +10,00% | 89.662 $ | 24/40 | +60,00% | prezzo iniziale | 81.511 $ | 5/24 | +20,83% | -9,09% | DEBOLE | 14,8 | 12,2 |
| +10,00% | 89.662 $ | 24/40 | +60,00% | -5,00% | 77.435 $ | 3/24 | +12,50% | -13,64% | DEBOLE | 14,8 | 16,0 |
| +10,00% | 89.662 $ | 24/40 | +60,00% | -8,00% | 74.990 $ | 2/24 | +8,33% | -16,36% | DEBOLE | 14,8 | 16,0 |
| +10,00% | 89.662 $ | 24/40 | +60,00% | -10,00% | 73.360 $ | 2/24 | +8,33% | -18,18% | DEBOLE | 14,8 | 16,0 |
| +10,00% | 89.662 $ | 24/40 | +60,00% | -15,00% | 69.284 $ | 2/24 | +8,33% | -22,73% | DEBOLE | 14,8 | 24,5 |
| +15,00% | 93.737 $ | 18/40 | +45,00% | prezzo iniziale | 81.511 $ | 1/18 | +5,56% | -13,04% | DEBOLE | 18,7 | 14,0 |
| +15,00% | 93.737 $ | 18/40 | +45,00% | -5,00% | 77.435 $ | 1/18 | +5,56% | -17,39% | DEBOLE | 18,7 | 14,0 |
| +15,00% | 93.737 $ | 18/40 | +45,00% | -8,00% | 74.990 $ | 1/18 | +5,56% | -20,00% | DEBOLE | 18,7 | 20,0 |
| +15,00% | 93.737 $ | 18/40 | +45,00% | -10,00% | 73.360 $ | 1/18 | +5,56% | -21,74% | DEBOLE | 18,7 | 20,0 |
| +15,00% | 93.737 $ | 18/40 | +45,00% | -15,00% | 69.284 $ | 1/18 | +5,56% | -26,09% | DEBOLE | 18,7 | 22,0 |
| +20,00% | 97.813 $ | 15/40 | +37,50% | prezzo iniziale | 81.511 $ | 0/15 | 0,00% | -16,67% | DEBOLE | 20,8 | n/d |
| +20,00% | 97.813 $ | 15/40 | +37,50% | -5,00% | 77.435 $ | 0/15 | 0,00% | -20,83% | DEBOLE | 20,8 | n/d |
| +20,00% | 97.813 $ | 15/40 | +37,50% | -8,00% | 74.990 $ | 0/15 | 0,00% | -23,33% | DEBOLE | 20,8 | n/d |
| +20,00% | 97.813 $ | 15/40 | +37,50% | -10,00% | 73.360 $ | 0/15 | 0,00% | -25,00% | DEBOLE | 20,8 | n/d |
| +20,00% | 97.813 $ | 15/40 | +37,50% | -15,00% | 69.284 $ | 0/15 | 0,00% | -29,17% | DEBOLE | 20,8 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 29 prima sono scesi a -5,00%. Tra quei 29, 13 poi sono rimbalzati fino a +10,00%. Percentuale: +44,83% (13/29). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- SOL: su 40 casi simili, 26 prima sono saliti a +10,00%. Tra quei 26, 2 poi sono scaricati a -5,00%. Percentuale: +7,69% (2/26). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 98,89 $ | 29/40 | +72,50% | +5,00% | 109,29 $ | 15/29 | +51,72% | +10,53% | MEDIA | 7,3 | 18,4 |
| -5,00% | 98,89 $ | 29/40 | +72,50% | +10,00% | 114,50 $ | 13/29 | +44,83% | +15,79% | BASSA | 7,3 | 20,5 |
| -5,00% | 98,89 $ | 29/40 | +72,50% | +15,00% | 119,70 $ | 8/29 | +27,59% | +21,05% | DEBOLE | 7,3 | 20,8 |
| -5,00% | 98,89 $ | 29/40 | +72,50% | +20,00% | 124,91 $ | 4/29 | +13,79% | +26,32% | DEBOLE | 7,3 | 22,5 |
| -8,00% | 95,76 $ | 24/40 | +60,00% | +5,00% | 109,29 $ | 10/24 | +41,67% | +14,13% | BASSA | 8,6 | 20,6 |
| -8,00% | 95,76 $ | 24/40 | +60,00% | +10,00% | 114,50 $ | 8/24 | +33,33% | +19,57% | DEBOLE | 8,6 | 21,4 |
| -8,00% | 95,76 $ | 24/40 | +60,00% | +15,00% | 119,70 $ | 6/24 | +25,00% | +25,00% | DEBOLE | 8,6 | 24,8 |
| -8,00% | 95,76 $ | 24/40 | +60,00% | +20,00% | 124,91 $ | 3/24 | +12,50% | +30,43% | DEBOLE | 8,6 | 28,7 |
| -10,00% | 93,68 $ | 21/40 | +52,50% | +5,00% | 109,29 $ | 7/21 | +33,33% | +16,67% | DEBOLE | 9,4 | 25,1 |
| -10,00% | 93,68 $ | 21/40 | +52,50% | +10,00% | 114,50 $ | 6/21 | +28,57% | +22,22% | DEBOLE | 9,4 | 25,3 |
| -10,00% | 93,68 $ | 21/40 | +52,50% | +15,00% | 119,70 $ | 5/21 | +23,81% | +27,78% | DEBOLE | 9,4 | 25,6 |
| -10,00% | 93,68 $ | 21/40 | +52,50% | +20,00% | 124,91 $ | 2/21 | +9,52% | +33,33% | DEBOLE | 9,4 | 30,0 |
| -15,00% | 88,48 $ | 15/40 | +37,50% | +5,00% | 109,29 $ | 3/15 | +20,00% | +23,53% | DEBOLE | 13,4 | 26,0 |
| -15,00% | 88,48 $ | 15/40 | +37,50% | +10,00% | 114,50 $ | 3/15 | +20,00% | +29,41% | DEBOLE | 13,4 | 26,0 |
| -15,00% | 88,48 $ | 15/40 | +37,50% | +15,00% | 119,70 $ | 2/15 | +13,33% | +35,29% | DEBOLE | 13,4 | 26,0 |
| -15,00% | 88,48 $ | 15/40 | +37,50% | +20,00% | 124,91 $ | 0/15 | 0,00% | +41,18% | DEBOLE | 13,4 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 109,29 $ | 30/40 | +75,00% | prezzo iniziale | 104,09 $ | 16/30 | +53,33% | -4,76% | MEDIA | 7,8 | 10,7 |
| +5,00% | 109,29 $ | 30/40 | +75,00% | -5,00% | 98,89 $ | 9/30 | +30,00% | -9,52% | DEBOLE | 7,8 | 11,7 |
| +5,00% | 109,29 $ | 30/40 | +75,00% | -8,00% | 95,76 $ | 7/30 | +23,33% | -12,38% | DEBOLE | 7,8 | 12,9 |
| +5,00% | 109,29 $ | 30/40 | +75,00% | -10,00% | 93,68 $ | 7/30 | +23,33% | -14,29% | DEBOLE | 7,8 | 16,0 |
| +5,00% | 109,29 $ | 30/40 | +75,00% | -15,00% | 88,48 $ | 5/30 | +16,67% | -19,05% | DEBOLE | 7,8 | 22,6 |
| +10,00% | 114,50 $ | 26/40 | +65,00% | prezzo iniziale | 104,09 $ | 7/26 | +26,92% | -9,09% | DEBOLE | 15,4 | 16,4 |
| +10,00% | 114,50 $ | 26/40 | +65,00% | -5,00% | 98,89 $ | 2/26 | +7,69% | -13,64% | DEBOLE | 15,4 | 12,0 |
| +10,00% | 114,50 $ | 26/40 | +65,00% | -8,00% | 95,76 $ | 2/26 | +7,69% | -16,36% | DEBOLE | 15,4 | 15,0 |
| +10,00% | 114,50 $ | 26/40 | +65,00% | -10,00% | 93,68 $ | 2/26 | +7,69% | -18,18% | DEBOLE | 15,4 | 15,0 |
| +10,00% | 114,50 $ | 26/40 | +65,00% | -15,00% | 88,48 $ | 2/26 | +7,69% | -22,73% | DEBOLE | 15,4 | 24,0 |
| +15,00% | 119,70 $ | 18/40 | +45,00% | prezzo iniziale | 104,09 $ | 3/18 | +16,67% | -13,04% | DEBOLE | 17,1 | 19,0 |
| +15,00% | 119,70 $ | 18/40 | +45,00% | -5,00% | 98,89 $ | 1/18 | +5,56% | -17,39% | DEBOLE | 17,1 | 14,0 |
| +15,00% | 119,70 $ | 18/40 | +45,00% | -8,00% | 95,76 $ | 1/18 | +5,56% | -20,00% | DEBOLE | 17,1 | 20,0 |
| +15,00% | 119,70 $ | 18/40 | +45,00% | -10,00% | 93,68 $ | 1/18 | +5,56% | -21,74% | DEBOLE | 17,1 | 20,0 |
| +15,00% | 119,70 $ | 18/40 | +45,00% | -15,00% | 88,48 $ | 1/18 | +5,56% | -26,09% | DEBOLE | 17,1 | 22,0 |
| +20,00% | 124,91 $ | 12/40 | +30,00% | prezzo iniziale | 104,09 $ | 0/12 | 0,00% | -16,67% | DEBOLE | 19,5 | n/d |
| +20,00% | 124,91 $ | 12/40 | +30,00% | -5,00% | 98,89 $ | 0/12 | 0,00% | -20,83% | DEBOLE | 19,5 | n/d |
| +20,00% | 124,91 $ | 12/40 | +30,00% | -8,00% | 95,76 $ | 0/12 | 0,00% | -23,33% | DEBOLE | 19,5 | n/d |
| +20,00% | 124,91 $ | 12/40 | +30,00% | -10,00% | 93,68 $ | 0/12 | 0,00% | -25,00% | DEBOLE | 19,5 | n/d |
| +20,00% | 124,91 $ | 12/40 | +30,00% | -15,00% | 88,48 $ | 0/12 | 0,00% | -29,17% | DEBOLE | 19,5 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 25 prima sono scesi a -5,00%. Tra quei 25, 14 poi sono rimbalzati fino a +10,00%. Percentuale: +56,00% (14/25). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.
- DOGE: su 40 casi simili, 30 prima sono saliti a +10,00%. Tra quei 30, 2 poi sono scaricati a -5,00%. Percentuale: +6,67% (2/30). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,07561 $ | 25/40 | +62,50% | +5,00% | 0,08357 $ | 14/25 | +56,00% | +10,53% | MEDIA | 6,1 | 19,9 |
| -5,00% | 0,07561 $ | 25/40 | +62,50% | +10,00% | 0,08755 $ | 14/25 | +56,00% | +15,79% | MEDIA | 6,1 | 22,3 |
| -5,00% | 0,07561 $ | 25/40 | +62,50% | +15,00% | 0,09153 $ | 10/25 | +40,00% | +21,05% | BASSA | 6,1 | 23,3 |
| -5,00% | 0,07561 $ | 25/40 | +62,50% | +20,00% | 0,09551 $ | 4/25 | +16,00% | +26,32% | DEBOLE | 6,1 | 27,5 |
| -8,00% | 0,07322 $ | 19/40 | +47,50% | +5,00% | 0,08357 $ | 8/19 | +42,11% | +14,13% | BASSA | 7,5 | 22,5 |
| -8,00% | 0,07322 $ | 19/40 | +47,50% | +10,00% | 0,08755 $ | 8/19 | +42,11% | +19,57% | BASSA | 7,5 | 23,0 |
| -8,00% | 0,07322 $ | 19/40 | +47,50% | +15,00% | 0,09153 $ | 7/19 | +36,84% | +25,00% | BASSA | 7,5 | 25,0 |
| -8,00% | 0,07322 $ | 19/40 | +47,50% | +20,00% | 0,09551 $ | 4/19 | +21,05% | +30,43% | DEBOLE | 7,5 | 27,5 |
| -10,00% | 0,07163 $ | 15/40 | +37,50% | +5,00% | 0,08357 $ | 4/15 | +26,67% | +16,67% | DEBOLE | 6,5 | 24,0 |
| -10,00% | 0,07163 $ | 15/40 | +37,50% | +10,00% | 0,08755 $ | 4/15 | +26,67% | +22,22% | DEBOLE | 6,5 | 24,2 |
| -10,00% | 0,07163 $ | 15/40 | +37,50% | +15,00% | 0,09153 $ | 4/15 | +26,67% | +27,78% | DEBOLE | 6,5 | 24,8 |
| -10,00% | 0,07163 $ | 15/40 | +37,50% | +20,00% | 0,09551 $ | 2/15 | +13,33% | +33,33% | DEBOLE | 6,5 | 30,0 |
| -15,00% | 0,06765 $ | 9/40 | +22,50% | +5,00% | 0,08357 $ | 1/9 | +11,11% | +23,53% | DEBOLE | 8,3 | 23,0 |
| -15,00% | 0,06765 $ | 9/40 | +22,50% | +10,00% | 0,08755 $ | 1/9 | +11,11% | +29,41% | DEBOLE | 8,3 | 23,0 |
| -15,00% | 0,06765 $ | 9/40 | +22,50% | +15,00% | 0,09153 $ | 1/9 | +11,11% | +35,29% | DEBOLE | 8,3 | 23,0 |
| -15,00% | 0,06765 $ | 9/40 | +22,50% | +20,00% | 0,09551 $ | 0/9 | 0,00% | +41,18% | DEBOLE | 8,3 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,08357 $ | 31/40 | +77,50% | prezzo iniziale | 0,07959 $ | 15/31 | +48,39% | -4,76% | BASSA | 8,8 | 13,3 |
| +5,00% | 0,08357 $ | 31/40 | +77,50% | -5,00% | 0,07561 $ | 6/31 | +19,35% | -9,52% | DEBOLE | 8,8 | 13,5 |
| +5,00% | 0,08357 $ | 31/40 | +77,50% | -8,00% | 0,07322 $ | 4/31 | +12,90% | -12,38% | DEBOLE | 8,8 | 16,5 |
| +5,00% | 0,08357 $ | 31/40 | +77,50% | -10,00% | 0,07163 $ | 3/31 | +9,68% | -14,29% | DEBOLE | 8,8 | 13,7 |
| +5,00% | 0,08357 $ | 31/40 | +77,50% | -15,00% | 0,06765 $ | 2/31 | +6,45% | -19,05% | DEBOLE | 8,8 | 23,5 |
| +10,00% | 0,08755 $ | 30/40 | +75,00% | prezzo iniziale | 0,07959 $ | 8/30 | +26,67% | -9,09% | DEBOLE | 15,7 | 19,4 |
| +10,00% | 0,08755 $ | 30/40 | +75,00% | -5,00% | 0,07561 $ | 2/30 | +6,67% | -13,64% | DEBOLE | 15,7 | 8,5 |
| +10,00% | 0,08755 $ | 30/40 | +75,00% | -8,00% | 0,07322 $ | 2/30 | +6,67% | -16,36% | DEBOLE | 15,7 | 10,5 |
| +10,00% | 0,08755 $ | 30/40 | +75,00% | -10,00% | 0,07163 $ | 2/30 | +6,67% | -18,18% | DEBOLE | 15,7 | 10,5 |
| +10,00% | 0,08755 $ | 30/40 | +75,00% | -15,00% | 0,06765 $ | 2/30 | +6,67% | -22,73% | DEBOLE | 15,7 | 23,5 |
| +15,00% | 0,09153 $ | 21/40 | +52,50% | prezzo iniziale | 0,07959 $ | 3/21 | +14,29% | -13,04% | DEBOLE | 17,1 | 24,3 |
| +15,00% | 0,09153 $ | 21/40 | +52,50% | -5,00% | 0,07561 $ | 0/21 | 0,00% | -17,39% | DEBOLE | 17,1 | n/d |
| +15,00% | 0,09153 $ | 21/40 | +52,50% | -8,00% | 0,07322 $ | 0/21 | 0,00% | -20,00% | DEBOLE | 17,1 | n/d |
| +15,00% | 0,09153 $ | 21/40 | +52,50% | -10,00% | 0,07163 $ | 0/21 | 0,00% | -21,74% | DEBOLE | 17,1 | n/d |
| +15,00% | 0,09153 $ | 21/40 | +52,50% | -15,00% | 0,06765 $ | 0/21 | 0,00% | -26,09% | DEBOLE | 17,1 | n/d |
| +20,00% | 0,09551 $ | 14/40 | +35,00% | prezzo iniziale | 0,07959 $ | 0/14 | 0,00% | -16,67% | DEBOLE | 17,2 | n/d |
| +20,00% | 0,09551 $ | 14/40 | +35,00% | -5,00% | 0,07561 $ | 0/14 | 0,00% | -20,83% | DEBOLE | 17,2 | n/d |
| +20,00% | 0,09551 $ | 14/40 | +35,00% | -8,00% | 0,07322 $ | 0/14 | 0,00% | -23,33% | DEBOLE | 17,2 | n/d |
| +20,00% | 0,09551 $ | 14/40 | +35,00% | -10,00% | 0,07163 $ | 0/14 | 0,00% | -25,00% | DEBOLE | 17,2 | n/d |
| +20,00% | 0,09551 $ | 14/40 | +35,00% | -15,00% | 0,06765 $ | 0/14 | 0,00% | -29,17% | DEBOLE | 17,2 | n/d |

---
