# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-16 12:01:33 CEST**  
UTC: **2026-07-16 10:01:33 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 60.825 $ | 70.429 $ | +41,94% | +15,79% | rimbalzo debole | 70.429 $ | 60.825 $ | +22,73% | -13,64% | spike storicamente più resistente |
| SOL | 72,15 $ | 83,54 $ | +16,13% | +15,79% | rimbalzo poco frequente | 83,54 $ | 72,15 $ | +29,41% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06939 $ | 0,08034 $ | +21,62% | +15,79% | rimbalzo poco frequente | 0,08034 $ | 0,06939 $ | +42,86% | -13,64% | scarico possibile |

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
| -5,00% | 60.825 $ | 31/40 | +77,50% | +5,00% | 67.227 $ | 15/31 | +48,39% | +10,53% | BASSA | 8,3 | 21,7 |
| -5,00% | 60.825 $ | 31/40 | +77,50% | +10,00% | 70.429 $ | 13/31 | +41,94% | +15,79% | BASSA | 8,3 | 25,2 |
| -5,00% | 60.825 $ | 31/40 | +77,50% | +15,00% | 73.630 $ | 7/31 | +22,58% | +21,05% | DEBOLE | 8,3 | 24,1 |
| -5,00% | 60.825 $ | 31/40 | +77,50% | +20,00% | 76.831 $ | 5/31 | +16,13% | +26,32% | DEBOLE | 8,3 | 25,4 |
| -8,00% | 58.904 $ | 24/40 | +60,00% | +5,00% | 67.227 $ | 9/24 | +37,50% | +14,13% | BASSA | 10,0 | 23,0 |
| -8,00% | 58.904 $ | 24/40 | +60,00% | +10,00% | 70.429 $ | 7/24 | +29,17% | +19,57% | DEBOLE | 10,0 | 25,0 |
| -8,00% | 58.904 $ | 24/40 | +60,00% | +15,00% | 73.630 $ | 3/24 | +12,50% | +25,00% | DEBOLE | 10,0 | 22,0 |
| -8,00% | 58.904 $ | 24/40 | +60,00% | +20,00% | 76.831 $ | 2/24 | +8,33% | +30,43% | DEBOLE | 10,0 | 21,0 |
| -10,00% | 57.624 $ | 18/40 | +45,00% | +5,00% | 67.227 $ | 5/18 | +27,78% | +16,67% | DEBOLE | 10,6 | 25,6 |
| -10,00% | 57.624 $ | 18/40 | +45,00% | +10,00% | 70.429 $ | 3/18 | +16,67% | +22,22% | DEBOLE | 10,6 | 28,0 |
| -10,00% | 57.624 $ | 18/40 | +45,00% | +15,00% | 73.630 $ | 1/18 | +5,56% | +27,78% | DEBOLE | 10,6 | 26,0 |
| -10,00% | 57.624 $ | 18/40 | +45,00% | +20,00% | 76.831 $ | 1/18 | +5,56% | +33,33% | DEBOLE | 10,6 | 26,0 |
| -15,00% | 54.422 $ | 12/40 | +30,00% | +5,00% | 67.227 $ | 1/12 | +8,33% | +23,53% | DEBOLE | 14,6 | 30,0 |
| -15,00% | 54.422 $ | 12/40 | +30,00% | +10,00% | 70.429 $ | 0/12 | 0,00% | +29,41% | DEBOLE | 14,6 | n/d |
| -15,00% | 54.422 $ | 12/40 | +30,00% | +15,00% | 73.630 $ | 0/12 | 0,00% | +35,29% | DEBOLE | 14,6 | n/d |
| -15,00% | 54.422 $ | 12/40 | +30,00% | +20,00% | 76.831 $ | 0/12 | 0,00% | +41,18% | DEBOLE | 14,6 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 67.227 $ | 29/40 | +72,50% | prezzo iniziale | 64.026 $ | 16/29 | +55,17% | -4,76% | MEDIA | 10,7 | 13,3 |
| +5,00% | 67.227 $ | 29/40 | +72,50% | -5,00% | 60.825 $ | 11/29 | +37,93% | -9,52% | BASSA | 10,7 | 13,6 |
| +5,00% | 67.227 $ | 29/40 | +72,50% | -8,00% | 58.904 $ | 7/29 | +24,14% | -12,38% | DEBOLE | 10,7 | 13,3 |
| +5,00% | 67.227 $ | 29/40 | +72,50% | -10,00% | 57.624 $ | 4/29 | +13,79% | -14,29% | DEBOLE | 10,7 | 13,8 |
| +5,00% | 67.227 $ | 29/40 | +72,50% | -15,00% | 54.422 $ | 2/29 | +6,90% | -19,05% | DEBOLE | 10,7 | 21,0 |
| +10,00% | 70.429 $ | 22/40 | +55,00% | prezzo iniziale | 64.026 $ | 6/22 | +27,27% | -9,09% | DEBOLE | 16,8 | 12,0 |
| +10,00% | 70.429 $ | 22/40 | +55,00% | -5,00% | 60.825 $ | 5/22 | +22,73% | -13,64% | DEBOLE | 16,8 | 12,2 |
| +10,00% | 70.429 $ | 22/40 | +55,00% | -8,00% | 58.904 $ | 3/22 | +13,64% | -16,36% | DEBOLE | 16,8 | 13,3 |
| +10,00% | 70.429 $ | 22/40 | +55,00% | -10,00% | 57.624 $ | 2/22 | +9,09% | -18,18% | DEBOLE | 16,8 | 14,0 |
| +10,00% | 70.429 $ | 22/40 | +55,00% | -15,00% | 54.422 $ | 1/22 | +4,55% | -22,73% | DEBOLE | 16,8 | 12,0 |
| +15,00% | 73.630 $ | 13/40 | +32,50% | prezzo iniziale | 64.026 $ | 1/13 | +7,69% | -13,04% | DEBOLE | 17,7 | 20,0 |
| +15,00% | 73.630 $ | 13/40 | +32,50% | -5,00% | 60.825 $ | 0/13 | 0,00% | -17,39% | DEBOLE | 17,7 | n/d |
| +15,00% | 73.630 $ | 13/40 | +32,50% | -8,00% | 58.904 $ | 0/13 | 0,00% | -20,00% | DEBOLE | 17,7 | n/d |
| +15,00% | 73.630 $ | 13/40 | +32,50% | -10,00% | 57.624 $ | 0/13 | 0,00% | -21,74% | DEBOLE | 17,7 | n/d |
| +15,00% | 73.630 $ | 13/40 | +32,50% | -15,00% | 54.422 $ | 0/13 | 0,00% | -26,09% | DEBOLE | 17,7 | n/d |
| +20,00% | 76.831 $ | 10/40 | +25,00% | prezzo iniziale | 64.026 $ | 0/10 | 0,00% | -16,67% | DEBOLE | 19,6 | n/d |
| +20,00% | 76.831 $ | 10/40 | +25,00% | -5,00% | 60.825 $ | 0/10 | 0,00% | -20,83% | DEBOLE | 19,6 | n/d |
| +20,00% | 76.831 $ | 10/40 | +25,00% | -8,00% | 58.904 $ | 0/10 | 0,00% | -23,33% | DEBOLE | 19,6 | n/d |
| +20,00% | 76.831 $ | 10/40 | +25,00% | -10,00% | 57.624 $ | 0/10 | 0,00% | -25,00% | DEBOLE | 19,6 | n/d |
| +20,00% | 76.831 $ | 10/40 | +25,00% | -15,00% | 54.422 $ | 0/10 | 0,00% | -29,17% | DEBOLE | 19,6 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 31 prima sono scesi a -5,00%. Tra quei 31, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +16,13% (5/31). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 17 prima sono saliti a +10,00%. Tra quei 17, 5 poi sono scaricati a -5,00%. Percentuale: +29,41% (5/17). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 72,15 $ | 31/40 | +77,50% | +5,00% | 79,75 $ | 11/31 | +35,48% | +10,53% | BASSA | 7,0 | 22,2 |
| -5,00% | 72,15 $ | 31/40 | +77,50% | +10,00% | 83,54 $ | 5/31 | +16,13% | +15,79% | DEBOLE | 7,0 | 20,4 |
| -5,00% | 72,15 $ | 31/40 | +77,50% | +15,00% | 87,34 $ | 3/31 | +9,68% | +21,05% | DEBOLE | 7,0 | 17,7 |
| -5,00% | 72,15 $ | 31/40 | +77,50% | +20,00% | 91,14 $ | 2/31 | +6,45% | +26,32% | DEBOLE | 7,0 | 21,5 |
| -8,00% | 69,87 $ | 27/40 | +67,50% | +5,00% | 79,75 $ | 6/27 | +22,22% | +14,13% | DEBOLE | 8,9 | 20,5 |
| -8,00% | 69,87 $ | 27/40 | +67,50% | +10,00% | 83,54 $ | 3/27 | +11,11% | +19,57% | DEBOLE | 8,9 | 20,0 |
| -8,00% | 69,87 $ | 27/40 | +67,50% | +15,00% | 87,34 $ | 2/27 | +7,41% | +25,00% | DEBOLE | 8,9 | 20,0 |
| -8,00% | 69,87 $ | 27/40 | +67,50% | +20,00% | 91,14 $ | 2/27 | +7,41% | +30,43% | DEBOLE | 8,9 | 21,5 |
| -10,00% | 68,35 $ | 21/40 | +52,50% | +5,00% | 79,75 $ | 3/21 | +14,29% | +16,67% | DEBOLE | 9,1 | 21,0 |
| -10,00% | 68,35 $ | 21/40 | +52,50% | +10,00% | 83,54 $ | 0/21 | 0,00% | +22,22% | DEBOLE | 9,1 | n/d |
| -10,00% | 68,35 $ | 21/40 | +52,50% | +15,00% | 87,34 $ | 0/21 | 0,00% | +27,78% | DEBOLE | 9,1 | n/d |
| -10,00% | 68,35 $ | 21/40 | +52,50% | +20,00% | 91,14 $ | 0/21 | 0,00% | +33,33% | DEBOLE | 9,1 | n/d |
| -15,00% | 64,56 $ | 16/40 | +40,00% | +5,00% | 79,75 $ | 2/16 | +12,50% | +23,53% | DEBOLE | 11,6 | 17,0 |
| -15,00% | 64,56 $ | 16/40 | +40,00% | +10,00% | 83,54 $ | 0/16 | 0,00% | +29,41% | DEBOLE | 11,6 | n/d |
| -15,00% | 64,56 $ | 16/40 | +40,00% | +15,00% | 87,34 $ | 0/16 | 0,00% | +35,29% | DEBOLE | 11,6 | n/d |
| -15,00% | 64,56 $ | 16/40 | +40,00% | +20,00% | 91,14 $ | 0/16 | 0,00% | +41,18% | DEBOLE | 11,6 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 79,75 $ | 24/40 | +60,00% | prezzo iniziale | 75,95 $ | 11/24 | +45,83% | -4,76% | BASSA | 10,9 | 11,0 |
| +5,00% | 79,75 $ | 24/40 | +60,00% | -5,00% | 72,15 $ | 9/24 | +37,50% | -9,52% | BASSA | 10,9 | 12,6 |
| +5,00% | 79,75 $ | 24/40 | +60,00% | -8,00% | 69,87 $ | 9/24 | +37,50% | -12,38% | BASSA | 10,9 | 16,7 |
| +5,00% | 79,75 $ | 24/40 | +60,00% | -10,00% | 68,35 $ | 5/24 | +20,83% | -14,29% | DEBOLE | 10,9 | 15,8 |
| +5,00% | 79,75 $ | 24/40 | +60,00% | -15,00% | 64,56 $ | 4/24 | +16,67% | -19,05% | DEBOLE | 10,9 | 21,2 |
| +10,00% | 83,54 $ | 17/40 | +42,50% | prezzo iniziale | 75,95 $ | 5/17 | +29,41% | -9,09% | DEBOLE | 10,9 | 7,0 |
| +10,00% | 83,54 $ | 17/40 | +42,50% | -5,00% | 72,15 $ | 5/17 | +29,41% | -13,64% | DEBOLE | 10,9 | 8,2 |
| +10,00% | 83,54 $ | 17/40 | +42,50% | -8,00% | 69,87 $ | 5/17 | +29,41% | -16,36% | DEBOLE | 10,9 | 14,2 |
| +10,00% | 83,54 $ | 17/40 | +42,50% | -10,00% | 68,35 $ | 3/17 | +17,65% | -18,18% | DEBOLE | 10,9 | 10,3 |
| +10,00% | 83,54 $ | 17/40 | +42,50% | -15,00% | 64,56 $ | 2/17 | +11,76% | -22,73% | DEBOLE | 10,9 | 18,0 |
| +15,00% | 87,34 $ | 11/40 | +27,50% | prezzo iniziale | 75,95 $ | 2/11 | +18,18% | -13,04% | DEBOLE | 9,1 | 7,5 |
| +15,00% | 87,34 $ | 11/40 | +27,50% | -5,00% | 72,15 $ | 2/11 | +18,18% | -17,39% | DEBOLE | 9,1 | 8,0 |
| +15,00% | 87,34 $ | 11/40 | +27,50% | -8,00% | 69,87 $ | 2/11 | +18,18% | -20,00% | DEBOLE | 9,1 | 18,5 |
| +15,00% | 87,34 $ | 11/40 | +27,50% | -10,00% | 68,35 $ | 1/11 | +9,09% | -21,74% | DEBOLE | 9,1 | 7,0 |
| +15,00% | 87,34 $ | 11/40 | +27,50% | -15,00% | 64,56 $ | 1/11 | +9,09% | -26,09% | DEBOLE | 9,1 | 8,0 |
| +20,00% | 91,14 $ | 10/40 | +25,00% | prezzo iniziale | 75,95 $ | 1/10 | +10,00% | -16,67% | DEBOLE | 11,2 | 10,0 |
| +20,00% | 91,14 $ | 10/40 | +25,00% | -5,00% | 72,15 $ | 1/10 | +10,00% | -20,83% | DEBOLE | 11,2 | 10,0 |
| +20,00% | 91,14 $ | 10/40 | +25,00% | -8,00% | 69,87 $ | 1/10 | +10,00% | -23,33% | DEBOLE | 11,2 | 30,0 |
| +20,00% | 91,14 $ | 10/40 | +25,00% | -10,00% | 68,35 $ | 0/10 | 0,00% | -25,00% | DEBOLE | 11,2 | n/d |
| +20,00% | 91,14 $ | 10/40 | +25,00% | -15,00% | 64,56 $ | 0/10 | 0,00% | -29,17% | DEBOLE | 11,2 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 37 prima sono scesi a -5,00%. Tra quei 37, 8 poi sono rimbalzati fino a +10,00%. Percentuale: +21,62% (8/37). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 14 prima sono saliti a +10,00%. Tra quei 14, 6 poi sono scaricati a -5,00%. Percentuale: +42,86% (6/14). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06939 $ | 37/40 | +92,50% | +5,00% | 0,07669 $ | 9/37 | +24,32% | +10,53% | DEBOLE | 3,8 | 14,2 |
| -5,00% | 0,06939 $ | 37/40 | +92,50% | +10,00% | 0,08034 $ | 8/37 | +21,62% | +15,79% | DEBOLE | 3,8 | 15,5 |
| -5,00% | 0,06939 $ | 37/40 | +92,50% | +15,00% | 0,08400 $ | 4/37 | +10,81% | +21,05% | DEBOLE | 3,8 | 15,2 |
| -5,00% | 0,06939 $ | 37/40 | +92,50% | +20,00% | 0,08765 $ | 4/37 | +10,81% | +26,32% | DEBOLE | 3,8 | 16,8 |
| -8,00% | 0,06720 $ | 35/40 | +87,50% | +5,00% | 0,07669 $ | 6/35 | +17,14% | +14,13% | DEBOLE | 5,3 | 16,7 |
| -8,00% | 0,06720 $ | 35/40 | +87,50% | +10,00% | 0,08034 $ | 5/35 | +14,29% | +19,57% | DEBOLE | 5,3 | 15,2 |
| -8,00% | 0,06720 $ | 35/40 | +87,50% | +15,00% | 0,08400 $ | 2/35 | +5,71% | +25,00% | DEBOLE | 5,3 | 9,0 |
| -8,00% | 0,06720 $ | 35/40 | +87,50% | +20,00% | 0,08765 $ | 2/35 | +5,71% | +30,43% | DEBOLE | 5,3 | 11,0 |
| -10,00% | 0,06574 $ | 32/40 | +80,00% | +5,00% | 0,07669 $ | 3/32 | +9,38% | +16,67% | DEBOLE | 5,4 | 20,7 |
| -10,00% | 0,06574 $ | 32/40 | +80,00% | +10,00% | 0,08034 $ | 3/32 | +9,38% | +22,22% | DEBOLE | 5,4 | 21,0 |
| -10,00% | 0,06574 $ | 32/40 | +80,00% | +15,00% | 0,08400 $ | 0/32 | 0,00% | +27,78% | DEBOLE | 5,4 | n/d |
| -10,00% | 0,06574 $ | 32/40 | +80,00% | +20,00% | 0,08765 $ | 0/32 | 0,00% | +33,33% | DEBOLE | 5,4 | n/d |
| -15,00% | 0,06208 $ | 31/40 | +77,50% | +5,00% | 0,07669 $ | 2/31 | +6,45% | +23,53% | DEBOLE | 7,3 | 18,0 |
| -15,00% | 0,06208 $ | 31/40 | +77,50% | +10,00% | 0,08034 $ | 2/31 | +6,45% | +29,41% | DEBOLE | 7,3 | 18,5 |
| -15,00% | 0,06208 $ | 31/40 | +77,50% | +15,00% | 0,08400 $ | 0/31 | 0,00% | +35,29% | DEBOLE | 7,3 | n/d |
| -15,00% | 0,06208 $ | 31/40 | +77,50% | +20,00% | 0,08765 $ | 0/31 | 0,00% | +41,18% | DEBOLE | 7,3 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07669 $ | 16/40 | +40,00% | prezzo iniziale | 0,07304 $ | 12/16 | +75,00% | -4,76% | ALTA | 5,2 | 8,8 |
| +5,00% | 0,07669 $ | 16/40 | +40,00% | -5,00% | 0,06939 $ | 9/16 | +56,25% | -9,52% | MEDIA | 5,2 | 10,2 |
| +5,00% | 0,07669 $ | 16/40 | +40,00% | -8,00% | 0,06720 $ | 9/16 | +56,25% | -12,38% | MEDIA | 5,2 | 11,7 |
| +5,00% | 0,07669 $ | 16/40 | +40,00% | -10,00% | 0,06574 $ | 7/16 | +43,75% | -14,29% | BASSA | 5,2 | 12,0 |
| +5,00% | 0,07669 $ | 16/40 | +40,00% | -15,00% | 0,06208 $ | 7/16 | +43,75% | -19,05% | BASSA | 5,2 | 12,9 |
| +10,00% | 0,08034 $ | 14/40 | +35,00% | prezzo iniziale | 0,07304 $ | 9/14 | +64,29% | -9,09% | MEDIA | 10,6 | 13,0 |
| +10,00% | 0,08034 $ | 14/40 | +35,00% | -5,00% | 0,06939 $ | 6/14 | +42,86% | -13,64% | BASSA | 10,6 | 13,3 |
| +10,00% | 0,08034 $ | 14/40 | +35,00% | -8,00% | 0,06720 $ | 6/14 | +42,86% | -16,36% | BASSA | 10,6 | 14,5 |
| +10,00% | 0,08034 $ | 14/40 | +35,00% | -10,00% | 0,06574 $ | 5/14 | +35,71% | -18,18% | BASSA | 10,6 | 17,2 |
| +10,00% | 0,08034 $ | 14/40 | +35,00% | -15,00% | 0,06208 $ | 4/14 | +28,57% | -22,73% | DEBOLE | 10,6 | 16,5 |
| +15,00% | 0,08400 $ | 9/40 | +22,50% | prezzo iniziale | 0,07304 $ | 4/9 | +44,44% | -13,04% | BASSA | 12,9 | 14,2 |
| +15,00% | 0,08400 $ | 9/40 | +22,50% | -5,00% | 0,06939 $ | 3/9 | +33,33% | -17,39% | DEBOLE | 12,9 | 18,7 |
| +15,00% | 0,08400 $ | 9/40 | +22,50% | -8,00% | 0,06720 $ | 2/9 | +22,22% | -20,00% | DEBOLE | 12,9 | 14,5 |
| +15,00% | 0,08400 $ | 9/40 | +22,50% | -10,00% | 0,06574 $ | 2/9 | +22,22% | -21,74% | DEBOLE | 12,9 | 14,5 |
| +15,00% | 0,08400 $ | 9/40 | +22,50% | -15,00% | 0,06208 $ | 2/9 | +22,22% | -26,09% | DEBOLE | 12,9 | 15,0 |
| +20,00% | 0,08765 $ | 7/40 | +17,50% | prezzo iniziale | 0,07304 $ | 2/7 | +28,57% | -16,67% | DEBOLE | 14,7 | 11,5 |
| +20,00% | 0,08765 $ | 7/40 | +17,50% | -5,00% | 0,06939 $ | 2/7 | +28,57% | -20,83% | DEBOLE | 14,7 | 17,5 |
| +20,00% | 0,08765 $ | 7/40 | +17,50% | -8,00% | 0,06720 $ | 1/7 | +14,29% | -23,33% | DEBOLE | 14,7 | 8,0 |
| +20,00% | 0,08765 $ | 7/40 | +17,50% | -10,00% | 0,06574 $ | 1/7 | +14,29% | -25,00% | DEBOLE | 14,7 | 8,0 |
| +20,00% | 0,08765 $ | 7/40 | +17,50% | -15,00% | 0,06208 $ | 1/7 | +14,29% | -29,17% | DEBOLE | 14,7 | 9,0 |

---
