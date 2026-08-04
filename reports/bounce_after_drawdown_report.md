# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-08-04 07:16:17 CEST**  
UTC: **2026-08-04 05:16:17 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 60.654 $ | 70.230 $ | +33,33% | +15,79% | rimbalzo poco frequente | 70.230 $ | 60.654 $ | +3,70% | -13,64% | spike storicamente più resistente |
| SOL | 70,03 $ | 81,09 $ | +23,53% | +15,79% | rimbalzo poco frequente | 81,09 $ | 70,03 $ | 0,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06668 $ | 0,07721 $ | +39,39% | +15,79% | rimbalzo debole | 0,07721 $ | 0,06668 $ | +21,74% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 18 prima sono scesi a -5,00%. Tra quei 18, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +33,33% (6/18). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- BTC: su 40 casi simili, 27 prima sono saliti a +10,00%. Tra quei 27, 1 poi sono scaricati a -5,00%. Percentuale: +3,70% (1/27). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 60.654 $ | 18/40 | +45,00% | +5,00% | 67.038 $ | 9/18 | +50,00% | +10,53% | MEDIA | 6,6 | 16,6 |
| -5,00% | 60.654 $ | 18/40 | +45,00% | +10,00% | 70.230 $ | 6/18 | +33,33% | +15,79% | DEBOLE | 6,6 | 19,8 |
| -5,00% | 60.654 $ | 18/40 | +45,00% | +15,00% | 73.423 $ | 5/18 | +27,78% | +21,05% | DEBOLE | 6,6 | 19,6 |
| -5,00% | 60.654 $ | 18/40 | +45,00% | +20,00% | 76.615 $ | 5/18 | +27,78% | +26,32% | DEBOLE | 6,6 | 20,2 |
| -8,00% | 58.738 $ | 15/40 | +37,50% | +5,00% | 67.038 $ | 5/15 | +33,33% | +14,13% | DEBOLE | 9,0 | 22,0 |
| -8,00% | 58.738 $ | 15/40 | +37,50% | +10,00% | 70.230 $ | 3/15 | +20,00% | +19,57% | DEBOLE | 9,0 | 25,7 |
| -8,00% | 58.738 $ | 15/40 | +37,50% | +15,00% | 73.423 $ | 2/15 | +13,33% | +25,00% | DEBOLE | 9,0 | 26,5 |
| -8,00% | 58.738 $ | 15/40 | +37,50% | +20,00% | 76.615 $ | 2/15 | +13,33% | +30,43% | DEBOLE | 9,0 | 27,5 |
| -10,00% | 57.461 $ | 13/40 | +32,50% | +5,00% | 67.038 $ | 3/13 | +23,08% | +16,67% | DEBOLE | 10,2 | 20,0 |
| -10,00% | 57.461 $ | 13/40 | +32,50% | +10,00% | 70.230 $ | 2/13 | +15,38% | +22,22% | DEBOLE | 10,2 | 25,0 |
| -10,00% | 57.461 $ | 13/40 | +32,50% | +15,00% | 73.423 $ | 1/13 | +7,69% | +27,78% | DEBOLE | 10,2 | 25,0 |
| -10,00% | 57.461 $ | 13/40 | +32,50% | +20,00% | 76.615 $ | 1/13 | +7,69% | +33,33% | DEBOLE | 10,2 | 25,0 |
| -15,00% | 54.269 $ | 6/40 | +15,00% | +5,00% | 67.038 $ | 0/6 | 0,00% | +23,53% | DEBOLE | 9,7 | n/d |
| -15,00% | 54.269 $ | 6/40 | +15,00% | +10,00% | 70.230 $ | 0/6 | 0,00% | +29,41% | DEBOLE | 9,7 | n/d |
| -15,00% | 54.269 $ | 6/40 | +15,00% | +15,00% | 73.423 $ | 0/6 | 0,00% | +35,29% | DEBOLE | 9,7 | n/d |
| -15,00% | 54.269 $ | 6/40 | +15,00% | +20,00% | 76.615 $ | 0/6 | 0,00% | +41,18% | DEBOLE | 9,7 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 67.038 $ | 33/40 | +82,50% | prezzo iniziale | 63.846 $ | 7/33 | +21,21% | -4,76% | DEBOLE | 8,4 | 9,0 |
| +5,00% | 67.038 $ | 33/40 | +82,50% | -5,00% | 60.654 $ | 5/33 | +15,15% | -9,52% | DEBOLE | 8,4 | 12,4 |
| +5,00% | 67.038 $ | 33/40 | +82,50% | -8,00% | 58.738 $ | 4/33 | +12,12% | -12,38% | DEBOLE | 8,4 | 14,0 |
| +5,00% | 67.038 $ | 33/40 | +82,50% | -10,00% | 57.461 $ | 4/33 | +12,12% | -14,29% | DEBOLE | 8,4 | 15,0 |
| +5,00% | 67.038 $ | 33/40 | +82,50% | -15,00% | 54.269 $ | 2/33 | +6,06% | -19,05% | DEBOLE | 8,4 | 9,5 |
| +10,00% | 70.230 $ | 27/40 | +67,50% | prezzo iniziale | 63.846 $ | 1/27 | +3,70% | -9,09% | DEBOLE | 13,4 | 17,0 |
| +10,00% | 70.230 $ | 27/40 | +67,50% | -5,00% | 60.654 $ | 1/27 | +3,70% | -13,64% | DEBOLE | 13,4 | 25,0 |
| +10,00% | 70.230 $ | 27/40 | +67,50% | -8,00% | 58.738 $ | 1/27 | +3,70% | -16,36% | DEBOLE | 13,4 | 26,0 |
| +10,00% | 70.230 $ | 27/40 | +67,50% | -10,00% | 57.461 $ | 1/27 | +3,70% | -18,18% | DEBOLE | 13,4 | 27,0 |
| +10,00% | 70.230 $ | 27/40 | +67,50% | -15,00% | 54.269 $ | 0/27 | 0,00% | -22,73% | DEBOLE | 13,4 | n/d |
| +15,00% | 73.423 $ | 22/40 | +55,00% | prezzo iniziale | 63.846 $ | 0/22 | 0,00% | -13,04% | DEBOLE | 14,5 | n/d |
| +15,00% | 73.423 $ | 22/40 | +55,00% | -5,00% | 60.654 $ | 0/22 | 0,00% | -17,39% | DEBOLE | 14,5 | n/d |
| +15,00% | 73.423 $ | 22/40 | +55,00% | -8,00% | 58.738 $ | 0/22 | 0,00% | -20,00% | DEBOLE | 14,5 | n/d |
| +15,00% | 73.423 $ | 22/40 | +55,00% | -10,00% | 57.461 $ | 0/22 | 0,00% | -21,74% | DEBOLE | 14,5 | n/d |
| +15,00% | 73.423 $ | 22/40 | +55,00% | -15,00% | 54.269 $ | 0/22 | 0,00% | -26,09% | DEBOLE | 14,5 | n/d |
| +20,00% | 76.615 $ | 19/40 | +47,50% | prezzo iniziale | 63.846 $ | 0/19 | 0,00% | -16,67% | DEBOLE | 16,3 | n/d |
| +20,00% | 76.615 $ | 19/40 | +47,50% | -5,00% | 60.654 $ | 0/19 | 0,00% | -20,83% | DEBOLE | 16,3 | n/d |
| +20,00% | 76.615 $ | 19/40 | +47,50% | -8,00% | 58.738 $ | 0/19 | 0,00% | -23,33% | DEBOLE | 16,3 | n/d |
| +20,00% | 76.615 $ | 19/40 | +47,50% | -10,00% | 57.461 $ | 0/19 | 0,00% | -25,00% | DEBOLE | 16,3 | n/d |
| +20,00% | 76.615 $ | 19/40 | +47,50% | -15,00% | 54.269 $ | 0/19 | 0,00% | -29,17% | DEBOLE | 16,3 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 17 prima sono scesi a -5,00%. Tra quei 17, 4 poi sono rimbalzati fino a +10,00%. Percentuale: +23,53% (4/17). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 22 prima sono saliti a +10,00%. Tra quei 22, 0 poi sono scaricati a -5,00%. Percentuale: 0,00% (0/22). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 70,03 $ | 17/40 | +42,50% | +5,00% | 77,41 $ | 6/17 | +35,29% | +10,53% | BASSA | 6,8 | 21,7 |
| -5,00% | 70,03 $ | 17/40 | +42,50% | +10,00% | 81,09 $ | 4/17 | +23,53% | +15,79% | DEBOLE | 6,8 | 24,5 |
| -5,00% | 70,03 $ | 17/40 | +42,50% | +15,00% | 84,78 $ | 1/17 | +5,88% | +21,05% | DEBOLE | 6,8 | 15,0 |
| -5,00% | 70,03 $ | 17/40 | +42,50% | +20,00% | 88,46 $ | 1/17 | +5,88% | +26,32% | DEBOLE | 6,8 | 16,0 |
| -8,00% | 67,82 $ | 15/40 | +37,50% | +5,00% | 77,41 $ | 4/15 | +26,67% | +14,13% | DEBOLE | 8,2 | 26,5 |
| -8,00% | 67,82 $ | 15/40 | +37,50% | +10,00% | 81,09 $ | 3/15 | +20,00% | +19,57% | DEBOLE | 8,2 | 27,7 |
| -8,00% | 67,82 $ | 15/40 | +37,50% | +15,00% | 84,78 $ | 0/15 | 0,00% | +25,00% | DEBOLE | 8,2 | n/d |
| -8,00% | 67,82 $ | 15/40 | +37,50% | +20,00% | 88,46 $ | 0/15 | 0,00% | +30,43% | DEBOLE | 8,2 | n/d |
| -10,00% | 66,35 $ | 14/40 | +35,00% | +5,00% | 77,41 $ | 4/14 | +28,57% | +16,67% | DEBOLE | 8,7 | 26,5 |
| -10,00% | 66,35 $ | 14/40 | +35,00% | +10,00% | 81,09 $ | 3/14 | +21,43% | +22,22% | DEBOLE | 8,7 | 27,7 |
| -10,00% | 66,35 $ | 14/40 | +35,00% | +15,00% | 84,78 $ | 0/14 | 0,00% | +27,78% | DEBOLE | 8,7 | n/d |
| -10,00% | 66,35 $ | 14/40 | +35,00% | +20,00% | 88,46 $ | 0/14 | 0,00% | +33,33% | DEBOLE | 8,7 | n/d |
| -15,00% | 62,66 $ | 9/40 | +22,50% | +5,00% | 77,41 $ | 1/9 | +11,11% | +23,53% | DEBOLE | 10,2 | 28,0 |
| -15,00% | 62,66 $ | 9/40 | +22,50% | +10,00% | 81,09 $ | 1/9 | +11,11% | +29,41% | DEBOLE | 10,2 | 30,0 |
| -15,00% | 62,66 $ | 9/40 | +22,50% | +15,00% | 84,78 $ | 0/9 | 0,00% | +35,29% | DEBOLE | 10,2 | n/d |
| -15,00% | 62,66 $ | 9/40 | +22,50% | +20,00% | 88,46 $ | 0/9 | 0,00% | +41,18% | DEBOLE | 10,2 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 77,41 $ | 28/40 | +70,00% | prezzo iniziale | 73,72 $ | 4/28 | +14,29% | -4,76% | DEBOLE | 9,3 | 10,8 |
| +5,00% | 77,41 $ | 28/40 | +70,00% | -5,00% | 70,03 $ | 3/28 | +10,71% | -9,52% | DEBOLE | 9,3 | 11,7 |
| +5,00% | 77,41 $ | 28/40 | +70,00% | -8,00% | 67,82 $ | 1/28 | +3,57% | -12,38% | DEBOLE | 9,3 | 18,0 |
| +5,00% | 77,41 $ | 28/40 | +70,00% | -10,00% | 66,35 $ | 0/28 | 0,00% | -14,29% | DEBOLE | 9,3 | n/d |
| +5,00% | 77,41 $ | 28/40 | +70,00% | -15,00% | 62,66 $ | 0/28 | 0,00% | -19,05% | DEBOLE | 9,3 | n/d |
| +10,00% | 81,09 $ | 22/40 | +55,00% | prezzo iniziale | 73,72 $ | 0/22 | 0,00% | -9,09% | DEBOLE | 13,5 | n/d |
| +10,00% | 81,09 $ | 22/40 | +55,00% | -5,00% | 70,03 $ | 0/22 | 0,00% | -13,64% | DEBOLE | 13,5 | n/d |
| +10,00% | 81,09 $ | 22/40 | +55,00% | -8,00% | 67,82 $ | 0/22 | 0,00% | -16,36% | DEBOLE | 13,5 | n/d |
| +10,00% | 81,09 $ | 22/40 | +55,00% | -10,00% | 66,35 $ | 0/22 | 0,00% | -18,18% | DEBOLE | 13,5 | n/d |
| +10,00% | 81,09 $ | 22/40 | +55,00% | -15,00% | 62,66 $ | 0/22 | 0,00% | -22,73% | DEBOLE | 13,5 | n/d |
| +15,00% | 84,78 $ | 15/40 | +37,50% | prezzo iniziale | 73,72 $ | 0/15 | 0,00% | -13,04% | DEBOLE | 12,7 | n/d |
| +15,00% | 84,78 $ | 15/40 | +37,50% | -5,00% | 70,03 $ | 0/15 | 0,00% | -17,39% | DEBOLE | 12,7 | n/d |
| +15,00% | 84,78 $ | 15/40 | +37,50% | -8,00% | 67,82 $ | 0/15 | 0,00% | -20,00% | DEBOLE | 12,7 | n/d |
| +15,00% | 84,78 $ | 15/40 | +37,50% | -10,00% | 66,35 $ | 0/15 | 0,00% | -21,74% | DEBOLE | 12,7 | n/d |
| +15,00% | 84,78 $ | 15/40 | +37,50% | -15,00% | 62,66 $ | 0/15 | 0,00% | -26,09% | DEBOLE | 12,7 | n/d |
| +20,00% | 88,46 $ | 12/40 | +30,00% | prezzo iniziale | 73,72 $ | 0/12 | 0,00% | -16,67% | DEBOLE | 15,8 | n/d |
| +20,00% | 88,46 $ | 12/40 | +30,00% | -5,00% | 70,03 $ | 0/12 | 0,00% | -20,83% | DEBOLE | 15,8 | n/d |
| +20,00% | 88,46 $ | 12/40 | +30,00% | -8,00% | 67,82 $ | 0/12 | 0,00% | -23,33% | DEBOLE | 15,8 | n/d |
| +20,00% | 88,46 $ | 12/40 | +30,00% | -10,00% | 66,35 $ | 0/12 | 0,00% | -25,00% | DEBOLE | 15,8 | n/d |
| +20,00% | 88,46 $ | 12/40 | +30,00% | -15,00% | 62,66 $ | 0/12 | 0,00% | -29,17% | DEBOLE | 15,8 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 33 prima sono scesi a -5,00%. Tra quei 33, 13 poi sono rimbalzati fino a +10,00%. Percentuale: +39,39% (13/33). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- DOGE: su 40 casi simili, 23 prima sono saliti a +10,00%. Tra quei 23, 5 poi sono scaricati a -5,00%. Percentuale: +21,74% (5/23). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06668 $ | 33/40 | +82,50% | +5,00% | 0,07370 $ | 18/33 | +54,55% | +10,53% | MEDIA | 5,0 | 19,1 |
| -5,00% | 0,06668 $ | 33/40 | +82,50% | +10,00% | 0,07721 $ | 13/33 | +39,39% | +15,79% | BASSA | 5,0 | 19,7 |
| -5,00% | 0,06668 $ | 33/40 | +82,50% | +15,00% | 0,08072 $ | 11/33 | +33,33% | +21,05% | DEBOLE | 5,0 | 21,3 |
| -5,00% | 0,06668 $ | 33/40 | +82,50% | +20,00% | 0,08423 $ | 6/33 | +18,18% | +26,32% | DEBOLE | 5,0 | 19,8 |
| -8,00% | 0,06457 $ | 28/40 | +70,00% | +5,00% | 0,07370 $ | 13/28 | +46,43% | +14,13% | BASSA | 6,4 | 19,3 |
| -8,00% | 0,06457 $ | 28/40 | +70,00% | +10,00% | 0,07721 $ | 9/28 | +32,14% | +19,57% | DEBOLE | 6,4 | 19,9 |
| -8,00% | 0,06457 $ | 28/40 | +70,00% | +15,00% | 0,08072 $ | 7/28 | +25,00% | +25,00% | DEBOLE | 6,4 | 20,1 |
| -8,00% | 0,06457 $ | 28/40 | +70,00% | +20,00% | 0,08423 $ | 5/28 | +17,86% | +30,43% | DEBOLE | 6,4 | 20,6 |
| -10,00% | 0,06317 $ | 25/40 | +62,50% | +5,00% | 0,07370 $ | 10/25 | +40,00% | +16,67% | BASSA | 7,9 | 21,8 |
| -10,00% | 0,06317 $ | 25/40 | +62,50% | +10,00% | 0,07721 $ | 6/25 | +24,00% | +22,22% | DEBOLE | 7,9 | 22,2 |
| -10,00% | 0,06317 $ | 25/40 | +62,50% | +15,00% | 0,08072 $ | 4/25 | +16,00% | +27,78% | DEBOLE | 7,9 | 23,8 |
| -10,00% | 0,06317 $ | 25/40 | +62,50% | +20,00% | 0,08423 $ | 2/25 | +8,00% | +33,33% | DEBOLE | 7,9 | 25,0 |
| -15,00% | 0,05966 $ | 18/40 | +45,00% | +5,00% | 0,07370 $ | 4/18 | +22,22% | +23,53% | DEBOLE | 12,0 | 24,5 |
| -15,00% | 0,05966 $ | 18/40 | +45,00% | +10,00% | 0,07721 $ | 3/18 | +16,67% | +29,41% | DEBOLE | 12,0 | 25,3 |
| -15,00% | 0,05966 $ | 18/40 | +45,00% | +15,00% | 0,08072 $ | 2/18 | +11,11% | +35,29% | DEBOLE | 12,0 | 23,5 |
| -15,00% | 0,05966 $ | 18/40 | +45,00% | +20,00% | 0,08423 $ | 2/18 | +11,11% | +41,18% | DEBOLE | 12,0 | 25,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07370 $ | 31/40 | +77,50% | prezzo iniziale | 0,07019 $ | 20/31 | +64,52% | -4,76% | MEDIA | 10,2 | 15,5 |
| +5,00% | 0,07370 $ | 31/40 | +77,50% | -5,00% | 0,06668 $ | 13/31 | +41,94% | -9,52% | BASSA | 10,2 | 13,6 |
| +5,00% | 0,07370 $ | 31/40 | +77,50% | -8,00% | 0,06457 $ | 10/31 | +32,26% | -12,38% | DEBOLE | 10,2 | 12,8 |
| +5,00% | 0,07370 $ | 31/40 | +77,50% | -10,00% | 0,06317 $ | 8/31 | +25,81% | -14,29% | DEBOLE | 10,2 | 12,1 |
| +5,00% | 0,07370 $ | 31/40 | +77,50% | -15,00% | 0,05966 $ | 6/31 | +19,35% | -19,05% | DEBOLE | 10,2 | 13,7 |
| +10,00% | 0,07721 $ | 23/40 | +57,50% | prezzo iniziale | 0,07019 $ | 9/23 | +39,13% | -9,09% | BASSA | 13,3 | 18,3 |
| +10,00% | 0,07721 $ | 23/40 | +57,50% | -5,00% | 0,06668 $ | 5/23 | +21,74% | -13,64% | DEBOLE | 13,3 | 17,0 |
| +10,00% | 0,07721 $ | 23/40 | +57,50% | -8,00% | 0,06457 $ | 3/23 | +13,04% | -16,36% | DEBOLE | 13,3 | 13,3 |
| +10,00% | 0,07721 $ | 23/40 | +57,50% | -10,00% | 0,06317 $ | 3/23 | +13,04% | -18,18% | DEBOLE | 13,3 | 13,3 |
| +10,00% | 0,07721 $ | 23/40 | +57,50% | -15,00% | 0,05966 $ | 3/23 | +13,04% | -22,73% | DEBOLE | 13,3 | 16,3 |
| +15,00% | 0,08072 $ | 19/40 | +47,50% | prezzo iniziale | 0,07019 $ | 5/19 | +26,32% | -13,04% | DEBOLE | 14,4 | 17,6 |
| +15,00% | 0,08072 $ | 19/40 | +47,50% | -5,00% | 0,06668 $ | 3/19 | +15,79% | -17,39% | DEBOLE | 14,4 | 14,3 |
| +15,00% | 0,08072 $ | 19/40 | +47,50% | -8,00% | 0,06457 $ | 2/19 | +10,53% | -20,00% | DEBOLE | 14,4 | 13,5 |
| +15,00% | 0,08072 $ | 19/40 | +47,50% | -10,00% | 0,06317 $ | 2/19 | +10,53% | -21,74% | DEBOLE | 14,4 | 13,5 |
| +15,00% | 0,08072 $ | 19/40 | +47,50% | -15,00% | 0,05966 $ | 2/19 | +10,53% | -26,09% | DEBOLE | 14,4 | 18,0 |
| +20,00% | 0,08423 $ | 13/40 | +32,50% | prezzo iniziale | 0,07019 $ | 3/13 | +23,08% | -16,67% | DEBOLE | 15,6 | 23,0 |
| +20,00% | 0,08423 $ | 13/40 | +32,50% | -5,00% | 0,06668 $ | 1/13 | +7,69% | -20,83% | DEBOLE | 15,6 | 17,0 |
| +20,00% | 0,08423 $ | 13/40 | +32,50% | -8,00% | 0,06457 $ | 0/13 | 0,00% | -23,33% | DEBOLE | 15,6 | n/d |
| +20,00% | 0,08423 $ | 13/40 | +32,50% | -10,00% | 0,06317 $ | 0/13 | 0,00% | -25,00% | DEBOLE | 15,6 | n/d |
| +20,00% | 0,08423 $ | 13/40 | +32,50% | -15,00% | 0,05966 $ | 0/13 | 0,00% | -29,17% | DEBOLE | 15,6 | n/d |

---
