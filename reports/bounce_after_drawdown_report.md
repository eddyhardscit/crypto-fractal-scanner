# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-10-18 07:32:45 CEST**  
UTC: **2026-10-18 05:32:45 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 77.560 $ | 89.806 $ | +30,77% | +15,79% | rimbalzo poco frequente | 89.806 $ | 77.560 $ | +16,00% | -13,64% | spike storicamente più resistente |
| SOL | 98,27 $ | 113,78 $ | +24,00% | +15,79% | rimbalzo poco frequente | 113,78 $ | 98,27 $ | +20,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07519 $ | 0,08706 $ | +37,50% | +15,79% | rimbalzo debole | 0,08706 $ | 0,07519 $ | +3,23% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 26 prima sono scesi a -5,00%. Tra quei 26, 8 poi sono rimbalzati fino a +10,00%. Percentuale: +30,77% (8/26). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- BTC: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 4 poi sono scaricati a -5,00%. Percentuale: +16,00% (4/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 77.560 $ | 26/40 | +65,00% | +5,00% | 85.724 $ | 13/26 | +50,00% | +10,53% | MEDIA | 6,4 | 17,1 |
| -5,00% | 77.560 $ | 26/40 | +65,00% | +10,00% | 89.806 $ | 8/26 | +30,77% | +15,79% | DEBOLE | 6,4 | 16,4 |
| -5,00% | 77.560 $ | 26/40 | +65,00% | +15,00% | 93.888 $ | 5/26 | +19,23% | +21,05% | DEBOLE | 6,4 | 12,6 |
| -5,00% | 77.560 $ | 26/40 | +65,00% | +20,00% | 97.970 $ | 4/26 | +15,38% | +26,32% | DEBOLE | 6,4 | 13,8 |
| -8,00% | 75.111 $ | 21/40 | +52,50% | +5,00% | 85.724 $ | 8/21 | +38,10% | +14,13% | BASSA | 10,2 | 19,0 |
| -8,00% | 75.111 $ | 21/40 | +52,50% | +10,00% | 89.806 $ | 5/21 | +23,81% | +19,57% | DEBOLE | 10,2 | 19,8 |
| -8,00% | 75.111 $ | 21/40 | +52,50% | +15,00% | 93.888 $ | 2/21 | +9,52% | +25,00% | DEBOLE | 10,2 | 13,5 |
| -8,00% | 75.111 $ | 21/40 | +52,50% | +20,00% | 97.970 $ | 2/21 | +9,52% | +30,43% | DEBOLE | 10,2 | 18,0 |
| -10,00% | 73.478 $ | 16/40 | +40,00% | +5,00% | 85.724 $ | 5/16 | +31,25% | +16,67% | DEBOLE | 9,8 | 20,2 |
| -10,00% | 73.478 $ | 16/40 | +40,00% | +10,00% | 89.806 $ | 3/16 | +18,75% | +22,22% | DEBOLE | 9,8 | 24,0 |
| -10,00% | 73.478 $ | 16/40 | +40,00% | +15,00% | 93.888 $ | 1/16 | +6,25% | +27,78% | DEBOLE | 9,8 | 17,0 |
| -10,00% | 73.478 $ | 16/40 | +40,00% | +20,00% | 97.970 $ | 1/16 | +6,25% | +33,33% | DEBOLE | 9,8 | 26,0 |
| -15,00% | 69.396 $ | 9/40 | +22,50% | +5,00% | 85.724 $ | 2/9 | +22,22% | +23,53% | DEBOLE | 13,3 | 29,0 |
| -15,00% | 69.396 $ | 9/40 | +22,50% | +10,00% | 89.806 $ | 1/9 | +11,11% | +29,41% | DEBOLE | 13,3 | 28,0 |
| -15,00% | 69.396 $ | 9/40 | +22,50% | +15,00% | 93.888 $ | 0/9 | 0,00% | +35,29% | DEBOLE | 13,3 | n/d |
| -15,00% | 69.396 $ | 9/40 | +22,50% | +20,00% | 97.970 $ | 0/9 | 0,00% | +41,18% | DEBOLE | 13,3 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 85.724 $ | 32/40 | +80,00% | prezzo iniziale | 81.642 $ | 15/32 | +46,88% | -4,76% | BASSA | 8,5 | 17,0 |
| +5,00% | 85.724 $ | 32/40 | +80,00% | -5,00% | 77.560 $ | 11/32 | +34,38% | -9,52% | DEBOLE | 8,5 | 16,6 |
| +5,00% | 85.724 $ | 32/40 | +80,00% | -8,00% | 75.111 $ | 7/32 | +21,88% | -12,38% | DEBOLE | 8,5 | 16,6 |
| +5,00% | 85.724 $ | 32/40 | +80,00% | -10,00% | 73.478 $ | 4/32 | +12,50% | -14,29% | DEBOLE | 8,5 | 13,0 |
| +5,00% | 85.724 $ | 32/40 | +80,00% | -15,00% | 69.396 $ | 2/32 | +6,25% | -19,05% | DEBOLE | 8,5 | 15,5 |
| +10,00% | 89.806 $ | 25/40 | +62,50% | prezzo iniziale | 81.642 $ | 9/25 | +36,00% | -9,09% | BASSA | 10,0 | 22,2 |
| +10,00% | 89.806 $ | 25/40 | +62,50% | -5,00% | 77.560 $ | 4/25 | +16,00% | -13,64% | DEBOLE | 10,0 | 20,0 |
| +10,00% | 89.806 $ | 25/40 | +62,50% | -8,00% | 75.111 $ | 2/25 | +8,00% | -16,36% | DEBOLE | 10,0 | 18,0 |
| +10,00% | 89.806 $ | 25/40 | +62,50% | -10,00% | 73.478 $ | 1/25 | +4,00% | -18,18% | DEBOLE | 10,0 | 17,0 |
| +10,00% | 89.806 $ | 25/40 | +62,50% | -15,00% | 69.396 $ | 0/25 | 0,00% | -22,73% | DEBOLE | 10,0 | n/d |
| +15,00% | 93.888 $ | 16/40 | +40,00% | prezzo iniziale | 81.642 $ | 2/16 | +12,50% | -13,04% | DEBOLE | 10,6 | 25,0 |
| +15,00% | 93.888 $ | 16/40 | +40,00% | -5,00% | 77.560 $ | 1/16 | +6,25% | -17,39% | DEBOLE | 10,6 | 27,0 |
| +15,00% | 93.888 $ | 16/40 | +40,00% | -8,00% | 75.111 $ | 0/16 | 0,00% | -20,00% | DEBOLE | 10,6 | n/d |
| +15,00% | 93.888 $ | 16/40 | +40,00% | -10,00% | 73.478 $ | 0/16 | 0,00% | -21,74% | DEBOLE | 10,6 | n/d |
| +15,00% | 93.888 $ | 16/40 | +40,00% | -15,00% | 69.396 $ | 0/16 | 0,00% | -26,09% | DEBOLE | 10,6 | n/d |
| +20,00% | 97.970 $ | 14/40 | +35,00% | prezzo iniziale | 81.642 $ | 1/14 | +7,14% | -16,67% | DEBOLE | 13,9 | 25,0 |
| +20,00% | 97.970 $ | 14/40 | +35,00% | -5,00% | 77.560 $ | 1/14 | +7,14% | -20,83% | DEBOLE | 13,9 | 27,0 |
| +20,00% | 97.970 $ | 14/40 | +35,00% | -8,00% | 75.111 $ | 0/14 | 0,00% | -23,33% | DEBOLE | 13,9 | n/d |
| +20,00% | 97.970 $ | 14/40 | +35,00% | -10,00% | 73.478 $ | 0/14 | 0,00% | -25,00% | DEBOLE | 13,9 | n/d |
| +20,00% | 97.970 $ | 14/40 | +35,00% | -15,00% | 69.396 $ | 0/14 | 0,00% | -29,17% | DEBOLE | 13,9 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 25 prima sono scesi a -5,00%. Tra quei 25, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +24,00% (6/25). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 5 poi sono scaricati a -5,00%. Percentuale: +20,00% (5/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 98,27 $ | 25/40 | +62,50% | +5,00% | 108,61 $ | 14/25 | +56,00% | +10,53% | MEDIA | 6,5 | 19,6 |
| -5,00% | 98,27 $ | 25/40 | +62,50% | +10,00% | 113,78 $ | 6/25 | +24,00% | +15,79% | DEBOLE | 6,5 | 18,3 |
| -5,00% | 98,27 $ | 25/40 | +62,50% | +15,00% | 118,96 $ | 3/25 | +12,00% | +21,05% | DEBOLE | 6,5 | 13,3 |
| -5,00% | 98,27 $ | 25/40 | +62,50% | +20,00% | 124,13 $ | 3/25 | +12,00% | +26,32% | DEBOLE | 6,5 | 13,3 |
| -8,00% | 95,16 $ | 21/40 | +52,50% | +5,00% | 108,61 $ | 10/21 | +47,62% | +14,13% | BASSA | 9,1 | 20,0 |
| -8,00% | 95,16 $ | 21/40 | +52,50% | +10,00% | 113,78 $ | 4/21 | +19,05% | +19,57% | DEBOLE | 9,1 | 20,5 |
| -8,00% | 95,16 $ | 21/40 | +52,50% | +15,00% | 118,96 $ | 1/21 | +4,76% | +25,00% | DEBOLE | 9,1 | 10,0 |
| -8,00% | 95,16 $ | 21/40 | +52,50% | +20,00% | 124,13 $ | 1/21 | +4,76% | +30,43% | DEBOLE | 9,1 | 10,0 |
| -10,00% | 93,10 $ | 15/40 | +37,50% | +5,00% | 108,61 $ | 5/15 | +33,33% | +16,67% | DEBOLE | 9,7 | 22,2 |
| -10,00% | 93,10 $ | 15/40 | +37,50% | +10,00% | 113,78 $ | 2/15 | +13,33% | +22,22% | DEBOLE | 9,7 | 27,5 |
| -10,00% | 93,10 $ | 15/40 | +37,50% | +15,00% | 118,96 $ | 0/15 | 0,00% | +27,78% | DEBOLE | 9,7 | n/d |
| -10,00% | 93,10 $ | 15/40 | +37,50% | +20,00% | 124,13 $ | 0/15 | 0,00% | +33,33% | DEBOLE | 9,7 | n/d |
| -15,00% | 87,92 $ | 10/40 | +25,00% | +5,00% | 108,61 $ | 2/10 | +20,00% | +23,53% | DEBOLE | 10,6 | 29,0 |
| -15,00% | 87,92 $ | 10/40 | +25,00% | +10,00% | 113,78 $ | 1/10 | +10,00% | +29,41% | DEBOLE | 10,6 | 28,0 |
| -15,00% | 87,92 $ | 10/40 | +25,00% | +15,00% | 118,96 $ | 0/10 | 0,00% | +35,29% | DEBOLE | 10,6 | n/d |
| -15,00% | 87,92 $ | 10/40 | +25,00% | +20,00% | 124,13 $ | 0/10 | 0,00% | +41,18% | DEBOLE | 10,6 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 108,61 $ | 32/40 | +80,00% | prezzo iniziale | 103,44 $ | 20/32 | +62,50% | -4,76% | MEDIA | 7,2 | 16,6 |
| +5,00% | 108,61 $ | 32/40 | +80,00% | -5,00% | 98,27 $ | 12/32 | +37,50% | -9,52% | BASSA | 7,2 | 16,7 |
| +5,00% | 108,61 $ | 32/40 | +80,00% | -8,00% | 95,16 $ | 8/32 | +25,00% | -12,38% | DEBOLE | 7,2 | 17,8 |
| +5,00% | 108,61 $ | 32/40 | +80,00% | -10,00% | 93,10 $ | 4/32 | +12,50% | -14,29% | DEBOLE | 7,2 | 18,2 |
| +5,00% | 108,61 $ | 32/40 | +80,00% | -15,00% | 87,92 $ | 3/32 | +9,38% | -19,05% | DEBOLE | 7,2 | 20,0 |
| +10,00% | 113,78 $ | 25/40 | +62,50% | prezzo iniziale | 103,44 $ | 12/25 | +48,00% | -9,09% | BASSA | 9,6 | 19,8 |
| +10,00% | 113,78 $ | 25/40 | +62,50% | -5,00% | 98,27 $ | 5/25 | +20,00% | -13,64% | DEBOLE | 9,6 | 19,4 |
| +10,00% | 113,78 $ | 25/40 | +62,50% | -8,00% | 95,16 $ | 3/25 | +12,00% | -16,36% | DEBOLE | 9,6 | 18,0 |
| +10,00% | 113,78 $ | 25/40 | +62,50% | -10,00% | 93,10 $ | 1/25 | +4,00% | -18,18% | DEBOLE | 9,6 | 16,0 |
| +10,00% | 113,78 $ | 25/40 | +62,50% | -15,00% | 87,92 $ | 0/25 | 0,00% | -22,73% | DEBOLE | 9,6 | n/d |
| +15,00% | 118,96 $ | 13/40 | +32,50% | prezzo iniziale | 103,44 $ | 2/13 | +15,38% | -13,04% | DEBOLE | 12,1 | 25,0 |
| +15,00% | 118,96 $ | 13/40 | +32,50% | -5,00% | 98,27 $ | 1/13 | +7,69% | -17,39% | DEBOLE | 12,1 | 27,0 |
| +15,00% | 118,96 $ | 13/40 | +32,50% | -8,00% | 95,16 $ | 0/13 | 0,00% | -20,00% | DEBOLE | 12,1 | n/d |
| +15,00% | 118,96 $ | 13/40 | +32,50% | -10,00% | 93,10 $ | 0/13 | 0,00% | -21,74% | DEBOLE | 12,1 | n/d |
| +15,00% | 118,96 $ | 13/40 | +32,50% | -15,00% | 87,92 $ | 0/13 | 0,00% | -26,09% | DEBOLE | 12,1 | n/d |
| +20,00% | 124,13 $ | 10/40 | +25,00% | prezzo iniziale | 103,44 $ | 1/10 | +10,00% | -16,67% | DEBOLE | 13,4 | 25,0 |
| +20,00% | 124,13 $ | 10/40 | +25,00% | -5,00% | 98,27 $ | 1/10 | +10,00% | -20,83% | DEBOLE | 13,4 | 27,0 |
| +20,00% | 124,13 $ | 10/40 | +25,00% | -8,00% | 95,16 $ | 0/10 | 0,00% | -23,33% | DEBOLE | 13,4 | n/d |
| +20,00% | 124,13 $ | 10/40 | +25,00% | -10,00% | 93,10 $ | 0/10 | 0,00% | -25,00% | DEBOLE | 13,4 | n/d |
| +20,00% | 124,13 $ | 10/40 | +25,00% | -15,00% | 87,92 $ | 0/10 | 0,00% | -29,17% | DEBOLE | 13,4 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 16 prima sono scesi a -5,00%. Tra quei 16, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +37,50% (6/16). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- DOGE: su 40 casi simili, 31 prima sono saliti a +10,00%. Tra quei 31, 1 poi sono scaricati a -5,00%. Percentuale: +3,23% (1/31). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,07519 $ | 16/40 | +40,00% | +5,00% | 0,08311 $ | 7/16 | +43,75% | +10,53% | BASSA | 5,4 | 18,3 |
| -5,00% | 0,07519 $ | 16/40 | +40,00% | +10,00% | 0,08706 $ | 6/16 | +37,50% | +15,79% | BASSA | 5,4 | 22,0 |
| -5,00% | 0,07519 $ | 16/40 | +40,00% | +15,00% | 0,09102 $ | 3/16 | +18,75% | +21,05% | DEBOLE | 5,4 | 20,7 |
| -5,00% | 0,07519 $ | 16/40 | +40,00% | +20,00% | 0,09498 $ | 2/16 | +12,50% | +26,32% | DEBOLE | 5,4 | 16,0 |
| -8,00% | 0,07282 $ | 13/40 | +32,50% | +5,00% | 0,08311 $ | 4/13 | +30,77% | +14,13% | DEBOLE | 8,6 | 19,5 |
| -8,00% | 0,07282 $ | 13/40 | +32,50% | +10,00% | 0,08706 $ | 4/13 | +30,77% | +19,57% | DEBOLE | 8,6 | 20,2 |
| -8,00% | 0,07282 $ | 13/40 | +32,50% | +15,00% | 0,09102 $ | 1/13 | +7,69% | +25,00% | DEBOLE | 8,6 | 10,0 |
| -8,00% | 0,07282 $ | 13/40 | +32,50% | +20,00% | 0,09498 $ | 1/13 | +7,69% | +30,43% | DEBOLE | 8,6 | 10,0 |
| -10,00% | 0,07123 $ | 10/40 | +25,00% | +5,00% | 0,08311 $ | 2/10 | +20,00% | +16,67% | DEBOLE | 9,0 | 27,0 |
| -10,00% | 0,07123 $ | 10/40 | +25,00% | +10,00% | 0,08706 $ | 2/10 | +20,00% | +22,22% | DEBOLE | 9,0 | 27,0 |
| -10,00% | 0,07123 $ | 10/40 | +25,00% | +15,00% | 0,09102 $ | 0/10 | 0,00% | +27,78% | DEBOLE | 9,0 | n/d |
| -10,00% | 0,07123 $ | 10/40 | +25,00% | +20,00% | 0,09498 $ | 0/10 | 0,00% | +33,33% | DEBOLE | 9,0 | n/d |
| -15,00% | 0,06728 $ | 7/40 | +17,50% | +5,00% | 0,08311 $ | 2/7 | +28,57% | +23,53% | DEBOLE | 11,1 | 27,0 |
| -15,00% | 0,06728 $ | 7/40 | +17,50% | +10,00% | 0,08706 $ | 2/7 | +28,57% | +29,41% | DEBOLE | 11,1 | 27,0 |
| -15,00% | 0,06728 $ | 7/40 | +17,50% | +15,00% | 0,09102 $ | 0/7 | 0,00% | +35,29% | DEBOLE | 11,1 | n/d |
| -15,00% | 0,06728 $ | 7/40 | +17,50% | +20,00% | 0,09498 $ | 0/7 | 0,00% | +41,18% | DEBOLE | 11,1 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,08311 $ | 34/40 | +85,00% | prezzo iniziale | 0,07915 $ | 17/34 | +50,00% | -4,76% | MEDIA | 5,7 | 12,9 |
| +5,00% | 0,08311 $ | 34/40 | +85,00% | -5,00% | 0,07519 $ | 4/34 | +11,76% | -9,52% | DEBOLE | 5,7 | 14,0 |
| +5,00% | 0,08311 $ | 34/40 | +85,00% | -8,00% | 0,07282 $ | 3/34 | +8,82% | -12,38% | DEBOLE | 5,7 | 16,0 |
| +5,00% | 0,08311 $ | 34/40 | +85,00% | -10,00% | 0,07123 $ | 2/34 | +5,88% | -14,29% | DEBOLE | 5,7 | 15,5 |
| +5,00% | 0,08311 $ | 34/40 | +85,00% | -15,00% | 0,06728 $ | 2/34 | +5,88% | -19,05% | DEBOLE | 5,7 | 20,5 |
| +10,00% | 0,08706 $ | 31/40 | +77,50% | prezzo iniziale | 0,07915 $ | 9/31 | +29,03% | -9,09% | DEBOLE | 10,5 | 18,4 |
| +10,00% | 0,08706 $ | 31/40 | +77,50% | -5,00% | 0,07519 $ | 1/31 | +3,23% | -13,64% | DEBOLE | 10,5 | 14,0 |
| +10,00% | 0,08706 $ | 31/40 | +77,50% | -8,00% | 0,07282 $ | 1/31 | +3,23% | -16,36% | DEBOLE | 10,5 | 16,0 |
| +10,00% | 0,08706 $ | 31/40 | +77,50% | -10,00% | 0,07123 $ | 1/31 | +3,23% | -18,18% | DEBOLE | 10,5 | 16,0 |
| +10,00% | 0,08706 $ | 31/40 | +77,50% | -15,00% | 0,06728 $ | 1/31 | +3,23% | -22,73% | DEBOLE | 10,5 | 26,0 |
| +15,00% | 0,09102 $ | 20/40 | +50,00% | prezzo iniziale | 0,07915 $ | 1/20 | +5,00% | -13,04% | DEBOLE | 11,2 | 25,0 |
| +15,00% | 0,09102 $ | 20/40 | +50,00% | -5,00% | 0,07519 $ | 0/20 | 0,00% | -17,39% | DEBOLE | 11,2 | n/d |
| +15,00% | 0,09102 $ | 20/40 | +50,00% | -8,00% | 0,07282 $ | 0/20 | 0,00% | -20,00% | DEBOLE | 11,2 | n/d |
| +15,00% | 0,09102 $ | 20/40 | +50,00% | -10,00% | 0,07123 $ | 0/20 | 0,00% | -21,74% | DEBOLE | 11,2 | n/d |
| +15,00% | 0,09102 $ | 20/40 | +50,00% | -15,00% | 0,06728 $ | 0/20 | 0,00% | -26,09% | DEBOLE | 11,2 | n/d |
| +20,00% | 0,09498 $ | 15/40 | +37,50% | prezzo iniziale | 0,07915 $ | 0/15 | 0,00% | -16,67% | DEBOLE | 13,4 | n/d |
| +20,00% | 0,09498 $ | 15/40 | +37,50% | -5,00% | 0,07519 $ | 0/15 | 0,00% | -20,83% | DEBOLE | 13,4 | n/d |
| +20,00% | 0,09498 $ | 15/40 | +37,50% | -8,00% | 0,07282 $ | 0/15 | 0,00% | -23,33% | DEBOLE | 13,4 | n/d |
| +20,00% | 0,09498 $ | 15/40 | +37,50% | -10,00% | 0,07123 $ | 0/15 | 0,00% | -25,00% | DEBOLE | 13,4 | n/d |
| +20,00% | 0,09498 $ | 15/40 | +37,50% | -15,00% | 0,06728 $ | 0/15 | 0,00% | -29,17% | DEBOLE | 13,4 | n/d |

---
