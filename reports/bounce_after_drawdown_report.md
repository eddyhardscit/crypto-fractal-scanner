# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-08-18 07:31:41 CEST**  
UTC: **2026-08-18 05:31:41 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 60.969 $ | 70.595 $ | +41,18% | +15,79% | rimbalzo debole | 70.595 $ | 60.969 $ | +12,00% | -13,64% | spike storicamente più resistente |
| SOL | 71,91 $ | 83,27 $ | +41,67% | +15,79% | rimbalzo debole | 83,27 $ | 71,91 $ | +3,45% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06627 $ | 0,07674 $ | +55,17% | +15,79% | rimbalzo possibile | 0,07674 $ | 0,06627 $ | +25,81% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 17 prima sono scesi a -5,00%. Tra quei 17, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +41,18% (7/17). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 3 poi sono scaricati a -5,00%. Percentuale: +12,00% (3/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 60.969 $ | 17/40 | +42,50% | +5,00% | 67.386 $ | 10/17 | +58,82% | +10,53% | MEDIA | 8,9 | 16,4 |
| -5,00% | 60.969 $ | 17/40 | +42,50% | +10,00% | 70.595 $ | 7/17 | +41,18% | +15,79% | BASSA | 8,9 | 15,4 |
| -5,00% | 60.969 $ | 17/40 | +42,50% | +15,00% | 73.804 $ | 7/17 | +41,18% | +21,05% | BASSA | 8,9 | 18,3 |
| -5,00% | 60.969 $ | 17/40 | +42,50% | +20,00% | 77.013 $ | 6/17 | +35,29% | +26,32% | BASSA | 8,9 | 17,3 |
| -8,00% | 59.043 $ | 11/40 | +27,50% | +5,00% | 67.386 $ | 5/11 | +45,45% | +14,13% | BASSA | 10,9 | 18,8 |
| -8,00% | 59.043 $ | 11/40 | +27,50% | +10,00% | 70.595 $ | 4/11 | +36,36% | +19,57% | BASSA | 10,9 | 18,5 |
| -8,00% | 59.043 $ | 11/40 | +27,50% | +15,00% | 73.804 $ | 4/11 | +36,36% | +25,00% | BASSA | 10,9 | 20,8 |
| -8,00% | 59.043 $ | 11/40 | +27,50% | +20,00% | 77.013 $ | 3/11 | +27,27% | +30,43% | DEBOLE | 10,9 | 18,3 |
| -10,00% | 57.760 $ | 11/40 | +27,50% | +5,00% | 67.386 $ | 5/11 | +45,45% | +16,67% | BASSA | 15,2 | 18,8 |
| -10,00% | 57.760 $ | 11/40 | +27,50% | +10,00% | 70.595 $ | 4/11 | +36,36% | +22,22% | BASSA | 15,2 | 18,5 |
| -10,00% | 57.760 $ | 11/40 | +27,50% | +15,00% | 73.804 $ | 4/11 | +36,36% | +27,78% | BASSA | 15,2 | 20,8 |
| -10,00% | 57.760 $ | 11/40 | +27,50% | +20,00% | 77.013 $ | 3/11 | +27,27% | +33,33% | DEBOLE | 15,2 | 18,3 |
| -15,00% | 54.551 $ | 5/40 | +12,50% | +5,00% | 67.386 $ | 1/5 | +20,00% | +23,53% | DEBOLE | 17,6 | 23,0 |
| -15,00% | 54.551 $ | 5/40 | +12,50% | +10,00% | 70.595 $ | 1/5 | +20,00% | +29,41% | DEBOLE | 17,6 | 24,0 |
| -15,00% | 54.551 $ | 5/40 | +12,50% | +15,00% | 73.804 $ | 1/5 | +20,00% | +35,29% | DEBOLE | 17,6 | 29,0 |
| -15,00% | 54.551 $ | 5/40 | +12,50% | +20,00% | 77.013 $ | 0/5 | 0,00% | +41,18% | DEBOLE | 17,6 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 67.386 $ | 37/40 | +92,50% | prezzo iniziale | 64.178 $ | 16/37 | +43,24% | -4,76% | BASSA | 10,1 | 22,2 |
| +5,00% | 67.386 $ | 37/40 | +92,50% | -5,00% | 60.969 $ | 7/37 | +18,92% | -9,52% | DEBOLE | 10,1 | 18,9 |
| +5,00% | 67.386 $ | 37/40 | +92,50% | -8,00% | 59.043 $ | 6/37 | +16,22% | -12,38% | DEBOLE | 10,1 | 20,0 |
| +5,00% | 67.386 $ | 37/40 | +92,50% | -10,00% | 57.760 $ | 5/37 | +13,51% | -14,29% | DEBOLE | 10,1 | 20,4 |
| +5,00% | 67.386 $ | 37/40 | +92,50% | -15,00% | 54.551 $ | 4/37 | +10,81% | -19,05% | DEBOLE | 10,1 | 20,8 |
| +10,00% | 70.595 $ | 25/40 | +62,50% | prezzo iniziale | 64.178 $ | 6/25 | +24,00% | -9,09% | DEBOLE | 11,0 | 25,0 |
| +10,00% | 70.595 $ | 25/40 | +62,50% | -5,00% | 60.969 $ | 3/25 | +12,00% | -13,64% | DEBOLE | 11,0 | 26,3 |
| +10,00% | 70.595 $ | 25/40 | +62,50% | -8,00% | 59.043 $ | 2/25 | +8,00% | -16,36% | DEBOLE | 11,0 | 25,0 |
| +10,00% | 70.595 $ | 25/40 | +62,50% | -10,00% | 57.760 $ | 1/25 | +4,00% | -18,18% | DEBOLE | 11,0 | 22,0 |
| +10,00% | 70.595 $ | 25/40 | +62,50% | -15,00% | 54.551 $ | 1/25 | +4,00% | -22,73% | DEBOLE | 11,0 | 23,0 |
| +15,00% | 73.804 $ | 23/40 | +57,50% | prezzo iniziale | 64.178 $ | 5/23 | +21,74% | -13,04% | DEBOLE | 12,8 | 24,4 |
| +15,00% | 73.804 $ | 23/40 | +57,50% | -5,00% | 60.969 $ | 2/23 | +8,70% | -17,39% | DEBOLE | 12,8 | 24,5 |
| +15,00% | 73.804 $ | 23/40 | +57,50% | -8,00% | 59.043 $ | 2/23 | +8,70% | -20,00% | DEBOLE | 12,8 | 25,0 |
| +15,00% | 73.804 $ | 23/40 | +57,50% | -10,00% | 57.760 $ | 1/23 | +4,35% | -21,74% | DEBOLE | 12,8 | 22,0 |
| +15,00% | 73.804 $ | 23/40 | +57,50% | -15,00% | 54.551 $ | 1/23 | +4,35% | -26,09% | DEBOLE | 12,8 | 23,0 |
| +20,00% | 77.013 $ | 18/40 | +45,00% | prezzo iniziale | 64.178 $ | 3/18 | +16,67% | -16,67% | DEBOLE | 12,7 | 24,7 |
| +20,00% | 77.013 $ | 18/40 | +45,00% | -5,00% | 60.969 $ | 2/18 | +11,11% | -20,83% | DEBOLE | 12,7 | 24,5 |
| +20,00% | 77.013 $ | 18/40 | +45,00% | -8,00% | 59.043 $ | 2/18 | +11,11% | -23,33% | DEBOLE | 12,7 | 25,0 |
| +20,00% | 77.013 $ | 18/40 | +45,00% | -10,00% | 57.760 $ | 1/18 | +5,56% | -25,00% | DEBOLE | 12,7 | 22,0 |
| +20,00% | 77.013 $ | 18/40 | +45,00% | -15,00% | 54.551 $ | 1/18 | +5,56% | -29,17% | DEBOLE | 12,7 | 23,0 |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 12 prima sono scesi a -5,00%. Tra quei 12, 5 poi sono rimbalzati fino a +10,00%. Percentuale: +41,67% (5/12). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- SOL: su 40 casi simili, 29 prima sono saliti a +10,00%. Tra quei 29, 1 poi sono scaricati a -5,00%. Percentuale: +3,45% (1/29). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 71,91 $ | 12/40 | +30,00% | +5,00% | 79,48 $ | 5/12 | +41,67% | +10,53% | BASSA | 11,0 | 13,8 |
| -5,00% | 71,91 $ | 12/40 | +30,00% | +10,00% | 83,27 $ | 5/12 | +41,67% | +15,79% | BASSA | 11,0 | 16,4 |
| -5,00% | 71,91 $ | 12/40 | +30,00% | +15,00% | 87,05 $ | 4/12 | +33,33% | +21,05% | DEBOLE | 11,0 | 15,0 |
| -5,00% | 71,91 $ | 12/40 | +30,00% | +20,00% | 90,84 $ | 4/12 | +33,33% | +26,32% | DEBOLE | 11,0 | 20,5 |
| -8,00% | 69,64 $ | 8/40 | +20,00% | +5,00% | 79,48 $ | 3/8 | +37,50% | +14,13% | BASSA | 10,2 | 15,3 |
| -8,00% | 69,64 $ | 8/40 | +20,00% | +10,00% | 83,27 $ | 3/8 | +37,50% | +19,57% | BASSA | 10,2 | 17,3 |
| -8,00% | 69,64 $ | 8/40 | +20,00% | +15,00% | 87,05 $ | 2/8 | +25,00% | +25,00% | DEBOLE | 10,2 | 14,5 |
| -8,00% | 69,64 $ | 8/40 | +20,00% | +20,00% | 90,84 $ | 2/8 | +25,00% | +30,43% | DEBOLE | 10,2 | 15,5 |
| -10,00% | 68,13 $ | 5/40 | +12,50% | +5,00% | 79,48 $ | 0/5 | 0,00% | +16,67% | DEBOLE | 12,4 | n/d |
| -10,00% | 68,13 $ | 5/40 | +12,50% | +10,00% | 83,27 $ | 0/5 | 0,00% | +22,22% | DEBOLE | 12,4 | n/d |
| -10,00% | 68,13 $ | 5/40 | +12,50% | +15,00% | 87,05 $ | 0/5 | 0,00% | +27,78% | DEBOLE | 12,4 | n/d |
| -10,00% | 68,13 $ | 5/40 | +12,50% | +20,00% | 90,84 $ | 0/5 | 0,00% | +33,33% | DEBOLE | 12,4 | n/d |
| -15,00% | 64,34 $ | 3/40 | +7,50% | +5,00% | 79,48 $ | 0/3 | 0,00% | +23,53% | DEBOLE | 17,7 | n/d |
| -15,00% | 64,34 $ | 3/40 | +7,50% | +10,00% | 83,27 $ | 0/3 | 0,00% | +29,41% | DEBOLE | 17,7 | n/d |
| -15,00% | 64,34 $ | 3/40 | +7,50% | +15,00% | 87,05 $ | 0/3 | 0,00% | +35,29% | DEBOLE | 17,7 | n/d |
| -15,00% | 64,34 $ | 3/40 | +7,50% | +20,00% | 90,84 $ | 0/3 | 0,00% | +41,18% | DEBOLE | 17,7 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 79,48 $ | 37/40 | +92,50% | prezzo iniziale | 75,70 $ | 11/37 | +29,73% | -4,76% | DEBOLE | 6,4 | 16,3 |
| +5,00% | 79,48 $ | 37/40 | +92,50% | -5,00% | 71,91 $ | 4/37 | +10,81% | -9,52% | DEBOLE | 6,4 | 18,5 |
| +5,00% | 79,48 $ | 37/40 | +92,50% | -8,00% | 69,64 $ | 3/37 | +8,11% | -12,38% | DEBOLE | 6,4 | 16,7 |
| +5,00% | 79,48 $ | 37/40 | +92,50% | -10,00% | 68,13 $ | 3/37 | +8,11% | -14,29% | DEBOLE | 6,4 | 17,0 |
| +5,00% | 79,48 $ | 37/40 | +92,50% | -15,00% | 64,34 $ | 1/37 | +2,70% | -19,05% | DEBOLE | 6,4 | 23,0 |
| +10,00% | 83,27 $ | 29/40 | +72,50% | prezzo iniziale | 75,70 $ | 4/29 | +13,79% | -9,09% | DEBOLE | 8,7 | 17,0 |
| +10,00% | 83,27 $ | 29/40 | +72,50% | -5,00% | 71,91 $ | 1/29 | +3,45% | -13,64% | DEBOLE | 8,7 | 2,0 |
| +10,00% | 83,27 $ | 29/40 | +72,50% | -8,00% | 69,64 $ | 1/29 | +3,45% | -16,36% | DEBOLE | 8,7 | 2,0 |
| +10,00% | 83,27 $ | 29/40 | +72,50% | -10,00% | 68,13 $ | 1/29 | +3,45% | -18,18% | DEBOLE | 8,7 | 2,0 |
| +10,00% | 83,27 $ | 29/40 | +72,50% | -15,00% | 64,34 $ | 0/29 | 0,00% | -22,73% | DEBOLE | 8,7 | n/d |
| +15,00% | 87,05 $ | 24/40 | +60,00% | prezzo iniziale | 75,70 $ | 2/24 | +8,33% | -13,04% | DEBOLE | 9,2 | 13,5 |
| +15,00% | 87,05 $ | 24/40 | +60,00% | -5,00% | 71,91 $ | 1/24 | +4,17% | -17,39% | DEBOLE | 9,2 | 2,0 |
| +15,00% | 87,05 $ | 24/40 | +60,00% | -8,00% | 69,64 $ | 1/24 | +4,17% | -20,00% | DEBOLE | 9,2 | 2,0 |
| +15,00% | 87,05 $ | 24/40 | +60,00% | -10,00% | 68,13 $ | 1/24 | +4,17% | -21,74% | DEBOLE | 9,2 | 2,0 |
| +15,00% | 87,05 $ | 24/40 | +60,00% | -15,00% | 64,34 $ | 0/24 | 0,00% | -26,09% | DEBOLE | 9,2 | n/d |
| +20,00% | 90,84 $ | 22/40 | +55,00% | prezzo iniziale | 75,70 $ | 2/22 | +9,09% | -16,67% | DEBOLE | 11,7 | 13,5 |
| +20,00% | 90,84 $ | 22/40 | +55,00% | -5,00% | 71,91 $ | 1/22 | +4,55% | -20,83% | DEBOLE | 11,7 | 2,0 |
| +20,00% | 90,84 $ | 22/40 | +55,00% | -8,00% | 69,64 $ | 1/22 | +4,55% | -23,33% | DEBOLE | 11,7 | 2,0 |
| +20,00% | 90,84 $ | 22/40 | +55,00% | -10,00% | 68,13 $ | 1/22 | +4,55% | -25,00% | DEBOLE | 11,7 | 2,0 |
| +20,00% | 90,84 $ | 22/40 | +55,00% | -15,00% | 64,34 $ | 0/22 | 0,00% | -29,17% | DEBOLE | 11,7 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 29 prima sono scesi a -5,00%. Tra quei 29, 16 poi sono rimbalzati fino a +10,00%. Percentuale: +55,17% (16/29). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.
- DOGE: su 40 casi simili, 31 prima sono saliti a +10,00%. Tra quei 31, 8 poi sono scaricati a -5,00%. Percentuale: +25,81% (8/31). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06627 $ | 29/40 | +72,50% | +5,00% | 0,07325 $ | 18/29 | +62,07% | +10,53% | MEDIA | 9,6 | 15,3 |
| -5,00% | 0,06627 $ | 29/40 | +72,50% | +10,00% | 0,07674 $ | 16/29 | +55,17% | +15,79% | MEDIA | 9,6 | 16,5 |
| -5,00% | 0,06627 $ | 29/40 | +72,50% | +15,00% | 0,08022 $ | 13/29 | +44,83% | +21,05% | BASSA | 9,6 | 21,1 |
| -5,00% | 0,06627 $ | 29/40 | +72,50% | +20,00% | 0,08371 $ | 10/29 | +34,48% | +26,32% | DEBOLE | 9,6 | 21,3 |
| -8,00% | 0,06418 $ | 21/40 | +52,50% | +5,00% | 0,07325 $ | 11/21 | +52,38% | +14,13% | MEDIA | 9,2 | 14,3 |
| -8,00% | 0,06418 $ | 21/40 | +52,50% | +10,00% | 0,07674 $ | 11/21 | +52,38% | +19,57% | MEDIA | 9,2 | 16,6 |
| -8,00% | 0,06418 $ | 21/40 | +52,50% | +15,00% | 0,08022 $ | 8/21 | +38,10% | +25,00% | BASSA | 9,2 | 21,4 |
| -8,00% | 0,06418 $ | 21/40 | +52,50% | +20,00% | 0,08371 $ | 7/21 | +33,33% | +30,43% | DEBOLE | 9,2 | 22,4 |
| -10,00% | 0,06278 $ | 15/40 | +37,50% | +5,00% | 0,07325 $ | 5/15 | +33,33% | +16,67% | DEBOLE | 11,0 | 14,8 |
| -10,00% | 0,06278 $ | 15/40 | +37,50% | +10,00% | 0,07674 $ | 5/15 | +33,33% | +22,22% | DEBOLE | 11,0 | 17,6 |
| -10,00% | 0,06278 $ | 15/40 | +37,50% | +15,00% | 0,08022 $ | 3/15 | +20,00% | +27,78% | DEBOLE | 11,0 | 19,3 |
| -10,00% | 0,06278 $ | 15/40 | +37,50% | +20,00% | 0,08371 $ | 3/15 | +20,00% | +33,33% | DEBOLE | 11,0 | 20,7 |
| -15,00% | 0,05930 $ | 8/40 | +20,00% | +5,00% | 0,07325 $ | 0/8 | 0,00% | +23,53% | DEBOLE | 16,6 | n/d |
| -15,00% | 0,05930 $ | 8/40 | +20,00% | +10,00% | 0,07674 $ | 0/8 | 0,00% | +29,41% | DEBOLE | 16,6 | n/d |
| -15,00% | 0,05930 $ | 8/40 | +20,00% | +15,00% | 0,08022 $ | 0/8 | 0,00% | +35,29% | DEBOLE | 16,6 | n/d |
| -15,00% | 0,05930 $ | 8/40 | +20,00% | +20,00% | 0,08371 $ | 0/8 | 0,00% | +41,18% | DEBOLE | 16,6 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07325 $ | 34/40 | +85,00% | prezzo iniziale | 0,06976 $ | 18/34 | +52,94% | -4,76% | MEDIA | 8,5 | 16,2 |
| +5,00% | 0,07325 $ | 34/40 | +85,00% | -5,00% | 0,06627 $ | 15/34 | +44,12% | -9,52% | BASSA | 8,5 | 18,0 |
| +5,00% | 0,07325 $ | 34/40 | +85,00% | -8,00% | 0,06418 $ | 8/34 | +23,53% | -12,38% | DEBOLE | 8,5 | 14,6 |
| +5,00% | 0,07325 $ | 34/40 | +85,00% | -10,00% | 0,06278 $ | 5/34 | +14,71% | -14,29% | DEBOLE | 8,5 | 16,8 |
| +5,00% | 0,07325 $ | 34/40 | +85,00% | -15,00% | 0,05930 $ | 3/34 | +8,82% | -19,05% | DEBOLE | 8,5 | 22,0 |
| +10,00% | 0,07674 $ | 31/40 | +77,50% | prezzo iniziale | 0,06976 $ | 12/31 | +38,71% | -9,09% | BASSA | 11,5 | 20,4 |
| +10,00% | 0,07674 $ | 31/40 | +77,50% | -5,00% | 0,06627 $ | 8/31 | +25,81% | -13,64% | DEBOLE | 11,5 | 21,4 |
| +10,00% | 0,07674 $ | 31/40 | +77,50% | -8,00% | 0,06418 $ | 4/31 | +12,90% | -16,36% | DEBOLE | 11,5 | 16,2 |
| +10,00% | 0,07674 $ | 31/40 | +77,50% | -10,00% | 0,06278 $ | 2/31 | +6,45% | -18,18% | DEBOLE | 11,5 | 19,5 |
| +10,00% | 0,07674 $ | 31/40 | +77,50% | -15,00% | 0,05930 $ | 1/31 | +3,23% | -22,73% | DEBOLE | 11,5 | 25,0 |
| +15,00% | 0,08022 $ | 26/40 | +65,00% | prezzo iniziale | 0,06976 $ | 3/26 | +11,54% | -13,04% | DEBOLE | 14,9 | 26,0 |
| +15,00% | 0,08022 $ | 26/40 | +65,00% | -5,00% | 0,06627 $ | 3/26 | +11,54% | -17,39% | DEBOLE | 14,9 | 28,3 |
| +15,00% | 0,08022 $ | 26/40 | +65,00% | -8,00% | 0,06418 $ | 1/26 | +3,85% | -20,00% | DEBOLE | 14,9 | 27,0 |
| +15,00% | 0,08022 $ | 26/40 | +65,00% | -10,00% | 0,06278 $ | 1/26 | +3,85% | -21,74% | DEBOLE | 14,9 | 28,0 |
| +15,00% | 0,08022 $ | 26/40 | +65,00% | -15,00% | 0,05930 $ | 0/26 | 0,00% | -26,09% | DEBOLE | 14,9 | n/d |
| +20,00% | 0,08371 $ | 22/40 | +55,00% | prezzo iniziale | 0,06976 $ | 1/22 | +4,55% | -16,67% | DEBOLE | 18,0 | 28,0 |
| +20,00% | 0,08371 $ | 22/40 | +55,00% | -5,00% | 0,06627 $ | 1/22 | +4,55% | -20,83% | DEBOLE | 18,0 | 28,0 |
| +20,00% | 0,08371 $ | 22/40 | +55,00% | -8,00% | 0,06418 $ | 0/22 | 0,00% | -23,33% | DEBOLE | 18,0 | n/d |
| +20,00% | 0,08371 $ | 22/40 | +55,00% | -10,00% | 0,06278 $ | 0/22 | 0,00% | -25,00% | DEBOLE | 18,0 | n/d |
| +20,00% | 0,08371 $ | 22/40 | +55,00% | -15,00% | 0,05930 $ | 0/22 | 0,00% | -29,17% | DEBOLE | 18,0 | n/d |

---
