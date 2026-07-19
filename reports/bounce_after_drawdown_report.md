# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-19 07:13:50 CEST**  
UTC: **2026-07-19 05:13:50 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 61.487 $ | 71.196 $ | +45,45% | +15,79% | rimbalzo debole | 71.196 $ | 61.487 $ | +29,17% | -13,64% | spike storicamente più resistente |
| SOL | 72,20 $ | 83,60 $ | +30,30% | +15,79% | rimbalzo poco frequente | 83,60 $ | 72,20 $ | +23,53% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06880 $ | 0,07966 $ | +17,65% | +15,79% | rimbalzo poco frequente | 0,07966 $ | 0,06880 $ | +41,18% | -13,64% | scarico possibile |

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

- BTC: su 40 casi simili, 33 prima sono scesi a -5,00%. Tra quei 33, 15 poi sono rimbalzati fino a +10,00%. Percentuale: +45,45% (15/33). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 24 prima sono saliti a +10,00%. Tra quei 24, 7 poi sono scaricati a -5,00%. Percentuale: +29,17% (7/24). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 61.487 $ | 33/40 | +82,50% | +5,00% | 67.960 $ | 18/33 | +54,55% | +10,53% | MEDIA | 9,0 | 21,9 |
| -5,00% | 61.487 $ | 33/40 | +82,50% | +10,00% | 71.196 $ | 15/33 | +45,45% | +15,79% | BASSA | 9,0 | 23,9 |
| -5,00% | 61.487 $ | 33/40 | +82,50% | +15,00% | 74.432 $ | 9/33 | +27,27% | +21,05% | DEBOLE | 9,0 | 23,4 |
| -5,00% | 61.487 $ | 33/40 | +82,50% | +20,00% | 77.668 $ | 5/33 | +15,15% | +26,32% | DEBOLE | 9,0 | 25,8 |
| -8,00% | 59.546 $ | 26/40 | +65,00% | +5,00% | 67.960 $ | 10/26 | +38,46% | +14,13% | BASSA | 12,4 | 23,2 |
| -8,00% | 59.546 $ | 26/40 | +65,00% | +10,00% | 71.196 $ | 7/26 | +26,92% | +19,57% | DEBOLE | 12,4 | 24,4 |
| -8,00% | 59.546 $ | 26/40 | +65,00% | +15,00% | 74.432 $ | 3/26 | +11,54% | +25,00% | DEBOLE | 12,4 | 22,3 |
| -8,00% | 59.546 $ | 26/40 | +65,00% | +20,00% | 77.668 $ | 2/26 | +7,69% | +30,43% | DEBOLE | 12,4 | 21,5 |
| -10,00% | 58.251 $ | 19/40 | +47,50% | +5,00% | 67.960 $ | 6/19 | +31,58% | +16,67% | DEBOLE | 12,9 | 25,5 |
| -10,00% | 58.251 $ | 19/40 | +47,50% | +10,00% | 71.196 $ | 3/19 | +15,79% | +22,22% | DEBOLE | 12,9 | 26,7 |
| -10,00% | 58.251 $ | 19/40 | +47,50% | +15,00% | 74.432 $ | 1/19 | +5,26% | +27,78% | DEBOLE | 12,9 | 27,0 |
| -10,00% | 58.251 $ | 19/40 | +47,50% | +20,00% | 77.668 $ | 1/19 | +5,26% | +33,33% | DEBOLE | 12,9 | 27,0 |
| -15,00% | 55.015 $ | 13/40 | +32,50% | +5,00% | 67.960 $ | 1/13 | +7,69% | +23,53% | DEBOLE | 15,1 | 30,0 |
| -15,00% | 55.015 $ | 13/40 | +32,50% | +10,00% | 71.196 $ | 0/13 | 0,00% | +29,41% | DEBOLE | 15,1 | n/d |
| -15,00% | 55.015 $ | 13/40 | +32,50% | +15,00% | 74.432 $ | 0/13 | 0,00% | +35,29% | DEBOLE | 15,1 | n/d |
| -15,00% | 55.015 $ | 13/40 | +32,50% | +20,00% | 77.668 $ | 0/13 | 0,00% | +41,18% | DEBOLE | 15,1 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 67.960 $ | 31/40 | +77,50% | prezzo iniziale | 64.723 $ | 14/31 | +45,16% | -4,76% | BASSA | 12,9 | 13,7 |
| +5,00% | 67.960 $ | 31/40 | +77,50% | -5,00% | 61.487 $ | 11/31 | +35,48% | -9,52% | BASSA | 12,9 | 15,7 |
| +5,00% | 67.960 $ | 31/40 | +77,50% | -8,00% | 59.546 $ | 9/31 | +29,03% | -12,38% | DEBOLE | 12,9 | 20,1 |
| +5,00% | 67.960 $ | 31/40 | +77,50% | -10,00% | 58.251 $ | 5/31 | +16,13% | -14,29% | DEBOLE | 12,9 | 22,6 |
| +5,00% | 67.960 $ | 31/40 | +77,50% | -15,00% | 55.015 $ | 4/31 | +12,90% | -19,05% | DEBOLE | 12,9 | 22,5 |
| +10,00% | 71.196 $ | 24/40 | +60,00% | prezzo iniziale | 64.723 $ | 8/24 | +33,33% | -9,09% | DEBOLE | 16,2 | 16,8 |
| +10,00% | 71.196 $ | 24/40 | +60,00% | -5,00% | 61.487 $ | 7/24 | +29,17% | -13,64% | DEBOLE | 16,2 | 17,7 |
| +10,00% | 71.196 $ | 24/40 | +60,00% | -8,00% | 59.546 $ | 5/24 | +20,83% | -16,36% | DEBOLE | 16,2 | 23,2 |
| +10,00% | 71.196 $ | 24/40 | +60,00% | -10,00% | 58.251 $ | 3/24 | +12,50% | -18,18% | DEBOLE | 16,2 | 24,7 |
| +10,00% | 71.196 $ | 24/40 | +60,00% | -15,00% | 55.015 $ | 3/24 | +12,50% | -22,73% | DEBOLE | 16,2 | 25,0 |
| +15,00% | 74.432 $ | 17/40 | +42,50% | prezzo iniziale | 64.723 $ | 5/17 | +29,41% | -13,04% | DEBOLE | 17,1 | 20,4 |
| +15,00% | 74.432 $ | 17/40 | +42,50% | -5,00% | 61.487 $ | 4/17 | +23,53% | -17,39% | DEBOLE | 17,1 | 21,0 |
| +15,00% | 74.432 $ | 17/40 | +42,50% | -8,00% | 59.546 $ | 4/17 | +23,53% | -20,00% | DEBOLE | 17,1 | 26,0 |
| +15,00% | 74.432 $ | 17/40 | +42,50% | -10,00% | 58.251 $ | 3/17 | +17,65% | -21,74% | DEBOLE | 17,1 | 24,7 |
| +15,00% | 74.432 $ | 17/40 | +42,50% | -15,00% | 55.015 $ | 3/17 | +17,65% | -26,09% | DEBOLE | 17,1 | 25,0 |
| +20,00% | 77.668 $ | 11/40 | +27,50% | prezzo iniziale | 64.723 $ | 2/11 | +18,18% | -16,67% | DEBOLE | 19,2 | 16,0 |
| +20,00% | 77.668 $ | 11/40 | +27,50% | -5,00% | 61.487 $ | 2/11 | +18,18% | -20,83% | DEBOLE | 19,2 | 16,0 |
| +20,00% | 77.668 $ | 11/40 | +27,50% | -8,00% | 59.546 $ | 2/11 | +18,18% | -23,33% | DEBOLE | 19,2 | 26,0 |
| +20,00% | 77.668 $ | 11/40 | +27,50% | -10,00% | 58.251 $ | 1/11 | +9,09% | -25,00% | DEBOLE | 19,2 | 22,0 |
| +20,00% | 77.668 $ | 11/40 | +27,50% | -15,00% | 55.015 $ | 1/11 | +9,09% | -29,17% | DEBOLE | 19,2 | 23,0 |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 33 prima sono scesi a -5,00%. Tra quei 33, 10 poi sono rimbalzati fino a +10,00%. Percentuale: +30,30% (10/33). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 17 prima sono saliti a +10,00%. Tra quei 17, 4 poi sono scaricati a -5,00%. Percentuale: +23,53% (4/17). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 72,20 $ | 33/40 | +82,50% | +5,00% | 79,80 $ | 17/33 | +51,52% | +10,53% | MEDIA | 5,3 | 20,2 |
| -5,00% | 72,20 $ | 33/40 | +82,50% | +10,00% | 83,60 $ | 10/33 | +30,30% | +15,79% | DEBOLE | 5,3 | 19,6 |
| -5,00% | 72,20 $ | 33/40 | +82,50% | +15,00% | 87,40 $ | 7/33 | +21,21% | +21,05% | DEBOLE | 5,3 | 19,9 |
| -5,00% | 72,20 $ | 33/40 | +82,50% | +20,00% | 91,20 $ | 6/33 | +18,18% | +26,32% | DEBOLE | 5,3 | 21,7 |
| -8,00% | 69,92 $ | 27/40 | +67,50% | +5,00% | 79,80 $ | 11/27 | +40,74% | +14,13% | BASSA | 5,6 | 19,2 |
| -8,00% | 69,92 $ | 27/40 | +67,50% | +10,00% | 83,60 $ | 8/27 | +29,63% | +19,57% | DEBOLE | 5,6 | 20,2 |
| -8,00% | 69,92 $ | 27/40 | +67,50% | +15,00% | 87,40 $ | 5/27 | +18,52% | +25,00% | DEBOLE | 5,6 | 19,0 |
| -8,00% | 69,92 $ | 27/40 | +67,50% | +20,00% | 91,20 $ | 4/27 | +14,81% | +30,43% | DEBOLE | 5,6 | 20,8 |
| -10,00% | 68,40 $ | 22/40 | +55,00% | +5,00% | 79,80 $ | 9/22 | +40,91% | +16,67% | BASSA | 5,9 | 19,6 |
| -10,00% | 68,40 $ | 22/40 | +55,00% | +10,00% | 83,60 $ | 6/22 | +27,27% | +22,22% | DEBOLE | 5,9 | 19,7 |
| -10,00% | 68,40 $ | 22/40 | +55,00% | +15,00% | 87,40 $ | 4/22 | +18,18% | +27,78% | DEBOLE | 5,9 | 17,5 |
| -10,00% | 68,40 $ | 22/40 | +55,00% | +20,00% | 91,20 $ | 3/22 | +13,64% | +33,33% | DEBOLE | 5,9 | 18,7 |
| -15,00% | 64,60 $ | 13/40 | +32,50% | +5,00% | 79,80 $ | 2/13 | +15,38% | +23,53% | DEBOLE | 9,5 | 16,0 |
| -15,00% | 64,60 $ | 13/40 | +32,50% | +10,00% | 83,60 $ | 1/13 | +7,69% | +29,41% | DEBOLE | 9,5 | 14,0 |
| -15,00% | 64,60 $ | 13/40 | +32,50% | +15,00% | 87,40 $ | 1/13 | +7,69% | +35,29% | DEBOLE | 9,5 | 14,0 |
| -15,00% | 64,60 $ | 13/40 | +32,50% | +20,00% | 91,20 $ | 1/13 | +7,69% | +41,18% | DEBOLE | 9,5 | 20,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 79,80 $ | 25/40 | +62,50% | prezzo iniziale | 76,00 $ | 15/25 | +60,00% | -4,76% | MEDIA | 12,8 | 15,9 |
| +5,00% | 79,80 $ | 25/40 | +62,50% | -5,00% | 72,20 $ | 10/25 | +40,00% | -9,52% | BASSA | 12,8 | 18,7 |
| +5,00% | 79,80 $ | 25/40 | +62,50% | -8,00% | 69,92 $ | 5/25 | +20,00% | -12,38% | DEBOLE | 12,8 | 21,8 |
| +5,00% | 79,80 $ | 25/40 | +62,50% | -10,00% | 68,40 $ | 3/25 | +12,00% | -14,29% | DEBOLE | 12,8 | 21,3 |
| +5,00% | 79,80 $ | 25/40 | +62,50% | -15,00% | 64,60 $ | 0/25 | 0,00% | -19,05% | DEBOLE | 12,8 | n/d |
| +10,00% | 83,60 $ | 17/40 | +42,50% | prezzo iniziale | 76,00 $ | 5/17 | +29,41% | -9,09% | DEBOLE | 15,9 | 20,4 |
| +10,00% | 83,60 $ | 17/40 | +42,50% | -5,00% | 72,20 $ | 4/17 | +23,53% | -13,64% | DEBOLE | 15,9 | 23,2 |
| +10,00% | 83,60 $ | 17/40 | +42,50% | -8,00% | 69,92 $ | 1/17 | +5,88% | -16,36% | DEBOLE | 15,9 | 30,0 |
| +10,00% | 83,60 $ | 17/40 | +42,50% | -10,00% | 68,40 $ | 1/17 | +5,88% | -18,18% | DEBOLE | 15,9 | 30,0 |
| +10,00% | 83,60 $ | 17/40 | +42,50% | -15,00% | 64,60 $ | 0/17 | 0,00% | -22,73% | DEBOLE | 15,9 | n/d |
| +15,00% | 87,40 $ | 12/40 | +30,00% | prezzo iniziale | 76,00 $ | 3/12 | +25,00% | -13,04% | DEBOLE | 13,8 | 17,3 |
| +15,00% | 87,40 $ | 12/40 | +30,00% | -5,00% | 72,20 $ | 2/12 | +16,67% | -17,39% | DEBOLE | 13,8 | 18,0 |
| +15,00% | 87,40 $ | 12/40 | +30,00% | -8,00% | 69,92 $ | 0/12 | 0,00% | -20,00% | DEBOLE | 13,8 | n/d |
| +15,00% | 87,40 $ | 12/40 | +30,00% | -10,00% | 68,40 $ | 0/12 | 0,00% | -21,74% | DEBOLE | 13,8 | n/d |
| +15,00% | 87,40 $ | 12/40 | +30,00% | -15,00% | 64,60 $ | 0/12 | 0,00% | -26,09% | DEBOLE | 13,8 | n/d |
| +20,00% | 91,20 $ | 10/40 | +25,00% | prezzo iniziale | 76,00 $ | 1/10 | +10,00% | -16,67% | DEBOLE | 15,3 | 7,0 |
| +20,00% | 91,20 $ | 10/40 | +25,00% | -5,00% | 72,20 $ | 1/10 | +10,00% | -20,83% | DEBOLE | 15,3 | 7,0 |
| +20,00% | 91,20 $ | 10/40 | +25,00% | -8,00% | 69,92 $ | 0/10 | 0,00% | -23,33% | DEBOLE | 15,3 | n/d |
| +20,00% | 91,20 $ | 10/40 | +25,00% | -10,00% | 68,40 $ | 0/10 | 0,00% | -25,00% | DEBOLE | 15,3 | n/d |
| +20,00% | 91,20 $ | 10/40 | +25,00% | -15,00% | 64,60 $ | 0/10 | 0,00% | -29,17% | DEBOLE | 15,3 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 34 prima sono scesi a -5,00%. Tra quei 34, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +17,65% (6/34). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 17 prima sono saliti a +10,00%. Tra quei 17, 7 poi sono scaricati a -5,00%. Percentuale: +41,18% (7/17). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06880 $ | 34/40 | +85,00% | +5,00% | 0,07604 $ | 8/34 | +23,53% | +10,53% | DEBOLE | 6,5 | 16,5 |
| -5,00% | 0,06880 $ | 34/40 | +85,00% | +10,00% | 0,07966 $ | 6/34 | +17,65% | +15,79% | DEBOLE | 6,5 | 20,0 |
| -5,00% | 0,06880 $ | 34/40 | +85,00% | +15,00% | 0,08328 $ | 3/34 | +8,82% | +21,05% | DEBOLE | 6,5 | 17,3 |
| -5,00% | 0,06880 $ | 34/40 | +85,00% | +20,00% | 0,08690 $ | 3/34 | +8,82% | +26,32% | DEBOLE | 6,5 | 18,3 |
| -8,00% | 0,06663 $ | 31/40 | +77,50% | +5,00% | 0,07604 $ | 6/31 | +19,35% | +14,13% | DEBOLE | 7,0 | 18,7 |
| -8,00% | 0,06663 $ | 31/40 | +77,50% | +10,00% | 0,07966 $ | 4/31 | +12,90% | +19,57% | DEBOLE | 7,0 | 20,0 |
| -8,00% | 0,06663 $ | 31/40 | +77,50% | +15,00% | 0,08328 $ | 1/31 | +3,23% | +25,00% | DEBOLE | 7,0 | 9,0 |
| -8,00% | 0,06663 $ | 31/40 | +77,50% | +20,00% | 0,08690 $ | 1/31 | +3,23% | +30,43% | DEBOLE | 7,0 | 10,0 |
| -10,00% | 0,06518 $ | 30/40 | +75,00% | +5,00% | 0,07604 $ | 5/30 | +16,67% | +16,67% | DEBOLE | 7,5 | 20,6 |
| -10,00% | 0,06518 $ | 30/40 | +75,00% | +10,00% | 0,07966 $ | 3/30 | +10,00% | +22,22% | DEBOLE | 7,5 | 23,7 |
| -10,00% | 0,06518 $ | 30/40 | +75,00% | +15,00% | 0,08328 $ | 0/30 | 0,00% | +27,78% | DEBOLE | 7,5 | n/d |
| -10,00% | 0,06518 $ | 30/40 | +75,00% | +20,00% | 0,08690 $ | 0/30 | 0,00% | +33,33% | DEBOLE | 7,5 | n/d |
| -15,00% | 0,06156 $ | 25/40 | +62,50% | +5,00% | 0,07604 $ | 2/25 | +8,00% | +23,53% | DEBOLE | 7,6 | 14,0 |
| -15,00% | 0,06156 $ | 25/40 | +62,50% | +10,00% | 0,07966 $ | 1/25 | +4,00% | +29,41% | DEBOLE | 7,6 | 15,0 |
| -15,00% | 0,06156 $ | 25/40 | +62,50% | +15,00% | 0,08328 $ | 0/25 | 0,00% | +35,29% | DEBOLE | 7,6 | n/d |
| -15,00% | 0,06156 $ | 25/40 | +62,50% | +20,00% | 0,08690 $ | 0/25 | 0,00% | +41,18% | DEBOLE | 7,6 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07604 $ | 21/40 | +52,50% | prezzo iniziale | 0,07242 $ | 16/21 | +76,19% | -4,76% | ALTA | 7,0 | 13,3 |
| +5,00% | 0,07604 $ | 21/40 | +52,50% | -5,00% | 0,06880 $ | 11/21 | +52,38% | -9,52% | MEDIA | 7,0 | 18,8 |
| +5,00% | 0,07604 $ | 21/40 | +52,50% | -8,00% | 0,06663 $ | 9/21 | +42,86% | -12,38% | BASSA | 7,0 | 19,8 |
| +5,00% | 0,07604 $ | 21/40 | +52,50% | -10,00% | 0,06518 $ | 8/21 | +38,10% | -14,29% | BASSA | 7,0 | 22,6 |
| +5,00% | 0,07604 $ | 21/40 | +52,50% | -15,00% | 0,06156 $ | 4/21 | +19,05% | -19,05% | DEBOLE | 7,0 | 23,8 |
| +10,00% | 0,07966 $ | 17/40 | +42,50% | prezzo iniziale | 0,07242 $ | 10/17 | +58,82% | -9,09% | MEDIA | 10,8 | 19,4 |
| +10,00% | 0,07966 $ | 17/40 | +42,50% | -5,00% | 0,06880 $ | 7/17 | +41,18% | -13,64% | BASSA | 10,8 | 22,3 |
| +10,00% | 0,07966 $ | 17/40 | +42,50% | -8,00% | 0,06663 $ | 5/17 | +29,41% | -16,36% | DEBOLE | 10,8 | 21,8 |
| +10,00% | 0,07966 $ | 17/40 | +42,50% | -10,00% | 0,06518 $ | 5/17 | +29,41% | -18,18% | DEBOLE | 10,8 | 21,8 |
| +10,00% | 0,07966 $ | 17/40 | +42,50% | -15,00% | 0,06156 $ | 3/17 | +17,65% | -22,73% | DEBOLE | 10,8 | 24,7 |
| +15,00% | 0,08328 $ | 14/40 | +35,00% | prezzo iniziale | 0,07242 $ | 9/14 | +64,29% | -13,04% | MEDIA | 9,3 | 21,3 |
| +15,00% | 0,08328 $ | 14/40 | +35,00% | -5,00% | 0,06880 $ | 6/14 | +42,86% | -17,39% | BASSA | 9,3 | 22,8 |
| +15,00% | 0,08328 $ | 14/40 | +35,00% | -8,00% | 0,06663 $ | 5/14 | +35,71% | -20,00% | BASSA | 9,3 | 21,8 |
| +15,00% | 0,08328 $ | 14/40 | +35,00% | -10,00% | 0,06518 $ | 5/14 | +35,71% | -21,74% | BASSA | 9,3 | 21,8 |
| +15,00% | 0,08328 $ | 14/40 | +35,00% | -15,00% | 0,06156 $ | 3/14 | +21,43% | -26,09% | DEBOLE | 9,3 | 24,7 |
| +20,00% | 0,08690 $ | 9/40 | +22,50% | prezzo iniziale | 0,07242 $ | 4/9 | +44,44% | -16,67% | BASSA | 11,3 | 23,2 |
| +20,00% | 0,08690 $ | 9/40 | +22,50% | -5,00% | 0,06880 $ | 2/9 | +22,22% | -20,83% | DEBOLE | 11,3 | 24,0 |
| +20,00% | 0,08690 $ | 9/40 | +22,50% | -8,00% | 0,06663 $ | 1/9 | +11,11% | -23,33% | DEBOLE | 11,3 | 19,0 |
| +20,00% | 0,08690 $ | 9/40 | +22,50% | -10,00% | 0,06518 $ | 1/9 | +11,11% | -25,00% | DEBOLE | 11,3 | 19,0 |
| +20,00% | 0,08690 $ | 9/40 | +22,50% | -15,00% | 0,06156 $ | 0/9 | 0,00% | -29,17% | DEBOLE | 11,3 | n/d |

---
