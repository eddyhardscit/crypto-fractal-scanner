# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-09-23 12:17:49 CEST**  
UTC: **2026-09-23 10:17:49 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 81.545 $ | 94.420 $ | +42,11% | +15,79% | rimbalzo debole | 94.420 $ | 81.545 $ | +6,90% | -13,64% | spike storicamente più resistente |
| SOL | 111,51 $ | 129,12 $ | +34,62% | +15,79% | rimbalzo poco frequente | 129,12 $ | 111,51 $ | +20,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,09470 $ | 0,10965 $ | +21,21% | +15,79% | rimbalzo poco frequente | 0,10965 $ | 0,09470 $ | +27,78% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 19 prima sono scesi a -5,00%. Tra quei 19, 8 poi sono rimbalzati fino a +10,00%. Percentuale: +42,11% (8/19). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 29 prima sono saliti a +10,00%. Tra quei 29, 2 poi sono scaricati a -5,00%. Percentuale: +6,90% (2/29). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 81.545 $ | 19/40 | +47,50% | +5,00% | 90.128 $ | 10/19 | +52,63% | +10,53% | MEDIA | 6,5 | 15,6 |
| -5,00% | 81.545 $ | 19/40 | +47,50% | +10,00% | 94.420 $ | 8/19 | +42,11% | +15,79% | BASSA | 6,5 | 15,4 |
| -5,00% | 81.545 $ | 19/40 | +47,50% | +15,00% | 98.712 $ | 5/19 | +26,32% | +21,05% | DEBOLE | 6,5 | 15,4 |
| -5,00% | 81.545 $ | 19/40 | +47,50% | +20,00% | 103.004 $ | 5/19 | +26,32% | +26,32% | DEBOLE | 6,5 | 15,8 |
| -8,00% | 78.970 $ | 17/40 | +42,50% | +5,00% | 90.128 $ | 8/17 | +47,06% | +14,13% | BASSA | 9,6 | 16,5 |
| -8,00% | 78.970 $ | 17/40 | +42,50% | +10,00% | 94.420 $ | 7/17 | +41,18% | +19,57% | BASSA | 9,6 | 15,9 |
| -8,00% | 78.970 $ | 17/40 | +42,50% | +15,00% | 98.712 $ | 4/17 | +23,53% | +25,00% | DEBOLE | 9,6 | 14,2 |
| -8,00% | 78.970 $ | 17/40 | +42,50% | +20,00% | 103.004 $ | 4/17 | +23,53% | +30,43% | DEBOLE | 9,6 | 14,5 |
| -10,00% | 77.253 $ | 13/40 | +32,50% | +5,00% | 90.128 $ | 5/13 | +38,46% | +16,67% | BASSA | 8,2 | 13,4 |
| -10,00% | 77.253 $ | 13/40 | +32,50% | +10,00% | 94.420 $ | 5/13 | +38,46% | +22,22% | BASSA | 8,2 | 13,8 |
| -10,00% | 77.253 $ | 13/40 | +32,50% | +15,00% | 98.712 $ | 3/13 | +23,08% | +27,78% | DEBOLE | 8,2 | 12,3 |
| -10,00% | 77.253 $ | 13/40 | +32,50% | +20,00% | 103.004 $ | 3/13 | +23,08% | +33,33% | DEBOLE | 8,2 | 12,7 |
| -15,00% | 72.961 $ | 10/40 | +25,00% | +5,00% | 90.128 $ | 3/10 | +30,00% | +23,53% | DEBOLE | 11,1 | 17,0 |
| -15,00% | 72.961 $ | 10/40 | +25,00% | +10,00% | 94.420 $ | 3/10 | +30,00% | +29,41% | DEBOLE | 11,1 | 17,7 |
| -15,00% | 72.961 $ | 10/40 | +25,00% | +15,00% | 98.712 $ | 1/10 | +10,00% | +35,29% | DEBOLE | 11,1 | 20,0 |
| -15,00% | 72.961 $ | 10/40 | +25,00% | +20,00% | 103.004 $ | 1/10 | +10,00% | +41,18% | DEBOLE | 11,1 | 20,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 90.128 $ | 34/40 | +85,00% | prezzo iniziale | 85.837 $ | 10/34 | +29,41% | -4,76% | DEBOLE | 5,2 | 10,8 |
| +5,00% | 90.128 $ | 34/40 | +85,00% | -5,00% | 81.545 $ | 7/34 | +20,59% | -9,52% | DEBOLE | 5,2 | 16,1 |
| +5,00% | 90.128 $ | 34/40 | +85,00% | -8,00% | 78.970 $ | 6/34 | +17,65% | -12,38% | DEBOLE | 5,2 | 18,3 |
| +5,00% | 90.128 $ | 34/40 | +85,00% | -10,00% | 77.253 $ | 3/34 | +8,82% | -14,29% | DEBOLE | 5,2 | 14,7 |
| +5,00% | 90.128 $ | 34/40 | +85,00% | -15,00% | 72.961 $ | 2/34 | +5,88% | -19,05% | DEBOLE | 5,2 | 20,5 |
| +10,00% | 94.420 $ | 29/40 | +72,50% | prezzo iniziale | 85.837 $ | 5/29 | +17,24% | -9,09% | DEBOLE | 7,8 | 13,2 |
| +10,00% | 94.420 $ | 29/40 | +72,50% | -5,00% | 81.545 $ | 2/29 | +6,90% | -13,64% | DEBOLE | 7,8 | 12,0 |
| +10,00% | 94.420 $ | 29/40 | +72,50% | -8,00% | 78.970 $ | 2/29 | +6,90% | -16,36% | DEBOLE | 7,8 | 12,0 |
| +10,00% | 94.420 $ | 29/40 | +72,50% | -10,00% | 77.253 $ | 1/29 | +3,45% | -18,18% | DEBOLE | 7,8 | 10,0 |
| +10,00% | 94.420 $ | 29/40 | +72,50% | -15,00% | 72.961 $ | 1/29 | +3,45% | -22,73% | DEBOLE | 7,8 | 22,0 |
| +15,00% | 98.712 $ | 25/40 | +62,50% | prezzo iniziale | 85.837 $ | 1/25 | +4,00% | -13,04% | DEBOLE | 8,9 | 13,0 |
| +15,00% | 98.712 $ | 25/40 | +62,50% | -5,00% | 81.545 $ | 0/25 | 0,00% | -17,39% | DEBOLE | 8,9 | n/d |
| +15,00% | 98.712 $ | 25/40 | +62,50% | -8,00% | 78.970 $ | 0/25 | 0,00% | -20,00% | DEBOLE | 8,9 | n/d |
| +15,00% | 98.712 $ | 25/40 | +62,50% | -10,00% | 77.253 $ | 0/25 | 0,00% | -21,74% | DEBOLE | 8,9 | n/d |
| +15,00% | 98.712 $ | 25/40 | +62,50% | -15,00% | 72.961 $ | 0/25 | 0,00% | -26,09% | DEBOLE | 8,9 | n/d |
| +20,00% | 103.004 $ | 23/40 | +57,50% | prezzo iniziale | 85.837 $ | 0/23 | 0,00% | -16,67% | DEBOLE | 11,3 | n/d |
| +20,00% | 103.004 $ | 23/40 | +57,50% | -5,00% | 81.545 $ | 0/23 | 0,00% | -20,83% | DEBOLE | 11,3 | n/d |
| +20,00% | 103.004 $ | 23/40 | +57,50% | -8,00% | 78.970 $ | 0/23 | 0,00% | -23,33% | DEBOLE | 11,3 | n/d |
| +20,00% | 103.004 $ | 23/40 | +57,50% | -10,00% | 77.253 $ | 0/23 | 0,00% | -25,00% | DEBOLE | 11,3 | n/d |
| +20,00% | 103.004 $ | 23/40 | +57,50% | -15,00% | 72.961 $ | 0/23 | 0,00% | -29,17% | DEBOLE | 11,3 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 26 prima sono scesi a -5,00%. Tra quei 26, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +34,62% (9/26). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 5 poi sono scaricati a -5,00%. Percentuale: +20,00% (5/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 111,51 $ | 26/40 | +65,00% | +5,00% | 123,25 $ | 10/26 | +38,46% | +10,53% | BASSA | 5,2 | 13,2 |
| -5,00% | 111,51 $ | 26/40 | +65,00% | +10,00% | 129,12 $ | 9/26 | +34,62% | +15,79% | DEBOLE | 5,2 | 14,0 |
| -5,00% | 111,51 $ | 26/40 | +65,00% | +15,00% | 134,99 $ | 6/26 | +23,08% | +21,05% | DEBOLE | 5,2 | 14,7 |
| -5,00% | 111,51 $ | 26/40 | +65,00% | +20,00% | 140,86 $ | 5/26 | +19,23% | +26,32% | DEBOLE | 5,2 | 14,6 |
| -8,00% | 107,99 $ | 23/40 | +57,50% | +5,00% | 123,25 $ | 7/23 | +30,43% | +14,13% | DEBOLE | 6,3 | 14,1 |
| -8,00% | 107,99 $ | 23/40 | +57,50% | +10,00% | 129,12 $ | 7/23 | +30,43% | +19,57% | DEBOLE | 6,3 | 15,6 |
| -8,00% | 107,99 $ | 23/40 | +57,50% | +15,00% | 134,99 $ | 4/23 | +17,39% | +25,00% | DEBOLE | 6,3 | 17,5 |
| -8,00% | 107,99 $ | 23/40 | +57,50% | +20,00% | 140,86 $ | 3/23 | +13,04% | +30,43% | DEBOLE | 6,3 | 16,7 |
| -10,00% | 105,64 $ | 22/40 | +55,00% | +5,00% | 123,25 $ | 6/22 | +27,27% | +16,67% | DEBOLE | 7,3 | 13,8 |
| -10,00% | 105,64 $ | 22/40 | +55,00% | +10,00% | 129,12 $ | 6/22 | +27,27% | +22,22% | DEBOLE | 7,3 | 15,0 |
| -10,00% | 105,64 $ | 22/40 | +55,00% | +15,00% | 134,99 $ | 3/22 | +13,64% | +27,78% | DEBOLE | 7,3 | 16,7 |
| -10,00% | 105,64 $ | 22/40 | +55,00% | +20,00% | 140,86 $ | 2/22 | +9,09% | +33,33% | DEBOLE | 7,3 | 15,0 |
| -15,00% | 99,77 $ | 20/40 | +50,00% | +5,00% | 123,25 $ | 3/20 | +15,00% | +23,53% | DEBOLE | 11,9 | 16,0 |
| -15,00% | 99,77 $ | 20/40 | +50,00% | +10,00% | 129,12 $ | 3/20 | +15,00% | +29,41% | DEBOLE | 11,9 | 16,3 |
| -15,00% | 99,77 $ | 20/40 | +50,00% | +15,00% | 134,99 $ | 1/20 | +5,00% | +35,29% | DEBOLE | 11,9 | 16,0 |
| -15,00% | 99,77 $ | 20/40 | +50,00% | +20,00% | 140,86 $ | 1/20 | +5,00% | +41,18% | DEBOLE | 11,9 | 20,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 123,25 $ | 27/40 | +67,50% | prezzo iniziale | 117,38 $ | 11/27 | +40,74% | -4,76% | BASSA | 4,6 | 9,2 |
| +5,00% | 123,25 $ | 27/40 | +67,50% | -5,00% | 111,51 $ | 8/27 | +29,63% | -9,52% | DEBOLE | 4,6 | 12,2 |
| +5,00% | 123,25 $ | 27/40 | +67,50% | -8,00% | 107,99 $ | 7/27 | +25,93% | -12,38% | DEBOLE | 4,6 | 11,9 |
| +5,00% | 123,25 $ | 27/40 | +67,50% | -10,00% | 105,64 $ | 7/27 | +25,93% | -14,29% | DEBOLE | 4,6 | 11,9 |
| +5,00% | 123,25 $ | 27/40 | +67,50% | -15,00% | 99,77 $ | 6/27 | +22,22% | -19,05% | DEBOLE | 4,6 | 21,0 |
| +10,00% | 129,12 $ | 25/40 | +62,50% | prezzo iniziale | 117,38 $ | 8/25 | +32,00% | -9,09% | DEBOLE | 7,2 | 13,6 |
| +10,00% | 129,12 $ | 25/40 | +62,50% | -5,00% | 111,51 $ | 5/25 | +20,00% | -13,64% | DEBOLE | 7,2 | 13,8 |
| +10,00% | 129,12 $ | 25/40 | +62,50% | -8,00% | 107,99 $ | 4/25 | +16,00% | -16,36% | DEBOLE | 7,2 | 12,5 |
| +10,00% | 129,12 $ | 25/40 | +62,50% | -10,00% | 105,64 $ | 4/25 | +16,00% | -18,18% | DEBOLE | 7,2 | 12,5 |
| +10,00% | 129,12 $ | 25/40 | +62,50% | -15,00% | 99,77 $ | 4/25 | +16,00% | -22,73% | DEBOLE | 7,2 | 20,0 |
| +15,00% | 134,99 $ | 20/40 | +50,00% | prezzo iniziale | 117,38 $ | 2/20 | +10,00% | -13,04% | DEBOLE | 7,3 | 19,0 |
| +15,00% | 134,99 $ | 20/40 | +50,00% | -5,00% | 111,51 $ | 1/20 | +5,00% | -17,39% | DEBOLE | 7,3 | 22,0 |
| +15,00% | 134,99 $ | 20/40 | +50,00% | -8,00% | 107,99 $ | 0/20 | 0,00% | -20,00% | DEBOLE | 7,3 | n/d |
| +15,00% | 134,99 $ | 20/40 | +50,00% | -10,00% | 105,64 $ | 0/20 | 0,00% | -21,74% | DEBOLE | 7,3 | n/d |
| +15,00% | 134,99 $ | 20/40 | +50,00% | -15,00% | 99,77 $ | 0/20 | 0,00% | -26,09% | DEBOLE | 7,3 | n/d |
| +20,00% | 140,86 $ | 19/40 | +47,50% | prezzo iniziale | 117,38 $ | 2/19 | +10,53% | -16,67% | DEBOLE | 8,9 | 19,0 |
| +20,00% | 140,86 $ | 19/40 | +47,50% | -5,00% | 111,51 $ | 1/19 | +5,26% | -20,83% | DEBOLE | 8,9 | 22,0 |
| +20,00% | 140,86 $ | 19/40 | +47,50% | -8,00% | 107,99 $ | 0/19 | 0,00% | -23,33% | DEBOLE | 8,9 | n/d |
| +20,00% | 140,86 $ | 19/40 | +47,50% | -10,00% | 105,64 $ | 0/19 | 0,00% | -25,00% | DEBOLE | 8,9 | n/d |
| +20,00% | 140,86 $ | 19/40 | +47,50% | -15,00% | 99,77 $ | 0/19 | 0,00% | -29,17% | DEBOLE | 8,9 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 33 prima sono scesi a -5,00%. Tra quei 33, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +21,21% (7/33). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 18 prima sono saliti a +10,00%. Tra quei 18, 5 poi sono scaricati a -5,00%. Percentuale: +27,78% (5/18). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,09470 $ | 33/40 | +82,50% | +5,00% | 0,10466 $ | 10/33 | +30,30% | +10,53% | DEBOLE | 6,2 | 12,5 |
| -5,00% | 0,09470 $ | 33/40 | +82,50% | +10,00% | 0,10965 $ | 7/33 | +21,21% | +15,79% | DEBOLE | 6,2 | 15,7 |
| -5,00% | 0,09470 $ | 33/40 | +82,50% | +15,00% | 0,11463 $ | 5/33 | +15,15% | +21,05% | DEBOLE | 6,2 | 16,8 |
| -5,00% | 0,09470 $ | 33/40 | +82,50% | +20,00% | 0,11962 $ | 3/33 | +9,09% | +26,32% | DEBOLE | 6,2 | 12,3 |
| -8,00% | 0,09171 $ | 31/40 | +77,50% | +5,00% | 0,10466 $ | 6/31 | +19,35% | +14,13% | DEBOLE | 8,6 | 14,2 |
| -8,00% | 0,09171 $ | 31/40 | +77,50% | +10,00% | 0,10965 $ | 6/31 | +19,35% | +19,57% | DEBOLE | 8,6 | 15,0 |
| -8,00% | 0,09171 $ | 31/40 | +77,50% | +15,00% | 0,11463 $ | 4/31 | +12,90% | +25,00% | DEBOLE | 8,6 | 15,8 |
| -8,00% | 0,09171 $ | 31/40 | +77,50% | +20,00% | 0,11962 $ | 3/31 | +9,68% | +30,43% | DEBOLE | 8,6 | 12,3 |
| -10,00% | 0,08971 $ | 30/40 | +75,00% | +5,00% | 0,10466 $ | 5/30 | +16,67% | +16,67% | DEBOLE | 9,6 | 14,8 |
| -10,00% | 0,08971 $ | 30/40 | +75,00% | +10,00% | 0,10965 $ | 5/30 | +16,67% | +22,22% | DEBOLE | 9,6 | 15,4 |
| -10,00% | 0,08971 $ | 30/40 | +75,00% | +15,00% | 0,11463 $ | 3/30 | +10,00% | +27,78% | DEBOLE | 9,6 | 16,7 |
| -10,00% | 0,08971 $ | 30/40 | +75,00% | +20,00% | 0,11962 $ | 2/30 | +6,67% | +33,33% | DEBOLE | 9,6 | 10,0 |
| -15,00% | 0,08473 $ | 27/40 | +67,50% | +5,00% | 0,10466 $ | 2/27 | +7,41% | +23,53% | DEBOLE | 12,6 | 14,5 |
| -15,00% | 0,08473 $ | 27/40 | +67,50% | +10,00% | 0,10965 $ | 2/27 | +7,41% | +29,41% | DEBOLE | 12,6 | 15,5 |
| -15,00% | 0,08473 $ | 27/40 | +67,50% | +15,00% | 0,11463 $ | 0/27 | 0,00% | +35,29% | DEBOLE | 12,6 | n/d |
| -15,00% | 0,08473 $ | 27/40 | +67,50% | +20,00% | 0,11962 $ | 0/27 | 0,00% | +41,18% | DEBOLE | 12,6 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,10466 $ | 26/40 | +65,00% | prezzo iniziale | 0,09968 $ | 20/26 | +76,92% | -4,76% | ALTA | 3,9 | 9,6 |
| +5,00% | 0,10466 $ | 26/40 | +65,00% | -5,00% | 0,09470 $ | 16/26 | +61,54% | -9,52% | MEDIA | 3,9 | 10,9 |
| +5,00% | 0,10466 $ | 26/40 | +65,00% | -8,00% | 0,09171 $ | 15/26 | +57,69% | -12,38% | MEDIA | 3,9 | 12,4 |
| +5,00% | 0,10466 $ | 26/40 | +65,00% | -10,00% | 0,08971 $ | 15/26 | +57,69% | -14,29% | MEDIA | 3,9 | 13,3 |
| +5,00% | 0,10466 $ | 26/40 | +65,00% | -15,00% | 0,08473 $ | 14/26 | +53,85% | -19,05% | MEDIA | 3,9 | 17,1 |
| +10,00% | 0,10965 $ | 18/40 | +45,00% | prezzo iniziale | 0,09968 $ | 9/18 | +50,00% | -9,09% | MEDIA | 7,8 | 13,8 |
| +10,00% | 0,10965 $ | 18/40 | +45,00% | -5,00% | 0,09470 $ | 5/18 | +27,78% | -13,64% | DEBOLE | 7,8 | 14,0 |
| +10,00% | 0,10965 $ | 18/40 | +45,00% | -8,00% | 0,09171 $ | 5/18 | +27,78% | -16,36% | DEBOLE | 7,8 | 15,0 |
| +10,00% | 0,10965 $ | 18/40 | +45,00% | -10,00% | 0,08971 $ | 5/18 | +27,78% | -18,18% | DEBOLE | 7,8 | 16,2 |
| +10,00% | 0,10965 $ | 18/40 | +45,00% | -15,00% | 0,08473 $ | 5/18 | +27,78% | -22,73% | DEBOLE | 7,8 | 20,2 |
| +15,00% | 0,11463 $ | 14/40 | +35,00% | prezzo iniziale | 0,09968 $ | 5/14 | +35,71% | -13,04% | BASSA | 9,5 | 19,8 |
| +15,00% | 0,11463 $ | 14/40 | +35,00% | -5,00% | 0,09470 $ | 2/14 | +14,29% | -17,39% | DEBOLE | 9,5 | 18,5 |
| +15,00% | 0,11463 $ | 14/40 | +35,00% | -8,00% | 0,09171 $ | 2/14 | +14,29% | -20,00% | DEBOLE | 9,5 | 19,0 |
| +15,00% | 0,11463 $ | 14/40 | +35,00% | -10,00% | 0,08971 $ | 2/14 | +14,29% | -21,74% | DEBOLE | 9,5 | 21,0 |
| +15,00% | 0,11463 $ | 14/40 | +35,00% | -15,00% | 0,08473 $ | 2/14 | +14,29% | -26,09% | DEBOLE | 9,5 | 21,5 |
| +20,00% | 0,11962 $ | 12/40 | +30,00% | prezzo iniziale | 0,09968 $ | 4/12 | +33,33% | -16,67% | DEBOLE | 9,2 | 17,2 |
| +20,00% | 0,11962 $ | 12/40 | +30,00% | -5,00% | 0,09470 $ | 2/12 | +16,67% | -20,83% | DEBOLE | 9,2 | 18,5 |
| +20,00% | 0,11962 $ | 12/40 | +30,00% | -8,00% | 0,09171 $ | 2/12 | +16,67% | -23,33% | DEBOLE | 9,2 | 19,0 |
| +20,00% | 0,11962 $ | 12/40 | +30,00% | -10,00% | 0,08971 $ | 2/12 | +16,67% | -25,00% | DEBOLE | 9,2 | 21,0 |
| +20,00% | 0,11962 $ | 12/40 | +30,00% | -15,00% | 0,08473 $ | 2/12 | +16,67% | -29,17% | DEBOLE | 9,2 | 21,5 |

---
