# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-10-13 07:32:09 CEST**  
UTC: **2026-10-13 05:32:09 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 79.450 $ | 91.994 $ | +37,50% | +15,79% | rimbalzo debole | 91.994 $ | 79.450 $ | +33,33% | -13,64% | spike storicamente più resistente |
| SOL | 102,80 $ | 119,03 $ | +41,38% | +15,79% | rimbalzo debole | 119,03 $ | 102,80 $ | +24,14% | -13,64% | spike storicamente più resistente |
| DOGE | 0,08046 $ | 0,09316 $ | +50,00% | +15,79% | rimbalzo possibile | 0,09316 $ | 0,08046 $ | +9,68% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 32 prima sono scesi a -5,00%. Tra quei 32, 12 poi sono rimbalzati fino a +10,00%. Percentuale: +37,50% (12/32). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 27 prima sono saliti a +10,00%. Tra quei 27, 9 poi sono scaricati a -5,00%. Percentuale: +33,33% (9/27). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 79.450 $ | 32/40 | +80,00% | +5,00% | 87.813 $ | 15/32 | +46,88% | +10,53% | BASSA | 8,6 | 13,6 |
| -5,00% | 79.450 $ | 32/40 | +80,00% | +10,00% | 91.994 $ | 12/32 | +37,50% | +15,79% | BASSA | 8,6 | 16,5 |
| -5,00% | 79.450 $ | 32/40 | +80,00% | +15,00% | 96.176 $ | 10/32 | +31,25% | +21,05% | DEBOLE | 8,6 | 18,6 |
| -5,00% | 79.450 $ | 32/40 | +80,00% | +20,00% | 100.357 $ | 9/32 | +28,12% | +26,32% | DEBOLE | 8,6 | 23,1 |
| -8,00% | 76.941 $ | 27/40 | +67,50% | +5,00% | 87.813 $ | 12/27 | +44,44% | +14,13% | BASSA | 8,3 | 13,6 |
| -8,00% | 76.941 $ | 27/40 | +67,50% | +10,00% | 91.994 $ | 9/27 | +33,33% | +19,57% | DEBOLE | 8,3 | 15,7 |
| -8,00% | 76.941 $ | 27/40 | +67,50% | +15,00% | 96.176 $ | 7/27 | +25,93% | +25,00% | DEBOLE | 8,3 | 18,1 |
| -8,00% | 76.941 $ | 27/40 | +67,50% | +20,00% | 100.357 $ | 6/27 | +22,22% | +30,43% | DEBOLE | 8,3 | 24,2 |
| -10,00% | 75.268 $ | 21/40 | +52,50% | +5,00% | 87.813 $ | 7/21 | +33,33% | +16,67% | DEBOLE | 9,1 | 17,0 |
| -10,00% | 75.268 $ | 21/40 | +52,50% | +10,00% | 91.994 $ | 5/21 | +23,81% | +22,22% | DEBOLE | 9,1 | 18,4 |
| -10,00% | 75.268 $ | 21/40 | +52,50% | +15,00% | 96.176 $ | 4/21 | +19,05% | +27,78% | DEBOLE | 9,1 | 19,8 |
| -10,00% | 75.268 $ | 21/40 | +52,50% | +20,00% | 100.357 $ | 3/21 | +14,29% | +33,33% | DEBOLE | 9,1 | 21,3 |
| -15,00% | 71.087 $ | 17/40 | +42,50% | +5,00% | 87.813 $ | 3/17 | +17,65% | +23,53% | DEBOLE | 13,4 | 17,7 |
| -15,00% | 71.087 $ | 17/40 | +42,50% | +10,00% | 91.994 $ | 2/17 | +11,76% | +29,41% | DEBOLE | 13,4 | 21,5 |
| -15,00% | 71.087 $ | 17/40 | +42,50% | +15,00% | 96.176 $ | 2/17 | +11,76% | +35,29% | DEBOLE | 13,4 | 24,5 |
| -15,00% | 71.087 $ | 17/40 | +42,50% | +20,00% | 100.357 $ | 1/17 | +5,88% | +41,18% | DEBOLE | 13,4 | 24,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 87.813 $ | 33/40 | +82,50% | prezzo iniziale | 83.631 $ | 23/33 | +69,70% | -4,76% | ALTA | 6,8 | 14,2 |
| +5,00% | 87.813 $ | 33/40 | +82,50% | -5,00% | 79.450 $ | 15/33 | +45,45% | -9,52% | BASSA | 6,8 | 16,4 |
| +5,00% | 87.813 $ | 33/40 | +82,50% | -8,00% | 76.941 $ | 11/33 | +33,33% | -12,38% | DEBOLE | 6,8 | 17,8 |
| +5,00% | 87.813 $ | 33/40 | +82,50% | -10,00% | 75.268 $ | 9/33 | +27,27% | -14,29% | DEBOLE | 6,8 | 16,9 |
| +5,00% | 87.813 $ | 33/40 | +82,50% | -15,00% | 71.087 $ | 8/33 | +24,24% | -19,05% | DEBOLE | 6,8 | 18,5 |
| +10,00% | 91.994 $ | 27/40 | +67,50% | prezzo iniziale | 83.631 $ | 15/27 | +55,56% | -9,09% | MEDIA | 10,5 | 19,5 |
| +10,00% | 91.994 $ | 27/40 | +67,50% | -5,00% | 79.450 $ | 9/27 | +33,33% | -13,64% | DEBOLE | 10,5 | 20,7 |
| +10,00% | 91.994 $ | 27/40 | +67,50% | -8,00% | 76.941 $ | 6/27 | +22,22% | -16,36% | DEBOLE | 10,5 | 21,7 |
| +10,00% | 91.994 $ | 27/40 | +67,50% | -10,00% | 75.268 $ | 5/27 | +18,52% | -18,18% | DEBOLE | 10,5 | 20,8 |
| +10,00% | 91.994 $ | 27/40 | +67,50% | -15,00% | 71.087 $ | 4/27 | +14,81% | -22,73% | DEBOLE | 10,5 | 22,8 |
| +15,00% | 96.176 $ | 19/40 | +47,50% | prezzo iniziale | 83.631 $ | 6/19 | +31,58% | -13,04% | DEBOLE | 12,5 | 18,2 |
| +15,00% | 96.176 $ | 19/40 | +47,50% | -5,00% | 79.450 $ | 4/19 | +21,05% | -17,39% | DEBOLE | 12,5 | 20,5 |
| +15,00% | 96.176 $ | 19/40 | +47,50% | -8,00% | 76.941 $ | 2/19 | +10,53% | -20,00% | DEBOLE | 12,5 | 21,5 |
| +15,00% | 96.176 $ | 19/40 | +47,50% | -10,00% | 75.268 $ | 1/19 | +5,26% | -21,74% | DEBOLE | 12,5 | 16,0 |
| +15,00% | 96.176 $ | 19/40 | +47,50% | -15,00% | 71.087 $ | 1/19 | +5,26% | -26,09% | DEBOLE | 12,5 | 17,0 |
| +20,00% | 100.357 $ | 13/40 | +32,50% | prezzo iniziale | 83.631 $ | 2/13 | +15,38% | -16,67% | DEBOLE | 18,8 | 28,5 |
| +20,00% | 100.357 $ | 13/40 | +32,50% | -5,00% | 79.450 $ | 1/13 | +7,69% | -20,83% | DEBOLE | 18,8 | 30,0 |
| +20,00% | 100.357 $ | 13/40 | +32,50% | -8,00% | 76.941 $ | 1/13 | +7,69% | -23,33% | DEBOLE | 18,8 | 30,0 |
| +20,00% | 100.357 $ | 13/40 | +32,50% | -10,00% | 75.268 $ | 0/13 | 0,00% | -25,00% | DEBOLE | 18,8 | n/d |
| +20,00% | 100.357 $ | 13/40 | +32,50% | -15,00% | 71.087 $ | 0/13 | 0,00% | -29,17% | DEBOLE | 18,8 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 29 prima sono scesi a -5,00%. Tra quei 29, 12 poi sono rimbalzati fino a +10,00%. Percentuale: +41,38% (12/29). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- SOL: su 40 casi simili, 29 prima sono saliti a +10,00%. Tra quei 29, 7 poi sono scaricati a -5,00%. Percentuale: +24,14% (7/29). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 102,80 $ | 29/40 | +72,50% | +5,00% | 113,62 $ | 18/29 | +62,07% | +10,53% | MEDIA | 7,9 | 14,2 |
| -5,00% | 102,80 $ | 29/40 | +72,50% | +10,00% | 119,03 $ | 12/29 | +41,38% | +15,79% | BASSA | 7,9 | 11,9 |
| -5,00% | 102,80 $ | 29/40 | +72,50% | +15,00% | 124,44 $ | 11/29 | +37,93% | +21,05% | BASSA | 7,9 | 13,3 |
| -5,00% | 102,80 $ | 29/40 | +72,50% | +20,00% | 129,85 $ | 10/29 | +34,48% | +26,32% | DEBOLE | 7,9 | 18,8 |
| -8,00% | 99,55 $ | 22/40 | +55,00% | +5,00% | 113,62 $ | 12/22 | +54,55% | +14,13% | MEDIA | 10,0 | 16,4 |
| -8,00% | 99,55 $ | 22/40 | +55,00% | +10,00% | 119,03 $ | 7/22 | +31,82% | +19,57% | DEBOLE | 10,0 | 13,1 |
| -8,00% | 99,55 $ | 22/40 | +55,00% | +15,00% | 124,44 $ | 6/22 | +27,27% | +25,00% | DEBOLE | 10,0 | 15,5 |
| -8,00% | 99,55 $ | 22/40 | +55,00% | +20,00% | 129,85 $ | 6/22 | +27,27% | +30,43% | DEBOLE | 10,0 | 22,7 |
| -10,00% | 97,39 $ | 15/40 | +37,50% | +5,00% | 113,62 $ | 5/15 | +33,33% | +16,67% | DEBOLE | 12,1 | 16,6 |
| -10,00% | 97,39 $ | 15/40 | +37,50% | +10,00% | 119,03 $ | 3/15 | +20,00% | +22,22% | DEBOLE | 12,1 | 14,3 |
| -10,00% | 97,39 $ | 15/40 | +37,50% | +15,00% | 124,44 $ | 3/15 | +20,00% | +27,78% | DEBOLE | 12,1 | 15,0 |
| -10,00% | 97,39 $ | 15/40 | +37,50% | +20,00% | 129,85 $ | 3/15 | +20,00% | +33,33% | DEBOLE | 12,1 | 18,3 |
| -15,00% | 91,98 $ | 10/40 | +25,00% | +5,00% | 113,62 $ | 0/10 | 0,00% | +23,53% | DEBOLE | 14,5 | n/d |
| -15,00% | 91,98 $ | 10/40 | +25,00% | +10,00% | 119,03 $ | 0/10 | 0,00% | +29,41% | DEBOLE | 14,5 | n/d |
| -15,00% | 91,98 $ | 10/40 | +25,00% | +15,00% | 124,44 $ | 0/10 | 0,00% | +35,29% | DEBOLE | 14,5 | n/d |
| -15,00% | 91,98 $ | 10/40 | +25,00% | +20,00% | 129,85 $ | 0/10 | 0,00% | +41,18% | DEBOLE | 14,5 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 113,62 $ | 35/40 | +87,50% | prezzo iniziale | 108,21 $ | 19/35 | +54,29% | -4,76% | MEDIA | 5,7 | 15,1 |
| +5,00% | 113,62 $ | 35/40 | +87,50% | -5,00% | 102,80 $ | 14/35 | +40,00% | -9,52% | BASSA | 5,7 | 17,8 |
| +5,00% | 113,62 $ | 35/40 | +87,50% | -8,00% | 99,55 $ | 11/35 | +31,43% | -12,38% | DEBOLE | 5,7 | 18,5 |
| +5,00% | 113,62 $ | 35/40 | +87,50% | -10,00% | 97,39 $ | 8/35 | +22,86% | -14,29% | DEBOLE | 5,7 | 18,2 |
| +5,00% | 113,62 $ | 35/40 | +87,50% | -15,00% | 91,98 $ | 6/35 | +17,14% | -19,05% | DEBOLE | 5,7 | 17,5 |
| +10,00% | 119,03 $ | 29/40 | +72,50% | prezzo iniziale | 108,21 $ | 11/29 | +37,93% | -9,09% | BASSA | 8,1 | 18,4 |
| +10,00% | 119,03 $ | 29/40 | +72,50% | -5,00% | 102,80 $ | 7/29 | +24,14% | -13,64% | DEBOLE | 8,1 | 20,4 |
| +10,00% | 119,03 $ | 29/40 | +72,50% | -8,00% | 99,55 $ | 5/29 | +17,24% | -16,36% | DEBOLE | 8,1 | 20,6 |
| +10,00% | 119,03 $ | 29/40 | +72,50% | -10,00% | 97,39 $ | 3/29 | +10,34% | -18,18% | DEBOLE | 8,1 | 20,7 |
| +10,00% | 119,03 $ | 29/40 | +72,50% | -15,00% | 91,98 $ | 2/29 | +6,90% | -22,73% | DEBOLE | 8,1 | 19,5 |
| +15,00% | 124,44 $ | 21/40 | +52,50% | prezzo iniziale | 108,21 $ | 3/21 | +14,29% | -13,04% | DEBOLE | 10,1 | 22,3 |
| +15,00% | 124,44 $ | 21/40 | +52,50% | -5,00% | 102,80 $ | 1/21 | +4,76% | -17,39% | DEBOLE | 10,1 | 26,0 |
| +15,00% | 124,44 $ | 21/40 | +52,50% | -8,00% | 99,55 $ | 1/21 | +4,76% | -20,00% | DEBOLE | 10,1 | 27,0 |
| +15,00% | 124,44 $ | 21/40 | +52,50% | -10,00% | 97,39 $ | 1/21 | +4,76% | -21,74% | DEBOLE | 10,1 | 28,0 |
| +15,00% | 124,44 $ | 21/40 | +52,50% | -15,00% | 91,98 $ | 1/21 | +4,76% | -26,09% | DEBOLE | 10,1 | 28,0 |
| +20,00% | 129,85 $ | 15/40 | +37,50% | prezzo iniziale | 108,21 $ | 1/15 | +6,67% | -16,67% | DEBOLE | 16,1 | 30,0 |
| +20,00% | 129,85 $ | 15/40 | +37,50% | -5,00% | 102,80 $ | 0/15 | 0,00% | -20,83% | DEBOLE | 16,1 | n/d |
| +20,00% | 129,85 $ | 15/40 | +37,50% | -8,00% | 99,55 $ | 0/15 | 0,00% | -23,33% | DEBOLE | 16,1 | n/d |
| +20,00% | 129,85 $ | 15/40 | +37,50% | -10,00% | 97,39 $ | 0/15 | 0,00% | -25,00% | DEBOLE | 16,1 | n/d |
| +20,00% | 129,85 $ | 15/40 | +37,50% | -15,00% | 91,98 $ | 0/15 | 0,00% | -29,17% | DEBOLE | 16,1 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 24 prima sono scesi a -5,00%. Tra quei 24, 12 poi sono rimbalzati fino a +10,00%. Percentuale: +50,00% (12/24). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.
- DOGE: su 40 casi simili, 31 prima sono saliti a +10,00%. Tra quei 31, 3 poi sono scaricati a -5,00%. Percentuale: +9,68% (3/31). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,08046 $ | 24/40 | +60,00% | +5,00% | 0,08892 $ | 17/24 | +70,83% | +10,53% | ALTA | 4,8 | 10,9 |
| -5,00% | 0,08046 $ | 24/40 | +60,00% | +10,00% | 0,09316 $ | 12/24 | +50,00% | +15,79% | MEDIA | 4,8 | 10,7 |
| -5,00% | 0,08046 $ | 24/40 | +60,00% | +15,00% | 0,09739 $ | 11/24 | +45,83% | +21,05% | BASSA | 4,8 | 13,5 |
| -5,00% | 0,08046 $ | 24/40 | +60,00% | +20,00% | 0,10163 $ | 10/24 | +41,67% | +26,32% | BASSA | 4,8 | 17,3 |
| -8,00% | 0,07791 $ | 17/40 | +42,50% | +5,00% | 0,08892 $ | 11/17 | +64,71% | +14,13% | MEDIA | 6,0 | 12,8 |
| -8,00% | 0,07791 $ | 17/40 | +42,50% | +10,00% | 0,09316 $ | 7/17 | +41,18% | +19,57% | BASSA | 6,0 | 13,0 |
| -8,00% | 0,07791 $ | 17/40 | +42,50% | +15,00% | 0,09739 $ | 6/17 | +35,29% | +25,00% | BASSA | 6,0 | 18,2 |
| -8,00% | 0,07791 $ | 17/40 | +42,50% | +20,00% | 0,10163 $ | 5/17 | +29,41% | +30,43% | DEBOLE | 6,0 | 24,4 |
| -10,00% | 0,07622 $ | 12/40 | +30,00% | +5,00% | 0,08892 $ | 6/12 | +50,00% | +16,67% | MEDIA | 9,2 | 16,0 |
| -10,00% | 0,07622 $ | 12/40 | +30,00% | +10,00% | 0,09316 $ | 2/12 | +16,67% | +22,22% | DEBOLE | 9,2 | 16,0 |
| -10,00% | 0,07622 $ | 12/40 | +30,00% | +15,00% | 0,09739 $ | 2/12 | +16,67% | +27,78% | DEBOLE | 9,2 | 16,0 |
| -10,00% | 0,07622 $ | 12/40 | +30,00% | +20,00% | 0,10163 $ | 2/12 | +16,67% | +33,33% | DEBOLE | 9,2 | 20,5 |
| -15,00% | 0,07199 $ | 9/40 | +22,50% | +5,00% | 0,08892 $ | 2/9 | +22,22% | +23,53% | DEBOLE | 13,4 | 20,5 |
| -15,00% | 0,07199 $ | 9/40 | +22,50% | +10,00% | 0,09316 $ | 0/9 | 0,00% | +29,41% | DEBOLE | 13,4 | n/d |
| -15,00% | 0,07199 $ | 9/40 | +22,50% | +15,00% | 0,09739 $ | 0/9 | 0,00% | +35,29% | DEBOLE | 13,4 | n/d |
| -15,00% | 0,07199 $ | 9/40 | +22,50% | +20,00% | 0,10163 $ | 0/9 | 0,00% | +41,18% | DEBOLE | 13,4 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,08892 $ | 38/40 | +95,00% | prezzo iniziale | 0,08469 $ | 13/38 | +34,21% | -4,76% | DEBOLE | 5,6 | 11,0 |
| +5,00% | 0,08892 $ | 38/40 | +95,00% | -5,00% | 0,08046 $ | 9/38 | +23,68% | -9,52% | DEBOLE | 5,6 | 13,8 |
| +5,00% | 0,08892 $ | 38/40 | +95,00% | -8,00% | 0,07791 $ | 7/38 | +18,42% | -12,38% | DEBOLE | 5,6 | 13,7 |
| +5,00% | 0,08892 $ | 38/40 | +95,00% | -10,00% | 0,07622 $ | 6/38 | +15,79% | -14,29% | DEBOLE | 5,6 | 14,7 |
| +5,00% | 0,08892 $ | 38/40 | +95,00% | -15,00% | 0,07199 $ | 5/38 | +13,16% | -19,05% | DEBOLE | 5,6 | 15,4 |
| +10,00% | 0,09316 $ | 31/40 | +77,50% | prezzo iniziale | 0,08469 $ | 5/31 | +16,13% | -9,09% | DEBOLE | 6,4 | 16,2 |
| +10,00% | 0,09316 $ | 31/40 | +77,50% | -5,00% | 0,08046 $ | 3/31 | +9,68% | -13,64% | DEBOLE | 6,4 | 16,0 |
| +10,00% | 0,09316 $ | 31/40 | +77,50% | -8,00% | 0,07791 $ | 1/31 | +3,23% | -16,36% | DEBOLE | 6,4 | 7,0 |
| +10,00% | 0,09316 $ | 31/40 | +77,50% | -10,00% | 0,07622 $ | 1/31 | +3,23% | -18,18% | DEBOLE | 6,4 | 7,0 |
| +10,00% | 0,09316 $ | 31/40 | +77,50% | -15,00% | 0,07199 $ | 1/31 | +3,23% | -22,73% | DEBOLE | 6,4 | 11,0 |
| +15,00% | 0,09739 $ | 26/40 | +65,00% | prezzo iniziale | 0,08469 $ | 1/26 | +3,85% | -13,04% | DEBOLE | 8,8 | 18,0 |
| +15,00% | 0,09739 $ | 26/40 | +65,00% | -5,00% | 0,08046 $ | 0/26 | 0,00% | -17,39% | DEBOLE | 8,8 | n/d |
| +15,00% | 0,09739 $ | 26/40 | +65,00% | -8,00% | 0,07791 $ | 0/26 | 0,00% | -20,00% | DEBOLE | 8,8 | n/d |
| +15,00% | 0,09739 $ | 26/40 | +65,00% | -10,00% | 0,07622 $ | 0/26 | 0,00% | -21,74% | DEBOLE | 8,8 | n/d |
| +15,00% | 0,09739 $ | 26/40 | +65,00% | -15,00% | 0,07199 $ | 0/26 | 0,00% | -26,09% | DEBOLE | 8,8 | n/d |
| +20,00% | 0,10163 $ | 20/40 | +50,00% | prezzo iniziale | 0,08469 $ | 0/20 | 0,00% | -16,67% | DEBOLE | 12,3 | n/d |
| +20,00% | 0,10163 $ | 20/40 | +50,00% | -5,00% | 0,08046 $ | 0/20 | 0,00% | -20,83% | DEBOLE | 12,3 | n/d |
| +20,00% | 0,10163 $ | 20/40 | +50,00% | -8,00% | 0,07791 $ | 0/20 | 0,00% | -23,33% | DEBOLE | 12,3 | n/d |
| +20,00% | 0,10163 $ | 20/40 | +50,00% | -10,00% | 0,07622 $ | 0/20 | 0,00% | -25,00% | DEBOLE | 12,3 | n/d |
| +20,00% | 0,10163 $ | 20/40 | +50,00% | -15,00% | 0,07199 $ | 0/20 | 0,00% | -29,17% | DEBOLE | 12,3 | n/d |

---
