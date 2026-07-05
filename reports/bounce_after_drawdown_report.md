# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-05 10:38:55 CEST**  
UTC: **2026-07-05 08:38:55 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 59.726 $ | 69.156 $ | +22,73% | +15,79% | rimbalzo poco frequente | 69.156 $ | 59.726 $ | +18,18% | -13,64% | spike storicamente più resistente |
| SOL | 76,47 $ | 88,55 $ | +20,83% | +15,79% | rimbalzo poco frequente | 88,55 $ | 76,47 $ | +21,74% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07222 $ | 0,08362 $ | +11,76% | +15,79% | rimbalzo poco frequente | 0,08362 $ | 0,07222 $ | +64,71% | -13,64% | attenzione a prendere profitto |

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
| -5,00% | 59.726 $ | 22/40 | +55,00% | +5,00% | 66.012 $ | 6/22 | +27,27% | +10,53% | DEBOLE | 10,0 | 10,2 |
| -5,00% | 59.726 $ | 22/40 | +55,00% | +10,00% | 69.156 $ | 5/22 | +22,73% | +15,79% | DEBOLE | 10,0 | 11,0 |
| -5,00% | 59.726 $ | 22/40 | +55,00% | +15,00% | 72.299 $ | 4/22 | +18,18% | +21,05% | DEBOLE | 10,0 | 15,2 |
| -5,00% | 59.726 $ | 22/40 | +55,00% | +20,00% | 75.443 $ | 4/22 | +18,18% | +26,32% | DEBOLE | 10,0 | 16,8 |
| -8,00% | 57.839 $ | 17/40 | +42,50% | +5,00% | 66.012 $ | 5/17 | +29,41% | +14,13% | DEBOLE | 9,6 | 10,6 |
| -8,00% | 57.839 $ | 17/40 | +42,50% | +10,00% | 69.156 $ | 4/17 | +23,53% | +19,57% | DEBOLE | 9,6 | 10,2 |
| -8,00% | 57.839 $ | 17/40 | +42,50% | +15,00% | 72.299 $ | 3/17 | +17,65% | +25,00% | DEBOLE | 9,6 | 15,0 |
| -8,00% | 57.839 $ | 17/40 | +42,50% | +20,00% | 75.443 $ | 3/17 | +17,65% | +30,43% | DEBOLE | 9,6 | 16,0 |
| -10,00% | 56.582 $ | 12/40 | +30,00% | +5,00% | 66.012 $ | 3/12 | +25,00% | +16,67% | DEBOLE | 7,1 | 15,7 |
| -10,00% | 56.582 $ | 12/40 | +30,00% | +10,00% | 69.156 $ | 2/12 | +16,67% | +22,22% | DEBOLE | 7,1 | 17,5 |
| -10,00% | 56.582 $ | 12/40 | +30,00% | +15,00% | 72.299 $ | 2/12 | +16,67% | +27,78% | DEBOLE | 7,1 | 18,5 |
| -10,00% | 56.582 $ | 12/40 | +30,00% | +20,00% | 75.443 $ | 2/12 | +16,67% | +33,33% | DEBOLE | 7,1 | 18,5 |
| -15,00% | 53.439 $ | 10/40 | +25,00% | +5,00% | 66.012 $ | 1/10 | +10,00% | +23,53% | DEBOLE | 8,4 | 16,0 |
| -15,00% | 53.439 $ | 10/40 | +25,00% | +10,00% | 69.156 $ | 1/10 | +10,00% | +29,41% | DEBOLE | 8,4 | 25,0 |
| -15,00% | 53.439 $ | 10/40 | +25,00% | +15,00% | 72.299 $ | 1/10 | +10,00% | +35,29% | DEBOLE | 8,4 | 26,0 |
| -15,00% | 53.439 $ | 10/40 | +25,00% | +20,00% | 75.443 $ | 1/10 | +10,00% | +41,18% | DEBOLE | 8,4 | 26,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 66.012 $ | 30/40 | +75,00% | prezzo iniziale | 62.869 $ | 21/30 | +70,00% | -4,76% | ALTA | 7,2 | 17,5 |
| +5,00% | 66.012 $ | 30/40 | +75,00% | -5,00% | 59.726 $ | 9/30 | +30,00% | -9,52% | DEBOLE | 7,2 | 20,6 |
| +5,00% | 66.012 $ | 30/40 | +75,00% | -8,00% | 57.839 $ | 5/30 | +16,67% | -12,38% | DEBOLE | 7,2 | 21,8 |
| +5,00% | 66.012 $ | 30/40 | +75,00% | -10,00% | 56.582 $ | 3/30 | +10,00% | -14,29% | DEBOLE | 7,2 | 16,7 |
| +5,00% | 66.012 $ | 30/40 | +75,00% | -15,00% | 53.439 $ | 3/30 | +10,00% | -19,05% | DEBOLE | 7,2 | 17,0 |
| +10,00% | 69.156 $ | 22/40 | +55,00% | prezzo iniziale | 62.869 $ | 10/22 | +45,45% | -9,09% | BASSA | 9,9 | 20,9 |
| +10,00% | 69.156 $ | 22/40 | +55,00% | -5,00% | 59.726 $ | 4/22 | +18,18% | -13,64% | DEBOLE | 9,9 | 22,5 |
| +10,00% | 69.156 $ | 22/40 | +55,00% | -8,00% | 57.839 $ | 4/22 | +18,18% | -16,36% | DEBOLE | 9,9 | 26,0 |
| +10,00% | 69.156 $ | 22/40 | +55,00% | -10,00% | 56.582 $ | 2/22 | +9,09% | -18,18% | DEBOLE | 9,9 | 22,5 |
| +10,00% | 69.156 $ | 22/40 | +55,00% | -15,00% | 53.439 $ | 2/22 | +9,09% | -22,73% | DEBOLE | 9,9 | 23,0 |
| +15,00% | 72.299 $ | 17/40 | +42,50% | prezzo iniziale | 62.869 $ | 5/17 | +29,41% | -13,04% | DEBOLE | 12,0 | 26,0 |
| +15,00% | 72.299 $ | 17/40 | +42,50% | -5,00% | 59.726 $ | 2/17 | +11,76% | -17,39% | DEBOLE | 12,0 | 22,0 |
| +15,00% | 72.299 $ | 17/40 | +42,50% | -8,00% | 57.839 $ | 2/17 | +11,76% | -20,00% | DEBOLE | 12,0 | 22,5 |
| +15,00% | 72.299 $ | 17/40 | +42,50% | -10,00% | 56.582 $ | 2/17 | +11,76% | -21,74% | DEBOLE | 12,0 | 22,5 |
| +15,00% | 72.299 $ | 17/40 | +42,50% | -15,00% | 53.439 $ | 2/17 | +11,76% | -26,09% | DEBOLE | 12,0 | 23,0 |
| +20,00% | 75.443 $ | 14/40 | +35,00% | prezzo iniziale | 62.869 $ | 2/14 | +14,29% | -16,67% | DEBOLE | 13,4 | 22,5 |
| +20,00% | 75.443 $ | 14/40 | +35,00% | -5,00% | 59.726 $ | 1/14 | +7,14% | -20,83% | DEBOLE | 13,4 | 16,0 |
| +20,00% | 75.443 $ | 14/40 | +35,00% | -8,00% | 57.839 $ | 1/14 | +7,14% | -23,33% | DEBOLE | 13,4 | 16,0 |
| +20,00% | 75.443 $ | 14/40 | +35,00% | -10,00% | 56.582 $ | 1/14 | +7,14% | -25,00% | DEBOLE | 13,4 | 16,0 |
| +20,00% | 75.443 $ | 14/40 | +35,00% | -15,00% | 53.439 $ | 1/14 | +7,14% | -29,17% | DEBOLE | 13,4 | 17,0 |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 24 prima sono scesi a -5,00%. Tra quei 24, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +20,83% (5/24). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 23 prima sono saliti a +10,00%. Tra quei 23, 5 poi sono scaricati a -5,00%. Percentuale: +21,74% (5/23). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 76,47 $ | 24/40 | +60,00% | +5,00% | 84,53 $ | 6/24 | +25,00% | +10,53% | DEBOLE | 8,0 | 11,8 |
| -5,00% | 76,47 $ | 24/40 | +60,00% | +10,00% | 88,55 $ | 5/24 | +20,83% | +15,79% | DEBOLE | 8,0 | 16,4 |
| -5,00% | 76,47 $ | 24/40 | +60,00% | +15,00% | 92,57 $ | 4/24 | +16,67% | +21,05% | DEBOLE | 8,0 | 19,5 |
| -5,00% | 76,47 $ | 24/40 | +60,00% | +20,00% | 96,60 $ | 3/24 | +12,50% | +26,32% | DEBOLE | 8,0 | 21,7 |
| -8,00% | 74,06 $ | 20/40 | +50,00% | +5,00% | 84,53 $ | 3/20 | +15,00% | +14,13% | DEBOLE | 11,3 | 14,3 |
| -8,00% | 74,06 $ | 20/40 | +50,00% | +10,00% | 88,55 $ | 3/20 | +15,00% | +19,57% | DEBOLE | 11,3 | 18,7 |
| -8,00% | 74,06 $ | 20/40 | +50,00% | +15,00% | 92,57 $ | 3/20 | +15,00% | +25,00% | DEBOLE | 11,3 | 19,3 |
| -8,00% | 74,06 $ | 20/40 | +50,00% | +20,00% | 96,60 $ | 2/20 | +10,00% | +30,43% | DEBOLE | 11,3 | 21,5 |
| -10,00% | 72,45 $ | 16/40 | +40,00% | +5,00% | 84,53 $ | 3/16 | +18,75% | +16,67% | DEBOLE | 9,9 | 14,3 |
| -10,00% | 72,45 $ | 16/40 | +40,00% | +10,00% | 88,55 $ | 3/16 | +18,75% | +22,22% | DEBOLE | 9,9 | 18,7 |
| -10,00% | 72,45 $ | 16/40 | +40,00% | +15,00% | 92,57 $ | 3/16 | +18,75% | +27,78% | DEBOLE | 9,9 | 19,3 |
| -10,00% | 72,45 $ | 16/40 | +40,00% | +20,00% | 96,60 $ | 2/16 | +12,50% | +33,33% | DEBOLE | 9,9 | 21,5 |
| -15,00% | 68,42 $ | 12/40 | +30,00% | +5,00% | 84,53 $ | 2/12 | +16,67% | +23,53% | DEBOLE | 12,4 | 14,5 |
| -15,00% | 68,42 $ | 12/40 | +30,00% | +10,00% | 88,55 $ | 2/12 | +16,67% | +29,41% | DEBOLE | 12,4 | 20,0 |
| -15,00% | 68,42 $ | 12/40 | +30,00% | +15,00% | 92,57 $ | 2/12 | +16,67% | +35,29% | DEBOLE | 12,4 | 20,5 |
| -15,00% | 68,42 $ | 12/40 | +30,00% | +20,00% | 96,60 $ | 1/12 | +8,33% | +41,18% | DEBOLE | 12,4 | 26,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 84,53 $ | 31/40 | +77,50% | prezzo iniziale | 80,50 $ | 25/31 | +80,65% | -4,76% | ALTA | 6,7 | 13,3 |
| +5,00% | 84,53 $ | 31/40 | +77,50% | -5,00% | 76,47 $ | 12/31 | +38,71% | -9,52% | BASSA | 6,7 | 13,4 |
| +5,00% | 84,53 $ | 31/40 | +77,50% | -8,00% | 74,06 $ | 11/31 | +35,48% | -12,38% | BASSA | 6,7 | 14,4 |
| +5,00% | 84,53 $ | 31/40 | +77,50% | -10,00% | 72,45 $ | 7/31 | +22,58% | -14,29% | DEBOLE | 6,7 | 9,7 |
| +5,00% | 84,53 $ | 31/40 | +77,50% | -15,00% | 68,42 $ | 6/31 | +19,35% | -19,05% | DEBOLE | 6,7 | 14,3 |
| +10,00% | 88,55 $ | 23/40 | +57,50% | prezzo iniziale | 80,50 $ | 11/23 | +47,83% | -9,09% | BASSA | 11,1 | 17,3 |
| +10,00% | 88,55 $ | 23/40 | +57,50% | -5,00% | 76,47 $ | 5/23 | +21,74% | -13,64% | DEBOLE | 11,1 | 17,0 |
| +10,00% | 88,55 $ | 23/40 | +57,50% | -8,00% | 74,06 $ | 5/23 | +21,74% | -16,36% | DEBOLE | 11,1 | 17,4 |
| +10,00% | 88,55 $ | 23/40 | +57,50% | -10,00% | 72,45 $ | 3/23 | +13,04% | -18,18% | DEBOLE | 11,1 | 14,3 |
| +10,00% | 88,55 $ | 23/40 | +57,50% | -15,00% | 68,42 $ | 2/23 | +8,70% | -22,73% | DEBOLE | 11,1 | 19,5 |
| +15,00% | 92,57 $ | 18/40 | +45,00% | prezzo iniziale | 80,50 $ | 7/18 | +38,89% | -13,04% | BASSA | 13,8 | 16,3 |
| +15,00% | 92,57 $ | 18/40 | +45,00% | -5,00% | 76,47 $ | 5/18 | +27,78% | -17,39% | DEBOLE | 13,8 | 17,0 |
| +15,00% | 92,57 $ | 18/40 | +45,00% | -8,00% | 74,06 $ | 5/18 | +27,78% | -20,00% | DEBOLE | 13,8 | 17,4 |
| +15,00% | 92,57 $ | 18/40 | +45,00% | -10,00% | 72,45 $ | 3/18 | +16,67% | -21,74% | DEBOLE | 13,8 | 14,3 |
| +15,00% | 92,57 $ | 18/40 | +45,00% | -15,00% | 68,42 $ | 2/18 | +11,11% | -26,09% | DEBOLE | 13,8 | 19,5 |
| +20,00% | 96,60 $ | 13/40 | +32,50% | prezzo iniziale | 80,50 $ | 2/13 | +15,38% | -16,67% | DEBOLE | 16,6 | 18,5 |
| +20,00% | 96,60 $ | 13/40 | +32,50% | -5,00% | 76,47 $ | 2/13 | +15,38% | -20,83% | DEBOLE | 16,6 | 19,0 |
| +20,00% | 96,60 $ | 13/40 | +32,50% | -8,00% | 74,06 $ | 2/13 | +15,38% | -23,33% | DEBOLE | 16,6 | 19,0 |
| +20,00% | 96,60 $ | 13/40 | +32,50% | -10,00% | 72,45 $ | 2/13 | +15,38% | -25,00% | DEBOLE | 16,6 | 19,0 |
| +20,00% | 96,60 $ | 13/40 | +32,50% | -15,00% | 68,42 $ | 2/13 | +15,38% | -29,17% | DEBOLE | 16,6 | 19,5 |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 34 prima sono scesi a -5,00%. Tra quei 34, 4 poi sono rimbalzati fino a +10,00%. Percentuale: +11,76% (4/34). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 17 prima sono saliti a +10,00%. Tra quei 17, 11 poi sono scaricati a -5,00%. Percentuale: +64,71% (11/17). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,07222 $ | 34/40 | +85,00% | +5,00% | 0,07982 $ | 9/34 | +26,47% | +10,53% | DEBOLE | 7,1 | 13,3 |
| -5,00% | 0,07222 $ | 34/40 | +85,00% | +10,00% | 0,08362 $ | 4/34 | +11,76% | +15,79% | DEBOLE | 7,1 | 14,2 |
| -5,00% | 0,07222 $ | 34/40 | +85,00% | +15,00% | 0,08742 $ | 3/34 | +8,82% | +21,05% | DEBOLE | 7,1 | 12,3 |
| -5,00% | 0,07222 $ | 34/40 | +85,00% | +20,00% | 0,09122 $ | 3/34 | +8,82% | +26,32% | DEBOLE | 7,1 | 12,7 |
| -8,00% | 0,06994 $ | 31/40 | +77,50% | +5,00% | 0,07982 $ | 6/31 | +19,35% | +14,13% | DEBOLE | 8,9 | 15,5 |
| -8,00% | 0,06994 $ | 31/40 | +77,50% | +10,00% | 0,08362 $ | 3/31 | +9,68% | +19,57% | DEBOLE | 8,9 | 13,3 |
| -8,00% | 0,06994 $ | 31/40 | +77,50% | +15,00% | 0,08742 $ | 2/31 | +6,45% | +25,00% | DEBOLE | 8,9 | 5,5 |
| -8,00% | 0,06994 $ | 31/40 | +77,50% | +20,00% | 0,09122 $ | 2/31 | +6,45% | +30,43% | DEBOLE | 8,9 | 5,5 |
| -10,00% | 0,06842 $ | 29/40 | +72,50% | +5,00% | 0,07982 $ | 4/29 | +13,79% | +16,67% | DEBOLE | 10,3 | 17,2 |
| -10,00% | 0,06842 $ | 29/40 | +72,50% | +10,00% | 0,08362 $ | 3/29 | +10,34% | +22,22% | DEBOLE | 10,3 | 13,3 |
| -10,00% | 0,06842 $ | 29/40 | +72,50% | +15,00% | 0,08742 $ | 2/29 | +6,90% | +27,78% | DEBOLE | 10,3 | 5,5 |
| -10,00% | 0,06842 $ | 29/40 | +72,50% | +20,00% | 0,09122 $ | 2/29 | +6,90% | +33,33% | DEBOLE | 10,3 | 5,5 |
| -15,00% | 0,06462 $ | 27/40 | +67,50% | +5,00% | 0,07982 $ | 2/27 | +7,41% | +23,53% | DEBOLE | 13,7 | 17,5 |
| -15,00% | 0,06462 $ | 27/40 | +67,50% | +10,00% | 0,08362 $ | 2/27 | +7,41% | +29,41% | DEBOLE | 13,7 | 17,5 |
| -15,00% | 0,06462 $ | 27/40 | +67,50% | +15,00% | 0,08742 $ | 1/27 | +3,70% | +35,29% | DEBOLE | 13,7 | 5,0 |
| -15,00% | 0,06462 $ | 27/40 | +67,50% | +20,00% | 0,09122 $ | 1/27 | +3,70% | +41,18% | DEBOLE | 13,7 | 5,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07982 $ | 24/40 | +60,00% | prezzo iniziale | 0,07602 $ | 18/24 | +75,00% | -4,76% | ALTA | 7,1 | 12,9 |
| +5,00% | 0,07982 $ | 24/40 | +60,00% | -5,00% | 0,07222 $ | 15/24 | +62,50% | -9,52% | MEDIA | 7,1 | 15,8 |
| +5,00% | 0,07982 $ | 24/40 | +60,00% | -8,00% | 0,06994 $ | 12/24 | +50,00% | -12,38% | MEDIA | 7,1 | 15,9 |
| +5,00% | 0,07982 $ | 24/40 | +60,00% | -10,00% | 0,06842 $ | 12/24 | +50,00% | -14,29% | MEDIA | 7,1 | 16,8 |
| +5,00% | 0,07982 $ | 24/40 | +60,00% | -15,00% | 0,06462 $ | 11/24 | +45,83% | -19,05% | BASSA | 7,1 | 17,2 |
| +10,00% | 0,08362 $ | 17/40 | +42,50% | prezzo iniziale | 0,07602 $ | 13/17 | +76,47% | -9,09% | ALTA | 7,9 | 15,5 |
| +10,00% | 0,08362 $ | 17/40 | +42,50% | -5,00% | 0,07222 $ | 11/17 | +64,71% | -13,64% | MEDIA | 7,9 | 17,1 |
| +10,00% | 0,08362 $ | 17/40 | +42,50% | -8,00% | 0,06994 $ | 8/17 | +47,06% | -16,36% | BASSA | 7,9 | 16,5 |
| +10,00% | 0,08362 $ | 17/40 | +42,50% | -10,00% | 0,06842 $ | 8/17 | +47,06% | -18,18% | BASSA | 7,9 | 17,4 |
| +10,00% | 0,08362 $ | 17/40 | +42,50% | -15,00% | 0,06462 $ | 7/17 | +41,18% | -22,73% | BASSA | 7,9 | 17,6 |
| +15,00% | 0,08742 $ | 8/40 | +20,00% | prezzo iniziale | 0,07602 $ | 6/8 | +75,00% | -13,04% | ALTA | 9,1 | 17,3 |
| +15,00% | 0,08742 $ | 8/40 | +20,00% | -5,00% | 0,07222 $ | 4/8 | +50,00% | -17,39% | MEDIA | 9,1 | 16,8 |
| +15,00% | 0,08742 $ | 8/40 | +20,00% | -8,00% | 0,06994 $ | 3/8 | +37,50% | -20,00% | BASSA | 9,1 | 18,0 |
| +15,00% | 0,08742 $ | 8/40 | +20,00% | -10,00% | 0,06842 $ | 3/8 | +37,50% | -21,74% | BASSA | 9,1 | 19,7 |
| +15,00% | 0,08742 $ | 8/40 | +20,00% | -15,00% | 0,06462 $ | 2/8 | +25,00% | -26,09% | DEBOLE | 9,1 | 19,0 |
| +20,00% | 0,09122 $ | 6/40 | +15,00% | prezzo iniziale | 0,07602 $ | 4/6 | +66,67% | -16,67% | ALTA | 10,0 | 15,0 |
| +20,00% | 0,09122 $ | 6/40 | +15,00% | -5,00% | 0,07222 $ | 3/6 | +50,00% | -20,83% | MEDIA | 10,0 | 17,3 |
| +20,00% | 0,09122 $ | 6/40 | +15,00% | -8,00% | 0,06994 $ | 2/6 | +33,33% | -23,33% | DEBOLE | 10,0 | 19,0 |
| +20,00% | 0,09122 $ | 6/40 | +15,00% | -10,00% | 0,06842 $ | 2/6 | +33,33% | -25,00% | DEBOLE | 10,0 | 21,5 |
| +20,00% | 0,09122 $ | 6/40 | +15,00% | -15,00% | 0,06462 $ | 1/6 | +16,67% | -29,17% | DEBOLE | 10,0 | 22,0 |

---
