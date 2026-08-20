# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-08-20 07:31:39 CEST**  
UTC: **2026-08-20 05:31:39 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 66.087 $ | 76.521 $ | +50,00% | +15,79% | rimbalzo possibile | 76.521 $ | 66.087 $ | +21,43% | -13,64% | spike storicamente più resistente |
| SOL | 80,63 $ | 93,36 $ | +38,10% | +15,79% | rimbalzo debole | 93,36 $ | 80,63 $ | +19,23% | -13,64% | spike storicamente più resistente |
| DOGE | 0,07086 $ | 0,08205 $ | +56,67% | +15,79% | rimbalzo possibile | 0,08205 $ | 0,07086 $ | +10,71% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 18 prima sono scesi a -5,00%. Tra quei 18, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +50,00% (9/18). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.
- BTC: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 6 poi sono scaricati a -5,00%. Percentuale: +21,43% (6/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 66.087 $ | 18/40 | +45,00% | +5,00% | 73.043 $ | 11/18 | +61,11% | +10,53% | MEDIA | 10,2 | 13,5 |
| -5,00% | 66.087 $ | 18/40 | +45,00% | +10,00% | 76.521 $ | 9/18 | +50,00% | +15,79% | MEDIA | 10,2 | 13,6 |
| -5,00% | 66.087 $ | 18/40 | +45,00% | +15,00% | 80.000 $ | 6/18 | +33,33% | +21,05% | DEBOLE | 10,2 | 17,2 |
| -5,00% | 66.087 $ | 18/40 | +45,00% | +20,00% | 83.478 $ | 6/18 | +33,33% | +26,32% | DEBOLE | 10,2 | 18,3 |
| -8,00% | 64.000 $ | 15/40 | +37,50% | +5,00% | 73.043 $ | 7/15 | +46,67% | +14,13% | BASSA | 13,9 | 16,0 |
| -8,00% | 64.000 $ | 15/40 | +37,50% | +10,00% | 76.521 $ | 5/15 | +33,33% | +19,57% | DEBOLE | 13,9 | 16,0 |
| -8,00% | 64.000 $ | 15/40 | +37,50% | +15,00% | 80.000 $ | 4/15 | +26,67% | +25,00% | DEBOLE | 13,9 | 19,2 |
| -8,00% | 64.000 $ | 15/40 | +37,50% | +20,00% | 83.478 $ | 4/15 | +26,67% | +30,43% | DEBOLE | 13,9 | 21,0 |
| -10,00% | 62.608 $ | 14/40 | +35,00% | +5,00% | 73.043 $ | 5/14 | +35,71% | +16,67% | BASSA | 16,5 | 19,4 |
| -10,00% | 62.608 $ | 14/40 | +35,00% | +10,00% | 76.521 $ | 3/14 | +21,43% | +22,22% | DEBOLE | 16,5 | 20,0 |
| -10,00% | 62.608 $ | 14/40 | +35,00% | +15,00% | 80.000 $ | 3/14 | +21,43% | +27,78% | DEBOLE | 16,5 | 20,0 |
| -10,00% | 62.608 $ | 14/40 | +35,00% | +20,00% | 83.478 $ | 3/14 | +21,43% | +33,33% | DEBOLE | 16,5 | 22,0 |
| -15,00% | 59.130 $ | 4/40 | +10,00% | +5,00% | 73.043 $ | 0/4 | 0,00% | +23,53% | DEBOLE | 26,0 | n/d |
| -15,00% | 59.130 $ | 4/40 | +10,00% | +10,00% | 76.521 $ | 0/4 | 0,00% | +29,41% | DEBOLE | 26,0 | n/d |
| -15,00% | 59.130 $ | 4/40 | +10,00% | +15,00% | 80.000 $ | 0/4 | 0,00% | +35,29% | DEBOLE | 26,0 | n/d |
| -15,00% | 59.130 $ | 4/40 | +10,00% | +20,00% | 83.478 $ | 0/4 | 0,00% | +41,18% | DEBOLE | 26,0 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 73.043 $ | 39/40 | +97,50% | prezzo iniziale | 69.565 $ | 19/39 | +48,72% | -4,76% | BASSA | 9,3 | 19,1 |
| +5,00% | 73.043 $ | 39/40 | +97,50% | -5,00% | 66.087 $ | 10/39 | +25,64% | -9,52% | DEBOLE | 9,3 | 19,6 |
| +5,00% | 73.043 $ | 39/40 | +97,50% | -8,00% | 64.000 $ | 10/39 | +25,64% | -12,38% | DEBOLE | 9,3 | 20,6 |
| +5,00% | 73.043 $ | 39/40 | +97,50% | -10,00% | 62.608 $ | 10/39 | +25,64% | -14,29% | DEBOLE | 9,3 | 21,8 |
| +5,00% | 73.043 $ | 39/40 | +97,50% | -15,00% | 59.130 $ | 4/39 | +10,26% | -19,05% | DEBOLE | 9,3 | 26,0 |
| +10,00% | 76.521 $ | 28/40 | +70,00% | prezzo iniziale | 69.565 $ | 11/28 | +39,29% | -9,09% | BASSA | 9,4 | 17,9 |
| +10,00% | 76.521 $ | 28/40 | +70,00% | -5,00% | 66.087 $ | 6/28 | +21,43% | -13,64% | DEBOLE | 9,4 | 17,0 |
| +10,00% | 76.521 $ | 28/40 | +70,00% | -8,00% | 64.000 $ | 6/28 | +21,43% | -16,36% | DEBOLE | 9,4 | 18,3 |
| +10,00% | 76.521 $ | 28/40 | +70,00% | -10,00% | 62.608 $ | 6/28 | +21,43% | -18,18% | DEBOLE | 9,4 | 19,0 |
| +10,00% | 76.521 $ | 28/40 | +70,00% | -15,00% | 59.130 $ | 3/28 | +10,71% | -22,73% | DEBOLE | 9,4 | 27,0 |
| +15,00% | 80.000 $ | 23/40 | +57,50% | prezzo iniziale | 69.565 $ | 6/23 | +26,09% | -13,04% | DEBOLE | 10,3 | 18,3 |
| +15,00% | 80.000 $ | 23/40 | +57,50% | -5,00% | 66.087 $ | 4/23 | +17,39% | -17,39% | DEBOLE | 10,3 | 16,8 |
| +15,00% | 80.000 $ | 23/40 | +57,50% | -8,00% | 64.000 $ | 4/23 | +17,39% | -20,00% | DEBOLE | 10,3 | 16,8 |
| +15,00% | 80.000 $ | 23/40 | +57,50% | -10,00% | 62.608 $ | 4/23 | +17,39% | -21,74% | DEBOLE | 10,3 | 16,8 |
| +15,00% | 80.000 $ | 23/40 | +57,50% | -15,00% | 59.130 $ | 3/23 | +13,04% | -26,09% | DEBOLE | 10,3 | 27,0 |
| +20,00% | 83.478 $ | 18/40 | +45,00% | prezzo iniziale | 69.565 $ | 4/18 | +22,22% | -16,67% | DEBOLE | 10,9 | 17,5 |
| +20,00% | 83.478 $ | 18/40 | +45,00% | -5,00% | 66.087 $ | 3/18 | +16,67% | -20,83% | DEBOLE | 10,9 | 15,3 |
| +20,00% | 83.478 $ | 18/40 | +45,00% | -8,00% | 64.000 $ | 3/18 | +16,67% | -23,33% | DEBOLE | 10,9 | 15,3 |
| +20,00% | 83.478 $ | 18/40 | +45,00% | -10,00% | 62.608 $ | 3/18 | +16,67% | -25,00% | DEBOLE | 10,9 | 15,3 |
| +20,00% | 83.478 $ | 18/40 | +45,00% | -15,00% | 59.130 $ | 2/18 | +11,11% | -29,17% | DEBOLE | 10,9 | 26,5 |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 21 prima sono scesi a -5,00%. Tra quei 21, 8 poi sono rimbalzati fino a +10,00%. Percentuale: +38,10% (8/21). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- SOL: su 40 casi simili, 26 prima sono saliti a +10,00%. Tra quei 26, 5 poi sono scaricati a -5,00%. Percentuale: +19,23% (5/26). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 80,63 $ | 21/40 | +52,50% | +5,00% | 89,11 $ | 9/21 | +42,86% | +10,53% | BASSA | 12,1 | 13,8 |
| -5,00% | 80,63 $ | 21/40 | +52,50% | +10,00% | 93,36 $ | 8/21 | +38,10% | +15,79% | BASSA | 12,1 | 15,1 |
| -5,00% | 80,63 $ | 21/40 | +52,50% | +15,00% | 97,60 $ | 5/21 | +23,81% | +21,05% | DEBOLE | 12,1 | 16,0 |
| -5,00% | 80,63 $ | 21/40 | +52,50% | +20,00% | 101,84 $ | 4/21 | +19,05% | +26,32% | DEBOLE | 12,1 | 16,2 |
| -8,00% | 78,08 $ | 14/40 | +35,00% | +5,00% | 89,11 $ | 5/14 | +35,71% | +14,13% | BASSA | 12,6 | 11,8 |
| -8,00% | 78,08 $ | 14/40 | +35,00% | +10,00% | 93,36 $ | 5/14 | +35,71% | +19,57% | BASSA | 12,6 | 14,2 |
| -8,00% | 78,08 $ | 14/40 | +35,00% | +15,00% | 97,60 $ | 2/14 | +14,29% | +25,00% | DEBOLE | 12,6 | 14,5 |
| -8,00% | 78,08 $ | 14/40 | +35,00% | +20,00% | 101,84 $ | 2/14 | +14,29% | +30,43% | DEBOLE | 12,6 | 15,5 |
| -10,00% | 76,38 $ | 9/40 | +22,50% | +5,00% | 89,11 $ | 0/9 | 0,00% | +16,67% | DEBOLE | 17,7 | n/d |
| -10,00% | 76,38 $ | 9/40 | +22,50% | +10,00% | 93,36 $ | 0/9 | 0,00% | +22,22% | DEBOLE | 17,7 | n/d |
| -10,00% | 76,38 $ | 9/40 | +22,50% | +15,00% | 97,60 $ | 0/9 | 0,00% | +27,78% | DEBOLE | 17,7 | n/d |
| -10,00% | 76,38 $ | 9/40 | +22,50% | +20,00% | 101,84 $ | 0/9 | 0,00% | +33,33% | DEBOLE | 17,7 | n/d |
| -15,00% | 72,14 $ | 3/40 | +7,50% | +5,00% | 89,11 $ | 0/3 | 0,00% | +23,53% | DEBOLE | 18,7 | n/d |
| -15,00% | 72,14 $ | 3/40 | +7,50% | +10,00% | 93,36 $ | 0/3 | 0,00% | +29,41% | DEBOLE | 18,7 | n/d |
| -15,00% | 72,14 $ | 3/40 | +7,50% | +15,00% | 97,60 $ | 0/3 | 0,00% | +35,29% | DEBOLE | 18,7 | n/d |
| -15,00% | 72,14 $ | 3/40 | +7,50% | +20,00% | 101,84 $ | 0/3 | 0,00% | +41,18% | DEBOLE | 18,7 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 89,11 $ | 35/40 | +87,50% | prezzo iniziale | 84,87 $ | 20/35 | +57,14% | -4,76% | MEDIA | 6,3 | 14,4 |
| +5,00% | 89,11 $ | 35/40 | +87,50% | -5,00% | 80,63 $ | 12/35 | +34,29% | -9,52% | DEBOLE | 6,3 | 17,5 |
| +5,00% | 89,11 $ | 35/40 | +87,50% | -8,00% | 78,08 $ | 7/35 | +20,00% | -12,38% | DEBOLE | 6,3 | 16,6 |
| +5,00% | 89,11 $ | 35/40 | +87,50% | -10,00% | 76,38 $ | 7/35 | +20,00% | -14,29% | DEBOLE | 6,3 | 18,3 |
| +5,00% | 89,11 $ | 35/40 | +87,50% | -15,00% | 72,14 $ | 2/35 | +5,71% | -19,05% | DEBOLE | 6,3 | 17,5 |
| +10,00% | 93,36 $ | 26/40 | +65,00% | prezzo iniziale | 84,87 $ | 9/26 | +34,62% | -9,09% | DEBOLE | 9,9 | 14,9 |
| +10,00% | 93,36 $ | 26/40 | +65,00% | -5,00% | 80,63 $ | 5/26 | +19,23% | -13,64% | DEBOLE | 9,9 | 14,0 |
| +10,00% | 93,36 $ | 26/40 | +65,00% | -8,00% | 78,08 $ | 4/26 | +15,38% | -16,36% | DEBOLE | 9,9 | 16,0 |
| +10,00% | 93,36 $ | 26/40 | +65,00% | -10,00% | 76,38 $ | 4/26 | +15,38% | -18,18% | DEBOLE | 9,9 | 18,2 |
| +10,00% | 93,36 $ | 26/40 | +65,00% | -15,00% | 72,14 $ | 0/26 | 0,00% | -22,73% | DEBOLE | 9,9 | n/d |
| +15,00% | 97,60 $ | 17/40 | +42,50% | prezzo iniziale | 84,87 $ | 3/17 | +17,65% | -13,04% | DEBOLE | 10,2 | 16,3 |
| +15,00% | 97,60 $ | 17/40 | +42,50% | -5,00% | 80,63 $ | 2/17 | +11,76% | -17,39% | DEBOLE | 10,2 | 11,5 |
| +15,00% | 97,60 $ | 17/40 | +42,50% | -8,00% | 78,08 $ | 2/17 | +11,76% | -20,00% | DEBOLE | 10,2 | 11,5 |
| +15,00% | 97,60 $ | 17/40 | +42,50% | -10,00% | 76,38 $ | 2/17 | +11,76% | -21,74% | DEBOLE | 10,2 | 14,0 |
| +15,00% | 97,60 $ | 17/40 | +42,50% | -15,00% | 72,14 $ | 0/17 | 0,00% | -26,09% | DEBOLE | 10,2 | n/d |
| +20,00% | 101,84 $ | 16/40 | +40,00% | prezzo iniziale | 84,87 $ | 3/16 | +18,75% | -16,67% | DEBOLE | 12,4 | 16,3 |
| +20,00% | 101,84 $ | 16/40 | +40,00% | -5,00% | 80,63 $ | 2/16 | +12,50% | -20,83% | DEBOLE | 12,4 | 11,5 |
| +20,00% | 101,84 $ | 16/40 | +40,00% | -8,00% | 78,08 $ | 2/16 | +12,50% | -23,33% | DEBOLE | 12,4 | 11,5 |
| +20,00% | 101,84 $ | 16/40 | +40,00% | -10,00% | 76,38 $ | 2/16 | +12,50% | -25,00% | DEBOLE | 12,4 | 14,0 |
| +20,00% | 101,84 $ | 16/40 | +40,00% | -15,00% | 72,14 $ | 0/16 | 0,00% | -29,17% | DEBOLE | 12,4 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 30 prima sono scesi a -5,00%. Tra quei 30, 17 poi sono rimbalzati fino a +10,00%. Percentuale: +56,67% (17/30). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.
- DOGE: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 3 poi sono scaricati a -5,00%. Percentuale: +10,71% (3/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,07086 $ | 30/40 | +75,00% | +5,00% | 0,07832 $ | 18/30 | +60,00% | +10,53% | MEDIA | 6,5 | 13,8 |
| -5,00% | 0,07086 $ | 30/40 | +75,00% | +10,00% | 0,08205 $ | 17/30 | +56,67% | +15,79% | MEDIA | 6,5 | 16,8 |
| -5,00% | 0,07086 $ | 30/40 | +75,00% | +15,00% | 0,08578 $ | 13/30 | +43,33% | +21,05% | BASSA | 6,5 | 19,5 |
| -5,00% | 0,07086 $ | 30/40 | +75,00% | +20,00% | 0,08951 $ | 10/30 | +33,33% | +26,32% | DEBOLE | 6,5 | 19,6 |
| -8,00% | 0,06862 $ | 25/40 | +62,50% | +5,00% | 0,07832 $ | 14/25 | +56,00% | +14,13% | MEDIA | 6,8 | 13,9 |
| -8,00% | 0,06862 $ | 25/40 | +62,50% | +10,00% | 0,08205 $ | 14/25 | +56,00% | +19,57% | MEDIA | 6,8 | 17,0 |
| -8,00% | 0,06862 $ | 25/40 | +62,50% | +15,00% | 0,08578 $ | 11/25 | +44,00% | +25,00% | BASSA | 6,8 | 20,0 |
| -8,00% | 0,06862 $ | 25/40 | +62,50% | +20,00% | 0,08951 $ | 9/25 | +36,00% | +30,43% | BASSA | 6,8 | 20,0 |
| -10,00% | 0,06713 $ | 22/40 | +55,00% | +5,00% | 0,07832 $ | 10/22 | +45,45% | +16,67% | BASSA | 9,1 | 13,5 |
| -10,00% | 0,06713 $ | 22/40 | +55,00% | +10,00% | 0,08205 $ | 10/22 | +45,45% | +22,22% | BASSA | 9,1 | 17,6 |
| -10,00% | 0,06713 $ | 22/40 | +55,00% | +15,00% | 0,08578 $ | 7/22 | +31,82% | +27,78% | DEBOLE | 9,1 | 19,3 |
| -10,00% | 0,06713 $ | 22/40 | +55,00% | +20,00% | 0,08951 $ | 6/22 | +27,27% | +33,33% | DEBOLE | 9,1 | 19,2 |
| -15,00% | 0,06340 $ | 14/40 | +35,00% | +5,00% | 0,07832 $ | 4/14 | +28,57% | +23,53% | DEBOLE | 13,7 | 16,8 |
| -15,00% | 0,06340 $ | 14/40 | +35,00% | +10,00% | 0,08205 $ | 4/14 | +28,57% | +29,41% | DEBOLE | 13,7 | 19,5 |
| -15,00% | 0,06340 $ | 14/40 | +35,00% | +15,00% | 0,08578 $ | 3/14 | +21,43% | +35,29% | DEBOLE | 13,7 | 21,0 |
| -15,00% | 0,06340 $ | 14/40 | +35,00% | +20,00% | 0,08951 $ | 2/14 | +14,29% | +41,18% | DEBOLE | 13,7 | 18,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07832 $ | 31/40 | +77,50% | prezzo iniziale | 0,07459 $ | 14/31 | +45,16% | -4,76% | BASSA | 9,0 | 14,7 |
| +5,00% | 0,07832 $ | 31/40 | +77,50% | -5,00% | 0,07086 $ | 8/31 | +25,81% | -9,52% | DEBOLE | 9,0 | 18,0 |
| +5,00% | 0,07832 $ | 31/40 | +77,50% | -8,00% | 0,06862 $ | 4/31 | +12,90% | -12,38% | DEBOLE | 9,0 | 19,0 |
| +5,00% | 0,07832 $ | 31/40 | +77,50% | -10,00% | 0,06713 $ | 3/31 | +9,68% | -14,29% | DEBOLE | 9,0 | 24,7 |
| +5,00% | 0,07832 $ | 31/40 | +77,50% | -15,00% | 0,06340 $ | 1/31 | +3,23% | -19,05% | DEBOLE | 9,0 | 22,0 |
| +10,00% | 0,08205 $ | 28/40 | +70,00% | prezzo iniziale | 0,07459 $ | 8/28 | +28,57% | -9,09% | DEBOLE | 12,3 | 18,0 |
| +10,00% | 0,08205 $ | 28/40 | +70,00% | -5,00% | 0,07086 $ | 3/28 | +10,71% | -13,64% | DEBOLE | 12,3 | 23,7 |
| +10,00% | 0,08205 $ | 28/40 | +70,00% | -8,00% | 0,06862 $ | 2/28 | +7,14% | -16,36% | DEBOLE | 12,3 | 21,0 |
| +10,00% | 0,08205 $ | 28/40 | +70,00% | -10,00% | 0,06713 $ | 1/28 | +3,57% | -18,18% | DEBOLE | 12,3 | 28,0 |
| +10,00% | 0,08205 $ | 28/40 | +70,00% | -15,00% | 0,06340 $ | 0/28 | 0,00% | -22,73% | DEBOLE | 12,3 | n/d |
| +15,00% | 0,08578 $ | 24/40 | +60,00% | prezzo iniziale | 0,07459 $ | 3/24 | +12,50% | -13,04% | DEBOLE | 14,5 | 26,0 |
| +15,00% | 0,08578 $ | 24/40 | +60,00% | -5,00% | 0,07086 $ | 2/24 | +8,33% | -17,39% | DEBOLE | 14,5 | 27,5 |
| +15,00% | 0,08578 $ | 24/40 | +60,00% | -8,00% | 0,06862 $ | 1/24 | +4,17% | -20,00% | DEBOLE | 14,5 | 26,0 |
| +15,00% | 0,08578 $ | 24/40 | +60,00% | -10,00% | 0,06713 $ | 1/24 | +4,17% | -21,74% | DEBOLE | 14,5 | 28,0 |
| +15,00% | 0,08578 $ | 24/40 | +60,00% | -15,00% | 0,06340 $ | 0/24 | 0,00% | -26,09% | DEBOLE | 14,5 | n/d |
| +20,00% | 0,08951 $ | 19/40 | +47,50% | prezzo iniziale | 0,07459 $ | 0/19 | 0,00% | -16,67% | DEBOLE | 15,7 | n/d |
| +20,00% | 0,08951 $ | 19/40 | +47,50% | -5,00% | 0,07086 $ | 0/19 | 0,00% | -20,83% | DEBOLE | 15,7 | n/d |
| +20,00% | 0,08951 $ | 19/40 | +47,50% | -8,00% | 0,06862 $ | 0/19 | 0,00% | -23,33% | DEBOLE | 15,7 | n/d |
| +20,00% | 0,08951 $ | 19/40 | +47,50% | -10,00% | 0,06713 $ | 0/19 | 0,00% | -25,00% | DEBOLE | 15,7 | n/d |
| +20,00% | 0,08951 $ | 19/40 | +47,50% | -15,00% | 0,06340 $ | 0/19 | 0,00% | -29,17% | DEBOLE | 15,7 | n/d |

---
