# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-07 13:23:39 CEST**  
UTC: **2026-07-07 11:23:39 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 59.971 $ | 69.440 $ | +33,33% | +15,79% | rimbalzo poco frequente | 69.440 $ | 59.971 $ | +20,83% | -13,64% | spike storicamente più resistente |
| SOL | 76,85 $ | 88,98 $ | +17,24% | +15,79% | rimbalzo poco frequente | 88,98 $ | 76,85 $ | +23,53% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07079 $ | 0,08197 $ | +14,29% | +15,79% | rimbalzo poco frequente | 0,08197 $ | 0,07079 $ | +60,00% | -13,64% | attenzione a prendere profitto |

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

- BTC: su 40 casi simili, 21 prima sono scesi a -5,00%. Tra quei 21, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +33,33% (7/21). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- BTC: su 40 casi simili, 24 prima sono saliti a +10,00%. Tra quei 24, 5 poi sono scaricati a -5,00%. Percentuale: +20,83% (5/24). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 59.971 $ | 21/40 | +52,50% | +5,00% | 66.283 $ | 8/21 | +38,10% | +10,53% | BASSA | 10,3 | 11,2 |
| -5,00% | 59.971 $ | 21/40 | +52,50% | +10,00% | 69.440 $ | 7/21 | +33,33% | +15,79% | DEBOLE | 10,3 | 13,4 |
| -5,00% | 59.971 $ | 21/40 | +52,50% | +15,00% | 72.596 $ | 5/21 | +23,81% | +21,05% | DEBOLE | 10,3 | 14,8 |
| -5,00% | 59.971 $ | 21/40 | +52,50% | +20,00% | 75.753 $ | 4/21 | +19,05% | +26,32% | DEBOLE | 10,3 | 14,8 |
| -8,00% | 58.077 $ | 14/40 | +35,00% | +5,00% | 66.283 $ | 4/14 | +28,57% | +14,13% | DEBOLE | 10,8 | 7,8 |
| -8,00% | 58.077 $ | 14/40 | +35,00% | +10,00% | 69.440 $ | 4/14 | +28,57% | +19,57% | DEBOLE | 10,8 | 10,2 |
| -8,00% | 58.077 $ | 14/40 | +35,00% | +15,00% | 72.596 $ | 3/14 | +21,43% | +25,00% | DEBOLE | 10,8 | 14,7 |
| -8,00% | 58.077 $ | 14/40 | +35,00% | +20,00% | 75.753 $ | 3/14 | +21,43% | +30,43% | DEBOLE | 10,8 | 16,0 |
| -10,00% | 56.814 $ | 8/40 | +20,00% | +5,00% | 66.283 $ | 1/8 | +12,50% | +16,67% | DEBOLE | 12,8 | 16,0 |
| -10,00% | 56.814 $ | 8/40 | +20,00% | +10,00% | 69.440 $ | 1/8 | +12,50% | +22,22% | DEBOLE | 12,8 | 25,0 |
| -10,00% | 56.814 $ | 8/40 | +20,00% | +15,00% | 72.596 $ | 1/8 | +12,50% | +27,78% | DEBOLE | 12,8 | 26,0 |
| -10,00% | 56.814 $ | 8/40 | +20,00% | +20,00% | 75.753 $ | 1/8 | +12,50% | +33,33% | DEBOLE | 12,8 | 26,0 |
| -15,00% | 53.658 $ | 6/40 | +15,00% | +5,00% | 66.283 $ | 1/6 | +16,67% | +23,53% | DEBOLE | 12,5 | 16,0 |
| -15,00% | 53.658 $ | 6/40 | +15,00% | +10,00% | 69.440 $ | 1/6 | +16,67% | +29,41% | DEBOLE | 12,5 | 25,0 |
| -15,00% | 53.658 $ | 6/40 | +15,00% | +15,00% | 72.596 $ | 1/6 | +16,67% | +35,29% | DEBOLE | 12,5 | 26,0 |
| -15,00% | 53.658 $ | 6/40 | +15,00% | +20,00% | 75.753 $ | 1/6 | +16,67% | +41,18% | DEBOLE | 12,5 | 26,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 66.283 $ | 34/40 | +85,00% | prezzo iniziale | 63.127 $ | 22/34 | +64,71% | -4,76% | MEDIA | 5,0 | 14,2 |
| +5,00% | 66.283 $ | 34/40 | +85,00% | -5,00% | 59.971 $ | 12/34 | +35,29% | -9,52% | BASSA | 5,0 | 15,2 |
| +5,00% | 66.283 $ | 34/40 | +85,00% | -8,00% | 58.077 $ | 8/34 | +23,53% | -12,38% | DEBOLE | 5,0 | 17,1 |
| +5,00% | 66.283 $ | 34/40 | +85,00% | -10,00% | 56.814 $ | 5/34 | +14,71% | -14,29% | DEBOLE | 5,0 | 16,8 |
| +5,00% | 66.283 $ | 34/40 | +85,00% | -15,00% | 53.658 $ | 3/34 | +8,82% | -19,05% | DEBOLE | 5,0 | 14,0 |
| +10,00% | 69.440 $ | 24/40 | +60,00% | prezzo iniziale | 63.127 $ | 10/24 | +41,67% | -9,09% | BASSA | 10,4 | 16,8 |
| +10,00% | 69.440 $ | 24/40 | +60,00% | -5,00% | 59.971 $ | 5/24 | +20,83% | -13,64% | DEBOLE | 10,4 | 16,4 |
| +10,00% | 69.440 $ | 24/40 | +60,00% | -8,00% | 58.077 $ | 4/24 | +16,67% | -16,36% | DEBOLE | 10,4 | 19,2 |
| +10,00% | 69.440 $ | 24/40 | +60,00% | -10,00% | 56.814 $ | 2/24 | +8,33% | -18,18% | DEBOLE | 10,4 | 22,0 |
| +10,00% | 69.440 $ | 24/40 | +60,00% | -15,00% | 53.658 $ | 1/24 | +4,17% | -22,73% | DEBOLE | 10,4 | 24,0 |
| +15,00% | 72.596 $ | 19/40 | +47,50% | prezzo iniziale | 63.127 $ | 5/19 | +26,32% | -13,04% | DEBOLE | 13,6 | 21,2 |
| +15,00% | 72.596 $ | 19/40 | +47,50% | -5,00% | 59.971 $ | 3/19 | +15,79% | -17,39% | DEBOLE | 13,6 | 23,0 |
| +15,00% | 72.596 $ | 19/40 | +47,50% | -8,00% | 58.077 $ | 1/19 | +5,26% | -20,00% | DEBOLE | 13,6 | 21,0 |
| +15,00% | 72.596 $ | 19/40 | +47,50% | -10,00% | 56.814 $ | 1/19 | +5,26% | -21,74% | DEBOLE | 13,6 | 21,0 |
| +15,00% | 72.596 $ | 19/40 | +47,50% | -15,00% | 53.658 $ | 0/19 | 0,00% | -26,09% | DEBOLE | 13,6 | n/d |
| +20,00% | 75.753 $ | 12/40 | +30,00% | prezzo iniziale | 63.127 $ | 2/12 | +16,67% | -16,67% | DEBOLE | 14,9 | 23,0 |
| +20,00% | 75.753 $ | 12/40 | +30,00% | -5,00% | 59.971 $ | 1/12 | +8,33% | -20,83% | DEBOLE | 14,9 | 28,0 |
| +20,00% | 75.753 $ | 12/40 | +30,00% | -8,00% | 58.077 $ | 0/12 | 0,00% | -23,33% | DEBOLE | 14,9 | n/d |
| +20,00% | 75.753 $ | 12/40 | +30,00% | -10,00% | 56.814 $ | 0/12 | 0,00% | -25,00% | DEBOLE | 14,9 | n/d |
| +20,00% | 75.753 $ | 12/40 | +30,00% | -15,00% | 53.658 $ | 0/12 | 0,00% | -29,17% | DEBOLE | 14,9 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 29 prima sono scesi a -5,00%. Tra quei 29, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +17,24% (5/29). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 17 prima sono saliti a +10,00%. Tra quei 17, 4 poi sono scaricati a -5,00%. Percentuale: +23,53% (4/17). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 76,85 $ | 29/40 | +72,50% | +5,00% | 84,93 $ | 9/29 | +31,03% | +10,53% | DEBOLE | 7,9 | 14,8 |
| -5,00% | 76,85 $ | 29/40 | +72,50% | +10,00% | 88,98 $ | 5/29 | +17,24% | +15,79% | DEBOLE | 7,9 | 19,4 |
| -5,00% | 76,85 $ | 29/40 | +72,50% | +15,00% | 93,02 $ | 3/29 | +10,34% | +21,05% | DEBOLE | 7,9 | 19,3 |
| -5,00% | 76,85 $ | 29/40 | +72,50% | +20,00% | 97,07 $ | 2/29 | +6,90% | +26,32% | DEBOLE | 7,9 | 21,5 |
| -8,00% | 74,42 $ | 26/40 | +65,00% | +5,00% | 84,93 $ | 6/26 | +23,08% | +14,13% | DEBOLE | 10,9 | 17,0 |
| -8,00% | 74,42 $ | 26/40 | +65,00% | +10,00% | 88,98 $ | 5/26 | +19,23% | +19,57% | DEBOLE | 10,9 | 19,4 |
| -8,00% | 74,42 $ | 26/40 | +65,00% | +15,00% | 93,02 $ | 3/26 | +11,54% | +25,00% | DEBOLE | 10,9 | 19,3 |
| -8,00% | 74,42 $ | 26/40 | +65,00% | +20,00% | 97,07 $ | 2/26 | +7,69% | +30,43% | DEBOLE | 10,9 | 21,5 |
| -10,00% | 72,80 $ | 22/40 | +55,00% | +5,00% | 84,93 $ | 5/22 | +22,73% | +16,67% | DEBOLE | 10,5 | 14,4 |
| -10,00% | 72,80 $ | 22/40 | +55,00% | +10,00% | 88,98 $ | 5/22 | +22,73% | +22,22% | DEBOLE | 10,5 | 19,4 |
| -10,00% | 72,80 $ | 22/40 | +55,00% | +15,00% | 93,02 $ | 3/22 | +13,64% | +27,78% | DEBOLE | 10,5 | 19,3 |
| -10,00% | 72,80 $ | 22/40 | +55,00% | +20,00% | 97,07 $ | 2/22 | +9,09% | +33,33% | DEBOLE | 10,5 | 21,5 |
| -15,00% | 68,76 $ | 16/40 | +40,00% | +5,00% | 84,93 $ | 3/16 | +18,75% | +23,53% | DEBOLE | 13,4 | 16,3 |
| -15,00% | 68,76 $ | 16/40 | +40,00% | +10,00% | 88,98 $ | 3/16 | +18,75% | +29,41% | DEBOLE | 13,4 | 20,0 |
| -15,00% | 68,76 $ | 16/40 | +40,00% | +15,00% | 93,02 $ | 2/16 | +12,50% | +35,29% | DEBOLE | 13,4 | 20,5 |
| -15,00% | 68,76 $ | 16/40 | +40,00% | +20,00% | 97,07 $ | 1/16 | +6,25% | +41,18% | DEBOLE | 13,4 | 26,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 84,93 $ | 29/40 | +72,50% | prezzo iniziale | 80,89 $ | 23/29 | +79,31% | -4,76% | ALTA | 5,2 | 12,0 |
| +5,00% | 84,93 $ | 29/40 | +72,50% | -5,00% | 76,85 $ | 17/29 | +58,62% | -9,52% | MEDIA | 5,2 | 13,5 |
| +5,00% | 84,93 $ | 29/40 | +72,50% | -8,00% | 74,42 $ | 16/29 | +55,17% | -12,38% | MEDIA | 5,2 | 16,0 |
| +5,00% | 84,93 $ | 29/40 | +72,50% | -10,00% | 72,80 $ | 10/29 | +34,48% | -14,29% | DEBOLE | 5,2 | 14,4 |
| +5,00% | 84,93 $ | 29/40 | +72,50% | -15,00% | 68,76 $ | 7/29 | +24,14% | -19,05% | DEBOLE | 5,2 | 16,1 |
| +10,00% | 88,98 $ | 17/40 | +42,50% | prezzo iniziale | 80,89 $ | 9/17 | +52,94% | -9,09% | MEDIA | 9,6 | 18,0 |
| +10,00% | 88,98 $ | 17/40 | +42,50% | -5,00% | 76,85 $ | 4/17 | +23,53% | -13,64% | DEBOLE | 9,6 | 18,2 |
| +10,00% | 88,98 $ | 17/40 | +42,50% | -8,00% | 74,42 $ | 4/17 | +23,53% | -16,36% | DEBOLE | 9,6 | 18,2 |
| +10,00% | 88,98 $ | 17/40 | +42,50% | -10,00% | 72,80 $ | 1/17 | +5,88% | -18,18% | DEBOLE | 9,6 | 19,0 |
| +10,00% | 88,98 $ | 17/40 | +42,50% | -15,00% | 68,76 $ | 1/17 | +5,88% | -22,73% | DEBOLE | 9,6 | 19,0 |
| +15,00% | 93,02 $ | 13/40 | +32,50% | prezzo iniziale | 80,89 $ | 6/13 | +46,15% | -13,04% | BASSA | 12,2 | 16,2 |
| +15,00% | 93,02 $ | 13/40 | +32,50% | -5,00% | 76,85 $ | 3/13 | +23,08% | -17,39% | DEBOLE | 12,2 | 18,0 |
| +15,00% | 93,02 $ | 13/40 | +32,50% | -8,00% | 74,42 $ | 3/13 | +23,08% | -20,00% | DEBOLE | 12,2 | 18,0 |
| +15,00% | 93,02 $ | 13/40 | +32,50% | -10,00% | 72,80 $ | 0/13 | 0,00% | -21,74% | DEBOLE | 12,2 | n/d |
| +15,00% | 93,02 $ | 13/40 | +32,50% | -15,00% | 68,76 $ | 0/13 | 0,00% | -26,09% | DEBOLE | 12,2 | n/d |
| +20,00% | 97,07 $ | 7/40 | +17,50% | prezzo iniziale | 80,89 $ | 0/7 | 0,00% | -16,67% | DEBOLE | 16,3 | n/d |
| +20,00% | 97,07 $ | 7/40 | +17,50% | -5,00% | 76,85 $ | 0/7 | 0,00% | -20,83% | DEBOLE | 16,3 | n/d |
| +20,00% | 97,07 $ | 7/40 | +17,50% | -8,00% | 74,42 $ | 0/7 | 0,00% | -23,33% | DEBOLE | 16,3 | n/d |
| +20,00% | 97,07 $ | 7/40 | +17,50% | -10,00% | 72,80 $ | 0/7 | 0,00% | -25,00% | DEBOLE | 16,3 | n/d |
| +20,00% | 97,07 $ | 7/40 | +17,50% | -15,00% | 68,76 $ | 0/7 | 0,00% | -29,17% | DEBOLE | 16,3 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 35 prima sono scesi a -5,00%. Tra quei 35, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +14,29% (5/35). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 15 prima sono saliti a +10,00%. Tra quei 15, 9 poi sono scaricati a -5,00%. Percentuale: +60,00% (9/15). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,07079 $ | 35/40 | +87,50% | +5,00% | 0,07825 $ | 7/35 | +20,00% | +10,53% | DEBOLE | 5,1 | 14,0 |
| -5,00% | 0,07079 $ | 35/40 | +87,50% | +10,00% | 0,08197 $ | 5/35 | +14,29% | +15,79% | DEBOLE | 5,1 | 11,8 |
| -5,00% | 0,07079 $ | 35/40 | +87,50% | +15,00% | 0,08570 $ | 5/35 | +14,29% | +21,05% | DEBOLE | 5,1 | 14,2 |
| -5,00% | 0,07079 $ | 35/40 | +87,50% | +20,00% | 0,08942 $ | 5/35 | +14,29% | +26,32% | DEBOLE | 5,1 | 14,8 |
| -8,00% | 0,06856 $ | 32/40 | +80,00% | +5,00% | 0,07825 $ | 5/32 | +15,62% | +14,13% | DEBOLE | 6,9 | 16,6 |
| -8,00% | 0,06856 $ | 32/40 | +80,00% | +10,00% | 0,08197 $ | 3/32 | +9,38% | +19,57% | DEBOLE | 6,9 | 14,0 |
| -8,00% | 0,06856 $ | 32/40 | +80,00% | +15,00% | 0,08570 $ | 3/32 | +9,38% | +25,00% | DEBOLE | 6,9 | 17,3 |
| -8,00% | 0,06856 $ | 32/40 | +80,00% | +20,00% | 0,08942 $ | 3/32 | +9,38% | +30,43% | DEBOLE | 6,9 | 17,7 |
| -10,00% | 0,06707 $ | 31/40 | +77,50% | +5,00% | 0,07825 $ | 4/31 | +12,90% | +16,67% | DEBOLE | 8,2 | 17,8 |
| -10,00% | 0,06707 $ | 31/40 | +77,50% | +10,00% | 0,08197 $ | 2/31 | +6,45% | +22,22% | DEBOLE | 8,2 | 15,0 |
| -10,00% | 0,06707 $ | 31/40 | +77,50% | +15,00% | 0,08570 $ | 2/31 | +6,45% | +27,78% | DEBOLE | 8,2 | 15,5 |
| -10,00% | 0,06707 $ | 31/40 | +77,50% | +20,00% | 0,08942 $ | 2/31 | +6,45% | +33,33% | DEBOLE | 8,2 | 15,5 |
| -15,00% | 0,06334 $ | 30/40 | +75,00% | +5,00% | 0,07825 $ | 3/30 | +10,00% | +23,53% | DEBOLE | 11,4 | 15,3 |
| -15,00% | 0,06334 $ | 30/40 | +75,00% | +10,00% | 0,08197 $ | 2/30 | +6,67% | +29,41% | DEBOLE | 11,4 | 15,0 |
| -15,00% | 0,06334 $ | 30/40 | +75,00% | +15,00% | 0,08570 $ | 2/30 | +6,67% | +35,29% | DEBOLE | 11,4 | 15,5 |
| -15,00% | 0,06334 $ | 30/40 | +75,00% | +20,00% | 0,08942 $ | 2/30 | +6,67% | +41,18% | DEBOLE | 11,4 | 15,5 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07825 $ | 18/40 | +45,00% | prezzo iniziale | 0,07452 $ | 15/18 | +83,33% | -4,76% | ALTA | 7,2 | 13,6 |
| +5,00% | 0,07825 $ | 18/40 | +45,00% | -5,00% | 0,07079 $ | 12/18 | +66,67% | -9,52% | ALTA | 7,2 | 15,8 |
| +5,00% | 0,07825 $ | 18/40 | +45,00% | -8,00% | 0,06856 $ | 9/18 | +50,00% | -12,38% | MEDIA | 7,2 | 14,9 |
| +5,00% | 0,07825 $ | 18/40 | +45,00% | -10,00% | 0,06707 $ | 8/18 | +44,44% | -14,29% | BASSA | 7,2 | 15,8 |
| +5,00% | 0,07825 $ | 18/40 | +45,00% | -15,00% | 0,06334 $ | 7/18 | +38,89% | -19,05% | BASSA | 7,2 | 14,9 |
| +10,00% | 0,08197 $ | 15/40 | +37,50% | prezzo iniziale | 0,07452 $ | 10/15 | +66,67% | -9,09% | ALTA | 9,1 | 14,9 |
| +10,00% | 0,08197 $ | 15/40 | +37,50% | -5,00% | 0,07079 $ | 9/15 | +60,00% | -13,64% | MEDIA | 9,1 | 14,3 |
| +10,00% | 0,08197 $ | 15/40 | +37,50% | -8,00% | 0,06856 $ | 7/15 | +46,67% | -16,36% | BASSA | 9,1 | 14,1 |
| +10,00% | 0,08197 $ | 15/40 | +37,50% | -10,00% | 0,06707 $ | 6/15 | +40,00% | -18,18% | BASSA | 9,1 | 15,2 |
| +10,00% | 0,08197 $ | 15/40 | +37,50% | -15,00% | 0,06334 $ | 6/15 | +40,00% | -22,73% | BASSA | 9,1 | 16,5 |
| +15,00% | 0,08570 $ | 10/40 | +25,00% | prezzo iniziale | 0,07452 $ | 5/10 | +50,00% | -13,04% | MEDIA | 10,7 | 16,6 |
| +15,00% | 0,08570 $ | 10/40 | +25,00% | -5,00% | 0,07079 $ | 4/10 | +40,00% | -17,39% | BASSA | 10,7 | 13,8 |
| +15,00% | 0,08570 $ | 10/40 | +25,00% | -8,00% | 0,06856 $ | 4/10 | +40,00% | -20,00% | BASSA | 10,7 | 14,2 |
| +15,00% | 0,08570 $ | 10/40 | +25,00% | -10,00% | 0,06707 $ | 3/10 | +30,00% | -21,74% | DEBOLE | 10,7 | 16,0 |
| +15,00% | 0,08570 $ | 10/40 | +25,00% | -15,00% | 0,06334 $ | 3/10 | +30,00% | -26,09% | DEBOLE | 10,7 | 17,3 |
| +20,00% | 0,08942 $ | 7/40 | +17,50% | prezzo iniziale | 0,07452 $ | 3/7 | +42,86% | -16,67% | BASSA | 14,6 | 19,0 |
| +20,00% | 0,08942 $ | 7/40 | +17,50% | -5,00% | 0,07079 $ | 2/7 | +28,57% | -20,83% | DEBOLE | 14,6 | 15,5 |
| +20,00% | 0,08942 $ | 7/40 | +17,50% | -8,00% | 0,06856 $ | 2/7 | +28,57% | -23,33% | DEBOLE | 14,6 | 16,0 |
| +20,00% | 0,08942 $ | 7/40 | +17,50% | -10,00% | 0,06707 $ | 2/7 | +28,57% | -25,00% | DEBOLE | 14,6 | 16,0 |
| +20,00% | 0,08942 $ | 7/40 | +17,50% | -15,00% | 0,06334 $ | 2/7 | +28,57% | -29,17% | DEBOLE | 14,6 | 18,0 |

---
