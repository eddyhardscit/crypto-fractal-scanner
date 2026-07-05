# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-05 14:45:36 CEST**  
UTC: **2026-07-05 12:45:36 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 59.535 $ | 68.935 $ | +22,73% | +15,79% | rimbalzo poco frequente | 68.935 $ | 59.535 $ | +18,18% | -13,64% | spike storicamente più resistente |
| SOL | 76,77 $ | 88,89 $ | +24,00% | +15,79% | rimbalzo poco frequente | 88,89 $ | 76,77 $ | +26,09% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07245 $ | 0,08389 $ | +11,76% | +15,79% | rimbalzo poco frequente | 0,08389 $ | 0,07245 $ | +64,71% | -13,64% | attenzione a prendere profitto |

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

- BTC: su 40 casi simili, 22 prima sono scesi a -5,00%. Tra quei 22, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +22,73% (5/22). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- BTC: su 40 casi simili, 22 prima sono saliti a +10,00%. Tra quei 22, 4 poi sono scaricati a -5,00%. Percentuale: +18,18% (4/22). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 59.535 $ | 22/40 | +55,00% | +5,00% | 65.801 $ | 6/22 | +27,27% | +10,53% | DEBOLE | 10,0 | 10,2 |
| -5,00% | 59.535 $ | 22/40 | +55,00% | +10,00% | 68.935 $ | 5/22 | +22,73% | +15,79% | DEBOLE | 10,0 | 11,0 |
| -5,00% | 59.535 $ | 22/40 | +55,00% | +15,00% | 72.068 $ | 4/22 | +18,18% | +21,05% | DEBOLE | 10,0 | 15,2 |
| -5,00% | 59.535 $ | 22/40 | +55,00% | +20,00% | 75.202 $ | 4/22 | +18,18% | +26,32% | DEBOLE | 10,0 | 16,8 |
| -8,00% | 57.654 $ | 17/40 | +42,50% | +5,00% | 65.801 $ | 5/17 | +29,41% | +14,13% | DEBOLE | 9,6 | 10,6 |
| -8,00% | 57.654 $ | 17/40 | +42,50% | +10,00% | 68.935 $ | 4/17 | +23,53% | +19,57% | DEBOLE | 9,6 | 10,2 |
| -8,00% | 57.654 $ | 17/40 | +42,50% | +15,00% | 72.068 $ | 3/17 | +17,65% | +25,00% | DEBOLE | 9,6 | 15,0 |
| -8,00% | 57.654 $ | 17/40 | +42,50% | +20,00% | 75.202 $ | 3/17 | +17,65% | +30,43% | DEBOLE | 9,6 | 16,0 |
| -10,00% | 56.401 $ | 12/40 | +30,00% | +5,00% | 65.801 $ | 3/12 | +25,00% | +16,67% | DEBOLE | 7,1 | 15,7 |
| -10,00% | 56.401 $ | 12/40 | +30,00% | +10,00% | 68.935 $ | 2/12 | +16,67% | +22,22% | DEBOLE | 7,1 | 17,5 |
| -10,00% | 56.401 $ | 12/40 | +30,00% | +15,00% | 72.068 $ | 2/12 | +16,67% | +27,78% | DEBOLE | 7,1 | 18,5 |
| -10,00% | 56.401 $ | 12/40 | +30,00% | +20,00% | 75.202 $ | 2/12 | +16,67% | +33,33% | DEBOLE | 7,1 | 18,5 |
| -15,00% | 53.268 $ | 10/40 | +25,00% | +5,00% | 65.801 $ | 1/10 | +10,00% | +23,53% | DEBOLE | 8,4 | 16,0 |
| -15,00% | 53.268 $ | 10/40 | +25,00% | +10,00% | 68.935 $ | 1/10 | +10,00% | +29,41% | DEBOLE | 8,4 | 25,0 |
| -15,00% | 53.268 $ | 10/40 | +25,00% | +15,00% | 72.068 $ | 1/10 | +10,00% | +35,29% | DEBOLE | 8,4 | 26,0 |
| -15,00% | 53.268 $ | 10/40 | +25,00% | +20,00% | 75.202 $ | 1/10 | +10,00% | +41,18% | DEBOLE | 8,4 | 26,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 65.801 $ | 30/40 | +75,00% | prezzo iniziale | 62.668 $ | 21/30 | +70,00% | -4,76% | ALTA | 7,2 | 17,5 |
| +5,00% | 65.801 $ | 30/40 | +75,00% | -5,00% | 59.535 $ | 9/30 | +30,00% | -9,52% | DEBOLE | 7,2 | 20,6 |
| +5,00% | 65.801 $ | 30/40 | +75,00% | -8,00% | 57.654 $ | 5/30 | +16,67% | -12,38% | DEBOLE | 7,2 | 21,8 |
| +5,00% | 65.801 $ | 30/40 | +75,00% | -10,00% | 56.401 $ | 3/30 | +10,00% | -14,29% | DEBOLE | 7,2 | 16,7 |
| +5,00% | 65.801 $ | 30/40 | +75,00% | -15,00% | 53.268 $ | 3/30 | +10,00% | -19,05% | DEBOLE | 7,2 | 17,0 |
| +10,00% | 68.935 $ | 22/40 | +55,00% | prezzo iniziale | 62.668 $ | 10/22 | +45,45% | -9,09% | BASSA | 9,9 | 20,9 |
| +10,00% | 68.935 $ | 22/40 | +55,00% | -5,00% | 59.535 $ | 4/22 | +18,18% | -13,64% | DEBOLE | 9,9 | 22,5 |
| +10,00% | 68.935 $ | 22/40 | +55,00% | -8,00% | 57.654 $ | 4/22 | +18,18% | -16,36% | DEBOLE | 9,9 | 26,0 |
| +10,00% | 68.935 $ | 22/40 | +55,00% | -10,00% | 56.401 $ | 2/22 | +9,09% | -18,18% | DEBOLE | 9,9 | 22,5 |
| +10,00% | 68.935 $ | 22/40 | +55,00% | -15,00% | 53.268 $ | 2/22 | +9,09% | -22,73% | DEBOLE | 9,9 | 23,0 |
| +15,00% | 72.068 $ | 17/40 | +42,50% | prezzo iniziale | 62.668 $ | 5/17 | +29,41% | -13,04% | DEBOLE | 12,0 | 26,0 |
| +15,00% | 72.068 $ | 17/40 | +42,50% | -5,00% | 59.535 $ | 2/17 | +11,76% | -17,39% | DEBOLE | 12,0 | 22,0 |
| +15,00% | 72.068 $ | 17/40 | +42,50% | -8,00% | 57.654 $ | 2/17 | +11,76% | -20,00% | DEBOLE | 12,0 | 22,5 |
| +15,00% | 72.068 $ | 17/40 | +42,50% | -10,00% | 56.401 $ | 2/17 | +11,76% | -21,74% | DEBOLE | 12,0 | 22,5 |
| +15,00% | 72.068 $ | 17/40 | +42,50% | -15,00% | 53.268 $ | 2/17 | +11,76% | -26,09% | DEBOLE | 12,0 | 23,0 |
| +20,00% | 75.202 $ | 14/40 | +35,00% | prezzo iniziale | 62.668 $ | 2/14 | +14,29% | -16,67% | DEBOLE | 13,4 | 22,5 |
| +20,00% | 75.202 $ | 14/40 | +35,00% | -5,00% | 59.535 $ | 1/14 | +7,14% | -20,83% | DEBOLE | 13,4 | 16,0 |
| +20,00% | 75.202 $ | 14/40 | +35,00% | -8,00% | 57.654 $ | 1/14 | +7,14% | -23,33% | DEBOLE | 13,4 | 16,0 |
| +20,00% | 75.202 $ | 14/40 | +35,00% | -10,00% | 56.401 $ | 1/14 | +7,14% | -25,00% | DEBOLE | 13,4 | 16,0 |
| +20,00% | 75.202 $ | 14/40 | +35,00% | -15,00% | 53.268 $ | 1/14 | +7,14% | -29,17% | DEBOLE | 13,4 | 17,0 |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 25 prima sono scesi a -5,00%. Tra quei 25, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +24,00% (6/25). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 23 prima sono saliti a +10,00%. Tra quei 23, 6 poi sono scaricati a -5,00%. Percentuale: +26,09% (6/23). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 76,77 $ | 25/40 | +62,50% | +5,00% | 84,85 $ | 7/25 | +28,00% | +10,53% | DEBOLE | 8,4 | 13,0 |
| -5,00% | 76,77 $ | 25/40 | +62,50% | +10,00% | 88,89 $ | 6/25 | +24,00% | +15,79% | DEBOLE | 8,4 | 17,0 |
| -5,00% | 76,77 $ | 25/40 | +62,50% | +15,00% | 92,93 $ | 4/25 | +16,00% | +21,05% | DEBOLE | 8,4 | 19,5 |
| -5,00% | 76,77 $ | 25/40 | +62,50% | +20,00% | 96,97 $ | 3/25 | +12,00% | +26,32% | DEBOLE | 8,4 | 21,7 |
| -8,00% | 74,35 $ | 21/40 | +52,50% | +5,00% | 84,85 $ | 4/21 | +19,05% | +14,13% | DEBOLE | 11,7 | 15,8 |
| -8,00% | 74,35 $ | 21/40 | +52,50% | +10,00% | 88,89 $ | 4/21 | +19,05% | +19,57% | DEBOLE | 11,7 | 19,0 |
| -8,00% | 74,35 $ | 21/40 | +52,50% | +15,00% | 92,93 $ | 3/21 | +14,29% | +25,00% | DEBOLE | 11,7 | 19,3 |
| -8,00% | 74,35 $ | 21/40 | +52,50% | +20,00% | 96,97 $ | 2/21 | +9,52% | +30,43% | DEBOLE | 11,7 | 21,5 |
| -10,00% | 72,73 $ | 17/40 | +42,50% | +5,00% | 84,85 $ | 4/17 | +23,53% | +16,67% | DEBOLE | 10,5 | 15,8 |
| -10,00% | 72,73 $ | 17/40 | +42,50% | +10,00% | 88,89 $ | 4/17 | +23,53% | +22,22% | DEBOLE | 10,5 | 19,0 |
| -10,00% | 72,73 $ | 17/40 | +42,50% | +15,00% | 92,93 $ | 3/17 | +17,65% | +27,78% | DEBOLE | 10,5 | 19,3 |
| -10,00% | 72,73 $ | 17/40 | +42,50% | +20,00% | 96,97 $ | 2/17 | +11,76% | +33,33% | DEBOLE | 10,5 | 21,5 |
| -15,00% | 68,69 $ | 13/40 | +32,50% | +5,00% | 84,85 $ | 3/13 | +23,08% | +23,53% | DEBOLE | 12,9 | 16,3 |
| -15,00% | 68,69 $ | 13/40 | +32,50% | +10,00% | 88,89 $ | 3/13 | +23,08% | +29,41% | DEBOLE | 12,9 | 20,0 |
| -15,00% | 68,69 $ | 13/40 | +32,50% | +15,00% | 92,93 $ | 2/13 | +15,38% | +35,29% | DEBOLE | 12,9 | 20,5 |
| -15,00% | 68,69 $ | 13/40 | +32,50% | +20,00% | 96,97 $ | 1/13 | +7,69% | +41,18% | DEBOLE | 12,9 | 26,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 84,85 $ | 31/40 | +77,50% | prezzo iniziale | 80,81 $ | 25/31 | +80,65% | -4,76% | ALTA | 6,6 | 13,4 |
| +5,00% | 84,85 $ | 31/40 | +77,50% | -5,00% | 76,77 $ | 13/31 | +41,94% | -9,52% | BASSA | 6,6 | 13,8 |
| +5,00% | 84,85 $ | 31/40 | +77,50% | -8,00% | 74,35 $ | 12/31 | +38,71% | -12,38% | BASSA | 6,6 | 14,8 |
| +5,00% | 84,85 $ | 31/40 | +77,50% | -10,00% | 72,73 $ | 8/31 | +25,81% | -14,29% | DEBOLE | 6,6 | 10,9 |
| +5,00% | 84,85 $ | 31/40 | +77,50% | -15,00% | 68,69 $ | 7/31 | +22,58% | -19,05% | DEBOLE | 6,6 | 15,0 |
| +10,00% | 88,89 $ | 23/40 | +57,50% | prezzo iniziale | 80,81 $ | 11/23 | +47,83% | -9,09% | BASSA | 11,2 | 17,5 |
| +10,00% | 88,89 $ | 23/40 | +57,50% | -5,00% | 76,77 $ | 6/23 | +26,09% | -13,64% | DEBOLE | 11,2 | 17,3 |
| +10,00% | 88,89 $ | 23/40 | +57,50% | -8,00% | 74,35 $ | 6/23 | +26,09% | -16,36% | DEBOLE | 11,2 | 17,7 |
| +10,00% | 88,89 $ | 23/40 | +57,50% | -10,00% | 72,73 $ | 4/23 | +17,39% | -18,18% | DEBOLE | 11,2 | 15,5 |
| +10,00% | 88,89 $ | 23/40 | +57,50% | -15,00% | 68,69 $ | 3/23 | +13,04% | -22,73% | DEBOLE | 11,2 | 19,3 |
| +15,00% | 92,93 $ | 18/40 | +45,00% | prezzo iniziale | 80,81 $ | 7/18 | +38,89% | -13,04% | BASSA | 13,8 | 16,3 |
| +15,00% | 92,93 $ | 18/40 | +45,00% | -5,00% | 76,77 $ | 5/18 | +27,78% | -17,39% | DEBOLE | 13,8 | 17,0 |
| +15,00% | 92,93 $ | 18/40 | +45,00% | -8,00% | 74,35 $ | 5/18 | +27,78% | -20,00% | DEBOLE | 13,8 | 17,4 |
| +15,00% | 92,93 $ | 18/40 | +45,00% | -10,00% | 72,73 $ | 3/18 | +16,67% | -21,74% | DEBOLE | 13,8 | 14,3 |
| +15,00% | 92,93 $ | 18/40 | +45,00% | -15,00% | 68,69 $ | 2/18 | +11,11% | -26,09% | DEBOLE | 13,8 | 19,5 |
| +20,00% | 96,97 $ | 13/40 | +32,50% | prezzo iniziale | 80,81 $ | 2/13 | +15,38% | -16,67% | DEBOLE | 16,6 | 18,5 |
| +20,00% | 96,97 $ | 13/40 | +32,50% | -5,00% | 76,77 $ | 2/13 | +15,38% | -20,83% | DEBOLE | 16,6 | 19,0 |
| +20,00% | 96,97 $ | 13/40 | +32,50% | -8,00% | 74,35 $ | 2/13 | +15,38% | -23,33% | DEBOLE | 16,6 | 19,0 |
| +20,00% | 96,97 $ | 13/40 | +32,50% | -10,00% | 72,73 $ | 2/13 | +15,38% | -25,00% | DEBOLE | 16,6 | 19,0 |
| +20,00% | 96,97 $ | 13/40 | +32,50% | -15,00% | 68,69 $ | 2/13 | +15,38% | -29,17% | DEBOLE | 16,6 | 19,5 |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 34 prima sono scesi a -5,00%. Tra quei 34, 4 poi sono rimbalzati fino a +10,00%. Percentuale: +11,76% (4/34). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 17 prima sono saliti a +10,00%. Tra quei 17, 11 poi sono scaricati a -5,00%. Percentuale: +64,71% (11/17). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,07245 $ | 34/40 | +85,00% | +5,00% | 0,08007 $ | 9/34 | +26,47% | +10,53% | DEBOLE | 7,1 | 13,3 |
| -5,00% | 0,07245 $ | 34/40 | +85,00% | +10,00% | 0,08389 $ | 4/34 | +11,76% | +15,79% | DEBOLE | 7,1 | 14,2 |
| -5,00% | 0,07245 $ | 34/40 | +85,00% | +15,00% | 0,08770 $ | 3/34 | +8,82% | +21,05% | DEBOLE | 7,1 | 12,3 |
| -5,00% | 0,07245 $ | 34/40 | +85,00% | +20,00% | 0,09151 $ | 3/34 | +8,82% | +26,32% | DEBOLE | 7,1 | 12,7 |
| -8,00% | 0,07016 $ | 31/40 | +77,50% | +5,00% | 0,08007 $ | 6/31 | +19,35% | +14,13% | DEBOLE | 8,9 | 15,5 |
| -8,00% | 0,07016 $ | 31/40 | +77,50% | +10,00% | 0,08389 $ | 3/31 | +9,68% | +19,57% | DEBOLE | 8,9 | 13,3 |
| -8,00% | 0,07016 $ | 31/40 | +77,50% | +15,00% | 0,08770 $ | 2/31 | +6,45% | +25,00% | DEBOLE | 8,9 | 5,5 |
| -8,00% | 0,07016 $ | 31/40 | +77,50% | +20,00% | 0,09151 $ | 2/31 | +6,45% | +30,43% | DEBOLE | 8,9 | 5,5 |
| -10,00% | 0,06863 $ | 29/40 | +72,50% | +5,00% | 0,08007 $ | 4/29 | +13,79% | +16,67% | DEBOLE | 10,3 | 17,2 |
| -10,00% | 0,06863 $ | 29/40 | +72,50% | +10,00% | 0,08389 $ | 3/29 | +10,34% | +22,22% | DEBOLE | 10,3 | 13,3 |
| -10,00% | 0,06863 $ | 29/40 | +72,50% | +15,00% | 0,08770 $ | 2/29 | +6,90% | +27,78% | DEBOLE | 10,3 | 5,5 |
| -10,00% | 0,06863 $ | 29/40 | +72,50% | +20,00% | 0,09151 $ | 2/29 | +6,90% | +33,33% | DEBOLE | 10,3 | 5,5 |
| -15,00% | 0,06482 $ | 27/40 | +67,50% | +5,00% | 0,08007 $ | 2/27 | +7,41% | +23,53% | DEBOLE | 13,7 | 17,5 |
| -15,00% | 0,06482 $ | 27/40 | +67,50% | +10,00% | 0,08389 $ | 2/27 | +7,41% | +29,41% | DEBOLE | 13,7 | 17,5 |
| -15,00% | 0,06482 $ | 27/40 | +67,50% | +15,00% | 0,08770 $ | 1/27 | +3,70% | +35,29% | DEBOLE | 13,7 | 5,0 |
| -15,00% | 0,06482 $ | 27/40 | +67,50% | +20,00% | 0,09151 $ | 1/27 | +3,70% | +41,18% | DEBOLE | 13,7 | 5,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,08007 $ | 24/40 | +60,00% | prezzo iniziale | 0,07626 $ | 18/24 | +75,00% | -4,76% | ALTA | 7,1 | 12,9 |
| +5,00% | 0,08007 $ | 24/40 | +60,00% | -5,00% | 0,07245 $ | 15/24 | +62,50% | -9,52% | MEDIA | 7,1 | 15,8 |
| +5,00% | 0,08007 $ | 24/40 | +60,00% | -8,00% | 0,07016 $ | 12/24 | +50,00% | -12,38% | MEDIA | 7,1 | 15,9 |
| +5,00% | 0,08007 $ | 24/40 | +60,00% | -10,00% | 0,06863 $ | 12/24 | +50,00% | -14,29% | MEDIA | 7,1 | 16,8 |
| +5,00% | 0,08007 $ | 24/40 | +60,00% | -15,00% | 0,06482 $ | 11/24 | +45,83% | -19,05% | BASSA | 7,1 | 17,2 |
| +10,00% | 0,08389 $ | 17/40 | +42,50% | prezzo iniziale | 0,07626 $ | 13/17 | +76,47% | -9,09% | ALTA | 7,9 | 15,5 |
| +10,00% | 0,08389 $ | 17/40 | +42,50% | -5,00% | 0,07245 $ | 11/17 | +64,71% | -13,64% | MEDIA | 7,9 | 17,1 |
| +10,00% | 0,08389 $ | 17/40 | +42,50% | -8,00% | 0,07016 $ | 8/17 | +47,06% | -16,36% | BASSA | 7,9 | 16,5 |
| +10,00% | 0,08389 $ | 17/40 | +42,50% | -10,00% | 0,06863 $ | 8/17 | +47,06% | -18,18% | BASSA | 7,9 | 17,4 |
| +10,00% | 0,08389 $ | 17/40 | +42,50% | -15,00% | 0,06482 $ | 7/17 | +41,18% | -22,73% | BASSA | 7,9 | 17,6 |
| +15,00% | 0,08770 $ | 8/40 | +20,00% | prezzo iniziale | 0,07626 $ | 6/8 | +75,00% | -13,04% | ALTA | 9,1 | 17,3 |
| +15,00% | 0,08770 $ | 8/40 | +20,00% | -5,00% | 0,07245 $ | 4/8 | +50,00% | -17,39% | MEDIA | 9,1 | 16,8 |
| +15,00% | 0,08770 $ | 8/40 | +20,00% | -8,00% | 0,07016 $ | 3/8 | +37,50% | -20,00% | BASSA | 9,1 | 18,0 |
| +15,00% | 0,08770 $ | 8/40 | +20,00% | -10,00% | 0,06863 $ | 3/8 | +37,50% | -21,74% | BASSA | 9,1 | 19,7 |
| +15,00% | 0,08770 $ | 8/40 | +20,00% | -15,00% | 0,06482 $ | 2/8 | +25,00% | -26,09% | DEBOLE | 9,1 | 19,0 |
| +20,00% | 0,09151 $ | 6/40 | +15,00% | prezzo iniziale | 0,07626 $ | 4/6 | +66,67% | -16,67% | ALTA | 10,0 | 15,0 |
| +20,00% | 0,09151 $ | 6/40 | +15,00% | -5,00% | 0,07245 $ | 3/6 | +50,00% | -20,83% | MEDIA | 10,0 | 17,3 |
| +20,00% | 0,09151 $ | 6/40 | +15,00% | -8,00% | 0,07016 $ | 2/6 | +33,33% | -23,33% | DEBOLE | 10,0 | 19,0 |
| +20,00% | 0,09151 $ | 6/40 | +15,00% | -10,00% | 0,06863 $ | 2/6 | +33,33% | -25,00% | DEBOLE | 10,0 | 21,5 |
| +20,00% | 0,09151 $ | 6/40 | +15,00% | -15,00% | 0,06482 $ | 1/6 | +16,67% | -29,17% | DEBOLE | 10,0 | 22,0 |

---
