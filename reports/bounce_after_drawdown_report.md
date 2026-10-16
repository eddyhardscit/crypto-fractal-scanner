# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-10-16 07:32:45 CEST**  
UTC: **2026-10-16 05:32:45 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 77.999 $ | 90.315 $ | +34,62% | +15,79% | rimbalzo poco frequente | 90.315 $ | 77.999 $ | +28,57% | -13,64% | spike storicamente più resistente |
| SOL | 100,53 $ | 116,40 $ | +38,10% | +15,79% | rimbalzo debole | 116,40 $ | 100,53 $ | +24,24% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07804 $ | 0,09036 $ | +29,41% | +15,79% | rimbalzo poco frequente | 0,09036 $ | 0,07804 $ | +15,15% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 26 prima sono scesi a -5,00%. Tra quei 26, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +34,62% (9/26). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- BTC: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 8 poi sono scaricati a -5,00%. Percentuale: +28,57% (8/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 77.999 $ | 26/40 | +65,00% | +5,00% | 86.209 $ | 14/26 | +53,85% | +10,53% | MEDIA | 7,8 | 15,9 |
| -5,00% | 77.999 $ | 26/40 | +65,00% | +10,00% | 90.315 $ | 9/26 | +34,62% | +15,79% | DEBOLE | 7,8 | 16,6 |
| -5,00% | 77.999 $ | 26/40 | +65,00% | +15,00% | 94.420 $ | 7/26 | +26,92% | +21,05% | DEBOLE | 7,8 | 15,4 |
| -5,00% | 77.999 $ | 26/40 | +65,00% | +20,00% | 98.525 $ | 6/26 | +23,08% | +26,32% | DEBOLE | 7,8 | 16,8 |
| -8,00% | 75.536 $ | 19/40 | +47,50% | +5,00% | 86.209 $ | 8/19 | +42,11% | +14,13% | BASSA | 10,2 | 20,1 |
| -8,00% | 75.536 $ | 19/40 | +47,50% | +10,00% | 90.315 $ | 4/19 | +21,05% | +19,57% | DEBOLE | 10,2 | 20,2 |
| -8,00% | 75.536 $ | 19/40 | +47,50% | +15,00% | 94.420 $ | 2/19 | +10,53% | +25,00% | DEBOLE | 10,2 | 17,0 |
| -8,00% | 75.536 $ | 19/40 | +47,50% | +20,00% | 98.525 $ | 2/19 | +10,53% | +30,43% | DEBOLE | 10,2 | 22,0 |
| -10,00% | 73.894 $ | 16/40 | +40,00% | +5,00% | 86.209 $ | 5/16 | +31,25% | +16,67% | DEBOLE | 10,7 | 17,8 |
| -10,00% | 73.894 $ | 16/40 | +40,00% | +10,00% | 90.315 $ | 3/16 | +18,75% | +22,22% | DEBOLE | 10,7 | 20,7 |
| -10,00% | 73.894 $ | 16/40 | +40,00% | +15,00% | 94.420 $ | 1/16 | +6,25% | +27,78% | DEBOLE | 10,7 | 15,0 |
| -10,00% | 73.894 $ | 16/40 | +40,00% | +20,00% | 98.525 $ | 1/16 | +6,25% | +33,33% | DEBOLE | 10,7 | 15,0 |
| -15,00% | 69.789 $ | 12/40 | +30,00% | +5,00% | 86.209 $ | 2/12 | +16,67% | +23,53% | DEBOLE | 14,6 | 24,5 |
| -15,00% | 69.789 $ | 12/40 | +30,00% | +10,00% | 90.315 $ | 1/12 | +8,33% | +29,41% | DEBOLE | 14,6 | 20,0 |
| -15,00% | 69.789 $ | 12/40 | +30,00% | +15,00% | 94.420 $ | 0/12 | 0,00% | +35,29% | DEBOLE | 14,6 | n/d |
| -15,00% | 69.789 $ | 12/40 | +30,00% | +20,00% | 98.525 $ | 0/12 | 0,00% | +41,18% | DEBOLE | 14,6 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 86.209 $ | 34/40 | +85,00% | prezzo iniziale | 82.104 $ | 18/34 | +52,94% | -4,76% | MEDIA | 5,5 | 12,3 |
| +5,00% | 86.209 $ | 34/40 | +85,00% | -5,00% | 77.999 $ | 16/34 | +47,06% | -9,52% | BASSA | 5,5 | 14,8 |
| +5,00% | 86.209 $ | 34/40 | +85,00% | -8,00% | 75.536 $ | 10/34 | +29,41% | -12,38% | DEBOLE | 5,5 | 14,0 |
| +5,00% | 86.209 $ | 34/40 | +85,00% | -10,00% | 73.894 $ | 8/34 | +23,53% | -14,29% | DEBOLE | 5,5 | 13,0 |
| +5,00% | 86.209 $ | 34/40 | +85,00% | -15,00% | 69.789 $ | 6/34 | +17,65% | -19,05% | DEBOLE | 5,5 | 15,0 |
| +10,00% | 90.315 $ | 28/40 | +70,00% | prezzo iniziale | 82.104 $ | 10/28 | +35,71% | -9,09% | BASSA | 8,1 | 17,2 |
| +10,00% | 90.315 $ | 28/40 | +70,00% | -5,00% | 77.999 $ | 8/28 | +28,57% | -13,64% | DEBOLE | 8,1 | 18,1 |
| +10,00% | 90.315 $ | 28/40 | +70,00% | -8,00% | 75.536 $ | 6/28 | +21,43% | -16,36% | DEBOLE | 8,1 | 17,3 |
| +10,00% | 90.315 $ | 28/40 | +70,00% | -10,00% | 73.894 $ | 4/28 | +14,29% | -18,18% | DEBOLE | 8,1 | 17,0 |
| +10,00% | 90.315 $ | 28/40 | +70,00% | -15,00% | 69.789 $ | 2/28 | +7,14% | -22,73% | DEBOLE | 8,1 | 12,5 |
| +15,00% | 94.420 $ | 18/40 | +45,00% | prezzo iniziale | 82.104 $ | 2/18 | +11,11% | -13,04% | DEBOLE | 9,3 | 25,0 |
| +15,00% | 94.420 $ | 18/40 | +45,00% | -5,00% | 77.999 $ | 1/18 | +5,56% | -17,39% | DEBOLE | 9,3 | 27,0 |
| +15,00% | 94.420 $ | 18/40 | +45,00% | -8,00% | 75.536 $ | 0/18 | 0,00% | -20,00% | DEBOLE | 9,3 | n/d |
| +15,00% | 94.420 $ | 18/40 | +45,00% | -10,00% | 73.894 $ | 0/18 | 0,00% | -21,74% | DEBOLE | 9,3 | n/d |
| +15,00% | 94.420 $ | 18/40 | +45,00% | -15,00% | 69.789 $ | 0/18 | 0,00% | -26,09% | DEBOLE | 9,3 | n/d |
| +20,00% | 98.525 $ | 15/40 | +37,50% | prezzo iniziale | 82.104 $ | 1/15 | +6,67% | -16,67% | DEBOLE | 10,8 | 25,0 |
| +20,00% | 98.525 $ | 15/40 | +37,50% | -5,00% | 77.999 $ | 1/15 | +6,67% | -20,83% | DEBOLE | 10,8 | 27,0 |
| +20,00% | 98.525 $ | 15/40 | +37,50% | -8,00% | 75.536 $ | 0/15 | 0,00% | -23,33% | DEBOLE | 10,8 | n/d |
| +20,00% | 98.525 $ | 15/40 | +37,50% | -10,00% | 73.894 $ | 0/15 | 0,00% | -25,00% | DEBOLE | 10,8 | n/d |
| +20,00% | 98.525 $ | 15/40 | +37,50% | -15,00% | 69.789 $ | 0/15 | 0,00% | -29,17% | DEBOLE | 10,8 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 21 prima sono scesi a -5,00%. Tra quei 21, 8 poi sono rimbalzati fino a +10,00%. Percentuale: +38,10% (8/21). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- SOL: su 40 casi simili, 33 prima sono saliti a +10,00%. Tra quei 33, 8 poi sono scaricati a -5,00%. Percentuale: +24,24% (8/33). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 100,53 $ | 21/40 | +52,50% | +5,00% | 111,11 $ | 15/21 | +71,43% | +10,53% | ALTA | 7,2 | 19,4 |
| -5,00% | 100,53 $ | 21/40 | +52,50% | +10,00% | 116,40 $ | 8/21 | +38,10% | +15,79% | BASSA | 7,2 | 18,6 |
| -5,00% | 100,53 $ | 21/40 | +52,50% | +15,00% | 121,69 $ | 6/21 | +28,57% | +21,05% | DEBOLE | 7,2 | 16,3 |
| -5,00% | 100,53 $ | 21/40 | +52,50% | +20,00% | 126,98 $ | 5/21 | +23,81% | +26,32% | DEBOLE | 7,2 | 17,2 |
| -8,00% | 97,35 $ | 16/40 | +40,00% | +5,00% | 111,11 $ | 10/16 | +62,50% | +14,13% | MEDIA | 10,5 | 22,3 |
| -8,00% | 97,35 $ | 16/40 | +40,00% | +10,00% | 116,40 $ | 5/16 | +31,25% | +19,57% | DEBOLE | 10,5 | 23,2 |
| -8,00% | 97,35 $ | 16/40 | +40,00% | +15,00% | 121,69 $ | 3/16 | +18,75% | +25,00% | DEBOLE | 10,5 | 20,3 |
| -8,00% | 97,35 $ | 16/40 | +40,00% | +20,00% | 126,98 $ | 2/16 | +12,50% | +30,43% | DEBOLE | 10,5 | 22,0 |
| -10,00% | 95,24 $ | 13/40 | +32,50% | +5,00% | 111,11 $ | 7/13 | +53,85% | +16,67% | MEDIA | 12,1 | 21,6 |
| -10,00% | 95,24 $ | 13/40 | +32,50% | +10,00% | 116,40 $ | 4/13 | +30,77% | +22,22% | DEBOLE | 12,1 | 24,2 |
| -10,00% | 95,24 $ | 13/40 | +32,50% | +15,00% | 121,69 $ | 2/13 | +15,38% | +27,78% | DEBOLE | 12,1 | 21,0 |
| -10,00% | 95,24 $ | 13/40 | +32,50% | +20,00% | 126,98 $ | 1/13 | +7,69% | +33,33% | DEBOLE | 12,1 | 15,0 |
| -15,00% | 89,95 $ | 6/40 | +15,00% | +5,00% | 111,11 $ | 2/6 | +33,33% | +23,53% | DEBOLE | 14,7 | 29,0 |
| -15,00% | 89,95 $ | 6/40 | +15,00% | +10,00% | 116,40 $ | 1/6 | +16,67% | +29,41% | DEBOLE | 14,7 | 28,0 |
| -15,00% | 89,95 $ | 6/40 | +15,00% | +15,00% | 121,69 $ | 0/6 | 0,00% | +35,29% | DEBOLE | 14,7 | n/d |
| -15,00% | 89,95 $ | 6/40 | +15,00% | +20,00% | 126,98 $ | 0/6 | 0,00% | +41,18% | DEBOLE | 14,7 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 111,11 $ | 38/40 | +95,00% | prezzo iniziale | 105,82 $ | 17/38 | +44,74% | -4,76% | BASSA | 6,0 | 15,3 |
| +5,00% | 111,11 $ | 38/40 | +95,00% | -5,00% | 100,53 $ | 12/38 | +31,58% | -9,52% | DEBOLE | 6,0 | 15,6 |
| +5,00% | 111,11 $ | 38/40 | +95,00% | -8,00% | 97,35 $ | 9/38 | +23,68% | -12,38% | DEBOLE | 6,0 | 15,4 |
| +5,00% | 111,11 $ | 38/40 | +95,00% | -10,00% | 95,24 $ | 7/38 | +18,42% | -14,29% | DEBOLE | 6,0 | 15,7 |
| +5,00% | 111,11 $ | 38/40 | +95,00% | -15,00% | 89,95 $ | 3/38 | +7,89% | -19,05% | DEBOLE | 6,0 | 18,7 |
| +10,00% | 116,40 $ | 33/40 | +82,50% | prezzo iniziale | 105,82 $ | 12/33 | +36,36% | -9,09% | BASSA | 7,5 | 19,1 |
| +10,00% | 116,40 $ | 33/40 | +82,50% | -5,00% | 100,53 $ | 8/33 | +24,24% | -13,64% | DEBOLE | 7,5 | 17,4 |
| +10,00% | 116,40 $ | 33/40 | +82,50% | -8,00% | 97,35 $ | 6/33 | +18,18% | -16,36% | DEBOLE | 7,5 | 16,2 |
| +10,00% | 116,40 $ | 33/40 | +82,50% | -10,00% | 95,24 $ | 4/33 | +12,12% | -18,18% | DEBOLE | 7,5 | 15,2 |
| +10,00% | 116,40 $ | 33/40 | +82,50% | -15,00% | 89,95 $ | 1/33 | +3,03% | -22,73% | DEBOLE | 7,5 | 11,0 |
| +15,00% | 121,69 $ | 22/40 | +55,00% | prezzo iniziale | 105,82 $ | 3/22 | +13,64% | -13,04% | DEBOLE | 9,7 | 26,7 |
| +15,00% | 121,69 $ | 22/40 | +55,00% | -5,00% | 100,53 $ | 1/22 | +4,55% | -17,39% | DEBOLE | 9,7 | 27,0 |
| +15,00% | 121,69 $ | 22/40 | +55,00% | -8,00% | 97,35 $ | 0/22 | 0,00% | -20,00% | DEBOLE | 9,7 | n/d |
| +15,00% | 121,69 $ | 22/40 | +55,00% | -10,00% | 95,24 $ | 0/22 | 0,00% | -21,74% | DEBOLE | 9,7 | n/d |
| +15,00% | 121,69 $ | 22/40 | +55,00% | -15,00% | 89,95 $ | 0/22 | 0,00% | -26,09% | DEBOLE | 9,7 | n/d |
| +20,00% | 126,98 $ | 16/40 | +40,00% | prezzo iniziale | 105,82 $ | 1/16 | +6,25% | -16,67% | DEBOLE | 11,8 | 25,0 |
| +20,00% | 126,98 $ | 16/40 | +40,00% | -5,00% | 100,53 $ | 1/16 | +6,25% | -20,83% | DEBOLE | 11,8 | 27,0 |
| +20,00% | 126,98 $ | 16/40 | +40,00% | -8,00% | 97,35 $ | 0/16 | 0,00% | -23,33% | DEBOLE | 11,8 | n/d |
| +20,00% | 126,98 $ | 16/40 | +40,00% | -10,00% | 95,24 $ | 0/16 | 0,00% | -25,00% | DEBOLE | 11,8 | n/d |
| +20,00% | 126,98 $ | 16/40 | +40,00% | -15,00% | 89,95 $ | 0/16 | 0,00% | -29,17% | DEBOLE | 11,8 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 17 prima sono scesi a -5,00%. Tra quei 17, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +29,41% (5/17). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 33 prima sono saliti a +10,00%. Tra quei 33, 5 poi sono scaricati a -5,00%. Percentuale: +15,15% (5/33). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,07804 $ | 17/40 | +42,50% | +5,00% | 0,08626 $ | 9/17 | +52,94% | +10,53% | MEDIA | 5,9 | 18,6 |
| -5,00% | 0,07804 $ | 17/40 | +42,50% | +10,00% | 0,09036 $ | 5/17 | +29,41% | +15,79% | DEBOLE | 5,9 | 17,8 |
| -5,00% | 0,07804 $ | 17/40 | +42,50% | +15,00% | 0,09447 $ | 4/17 | +23,53% | +21,05% | DEBOLE | 5,9 | 15,8 |
| -5,00% | 0,07804 $ | 17/40 | +42,50% | +20,00% | 0,09858 $ | 4/17 | +23,53% | +26,32% | DEBOLE | 5,9 | 19,5 |
| -8,00% | 0,07558 $ | 13/40 | +32,50% | +5,00% | 0,08626 $ | 5/13 | +38,46% | +14,13% | BASSA | 9,0 | 20,6 |
| -8,00% | 0,07558 $ | 13/40 | +32,50% | +10,00% | 0,09036 $ | 3/13 | +23,08% | +19,57% | DEBOLE | 9,0 | 20,7 |
| -8,00% | 0,07558 $ | 13/40 | +32,50% | +15,00% | 0,09447 $ | 2/13 | +15,38% | +25,00% | DEBOLE | 9,0 | 17,0 |
| -8,00% | 0,07558 $ | 13/40 | +32,50% | +20,00% | 0,09858 $ | 2/13 | +15,38% | +30,43% | DEBOLE | 9,0 | 22,0 |
| -10,00% | 0,07393 $ | 11/40 | +27,50% | +5,00% | 0,08626 $ | 4/11 | +36,36% | +16,67% | BASSA | 10,6 | 22,0 |
| -10,00% | 0,07393 $ | 11/40 | +27,50% | +10,00% | 0,09036 $ | 2/11 | +18,18% | +22,22% | DEBOLE | 10,6 | 21,5 |
| -10,00% | 0,07393 $ | 11/40 | +27,50% | +15,00% | 0,09447 $ | 1/11 | +9,09% | +27,78% | DEBOLE | 10,6 | 15,0 |
| -10,00% | 0,07393 $ | 11/40 | +27,50% | +20,00% | 0,09858 $ | 1/11 | +9,09% | +33,33% | DEBOLE | 10,6 | 15,0 |
| -15,00% | 0,06983 $ | 8/40 | +20,00% | +5,00% | 0,08626 $ | 2/8 | +25,00% | +23,53% | DEBOLE | 14,4 | 29,0 |
| -15,00% | 0,06983 $ | 8/40 | +20,00% | +10,00% | 0,09036 $ | 1/8 | +12,50% | +29,41% | DEBOLE | 14,4 | 28,0 |
| -15,00% | 0,06983 $ | 8/40 | +20,00% | +15,00% | 0,09447 $ | 0/8 | 0,00% | +35,29% | DEBOLE | 14,4 | n/d |
| -15,00% | 0,06983 $ | 8/40 | +20,00% | +20,00% | 0,09858 $ | 0/8 | 0,00% | +41,18% | DEBOLE | 14,4 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,08626 $ | 37/40 | +92,50% | prezzo iniziale | 0,08215 $ | 12/37 | +32,43% | -4,76% | DEBOLE | 5,6 | 13,6 |
| +5,00% | 0,08626 $ | 37/40 | +92,50% | -5,00% | 0,07804 $ | 7/37 | +18,92% | -9,52% | DEBOLE | 5,6 | 14,3 |
| +5,00% | 0,08626 $ | 37/40 | +92,50% | -8,00% | 0,07558 $ | 6/37 | +16,22% | -12,38% | DEBOLE | 5,6 | 14,3 |
| +5,00% | 0,08626 $ | 37/40 | +92,50% | -10,00% | 0,07393 $ | 5/37 | +13,51% | -14,29% | DEBOLE | 5,6 | 13,2 |
| +5,00% | 0,08626 $ | 37/40 | +92,50% | -15,00% | 0,06983 $ | 5/37 | +13,51% | -19,05% | DEBOLE | 5,6 | 16,6 |
| +10,00% | 0,09036 $ | 33/40 | +82,50% | prezzo iniziale | 0,08215 $ | 9/33 | +27,27% | -9,09% | DEBOLE | 5,7 | 15,1 |
| +10,00% | 0,09036 $ | 33/40 | +82,50% | -5,00% | 0,07804 $ | 5/33 | +15,15% | -13,64% | DEBOLE | 5,7 | 13,2 |
| +10,00% | 0,09036 $ | 33/40 | +82,50% | -8,00% | 0,07558 $ | 4/33 | +12,12% | -16,36% | DEBOLE | 5,7 | 12,5 |
| +10,00% | 0,09036 $ | 33/40 | +82,50% | -10,00% | 0,07393 $ | 3/33 | +9,09% | -18,18% | DEBOLE | 5,7 | 10,0 |
| +10,00% | 0,09036 $ | 33/40 | +82,50% | -15,00% | 0,06983 $ | 3/33 | +9,09% | -22,73% | DEBOLE | 5,7 | 15,0 |
| +15,00% | 0,09447 $ | 24/40 | +60,00% | prezzo iniziale | 0,08215 $ | 1/24 | +4,17% | -13,04% | DEBOLE | 7,0 | 25,0 |
| +15,00% | 0,09447 $ | 24/40 | +60,00% | -5,00% | 0,07804 $ | 0/24 | 0,00% | -17,39% | DEBOLE | 7,0 | n/d |
| +15,00% | 0,09447 $ | 24/40 | +60,00% | -8,00% | 0,07558 $ | 0/24 | 0,00% | -20,00% | DEBOLE | 7,0 | n/d |
| +15,00% | 0,09447 $ | 24/40 | +60,00% | -10,00% | 0,07393 $ | 0/24 | 0,00% | -21,74% | DEBOLE | 7,0 | n/d |
| +15,00% | 0,09447 $ | 24/40 | +60,00% | -15,00% | 0,06983 $ | 0/24 | 0,00% | -26,09% | DEBOLE | 7,0 | n/d |
| +20,00% | 0,09858 $ | 19/40 | +47,50% | prezzo iniziale | 0,08215 $ | 0/19 | 0,00% | -16,67% | DEBOLE | 10,7 | n/d |
| +20,00% | 0,09858 $ | 19/40 | +47,50% | -5,00% | 0,07804 $ | 0/19 | 0,00% | -20,83% | DEBOLE | 10,7 | n/d |
| +20,00% | 0,09858 $ | 19/40 | +47,50% | -8,00% | 0,07558 $ | 0/19 | 0,00% | -23,33% | DEBOLE | 10,7 | n/d |
| +20,00% | 0,09858 $ | 19/40 | +47,50% | -10,00% | 0,07393 $ | 0/19 | 0,00% | -25,00% | DEBOLE | 10,7 | n/d |
| +20,00% | 0,09858 $ | 19/40 | +47,50% | -15,00% | 0,06983 $ | 0/19 | 0,00% | -29,17% | DEBOLE | 10,7 | n/d |

---
