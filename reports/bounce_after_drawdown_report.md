# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-08-21 07:31:40 CEST**  
UTC: **2026-08-21 05:31:40 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 71.377 $ | 82.647 $ | +40,91% | +15,79% | rimbalzo debole | 82.647 $ | 71.377 $ | +29,63% | -13,64% | spike storicamente più resistente |
| SOL | 85,07 $ | 98,51 $ | +36,00% | +15,79% | rimbalzo debole | 98,51 $ | 85,07 $ | +25,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07826 $ | 0,09062 $ | +46,67% | +15,79% | rimbalzo debole | 0,09062 $ | 0,07826 $ | +25,00% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 22 prima sono scesi a -5,00%. Tra quei 22, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +40,91% (9/22). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 27 prima sono saliti a +10,00%. Tra quei 27, 8 poi sono scaricati a -5,00%. Percentuale: +29,63% (8/27). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 71.377 $ | 22/40 | +55,00% | +5,00% | 78.890 $ | 12/22 | +54,55% | +10,53% | MEDIA | 9,6 | 14,2 |
| -5,00% | 71.377 $ | 22/40 | +55,00% | +10,00% | 82.647 $ | 9/22 | +40,91% | +15,79% | BASSA | 9,6 | 13,7 |
| -5,00% | 71.377 $ | 22/40 | +55,00% | +15,00% | 86.403 $ | 7/22 | +31,82% | +21,05% | DEBOLE | 9,6 | 16,0 |
| -5,00% | 71.377 $ | 22/40 | +55,00% | +20,00% | 90.160 $ | 6/22 | +27,27% | +26,32% | DEBOLE | 9,6 | 19,3 |
| -8,00% | 69.123 $ | 19/40 | +47,50% | +5,00% | 78.890 $ | 9/19 | +47,37% | +14,13% | BASSA | 13,2 | 18,6 |
| -8,00% | 69.123 $ | 19/40 | +47,50% | +10,00% | 82.647 $ | 6/19 | +31,58% | +19,57% | DEBOLE | 13,2 | 19,8 |
| -8,00% | 69.123 $ | 19/40 | +47,50% | +15,00% | 86.403 $ | 5/19 | +26,32% | +25,00% | DEBOLE | 13,2 | 23,6 |
| -8,00% | 69.123 $ | 19/40 | +47,50% | +20,00% | 90.160 $ | 4/19 | +21,05% | +30,43% | DEBOLE | 13,2 | 23,8 |
| -10,00% | 67.620 $ | 19/40 | +47,50% | +5,00% | 78.890 $ | 8/19 | +42,11% | +16,67% | BASSA | 15,6 | 20,5 |
| -10,00% | 67.620 $ | 19/40 | +47,50% | +10,00% | 82.647 $ | 5/19 | +26,32% | +22,22% | DEBOLE | 15,6 | 23,2 |
| -10,00% | 67.620 $ | 19/40 | +47,50% | +15,00% | 86.403 $ | 5/19 | +26,32% | +27,78% | DEBOLE | 15,6 | 23,6 |
| -10,00% | 67.620 $ | 19/40 | +47,50% | +20,00% | 90.160 $ | 4/19 | +21,05% | +33,33% | DEBOLE | 15,6 | 23,8 |
| -15,00% | 63.863 $ | 6/40 | +15,00% | +5,00% | 78.890 $ | 1/6 | +16,67% | +23,53% | DEBOLE | 19,3 | 13,0 |
| -15,00% | 63.863 $ | 6/40 | +15,00% | +10,00% | 82.647 $ | 0/6 | 0,00% | +29,41% | DEBOLE | 19,3 | n/d |
| -15,00% | 63.863 $ | 6/40 | +15,00% | +15,00% | 86.403 $ | 0/6 | 0,00% | +35,29% | DEBOLE | 19,3 | n/d |
| -15,00% | 63.863 $ | 6/40 | +15,00% | +20,00% | 90.160 $ | 0/6 | 0,00% | +41,18% | DEBOLE | 19,3 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 78.890 $ | 35/40 | +87,50% | prezzo iniziale | 75.133 $ | 18/35 | +51,43% | -4,76% | MEDIA | 8,4 | 14,9 |
| +5,00% | 78.890 $ | 35/40 | +87,50% | -5,00% | 71.377 $ | 12/35 | +34,29% | -9,52% | DEBOLE | 8,4 | 17,4 |
| +5,00% | 78.890 $ | 35/40 | +87,50% | -8,00% | 69.123 $ | 12/35 | +34,29% | -12,38% | DEBOLE | 8,4 | 19,2 |
| +5,00% | 78.890 $ | 35/40 | +87,50% | -10,00% | 67.620 $ | 11/35 | +31,43% | -14,29% | DEBOLE | 8,4 | 20,0 |
| +5,00% | 78.890 $ | 35/40 | +87,50% | -15,00% | 63.863 $ | 3/35 | +8,57% | -19,05% | DEBOLE | 8,4 | 24,7 |
| +10,00% | 82.647 $ | 27/40 | +67,50% | prezzo iniziale | 75.133 $ | 12/27 | +44,44% | -9,09% | BASSA | 9,4 | 13,9 |
| +10,00% | 82.647 $ | 27/40 | +67,50% | -5,00% | 71.377 $ | 8/27 | +29,63% | -13,64% | DEBOLE | 9,4 | 13,8 |
| +10,00% | 82.647 $ | 27/40 | +67,50% | -8,00% | 69.123 $ | 8/27 | +29,63% | -16,36% | DEBOLE | 9,4 | 16,2 |
| +10,00% | 82.647 $ | 27/40 | +67,50% | -10,00% | 67.620 $ | 8/27 | +29,63% | -18,18% | DEBOLE | 9,4 | 17,0 |
| +10,00% | 82.647 $ | 27/40 | +67,50% | -15,00% | 63.863 $ | 3/27 | +11,11% | -22,73% | DEBOLE | 9,4 | 24,7 |
| +15,00% | 86.403 $ | 22/40 | +55,00% | prezzo iniziale | 75.133 $ | 8/22 | +36,36% | -13,04% | BASSA | 10,6 | 14,4 |
| +15,00% | 86.403 $ | 22/40 | +55,00% | -5,00% | 71.377 $ | 5/22 | +22,73% | -17,39% | DEBOLE | 10,6 | 14,0 |
| +15,00% | 86.403 $ | 22/40 | +55,00% | -8,00% | 69.123 $ | 5/22 | +22,73% | -20,00% | DEBOLE | 10,6 | 16,4 |
| +15,00% | 86.403 $ | 22/40 | +55,00% | -10,00% | 67.620 $ | 5/22 | +22,73% | -21,74% | DEBOLE | 10,6 | 16,8 |
| +15,00% | 86.403 $ | 22/40 | +55,00% | -15,00% | 63.863 $ | 3/22 | +13,64% | -26,09% | DEBOLE | 10,6 | 24,7 |
| +20,00% | 90.160 $ | 16/40 | +40,00% | prezzo iniziale | 75.133 $ | 5/16 | +31,25% | -16,67% | DEBOLE | 11,8 | 15,2 |
| +20,00% | 90.160 $ | 16/40 | +40,00% | -5,00% | 71.377 $ | 3/16 | +18,75% | -20,83% | DEBOLE | 11,8 | 15,3 |
| +20,00% | 90.160 $ | 16/40 | +40,00% | -8,00% | 69.123 $ | 3/16 | +18,75% | -23,33% | DEBOLE | 11,8 | 15,3 |
| +20,00% | 90.160 $ | 16/40 | +40,00% | -10,00% | 67.620 $ | 3/16 | +18,75% | -25,00% | DEBOLE | 11,8 | 15,3 |
| +20,00% | 90.160 $ | 16/40 | +40,00% | -15,00% | 63.863 $ | 2/16 | +12,50% | -29,17% | DEBOLE | 11,8 | 26,5 |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 25 prima sono scesi a -5,00%. Tra quei 25, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +36,00% (9/25). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- SOL: su 40 casi simili, 24 prima sono saliti a +10,00%. Tra quei 24, 6 poi sono scaricati a -5,00%. Percentuale: +25,00% (6/24). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 85,07 $ | 25/40 | +62,50% | +5,00% | 94,03 $ | 12/25 | +48,00% | +10,53% | BASSA | 9,3 | 14,8 |
| -5,00% | 85,07 $ | 25/40 | +62,50% | +10,00% | 98,51 $ | 9/25 | +36,00% | +15,79% | BASSA | 9,3 | 14,0 |
| -5,00% | 85,07 $ | 25/40 | +62,50% | +15,00% | 102,98 $ | 5/25 | +20,00% | +21,05% | DEBOLE | 9,3 | 18,4 |
| -5,00% | 85,07 $ | 25/40 | +62,50% | +20,00% | 107,46 $ | 4/25 | +16,00% | +26,32% | DEBOLE | 9,3 | 17,5 |
| -8,00% | 82,39 $ | 20/40 | +50,00% | +5,00% | 94,03 $ | 7/20 | +35,00% | +14,13% | BASSA | 12,8 | 16,9 |
| -8,00% | 82,39 $ | 20/40 | +50,00% | +10,00% | 98,51 $ | 5/20 | +25,00% | +19,57% | DEBOLE | 12,8 | 16,2 |
| -8,00% | 82,39 $ | 20/40 | +50,00% | +15,00% | 102,98 $ | 2/20 | +10,00% | +25,00% | DEBOLE | 12,8 | 21,0 |
| -8,00% | 82,39 $ | 20/40 | +50,00% | +20,00% | 107,46 $ | 2/20 | +10,00% | +30,43% | DEBOLE | 12,8 | 21,5 |
| -10,00% | 80,60 $ | 15/40 | +37,50% | +5,00% | 94,03 $ | 1/15 | +6,67% | +16,67% | DEBOLE | 18,1 | 23,0 |
| -10,00% | 80,60 $ | 15/40 | +37,50% | +10,00% | 98,51 $ | 1/15 | +6,67% | +22,22% | DEBOLE | 18,1 | 27,0 |
| -10,00% | 80,60 $ | 15/40 | +37,50% | +15,00% | 102,98 $ | 1/15 | +6,67% | +27,78% | DEBOLE | 18,1 | 30,0 |
| -10,00% | 80,60 $ | 15/40 | +37,50% | +20,00% | 107,46 $ | 1/15 | +6,67% | +33,33% | DEBOLE | 18,1 | 30,0 |
| -15,00% | 76,12 $ | 2/40 | +5,00% | +5,00% | 94,03 $ | 0/2 | 0,00% | +23,53% | DEBOLE | 13,5 | n/d |
| -15,00% | 76,12 $ | 2/40 | +5,00% | +10,00% | 98,51 $ | 0/2 | 0,00% | +29,41% | DEBOLE | 13,5 | n/d |
| -15,00% | 76,12 $ | 2/40 | +5,00% | +15,00% | 102,98 $ | 0/2 | 0,00% | +35,29% | DEBOLE | 13,5 | n/d |
| -15,00% | 76,12 $ | 2/40 | +5,00% | +20,00% | 107,46 $ | 0/2 | 0,00% | +41,18% | DEBOLE | 13,5 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 94,03 $ | 32/40 | +80,00% | prezzo iniziale | 89,55 $ | 20/32 | +62,50% | -4,76% | MEDIA | 7,8 | 15,4 |
| +5,00% | 94,03 $ | 32/40 | +80,00% | -5,00% | 85,07 $ | 11/32 | +34,38% | -9,52% | DEBOLE | 7,8 | 16,2 |
| +5,00% | 94,03 $ | 32/40 | +80,00% | -8,00% | 82,39 $ | 7/32 | +21,88% | -12,38% | DEBOLE | 7,8 | 15,6 |
| +5,00% | 94,03 $ | 32/40 | +80,00% | -10,00% | 80,60 $ | 7/32 | +21,88% | -14,29% | DEBOLE | 7,8 | 17,1 |
| +5,00% | 94,03 $ | 32/40 | +80,00% | -15,00% | 76,12 $ | 1/32 | +3,12% | -19,05% | DEBOLE | 7,8 | 12,0 |
| +10,00% | 98,51 $ | 24/40 | +60,00% | prezzo iniziale | 89,55 $ | 11/24 | +45,83% | -9,09% | BASSA | 9,8 | 15,3 |
| +10,00% | 98,51 $ | 24/40 | +60,00% | -5,00% | 85,07 $ | 6/24 | +25,00% | -13,64% | DEBOLE | 9,8 | 13,5 |
| +10,00% | 98,51 $ | 24/40 | +60,00% | -8,00% | 82,39 $ | 5/24 | +20,83% | -16,36% | DEBOLE | 9,8 | 15,2 |
| +10,00% | 98,51 $ | 24/40 | +60,00% | -10,00% | 80,60 $ | 5/24 | +20,83% | -18,18% | DEBOLE | 9,8 | 17,0 |
| +10,00% | 98,51 $ | 24/40 | +60,00% | -15,00% | 76,12 $ | 0/24 | 0,00% | -22,73% | DEBOLE | 9,8 | n/d |
| +15,00% | 102,98 $ | 16/40 | +40,00% | prezzo iniziale | 89,55 $ | 5/16 | +31,25% | -13,04% | DEBOLE | 11,4 | 19,2 |
| +15,00% | 102,98 $ | 16/40 | +40,00% | -5,00% | 85,07 $ | 2/16 | +12,50% | -17,39% | DEBOLE | 11,4 | 11,5 |
| +15,00% | 102,98 $ | 16/40 | +40,00% | -8,00% | 82,39 $ | 2/16 | +12,50% | -20,00% | DEBOLE | 11,4 | 11,5 |
| +15,00% | 102,98 $ | 16/40 | +40,00% | -10,00% | 80,60 $ | 2/16 | +12,50% | -21,74% | DEBOLE | 11,4 | 14,0 |
| +15,00% | 102,98 $ | 16/40 | +40,00% | -15,00% | 76,12 $ | 0/16 | 0,00% | -26,09% | DEBOLE | 11,4 | n/d |
| +20,00% | 107,46 $ | 15/40 | +37,50% | prezzo iniziale | 89,55 $ | 4/15 | +26,67% | -16,67% | DEBOLE | 12,9 | 19,2 |
| +20,00% | 107,46 $ | 15/40 | +37,50% | -5,00% | 85,07 $ | 2/15 | +13,33% | -20,83% | DEBOLE | 12,9 | 11,5 |
| +20,00% | 107,46 $ | 15/40 | +37,50% | -8,00% | 82,39 $ | 2/15 | +13,33% | -23,33% | DEBOLE | 12,9 | 11,5 |
| +20,00% | 107,46 $ | 15/40 | +37,50% | -10,00% | 80,60 $ | 2/15 | +13,33% | -25,00% | DEBOLE | 12,9 | 14,0 |
| +20,00% | 107,46 $ | 15/40 | +37,50% | -15,00% | 76,12 $ | 0/15 | 0,00% | -29,17% | DEBOLE | 12,9 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 30 prima sono scesi a -5,00%. Tra quei 30, 14 poi sono rimbalzati fino a +10,00%. Percentuale: +46,67% (14/30). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- DOGE: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 7 poi sono scaricati a -5,00%. Percentuale: +25,00% (7/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,07826 $ | 30/40 | +75,00% | +5,00% | 0,08650 $ | 17/30 | +56,67% | +10,53% | MEDIA | 7,6 | 15,5 |
| -5,00% | 0,07826 $ | 30/40 | +75,00% | +10,00% | 0,09062 $ | 14/30 | +46,67% | +15,79% | BASSA | 7,6 | 15,9 |
| -5,00% | 0,07826 $ | 30/40 | +75,00% | +15,00% | 0,09474 $ | 10/30 | +33,33% | +21,05% | DEBOLE | 7,6 | 16,8 |
| -5,00% | 0,07826 $ | 30/40 | +75,00% | +20,00% | 0,09886 $ | 6/30 | +20,00% | +26,32% | DEBOLE | 7,6 | 17,2 |
| -8,00% | 0,07579 $ | 25/40 | +62,50% | +5,00% | 0,08650 $ | 10/25 | +40,00% | +14,13% | BASSA | 10,8 | 15,0 |
| -8,00% | 0,07579 $ | 25/40 | +62,50% | +10,00% | 0,09062 $ | 10/25 | +40,00% | +19,57% | BASSA | 10,8 | 16,5 |
| -8,00% | 0,07579 $ | 25/40 | +62,50% | +15,00% | 0,09474 $ | 8/25 | +32,00% | +25,00% | DEBOLE | 10,8 | 16,9 |
| -8,00% | 0,07579 $ | 25/40 | +62,50% | +20,00% | 0,09886 $ | 5/25 | +20,00% | +30,43% | DEBOLE | 10,8 | 17,4 |
| -10,00% | 0,07414 $ | 23/40 | +57,50% | +5,00% | 0,08650 $ | 7/23 | +30,43% | +16,67% | DEBOLE | 13,0 | 14,3 |
| -10,00% | 0,07414 $ | 23/40 | +57,50% | +10,00% | 0,09062 $ | 7/23 | +30,43% | +22,22% | DEBOLE | 13,0 | 16,1 |
| -10,00% | 0,07414 $ | 23/40 | +57,50% | +15,00% | 0,09474 $ | 5/23 | +21,74% | +27,78% | DEBOLE | 13,0 | 16,0 |
| -10,00% | 0,07414 $ | 23/40 | +57,50% | +20,00% | 0,09886 $ | 4/23 | +17,39% | +33,33% | DEBOLE | 13,0 | 17,5 |
| -15,00% | 0,07002 $ | 15/40 | +37,50% | +5,00% | 0,08650 $ | 3/15 | +20,00% | +23,53% | DEBOLE | 14,9 | 18,3 |
| -15,00% | 0,07002 $ | 15/40 | +37,50% | +10,00% | 0,09062 $ | 3/15 | +20,00% | +29,41% | DEBOLE | 14,9 | 18,7 |
| -15,00% | 0,07002 $ | 15/40 | +37,50% | +15,00% | 0,09474 $ | 2/15 | +13,33% | +35,29% | DEBOLE | 14,9 | 15,0 |
| -15,00% | 0,07002 $ | 15/40 | +37,50% | +20,00% | 0,09886 $ | 2/15 | +13,33% | +41,18% | DEBOLE | 14,9 | 15,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,08650 $ | 31/40 | +77,50% | prezzo iniziale | 0,08238 $ | 15/31 | +48,39% | -4,76% | BASSA | 8,1 | 14,5 |
| +5,00% | 0,08650 $ | 31/40 | +77,50% | -5,00% | 0,07826 $ | 12/31 | +38,71% | -9,52% | BASSA | 8,1 | 17,3 |
| +5,00% | 0,08650 $ | 31/40 | +77,50% | -8,00% | 0,07579 $ | 8/31 | +25,81% | -12,38% | DEBOLE | 8,1 | 21,4 |
| +5,00% | 0,08650 $ | 31/40 | +77,50% | -10,00% | 0,07414 $ | 7/31 | +22,58% | -14,29% | DEBOLE | 8,1 | 24,4 |
| +5,00% | 0,08650 $ | 31/40 | +77,50% | -15,00% | 0,07002 $ | 3/31 | +9,68% | -19,05% | DEBOLE | 8,1 | 26,7 |
| +10,00% | 0,09062 $ | 28/40 | +70,00% | prezzo iniziale | 0,08238 $ | 10/28 | +35,71% | -9,09% | BASSA | 11,0 | 18,7 |
| +10,00% | 0,09062 $ | 28/40 | +70,00% | -5,00% | 0,07826 $ | 7/28 | +25,00% | -13,64% | DEBOLE | 11,0 | 19,3 |
| +10,00% | 0,09062 $ | 28/40 | +70,00% | -8,00% | 0,07579 $ | 6/28 | +21,43% | -16,36% | DEBOLE | 11,0 | 22,8 |
| +10,00% | 0,09062 $ | 28/40 | +70,00% | -10,00% | 0,07414 $ | 5/28 | +17,86% | -18,18% | DEBOLE | 11,0 | 25,0 |
| +10,00% | 0,09062 $ | 28/40 | +70,00% | -15,00% | 0,07002 $ | 2/28 | +7,14% | -22,73% | DEBOLE | 11,0 | 29,0 |
| +15,00% | 0,09474 $ | 23/40 | +57,50% | prezzo iniziale | 0,08238 $ | 7/23 | +30,43% | -13,04% | DEBOLE | 12,4 | 23,6 |
| +15,00% | 0,09474 $ | 23/40 | +57,50% | -5,00% | 0,07826 $ | 4/23 | +17,39% | -17,39% | DEBOLE | 12,4 | 21,0 |
| +15,00% | 0,09474 $ | 23/40 | +57,50% | -8,00% | 0,07579 $ | 3/23 | +13,04% | -20,00% | DEBOLE | 12,4 | 24,7 |
| +15,00% | 0,09474 $ | 23/40 | +57,50% | -10,00% | 0,07414 $ | 3/23 | +13,04% | -21,74% | DEBOLE | 12,4 | 25,3 |
| +15,00% | 0,09474 $ | 23/40 | +57,50% | -15,00% | 0,07002 $ | 2/23 | +8,70% | -26,09% | DEBOLE | 12,4 | 29,0 |
| +20,00% | 0,09886 $ | 16/40 | +40,00% | prezzo iniziale | 0,08238 $ | 2/16 | +12,50% | -16,67% | DEBOLE | 13,0 | 25,5 |
| +20,00% | 0,09886 $ | 16/40 | +40,00% | -5,00% | 0,07826 $ | 1/16 | +6,25% | -20,83% | DEBOLE | 13,0 | 23,0 |
| +20,00% | 0,09886 $ | 16/40 | +40,00% | -8,00% | 0,07579 $ | 0/16 | 0,00% | -23,33% | DEBOLE | 13,0 | n/d |
| +20,00% | 0,09886 $ | 16/40 | +40,00% | -10,00% | 0,07414 $ | 0/16 | 0,00% | -25,00% | DEBOLE | 13,0 | n/d |
| +20,00% | 0,09886 $ | 16/40 | +40,00% | -15,00% | 0,07002 $ | 0/16 | 0,00% | -29,17% | DEBOLE | 13,0 | n/d |

---
