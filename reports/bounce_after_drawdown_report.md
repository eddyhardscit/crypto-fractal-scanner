# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-10-22 07:32:50 CEST**  
UTC: **2026-10-22 05:32:50 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 78.695 $ | 91.121 $ | +37,93% | +15,79% | rimbalzo debole | 91.121 $ | 78.695 $ | +15,38% | -13,64% | spike storicamente più resistente |
| SOL | 99,93 $ | 115,71 $ | +44,44% | +15,79% | rimbalzo debole | 115,71 $ | 99,93 $ | +7,69% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07608 $ | 0,08809 $ | +50,00% | +15,79% | rimbalzo possibile | 0,08809 $ | 0,07608 $ | +6,90% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 29 prima sono scesi a -5,00%. Tra quei 29, 11 poi sono rimbalzati fino a +10,00%. Percentuale: +37,93% (11/29). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 26 prima sono saliti a +10,00%. Tra quei 26, 4 poi sono scaricati a -5,00%. Percentuale: +15,38% (4/26). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 78.695 $ | 29/40 | +72,50% | +5,00% | 86.979 $ | 13/29 | +44,83% | +10,53% | BASSA | 8,4 | 18,4 |
| -5,00% | 78.695 $ | 29/40 | +72,50% | +10,00% | 91.121 $ | 11/29 | +37,93% | +15,79% | BASSA | 8,4 | 21,6 |
| -5,00% | 78.695 $ | 29/40 | +72,50% | +15,00% | 95.263 $ | 8/29 | +27,59% | +21,05% | DEBOLE | 8,4 | 22,5 |
| -5,00% | 78.695 $ | 29/40 | +72,50% | +20,00% | 99.405 $ | 7/29 | +24,14% | +26,32% | DEBOLE | 8,4 | 22,7 |
| -8,00% | 76.210 $ | 24/40 | +60,00% | +5,00% | 86.979 $ | 9/24 | +37,50% | +14,13% | BASSA | 9,3 | 19,9 |
| -8,00% | 76.210 $ | 24/40 | +60,00% | +10,00% | 91.121 $ | 7/24 | +29,17% | +19,57% | DEBOLE | 9,3 | 20,9 |
| -8,00% | 76.210 $ | 24/40 | +60,00% | +15,00% | 95.263 $ | 5/24 | +20,83% | +25,00% | DEBOLE | 9,3 | 22,2 |
| -8,00% | 76.210 $ | 24/40 | +60,00% | +20,00% | 99.405 $ | 5/24 | +20,83% | +30,43% | DEBOLE | 9,3 | 23,8 |
| -10,00% | 74.554 $ | 20/40 | +50,00% | +5,00% | 86.979 $ | 5/20 | +25,00% | +16,67% | DEBOLE | 11,8 | 27,0 |
| -10,00% | 74.554 $ | 20/40 | +50,00% | +10,00% | 91.121 $ | 4/20 | +20,00% | +22,22% | DEBOLE | 11,8 | 27,8 |
| -10,00% | 74.554 $ | 20/40 | +50,00% | +15,00% | 95.263 $ | 2/20 | +10,00% | +27,78% | DEBOLE | 11,8 | 29,5 |
| -10,00% | 74.554 $ | 20/40 | +50,00% | +20,00% | 99.405 $ | 2/20 | +10,00% | +33,33% | DEBOLE | 11,8 | 30,0 |
| -15,00% | 70.412 $ | 14/40 | +35,00% | +5,00% | 86.979 $ | 2/14 | +14,29% | +23,53% | DEBOLE | 18,7 | 27,0 |
| -15,00% | 70.412 $ | 14/40 | +35,00% | +10,00% | 91.121 $ | 2/14 | +14,29% | +29,41% | DEBOLE | 18,7 | 27,0 |
| -15,00% | 70.412 $ | 14/40 | +35,00% | +15,00% | 95.263 $ | 0/14 | 0,00% | +35,29% | DEBOLE | 18,7 | n/d |
| -15,00% | 70.412 $ | 14/40 | +35,00% | +20,00% | 99.405 $ | 0/14 | 0,00% | +41,18% | DEBOLE | 18,7 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 86.979 $ | 28/40 | +70,00% | prezzo iniziale | 82.837 $ | 17/28 | +60,71% | -4,76% | MEDIA | 7,1 | 11,5 |
| +5,00% | 86.979 $ | 28/40 | +70,00% | -5,00% | 78.695 $ | 10/28 | +35,71% | -9,52% | BASSA | 7,1 | 15,6 |
| +5,00% | 86.979 $ | 28/40 | +70,00% | -8,00% | 76.210 $ | 6/28 | +21,43% | -12,38% | DEBOLE | 7,1 | 16,8 |
| +5,00% | 86.979 $ | 28/40 | +70,00% | -10,00% | 74.554 $ | 6/28 | +21,43% | -14,29% | DEBOLE | 7,1 | 19,0 |
| +5,00% | 86.979 $ | 28/40 | +70,00% | -15,00% | 70.412 $ | 4/28 | +14,29% | -19,05% | DEBOLE | 7,1 | 24,2 |
| +10,00% | 91.121 $ | 26/40 | +65,00% | prezzo iniziale | 82.837 $ | 10/26 | +38,46% | -9,09% | BASSA | 14,0 | 14,6 |
| +10,00% | 91.121 $ | 26/40 | +65,00% | -5,00% | 78.695 $ | 4/26 | +15,38% | -13,64% | DEBOLE | 14,0 | 19,5 |
| +10,00% | 91.121 $ | 26/40 | +65,00% | -8,00% | 76.210 $ | 3/26 | +11,54% | -16,36% | DEBOLE | 14,0 | 20,3 |
| +10,00% | 91.121 $ | 26/40 | +65,00% | -10,00% | 74.554 $ | 3/26 | +11,54% | -18,18% | DEBOLE | 14,0 | 20,7 |
| +10,00% | 91.121 $ | 26/40 | +65,00% | -15,00% | 70.412 $ | 2/26 | +7,69% | -22,73% | DEBOLE | 14,0 | 24,5 |
| +15,00% | 95.263 $ | 19/40 | +47,50% | prezzo iniziale | 82.837 $ | 3/19 | +15,79% | -13,04% | DEBOLE | 18,6 | 15,0 |
| +15,00% | 95.263 $ | 19/40 | +47,50% | -5,00% | 78.695 $ | 2/19 | +10,53% | -17,39% | DEBOLE | 18,6 | 21,5 |
| +15,00% | 95.263 $ | 19/40 | +47,50% | -8,00% | 76.210 $ | 2/19 | +10,53% | -20,00% | DEBOLE | 18,6 | 24,5 |
| +15,00% | 95.263 $ | 19/40 | +47,50% | -10,00% | 74.554 $ | 2/19 | +10,53% | -21,74% | DEBOLE | 18,6 | 25,0 |
| +15,00% | 95.263 $ | 19/40 | +47,50% | -15,00% | 70.412 $ | 1/19 | +5,26% | -26,09% | DEBOLE | 18,6 | 22,0 |
| +20,00% | 99.405 $ | 15/40 | +37,50% | prezzo iniziale | 82.837 $ | 0/15 | 0,00% | -16,67% | DEBOLE | 22,3 | n/d |
| +20,00% | 99.405 $ | 15/40 | +37,50% | -5,00% | 78.695 $ | 0/15 | 0,00% | -20,83% | DEBOLE | 22,3 | n/d |
| +20,00% | 99.405 $ | 15/40 | +37,50% | -8,00% | 76.210 $ | 0/15 | 0,00% | -23,33% | DEBOLE | 22,3 | n/d |
| +20,00% | 99.405 $ | 15/40 | +37,50% | -10,00% | 74.554 $ | 0/15 | 0,00% | -25,00% | DEBOLE | 22,3 | n/d |
| +20,00% | 99.405 $ | 15/40 | +37,50% | -15,00% | 70.412 $ | 0/15 | 0,00% | -29,17% | DEBOLE | 22,3 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 27 prima sono scesi a -5,00%. Tra quei 27, 12 poi sono rimbalzati fino a +10,00%. Percentuale: +44,44% (12/27). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- SOL: su 40 casi simili, 26 prima sono saliti a +10,00%. Tra quei 26, 2 poi sono scaricati a -5,00%. Percentuale: +7,69% (2/26). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 99,93 $ | 27/40 | +67,50% | +5,00% | 110,45 $ | 14/27 | +51,85% | +10,53% | MEDIA | 7,8 | 19,0 |
| -5,00% | 99,93 $ | 27/40 | +67,50% | +10,00% | 115,71 $ | 12/27 | +44,44% | +15,79% | BASSA | 7,8 | 21,9 |
| -5,00% | 99,93 $ | 27/40 | +67,50% | +15,00% | 120,97 $ | 8/27 | +29,63% | +21,05% | DEBOLE | 7,8 | 22,1 |
| -5,00% | 99,93 $ | 27/40 | +67,50% | +20,00% | 126,23 $ | 5/27 | +18,52% | +26,32% | DEBOLE | 7,8 | 23,6 |
| -8,00% | 96,77 $ | 22/40 | +55,00% | +5,00% | 110,45 $ | 9/22 | +40,91% | +14,13% | BASSA | 8,4 | 20,3 |
| -8,00% | 96,77 $ | 22/40 | +55,00% | +10,00% | 115,71 $ | 7/22 | +31,82% | +19,57% | DEBOLE | 8,4 | 21,3 |
| -8,00% | 96,77 $ | 22/40 | +55,00% | +15,00% | 120,97 $ | 6/22 | +27,27% | +25,00% | DEBOLE | 8,4 | 23,7 |
| -8,00% | 96,77 $ | 22/40 | +55,00% | +20,00% | 126,23 $ | 4/22 | +18,18% | +30,43% | DEBOLE | 8,4 | 24,0 |
| -10,00% | 94,67 $ | 18/40 | +45,00% | +5,00% | 110,45 $ | 6/18 | +33,33% | +16,67% | DEBOLE | 9,6 | 26,5 |
| -10,00% | 94,67 $ | 18/40 | +45,00% | +10,00% | 115,71 $ | 5/18 | +27,78% | +22,22% | DEBOLE | 9,6 | 27,0 |
| -10,00% | 94,67 $ | 18/40 | +45,00% | +15,00% | 120,97 $ | 4/18 | +22,22% | +27,78% | DEBOLE | 9,6 | 27,8 |
| -10,00% | 94,67 $ | 18/40 | +45,00% | +20,00% | 126,23 $ | 2/18 | +11,11% | +33,33% | DEBOLE | 9,6 | 30,0 |
| -15,00% | 89,41 $ | 14/40 | +35,00% | +5,00% | 110,45 $ | 3/14 | +21,43% | +23,53% | DEBOLE | 13,6 | 26,0 |
| -15,00% | 89,41 $ | 14/40 | +35,00% | +10,00% | 115,71 $ | 3/14 | +21,43% | +29,41% | DEBOLE | 13,6 | 26,0 |
| -15,00% | 89,41 $ | 14/40 | +35,00% | +15,00% | 120,97 $ | 2/14 | +14,29% | +35,29% | DEBOLE | 13,6 | 26,0 |
| -15,00% | 89,41 $ | 14/40 | +35,00% | +20,00% | 126,23 $ | 0/14 | 0,00% | +41,18% | DEBOLE | 13,6 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 110,45 $ | 31/40 | +77,50% | prezzo iniziale | 105,19 $ | 17/31 | +54,84% | -4,76% | MEDIA | 7,1 | 9,4 |
| +5,00% | 110,45 $ | 31/40 | +77,50% | -5,00% | 99,93 $ | 10/31 | +32,26% | -9,52% | DEBOLE | 7,1 | 11,6 |
| +5,00% | 110,45 $ | 31/40 | +77,50% | -8,00% | 96,77 $ | 7/31 | +22,58% | -12,38% | DEBOLE | 7,1 | 12,9 |
| +5,00% | 110,45 $ | 31/40 | +77,50% | -10,00% | 94,67 $ | 7/31 | +22,58% | -14,29% | DEBOLE | 7,1 | 16,0 |
| +5,00% | 110,45 $ | 31/40 | +77,50% | -15,00% | 89,41 $ | 5/31 | +16,13% | -19,05% | DEBOLE | 7,1 | 22,6 |
| +10,00% | 115,71 $ | 26/40 | +65,00% | prezzo iniziale | 105,19 $ | 6/26 | +23,08% | -9,09% | DEBOLE | 16,4 | 15,0 |
| +10,00% | 115,71 $ | 26/40 | +65,00% | -5,00% | 99,93 $ | 2/26 | +7,69% | -13,64% | DEBOLE | 16,4 | 12,0 |
| +10,00% | 115,71 $ | 26/40 | +65,00% | -8,00% | 96,77 $ | 2/26 | +7,69% | -16,36% | DEBOLE | 16,4 | 15,0 |
| +10,00% | 115,71 $ | 26/40 | +65,00% | -10,00% | 94,67 $ | 2/26 | +7,69% | -18,18% | DEBOLE | 16,4 | 15,0 |
| +10,00% | 115,71 $ | 26/40 | +65,00% | -15,00% | 89,41 $ | 2/26 | +7,69% | -22,73% | DEBOLE | 16,4 | 24,0 |
| +15,00% | 120,97 $ | 18/40 | +45,00% | prezzo iniziale | 105,19 $ | 2/18 | +11,11% | -13,04% | DEBOLE | 18,2 | 16,0 |
| +15,00% | 120,97 $ | 18/40 | +45,00% | -5,00% | 99,93 $ | 1/18 | +5,56% | -17,39% | DEBOLE | 18,2 | 14,0 |
| +15,00% | 120,97 $ | 18/40 | +45,00% | -8,00% | 96,77 $ | 1/18 | +5,56% | -20,00% | DEBOLE | 18,2 | 20,0 |
| +15,00% | 120,97 $ | 18/40 | +45,00% | -10,00% | 94,67 $ | 1/18 | +5,56% | -21,74% | DEBOLE | 18,2 | 20,0 |
| +15,00% | 120,97 $ | 18/40 | +45,00% | -15,00% | 89,41 $ | 1/18 | +5,56% | -26,09% | DEBOLE | 18,2 | 22,0 |
| +20,00% | 126,23 $ | 14/40 | +35,00% | prezzo iniziale | 105,19 $ | 0/14 | 0,00% | -16,67% | DEBOLE | 20,9 | n/d |
| +20,00% | 126,23 $ | 14/40 | +35,00% | -5,00% | 99,93 $ | 0/14 | 0,00% | -20,83% | DEBOLE | 20,9 | n/d |
| +20,00% | 126,23 $ | 14/40 | +35,00% | -8,00% | 96,77 $ | 0/14 | 0,00% | -23,33% | DEBOLE | 20,9 | n/d |
| +20,00% | 126,23 $ | 14/40 | +35,00% | -10,00% | 94,67 $ | 0/14 | 0,00% | -25,00% | DEBOLE | 20,9 | n/d |
| +20,00% | 126,23 $ | 14/40 | +35,00% | -15,00% | 89,41 $ | 0/14 | 0,00% | -29,17% | DEBOLE | 20,9 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 24 prima sono scesi a -5,00%. Tra quei 24, 12 poi sono rimbalzati fino a +10,00%. Percentuale: +50,00% (12/24). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.
- DOGE: su 40 casi simili, 29 prima sono saliti a +10,00%. Tra quei 29, 2 poi sono scaricati a -5,00%. Percentuale: +6,90% (2/29). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,07608 $ | 24/40 | +60,00% | +5,00% | 0,08408 $ | 15/24 | +62,50% | +10,53% | MEDIA | 7,0 | 19,9 |
| -5,00% | 0,07608 $ | 24/40 | +60,00% | +10,00% | 0,08809 $ | 12/24 | +50,00% | +15,79% | MEDIA | 7,0 | 23,9 |
| -5,00% | 0,07608 $ | 24/40 | +60,00% | +15,00% | 0,09209 $ | 8/24 | +33,33% | +21,05% | DEBOLE | 7,0 | 24,4 |
| -5,00% | 0,07608 $ | 24/40 | +60,00% | +20,00% | 0,09610 $ | 5/24 | +20,83% | +26,32% | DEBOLE | 7,0 | 26,4 |
| -8,00% | 0,07367 $ | 17/40 | +42,50% | +5,00% | 0,08408 $ | 8/17 | +47,06% | +14,13% | BASSA | 7,5 | 19,4 |
| -8,00% | 0,07367 $ | 17/40 | +42,50% | +10,00% | 0,08809 $ | 6/17 | +35,29% | +19,57% | BASSA | 7,5 | 23,7 |
| -8,00% | 0,07367 $ | 17/40 | +42,50% | +15,00% | 0,09209 $ | 5/17 | +29,41% | +25,00% | DEBOLE | 7,5 | 26,0 |
| -8,00% | 0,07367 $ | 17/40 | +42,50% | +20,00% | 0,09610 $ | 4/17 | +23,53% | +30,43% | DEBOLE | 7,5 | 27,5 |
| -10,00% | 0,07207 $ | 13/40 | +32,50% | +5,00% | 0,08408 $ | 4/13 | +30,77% | +16,67% | DEBOLE | 8,1 | 20,8 |
| -10,00% | 0,07207 $ | 13/40 | +32,50% | +10,00% | 0,08809 $ | 3/13 | +23,08% | +22,22% | DEBOLE | 8,1 | 26,7 |
| -10,00% | 0,07207 $ | 13/40 | +32,50% | +15,00% | 0,09209 $ | 3/13 | +23,08% | +27,78% | DEBOLE | 8,1 | 27,3 |
| -10,00% | 0,07207 $ | 13/40 | +32,50% | +20,00% | 0,09610 $ | 2/13 | +15,38% | +33,33% | DEBOLE | 8,1 | 30,0 |
| -15,00% | 0,06807 $ | 9/40 | +22,50% | +5,00% | 0,08408 $ | 1/9 | +11,11% | +23,53% | DEBOLE | 11,0 | 23,0 |
| -15,00% | 0,06807 $ | 9/40 | +22,50% | +10,00% | 0,08809 $ | 1/9 | +11,11% | +29,41% | DEBOLE | 11,0 | 23,0 |
| -15,00% | 0,06807 $ | 9/40 | +22,50% | +15,00% | 0,09209 $ | 1/9 | +11,11% | +35,29% | DEBOLE | 11,0 | 23,0 |
| -15,00% | 0,06807 $ | 9/40 | +22,50% | +20,00% | 0,09610 $ | 0/9 | 0,00% | +41,18% | DEBOLE | 11,0 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,08408 $ | 33/40 | +82,50% | prezzo iniziale | 0,08008 $ | 18/33 | +54,55% | -4,76% | MEDIA | 7,2 | 8,7 |
| +5,00% | 0,08408 $ | 33/40 | +82,50% | -5,00% | 0,07608 $ | 10/33 | +30,30% | -9,52% | DEBOLE | 7,2 | 11,5 |
| +5,00% | 0,08408 $ | 33/40 | +82,50% | -8,00% | 0,07367 $ | 6/33 | +18,18% | -12,38% | DEBOLE | 7,2 | 13,0 |
| +5,00% | 0,08408 $ | 33/40 | +82,50% | -10,00% | 0,07207 $ | 5/33 | +15,15% | -14,29% | DEBOLE | 7,2 | 13,6 |
| +5,00% | 0,08408 $ | 33/40 | +82,50% | -15,00% | 0,06807 $ | 4/33 | +12,12% | -19,05% | DEBOLE | 7,2 | 18,8 |
| +10,00% | 0,08809 $ | 29/40 | +72,50% | prezzo iniziale | 0,08008 $ | 6/29 | +20,69% | -9,09% | DEBOLE | 16,3 | 13,0 |
| +10,00% | 0,08809 $ | 29/40 | +72,50% | -5,00% | 0,07608 $ | 2/29 | +6,90% | -13,64% | DEBOLE | 16,3 | 8,5 |
| +10,00% | 0,08809 $ | 29/40 | +72,50% | -8,00% | 0,07367 $ | 2/29 | +6,90% | -16,36% | DEBOLE | 16,3 | 10,5 |
| +10,00% | 0,08809 $ | 29/40 | +72,50% | -10,00% | 0,07207 $ | 2/29 | +6,90% | -18,18% | DEBOLE | 16,3 | 10,5 |
| +10,00% | 0,08809 $ | 29/40 | +72,50% | -15,00% | 0,06807 $ | 2/29 | +6,90% | -22,73% | DEBOLE | 16,3 | 23,5 |
| +15,00% | 0,09209 $ | 20/40 | +50,00% | prezzo iniziale | 0,08008 $ | 1/20 | +5,00% | -13,04% | DEBOLE | 18,9 | 14,0 |
| +15,00% | 0,09209 $ | 20/40 | +50,00% | -5,00% | 0,07608 $ | 0/20 | 0,00% | -17,39% | DEBOLE | 18,9 | n/d |
| +15,00% | 0,09209 $ | 20/40 | +50,00% | -8,00% | 0,07367 $ | 0/20 | 0,00% | -20,00% | DEBOLE | 18,9 | n/d |
| +15,00% | 0,09209 $ | 20/40 | +50,00% | -10,00% | 0,07207 $ | 0/20 | 0,00% | -21,74% | DEBOLE | 18,9 | n/d |
| +15,00% | 0,09209 $ | 20/40 | +50,00% | -15,00% | 0,06807 $ | 0/20 | 0,00% | -26,09% | DEBOLE | 18,9 | n/d |
| +20,00% | 0,09610 $ | 16/40 | +40,00% | prezzo iniziale | 0,08008 $ | 0/16 | 0,00% | -16,67% | DEBOLE | 20,4 | n/d |
| +20,00% | 0,09610 $ | 16/40 | +40,00% | -5,00% | 0,07608 $ | 0/16 | 0,00% | -20,83% | DEBOLE | 20,4 | n/d |
| +20,00% | 0,09610 $ | 16/40 | +40,00% | -8,00% | 0,07367 $ | 0/16 | 0,00% | -23,33% | DEBOLE | 20,4 | n/d |
| +20,00% | 0,09610 $ | 16/40 | +40,00% | -10,00% | 0,07207 $ | 0/16 | 0,00% | -25,00% | DEBOLE | 20,4 | n/d |
| +20,00% | 0,09610 $ | 16/40 | +40,00% | -15,00% | 0,06807 $ | 0/16 | 0,00% | -29,17% | DEBOLE | 20,4 | n/d |

---
