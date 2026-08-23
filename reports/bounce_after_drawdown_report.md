# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-08-23 07:31:39 CEST**  
UTC: **2026-08-23 05:31:39 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 72.512 $ | 83.961 $ | +27,27% | +15,79% | rimbalzo poco frequente | 83.961 $ | 72.512 $ | +33,33% | -13,64% | spike storicamente più resistente |
| SOL | 88,53 $ | 102,51 $ | +27,59% | +15,79% | rimbalzo poco frequente | 102,51 $ | 88,53 $ | +23,81% | -13,64% | spike storicamente più resistente |
| DOGE | 0,08614 $ | 0,09974 $ | +59,26% | +15,79% | rimbalzo possibile | 0,09974 $ | 0,08614 $ | +25,71% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 22 prima sono scesi a -5,00%. Tra quei 22, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +27,27% (6/22). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- BTC: su 40 casi simili, 27 prima sono saliti a +10,00%. Tra quei 27, 9 poi sono scaricati a -5,00%. Percentuale: +33,33% (9/27). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 72.512 $ | 22/40 | +55,00% | +5,00% | 80.145 $ | 10/22 | +45,45% | +10,53% | BASSA | 12,1 | 16,6 |
| -5,00% | 72.512 $ | 22/40 | +55,00% | +10,00% | 83.961 $ | 6/22 | +27,27% | +15,79% | DEBOLE | 12,1 | 13,0 |
| -5,00% | 72.512 $ | 22/40 | +55,00% | +15,00% | 87.777 $ | 4/22 | +18,18% | +21,05% | DEBOLE | 12,1 | 11,2 |
| -5,00% | 72.512 $ | 22/40 | +55,00% | +20,00% | 91.594 $ | 3/22 | +13,64% | +26,32% | DEBOLE | 12,1 | 20,3 |
| -8,00% | 70.222 $ | 16/40 | +40,00% | +5,00% | 80.145 $ | 5/16 | +31,25% | +14,13% | DEBOLE | 15,2 | 17,4 |
| -8,00% | 70.222 $ | 16/40 | +40,00% | +10,00% | 83.961 $ | 4/16 | +25,00% | +19,57% | DEBOLE | 15,2 | 16,2 |
| -8,00% | 70.222 $ | 16/40 | +40,00% | +15,00% | 87.777 $ | 3/16 | +18,75% | +25,00% | DEBOLE | 15,2 | 21,3 |
| -8,00% | 70.222 $ | 16/40 | +40,00% | +20,00% | 91.594 $ | 2/16 | +12,50% | +30,43% | DEBOLE | 15,2 | 26,5 |
| -10,00% | 68.695 $ | 16/40 | +40,00% | +5,00% | 80.145 $ | 4/16 | +25,00% | +16,67% | DEBOLE | 18,2 | 21,0 |
| -10,00% | 68.695 $ | 16/40 | +40,00% | +10,00% | 83.961 $ | 3/16 | +18,75% | +22,22% | DEBOLE | 18,2 | 20,7 |
| -10,00% | 68.695 $ | 16/40 | +40,00% | +15,00% | 87.777 $ | 3/16 | +18,75% | +27,78% | DEBOLE | 18,2 | 21,3 |
| -10,00% | 68.695 $ | 16/40 | +40,00% | +20,00% | 91.594 $ | 2/16 | +12,50% | +33,33% | DEBOLE | 18,2 | 26,5 |
| -15,00% | 64.879 $ | 6/40 | +15,00% | +5,00% | 80.145 $ | 0/6 | 0,00% | +23,53% | DEBOLE | 18,3 | n/d |
| -15,00% | 64.879 $ | 6/40 | +15,00% | +10,00% | 83.961 $ | 0/6 | 0,00% | +29,41% | DEBOLE | 18,3 | n/d |
| -15,00% | 64.879 $ | 6/40 | +15,00% | +15,00% | 87.777 $ | 0/6 | 0,00% | +35,29% | DEBOLE | 18,3 | n/d |
| -15,00% | 64.879 $ | 6/40 | +15,00% | +20,00% | 91.594 $ | 0/6 | 0,00% | +41,18% | DEBOLE | 18,3 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 80.145 $ | 33/40 | +82,50% | prezzo iniziale | 76.328 $ | 15/33 | +45,45% | -4,76% | BASSA | 6,6 | 14,1 |
| +5,00% | 80.145 $ | 33/40 | +82,50% | -5,00% | 72.512 $ | 10/33 | +30,30% | -9,52% | DEBOLE | 6,6 | 16,6 |
| +5,00% | 80.145 $ | 33/40 | +82,50% | -8,00% | 70.222 $ | 7/33 | +21,21% | -12,38% | DEBOLE | 6,6 | 21,3 |
| +5,00% | 80.145 $ | 33/40 | +82,50% | -10,00% | 68.695 $ | 7/33 | +21,21% | -14,29% | DEBOLE | 6,6 | 22,9 |
| +5,00% | 80.145 $ | 33/40 | +82,50% | -15,00% | 64.879 $ | 2/33 | +6,06% | -19,05% | DEBOLE | 6,6 | 25,5 |
| +10,00% | 83.961 $ | 27/40 | +67,50% | prezzo iniziale | 76.328 $ | 13/27 | +48,15% | -9,09% | BASSA | 6,6 | 14,9 |
| +10,00% | 83.961 $ | 27/40 | +67,50% | -5,00% | 72.512 $ | 9/27 | +33,33% | -13,64% | DEBOLE | 6,6 | 15,2 |
| +10,00% | 83.961 $ | 27/40 | +67,50% | -8,00% | 70.222 $ | 6/27 | +22,22% | -16,36% | DEBOLE | 6,6 | 20,0 |
| +10,00% | 83.961 $ | 27/40 | +67,50% | -10,00% | 68.695 $ | 6/27 | +22,22% | -18,18% | DEBOLE | 6,6 | 21,8 |
| +10,00% | 83.961 $ | 27/40 | +67,50% | -15,00% | 64.879 $ | 2/27 | +7,41% | -22,73% | DEBOLE | 6,6 | 25,5 |
| +15,00% | 87.777 $ | 21/40 | +52,50% | prezzo iniziale | 76.328 $ | 8/21 | +38,10% | -13,04% | BASSA | 8,0 | 16,8 |
| +15,00% | 87.777 $ | 21/40 | +52,50% | -5,00% | 72.512 $ | 4/21 | +19,05% | -17,39% | DEBOLE | 8,0 | 16,8 |
| +15,00% | 87.777 $ | 21/40 | +52,50% | -8,00% | 70.222 $ | 4/21 | +19,05% | -20,00% | DEBOLE | 8,0 | 19,8 |
| +15,00% | 87.777 $ | 21/40 | +52,50% | -10,00% | 68.695 $ | 4/21 | +19,05% | -21,74% | DEBOLE | 8,0 | 21,5 |
| +15,00% | 87.777 $ | 21/40 | +52,50% | -15,00% | 64.879 $ | 2/21 | +9,52% | -26,09% | DEBOLE | 8,0 | 25,5 |
| +20,00% | 91.594 $ | 16/40 | +40,00% | prezzo iniziale | 76.328 $ | 4/16 | +25,00% | -16,67% | DEBOLE | 11,2 | 18,2 |
| +20,00% | 91.594 $ | 16/40 | +40,00% | -5,00% | 72.512 $ | 2/16 | +12,50% | -20,83% | DEBOLE | 11,2 | 21,5 |
| +20,00% | 91.594 $ | 16/40 | +40,00% | -8,00% | 70.222 $ | 2/16 | +12,50% | -23,33% | DEBOLE | 11,2 | 21,5 |
| +20,00% | 91.594 $ | 16/40 | +40,00% | -10,00% | 68.695 $ | 2/16 | +12,50% | -25,00% | DEBOLE | 11,2 | 24,0 |
| +20,00% | 91.594 $ | 16/40 | +40,00% | -15,00% | 64.879 $ | 1/16 | +6,25% | -29,17% | DEBOLE | 11,2 | 30,0 |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 29 prima sono scesi a -5,00%. Tra quei 29, 8 poi sono rimbalzati fino a +10,00%. Percentuale: +27,59% (8/29). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 21 prima sono saliti a +10,00%. Tra quei 21, 5 poi sono scaricati a -5,00%. Percentuale: +23,81% (5/21). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 88,53 $ | 29/40 | +72,50% | +5,00% | 97,85 $ | 12/29 | +41,38% | +10,53% | BASSA | 10,1 | 17,2 |
| -5,00% | 88,53 $ | 29/40 | +72,50% | +10,00% | 102,51 $ | 8/29 | +27,59% | +15,79% | DEBOLE | 10,1 | 17,2 |
| -5,00% | 88,53 $ | 29/40 | +72,50% | +15,00% | 107,17 $ | 6/29 | +20,69% | +21,05% | DEBOLE | 10,1 | 18,7 |
| -5,00% | 88,53 $ | 29/40 | +72,50% | +20,00% | 111,83 $ | 4/29 | +13,79% | +26,32% | DEBOLE | 10,1 | 18,5 |
| -8,00% | 85,73 $ | 23/40 | +57,50% | +5,00% | 97,85 $ | 6/23 | +26,09% | +14,13% | DEBOLE | 15,5 | 21,5 |
| -8,00% | 85,73 $ | 23/40 | +57,50% | +10,00% | 102,51 $ | 3/23 | +13,04% | +19,57% | DEBOLE | 15,5 | 19,3 |
| -8,00% | 85,73 $ | 23/40 | +57,50% | +15,00% | 107,17 $ | 2/23 | +8,70% | +25,00% | DEBOLE | 15,5 | 27,0 |
| -8,00% | 85,73 $ | 23/40 | +57,50% | +20,00% | 111,83 $ | 1/23 | +4,35% | +30,43% | DEBOLE | 15,5 | 26,0 |
| -10,00% | 83,87 $ | 18/40 | +45,00% | +5,00% | 97,85 $ | 2/18 | +11,11% | +16,67% | DEBOLE | 19,8 | 19,5 |
| -10,00% | 83,87 $ | 18/40 | +45,00% | +10,00% | 102,51 $ | 2/18 | +11,11% | +22,22% | DEBOLE | 19,8 | 21,0 |
| -10,00% | 83,87 $ | 18/40 | +45,00% | +15,00% | 107,17 $ | 2/18 | +11,11% | +27,78% | DEBOLE | 19,8 | 27,0 |
| -10,00% | 83,87 $ | 18/40 | +45,00% | +20,00% | 111,83 $ | 1/18 | +5,56% | +33,33% | DEBOLE | 19,8 | 26,0 |
| -15,00% | 79,21 $ | 5/40 | +12,50% | +5,00% | 97,85 $ | 0/5 | 0,00% | +23,53% | DEBOLE | 19,8 | n/d |
| -15,00% | 79,21 $ | 5/40 | +12,50% | +10,00% | 102,51 $ | 0/5 | 0,00% | +29,41% | DEBOLE | 19,8 | n/d |
| -15,00% | 79,21 $ | 5/40 | +12,50% | +15,00% | 107,17 $ | 0/5 | 0,00% | +35,29% | DEBOLE | 19,8 | n/d |
| -15,00% | 79,21 $ | 5/40 | +12,50% | +20,00% | 111,83 $ | 0/5 | 0,00% | +41,18% | DEBOLE | 19,8 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 97,85 $ | 28/40 | +70,00% | prezzo iniziale | 93,19 $ | 16/28 | +57,14% | -4,76% | MEDIA | 7,4 | 14,6 |
| +5,00% | 97,85 $ | 28/40 | +70,00% | -5,00% | 88,53 $ | 11/28 | +39,29% | -9,52% | BASSA | 7,4 | 15,7 |
| +5,00% | 97,85 $ | 28/40 | +70,00% | -8,00% | 85,73 $ | 7/28 | +25,00% | -12,38% | DEBOLE | 7,4 | 18,1 |
| +5,00% | 97,85 $ | 28/40 | +70,00% | -10,00% | 83,87 $ | 6/28 | +21,43% | -14,29% | DEBOLE | 7,4 | 20,8 |
| +5,00% | 97,85 $ | 28/40 | +70,00% | -15,00% | 79,21 $ | 2/28 | +7,14% | -19,05% | DEBOLE | 7,4 | 19,5 |
| +10,00% | 102,51 $ | 21/40 | +52,50% | prezzo iniziale | 93,19 $ | 9/21 | +42,86% | -9,09% | BASSA | 8,8 | 17,8 |
| +10,00% | 102,51 $ | 21/40 | +52,50% | -5,00% | 88,53 $ | 5/21 | +23,81% | -13,64% | DEBOLE | 8,8 | 18,8 |
| +10,00% | 102,51 $ | 21/40 | +52,50% | -8,00% | 85,73 $ | 3/21 | +14,29% | -16,36% | DEBOLE | 8,8 | 25,7 |
| +10,00% | 102,51 $ | 21/40 | +52,50% | -10,00% | 83,87 $ | 3/21 | +14,29% | -18,18% | DEBOLE | 8,8 | 27,3 |
| +10,00% | 102,51 $ | 21/40 | +52,50% | -15,00% | 79,21 $ | 0/21 | 0,00% | -22,73% | DEBOLE | 8,8 | n/d |
| +15,00% | 107,17 $ | 18/40 | +45,00% | prezzo iniziale | 93,19 $ | 5/18 | +27,78% | -13,04% | DEBOLE | 11,1 | 21,8 |
| +15,00% | 107,17 $ | 18/40 | +45,00% | -5,00% | 88,53 $ | 2/18 | +11,11% | -17,39% | DEBOLE | 11,1 | 18,0 |
| +15,00% | 107,17 $ | 18/40 | +45,00% | -8,00% | 85,73 $ | 1/18 | +5,56% | -20,00% | DEBOLE | 11,1 | 21,0 |
| +15,00% | 107,17 $ | 18/40 | +45,00% | -10,00% | 83,87 $ | 1/18 | +5,56% | -21,74% | DEBOLE | 11,1 | 26,0 |
| +15,00% | 107,17 $ | 18/40 | +45,00% | -15,00% | 79,21 $ | 0/18 | 0,00% | -26,09% | DEBOLE | 11,1 | n/d |
| +20,00% | 111,83 $ | 14/40 | +35,00% | prezzo iniziale | 93,19 $ | 3/14 | +21,43% | -16,67% | DEBOLE | 13,6 | 25,0 |
| +20,00% | 111,83 $ | 14/40 | +35,00% | -5,00% | 88,53 $ | 1/14 | +7,14% | -20,83% | DEBOLE | 13,6 | 21,0 |
| +20,00% | 111,83 $ | 14/40 | +35,00% | -8,00% | 85,73 $ | 1/14 | +7,14% | -23,33% | DEBOLE | 13,6 | 21,0 |
| +20,00% | 111,83 $ | 14/40 | +35,00% | -10,00% | 83,87 $ | 1/14 | +7,14% | -25,00% | DEBOLE | 13,6 | 26,0 |
| +20,00% | 111,83 $ | 14/40 | +35,00% | -15,00% | 79,21 $ | 0/14 | 0,00% | -29,17% | DEBOLE | 13,6 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 27 prima sono scesi a -5,00%. Tra quei 27, 16 poi sono rimbalzati fino a +10,00%. Percentuale: +59,26% (16/27). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.
- DOGE: su 40 casi simili, 35 prima sono saliti a +10,00%. Tra quei 35, 9 poi sono scaricati a -5,00%. Percentuale: +25,71% (9/35). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,08614 $ | 27/40 | +67,50% | +5,00% | 0,09520 $ | 18/27 | +66,67% | +10,53% | ALTA | 9,1 | 14,8 |
| -5,00% | 0,08614 $ | 27/40 | +67,50% | +10,00% | 0,09974 $ | 16/27 | +59,26% | +15,79% | MEDIA | 9,1 | 15,8 |
| -5,00% | 0,08614 $ | 27/40 | +67,50% | +15,00% | 0,10427 $ | 13/27 | +48,15% | +21,05% | BASSA | 9,1 | 17,6 |
| -5,00% | 0,08614 $ | 27/40 | +67,50% | +20,00% | 0,10880 $ | 6/27 | +22,22% | +26,32% | DEBOLE | 9,1 | 20,8 |
| -8,00% | 0,08342 $ | 19/40 | +47,50% | +5,00% | 0,09520 $ | 9/19 | +47,37% | +14,13% | BASSA | 12,6 | 15,7 |
| -8,00% | 0,08342 $ | 19/40 | +47,50% | +10,00% | 0,09974 $ | 9/19 | +47,37% | +19,57% | BASSA | 12,6 | 16,9 |
| -8,00% | 0,08342 $ | 19/40 | +47,50% | +15,00% | 0,10427 $ | 8/19 | +42,11% | +25,00% | BASSA | 12,6 | 18,6 |
| -8,00% | 0,08342 $ | 19/40 | +47,50% | +20,00% | 0,10880 $ | 3/19 | +15,79% | +30,43% | DEBOLE | 12,6 | 22,0 |
| -10,00% | 0,08160 $ | 15/40 | +37,50% | +5,00% | 0,09520 $ | 3/15 | +20,00% | +16,67% | DEBOLE | 16,5 | 16,3 |
| -10,00% | 0,08160 $ | 15/40 | +37,50% | +10,00% | 0,09974 $ | 3/15 | +20,00% | +22,22% | DEBOLE | 16,5 | 17,0 |
| -10,00% | 0,08160 $ | 15/40 | +37,50% | +15,00% | 0,10427 $ | 3/15 | +20,00% | +27,78% | DEBOLE | 16,5 | 18,3 |
| -10,00% | 0,08160 $ | 15/40 | +37,50% | +20,00% | 0,10880 $ | 1/15 | +6,67% | +33,33% | DEBOLE | 16,5 | 26,0 |
| -15,00% | 0,07707 $ | 9/40 | +22,50% | +5,00% | 0,09520 $ | 0/9 | 0,00% | +23,53% | DEBOLE | 19,9 | n/d |
| -15,00% | 0,07707 $ | 9/40 | +22,50% | +10,00% | 0,09974 $ | 0/9 | 0,00% | +29,41% | DEBOLE | 19,9 | n/d |
| -15,00% | 0,07707 $ | 9/40 | +22,50% | +15,00% | 0,10427 $ | 0/9 | 0,00% | +35,29% | DEBOLE | 19,9 | n/d |
| -15,00% | 0,07707 $ | 9/40 | +22,50% | +20,00% | 0,10880 $ | 0/9 | 0,00% | +41,18% | DEBOLE | 19,9 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,09520 $ | 36/40 | +90,00% | prezzo iniziale | 0,09067 $ | 18/36 | +50,00% | -4,76% | MEDIA | 6,3 | 12,4 |
| +5,00% | 0,09520 $ | 36/40 | +90,00% | -5,00% | 0,08614 $ | 13/36 | +36,11% | -9,52% | BASSA | 6,3 | 17,5 |
| +5,00% | 0,09520 $ | 36/40 | +90,00% | -8,00% | 0,08342 $ | 8/36 | +22,22% | -12,38% | DEBOLE | 6,3 | 21,8 |
| +5,00% | 0,09520 $ | 36/40 | +90,00% | -10,00% | 0,08160 $ | 8/36 | +22,22% | -14,29% | DEBOLE | 6,3 | 23,6 |
| +5,00% | 0,09520 $ | 36/40 | +90,00% | -15,00% | 0,07707 $ | 5/36 | +13,89% | -19,05% | DEBOLE | 6,3 | 25,4 |
| +10,00% | 0,09974 $ | 35/40 | +87,50% | prezzo iniziale | 0,09067 $ | 15/35 | +42,86% | -9,09% | BASSA | 9,9 | 19,5 |
| +10,00% | 0,09974 $ | 35/40 | +87,50% | -5,00% | 0,08614 $ | 9/35 | +25,71% | -13,64% | DEBOLE | 9,9 | 21,8 |
| +10,00% | 0,09974 $ | 35/40 | +87,50% | -8,00% | 0,08342 $ | 7/35 | +20,00% | -16,36% | DEBOLE | 9,9 | 23,3 |
| +10,00% | 0,09974 $ | 35/40 | +87,50% | -10,00% | 0,08160 $ | 7/35 | +20,00% | -18,18% | DEBOLE | 9,9 | 24,0 |
| +10,00% | 0,09974 $ | 35/40 | +87,50% | -15,00% | 0,07707 $ | 4/35 | +11,43% | -22,73% | DEBOLE | 9,9 | 26,2 |
| +15,00% | 0,10427 $ | 31/40 | +77,50% | prezzo iniziale | 0,09067 $ | 11/31 | +35,48% | -13,04% | BASSA | 11,3 | 21,1 |
| +15,00% | 0,10427 $ | 31/40 | +77,50% | -5,00% | 0,08614 $ | 6/31 | +19,35% | -17,39% | DEBOLE | 11,3 | 21,8 |
| +15,00% | 0,10427 $ | 31/40 | +77,50% | -8,00% | 0,08342 $ | 4/31 | +12,90% | -20,00% | DEBOLE | 11,3 | 21,5 |
| +15,00% | 0,10427 $ | 31/40 | +77,50% | -10,00% | 0,08160 $ | 4/31 | +12,90% | -21,74% | DEBOLE | 11,3 | 22,2 |
| +15,00% | 0,10427 $ | 31/40 | +77,50% | -15,00% | 0,07707 $ | 3/31 | +9,68% | -26,09% | DEBOLE | 11,3 | 25,0 |
| +20,00% | 0,10880 $ | 21/40 | +52,50% | prezzo iniziale | 0,09067 $ | 5/21 | +23,81% | -16,67% | DEBOLE | 12,8 | 24,6 |
| +20,00% | 0,10880 $ | 21/40 | +52,50% | -5,00% | 0,08614 $ | 2/21 | +9,52% | -20,83% | DEBOLE | 12,8 | 23,0 |
| +20,00% | 0,10880 $ | 21/40 | +52,50% | -8,00% | 0,08342 $ | 0/21 | 0,00% | -23,33% | DEBOLE | 12,8 | n/d |
| +20,00% | 0,10880 $ | 21/40 | +52,50% | -10,00% | 0,08160 $ | 0/21 | 0,00% | -25,00% | DEBOLE | 12,8 | n/d |
| +20,00% | 0,10880 $ | 21/40 | +52,50% | -15,00% | 0,07707 $ | 0/21 | 0,00% | -29,17% | DEBOLE | 12,8 | n/d |

---
