# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-21 07:13:50 CEST**  
UTC: **2026-07-21 05:13:50 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.198 $ | 72.019 $ | +44,12% | +15,79% | rimbalzo debole | 72.019 $ | 62.198 $ | +20,00% | -13,64% | spike storicamente più resistente |
| SOL | 74,27 $ | 86,00 $ | +31,03% | +15,79% | rimbalzo poco frequente | 86,00 $ | 74,27 $ | +15,79% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06913 $ | 0,08005 $ | +25,71% | +15,79% | rimbalzo poco frequente | 0,08005 $ | 0,06913 $ | +50,00% | -13,64% | attenzione a prendere profitto |

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

- BTC: su 40 casi simili, 34 prima sono scesi a -5,00%. Tra quei 34, 15 poi sono rimbalzati fino a +10,00%. Percentuale: +44,12% (15/34). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 5 poi sono scaricati a -5,00%. Percentuale: +20,00% (5/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 62.198 $ | 34/40 | +85,00% | +5,00% | 68.745 $ | 19/34 | +55,88% | +10,53% | MEDIA | 7,4 | 22,4 |
| -5,00% | 62.198 $ | 34/40 | +85,00% | +10,00% | 72.019 $ | 15/34 | +44,12% | +15,79% | BASSA | 7,4 | 24,1 |
| -5,00% | 62.198 $ | 34/40 | +85,00% | +15,00% | 75.292 $ | 10/34 | +29,41% | +21,05% | DEBOLE | 7,4 | 25,4 |
| -5,00% | 62.198 $ | 34/40 | +85,00% | +20,00% | 78.566 $ | 10/34 | +29,41% | +26,32% | DEBOLE | 7,4 | 27,0 |
| -8,00% | 60.234 $ | 29/40 | +72,50% | +5,00% | 68.745 $ | 15/29 | +51,72% | +14,13% | MEDIA | 10,2 | 22,9 |
| -8,00% | 60.234 $ | 29/40 | +72,50% | +10,00% | 72.019 $ | 11/29 | +37,93% | +19,57% | BASSA | 10,2 | 23,6 |
| -8,00% | 60.234 $ | 29/40 | +72,50% | +15,00% | 75.292 $ | 8/29 | +27,59% | +25,00% | DEBOLE | 10,2 | 24,9 |
| -8,00% | 60.234 $ | 29/40 | +72,50% | +20,00% | 78.566 $ | 8/29 | +27,59% | +30,43% | DEBOLE | 10,2 | 26,2 |
| -10,00% | 58.924 $ | 24/40 | +60,00% | +5,00% | 68.745 $ | 11/24 | +45,83% | +16,67% | BASSA | 12,4 | 23,3 |
| -10,00% | 58.924 $ | 24/40 | +60,00% | +10,00% | 72.019 $ | 8/24 | +33,33% | +22,22% | DEBOLE | 12,4 | 23,8 |
| -10,00% | 58.924 $ | 24/40 | +60,00% | +15,00% | 75.292 $ | 6/24 | +25,00% | +27,78% | DEBOLE | 12,4 | 25,2 |
| -10,00% | 58.924 $ | 24/40 | +60,00% | +20,00% | 78.566 $ | 6/24 | +25,00% | +33,33% | DEBOLE | 12,4 | 26,0 |
| -15,00% | 55.651 $ | 11/40 | +27,50% | +5,00% | 68.745 $ | 0/11 | 0,00% | +23,53% | DEBOLE | 13,6 | n/d |
| -15,00% | 55.651 $ | 11/40 | +27,50% | +10,00% | 72.019 $ | 0/11 | 0,00% | +29,41% | DEBOLE | 13,6 | n/d |
| -15,00% | 55.651 $ | 11/40 | +27,50% | +15,00% | 75.292 $ | 0/11 | 0,00% | +35,29% | DEBOLE | 13,6 | n/d |
| -15,00% | 55.651 $ | 11/40 | +27,50% | +20,00% | 78.566 $ | 0/11 | 0,00% | +41,18% | DEBOLE | 13,6 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 68.745 $ | 31/40 | +77,50% | prezzo iniziale | 65.472 $ | 10/31 | +32,26% | -4,76% | DEBOLE | 15,7 | 14,8 |
| +5,00% | 68.745 $ | 31/40 | +77,50% | -5,00% | 62.198 $ | 7/31 | +22,58% | -9,52% | DEBOLE | 15,7 | 16,7 |
| +5,00% | 68.745 $ | 31/40 | +77,50% | -8,00% | 60.234 $ | 6/31 | +19,35% | -12,38% | DEBOLE | 15,7 | 19,3 |
| +5,00% | 68.745 $ | 31/40 | +77,50% | -10,00% | 58.924 $ | 6/31 | +19,35% | -14,29% | DEBOLE | 15,7 | 19,7 |
| +5,00% | 68.745 $ | 31/40 | +77,50% | -15,00% | 55.651 $ | 3/31 | +9,68% | -19,05% | DEBOLE | 15,7 | 25,0 |
| +10,00% | 72.019 $ | 25/40 | +62,50% | prezzo iniziale | 65.472 $ | 6/25 | +24,00% | -9,09% | DEBOLE | 18,3 | 20,3 |
| +10,00% | 72.019 $ | 25/40 | +62,50% | -5,00% | 62.198 $ | 5/25 | +20,00% | -13,64% | DEBOLE | 18,3 | 21,0 |
| +10,00% | 72.019 $ | 25/40 | +62,50% | -8,00% | 60.234 $ | 4/25 | +16,00% | -16,36% | DEBOLE | 18,3 | 22,2 |
| +10,00% | 72.019 $ | 25/40 | +62,50% | -10,00% | 58.924 $ | 4/25 | +16,00% | -18,18% | DEBOLE | 18,3 | 22,5 |
| +10,00% | 72.019 $ | 25/40 | +62,50% | -15,00% | 55.651 $ | 3/25 | +12,00% | -22,73% | DEBOLE | 18,3 | 25,0 |
| +15,00% | 75.292 $ | 17/40 | +42,50% | prezzo iniziale | 65.472 $ | 3/17 | +17,65% | -13,04% | DEBOLE | 20,0 | 24,3 |
| +15,00% | 75.292 $ | 17/40 | +42,50% | -5,00% | 62.198 $ | 3/17 | +17,65% | -17,39% | DEBOLE | 20,0 | 24,7 |
| +15,00% | 75.292 $ | 17/40 | +42,50% | -8,00% | 60.234 $ | 3/17 | +17,65% | -20,00% | DEBOLE | 20,0 | 24,7 |
| +15,00% | 75.292 $ | 17/40 | +42,50% | -10,00% | 58.924 $ | 3/17 | +17,65% | -21,74% | DEBOLE | 20,0 | 24,7 |
| +15,00% | 75.292 $ | 17/40 | +42,50% | -15,00% | 55.651 $ | 3/17 | +17,65% | -26,09% | DEBOLE | 20,0 | 25,0 |
| +20,00% | 78.566 $ | 14/40 | +35,00% | prezzo iniziale | 65.472 $ | 1/14 | +7,14% | -16,67% | DEBOLE | 24,4 | 22,0 |
| +20,00% | 78.566 $ | 14/40 | +35,00% | -5,00% | 62.198 $ | 1/14 | +7,14% | -20,83% | DEBOLE | 24,4 | 22,0 |
| +20,00% | 78.566 $ | 14/40 | +35,00% | -8,00% | 60.234 $ | 1/14 | +7,14% | -23,33% | DEBOLE | 24,4 | 22,0 |
| +20,00% | 78.566 $ | 14/40 | +35,00% | -10,00% | 58.924 $ | 1/14 | +7,14% | -25,00% | DEBOLE | 24,4 | 22,0 |
| +20,00% | 78.566 $ | 14/40 | +35,00% | -15,00% | 55.651 $ | 1/14 | +7,14% | -29,17% | DEBOLE | 24,4 | 23,0 |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 29 prima sono scesi a -5,00%. Tra quei 29, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +31,03% (9/29). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 19 prima sono saliti a +10,00%. Tra quei 19, 3 poi sono scaricati a -5,00%. Percentuale: +15,79% (3/19). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 74,27 $ | 29/40 | +72,50% | +5,00% | 82,09 $ | 17/29 | +58,62% | +10,53% | MEDIA | 5,2 | 20,0 |
| -5,00% | 74,27 $ | 29/40 | +72,50% | +10,00% | 86,00 $ | 9/29 | +31,03% | +15,79% | DEBOLE | 5,2 | 20,9 |
| -5,00% | 74,27 $ | 29/40 | +72,50% | +15,00% | 89,91 $ | 6/29 | +20,69% | +21,05% | DEBOLE | 5,2 | 20,8 |
| -5,00% | 74,27 $ | 29/40 | +72,50% | +20,00% | 93,82 $ | 5/29 | +17,24% | +26,32% | DEBOLE | 5,2 | 22,0 |
| -8,00% | 71,93 $ | 22/40 | +55,00% | +5,00% | 82,09 $ | 10/22 | +45,45% | +14,13% | BASSA | 6,0 | 19,3 |
| -8,00% | 71,93 $ | 22/40 | +55,00% | +10,00% | 86,00 $ | 5/22 | +22,73% | +19,57% | DEBOLE | 6,0 | 19,4 |
| -8,00% | 71,93 $ | 22/40 | +55,00% | +15,00% | 89,91 $ | 4/22 | +18,18% | +25,00% | DEBOLE | 6,0 | 20,2 |
| -8,00% | 71,93 $ | 22/40 | +55,00% | +20,00% | 93,82 $ | 3/22 | +13,64% | +30,43% | DEBOLE | 6,0 | 21,0 |
| -10,00% | 70,36 $ | 19/40 | +47,50% | +5,00% | 82,09 $ | 8/19 | +42,11% | +16,67% | BASSA | 6,8 | 19,8 |
| -10,00% | 70,36 $ | 19/40 | +47,50% | +10,00% | 86,00 $ | 3/19 | +15,79% | +22,22% | DEBOLE | 6,8 | 17,7 |
| -10,00% | 70,36 $ | 19/40 | +47,50% | +15,00% | 89,91 $ | 3/19 | +15,79% | +27,78% | DEBOLE | 6,8 | 18,7 |
| -10,00% | 70,36 $ | 19/40 | +47,50% | +20,00% | 93,82 $ | 2/19 | +10,53% | +33,33% | DEBOLE | 6,8 | 18,0 |
| -15,00% | 66,45 $ | 12/40 | +30,00% | +5,00% | 82,09 $ | 2/12 | +16,67% | +23,53% | DEBOLE | 12,9 | 21,5 |
| -15,00% | 66,45 $ | 12/40 | +30,00% | +10,00% | 86,00 $ | 0/12 | 0,00% | +29,41% | DEBOLE | 12,9 | n/d |
| -15,00% | 66,45 $ | 12/40 | +30,00% | +15,00% | 89,91 $ | 0/12 | 0,00% | +35,29% | DEBOLE | 12,9 | n/d |
| -15,00% | 66,45 $ | 12/40 | +30,00% | +20,00% | 93,82 $ | 0/12 | 0,00% | +41,18% | DEBOLE | 12,9 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 82,09 $ | 28/40 | +70,00% | prezzo iniziale | 78,18 $ | 15/28 | +53,57% | -4,76% | MEDIA | 13,3 | 17,1 |
| +5,00% | 82,09 $ | 28/40 | +70,00% | -5,00% | 74,27 $ | 10/28 | +35,71% | -9,52% | BASSA | 13,3 | 20,0 |
| +5,00% | 82,09 $ | 28/40 | +70,00% | -8,00% | 71,93 $ | 5/28 | +17,86% | -12,38% | DEBOLE | 13,3 | 24,2 |
| +5,00% | 82,09 $ | 28/40 | +70,00% | -10,00% | 70,36 $ | 3/28 | +10,71% | -14,29% | DEBOLE | 13,3 | 20,7 |
| +5,00% | 82,09 $ | 28/40 | +70,00% | -15,00% | 66,45 $ | 1/28 | +3,57% | -19,05% | DEBOLE | 13,3 | 30,0 |
| +10,00% | 86,00 $ | 19/40 | +47,50% | prezzo iniziale | 78,18 $ | 5/19 | +26,32% | -9,09% | DEBOLE | 15,3 | 18,0 |
| +10,00% | 86,00 $ | 19/40 | +47,50% | -5,00% | 74,27 $ | 3/19 | +15,79% | -13,64% | DEBOLE | 15,3 | 22,0 |
| +10,00% | 86,00 $ | 19/40 | +47,50% | -8,00% | 71,93 $ | 0/19 | 0,00% | -16,36% | DEBOLE | 15,3 | n/d |
| +10,00% | 86,00 $ | 19/40 | +47,50% | -10,00% | 70,36 $ | 0/19 | 0,00% | -18,18% | DEBOLE | 15,3 | n/d |
| +10,00% | 86,00 $ | 19/40 | +47,50% | -15,00% | 66,45 $ | 0/19 | 0,00% | -22,73% | DEBOLE | 15,3 | n/d |
| +15,00% | 89,91 $ | 15/40 | +37,50% | prezzo iniziale | 78,18 $ | 3/15 | +20,00% | -13,04% | DEBOLE | 15,1 | 17,3 |
| +15,00% | 89,91 $ | 15/40 | +37,50% | -5,00% | 74,27 $ | 2/15 | +13,33% | -17,39% | DEBOLE | 15,1 | 18,0 |
| +15,00% | 89,91 $ | 15/40 | +37,50% | -8,00% | 71,93 $ | 0/15 | 0,00% | -20,00% | DEBOLE | 15,1 | n/d |
| +15,00% | 89,91 $ | 15/40 | +37,50% | -10,00% | 70,36 $ | 0/15 | 0,00% | -21,74% | DEBOLE | 15,1 | n/d |
| +15,00% | 89,91 $ | 15/40 | +37,50% | -15,00% | 66,45 $ | 0/15 | 0,00% | -26,09% | DEBOLE | 15,1 | n/d |
| +20,00% | 93,82 $ | 10/40 | +25,00% | prezzo iniziale | 78,18 $ | 1/10 | +10,00% | -16,67% | DEBOLE | 16,5 | 7,0 |
| +20,00% | 93,82 $ | 10/40 | +25,00% | -5,00% | 74,27 $ | 1/10 | +10,00% | -20,83% | DEBOLE | 16,5 | 7,0 |
| +20,00% | 93,82 $ | 10/40 | +25,00% | -8,00% | 71,93 $ | 0/10 | 0,00% | -23,33% | DEBOLE | 16,5 | n/d |
| +20,00% | 93,82 $ | 10/40 | +25,00% | -10,00% | 70,36 $ | 0/10 | 0,00% | -25,00% | DEBOLE | 16,5 | n/d |
| +20,00% | 93,82 $ | 10/40 | +25,00% | -15,00% | 66,45 $ | 0/10 | 0,00% | -29,17% | DEBOLE | 16,5 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 35 prima sono scesi a -5,00%. Tra quei 35, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +25,71% (9/35). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 20 prima sono saliti a +10,00%. Tra quei 20, 10 poi sono scaricati a -5,00%. Percentuale: +50,00% (10/20). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06913 $ | 35/40 | +87,50% | +5,00% | 0,07641 $ | 10/35 | +28,57% | +10,53% | DEBOLE | 6,9 | 13,0 |
| -5,00% | 0,06913 $ | 35/40 | +87,50% | +10,00% | 0,08005 $ | 9/35 | +25,71% | +15,79% | DEBOLE | 6,9 | 16,8 |
| -5,00% | 0,06913 $ | 35/40 | +87,50% | +15,00% | 0,08369 $ | 8/35 | +22,86% | +21,05% | DEBOLE | 6,9 | 20,2 |
| -5,00% | 0,06913 $ | 35/40 | +87,50% | +20,00% | 0,08732 $ | 6/35 | +17,14% | +26,32% | DEBOLE | 6,9 | 23,7 |
| -8,00% | 0,06695 $ | 28/40 | +70,00% | +5,00% | 0,07641 $ | 5/28 | +17,86% | +14,13% | DEBOLE | 6,4 | 11,6 |
| -8,00% | 0,06695 $ | 28/40 | +70,00% | +10,00% | 0,08005 $ | 4/28 | +14,29% | +19,57% | DEBOLE | 6,4 | 11,5 |
| -8,00% | 0,06695 $ | 28/40 | +70,00% | +15,00% | 0,08369 $ | 3/28 | +10,71% | +25,00% | DEBOLE | 6,4 | 15,0 |
| -8,00% | 0,06695 $ | 28/40 | +70,00% | +20,00% | 0,08732 $ | 2/28 | +7,14% | +30,43% | DEBOLE | 6,4 | 18,0 |
| -10,00% | 0,06549 $ | 26/40 | +65,00% | +5,00% | 0,07641 $ | 3/26 | +11,54% | +16,67% | DEBOLE | 6,8 | 12,3 |
| -10,00% | 0,06549 $ | 26/40 | +65,00% | +10,00% | 0,08005 $ | 2/26 | +7,69% | +22,22% | DEBOLE | 6,8 | 12,0 |
| -10,00% | 0,06549 $ | 26/40 | +65,00% | +15,00% | 0,08369 $ | 1/26 | +3,85% | +27,78% | DEBOLE | 6,8 | 10,0 |
| -10,00% | 0,06549 $ | 26/40 | +65,00% | +20,00% | 0,08732 $ | 0/26 | 0,00% | +33,33% | DEBOLE | 6,8 | n/d |
| -15,00% | 0,06185 $ | 23/40 | +57,50% | +5,00% | 0,07641 $ | 3/23 | +13,04% | +23,53% | DEBOLE | 7,4 | 12,3 |
| -15,00% | 0,06185 $ | 23/40 | +57,50% | +10,00% | 0,08005 $ | 2/23 | +8,70% | +29,41% | DEBOLE | 7,4 | 12,0 |
| -15,00% | 0,06185 $ | 23/40 | +57,50% | +15,00% | 0,08369 $ | 1/23 | +4,35% | +35,29% | DEBOLE | 7,4 | 10,0 |
| -15,00% | 0,06185 $ | 23/40 | +57,50% | +20,00% | 0,08732 $ | 0/23 | 0,00% | +41,18% | DEBOLE | 7,4 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07641 $ | 23/40 | +57,50% | prezzo iniziale | 0,07277 $ | 20/23 | +86,96% | -4,76% | ALTA | 6,1 | 12,3 |
| +5,00% | 0,07641 $ | 23/40 | +57,50% | -5,00% | 0,06913 $ | 15/23 | +65,22% | -9,52% | ALTA | 6,1 | 17,7 |
| +5,00% | 0,07641 $ | 23/40 | +57,50% | -8,00% | 0,06695 $ | 10/23 | +43,48% | -12,38% | BASSA | 6,1 | 19,2 |
| +5,00% | 0,07641 $ | 23/40 | +57,50% | -10,00% | 0,06549 $ | 8/23 | +34,78% | -14,29% | DEBOLE | 6,1 | 22,0 |
| +5,00% | 0,07641 $ | 23/40 | +57,50% | -15,00% | 0,06185 $ | 4/23 | +17,39% | -19,05% | DEBOLE | 6,1 | 23,2 |
| +10,00% | 0,08005 $ | 20/40 | +50,00% | prezzo iniziale | 0,07277 $ | 13/20 | +65,00% | -9,09% | ALTA | 9,6 | 16,3 |
| +10,00% | 0,08005 $ | 20/40 | +50,00% | -5,00% | 0,06913 $ | 10/20 | +50,00% | -13,64% | MEDIA | 9,6 | 21,0 |
| +10,00% | 0,08005 $ | 20/40 | +50,00% | -8,00% | 0,06695 $ | 6/20 | +30,00% | -16,36% | DEBOLE | 9,6 | 20,5 |
| +10,00% | 0,08005 $ | 20/40 | +50,00% | -10,00% | 0,06549 $ | 5/20 | +25,00% | -18,18% | DEBOLE | 9,6 | 20,8 |
| +10,00% | 0,08005 $ | 20/40 | +50,00% | -15,00% | 0,06185 $ | 3/20 | +15,00% | -22,73% | DEBOLE | 9,6 | 24,0 |
| +15,00% | 0,08369 $ | 19/40 | +47,50% | prezzo iniziale | 0,07277 $ | 10/19 | +52,63% | -13,04% | MEDIA | 12,5 | 18,6 |
| +15,00% | 0,08369 $ | 19/40 | +47,50% | -5,00% | 0,06913 $ | 7/19 | +36,84% | -17,39% | BASSA | 12,5 | 22,7 |
| +15,00% | 0,08369 $ | 19/40 | +47,50% | -8,00% | 0,06695 $ | 5/19 | +26,32% | -20,00% | DEBOLE | 12,5 | 20,8 |
| +15,00% | 0,08369 $ | 19/40 | +47,50% | -10,00% | 0,06549 $ | 5/19 | +26,32% | -21,74% | DEBOLE | 12,5 | 20,8 |
| +15,00% | 0,08369 $ | 19/40 | +47,50% | -15,00% | 0,06185 $ | 3/19 | +15,79% | -26,09% | DEBOLE | 12,5 | 24,0 |
| +20,00% | 0,08732 $ | 12/40 | +30,00% | prezzo iniziale | 0,07277 $ | 4/12 | +33,33% | -16,67% | DEBOLE | 15,2 | 19,0 |
| +20,00% | 0,08732 $ | 12/40 | +30,00% | -5,00% | 0,06913 $ | 2/12 | +16,67% | -20,83% | DEBOLE | 15,2 | 28,5 |
| +20,00% | 0,08732 $ | 12/40 | +30,00% | -8,00% | 0,06695 $ | 0/12 | 0,00% | -23,33% | DEBOLE | 15,2 | n/d |
| +20,00% | 0,08732 $ | 12/40 | +30,00% | -10,00% | 0,06549 $ | 0/12 | 0,00% | -25,00% | DEBOLE | 15,2 | n/d |
| +20,00% | 0,08732 $ | 12/40 | +30,00% | -15,00% | 0,06185 $ | 0/12 | 0,00% | -29,17% | DEBOLE | 15,2 | n/d |

---
