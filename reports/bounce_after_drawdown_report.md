# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-08-16 07:33:46 CEST**  
UTC: **2026-08-16 05:33:46 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 59.850 $ | 69.300 $ | +46,67% | +15,79% | rimbalzo debole | 69.300 $ | 59.850 $ | +7,14% | -13,64% | spike storicamente più resistente |
| SOL | 71,54 $ | 82,84 $ | +28,57% | +15,79% | rimbalzo poco frequente | 82,84 $ | 71,54 $ | 0,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06616 $ | 0,07660 $ | +62,07% | +15,79% | rimbalzo possibile | 0,07660 $ | 0,06616 $ | +25,00% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 15 prima sono scesi a -5,00%. Tra quei 15, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +46,67% (7/15). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 2 poi sono scaricati a -5,00%. Percentuale: +7,14% (2/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 59.850 $ | 15/40 | +37,50% | +5,00% | 66.150 $ | 10/15 | +66,67% | +10,53% | ALTA | 8,0 | 18,1 |
| -5,00% | 59.850 $ | 15/40 | +37,50% | +10,00% | 69.300 $ | 7/15 | +46,67% | +15,79% | BASSA | 8,0 | 18,3 |
| -5,00% | 59.850 $ | 15/40 | +37,50% | +15,00% | 72.450 $ | 6/15 | +40,00% | +21,05% | BASSA | 8,0 | 19,0 |
| -5,00% | 59.850 $ | 15/40 | +37,50% | +20,00% | 75.600 $ | 4/15 | +26,67% | +26,32% | DEBOLE | 8,0 | 18,8 |
| -8,00% | 57.960 $ | 9/40 | +22,50% | +5,00% | 66.150 $ | 5/9 | +55,56% | +14,13% | MEDIA | 8,1 | 20,8 |
| -8,00% | 57.960 $ | 9/40 | +22,50% | +10,00% | 69.300 $ | 4/9 | +44,44% | +19,57% | BASSA | 8,1 | 19,8 |
| -8,00% | 57.960 $ | 9/40 | +22,50% | +15,00% | 72.450 $ | 3/9 | +33,33% | +25,00% | DEBOLE | 8,1 | 20,7 |
| -8,00% | 57.960 $ | 9/40 | +22,50% | +20,00% | 75.600 $ | 2/9 | +22,22% | +30,43% | DEBOLE | 8,1 | 17,0 |
| -10,00% | 56.700 $ | 9/40 | +22,50% | +5,00% | 66.150 $ | 5/9 | +55,56% | +16,67% | MEDIA | 10,8 | 20,8 |
| -10,00% | 56.700 $ | 9/40 | +22,50% | +10,00% | 69.300 $ | 4/9 | +44,44% | +22,22% | BASSA | 10,8 | 19,8 |
| -10,00% | 56.700 $ | 9/40 | +22,50% | +15,00% | 72.450 $ | 3/9 | +33,33% | +27,78% | DEBOLE | 10,8 | 20,7 |
| -10,00% | 56.700 $ | 9/40 | +22,50% | +20,00% | 75.600 $ | 2/9 | +22,22% | +33,33% | DEBOLE | 10,8 | 17,0 |
| -15,00% | 53.550 $ | 6/40 | +15,00% | +5,00% | 66.150 $ | 2/6 | +33,33% | +23,53% | DEBOLE | 14,3 | 24,5 |
| -15,00% | 53.550 $ | 6/40 | +15,00% | +10,00% | 69.300 $ | 2/6 | +33,33% | +29,41% | DEBOLE | 14,3 | 25,0 |
| -15,00% | 53.550 $ | 6/40 | +15,00% | +15,00% | 72.450 $ | 1/6 | +16,67% | +35,29% | DEBOLE | 14,3 | 29,0 |
| -15,00% | 53.550 $ | 6/40 | +15,00% | +20,00% | 75.600 $ | 0/6 | 0,00% | +41,18% | DEBOLE | 14,3 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 66.150 $ | 37/40 | +92,50% | prezzo iniziale | 63.000 $ | 14/37 | +37,84% | -4,76% | BASSA | 8,6 | 20,6 |
| +5,00% | 66.150 $ | 37/40 | +92,50% | -5,00% | 59.850 $ | 6/37 | +16,22% | -9,52% | DEBOLE | 8,6 | 18,2 |
| +5,00% | 66.150 $ | 37/40 | +92,50% | -8,00% | 57.960 $ | 5/37 | +13,51% | -12,38% | DEBOLE | 8,6 | 16,2 |
| +5,00% | 66.150 $ | 37/40 | +92,50% | -10,00% | 56.700 $ | 4/37 | +10,81% | -14,29% | DEBOLE | 8,6 | 16,5 |
| +5,00% | 66.150 $ | 37/40 | +92,50% | -15,00% | 53.550 $ | 3/37 | +8,11% | -19,05% | DEBOLE | 8,6 | 20,0 |
| +10,00% | 69.300 $ | 28/40 | +70,00% | prezzo iniziale | 63.000 $ | 4/28 | +14,29% | -9,09% | DEBOLE | 13,1 | 27,2 |
| +10,00% | 69.300 $ | 28/40 | +70,00% | -5,00% | 59.850 $ | 2/28 | +7,14% | -13,64% | DEBOLE | 13,1 | 28,5 |
| +10,00% | 69.300 $ | 28/40 | +70,00% | -8,00% | 57.960 $ | 1/28 | +3,57% | -16,36% | DEBOLE | 13,1 | 28,0 |
| +10,00% | 69.300 $ | 28/40 | +70,00% | -10,00% | 56.700 $ | 0/28 | 0,00% | -18,18% | DEBOLE | 13,1 | n/d |
| +10,00% | 69.300 $ | 28/40 | +70,00% | -15,00% | 53.550 $ | 0/28 | 0,00% | -22,73% | DEBOLE | 13,1 | n/d |
| +15,00% | 72.450 $ | 22/40 | +55,00% | prezzo iniziale | 63.000 $ | 2/22 | +9,09% | -13,04% | DEBOLE | 13,2 | 28,0 |
| +15,00% | 72.450 $ | 22/40 | +55,00% | -5,00% | 59.850 $ | 1/22 | +4,55% | -17,39% | DEBOLE | 13,2 | 27,0 |
| +15,00% | 72.450 $ | 22/40 | +55,00% | -8,00% | 57.960 $ | 1/22 | +4,55% | -20,00% | DEBOLE | 13,2 | 28,0 |
| +15,00% | 72.450 $ | 22/40 | +55,00% | -10,00% | 56.700 $ | 0/22 | 0,00% | -21,74% | DEBOLE | 13,2 | n/d |
| +15,00% | 72.450 $ | 22/40 | +55,00% | -15,00% | 53.550 $ | 0/22 | 0,00% | -26,09% | DEBOLE | 13,2 | n/d |
| +20,00% | 75.600 $ | 17/40 | +42,50% | prezzo iniziale | 63.000 $ | 1/17 | +5,88% | -16,67% | DEBOLE | 12,2 | 27,0 |
| +20,00% | 75.600 $ | 17/40 | +42,50% | -5,00% | 59.850 $ | 1/17 | +5,88% | -20,83% | DEBOLE | 12,2 | 27,0 |
| +20,00% | 75.600 $ | 17/40 | +42,50% | -8,00% | 57.960 $ | 1/17 | +5,88% | -23,33% | DEBOLE | 12,2 | 28,0 |
| +20,00% | 75.600 $ | 17/40 | +42,50% | -10,00% | 56.700 $ | 0/17 | 0,00% | -25,00% | DEBOLE | 12,2 | n/d |
| +20,00% | 75.600 $ | 17/40 | +42,50% | -15,00% | 53.550 $ | 0/17 | 0,00% | -29,17% | DEBOLE | 12,2 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 14 prima sono scesi a -5,00%. Tra quei 14, 4 poi sono rimbalzati fino a +10,00%. Percentuale: +28,57% (4/14). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 27 prima sono saliti a +10,00%. Tra quei 27, 0 poi sono scaricati a -5,00%. Percentuale: 0,00% (0/27). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 71,54 $ | 14/40 | +35,00% | +5,00% | 79,08 $ | 8/14 | +57,14% | +10,53% | MEDIA | 8,0 | 17,4 |
| -5,00% | 71,54 $ | 14/40 | +35,00% | +10,00% | 82,84 $ | 4/14 | +28,57% | +15,79% | DEBOLE | 8,0 | 15,5 |
| -5,00% | 71,54 $ | 14/40 | +35,00% | +15,00% | 86,61 $ | 3/14 | +21,43% | +21,05% | DEBOLE | 8,0 | 17,7 |
| -5,00% | 71,54 $ | 14/40 | +35,00% | +20,00% | 90,37 $ | 2/14 | +14,29% | +26,32% | DEBOLE | 8,0 | 21,5 |
| -8,00% | 69,29 $ | 7/40 | +17,50% | +5,00% | 79,08 $ | 2/7 | +28,57% | +14,13% | DEBOLE | 12,3 | 18,0 |
| -8,00% | 69,29 $ | 7/40 | +17,50% | +10,00% | 82,84 $ | 1/7 | +14,29% | +19,57% | DEBOLE | 12,3 | 17,0 |
| -8,00% | 69,29 $ | 7/40 | +17,50% | +15,00% | 86,61 $ | 1/7 | +14,29% | +25,00% | DEBOLE | 12,3 | 18,0 |
| -8,00% | 69,29 $ | 7/40 | +17,50% | +20,00% | 90,37 $ | 1/7 | +14,29% | +30,43% | DEBOLE | 12,3 | 18,0 |
| -10,00% | 67,78 $ | 6/40 | +15,00% | +5,00% | 79,08 $ | 2/6 | +33,33% | +16,67% | DEBOLE | 12,2 | 18,0 |
| -10,00% | 67,78 $ | 6/40 | +15,00% | +10,00% | 82,84 $ | 1/6 | +16,67% | +22,22% | DEBOLE | 12,2 | 17,0 |
| -10,00% | 67,78 $ | 6/40 | +15,00% | +15,00% | 86,61 $ | 1/6 | +16,67% | +27,78% | DEBOLE | 12,2 | 18,0 |
| -10,00% | 67,78 $ | 6/40 | +15,00% | +20,00% | 90,37 $ | 1/6 | +16,67% | +33,33% | DEBOLE | 12,2 | 18,0 |
| -15,00% | 64,01 $ | 3/40 | +7,50% | +5,00% | 79,08 $ | 0/3 | 0,00% | +23,53% | DEBOLE | 16,3 | n/d |
| -15,00% | 64,01 $ | 3/40 | +7,50% | +10,00% | 82,84 $ | 0/3 | 0,00% | +29,41% | DEBOLE | 16,3 | n/d |
| -15,00% | 64,01 $ | 3/40 | +7,50% | +15,00% | 86,61 $ | 0/3 | 0,00% | +35,29% | DEBOLE | 16,3 | n/d |
| -15,00% | 64,01 $ | 3/40 | +7,50% | +20,00% | 90,37 $ | 0/3 | 0,00% | +41,18% | DEBOLE | 16,3 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 79,08 $ | 36/40 | +90,00% | prezzo iniziale | 75,31 $ | 9/36 | +25,00% | -4,76% | DEBOLE | 7,3 | 19,3 |
| +5,00% | 79,08 $ | 36/40 | +90,00% | -5,00% | 71,54 $ | 3/36 | +8,33% | -9,52% | DEBOLE | 7,3 | 20,0 |
| +5,00% | 79,08 $ | 36/40 | +90,00% | -8,00% | 69,29 $ | 1/36 | +2,78% | -12,38% | DEBOLE | 7,3 | 19,0 |
| +5,00% | 79,08 $ | 36/40 | +90,00% | -10,00% | 67,78 $ | 1/36 | +2,78% | -14,29% | DEBOLE | 7,3 | 20,0 |
| +5,00% | 79,08 $ | 36/40 | +90,00% | -15,00% | 64,01 $ | 1/36 | +2,78% | -19,05% | DEBOLE | 7,3 | 23,0 |
| +10,00% | 82,84 $ | 27/40 | +67,50% | prezzo iniziale | 75,31 $ | 3/27 | +11,11% | -9,09% | DEBOLE | 8,0 | 22,3 |
| +10,00% | 82,84 $ | 27/40 | +67,50% | -5,00% | 71,54 $ | 0/27 | 0,00% | -13,64% | DEBOLE | 8,0 | n/d |
| +10,00% | 82,84 $ | 27/40 | +67,50% | -8,00% | 69,29 $ | 0/27 | 0,00% | -16,36% | DEBOLE | 8,0 | n/d |
| +10,00% | 82,84 $ | 27/40 | +67,50% | -10,00% | 67,78 $ | 0/27 | 0,00% | -18,18% | DEBOLE | 8,0 | n/d |
| +10,00% | 82,84 $ | 27/40 | +67,50% | -15,00% | 64,01 $ | 0/27 | 0,00% | -22,73% | DEBOLE | 8,0 | n/d |
| +15,00% | 86,61 $ | 22/40 | +55,00% | prezzo iniziale | 75,31 $ | 1/22 | +4,55% | -13,04% | DEBOLE | 9,9 | 25,0 |
| +15,00% | 86,61 $ | 22/40 | +55,00% | -5,00% | 71,54 $ | 0/22 | 0,00% | -17,39% | DEBOLE | 9,9 | n/d |
| +15,00% | 86,61 $ | 22/40 | +55,00% | -8,00% | 69,29 $ | 0/22 | 0,00% | -20,00% | DEBOLE | 9,9 | n/d |
| +15,00% | 86,61 $ | 22/40 | +55,00% | -10,00% | 67,78 $ | 0/22 | 0,00% | -21,74% | DEBOLE | 9,9 | n/d |
| +15,00% | 86,61 $ | 22/40 | +55,00% | -15,00% | 64,01 $ | 0/22 | 0,00% | -26,09% | DEBOLE | 9,9 | n/d |
| +20,00% | 90,37 $ | 19/40 | +47,50% | prezzo iniziale | 75,31 $ | 1/19 | +5,26% | -16,67% | DEBOLE | 11,9 | 25,0 |
| +20,00% | 90,37 $ | 19/40 | +47,50% | -5,00% | 71,54 $ | 0/19 | 0,00% | -20,83% | DEBOLE | 11,9 | n/d |
| +20,00% | 90,37 $ | 19/40 | +47,50% | -8,00% | 69,29 $ | 0/19 | 0,00% | -23,33% | DEBOLE | 11,9 | n/d |
| +20,00% | 90,37 $ | 19/40 | +47,50% | -10,00% | 67,78 $ | 0/19 | 0,00% | -25,00% | DEBOLE | 11,9 | n/d |
| +20,00% | 90,37 $ | 19/40 | +47,50% | -15,00% | 64,01 $ | 0/19 | 0,00% | -29,17% | DEBOLE | 11,9 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 29 prima sono scesi a -5,00%. Tra quei 29, 18 poi sono rimbalzati fino a +10,00%. Percentuale: +62,07% (18/29). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.
- DOGE: su 40 casi simili, 32 prima sono saliti a +10,00%. Tra quei 32, 8 poi sono scaricati a -5,00%. Percentuale: +25,00% (8/32). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06616 $ | 29/40 | +72,50% | +5,00% | 0,07312 $ | 18/29 | +62,07% | +10,53% | MEDIA | 7,9 | 12,6 |
| -5,00% | 0,06616 $ | 29/40 | +72,50% | +10,00% | 0,07660 $ | 18/29 | +62,07% | +15,79% | MEDIA | 7,9 | 15,3 |
| -5,00% | 0,06616 $ | 29/40 | +72,50% | +15,00% | 0,08009 $ | 15/29 | +51,72% | +21,05% | MEDIA | 7,9 | 18,8 |
| -5,00% | 0,06616 $ | 29/40 | +72,50% | +20,00% | 0,08357 $ | 13/29 | +44,83% | +26,32% | BASSA | 7,9 | 20,3 |
| -8,00% | 0,06407 $ | 23/40 | +57,50% | +5,00% | 0,07312 $ | 13/23 | +56,52% | +14,13% | MEDIA | 8,3 | 13,2 |
| -8,00% | 0,06407 $ | 23/40 | +57,50% | +10,00% | 0,07660 $ | 13/23 | +56,52% | +19,57% | MEDIA | 8,3 | 15,8 |
| -8,00% | 0,06407 $ | 23/40 | +57,50% | +15,00% | 0,08009 $ | 10/23 | +43,48% | +25,00% | BASSA | 8,3 | 19,5 |
| -8,00% | 0,06407 $ | 23/40 | +57,50% | +20,00% | 0,08357 $ | 9/23 | +39,13% | +30,43% | BASSA | 8,3 | 21,7 |
| -10,00% | 0,06268 $ | 18/40 | +45,00% | +5,00% | 0,07312 $ | 8/18 | +44,44% | +16,67% | BASSA | 9,0 | 13,6 |
| -10,00% | 0,06268 $ | 18/40 | +45,00% | +10,00% | 0,07660 $ | 8/18 | +44,44% | +22,22% | BASSA | 9,0 | 16,4 |
| -10,00% | 0,06268 $ | 18/40 | +45,00% | +15,00% | 0,08009 $ | 6/18 | +33,33% | +27,78% | DEBOLE | 9,0 | 17,5 |
| -10,00% | 0,06268 $ | 18/40 | +45,00% | +20,00% | 0,08357 $ | 6/18 | +33,33% | +33,33% | DEBOLE | 9,0 | 20,8 |
| -15,00% | 0,05919 $ | 10/40 | +25,00% | +5,00% | 0,07312 $ | 1/10 | +10,00% | +23,53% | DEBOLE | 11,7 | 9,0 |
| -15,00% | 0,05919 $ | 10/40 | +25,00% | +10,00% | 0,07660 $ | 1/10 | +10,00% | +29,41% | DEBOLE | 11,7 | 10,0 |
| -15,00% | 0,05919 $ | 10/40 | +25,00% | +15,00% | 0,08009 $ | 1/10 | +10,00% | +35,29% | DEBOLE | 11,7 | 10,0 |
| -15,00% | 0,05919 $ | 10/40 | +25,00% | +20,00% | 0,08357 $ | 1/10 | +10,00% | +41,18% | DEBOLE | 11,7 | 27,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07312 $ | 34/40 | +85,00% | prezzo iniziale | 0,06964 $ | 24/34 | +70,59% | -4,76% | ALTA | 6,1 | 13,7 |
| +5,00% | 0,07312 $ | 34/40 | +85,00% | -5,00% | 0,06616 $ | 16/34 | +47,06% | -9,52% | BASSA | 6,1 | 14,4 |
| +5,00% | 0,07312 $ | 34/40 | +85,00% | -8,00% | 0,06407 $ | 11/34 | +32,35% | -12,38% | DEBOLE | 6,1 | 13,5 |
| +5,00% | 0,07312 $ | 34/40 | +85,00% | -10,00% | 0,06268 $ | 8/34 | +23,53% | -14,29% | DEBOLE | 6,1 | 14,5 |
| +5,00% | 0,07312 $ | 34/40 | +85,00% | -15,00% | 0,05919 $ | 3/34 | +8,82% | -19,05% | DEBOLE | 6,1 | 24,3 |
| +10,00% | 0,07660 $ | 32/40 | +80,00% | prezzo iniziale | 0,06964 $ | 16/32 | +50,00% | -9,09% | MEDIA | 10,4 | 17,9 |
| +10,00% | 0,07660 $ | 32/40 | +80,00% | -5,00% | 0,06616 $ | 8/32 | +25,00% | -13,64% | DEBOLE | 10,4 | 18,1 |
| +10,00% | 0,07660 $ | 32/40 | +80,00% | -8,00% | 0,06407 $ | 4/32 | +12,50% | -16,36% | DEBOLE | 10,4 | 16,2 |
| +10,00% | 0,07660 $ | 32/40 | +80,00% | -10,00% | 0,06268 $ | 2/32 | +6,25% | -18,18% | DEBOLE | 10,4 | 19,5 |
| +10,00% | 0,07660 $ | 32/40 | +80,00% | -15,00% | 0,05919 $ | 1/32 | +3,12% | -22,73% | DEBOLE | 10,4 | 25,0 |
| +15,00% | 0,08009 $ | 26/40 | +65,00% | prezzo iniziale | 0,06964 $ | 4/26 | +15,38% | -13,04% | DEBOLE | 15,1 | 19,2 |
| +15,00% | 0,08009 $ | 26/40 | +65,00% | -5,00% | 0,06616 $ | 2/26 | +7,69% | -17,39% | DEBOLE | 15,1 | 17,0 |
| +15,00% | 0,08009 $ | 26/40 | +65,00% | -8,00% | 0,06407 $ | 1/26 | +3,85% | -20,00% | DEBOLE | 15,1 | 27,0 |
| +15,00% | 0,08009 $ | 26/40 | +65,00% | -10,00% | 0,06268 $ | 1/26 | +3,85% | -21,74% | DEBOLE | 15,1 | 28,0 |
| +15,00% | 0,08009 $ | 26/40 | +65,00% | -15,00% | 0,05919 $ | 0/26 | 0,00% | -26,09% | DEBOLE | 15,1 | n/d |
| +20,00% | 0,08357 $ | 23/40 | +57,50% | prezzo iniziale | 0,06964 $ | 1/23 | +4,35% | -16,67% | DEBOLE | 18,1 | 30,0 |
| +20,00% | 0,08357 $ | 23/40 | +57,50% | -5,00% | 0,06616 $ | 0/23 | 0,00% | -20,83% | DEBOLE | 18,1 | n/d |
| +20,00% | 0,08357 $ | 23/40 | +57,50% | -8,00% | 0,06407 $ | 0/23 | 0,00% | -23,33% | DEBOLE | 18,1 | n/d |
| +20,00% | 0,08357 $ | 23/40 | +57,50% | -10,00% | 0,06268 $ | 0/23 | 0,00% | -25,00% | DEBOLE | 18,1 | n/d |
| +20,00% | 0,08357 $ | 23/40 | +57,50% | -15,00% | 0,05919 $ | 0/23 | 0,00% | -29,17% | DEBOLE | 18,1 | n/d |

---
