# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-17 02:32:01 CEST**  
UTC: **2026-07-17 00:32:01 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 60.554 $ | 70.116 $ | +41,94% | +15,79% | rimbalzo debole | 70.116 $ | 60.554 $ | +22,73% | -13,64% | spike storicamente più resistente |
| SOL | 71,52 $ | 82,81 $ | +12,90% | +15,79% | rimbalzo poco frequente | 82,81 $ | 71,52 $ | +31,25% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06868 $ | 0,07952 $ | +19,44% | +15,79% | rimbalzo poco frequente | 0,07952 $ | 0,06868 $ | +40,00% | -13,64% | scarico possibile |

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

- BTC: su 40 casi simili, 31 prima sono scesi a -5,00%. Tra quei 31, 13 poi sono rimbalzati fino a +10,00%. Percentuale: +41,94% (13/31). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 22 prima sono saliti a +10,00%. Tra quei 22, 5 poi sono scaricati a -5,00%. Percentuale: +22,73% (5/22). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 60.554 $ | 31/40 | +77,50% | +5,00% | 66.928 $ | 15/31 | +48,39% | +10,53% | BASSA | 8,3 | 21,7 |
| -5,00% | 60.554 $ | 31/40 | +77,50% | +10,00% | 70.116 $ | 13/31 | +41,94% | +15,79% | BASSA | 8,3 | 25,2 |
| -5,00% | 60.554 $ | 31/40 | +77,50% | +15,00% | 73.303 $ | 7/31 | +22,58% | +21,05% | DEBOLE | 8,3 | 24,1 |
| -5,00% | 60.554 $ | 31/40 | +77,50% | +20,00% | 76.490 $ | 5/31 | +16,13% | +26,32% | DEBOLE | 8,3 | 25,4 |
| -8,00% | 58.642 $ | 25/40 | +62,50% | +5,00% | 66.928 $ | 9/25 | +36,00% | +14,13% | BASSA | 10,6 | 23,0 |
| -8,00% | 58.642 $ | 25/40 | +62,50% | +10,00% | 70.116 $ | 7/25 | +28,00% | +19,57% | DEBOLE | 10,6 | 25,0 |
| -8,00% | 58.642 $ | 25/40 | +62,50% | +15,00% | 73.303 $ | 3/25 | +12,00% | +25,00% | DEBOLE | 10,6 | 22,0 |
| -8,00% | 58.642 $ | 25/40 | +62,50% | +20,00% | 76.490 $ | 2/25 | +8,00% | +30,43% | DEBOLE | 10,6 | 21,0 |
| -10,00% | 57.367 $ | 19/40 | +47,50% | +5,00% | 66.928 $ | 5/19 | +26,32% | +16,67% | DEBOLE | 11,5 | 25,6 |
| -10,00% | 57.367 $ | 19/40 | +47,50% | +10,00% | 70.116 $ | 3/19 | +15,79% | +22,22% | DEBOLE | 11,5 | 28,0 |
| -10,00% | 57.367 $ | 19/40 | +47,50% | +15,00% | 73.303 $ | 1/19 | +5,26% | +27,78% | DEBOLE | 11,5 | 26,0 |
| -10,00% | 57.367 $ | 19/40 | +47,50% | +20,00% | 76.490 $ | 1/19 | +5,26% | +33,33% | DEBOLE | 11,5 | 26,0 |
| -15,00% | 54.180 $ | 12/40 | +30,00% | +5,00% | 66.928 $ | 1/12 | +8,33% | +23,53% | DEBOLE | 14,6 | 30,0 |
| -15,00% | 54.180 $ | 12/40 | +30,00% | +10,00% | 70.116 $ | 0/12 | 0,00% | +29,41% | DEBOLE | 14,6 | n/d |
| -15,00% | 54.180 $ | 12/40 | +30,00% | +15,00% | 73.303 $ | 0/12 | 0,00% | +35,29% | DEBOLE | 14,6 | n/d |
| -15,00% | 54.180 $ | 12/40 | +30,00% | +20,00% | 76.490 $ | 0/12 | 0,00% | +41,18% | DEBOLE | 14,6 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 66.928 $ | 29/40 | +72,50% | prezzo iniziale | 63.741 $ | 15/29 | +51,72% | -4,76% | MEDIA | 10,9 | 13,3 |
| +5,00% | 66.928 $ | 29/40 | +72,50% | -5,00% | 60.554 $ | 11/29 | +37,93% | -9,52% | BASSA | 10,9 | 13,5 |
| +5,00% | 66.928 $ | 29/40 | +72,50% | -8,00% | 58.642 $ | 8/29 | +27,59% | -12,38% | DEBOLE | 10,9 | 15,0 |
| +5,00% | 66.928 $ | 29/40 | +72,50% | -10,00% | 57.367 $ | 5/29 | +17,24% | -14,29% | DEBOLE | 10,9 | 16,6 |
| +5,00% | 66.928 $ | 29/40 | +72,50% | -15,00% | 54.180 $ | 2/29 | +6,90% | -19,05% | DEBOLE | 10,9 | 21,0 |
| +10,00% | 70.116 $ | 22/40 | +55,00% | prezzo iniziale | 63.741 $ | 6/22 | +27,27% | -9,09% | DEBOLE | 16,0 | 12,0 |
| +10,00% | 70.116 $ | 22/40 | +55,00% | -5,00% | 60.554 $ | 5/22 | +22,73% | -13,64% | DEBOLE | 16,0 | 12,2 |
| +10,00% | 70.116 $ | 22/40 | +55,00% | -8,00% | 58.642 $ | 3/22 | +13,64% | -16,36% | DEBOLE | 16,0 | 13,3 |
| +10,00% | 70.116 $ | 22/40 | +55,00% | -10,00% | 57.367 $ | 2/22 | +9,09% | -18,18% | DEBOLE | 16,0 | 14,0 |
| +10,00% | 70.116 $ | 22/40 | +55,00% | -15,00% | 54.180 $ | 1/22 | +4,55% | -22,73% | DEBOLE | 16,0 | 12,0 |
| +15,00% | 73.303 $ | 13/40 | +32,50% | prezzo iniziale | 63.741 $ | 1/13 | +7,69% | -13,04% | DEBOLE | 16,4 | 20,0 |
| +15,00% | 73.303 $ | 13/40 | +32,50% | -5,00% | 60.554 $ | 0/13 | 0,00% | -17,39% | DEBOLE | 16,4 | n/d |
| +15,00% | 73.303 $ | 13/40 | +32,50% | -8,00% | 58.642 $ | 0/13 | 0,00% | -20,00% | DEBOLE | 16,4 | n/d |
| +15,00% | 73.303 $ | 13/40 | +32,50% | -10,00% | 57.367 $ | 0/13 | 0,00% | -21,74% | DEBOLE | 16,4 | n/d |
| +15,00% | 73.303 $ | 13/40 | +32,50% | -15,00% | 54.180 $ | 0/13 | 0,00% | -26,09% | DEBOLE | 16,4 | n/d |
| +20,00% | 76.490 $ | 10/40 | +25,00% | prezzo iniziale | 63.741 $ | 0/10 | 0,00% | -16,67% | DEBOLE | 17,9 | n/d |
| +20,00% | 76.490 $ | 10/40 | +25,00% | -5,00% | 60.554 $ | 0/10 | 0,00% | -20,83% | DEBOLE | 17,9 | n/d |
| +20,00% | 76.490 $ | 10/40 | +25,00% | -8,00% | 58.642 $ | 0/10 | 0,00% | -23,33% | DEBOLE | 17,9 | n/d |
| +20,00% | 76.490 $ | 10/40 | +25,00% | -10,00% | 57.367 $ | 0/10 | 0,00% | -25,00% | DEBOLE | 17,9 | n/d |
| +20,00% | 76.490 $ | 10/40 | +25,00% | -15,00% | 54.180 $ | 0/10 | 0,00% | -29,17% | DEBOLE | 17,9 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 31 prima sono scesi a -5,00%. Tra quei 31, 4 poi sono rimbalzati fino a +10,00%. Percentuale: +12,90% (4/31). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 16 prima sono saliti a +10,00%. Tra quei 16, 5 poi sono scaricati a -5,00%. Percentuale: +31,25% (5/16). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 71,52 $ | 31/40 | +77,50% | +5,00% | 79,04 $ | 11/31 | +35,48% | +10,53% | BASSA | 7,0 | 22,1 |
| -5,00% | 71,52 $ | 31/40 | +77,50% | +10,00% | 82,81 $ | 4/31 | +12,90% | +15,79% | DEBOLE | 7,0 | 18,2 |
| -5,00% | 71,52 $ | 31/40 | +77,50% | +15,00% | 86,57 $ | 3/31 | +9,68% | +21,05% | DEBOLE | 7,0 | 17,7 |
| -5,00% | 71,52 $ | 31/40 | +77,50% | +20,00% | 90,34 $ | 2/31 | +6,45% | +26,32% | DEBOLE | 7,0 | 21,5 |
| -8,00% | 69,26 $ | 27/40 | +67,50% | +5,00% | 79,04 $ | 6/27 | +22,22% | +14,13% | DEBOLE | 8,9 | 20,5 |
| -8,00% | 69,26 $ | 27/40 | +67,50% | +10,00% | 82,81 $ | 3/27 | +11,11% | +19,57% | DEBOLE | 8,9 | 20,0 |
| -8,00% | 69,26 $ | 27/40 | +67,50% | +15,00% | 86,57 $ | 2/27 | +7,41% | +25,00% | DEBOLE | 8,9 | 20,0 |
| -8,00% | 69,26 $ | 27/40 | +67,50% | +20,00% | 90,34 $ | 2/27 | +7,41% | +30,43% | DEBOLE | 8,9 | 21,5 |
| -10,00% | 67,75 $ | 21/40 | +52,50% | +5,00% | 79,04 $ | 3/21 | +14,29% | +16,67% | DEBOLE | 9,1 | 21,0 |
| -10,00% | 67,75 $ | 21/40 | +52,50% | +10,00% | 82,81 $ | 0/21 | 0,00% | +22,22% | DEBOLE | 9,1 | n/d |
| -10,00% | 67,75 $ | 21/40 | +52,50% | +15,00% | 86,57 $ | 0/21 | 0,00% | +27,78% | DEBOLE | 9,1 | n/d |
| -10,00% | 67,75 $ | 21/40 | +52,50% | +20,00% | 90,34 $ | 0/21 | 0,00% | +33,33% | DEBOLE | 9,1 | n/d |
| -15,00% | 63,99 $ | 16/40 | +40,00% | +5,00% | 79,04 $ | 2/16 | +12,50% | +23,53% | DEBOLE | 11,6 | 17,0 |
| -15,00% | 63,99 $ | 16/40 | +40,00% | +10,00% | 82,81 $ | 0/16 | 0,00% | +29,41% | DEBOLE | 11,6 | n/d |
| -15,00% | 63,99 $ | 16/40 | +40,00% | +15,00% | 86,57 $ | 0/16 | 0,00% | +35,29% | DEBOLE | 11,6 | n/d |
| -15,00% | 63,99 $ | 16/40 | +40,00% | +20,00% | 90,34 $ | 0/16 | 0,00% | +41,18% | DEBOLE | 11,6 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 79,04 $ | 24/40 | +60,00% | prezzo iniziale | 75,28 $ | 11/24 | +45,83% | -4,76% | BASSA | 10,8 | 11,0 |
| +5,00% | 79,04 $ | 24/40 | +60,00% | -5,00% | 71,52 $ | 9/24 | +37,50% | -9,52% | BASSA | 10,8 | 12,6 |
| +5,00% | 79,04 $ | 24/40 | +60,00% | -8,00% | 69,26 $ | 9/24 | +37,50% | -12,38% | BASSA | 10,8 | 16,7 |
| +5,00% | 79,04 $ | 24/40 | +60,00% | -10,00% | 67,75 $ | 5/24 | +20,83% | -14,29% | DEBOLE | 10,8 | 15,8 |
| +5,00% | 79,04 $ | 24/40 | +60,00% | -15,00% | 63,99 $ | 4/24 | +16,67% | -19,05% | DEBOLE | 10,8 | 21,2 |
| +10,00% | 82,81 $ | 16/40 | +40,00% | prezzo iniziale | 75,28 $ | 5/16 | +31,25% | -9,09% | DEBOLE | 9,8 | 7,0 |
| +10,00% | 82,81 $ | 16/40 | +40,00% | -5,00% | 71,52 $ | 5/16 | +31,25% | -13,64% | DEBOLE | 9,8 | 8,2 |
| +10,00% | 82,81 $ | 16/40 | +40,00% | -8,00% | 69,26 $ | 5/16 | +31,25% | -16,36% | DEBOLE | 9,8 | 14,2 |
| +10,00% | 82,81 $ | 16/40 | +40,00% | -10,00% | 67,75 $ | 3/16 | +18,75% | -18,18% | DEBOLE | 9,8 | 10,3 |
| +10,00% | 82,81 $ | 16/40 | +40,00% | -15,00% | 63,99 $ | 2/16 | +12,50% | -22,73% | DEBOLE | 9,8 | 18,0 |
| +15,00% | 86,57 $ | 11/40 | +27,50% | prezzo iniziale | 75,28 $ | 2/11 | +18,18% | -13,04% | DEBOLE | 9,5 | 7,5 |
| +15,00% | 86,57 $ | 11/40 | +27,50% | -5,00% | 71,52 $ | 2/11 | +18,18% | -17,39% | DEBOLE | 9,5 | 8,0 |
| +15,00% | 86,57 $ | 11/40 | +27,50% | -8,00% | 69,26 $ | 2/11 | +18,18% | -20,00% | DEBOLE | 9,5 | 18,5 |
| +15,00% | 86,57 $ | 11/40 | +27,50% | -10,00% | 67,75 $ | 1/11 | +9,09% | -21,74% | DEBOLE | 9,5 | 7,0 |
| +15,00% | 86,57 $ | 11/40 | +27,50% | -15,00% | 63,99 $ | 1/11 | +9,09% | -26,09% | DEBOLE | 9,5 | 8,0 |
| +20,00% | 90,34 $ | 10/40 | +25,00% | prezzo iniziale | 75,28 $ | 1/10 | +10,00% | -16,67% | DEBOLE | 10,9 | 10,0 |
| +20,00% | 90,34 $ | 10/40 | +25,00% | -5,00% | 71,52 $ | 1/10 | +10,00% | -20,83% | DEBOLE | 10,9 | 10,0 |
| +20,00% | 90,34 $ | 10/40 | +25,00% | -8,00% | 69,26 $ | 1/10 | +10,00% | -23,33% | DEBOLE | 10,9 | 30,0 |
| +20,00% | 90,34 $ | 10/40 | +25,00% | -10,00% | 67,75 $ | 0/10 | 0,00% | -25,00% | DEBOLE | 10,9 | n/d |
| +20,00% | 90,34 $ | 10/40 | +25,00% | -15,00% | 63,99 $ | 0/10 | 0,00% | -29,17% | DEBOLE | 10,9 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 36 prima sono scesi a -5,00%. Tra quei 36, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +19,44% (7/36). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 15 prima sono saliti a +10,00%. Tra quei 15, 6 poi sono scaricati a -5,00%. Percentuale: +40,00% (6/15). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06868 $ | 36/40 | +90,00% | +5,00% | 0,07590 $ | 8/36 | +22,22% | +10,53% | DEBOLE | 4,7 | 15,0 |
| -5,00% | 0,06868 $ | 36/40 | +90,00% | +10,00% | 0,07952 $ | 7/36 | +19,44% | +15,79% | DEBOLE | 4,7 | 16,6 |
| -5,00% | 0,06868 $ | 36/40 | +90,00% | +15,00% | 0,08313 $ | 4/36 | +11,11% | +21,05% | DEBOLE | 4,7 | 15,2 |
| -5,00% | 0,06868 $ | 36/40 | +90,00% | +20,00% | 0,08675 $ | 4/36 | +11,11% | +26,32% | DEBOLE | 4,7 | 16,8 |
| -8,00% | 0,06651 $ | 34/40 | +85,00% | +5,00% | 0,07590 $ | 6/34 | +17,65% | +14,13% | DEBOLE | 5,6 | 16,7 |
| -8,00% | 0,06651 $ | 34/40 | +85,00% | +10,00% | 0,07952 $ | 5/34 | +14,71% | +19,57% | DEBOLE | 5,6 | 15,2 |
| -8,00% | 0,06651 $ | 34/40 | +85,00% | +15,00% | 0,08313 $ | 2/34 | +5,88% | +25,00% | DEBOLE | 5,6 | 9,0 |
| -8,00% | 0,06651 $ | 34/40 | +85,00% | +20,00% | 0,08675 $ | 2/34 | +5,88% | +30,43% | DEBOLE | 5,6 | 11,0 |
| -10,00% | 0,06506 $ | 31/40 | +77,50% | +5,00% | 0,07590 $ | 3/31 | +9,68% | +16,67% | DEBOLE | 5,5 | 20,7 |
| -10,00% | 0,06506 $ | 31/40 | +77,50% | +10,00% | 0,07952 $ | 3/31 | +9,68% | +22,22% | DEBOLE | 5,5 | 21,0 |
| -10,00% | 0,06506 $ | 31/40 | +77,50% | +15,00% | 0,08313 $ | 0/31 | 0,00% | +27,78% | DEBOLE | 5,5 | n/d |
| -10,00% | 0,06506 $ | 31/40 | +77,50% | +20,00% | 0,08675 $ | 0/31 | 0,00% | +33,33% | DEBOLE | 5,5 | n/d |
| -15,00% | 0,06145 $ | 30/40 | +75,00% | +5,00% | 0,07590 $ | 2/30 | +6,67% | +23,53% | DEBOLE | 7,6 | 18,0 |
| -15,00% | 0,06145 $ | 30/40 | +75,00% | +10,00% | 0,07952 $ | 2/30 | +6,67% | +29,41% | DEBOLE | 7,6 | 18,5 |
| -15,00% | 0,06145 $ | 30/40 | +75,00% | +15,00% | 0,08313 $ | 0/30 | 0,00% | +35,29% | DEBOLE | 7,6 | n/d |
| -15,00% | 0,06145 $ | 30/40 | +75,00% | +20,00% | 0,08675 $ | 0/30 | 0,00% | +41,18% | DEBOLE | 7,6 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07590 $ | 18/40 | +45,00% | prezzo iniziale | 0,07229 $ | 13/18 | +72,22% | -4,76% | ALTA | 4,9 | 8,8 |
| +5,00% | 0,07590 $ | 18/40 | +45,00% | -5,00% | 0,06868 $ | 10/18 | +55,56% | -9,52% | MEDIA | 4,9 | 10,4 |
| +5,00% | 0,07590 $ | 18/40 | +45,00% | -8,00% | 0,06651 $ | 10/18 | +55,56% | -12,38% | MEDIA | 4,9 | 11,5 |
| +5,00% | 0,07590 $ | 18/40 | +45,00% | -10,00% | 0,06506 $ | 8/18 | +44,44% | -14,29% | BASSA | 4,9 | 11,4 |
| +5,00% | 0,07590 $ | 18/40 | +45,00% | -15,00% | 0,06145 $ | 8/18 | +44,44% | -19,05% | BASSA | 4,9 | 12,4 |
| +10,00% | 0,07952 $ | 15/40 | +37,50% | prezzo iniziale | 0,07229 $ | 9/15 | +60,00% | -9,09% | MEDIA | 10,1 | 13,3 |
| +10,00% | 0,07952 $ | 15/40 | +37,50% | -5,00% | 0,06868 $ | 6/15 | +40,00% | -13,64% | BASSA | 10,1 | 14,0 |
| +10,00% | 0,07952 $ | 15/40 | +37,50% | -8,00% | 0,06651 $ | 6/15 | +40,00% | -16,36% | BASSA | 10,1 | 14,8 |
| +10,00% | 0,07952 $ | 15/40 | +37,50% | -10,00% | 0,06506 $ | 5/15 | +33,33% | -18,18% | DEBOLE | 10,1 | 17,0 |
| +10,00% | 0,07952 $ | 15/40 | +37,50% | -15,00% | 0,06145 $ | 4/15 | +26,67% | -22,73% | DEBOLE | 10,1 | 16,5 |
| +15,00% | 0,08313 $ | 11/40 | +27,50% | prezzo iniziale | 0,07229 $ | 5/11 | +45,45% | -13,04% | BASSA | 11,6 | 16,4 |
| +15,00% | 0,08313 $ | 11/40 | +27,50% | -5,00% | 0,06868 $ | 4/11 | +36,36% | -17,39% | BASSA | 11,6 | 21,0 |
| +15,00% | 0,08313 $ | 11/40 | +27,50% | -8,00% | 0,06651 $ | 3/11 | +27,27% | -20,00% | DEBOLE | 11,6 | 19,0 |
| +15,00% | 0,08313 $ | 11/40 | +27,50% | -10,00% | 0,06506 $ | 3/11 | +27,27% | -21,74% | DEBOLE | 11,6 | 19,0 |
| +15,00% | 0,08313 $ | 11/40 | +27,50% | -15,00% | 0,06145 $ | 3/11 | +27,27% | -26,09% | DEBOLE | 11,6 | 19,7 |
| +20,00% | 0,08675 $ | 8/40 | +20,00% | prezzo iniziale | 0,07229 $ | 2/8 | +25,00% | -16,67% | DEBOLE | 13,6 | 11,5 |
| +20,00% | 0,08675 $ | 8/40 | +20,00% | -5,00% | 0,06868 $ | 2/8 | +25,00% | -20,83% | DEBOLE | 13,6 | 17,5 |
| +20,00% | 0,08675 $ | 8/40 | +20,00% | -8,00% | 0,06651 $ | 1/8 | +12,50% | -23,33% | DEBOLE | 13,6 | 8,0 |
| +20,00% | 0,08675 $ | 8/40 | +20,00% | -10,00% | 0,06506 $ | 1/8 | +12,50% | -25,00% | DEBOLE | 13,6 | 8,0 |
| +20,00% | 0,08675 $ | 8/40 | +20,00% | -15,00% | 0,06145 $ | 1/8 | +12,50% | -29,17% | DEBOLE | 13,6 | 9,0 |

---
