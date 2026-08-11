# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-08-11 07:20:55 CEST**  
UTC: **2026-08-11 05:20:55 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 60.778 $ | 70.374 $ | +53,33% | +15,79% | rimbalzo possibile | 70.374 $ | 60.778 $ | +3,33% | -13,64% | spike storicamente più resistente |
| SOL | 72,18 $ | 83,58 $ | +50,00% | +15,79% | rimbalzo possibile | 83,58 $ | 72,18 $ | 0,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06650 $ | 0,07700 $ | +65,52% | +15,79% | buona zona storica di rimbalzo | 0,07700 $ | 0,06650 $ | +12,90% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 15 prima sono scesi a -5,00%. Tra quei 15, 8 poi sono rimbalzati fino a +10,00%. Percentuale: +53,33% (8/15). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.
- BTC: su 40 casi simili, 30 prima sono saliti a +10,00%. Tra quei 30, 1 poi sono scaricati a -5,00%. Percentuale: +3,33% (1/30). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 60.778 $ | 15/40 | +37,50% | +5,00% | 67.175 $ | 9/15 | +60,00% | +10,53% | MEDIA | 6,8 | 18,1 |
| -5,00% | 60.778 $ | 15/40 | +37,50% | +10,00% | 70.374 $ | 8/15 | +53,33% | +15,79% | MEDIA | 6,8 | 19,6 |
| -5,00% | 60.778 $ | 15/40 | +37,50% | +15,00% | 73.573 $ | 5/15 | +33,33% | +21,05% | DEBOLE | 6,8 | 20,0 |
| -5,00% | 60.778 $ | 15/40 | +37,50% | +20,00% | 76.772 $ | 4/15 | +26,67% | +26,32% | DEBOLE | 6,8 | 19,0 |
| -8,00% | 58.858 $ | 13/40 | +32,50% | +5,00% | 67.175 $ | 7/13 | +53,85% | +14,13% | MEDIA | 9,6 | 18,6 |
| -8,00% | 58.858 $ | 13/40 | +32,50% | +10,00% | 70.374 $ | 6/13 | +46,15% | +19,57% | BASSA | 9,6 | 20,2 |
| -8,00% | 58.858 $ | 13/40 | +32,50% | +15,00% | 73.573 $ | 4/13 | +30,77% | +25,00% | DEBOLE | 9,6 | 20,2 |
| -8,00% | 58.858 $ | 13/40 | +32,50% | +20,00% | 76.772 $ | 3/13 | +23,08% | +30,43% | DEBOLE | 9,6 | 18,7 |
| -10,00% | 57.579 $ | 12/40 | +30,00% | +5,00% | 67.175 $ | 6/12 | +50,00% | +16,67% | MEDIA | 11,2 | 19,2 |
| -10,00% | 57.579 $ | 12/40 | +30,00% | +10,00% | 70.374 $ | 5/12 | +41,67% | +22,22% | BASSA | 11,2 | 20,6 |
| -10,00% | 57.579 $ | 12/40 | +30,00% | +15,00% | 73.573 $ | 3/12 | +25,00% | +27,78% | DEBOLE | 11,2 | 19,3 |
| -10,00% | 57.579 $ | 12/40 | +30,00% | +20,00% | 76.772 $ | 2/12 | +16,67% | +33,33% | DEBOLE | 11,2 | 15,5 |
| -15,00% | 54.380 $ | 6/40 | +15,00% | +5,00% | 67.175 $ | 1/6 | +16,67% | +23,53% | DEBOLE | 16,2 | 23,0 |
| -15,00% | 54.380 $ | 6/40 | +15,00% | +10,00% | 70.374 $ | 0/6 | 0,00% | +29,41% | DEBOLE | 16,2 | n/d |
| -15,00% | 54.380 $ | 6/40 | +15,00% | +15,00% | 73.573 $ | 0/6 | 0,00% | +35,29% | DEBOLE | 16,2 | n/d |
| -15,00% | 54.380 $ | 6/40 | +15,00% | +20,00% | 76.772 $ | 0/6 | 0,00% | +41,18% | DEBOLE | 16,2 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 67.175 $ | 36/40 | +90,00% | prezzo iniziale | 63.976 $ | 7/36 | +19,44% | -4,76% | DEBOLE | 9,1 | 15,9 |
| +5,00% | 67.175 $ | 36/40 | +90,00% | -5,00% | 60.778 $ | 3/36 | +8,33% | -9,52% | DEBOLE | 9,1 | 18,7 |
| +5,00% | 67.175 $ | 36/40 | +90,00% | -8,00% | 58.858 $ | 3/36 | +8,33% | -12,38% | DEBOLE | 9,1 | 19,3 |
| +5,00% | 67.175 $ | 36/40 | +90,00% | -10,00% | 57.579 $ | 3/36 | +8,33% | -14,29% | DEBOLE | 9,1 | 20,3 |
| +5,00% | 67.175 $ | 36/40 | +90,00% | -15,00% | 54.380 $ | 1/36 | +2,78% | -19,05% | DEBOLE | 9,1 | 27,0 |
| +10,00% | 70.374 $ | 30/40 | +75,00% | prezzo iniziale | 63.976 $ | 2/30 | +6,67% | -9,09% | DEBOLE | 14,1 | 20,5 |
| +10,00% | 70.374 $ | 30/40 | +75,00% | -5,00% | 60.778 $ | 1/30 | +3,33% | -13,64% | DEBOLE | 14,1 | 19,0 |
| +10,00% | 70.374 $ | 30/40 | +75,00% | -8,00% | 58.858 $ | 1/30 | +3,33% | -16,36% | DEBOLE | 14,1 | 21,0 |
| +10,00% | 70.374 $ | 30/40 | +75,00% | -10,00% | 57.579 $ | 1/30 | +3,33% | -18,18% | DEBOLE | 14,1 | 22,0 |
| +10,00% | 70.374 $ | 30/40 | +75,00% | -15,00% | 54.380 $ | 0/30 | 0,00% | -22,73% | DEBOLE | 14,1 | n/d |
| +15,00% | 73.573 $ | 22/40 | +55,00% | prezzo iniziale | 63.976 $ | 0/22 | 0,00% | -13,04% | DEBOLE | 15,0 | n/d |
| +15,00% | 73.573 $ | 22/40 | +55,00% | -5,00% | 60.778 $ | 0/22 | 0,00% | -17,39% | DEBOLE | 15,0 | n/d |
| +15,00% | 73.573 $ | 22/40 | +55,00% | -8,00% | 58.858 $ | 0/22 | 0,00% | -20,00% | DEBOLE | 15,0 | n/d |
| +15,00% | 73.573 $ | 22/40 | +55,00% | -10,00% | 57.579 $ | 0/22 | 0,00% | -21,74% | DEBOLE | 15,0 | n/d |
| +15,00% | 73.573 $ | 22/40 | +55,00% | -15,00% | 54.380 $ | 0/22 | 0,00% | -26,09% | DEBOLE | 15,0 | n/d |
| +20,00% | 76.772 $ | 16/40 | +40,00% | prezzo iniziale | 63.976 $ | 0/16 | 0,00% | -16,67% | DEBOLE | 14,0 | n/d |
| +20,00% | 76.772 $ | 16/40 | +40,00% | -5,00% | 60.778 $ | 0/16 | 0,00% | -20,83% | DEBOLE | 14,0 | n/d |
| +20,00% | 76.772 $ | 16/40 | +40,00% | -8,00% | 58.858 $ | 0/16 | 0,00% | -23,33% | DEBOLE | 14,0 | n/d |
| +20,00% | 76.772 $ | 16/40 | +40,00% | -10,00% | 57.579 $ | 0/16 | 0,00% | -25,00% | DEBOLE | 14,0 | n/d |
| +20,00% | 76.772 $ | 16/40 | +40,00% | -15,00% | 54.380 $ | 0/16 | 0,00% | -29,17% | DEBOLE | 14,0 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 18 prima sono scesi a -5,00%. Tra quei 18, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +50,00% (9/18). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.
- SOL: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 0 poi sono scaricati a -5,00%. Percentuale: 0,00% (0/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 72,18 $ | 18/40 | +45,00% | +5,00% | 79,78 $ | 10/18 | +55,56% | +10,53% | MEDIA | 8,1 | 18,9 |
| -5,00% | 72,18 $ | 18/40 | +45,00% | +10,00% | 83,58 $ | 9/18 | +50,00% | +15,79% | MEDIA | 8,1 | 21,3 |
| -5,00% | 72,18 $ | 18/40 | +45,00% | +15,00% | 87,38 $ | 7/18 | +38,89% | +21,05% | BASSA | 8,1 | 22,4 |
| -5,00% | 72,18 $ | 18/40 | +45,00% | +20,00% | 91,18 $ | 5/18 | +27,78% | +26,32% | DEBOLE | 8,1 | 25,0 |
| -8,00% | 69,90 $ | 12/40 | +30,00% | +5,00% | 79,78 $ | 5/12 | +41,67% | +14,13% | BASSA | 9,6 | 21,4 |
| -8,00% | 69,90 $ | 12/40 | +30,00% | +10,00% | 83,58 $ | 4/12 | +33,33% | +19,57% | DEBOLE | 9,6 | 23,5 |
| -8,00% | 69,90 $ | 12/40 | +30,00% | +15,00% | 87,38 $ | 3/12 | +25,00% | +25,00% | DEBOLE | 9,6 | 23,3 |
| -8,00% | 69,90 $ | 12/40 | +30,00% | +20,00% | 91,18 $ | 3/12 | +25,00% | +30,43% | DEBOLE | 9,6 | 25,0 |
| -10,00% | 68,38 $ | 11/40 | +27,50% | +5,00% | 79,78 $ | 5/11 | +45,45% | +16,67% | BASSA | 11,1 | 21,4 |
| -10,00% | 68,38 $ | 11/40 | +27,50% | +10,00% | 83,58 $ | 4/11 | +36,36% | +22,22% | BASSA | 11,1 | 23,5 |
| -10,00% | 68,38 $ | 11/40 | +27,50% | +15,00% | 87,38 $ | 3/11 | +27,27% | +27,78% | DEBOLE | 11,1 | 23,3 |
| -10,00% | 68,38 $ | 11/40 | +27,50% | +20,00% | 91,18 $ | 3/11 | +27,27% | +33,33% | DEBOLE | 11,1 | 25,0 |
| -15,00% | 64,58 $ | 6/40 | +15,00% | +5,00% | 79,78 $ | 2/6 | +33,33% | +23,53% | DEBOLE | 13,7 | 20,5 |
| -15,00% | 64,58 $ | 6/40 | +15,00% | +10,00% | 83,58 $ | 2/6 | +33,33% | +29,41% | DEBOLE | 13,7 | 28,5 |
| -15,00% | 64,58 $ | 6/40 | +15,00% | +15,00% | 87,38 $ | 1/6 | +16,67% | +35,29% | DEBOLE | 13,7 | 27,0 |
| -15,00% | 64,58 $ | 6/40 | +15,00% | +20,00% | 91,18 $ | 1/6 | +16,67% | +41,18% | DEBOLE | 13,7 | 30,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 79,78 $ | 33/40 | +82,50% | prezzo iniziale | 75,98 $ | 10/33 | +30,30% | -4,76% | DEBOLE | 9,6 | 17,2 |
| +5,00% | 79,78 $ | 33/40 | +82,50% | -5,00% | 72,18 $ | 3/33 | +9,09% | -9,52% | DEBOLE | 9,6 | 20,7 |
| +5,00% | 79,78 $ | 33/40 | +82,50% | -8,00% | 69,90 $ | 1/33 | +3,03% | -12,38% | DEBOLE | 9,6 | 10,0 |
| +5,00% | 79,78 $ | 33/40 | +82,50% | -10,00% | 68,38 $ | 1/33 | +3,03% | -14,29% | DEBOLE | 9,6 | 14,0 |
| +5,00% | 79,78 $ | 33/40 | +82,50% | -15,00% | 64,58 $ | 0/33 | 0,00% | -19,05% | DEBOLE | 9,6 | n/d |
| +10,00% | 83,58 $ | 28/40 | +70,00% | prezzo iniziale | 75,98 $ | 2/28 | +7,14% | -9,09% | DEBOLE | 15,4 | 25,5 |
| +10,00% | 83,58 $ | 28/40 | +70,00% | -5,00% | 72,18 $ | 0/28 | 0,00% | -13,64% | DEBOLE | 15,4 | n/d |
| +10,00% | 83,58 $ | 28/40 | +70,00% | -8,00% | 69,90 $ | 0/28 | 0,00% | -16,36% | DEBOLE | 15,4 | n/d |
| +10,00% | 83,58 $ | 28/40 | +70,00% | -10,00% | 68,38 $ | 0/28 | 0,00% | -18,18% | DEBOLE | 15,4 | n/d |
| +10,00% | 83,58 $ | 28/40 | +70,00% | -15,00% | 64,58 $ | 0/28 | 0,00% | -22,73% | DEBOLE | 15,4 | n/d |
| +15,00% | 87,38 $ | 22/40 | +55,00% | prezzo iniziale | 75,98 $ | 1/22 | +4,55% | -13,04% | DEBOLE | 15,5 | 29,0 |
| +15,00% | 87,38 $ | 22/40 | +55,00% | -5,00% | 72,18 $ | 0/22 | 0,00% | -17,39% | DEBOLE | 15,5 | n/d |
| +15,00% | 87,38 $ | 22/40 | +55,00% | -8,00% | 69,90 $ | 0/22 | 0,00% | -20,00% | DEBOLE | 15,5 | n/d |
| +15,00% | 87,38 $ | 22/40 | +55,00% | -10,00% | 68,38 $ | 0/22 | 0,00% | -21,74% | DEBOLE | 15,5 | n/d |
| +15,00% | 87,38 $ | 22/40 | +55,00% | -15,00% | 64,58 $ | 0/22 | 0,00% | -26,09% | DEBOLE | 15,5 | n/d |
| +20,00% | 91,18 $ | 16/40 | +40,00% | prezzo iniziale | 75,98 $ | 0/16 | 0,00% | -16,67% | DEBOLE | 16,7 | n/d |
| +20,00% | 91,18 $ | 16/40 | +40,00% | -5,00% | 72,18 $ | 0/16 | 0,00% | -20,83% | DEBOLE | 16,7 | n/d |
| +20,00% | 91,18 $ | 16/40 | +40,00% | -8,00% | 69,90 $ | 0/16 | 0,00% | -23,33% | DEBOLE | 16,7 | n/d |
| +20,00% | 91,18 $ | 16/40 | +40,00% | -10,00% | 68,38 $ | 0/16 | 0,00% | -25,00% | DEBOLE | 16,7 | n/d |
| +20,00% | 91,18 $ | 16/40 | +40,00% | -15,00% | 64,58 $ | 0/16 | 0,00% | -29,17% | DEBOLE | 16,7 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 29 prima sono scesi a -5,00%. Tra quei 29, 19 poi sono rimbalzati fino a +10,00%. Percentuale: +65,52% (19/29). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: buona zona storica di rimbalzo.
- DOGE: su 40 casi simili, 31 prima sono saliti a +10,00%. Tra quei 31, 4 poi sono scaricati a -5,00%. Percentuale: +12,90% (4/31). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06650 $ | 29/40 | +72,50% | +5,00% | 0,07350 $ | 19/29 | +65,52% | +10,53% | ALTA | 7,0 | 15,2 |
| -5,00% | 0,06650 $ | 29/40 | +72,50% | +10,00% | 0,07700 $ | 19/29 | +65,52% | +15,79% | ALTA | 7,0 | 17,2 |
| -5,00% | 0,06650 $ | 29/40 | +72,50% | +15,00% | 0,08050 $ | 17/29 | +58,62% | +21,05% | MEDIA | 7,0 | 20,2 |
| -5,00% | 0,06650 $ | 29/40 | +72,50% | +20,00% | 0,08400 $ | 14/29 | +48,28% | +26,32% | BASSA | 7,0 | 22,1 |
| -8,00% | 0,06440 $ | 22/40 | +55,00% | +5,00% | 0,07350 $ | 12/22 | +54,55% | +14,13% | MEDIA | 8,5 | 17,2 |
| -8,00% | 0,06440 $ | 22/40 | +55,00% | +10,00% | 0,07700 $ | 12/22 | +54,55% | +19,57% | MEDIA | 8,5 | 19,0 |
| -8,00% | 0,06440 $ | 22/40 | +55,00% | +15,00% | 0,08050 $ | 10/22 | +45,45% | +25,00% | BASSA | 8,5 | 23,3 |
| -8,00% | 0,06440 $ | 22/40 | +55,00% | +20,00% | 0,08400 $ | 7/22 | +31,82% | +30,43% | DEBOLE | 8,5 | 25,0 |
| -10,00% | 0,06300 $ | 18/40 | +45,00% | +5,00% | 0,07350 $ | 8/18 | +44,44% | +16,67% | BASSA | 8,1 | 17,8 |
| -10,00% | 0,06300 $ | 18/40 | +45,00% | +10,00% | 0,07700 $ | 8/18 | +44,44% | +22,22% | BASSA | 8,1 | 20,1 |
| -10,00% | 0,06300 $ | 18/40 | +45,00% | +15,00% | 0,08050 $ | 7/18 | +38,89% | +27,78% | BASSA | 8,1 | 24,6 |
| -10,00% | 0,06300 $ | 18/40 | +45,00% | +20,00% | 0,08400 $ | 4/18 | +22,22% | +33,33% | DEBOLE | 8,1 | 28,2 |
| -15,00% | 0,05950 $ | 11/40 | +27,50% | +5,00% | 0,07350 $ | 2/11 | +18,18% | +23,53% | DEBOLE | 7,5 | 15,5 |
| -15,00% | 0,05950 $ | 11/40 | +27,50% | +10,00% | 0,07700 $ | 2/11 | +18,18% | +29,41% | DEBOLE | 7,5 | 16,5 |
| -15,00% | 0,05950 $ | 11/40 | +27,50% | +15,00% | 0,08050 $ | 2/11 | +18,18% | +35,29% | DEBOLE | 7,5 | 20,0 |
| -15,00% | 0,05950 $ | 11/40 | +27,50% | +20,00% | 0,08400 $ | 1/11 | +9,09% | +41,18% | DEBOLE | 7,5 | 27,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07350 $ | 33/40 | +82,50% | prezzo iniziale | 0,07000 $ | 19/33 | +57,58% | -4,76% | MEDIA | 8,9 | 13,7 |
| +5,00% | 0,07350 $ | 33/40 | +82,50% | -5,00% | 0,06650 $ | 11/33 | +33,33% | -9,52% | DEBOLE | 8,9 | 15,6 |
| +5,00% | 0,07350 $ | 33/40 | +82,50% | -8,00% | 0,06440 $ | 6/33 | +18,18% | -12,38% | DEBOLE | 8,9 | 14,2 |
| +5,00% | 0,07350 $ | 33/40 | +82,50% | -10,00% | 0,06300 $ | 5/33 | +15,15% | -14,29% | DEBOLE | 8,9 | 14,8 |
| +5,00% | 0,07350 $ | 33/40 | +82,50% | -15,00% | 0,05950 $ | 2/33 | +6,06% | -19,05% | DEBOLE | 8,9 | 15,5 |
| +10,00% | 0,07700 $ | 31/40 | +77,50% | prezzo iniziale | 0,07000 $ | 11/31 | +35,48% | -9,09% | BASSA | 13,9 | 18,7 |
| +10,00% | 0,07700 $ | 31/40 | +77,50% | -5,00% | 0,06650 $ | 4/31 | +12,90% | -13,64% | DEBOLE | 13,9 | 18,2 |
| +10,00% | 0,07700 $ | 31/40 | +77,50% | -8,00% | 0,06440 $ | 1/31 | +3,23% | -16,36% | DEBOLE | 13,9 | 21,0 |
| +10,00% | 0,07700 $ | 31/40 | +77,50% | -10,00% | 0,06300 $ | 1/31 | +3,23% | -18,18% | DEBOLE | 13,9 | 23,0 |
| +10,00% | 0,07700 $ | 31/40 | +77,50% | -15,00% | 0,05950 $ | 0/31 | 0,00% | -22,73% | DEBOLE | 13,9 | n/d |
| +15,00% | 0,08050 $ | 28/40 | +70,00% | prezzo iniziale | 0,07000 $ | 4/28 | +14,29% | -13,04% | DEBOLE | 17,9 | 20,8 |
| +15,00% | 0,08050 $ | 28/40 | +70,00% | -5,00% | 0,06650 $ | 1/28 | +3,57% | -17,39% | DEBOLE | 17,9 | 26,0 |
| +15,00% | 0,08050 $ | 28/40 | +70,00% | -8,00% | 0,06440 $ | 0/28 | 0,00% | -20,00% | DEBOLE | 17,9 | n/d |
| +15,00% | 0,08050 $ | 28/40 | +70,00% | -10,00% | 0,06300 $ | 0/28 | 0,00% | -21,74% | DEBOLE | 17,9 | n/d |
| +15,00% | 0,08050 $ | 28/40 | +70,00% | -15,00% | 0,05950 $ | 0/28 | 0,00% | -26,09% | DEBOLE | 17,9 | n/d |
| +20,00% | 0,08400 $ | 24/40 | +60,00% | prezzo iniziale | 0,07000 $ | 2/24 | +8,33% | -16,67% | DEBOLE | 21,0 | 20,5 |
| +20,00% | 0,08400 $ | 24/40 | +60,00% | -5,00% | 0,06650 $ | 0/24 | 0,00% | -20,83% | DEBOLE | 21,0 | n/d |
| +20,00% | 0,08400 $ | 24/40 | +60,00% | -8,00% | 0,06440 $ | 0/24 | 0,00% | -23,33% | DEBOLE | 21,0 | n/d |
| +20,00% | 0,08400 $ | 24/40 | +60,00% | -10,00% | 0,06300 $ | 0/24 | 0,00% | -25,00% | DEBOLE | 21,0 | n/d |
| +20,00% | 0,08400 $ | 24/40 | +60,00% | -15,00% | 0,05950 $ | 0/24 | 0,00% | -29,17% | DEBOLE | 21,0 | n/d |

---
