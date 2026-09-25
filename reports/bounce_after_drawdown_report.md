# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-09-25 07:31:42 CEST**  
UTC: **2026-09-25 05:31:42 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 79.943 $ | 92.566 $ | +50,00% | +15,79% | rimbalzo possibile | 92.566 $ | 79.943 $ | +9,38% | -13,64% | spike storicamente più resistente |
| SOL | 110,60 $ | 128,06 $ | +33,33% | +15,79% | rimbalzo poco frequente | 128,06 $ | 110,60 $ | +23,08% | -13,64% | spike storicamente più resistente |
| DOGE | 0,09031 $ | 0,10457 $ | +16,67% | +15,79% | rimbalzo poco frequente | 0,10457 $ | 0,09031 $ | +17,65% | -13,64% | spike storicamente più resistente |

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
- BTC: su 40 casi simili, 32 prima sono saliti a +10,00%. Tra quei 32, 3 poi sono scaricati a -5,00%. Percentuale: +9,38% (3/32). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 79.943 $ | 18/40 | +45,00% | +5,00% | 88.359 $ | 10/18 | +55,56% | +10,53% | MEDIA | 6,3 | 14,3 |
| -5,00% | 79.943 $ | 18/40 | +45,00% | +10,00% | 92.566 $ | 9/18 | +50,00% | +15,79% | MEDIA | 6,3 | 13,6 |
| -5,00% | 79.943 $ | 18/40 | +45,00% | +15,00% | 96.774 $ | 8/18 | +44,44% | +21,05% | BASSA | 6,3 | 17,0 |
| -5,00% | 79.943 $ | 18/40 | +45,00% | +20,00% | 100.981 $ | 6/18 | +33,33% | +26,32% | DEBOLE | 6,3 | 14,8 |
| -8,00% | 77.419 $ | 16/40 | +40,00% | +5,00% | 88.359 $ | 8/16 | +50,00% | +14,13% | MEDIA | 9,2 | 16,0 |
| -8,00% | 77.419 $ | 16/40 | +40,00% | +10,00% | 92.566 $ | 7/16 | +43,75% | +19,57% | BASSA | 9,2 | 15,3 |
| -8,00% | 77.419 $ | 16/40 | +40,00% | +15,00% | 96.774 $ | 6/16 | +37,50% | +25,00% | BASSA | 9,2 | 18,7 |
| -8,00% | 77.419 $ | 16/40 | +40,00% | +20,00% | 100.981 $ | 4/16 | +25,00% | +30,43% | DEBOLE | 9,2 | 15,0 |
| -10,00% | 75.736 $ | 13/40 | +32,50% | +5,00% | 88.359 $ | 5/13 | +38,46% | +16,67% | BASSA | 8,6 | 15,0 |
| -10,00% | 75.736 $ | 13/40 | +32,50% | +10,00% | 92.566 $ | 5/13 | +38,46% | +22,22% | BASSA | 8,6 | 15,6 |
| -10,00% | 75.736 $ | 13/40 | +32,50% | +15,00% | 96.774 $ | 4/13 | +30,77% | +27,78% | DEBOLE | 8,6 | 20,5 |
| -10,00% | 75.736 $ | 13/40 | +32,50% | +20,00% | 100.981 $ | 2/13 | +15,38% | +33,33% | DEBOLE | 8,6 | 15,0 |
| -15,00% | 71.528 $ | 11/40 | +27,50% | +5,00% | 88.359 $ | 3/11 | +27,27% | +23,53% | DEBOLE | 12,1 | 16,3 |
| -15,00% | 71.528 $ | 11/40 | +27,50% | +10,00% | 92.566 $ | 3/11 | +27,27% | +29,41% | DEBOLE | 12,1 | 17,0 |
| -15,00% | 71.528 $ | 11/40 | +27,50% | +15,00% | 96.774 $ | 2/11 | +18,18% | +35,29% | DEBOLE | 12,1 | 24,0 |
| -15,00% | 71.528 $ | 11/40 | +27,50% | +20,00% | 100.981 $ | 1/11 | +9,09% | +41,18% | DEBOLE | 12,1 | 20,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 88.359 $ | 36/40 | +90,00% | prezzo iniziale | 84.151 $ | 13/36 | +36,11% | -4,76% | BASSA | 5,2 | 9,2 |
| +5,00% | 88.359 $ | 36/40 | +90,00% | -5,00% | 79.943 $ | 7/36 | +19,44% | -9,52% | DEBOLE | 5,2 | 13,6 |
| +5,00% | 88.359 $ | 36/40 | +90,00% | -8,00% | 77.419 $ | 7/36 | +19,44% | -12,38% | DEBOLE | 5,2 | 16,6 |
| +5,00% | 88.359 $ | 36/40 | +90,00% | -10,00% | 75.736 $ | 5/36 | +13,89% | -14,29% | DEBOLE | 5,2 | 12,8 |
| +5,00% | 88.359 $ | 36/40 | +90,00% | -15,00% | 71.528 $ | 5/36 | +13,89% | -19,05% | DEBOLE | 5,2 | 18,0 |
| +10,00% | 92.566 $ | 32/40 | +80,00% | prezzo iniziale | 84.151 $ | 8/32 | +25,00% | -9,09% | DEBOLE | 7,8 | 13,1 |
| +10,00% | 92.566 $ | 32/40 | +80,00% | -5,00% | 79.943 $ | 3/32 | +9,38% | -13,64% | DEBOLE | 7,8 | 13,3 |
| +10,00% | 92.566 $ | 32/40 | +80,00% | -8,00% | 77.419 $ | 3/32 | +9,38% | -16,36% | DEBOLE | 7,8 | 13,3 |
| +10,00% | 92.566 $ | 32/40 | +80,00% | -10,00% | 75.736 $ | 3/32 | +9,38% | -18,18% | DEBOLE | 7,8 | 13,3 |
| +10,00% | 92.566 $ | 32/40 | +80,00% | -15,00% | 71.528 $ | 3/32 | +9,38% | -22,73% | DEBOLE | 7,8 | 18,7 |
| +15,00% | 96.774 $ | 29/40 | +72,50% | prezzo iniziale | 84.151 $ | 2/29 | +6,90% | -13,04% | DEBOLE | 10,7 | 17,0 |
| +15,00% | 96.774 $ | 29/40 | +72,50% | -5,00% | 79.943 $ | 1/29 | +3,45% | -17,39% | DEBOLE | 10,7 | 21,0 |
| +15,00% | 96.774 $ | 29/40 | +72,50% | -8,00% | 77.419 $ | 1/29 | +3,45% | -20,00% | DEBOLE | 10,7 | 21,0 |
| +15,00% | 96.774 $ | 29/40 | +72,50% | -10,00% | 75.736 $ | 1/29 | +3,45% | -21,74% | DEBOLE | 10,7 | 21,0 |
| +15,00% | 96.774 $ | 29/40 | +72,50% | -15,00% | 71.528 $ | 1/29 | +3,45% | -26,09% | DEBOLE | 10,7 | 21,0 |
| +20,00% | 100.981 $ | 25/40 | +62,50% | prezzo iniziale | 84.151 $ | 1/25 | +4,00% | -16,67% | DEBOLE | 11,4 | 21,0 |
| +20,00% | 100.981 $ | 25/40 | +62,50% | -5,00% | 79.943 $ | 1/25 | +4,00% | -20,83% | DEBOLE | 11,4 | 21,0 |
| +20,00% | 100.981 $ | 25/40 | +62,50% | -8,00% | 77.419 $ | 1/25 | +4,00% | -23,33% | DEBOLE | 11,4 | 21,0 |
| +20,00% | 100.981 $ | 25/40 | +62,50% | -10,00% | 75.736 $ | 1/25 | +4,00% | -25,00% | DEBOLE | 11,4 | 21,0 |
| +20,00% | 100.981 $ | 25/40 | +62,50% | -15,00% | 71.528 $ | 1/25 | +4,00% | -29,17% | DEBOLE | 11,4 | 21,0 |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 24 prima sono scesi a -5,00%. Tra quei 24, 8 poi sono rimbalzati fino a +10,00%. Percentuale: +33,33% (8/24). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 26 prima sono saliti a +10,00%. Tra quei 26, 6 poi sono scaricati a -5,00%. Percentuale: +23,08% (6/26). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 110,60 $ | 24/40 | +60,00% | +5,00% | 122,24 $ | 9/24 | +37,50% | +10,53% | BASSA | 6,3 | 14,4 |
| -5,00% | 110,60 $ | 24/40 | +60,00% | +10,00% | 128,06 $ | 8/24 | +33,33% | +15,79% | DEBOLE | 6,3 | 13,9 |
| -5,00% | 110,60 $ | 24/40 | +60,00% | +15,00% | 133,88 $ | 7/24 | +29,17% | +21,05% | DEBOLE | 6,3 | 15,6 |
| -5,00% | 110,60 $ | 24/40 | +60,00% | +20,00% | 139,70 $ | 4/24 | +16,67% | +26,32% | DEBOLE | 6,3 | 13,2 |
| -8,00% | 107,11 $ | 22/40 | +55,00% | +5,00% | 122,24 $ | 6/22 | +27,27% | +14,13% | DEBOLE | 7,7 | 15,2 |
| -8,00% | 107,11 $ | 22/40 | +55,00% | +10,00% | 128,06 $ | 6/22 | +27,27% | +19,57% | DEBOLE | 7,7 | 16,2 |
| -8,00% | 107,11 $ | 22/40 | +55,00% | +15,00% | 133,88 $ | 5/22 | +22,73% | +25,00% | DEBOLE | 7,7 | 18,6 |
| -8,00% | 107,11 $ | 22/40 | +55,00% | +20,00% | 139,70 $ | 3/22 | +13,64% | +30,43% | DEBOLE | 7,7 | 15,0 |
| -10,00% | 104,78 $ | 22/40 | +55,00% | +5,00% | 122,24 $ | 6/22 | +27,27% | +16,67% | DEBOLE | 9,4 | 15,2 |
| -10,00% | 104,78 $ | 22/40 | +55,00% | +10,00% | 128,06 $ | 6/22 | +27,27% | +22,22% | DEBOLE | 9,4 | 16,2 |
| -10,00% | 104,78 $ | 22/40 | +55,00% | +15,00% | 133,88 $ | 5/22 | +22,73% | +27,78% | DEBOLE | 9,4 | 18,6 |
| -10,00% | 104,78 $ | 22/40 | +55,00% | +20,00% | 139,70 $ | 3/22 | +13,64% | +33,33% | DEBOLE | 9,4 | 15,0 |
| -15,00% | 98,96 $ | 18/40 | +45,00% | +5,00% | 122,24 $ | 2/18 | +11,11% | +23,53% | DEBOLE | 13,3 | 21,0 |
| -15,00% | 98,96 $ | 18/40 | +45,00% | +10,00% | 128,06 $ | 2/18 | +11,11% | +29,41% | DEBOLE | 13,3 | 21,0 |
| -15,00% | 98,96 $ | 18/40 | +45,00% | +15,00% | 133,88 $ | 2/18 | +11,11% | +35,29% | DEBOLE | 13,3 | 22,0 |
| -15,00% | 98,96 $ | 18/40 | +45,00% | +20,00% | 139,70 $ | 1/18 | +5,56% | +41,18% | DEBOLE | 13,3 | 20,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 122,24 $ | 30/40 | +75,00% | prezzo iniziale | 116,42 $ | 16/30 | +53,33% | -4,76% | MEDIA | 4,5 | 10,2 |
| +5,00% | 122,24 $ | 30/40 | +75,00% | -5,00% | 110,60 $ | 11/30 | +36,67% | -9,52% | BASSA | 4,5 | 13,4 |
| +5,00% | 122,24 $ | 30/40 | +75,00% | -8,00% | 107,11 $ | 10/30 | +33,33% | -12,38% | DEBOLE | 4,5 | 15,5 |
| +5,00% | 122,24 $ | 30/40 | +75,00% | -10,00% | 104,78 $ | 10/30 | +33,33% | -14,29% | DEBOLE | 4,5 | 16,0 |
| +5,00% | 122,24 $ | 30/40 | +75,00% | -15,00% | 98,96 $ | 7/30 | +23,33% | -19,05% | DEBOLE | 4,5 | 19,6 |
| +10,00% | 128,06 $ | 26/40 | +65,00% | prezzo iniziale | 116,42 $ | 11/26 | +42,31% | -9,09% | BASSA | 7,2 | 16,9 |
| +10,00% | 128,06 $ | 26/40 | +65,00% | -5,00% | 110,60 $ | 6/26 | +23,08% | -13,64% | DEBOLE | 7,2 | 19,0 |
| +10,00% | 128,06 $ | 26/40 | +65,00% | -8,00% | 107,11 $ | 5/26 | +19,23% | -16,36% | DEBOLE | 7,2 | 19,2 |
| +10,00% | 128,06 $ | 26/40 | +65,00% | -10,00% | 104,78 $ | 5/26 | +19,23% | -18,18% | DEBOLE | 7,2 | 19,6 |
| +10,00% | 128,06 $ | 26/40 | +65,00% | -15,00% | 98,96 $ | 3/26 | +11,54% | -22,73% | DEBOLE | 7,2 | 19,3 |
| +15,00% | 133,88 $ | 23/40 | +57,50% | prezzo iniziale | 116,42 $ | 5/23 | +21,74% | -13,04% | DEBOLE | 9,4 | 23,4 |
| +15,00% | 133,88 $ | 23/40 | +57,50% | -5,00% | 110,60 $ | 3/23 | +13,04% | -17,39% | DEBOLE | 9,4 | 25,7 |
| +15,00% | 133,88 $ | 23/40 | +57,50% | -8,00% | 107,11 $ | 2/23 | +8,70% | -20,00% | DEBOLE | 9,4 | 28,0 |
| +15,00% | 133,88 $ | 23/40 | +57,50% | -10,00% | 104,78 $ | 2/23 | +8,70% | -21,74% | DEBOLE | 9,4 | 29,0 |
| +15,00% | 133,88 $ | 23/40 | +57,50% | -15,00% | 98,96 $ | 0/23 | 0,00% | -26,09% | DEBOLE | 9,4 | n/d |
| +20,00% | 139,70 $ | 20/40 | +50,00% | prezzo iniziale | 116,42 $ | 4/20 | +20,00% | -16,67% | DEBOLE | 9,7 | 22,8 |
| +20,00% | 139,70 $ | 20/40 | +50,00% | -5,00% | 110,60 $ | 2/20 | +10,00% | -20,83% | DEBOLE | 9,7 | 25,0 |
| +20,00% | 139,70 $ | 20/40 | +50,00% | -8,00% | 107,11 $ | 1/20 | +5,00% | -23,33% | DEBOLE | 9,7 | 28,0 |
| +20,00% | 139,70 $ | 20/40 | +50,00% | -10,00% | 104,78 $ | 1/20 | +5,00% | -25,00% | DEBOLE | 9,7 | 30,0 |
| +20,00% | 139,70 $ | 20/40 | +50,00% | -15,00% | 98,96 $ | 0/20 | 0,00% | -29,17% | DEBOLE | 9,7 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 30 prima sono scesi a -5,00%. Tra quei 30, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +16,67% (5/30). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 17 prima sono saliti a +10,00%. Tra quei 17, 3 poi sono scaricati a -5,00%. Percentuale: +17,65% (3/17). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,09031 $ | 30/40 | +75,00% | +5,00% | 0,09981 $ | 8/30 | +26,67% | +10,53% | DEBOLE | 6,2 | 14,2 |
| -5,00% | 0,09031 $ | 30/40 | +75,00% | +10,00% | 0,10457 $ | 5/30 | +16,67% | +15,79% | DEBOLE | 6,2 | 19,6 |
| -5,00% | 0,09031 $ | 30/40 | +75,00% | +15,00% | 0,10932 $ | 4/30 | +13,33% | +21,05% | DEBOLE | 6,2 | 19,0 |
| -5,00% | 0,09031 $ | 30/40 | +75,00% | +20,00% | 0,11407 $ | 2/30 | +6,67% | +26,32% | DEBOLE | 6,2 | 14,5 |
| -8,00% | 0,08746 $ | 29/40 | +72,50% | +5,00% | 0,09981 $ | 4/29 | +13,79% | +14,13% | DEBOLE | 8,2 | 18,5 |
| -8,00% | 0,08746 $ | 29/40 | +72,50% | +10,00% | 0,10457 $ | 4/29 | +13,79% | +19,57% | DEBOLE | 8,2 | 19,5 |
| -8,00% | 0,08746 $ | 29/40 | +72,50% | +15,00% | 0,10932 $ | 3/29 | +10,34% | +25,00% | DEBOLE | 8,2 | 18,3 |
| -8,00% | 0,08746 $ | 29/40 | +72,50% | +20,00% | 0,11407 $ | 2/29 | +6,90% | +30,43% | DEBOLE | 8,2 | 14,5 |
| -10,00% | 0,08555 $ | 28/40 | +70,00% | +5,00% | 0,09981 $ | 3/28 | +10,71% | +16,67% | DEBOLE | 9,1 | 21,0 |
| -10,00% | 0,08555 $ | 28/40 | +70,00% | +10,00% | 0,10457 $ | 3/28 | +10,71% | +22,22% | DEBOLE | 9,1 | 21,7 |
| -10,00% | 0,08555 $ | 28/40 | +70,00% | +15,00% | 0,10932 $ | 2/28 | +7,14% | +27,78% | DEBOLE | 9,1 | 21,0 |
| -10,00% | 0,08555 $ | 28/40 | +70,00% | +20,00% | 0,11407 $ | 1/28 | +3,57% | +33,33% | DEBOLE | 9,1 | 12,0 |
| -15,00% | 0,08080 $ | 26/40 | +65,00% | +5,00% | 0,09981 $ | 1/26 | +3,85% | +23,53% | DEBOLE | 12,4 | 25,0 |
| -15,00% | 0,08080 $ | 26/40 | +65,00% | +10,00% | 0,10457 $ | 1/26 | +3,85% | +29,41% | DEBOLE | 12,4 | 26,0 |
| -15,00% | 0,08080 $ | 26/40 | +65,00% | +15,00% | 0,10932 $ | 0/26 | 0,00% | +35,29% | DEBOLE | 12,4 | n/d |
| -15,00% | 0,08080 $ | 26/40 | +65,00% | +20,00% | 0,11407 $ | 0/26 | 0,00% | +41,18% | DEBOLE | 12,4 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,09981 $ | 25/40 | +62,50% | prezzo iniziale | 0,09506 $ | 18/25 | +72,00% | -4,76% | ALTA | 3,9 | 7,4 |
| +5,00% | 0,09981 $ | 25/40 | +62,50% | -5,00% | 0,09031 $ | 14/25 | +56,00% | -9,52% | MEDIA | 3,9 | 10,2 |
| +5,00% | 0,09981 $ | 25/40 | +62,50% | -8,00% | 0,08746 $ | 13/25 | +52,00% | -12,38% | MEDIA | 3,9 | 11,8 |
| +5,00% | 0,09981 $ | 25/40 | +62,50% | -10,00% | 0,08555 $ | 13/25 | +52,00% | -14,29% | MEDIA | 3,9 | 12,7 |
| +5,00% | 0,09981 $ | 25/40 | +62,50% | -15,00% | 0,08080 $ | 12/25 | +48,00% | -19,05% | BASSA | 3,9 | 15,8 |
| +10,00% | 0,10457 $ | 17/40 | +42,50% | prezzo iniziale | 0,09506 $ | 7/17 | +41,18% | -9,09% | BASSA | 7,9 | 10,4 |
| +10,00% | 0,10457 $ | 17/40 | +42,50% | -5,00% | 0,09031 $ | 3/17 | +17,65% | -13,64% | DEBOLE | 7,9 | 14,3 |
| +10,00% | 0,10457 $ | 17/40 | +42,50% | -8,00% | 0,08746 $ | 3/17 | +17,65% | -16,36% | DEBOLE | 7,9 | 15,7 |
| +10,00% | 0,10457 $ | 17/40 | +42,50% | -10,00% | 0,08555 $ | 3/17 | +17,65% | -18,18% | DEBOLE | 7,9 | 16,7 |
| +10,00% | 0,10457 $ | 17/40 | +42,50% | -15,00% | 0,08080 $ | 3/17 | +17,65% | -22,73% | DEBOLE | 7,9 | 19,0 |
| +15,00% | 0,10932 $ | 14/40 | +35,00% | prezzo iniziale | 0,09506 $ | 2/14 | +14,29% | -13,04% | DEBOLE | 11,4 | 23,5 |
| +15,00% | 0,10932 $ | 14/40 | +35,00% | -5,00% | 0,09031 $ | 1/14 | +7,14% | -17,39% | DEBOLE | 11,4 | 20,0 |
| +15,00% | 0,10932 $ | 14/40 | +35,00% | -8,00% | 0,08746 $ | 1/14 | +7,14% | -20,00% | DEBOLE | 11,4 | 20,0 |
| +15,00% | 0,10932 $ | 14/40 | +35,00% | -10,00% | 0,08555 $ | 1/14 | +7,14% | -21,74% | DEBOLE | 11,4 | 21,0 |
| +15,00% | 0,10932 $ | 14/40 | +35,00% | -15,00% | 0,08080 $ | 1/14 | +7,14% | -26,09% | DEBOLE | 11,4 | 21,0 |
| +20,00% | 0,11407 $ | 12/40 | +30,00% | prezzo iniziale | 0,09506 $ | 1/12 | +8,33% | -16,67% | DEBOLE | 11,5 | 17,0 |
| +20,00% | 0,11407 $ | 12/40 | +30,00% | -5,00% | 0,09031 $ | 1/12 | +8,33% | -20,83% | DEBOLE | 11,5 | 20,0 |
| +20,00% | 0,11407 $ | 12/40 | +30,00% | -8,00% | 0,08746 $ | 1/12 | +8,33% | -23,33% | DEBOLE | 11,5 | 20,0 |
| +20,00% | 0,11407 $ | 12/40 | +30,00% | -10,00% | 0,08555 $ | 1/12 | +8,33% | -25,00% | DEBOLE | 11,5 | 21,0 |
| +20,00% | 0,11407 $ | 12/40 | +30,00% | -15,00% | 0,08080 $ | 1/12 | +8,33% | -29,17% | DEBOLE | 11,5 | 21,0 |

---
