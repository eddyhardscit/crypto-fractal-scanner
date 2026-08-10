# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-08-10 07:15:26 CEST**  
UTC: **2026-08-10 05:15:26 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 61.699 $ | 71.441 $ | +57,14% | +15,79% | rimbalzo possibile | 71.441 $ | 61.699 $ | +3,33% | -13,64% | spike storicamente più resistente |
| SOL | 72,72 $ | 84,21 $ | +42,86% | +15,79% | rimbalzo debole | 84,21 $ | 72,72 $ | 0,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06622 $ | 0,07668 $ | +64,29% | +15,79% | rimbalzo possibile | 0,07668 $ | 0,06622 $ | +9,68% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 14 prima sono scesi a -5,00%. Tra quei 14, 8 poi sono rimbalzati fino a +10,00%. Percentuale: +57,14% (8/14). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.
- BTC: su 40 casi simili, 30 prima sono saliti a +10,00%. Tra quei 30, 1 poi sono scaricati a -5,00%. Percentuale: +3,33% (1/30). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 61.699 $ | 14/40 | +35,00% | +5,00% | 68.194 $ | 10/14 | +71,43% | +10,53% | ALTA | 7,2 | 21,8 |
| -5,00% | 61.699 $ | 14/40 | +35,00% | +10,00% | 71.441 $ | 8/14 | +57,14% | +15,79% | MEDIA | 7,2 | 22,6 |
| -5,00% | 61.699 $ | 14/40 | +35,00% | +15,00% | 74.688 $ | 6/14 | +42,86% | +21,05% | BASSA | 7,2 | 24,5 |
| -5,00% | 61.699 $ | 14/40 | +35,00% | +20,00% | 77.936 $ | 3/14 | +21,43% | +26,32% | DEBOLE | 7,2 | 21,0 |
| -8,00% | 59.751 $ | 12/40 | +30,00% | +5,00% | 68.194 $ | 8/12 | +66,67% | +14,13% | ALTA | 9,0 | 20,6 |
| -8,00% | 59.751 $ | 12/40 | +30,00% | +10,00% | 71.441 $ | 7/12 | +58,33% | +19,57% | MEDIA | 9,0 | 22,1 |
| -8,00% | 59.751 $ | 12/40 | +30,00% | +15,00% | 74.688 $ | 5/12 | +41,67% | +25,00% | BASSA | 9,0 | 23,6 |
| -8,00% | 59.751 $ | 12/40 | +30,00% | +20,00% | 77.936 $ | 3/12 | +25,00% | +30,43% | DEBOLE | 9,0 | 21,0 |
| -10,00% | 58.452 $ | 11/40 | +27,50% | +5,00% | 68.194 $ | 7/11 | +63,64% | +16,67% | MEDIA | 10,9 | 21,4 |
| -10,00% | 58.452 $ | 11/40 | +27,50% | +10,00% | 71.441 $ | 6/11 | +54,55% | +22,22% | MEDIA | 10,9 | 22,8 |
| -10,00% | 58.452 $ | 11/40 | +27,50% | +15,00% | 74.688 $ | 4/11 | +36,36% | +27,78% | BASSA | 10,9 | 23,8 |
| -10,00% | 58.452 $ | 11/40 | +27,50% | +20,00% | 77.936 $ | 2/11 | +18,18% | +33,33% | DEBOLE | 10,9 | 19,0 |
| -15,00% | 55.204 $ | 5/40 | +12,50% | +5,00% | 68.194 $ | 2/5 | +40,00% | +23,53% | BASSA | 15,0 | 22,5 |
| -15,00% | 55.204 $ | 5/40 | +12,50% | +10,00% | 71.441 $ | 1/5 | +20,00% | +29,41% | DEBOLE | 15,0 | 23,0 |
| -15,00% | 55.204 $ | 5/40 | +12,50% | +15,00% | 74.688 $ | 1/5 | +20,00% | +35,29% | DEBOLE | 15,0 | 30,0 |
| -15,00% | 55.204 $ | 5/40 | +12,50% | +20,00% | 77.936 $ | 0/5 | 0,00% | +41,18% | DEBOLE | 15,0 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 68.194 $ | 37/40 | +92,50% | prezzo iniziale | 64.946 $ | 8/37 | +21,62% | -4,76% | DEBOLE | 10,3 | 18,0 |
| +5,00% | 68.194 $ | 37/40 | +92,50% | -5,00% | 61.699 $ | 3/37 | +8,11% | -9,52% | DEBOLE | 10,3 | 14,3 |
| +5,00% | 68.194 $ | 37/40 | +92,50% | -8,00% | 59.751 $ | 3/37 | +8,11% | -12,38% | DEBOLE | 10,3 | 17,0 |
| +5,00% | 68.194 $ | 37/40 | +92,50% | -10,00% | 58.452 $ | 3/37 | +8,11% | -14,29% | DEBOLE | 10,3 | 19,0 |
| +5,00% | 68.194 $ | 37/40 | +92,50% | -15,00% | 55.204 $ | 0/37 | 0,00% | -19,05% | DEBOLE | 10,3 | n/d |
| +10,00% | 71.441 $ | 30/40 | +75,00% | prezzo iniziale | 64.946 $ | 3/30 | +10,00% | -9,09% | DEBOLE | 14,8 | 22,3 |
| +10,00% | 71.441 $ | 30/40 | +75,00% | -5,00% | 61.699 $ | 1/30 | +3,33% | -13,64% | DEBOLE | 14,8 | 19,0 |
| +10,00% | 71.441 $ | 30/40 | +75,00% | -8,00% | 59.751 $ | 1/30 | +3,33% | -16,36% | DEBOLE | 14,8 | 21,0 |
| +10,00% | 71.441 $ | 30/40 | +75,00% | -10,00% | 58.452 $ | 1/30 | +3,33% | -18,18% | DEBOLE | 14,8 | 22,0 |
| +10,00% | 71.441 $ | 30/40 | +75,00% | -15,00% | 55.204 $ | 0/30 | 0,00% | -22,73% | DEBOLE | 14,8 | n/d |
| +15,00% | 74.688 $ | 24/40 | +60,00% | prezzo iniziale | 64.946 $ | 1/24 | +4,17% | -13,04% | DEBOLE | 15,6 | 26,0 |
| +15,00% | 74.688 $ | 24/40 | +60,00% | -5,00% | 61.699 $ | 0/24 | 0,00% | -17,39% | DEBOLE | 15,6 | n/d |
| +15,00% | 74.688 $ | 24/40 | +60,00% | -8,00% | 59.751 $ | 0/24 | 0,00% | -20,00% | DEBOLE | 15,6 | n/d |
| +15,00% | 74.688 $ | 24/40 | +60,00% | -10,00% | 58.452 $ | 0/24 | 0,00% | -21,74% | DEBOLE | 15,6 | n/d |
| +15,00% | 74.688 $ | 24/40 | +60,00% | -15,00% | 55.204 $ | 0/24 | 0,00% | -26,09% | DEBOLE | 15,6 | n/d |
| +20,00% | 77.936 $ | 17/40 | +42,50% | prezzo iniziale | 64.946 $ | 1/17 | +5,88% | -16,67% | DEBOLE | 14,3 | 26,0 |
| +20,00% | 77.936 $ | 17/40 | +42,50% | -5,00% | 61.699 $ | 0/17 | 0,00% | -20,83% | DEBOLE | 14,3 | n/d |
| +20,00% | 77.936 $ | 17/40 | +42,50% | -8,00% | 59.751 $ | 0/17 | 0,00% | -23,33% | DEBOLE | 14,3 | n/d |
| +20,00% | 77.936 $ | 17/40 | +42,50% | -10,00% | 58.452 $ | 0/17 | 0,00% | -25,00% | DEBOLE | 14,3 | n/d |
| +20,00% | 77.936 $ | 17/40 | +42,50% | -15,00% | 55.204 $ | 0/17 | 0,00% | -29,17% | DEBOLE | 14,3 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 14 prima sono scesi a -5,00%. Tra quei 14, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +42,86% (6/14). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- SOL: su 40 casi simili, 27 prima sono saliti a +10,00%. Tra quei 27, 0 poi sono scaricati a -5,00%. Percentuale: 0,00% (0/27). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 72,72 $ | 14/40 | +35,00% | +5,00% | 80,38 $ | 8/14 | +57,14% | +10,53% | MEDIA | 7,6 | 24,6 |
| -5,00% | 72,72 $ | 14/40 | +35,00% | +10,00% | 84,21 $ | 6/14 | +42,86% | +15,79% | BASSA | 7,6 | 23,8 |
| -5,00% | 72,72 $ | 14/40 | +35,00% | +15,00% | 88,03 $ | 6/14 | +42,86% | +21,05% | BASSA | 7,6 | 25,2 |
| -5,00% | 72,72 $ | 14/40 | +35,00% | +20,00% | 91,86 $ | 4/14 | +28,57% | +26,32% | DEBOLE | 7,6 | 25,5 |
| -8,00% | 70,43 $ | 12/40 | +30,00% | +5,00% | 80,38 $ | 6/12 | +50,00% | +14,13% | MEDIA | 9,8 | 24,7 |
| -8,00% | 70,43 $ | 12/40 | +30,00% | +10,00% | 84,21 $ | 4/12 | +33,33% | +19,57% | DEBOLE | 9,8 | 23,0 |
| -8,00% | 70,43 $ | 12/40 | +30,00% | +15,00% | 88,03 $ | 4/12 | +33,33% | +25,00% | DEBOLE | 9,8 | 24,5 |
| -8,00% | 70,43 $ | 12/40 | +30,00% | +20,00% | 91,86 $ | 3/12 | +25,00% | +30,43% | DEBOLE | 9,8 | 25,0 |
| -10,00% | 68,90 $ | 11/40 | +27,50% | +5,00% | 80,38 $ | 6/11 | +54,55% | +16,67% | MEDIA | 9,4 | 24,7 |
| -10,00% | 68,90 $ | 11/40 | +27,50% | +10,00% | 84,21 $ | 4/11 | +36,36% | +22,22% | BASSA | 9,4 | 23,0 |
| -10,00% | 68,90 $ | 11/40 | +27,50% | +15,00% | 88,03 $ | 4/11 | +36,36% | +27,78% | BASSA | 9,4 | 24,5 |
| -10,00% | 68,90 $ | 11/40 | +27,50% | +20,00% | 91,86 $ | 3/11 | +27,27% | +33,33% | DEBOLE | 9,4 | 25,0 |
| -15,00% | 65,07 $ | 5/40 | +12,50% | +5,00% | 80,38 $ | 2/5 | +40,00% | +23,53% | BASSA | 13,0 | 26,5 |
| -15,00% | 65,07 $ | 5/40 | +12,50% | +10,00% | 84,21 $ | 2/5 | +40,00% | +29,41% | BASSA | 13,0 | 27,5 |
| -15,00% | 65,07 $ | 5/40 | +12,50% | +15,00% | 88,03 $ | 2/5 | +40,00% | +35,29% | BASSA | 13,0 | 27,5 |
| -15,00% | 65,07 $ | 5/40 | +12,50% | +20,00% | 91,86 $ | 1/5 | +20,00% | +41,18% | DEBOLE | 13,0 | 30,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 80,38 $ | 34/40 | +85,00% | prezzo iniziale | 76,55 $ | 9/34 | +26,47% | -4,76% | DEBOLE | 9,9 | 15,8 |
| +5,00% | 80,38 $ | 34/40 | +85,00% | -5,00% | 72,72 $ | 1/34 | +2,94% | -9,52% | DEBOLE | 9,9 | 10,0 |
| +5,00% | 80,38 $ | 34/40 | +85,00% | -8,00% | 70,43 $ | 1/34 | +2,94% | -12,38% | DEBOLE | 9,9 | 10,0 |
| +5,00% | 80,38 $ | 34/40 | +85,00% | -10,00% | 68,90 $ | 1/34 | +2,94% | -14,29% | DEBOLE | 9,9 | 14,0 |
| +5,00% | 80,38 $ | 34/40 | +85,00% | -15,00% | 65,07 $ | 0/34 | 0,00% | -19,05% | DEBOLE | 9,9 | n/d |
| +10,00% | 84,21 $ | 27/40 | +67,50% | prezzo iniziale | 76,55 $ | 1/27 | +3,70% | -9,09% | DEBOLE | 14,6 | 29,0 |
| +10,00% | 84,21 $ | 27/40 | +67,50% | -5,00% | 72,72 $ | 0/27 | 0,00% | -13,64% | DEBOLE | 14,6 | n/d |
| +10,00% | 84,21 $ | 27/40 | +67,50% | -8,00% | 70,43 $ | 0/27 | 0,00% | -16,36% | DEBOLE | 14,6 | n/d |
| +10,00% | 84,21 $ | 27/40 | +67,50% | -10,00% | 68,90 $ | 0/27 | 0,00% | -18,18% | DEBOLE | 14,6 | n/d |
| +10,00% | 84,21 $ | 27/40 | +67,50% | -15,00% | 65,07 $ | 0/27 | 0,00% | -22,73% | DEBOLE | 14,6 | n/d |
| +15,00% | 88,03 $ | 23/40 | +57,50% | prezzo iniziale | 76,55 $ | 1/23 | +4,35% | -13,04% | DEBOLE | 15,6 | 29,0 |
| +15,00% | 88,03 $ | 23/40 | +57,50% | -5,00% | 72,72 $ | 0/23 | 0,00% | -17,39% | DEBOLE | 15,6 | n/d |
| +15,00% | 88,03 $ | 23/40 | +57,50% | -8,00% | 70,43 $ | 0/23 | 0,00% | -20,00% | DEBOLE | 15,6 | n/d |
| +15,00% | 88,03 $ | 23/40 | +57,50% | -10,00% | 68,90 $ | 0/23 | 0,00% | -21,74% | DEBOLE | 15,6 | n/d |
| +15,00% | 88,03 $ | 23/40 | +57,50% | -15,00% | 65,07 $ | 0/23 | 0,00% | -26,09% | DEBOLE | 15,6 | n/d |
| +20,00% | 91,86 $ | 19/40 | +47,50% | prezzo iniziale | 76,55 $ | 0/19 | 0,00% | -16,67% | DEBOLE | 15,9 | n/d |
| +20,00% | 91,86 $ | 19/40 | +47,50% | -5,00% | 72,72 $ | 0/19 | 0,00% | -20,83% | DEBOLE | 15,9 | n/d |
| +20,00% | 91,86 $ | 19/40 | +47,50% | -8,00% | 70,43 $ | 0/19 | 0,00% | -23,33% | DEBOLE | 15,9 | n/d |
| +20,00% | 91,86 $ | 19/40 | +47,50% | -10,00% | 68,90 $ | 0/19 | 0,00% | -25,00% | DEBOLE | 15,9 | n/d |
| +20,00% | 91,86 $ | 19/40 | +47,50% | -15,00% | 65,07 $ | 0/19 | 0,00% | -29,17% | DEBOLE | 15,9 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 28 prima sono scesi a -5,00%. Tra quei 28, 18 poi sono rimbalzati fino a +10,00%. Percentuale: +64,29% (18/28). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.
- DOGE: su 40 casi simili, 31 prima sono saliti a +10,00%. Tra quei 31, 3 poi sono scaricati a -5,00%. Percentuale: +9,68% (3/31). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06622 $ | 28/40 | +70,00% | +5,00% | 0,07320 $ | 18/28 | +64,29% | +10,53% | MEDIA | 6,2 | 15,7 |
| -5,00% | 0,06622 $ | 28/40 | +70,00% | +10,00% | 0,07668 $ | 18/28 | +64,29% | +15,79% | MEDIA | 6,2 | 17,7 |
| -5,00% | 0,06622 $ | 28/40 | +70,00% | +15,00% | 0,08017 $ | 17/28 | +60,71% | +21,05% | MEDIA | 6,2 | 20,0 |
| -5,00% | 0,06622 $ | 28/40 | +70,00% | +20,00% | 0,08365 $ | 13/28 | +46,43% | +26,32% | BASSA | 6,2 | 21,9 |
| -8,00% | 0,06413 $ | 22/40 | +55,00% | +5,00% | 0,07320 $ | 12/22 | +54,55% | +14,13% | MEDIA | 8,0 | 17,5 |
| -8,00% | 0,06413 $ | 22/40 | +55,00% | +10,00% | 0,07668 $ | 12/22 | +54,55% | +19,57% | MEDIA | 8,0 | 19,2 |
| -8,00% | 0,06413 $ | 22/40 | +55,00% | +15,00% | 0,08017 $ | 11/22 | +50,00% | +25,00% | MEDIA | 8,0 | 22,6 |
| -8,00% | 0,06413 $ | 22/40 | +55,00% | +20,00% | 0,08365 $ | 7/22 | +31,82% | +30,43% | DEBOLE | 8,0 | 24,3 |
| -10,00% | 0,06274 $ | 19/40 | +47,50% | +5,00% | 0,07320 $ | 9/19 | +47,37% | +16,67% | BASSA | 7,4 | 17,3 |
| -10,00% | 0,06274 $ | 19/40 | +47,50% | +10,00% | 0,07668 $ | 9/19 | +47,37% | +22,22% | BASSA | 7,4 | 19,4 |
| -10,00% | 0,06274 $ | 19/40 | +47,50% | +15,00% | 0,08017 $ | 8/19 | +42,11% | +27,78% | BASSA | 7,4 | 23,4 |
| -10,00% | 0,06274 $ | 19/40 | +47,50% | +20,00% | 0,08365 $ | 5/19 | +26,32% | +33,33% | DEBOLE | 7,4 | 25,6 |
| -15,00% | 0,05925 $ | 11/40 | +27,50% | +5,00% | 0,07320 $ | 2/11 | +18,18% | +23,53% | DEBOLE | 6,2 | 15,5 |
| -15,00% | 0,05925 $ | 11/40 | +27,50% | +10,00% | 0,07668 $ | 2/11 | +18,18% | +29,41% | DEBOLE | 6,2 | 16,5 |
| -15,00% | 0,05925 $ | 11/40 | +27,50% | +15,00% | 0,08017 $ | 2/11 | +18,18% | +35,29% | DEBOLE | 6,2 | 20,0 |
| -15,00% | 0,05925 $ | 11/40 | +27,50% | +20,00% | 0,08365 $ | 1/11 | +9,09% | +41,18% | DEBOLE | 6,2 | 27,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07320 $ | 33/40 | +82,50% | prezzo iniziale | 0,06971 $ | 20/33 | +60,61% | -4,76% | MEDIA | 8,4 | 12,5 |
| +5,00% | 0,07320 $ | 33/40 | +82,50% | -5,00% | 0,06622 $ | 11/33 | +33,33% | -9,52% | DEBOLE | 8,4 | 13,1 |
| +5,00% | 0,07320 $ | 33/40 | +82,50% | -8,00% | 0,06413 $ | 7/33 | +21,21% | -12,38% | DEBOLE | 8,4 | 11,0 |
| +5,00% | 0,07320 $ | 33/40 | +82,50% | -10,00% | 0,06274 $ | 6/33 | +18,18% | -14,29% | DEBOLE | 8,4 | 11,2 |
| +5,00% | 0,07320 $ | 33/40 | +82,50% | -15,00% | 0,05925 $ | 2/33 | +6,06% | -19,05% | DEBOLE | 8,4 | 7,5 |
| +10,00% | 0,07668 $ | 31/40 | +77,50% | prezzo iniziale | 0,06971 $ | 10/31 | +32,26% | -9,09% | DEBOLE | 14,1 | 18,7 |
| +10,00% | 0,07668 $ | 31/40 | +77,50% | -5,00% | 0,06622 $ | 3/31 | +9,68% | -13,64% | DEBOLE | 14,1 | 18,0 |
| +10,00% | 0,07668 $ | 31/40 | +77,50% | -8,00% | 0,06413 $ | 1/31 | +3,23% | -16,36% | DEBOLE | 14,1 | 21,0 |
| +10,00% | 0,07668 $ | 31/40 | +77,50% | -10,00% | 0,06274 $ | 1/31 | +3,23% | -18,18% | DEBOLE | 14,1 | 23,0 |
| +10,00% | 0,07668 $ | 31/40 | +77,50% | -15,00% | 0,05925 $ | 0/31 | 0,00% | -22,73% | DEBOLE | 14,1 | n/d |
| +15,00% | 0,08017 $ | 29/40 | +72,50% | prezzo iniziale | 0,06971 $ | 4/29 | +13,79% | -13,04% | DEBOLE | 17,7 | 20,8 |
| +15,00% | 0,08017 $ | 29/40 | +72,50% | -5,00% | 0,06622 $ | 1/29 | +3,45% | -17,39% | DEBOLE | 17,7 | 26,0 |
| +15,00% | 0,08017 $ | 29/40 | +72,50% | -8,00% | 0,06413 $ | 0/29 | 0,00% | -20,00% | DEBOLE | 17,7 | n/d |
| +15,00% | 0,08017 $ | 29/40 | +72,50% | -10,00% | 0,06274 $ | 0/29 | 0,00% | -21,74% | DEBOLE | 17,7 | n/d |
| +15,00% | 0,08017 $ | 29/40 | +72,50% | -15,00% | 0,05925 $ | 0/29 | 0,00% | -26,09% | DEBOLE | 17,7 | n/d |
| +20,00% | 0,08365 $ | 24/40 | +60,00% | prezzo iniziale | 0,06971 $ | 2/24 | +8,33% | -16,67% | DEBOLE | 20,4 | 20,5 |
| +20,00% | 0,08365 $ | 24/40 | +60,00% | -5,00% | 0,06622 $ | 0/24 | 0,00% | -20,83% | DEBOLE | 20,4 | n/d |
| +20,00% | 0,08365 $ | 24/40 | +60,00% | -8,00% | 0,06413 $ | 0/24 | 0,00% | -23,33% | DEBOLE | 20,4 | n/d |
| +20,00% | 0,08365 $ | 24/40 | +60,00% | -10,00% | 0,06274 $ | 0/24 | 0,00% | -25,00% | DEBOLE | 20,4 | n/d |
| +20,00% | 0,08365 $ | 24/40 | +60,00% | -15,00% | 0,05925 $ | 0/24 | 0,00% | -29,17% | DEBOLE | 20,4 | n/d |

---
