# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-08-09 07:15:18 CEST**  
UTC: **2026-08-09 05:15:18 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 61.491 $ | 71.200 $ | +45,45% | +15,79% | rimbalzo debole | 71.200 $ | 61.491 $ | +3,45% | -13,64% | spike storicamente più resistente |
| SOL | 72,15 $ | 83,54 $ | +42,86% | +15,79% | rimbalzo debole | 83,54 $ | 72,15 $ | +3,33% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06647 $ | 0,07697 $ | +60,71% | +15,79% | rimbalzo possibile | 0,07697 $ | 0,06647 $ | +3,45% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 11 prima sono scesi a -5,00%. Tra quei 11, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +45,45% (5/11). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 29 prima sono saliti a +10,00%. Tra quei 29, 1 poi sono scaricati a -5,00%. Percentuale: +3,45% (1/29). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 61.491 $ | 11/40 | +27,50% | +5,00% | 67.964 $ | 7/11 | +63,64% | +10,53% | MEDIA | 8,1 | 23,0 |
| -5,00% | 61.491 $ | 11/40 | +27,50% | +10,00% | 71.200 $ | 5/11 | +45,45% | +15,79% | BASSA | 8,1 | 23,8 |
| -5,00% | 61.491 $ | 11/40 | +27,50% | +15,00% | 74.437 $ | 4/11 | +36,36% | +21,05% | BASSA | 8,1 | 28,0 |
| -5,00% | 61.491 $ | 11/40 | +27,50% | +20,00% | 77.673 $ | 1/11 | +9,09% | +26,32% | DEBOLE | 8,1 | 25,0 |
| -8,00% | 59.549 $ | 9/40 | +22,50% | +5,00% | 67.964 $ | 5/9 | +55,56% | +14,13% | MEDIA | 9,9 | 21,4 |
| -8,00% | 59.549 $ | 9/40 | +22,50% | +10,00% | 71.200 $ | 4/9 | +44,44% | +19,57% | BASSA | 9,9 | 23,0 |
| -8,00% | 59.549 $ | 9/40 | +22,50% | +15,00% | 74.437 $ | 3/9 | +33,33% | +25,00% | DEBOLE | 9,9 | 27,3 |
| -8,00% | 59.549 $ | 9/40 | +22,50% | +20,00% | 77.673 $ | 1/9 | +11,11% | +30,43% | DEBOLE | 9,9 | 25,0 |
| -10,00% | 58.255 $ | 8/40 | +20,00% | +5,00% | 67.964 $ | 4/8 | +50,00% | +16,67% | MEDIA | 11,2 | 23,0 |
| -10,00% | 58.255 $ | 8/40 | +20,00% | +10,00% | 71.200 $ | 3/8 | +37,50% | +22,22% | BASSA | 11,2 | 24,7 |
| -10,00% | 58.255 $ | 8/40 | +20,00% | +15,00% | 74.437 $ | 2/8 | +25,00% | +27,78% | DEBOLE | 11,2 | 29,5 |
| -10,00% | 58.255 $ | 8/40 | +20,00% | +20,00% | 77.673 $ | 0/8 | 0,00% | +33,33% | DEBOLE | 11,2 | n/d |
| -15,00% | 55.018 $ | 5/40 | +12,50% | +5,00% | 67.964 $ | 2/5 | +40,00% | +23,53% | BASSA | 15,0 | 22,5 |
| -15,00% | 55.018 $ | 5/40 | +12,50% | +10,00% | 71.200 $ | 1/5 | +20,00% | +29,41% | DEBOLE | 15,0 | 23,0 |
| -15,00% | 55.018 $ | 5/40 | +12,50% | +15,00% | 74.437 $ | 1/5 | +20,00% | +35,29% | DEBOLE | 15,0 | 30,0 |
| -15,00% | 55.018 $ | 5/40 | +12,50% | +20,00% | 77.673 $ | 0/5 | 0,00% | +41,18% | DEBOLE | 15,0 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 67.964 $ | 35/40 | +87,50% | prezzo iniziale | 64.728 $ | 5/35 | +14,29% | -4,76% | DEBOLE | 8,5 | 16,6 |
| +5,00% | 67.964 $ | 35/40 | +87,50% | -5,00% | 61.491 $ | 2/35 | +5,71% | -9,52% | DEBOLE | 8,5 | 17,0 |
| +5,00% | 67.964 $ | 35/40 | +87,50% | -8,00% | 59.549 $ | 2/35 | +5,71% | -12,38% | DEBOLE | 8,5 | 18,0 |
| +5,00% | 67.964 $ | 35/40 | +87,50% | -10,00% | 58.255 $ | 2/35 | +5,71% | -14,29% | DEBOLE | 8,5 | 19,5 |
| +5,00% | 67.964 $ | 35/40 | +87,50% | -15,00% | 55.018 $ | 0/35 | 0,00% | -19,05% | DEBOLE | 8,5 | n/d |
| +10,00% | 71.200 $ | 29/40 | +72,50% | prezzo iniziale | 64.728 $ | 2/29 | +6,90% | -9,09% | DEBOLE | 13,0 | 19,0 |
| +10,00% | 71.200 $ | 29/40 | +72,50% | -5,00% | 61.491 $ | 1/29 | +3,45% | -13,64% | DEBOLE | 13,0 | 19,0 |
| +10,00% | 71.200 $ | 29/40 | +72,50% | -8,00% | 59.549 $ | 1/29 | +3,45% | -16,36% | DEBOLE | 13,0 | 21,0 |
| +10,00% | 71.200 $ | 29/40 | +72,50% | -10,00% | 58.255 $ | 1/29 | +3,45% | -18,18% | DEBOLE | 13,0 | 22,0 |
| +10,00% | 71.200 $ | 29/40 | +72,50% | -15,00% | 55.018 $ | 0/29 | 0,00% | -22,73% | DEBOLE | 13,0 | n/d |
| +15,00% | 74.437 $ | 25/40 | +62,50% | prezzo iniziale | 64.728 $ | 1/25 | +4,00% | -13,04% | DEBOLE | 16,2 | 26,0 |
| +15,00% | 74.437 $ | 25/40 | +62,50% | -5,00% | 61.491 $ | 0/25 | 0,00% | -17,39% | DEBOLE | 16,2 | n/d |
| +15,00% | 74.437 $ | 25/40 | +62,50% | -8,00% | 59.549 $ | 0/25 | 0,00% | -20,00% | DEBOLE | 16,2 | n/d |
| +15,00% | 74.437 $ | 25/40 | +62,50% | -10,00% | 58.255 $ | 0/25 | 0,00% | -21,74% | DEBOLE | 16,2 | n/d |
| +15,00% | 74.437 $ | 25/40 | +62,50% | -15,00% | 55.018 $ | 0/25 | 0,00% | -26,09% | DEBOLE | 16,2 | n/d |
| +20,00% | 77.673 $ | 17/40 | +42,50% | prezzo iniziale | 64.728 $ | 1/17 | +5,88% | -16,67% | DEBOLE | 14,5 | 26,0 |
| +20,00% | 77.673 $ | 17/40 | +42,50% | -5,00% | 61.491 $ | 0/17 | 0,00% | -20,83% | DEBOLE | 14,5 | n/d |
| +20,00% | 77.673 $ | 17/40 | +42,50% | -8,00% | 59.549 $ | 0/17 | 0,00% | -23,33% | DEBOLE | 14,5 | n/d |
| +20,00% | 77.673 $ | 17/40 | +42,50% | -10,00% | 58.255 $ | 0/17 | 0,00% | -25,00% | DEBOLE | 14,5 | n/d |
| +20,00% | 77.673 $ | 17/40 | +42,50% | -15,00% | 55.018 $ | 0/17 | 0,00% | -29,17% | DEBOLE | 14,5 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 14 prima sono scesi a -5,00%. Tra quei 14, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +42,86% (6/14). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- SOL: su 40 casi simili, 30 prima sono saliti a +10,00%. Tra quei 30, 1 poi sono scaricati a -5,00%. Percentuale: +3,33% (1/30). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 72,15 $ | 14/40 | +35,00% | +5,00% | 79,75 $ | 8/14 | +57,14% | +10,53% | MEDIA | 7,0 | 22,2 |
| -5,00% | 72,15 $ | 14/40 | +35,00% | +10,00% | 83,54 $ | 6/14 | +42,86% | +15,79% | BASSA | 7,0 | 21,8 |
| -5,00% | 72,15 $ | 14/40 | +35,00% | +15,00% | 87,34 $ | 6/14 | +42,86% | +21,05% | BASSA | 7,0 | 23,0 |
| -5,00% | 72,15 $ | 14/40 | +35,00% | +20,00% | 91,14 $ | 4/14 | +28,57% | +26,32% | DEBOLE | 7,0 | 22,0 |
| -8,00% | 69,87 $ | 13/40 | +32,50% | +5,00% | 79,75 $ | 7/13 | +53,85% | +14,13% | MEDIA | 9,8 | 21,6 |
| -8,00% | 69,87 $ | 13/40 | +32,50% | +10,00% | 83,54 $ | 5/13 | +38,46% | +19,57% | BASSA | 9,8 | 20,4 |
| -8,00% | 69,87 $ | 13/40 | +32,50% | +15,00% | 87,34 $ | 5/13 | +38,46% | +25,00% | BASSA | 9,8 | 21,8 |
| -8,00% | 69,87 $ | 13/40 | +32,50% | +20,00% | 91,14 $ | 4/13 | +30,77% | +30,43% | DEBOLE | 9,8 | 22,0 |
| -10,00% | 68,35 $ | 12/40 | +30,00% | +5,00% | 79,75 $ | 7/12 | +58,33% | +16,67% | MEDIA | 8,9 | 21,6 |
| -10,00% | 68,35 $ | 12/40 | +30,00% | +10,00% | 83,54 $ | 5/12 | +41,67% | +22,22% | BASSA | 8,9 | 20,4 |
| -10,00% | 68,35 $ | 12/40 | +30,00% | +15,00% | 87,34 $ | 5/12 | +41,67% | +27,78% | BASSA | 8,9 | 21,8 |
| -10,00% | 68,35 $ | 12/40 | +30,00% | +20,00% | 91,14 $ | 4/12 | +33,33% | +33,33% | DEBOLE | 8,9 | 22,0 |
| -15,00% | 64,56 $ | 6/40 | +15,00% | +5,00% | 79,75 $ | 3/6 | +50,00% | +23,53% | MEDIA | 13,0 | 25,3 |
| -15,00% | 64,56 $ | 6/40 | +15,00% | +10,00% | 83,54 $ | 2/6 | +33,33% | +29,41% | DEBOLE | 13,0 | 27,5 |
| -15,00% | 64,56 $ | 6/40 | +15,00% | +15,00% | 87,34 $ | 2/6 | +33,33% | +35,29% | DEBOLE | 13,0 | 27,5 |
| -15,00% | 64,56 $ | 6/40 | +15,00% | +20,00% | 91,14 $ | 1/6 | +16,67% | +41,18% | DEBOLE | 13,0 | 30,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 79,75 $ | 35/40 | +87,50% | prezzo iniziale | 75,95 $ | 9/35 | +25,71% | -4,76% | DEBOLE | 9,1 | 14,0 |
| +5,00% | 79,75 $ | 35/40 | +87,50% | -5,00% | 72,15 $ | 1/35 | +2,86% | -9,52% | DEBOLE | 9,1 | 10,0 |
| +5,00% | 79,75 $ | 35/40 | +87,50% | -8,00% | 69,87 $ | 1/35 | +2,86% | -12,38% | DEBOLE | 9,1 | 11,0 |
| +5,00% | 79,75 $ | 35/40 | +87,50% | -10,00% | 68,35 $ | 1/35 | +2,86% | -14,29% | DEBOLE | 9,1 | 11,0 |
| +5,00% | 79,75 $ | 35/40 | +87,50% | -15,00% | 64,56 $ | 1/35 | +2,86% | -19,05% | DEBOLE | 9,1 | 11,0 |
| +10,00% | 83,54 $ | 30/40 | +75,00% | prezzo iniziale | 75,95 $ | 3/30 | +10,00% | -9,09% | DEBOLE | 12,8 | 17,0 |
| +10,00% | 83,54 $ | 30/40 | +75,00% | -5,00% | 72,15 $ | 1/30 | +3,33% | -13,64% | DEBOLE | 12,8 | 10,0 |
| +10,00% | 83,54 $ | 30/40 | +75,00% | -8,00% | 69,87 $ | 1/30 | +3,33% | -16,36% | DEBOLE | 12,8 | 11,0 |
| +10,00% | 83,54 $ | 30/40 | +75,00% | -10,00% | 68,35 $ | 1/30 | +3,33% | -18,18% | DEBOLE | 12,8 | 11,0 |
| +10,00% | 83,54 $ | 30/40 | +75,00% | -15,00% | 64,56 $ | 1/30 | +3,33% | -22,73% | DEBOLE | 12,8 | 11,0 |
| +15,00% | 87,34 $ | 24/40 | +60,00% | prezzo iniziale | 75,95 $ | 2/24 | +8,33% | -13,04% | DEBOLE | 14,7 | 20,5 |
| +15,00% | 87,34 $ | 24/40 | +60,00% | -5,00% | 72,15 $ | 0/24 | 0,00% | -17,39% | DEBOLE | 14,7 | n/d |
| +15,00% | 87,34 $ | 24/40 | +60,00% | -8,00% | 69,87 $ | 0/24 | 0,00% | -20,00% | DEBOLE | 14,7 | n/d |
| +15,00% | 87,34 $ | 24/40 | +60,00% | -10,00% | 68,35 $ | 0/24 | 0,00% | -21,74% | DEBOLE | 14,7 | n/d |
| +15,00% | 87,34 $ | 24/40 | +60,00% | -15,00% | 64,56 $ | 0/24 | 0,00% | -26,09% | DEBOLE | 14,7 | n/d |
| +20,00% | 91,14 $ | 19/40 | +47,50% | prezzo iniziale | 75,95 $ | 0/19 | 0,00% | -16,67% | DEBOLE | 15,3 | n/d |
| +20,00% | 91,14 $ | 19/40 | +47,50% | -5,00% | 72,15 $ | 0/19 | 0,00% | -20,83% | DEBOLE | 15,3 | n/d |
| +20,00% | 91,14 $ | 19/40 | +47,50% | -8,00% | 69,87 $ | 0/19 | 0,00% | -23,33% | DEBOLE | 15,3 | n/d |
| +20,00% | 91,14 $ | 19/40 | +47,50% | -10,00% | 68,35 $ | 0/19 | 0,00% | -25,00% | DEBOLE | 15,3 | n/d |
| +20,00% | 91,14 $ | 19/40 | +47,50% | -15,00% | 64,56 $ | 0/19 | 0,00% | -29,17% | DEBOLE | 15,3 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 28 prima sono scesi a -5,00%. Tra quei 28, 17 poi sono rimbalzati fino a +10,00%. Percentuale: +60,71% (17/28). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.
- DOGE: su 40 casi simili, 29 prima sono saliti a +10,00%. Tra quei 29, 1 poi sono scaricati a -5,00%. Percentuale: +3,45% (1/29). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06647 $ | 28/40 | +70,00% | +5,00% | 0,07347 $ | 17/28 | +60,71% | +10,53% | MEDIA | 5,6 | 16,6 |
| -5,00% | 0,06647 $ | 28/40 | +70,00% | +10,00% | 0,07697 $ | 17/28 | +60,71% | +15,79% | MEDIA | 5,6 | 18,7 |
| -5,00% | 0,06647 $ | 28/40 | +70,00% | +15,00% | 0,08047 $ | 16/28 | +57,14% | +21,05% | MEDIA | 5,6 | 21,8 |
| -5,00% | 0,06647 $ | 28/40 | +70,00% | +20,00% | 0,08396 $ | 11/28 | +39,29% | +26,32% | BASSA | 5,6 | 23,5 |
| -8,00% | 0,06437 $ | 23/40 | +57,50% | +5,00% | 0,07347 $ | 12/23 | +52,17% | +14,13% | MEDIA | 7,5 | 17,5 |
| -8,00% | 0,06437 $ | 23/40 | +57,50% | +10,00% | 0,07697 $ | 12/23 | +52,17% | +19,57% | MEDIA | 7,5 | 19,2 |
| -8,00% | 0,06437 $ | 23/40 | +57,50% | +15,00% | 0,08047 $ | 11/23 | +47,83% | +25,00% | BASSA | 7,5 | 22,6 |
| -8,00% | 0,06437 $ | 23/40 | +57,50% | +20,00% | 0,08396 $ | 7/23 | +30,43% | +30,43% | DEBOLE | 7,5 | 24,3 |
| -10,00% | 0,06297 $ | 20/40 | +50,00% | +5,00% | 0,07347 $ | 9/20 | +45,00% | +16,67% | BASSA | 6,8 | 17,3 |
| -10,00% | 0,06297 $ | 20/40 | +50,00% | +10,00% | 0,07697 $ | 9/20 | +45,00% | +22,22% | BASSA | 6,8 | 19,4 |
| -10,00% | 0,06297 $ | 20/40 | +50,00% | +15,00% | 0,08047 $ | 8/20 | +40,00% | +27,78% | BASSA | 6,8 | 23,4 |
| -10,00% | 0,06297 $ | 20/40 | +50,00% | +20,00% | 0,08396 $ | 5/20 | +25,00% | +33,33% | DEBOLE | 6,8 | 25,6 |
| -15,00% | 0,05947 $ | 13/40 | +32,50% | +5,00% | 0,07347 $ | 2/13 | +15,38% | +23,53% | DEBOLE | 6,8 | 15,5 |
| -15,00% | 0,05947 $ | 13/40 | +32,50% | +10,00% | 0,07697 $ | 2/13 | +15,38% | +29,41% | DEBOLE | 6,8 | 16,5 |
| -15,00% | 0,05947 $ | 13/40 | +32,50% | +15,00% | 0,08047 $ | 2/13 | +15,38% | +35,29% | DEBOLE | 6,8 | 20,0 |
| -15,00% | 0,05947 $ | 13/40 | +32,50% | +20,00% | 0,08396 $ | 1/13 | +7,69% | +41,18% | DEBOLE | 6,8 | 27,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07347 $ | 32/40 | +80,00% | prezzo iniziale | 0,06997 $ | 20/32 | +62,50% | -4,76% | MEDIA | 8,8 | 13,8 |
| +5,00% | 0,07347 $ | 32/40 | +80,00% | -5,00% | 0,06647 $ | 10/32 | +31,25% | -9,52% | DEBOLE | 8,8 | 12,5 |
| +5,00% | 0,07347 $ | 32/40 | +80,00% | -8,00% | 0,06437 $ | 7/32 | +21,88% | -12,38% | DEBOLE | 8,8 | 9,4 |
| +5,00% | 0,07347 $ | 32/40 | +80,00% | -10,00% | 0,06297 $ | 6/32 | +18,75% | -14,29% | DEBOLE | 8,8 | 9,0 |
| +5,00% | 0,07347 $ | 32/40 | +80,00% | -15,00% | 0,05947 $ | 3/32 | +9,38% | -19,05% | DEBOLE | 8,8 | 8,3 |
| +10,00% | 0,07697 $ | 29/40 | +72,50% | prezzo iniziale | 0,06997 $ | 10/29 | +34,48% | -9,09% | DEBOLE | 14,8 | 21,4 |
| +10,00% | 0,07697 $ | 29/40 | +72,50% | -5,00% | 0,06647 $ | 1/29 | +3,45% | -13,64% | DEBOLE | 14,8 | 26,0 |
| +10,00% | 0,07697 $ | 29/40 | +72,50% | -8,00% | 0,06437 $ | 0/29 | 0,00% | -16,36% | DEBOLE | 14,8 | n/d |
| +10,00% | 0,07697 $ | 29/40 | +72,50% | -10,00% | 0,06297 $ | 0/29 | 0,00% | -18,18% | DEBOLE | 14,8 | n/d |
| +10,00% | 0,07697 $ | 29/40 | +72,50% | -15,00% | 0,05947 $ | 0/29 | 0,00% | -22,73% | DEBOLE | 14,8 | n/d |
| +15,00% | 0,08047 $ | 28/40 | +70,00% | prezzo iniziale | 0,06997 $ | 4/28 | +14,29% | -13,04% | DEBOLE | 18,9 | 20,8 |
| +15,00% | 0,08047 $ | 28/40 | +70,00% | -5,00% | 0,06647 $ | 1/28 | +3,57% | -17,39% | DEBOLE | 18,9 | 26,0 |
| +15,00% | 0,08047 $ | 28/40 | +70,00% | -8,00% | 0,06437 $ | 0/28 | 0,00% | -20,00% | DEBOLE | 18,9 | n/d |
| +15,00% | 0,08047 $ | 28/40 | +70,00% | -10,00% | 0,06297 $ | 0/28 | 0,00% | -21,74% | DEBOLE | 18,9 | n/d |
| +15,00% | 0,08047 $ | 28/40 | +70,00% | -15,00% | 0,05947 $ | 0/28 | 0,00% | -26,09% | DEBOLE | 18,9 | n/d |
| +20,00% | 0,08396 $ | 22/40 | +55,00% | prezzo iniziale | 0,06997 $ | 2/22 | +9,09% | -16,67% | DEBOLE | 20,9 | 20,5 |
| +20,00% | 0,08396 $ | 22/40 | +55,00% | -5,00% | 0,06647 $ | 0/22 | 0,00% | -20,83% | DEBOLE | 20,9 | n/d |
| +20,00% | 0,08396 $ | 22/40 | +55,00% | -8,00% | 0,06437 $ | 0/22 | 0,00% | -23,33% | DEBOLE | 20,9 | n/d |
| +20,00% | 0,08396 $ | 22/40 | +55,00% | -10,00% | 0,06297 $ | 0/22 | 0,00% | -25,00% | DEBOLE | 20,9 | n/d |
| +20,00% | 0,08396 $ | 22/40 | +55,00% | -15,00% | 0,05947 $ | 0/22 | 0,00% | -29,17% | DEBOLE | 20,9 | n/d |

---
