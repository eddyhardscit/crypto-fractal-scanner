# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-23 09:37:02 CEST**  
UTC: **2026-07-23 07:37:02 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.130 $ | 71.940 $ | +51,43% | +15,79% | rimbalzo possibile | 71.940 $ | 62.130 $ | +8,70% | -13,64% | spike storicamente più resistente |
| SOL | 73,25 $ | 84,82 $ | +36,67% | +15,79% | rimbalzo debole | 84,82 $ | 73,25 $ | +15,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06865 $ | 0,07949 $ | +27,27% | +15,79% | rimbalzo poco frequente | 0,07949 $ | 0,06865 $ | +52,00% | -13,64% | attenzione a prendere profitto |

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

- BTC: su 40 casi simili, 35 prima sono scesi a -5,00%. Tra quei 35, 18 poi sono rimbalzati fino a +10,00%. Percentuale: +51,43% (18/35). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.
- BTC: su 40 casi simili, 23 prima sono saliti a +10,00%. Tra quei 23, 2 poi sono scaricati a -5,00%. Percentuale: +8,70% (2/23). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 62.130 $ | 35/40 | +87,50% | +5,00% | 68.670 $ | 22/35 | +62,86% | +10,53% | MEDIA | 5,2 | 19,2 |
| -5,00% | 62.130 $ | 35/40 | +87,50% | +10,00% | 71.940 $ | 18/35 | +51,43% | +15,79% | MEDIA | 5,2 | 21,4 |
| -5,00% | 62.130 $ | 35/40 | +87,50% | +15,00% | 75.210 $ | 15/35 | +42,86% | +21,05% | BASSA | 5,2 | 25,2 |
| -5,00% | 62.130 $ | 35/40 | +87,50% | +20,00% | 78.480 $ | 13/35 | +37,14% | +26,32% | BASSA | 5,2 | 26,6 |
| -8,00% | 60.168 $ | 27/40 | +67,50% | +5,00% | 68.670 $ | 14/27 | +51,85% | +14,13% | MEDIA | 8,6 | 20,9 |
| -8,00% | 60.168 $ | 27/40 | +67,50% | +10,00% | 71.940 $ | 11/27 | +40,74% | +19,57% | BASSA | 8,6 | 22,4 |
| -8,00% | 60.168 $ | 27/40 | +67,50% | +15,00% | 75.210 $ | 9/27 | +33,33% | +25,00% | DEBOLE | 8,6 | 25,1 |
| -8,00% | 60.168 $ | 27/40 | +67,50% | +20,00% | 78.480 $ | 8/27 | +29,63% | +30,43% | DEBOLE | 8,6 | 25,9 |
| -10,00% | 58.860 $ | 22/40 | +55,00% | +5,00% | 68.670 $ | 9/22 | +40,91% | +16,67% | BASSA | 11,0 | 21,2 |
| -10,00% | 58.860 $ | 22/40 | +55,00% | +10,00% | 71.940 $ | 7/22 | +31,82% | +22,22% | DEBOLE | 11,0 | 23,0 |
| -10,00% | 58.860 $ | 22/40 | +55,00% | +15,00% | 75.210 $ | 6/22 | +27,27% | +27,78% | DEBOLE | 11,0 | 24,7 |
| -10,00% | 58.860 $ | 22/40 | +55,00% | +20,00% | 78.480 $ | 6/22 | +27,27% | +33,33% | DEBOLE | 11,0 | 25,5 |
| -15,00% | 55.590 $ | 13/40 | +32,50% | +5,00% | 68.670 $ | 1/13 | +7,69% | +23,53% | DEBOLE | 15,0 | 21,0 |
| -15,00% | 55.590 $ | 13/40 | +32,50% | +10,00% | 71.940 $ | 0/13 | 0,00% | +29,41% | DEBOLE | 15,0 | n/d |
| -15,00% | 55.590 $ | 13/40 | +32,50% | +15,00% | 75.210 $ | 0/13 | 0,00% | +35,29% | DEBOLE | 15,0 | n/d |
| -15,00% | 55.590 $ | 13/40 | +32,50% | +20,00% | 78.480 $ | 0/13 | 0,00% | +41,18% | DEBOLE | 15,0 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 68.670 $ | 31/40 | +77,50% | prezzo iniziale | 65.400 $ | 13/31 | +41,94% | -4,76% | BASSA | 14,8 | 13,2 |
| +5,00% | 68.670 $ | 31/40 | +77,50% | -5,00% | 62.130 $ | 10/31 | +32,26% | -9,52% | DEBOLE | 14,8 | 13,4 |
| +5,00% | 68.670 $ | 31/40 | +77,50% | -8,00% | 60.168 $ | 9/31 | +29,03% | -12,38% | DEBOLE | 14,8 | 14,6 |
| +5,00% | 68.670 $ | 31/40 | +77,50% | -10,00% | 58.860 $ | 7/31 | +22,58% | -14,29% | DEBOLE | 14,8 | 14,6 |
| +5,00% | 68.670 $ | 31/40 | +77,50% | -15,00% | 55.590 $ | 6/31 | +19,35% | -19,05% | DEBOLE | 14,8 | 18,3 |
| +10,00% | 71.940 $ | 23/40 | +57,50% | prezzo iniziale | 65.400 $ | 3/23 | +13,04% | -9,09% | DEBOLE | 19,8 | 19,7 |
| +10,00% | 71.940 $ | 23/40 | +57,50% | -5,00% | 62.130 $ | 2/23 | +8,70% | -13,64% | DEBOLE | 19,8 | 19,0 |
| +10,00% | 71.940 $ | 23/40 | +57,50% | -8,00% | 60.168 $ | 2/23 | +8,70% | -16,36% | DEBOLE | 19,8 | 19,0 |
| +10,00% | 71.940 $ | 23/40 | +57,50% | -10,00% | 58.860 $ | 2/23 | +8,70% | -18,18% | DEBOLE | 19,8 | 19,0 |
| +10,00% | 71.940 $ | 23/40 | +57,50% | -15,00% | 55.590 $ | 2/23 | +8,70% | -22,73% | DEBOLE | 19,8 | 19,5 |
| +15,00% | 75.210 $ | 19/40 | +47,50% | prezzo iniziale | 65.400 $ | 1/19 | +5,26% | -13,04% | DEBOLE | 22,7 | 17,0 |
| +15,00% | 75.210 $ | 19/40 | +47,50% | -5,00% | 62.130 $ | 1/19 | +5,26% | -17,39% | DEBOLE | 22,7 | 17,0 |
| +15,00% | 75.210 $ | 19/40 | +47,50% | -8,00% | 60.168 $ | 1/19 | +5,26% | -20,00% | DEBOLE | 22,7 | 17,0 |
| +15,00% | 75.210 $ | 19/40 | +47,50% | -10,00% | 58.860 $ | 1/19 | +5,26% | -21,74% | DEBOLE | 22,7 | 17,0 |
| +15,00% | 75.210 $ | 19/40 | +47,50% | -15,00% | 55.590 $ | 1/19 | +5,26% | -26,09% | DEBOLE | 22,7 | 18,0 |
| +20,00% | 78.480 $ | 17/40 | +42,50% | prezzo iniziale | 65.400 $ | 1/17 | +5,88% | -16,67% | DEBOLE | 24,3 | 17,0 |
| +20,00% | 78.480 $ | 17/40 | +42,50% | -5,00% | 62.130 $ | 1/17 | +5,88% | -20,83% | DEBOLE | 24,3 | 17,0 |
| +20,00% | 78.480 $ | 17/40 | +42,50% | -8,00% | 60.168 $ | 1/17 | +5,88% | -23,33% | DEBOLE | 24,3 | 17,0 |
| +20,00% | 78.480 $ | 17/40 | +42,50% | -10,00% | 58.860 $ | 1/17 | +5,88% | -25,00% | DEBOLE | 24,3 | 17,0 |
| +20,00% | 78.480 $ | 17/40 | +42,50% | -15,00% | 55.590 $ | 1/17 | +5,88% | -29,17% | DEBOLE | 24,3 | 18,0 |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 30 prima sono scesi a -5,00%. Tra quei 30, 11 poi sono rimbalzati fino a +10,00%. Percentuale: +36,67% (11/30). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- SOL: su 40 casi simili, 20 prima sono saliti a +10,00%. Tra quei 20, 3 poi sono scaricati a -5,00%. Percentuale: +15,00% (3/20). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 73,25 $ | 30/40 | +75,00% | +5,00% | 80,97 $ | 15/30 | +50,00% | +10,53% | MEDIA | 7,3 | 17,1 |
| -5,00% | 73,25 $ | 30/40 | +75,00% | +10,00% | 84,82 $ | 11/30 | +36,67% | +15,79% | BASSA | 7,3 | 20,6 |
| -5,00% | 73,25 $ | 30/40 | +75,00% | +15,00% | 88,68 $ | 8/30 | +26,67% | +21,05% | DEBOLE | 7,3 | 22,4 |
| -5,00% | 73,25 $ | 30/40 | +75,00% | +20,00% | 92,53 $ | 7/30 | +23,33% | +26,32% | DEBOLE | 7,3 | 23,3 |
| -8,00% | 70,94 $ | 23/40 | +57,50% | +5,00% | 80,97 $ | 9/23 | +39,13% | +14,13% | BASSA | 10,3 | 18,4 |
| -8,00% | 70,94 $ | 23/40 | +57,50% | +10,00% | 84,82 $ | 7/23 | +30,43% | +19,57% | DEBOLE | 10,3 | 21,7 |
| -8,00% | 70,94 $ | 23/40 | +57,50% | +15,00% | 88,68 $ | 5/23 | +21,74% | +25,00% | DEBOLE | 10,3 | 23,8 |
| -8,00% | 70,94 $ | 23/40 | +57,50% | +20,00% | 92,53 $ | 4/23 | +17,39% | +30,43% | DEBOLE | 10,3 | 25,2 |
| -10,00% | 69,40 $ | 16/40 | +40,00% | +5,00% | 80,97 $ | 3/16 | +18,75% | +16,67% | DEBOLE | 13,4 | 23,0 |
| -10,00% | 69,40 $ | 16/40 | +40,00% | +10,00% | 84,82 $ | 2/16 | +12,50% | +22,22% | DEBOLE | 13,4 | 27,5 |
| -10,00% | 69,40 $ | 16/40 | +40,00% | +15,00% | 88,68 $ | 2/16 | +12,50% | +27,78% | DEBOLE | 13,4 | 28,0 |
| -10,00% | 69,40 $ | 16/40 | +40,00% | +20,00% | 92,53 $ | 2/16 | +12,50% | +33,33% | DEBOLE | 13,4 | 28,0 |
| -15,00% | 65,54 $ | 9/40 | +22,50% | +5,00% | 80,97 $ | 1/9 | +11,11% | +23,53% | DEBOLE | 16,2 | 21,0 |
| -15,00% | 65,54 $ | 9/40 | +22,50% | +10,00% | 84,82 $ | 0/9 | 0,00% | +29,41% | DEBOLE | 16,2 | n/d |
| -15,00% | 65,54 $ | 9/40 | +22,50% | +15,00% | 88,68 $ | 0/9 | 0,00% | +35,29% | DEBOLE | 16,2 | n/d |
| -15,00% | 65,54 $ | 9/40 | +22,50% | +20,00% | 92,53 $ | 0/9 | 0,00% | +41,18% | DEBOLE | 16,2 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 80,97 $ | 30/40 | +75,00% | prezzo iniziale | 77,11 $ | 12/30 | +40,00% | -4,76% | BASSA | 13,5 | 15,4 |
| +5,00% | 80,97 $ | 30/40 | +75,00% | -5,00% | 73,25 $ | 8/30 | +26,67% | -9,52% | DEBOLE | 13,5 | 21,1 |
| +5,00% | 80,97 $ | 30/40 | +75,00% | -8,00% | 70,94 $ | 5/30 | +16,67% | -12,38% | DEBOLE | 13,5 | 20,8 |
| +5,00% | 80,97 $ | 30/40 | +75,00% | -10,00% | 69,40 $ | 4/30 | +13,33% | -14,29% | DEBOLE | 13,5 | 23,5 |
| +5,00% | 80,97 $ | 30/40 | +75,00% | -15,00% | 65,54 $ | 3/30 | +10,00% | -19,05% | DEBOLE | 13,5 | 25,0 |
| +10,00% | 84,82 $ | 20/40 | +50,00% | prezzo iniziale | 77,11 $ | 4/20 | +20,00% | -9,09% | DEBOLE | 17,4 | 20,5 |
| +10,00% | 84,82 $ | 20/40 | +50,00% | -5,00% | 73,25 $ | 3/20 | +15,00% | -13,64% | DEBOLE | 17,4 | 27,0 |
| +10,00% | 84,82 $ | 20/40 | +50,00% | -8,00% | 70,94 $ | 1/20 | +5,00% | -16,36% | DEBOLE | 17,4 | 24,0 |
| +10,00% | 84,82 $ | 20/40 | +50,00% | -10,00% | 69,40 $ | 1/20 | +5,00% | -18,18% | DEBOLE | 17,4 | 24,0 |
| +10,00% | 84,82 $ | 20/40 | +50,00% | -15,00% | 65,54 $ | 0/20 | 0,00% | -22,73% | DEBOLE | 17,4 | n/d |
| +15,00% | 88,68 $ | 16/40 | +40,00% | prezzo iniziale | 77,11 $ | 2/16 | +12,50% | -13,04% | DEBOLE | 19,2 | 22,0 |
| +15,00% | 88,68 $ | 16/40 | +40,00% | -5,00% | 73,25 $ | 2/16 | +12,50% | -17,39% | DEBOLE | 19,2 | 25,5 |
| +15,00% | 88,68 $ | 16/40 | +40,00% | -8,00% | 70,94 $ | 1/16 | +6,25% | -20,00% | DEBOLE | 19,2 | 24,0 |
| +15,00% | 88,68 $ | 16/40 | +40,00% | -10,00% | 69,40 $ | 1/16 | +6,25% | -21,74% | DEBOLE | 19,2 | 24,0 |
| +15,00% | 88,68 $ | 16/40 | +40,00% | -15,00% | 65,54 $ | 0/16 | 0,00% | -26,09% | DEBOLE | 19,2 | n/d |
| +20,00% | 92,53 $ | 12/40 | +30,00% | prezzo iniziale | 77,11 $ | 1/12 | +8,33% | -16,67% | DEBOLE | 18,3 | 19,0 |
| +20,00% | 92,53 $ | 12/40 | +30,00% | -5,00% | 73,25 $ | 1/12 | +8,33% | -20,83% | DEBOLE | 18,3 | 23,0 |
| +20,00% | 92,53 $ | 12/40 | +30,00% | -8,00% | 70,94 $ | 1/12 | +8,33% | -23,33% | DEBOLE | 18,3 | 24,0 |
| +20,00% | 92,53 $ | 12/40 | +30,00% | -10,00% | 69,40 $ | 1/12 | +8,33% | -25,00% | DEBOLE | 18,3 | 24,0 |
| +20,00% | 92,53 $ | 12/40 | +30,00% | -15,00% | 65,54 $ | 0/12 | 0,00% | -29,17% | DEBOLE | 18,3 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 33 prima sono scesi a -5,00%. Tra quei 33, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +27,27% (9/33). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 13 poi sono scaricati a -5,00%. Percentuale: +52,00% (13/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06865 $ | 33/40 | +82,50% | +5,00% | 0,07587 $ | 15/33 | +45,45% | +10,53% | BASSA | 7,6 | 16,9 |
| -5,00% | 0,06865 $ | 33/40 | +82,50% | +10,00% | 0,07949 $ | 9/33 | +27,27% | +15,79% | DEBOLE | 7,6 | 18,9 |
| -5,00% | 0,06865 $ | 33/40 | +82,50% | +15,00% | 0,08310 $ | 5/33 | +15,15% | +21,05% | DEBOLE | 7,6 | 20,0 |
| -5,00% | 0,06865 $ | 33/40 | +82,50% | +20,00% | 0,08671 $ | 3/33 | +9,09% | +26,32% | DEBOLE | 7,6 | 27,0 |
| -8,00% | 0,06648 $ | 26/40 | +65,00% | +5,00% | 0,07587 $ | 6/26 | +23,08% | +14,13% | DEBOLE | 10,4 | 17,2 |
| -8,00% | 0,06648 $ | 26/40 | +65,00% | +10,00% | 0,07949 $ | 3/26 | +11,54% | +19,57% | DEBOLE | 10,4 | 19,0 |
| -8,00% | 0,06648 $ | 26/40 | +65,00% | +15,00% | 0,08310 $ | 2/26 | +7,69% | +25,00% | DEBOLE | 10,4 | 17,5 |
| -8,00% | 0,06648 $ | 26/40 | +65,00% | +20,00% | 0,08671 $ | 1/26 | +3,85% | +30,43% | DEBOLE | 10,4 | 30,0 |
| -10,00% | 0,06503 $ | 24/40 | +60,00% | +5,00% | 0,07587 $ | 6/24 | +25,00% | +16,67% | DEBOLE | 10,3 | 17,2 |
| -10,00% | 0,06503 $ | 24/40 | +60,00% | +10,00% | 0,07949 $ | 3/24 | +12,50% | +22,22% | DEBOLE | 10,3 | 19,0 |
| -10,00% | 0,06503 $ | 24/40 | +60,00% | +15,00% | 0,08310 $ | 2/24 | +8,33% | +27,78% | DEBOLE | 10,3 | 17,5 |
| -10,00% | 0,06503 $ | 24/40 | +60,00% | +20,00% | 0,08671 $ | 1/24 | +4,17% | +33,33% | DEBOLE | 10,3 | 30,0 |
| -15,00% | 0,06142 $ | 18/40 | +45,00% | +5,00% | 0,07587 $ | 3/18 | +16,67% | +23,53% | DEBOLE | 10,9 | 15,7 |
| -15,00% | 0,06142 $ | 18/40 | +45,00% | +10,00% | 0,07949 $ | 2/18 | +11,11% | +29,41% | DEBOLE | 10,9 | 17,0 |
| -15,00% | 0,06142 $ | 18/40 | +45,00% | +15,00% | 0,08310 $ | 1/18 | +5,56% | +35,29% | DEBOLE | 10,9 | 10,0 |
| -15,00% | 0,06142 $ | 18/40 | +45,00% | +20,00% | 0,08671 $ | 0/18 | 0,00% | +41,18% | DEBOLE | 10,9 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07587 $ | 31/40 | +77,50% | prezzo iniziale | 0,07226 $ | 23/31 | +74,19% | -4,76% | ALTA | 6,5 | 11,8 |
| +5,00% | 0,07587 $ | 31/40 | +77,50% | -5,00% | 0,06865 $ | 20/31 | +64,52% | -9,52% | MEDIA | 6,5 | 15,6 |
| +5,00% | 0,07587 $ | 31/40 | +77,50% | -8,00% | 0,06648 $ | 15/31 | +48,39% | -12,38% | BASSA | 6,5 | 18,3 |
| +5,00% | 0,07587 $ | 31/40 | +77,50% | -10,00% | 0,06503 $ | 13/31 | +41,94% | -14,29% | BASSA | 6,5 | 18,8 |
| +5,00% | 0,07587 $ | 31/40 | +77,50% | -15,00% | 0,06142 $ | 6/31 | +19,35% | -19,05% | DEBOLE | 6,5 | 18,0 |
| +10,00% | 0,07949 $ | 25/40 | +62,50% | prezzo iniziale | 0,07226 $ | 15/25 | +60,00% | -9,09% | MEDIA | 8,2 | 13,0 |
| +10,00% | 0,07949 $ | 25/40 | +62,50% | -5,00% | 0,06865 $ | 13/25 | +52,00% | -13,64% | MEDIA | 8,2 | 17,8 |
| +10,00% | 0,07949 $ | 25/40 | +62,50% | -8,00% | 0,06648 $ | 9/25 | +36,00% | -16,36% | BASSA | 8,2 | 17,8 |
| +10,00% | 0,07949 $ | 25/40 | +62,50% | -10,00% | 0,06503 $ | 7/25 | +28,00% | -18,18% | DEBOLE | 8,2 | 17,6 |
| +10,00% | 0,07949 $ | 25/40 | +62,50% | -15,00% | 0,06142 $ | 3/25 | +12,00% | -22,73% | DEBOLE | 8,2 | 15,3 |
| +15,00% | 0,08310 $ | 18/40 | +45,00% | prezzo iniziale | 0,07226 $ | 9/18 | +50,00% | -13,04% | MEDIA | 9,5 | 13,6 |
| +15,00% | 0,08310 $ | 18/40 | +45,00% | -5,00% | 0,06865 $ | 7/18 | +38,89% | -17,39% | BASSA | 9,5 | 20,1 |
| +15,00% | 0,08310 $ | 18/40 | +45,00% | -8,00% | 0,06648 $ | 4/18 | +22,22% | -20,00% | DEBOLE | 9,5 | 16,0 |
| +15,00% | 0,08310 $ | 18/40 | +45,00% | -10,00% | 0,06503 $ | 3/18 | +16,67% | -21,74% | DEBOLE | 9,5 | 17,0 |
| +15,00% | 0,08310 $ | 18/40 | +45,00% | -15,00% | 0,06142 $ | 1/18 | +5,56% | -26,09% | DEBOLE | 9,5 | 14,0 |
| +20,00% | 0,08671 $ | 11/40 | +27,50% | prezzo iniziale | 0,07226 $ | 3/11 | +27,27% | -16,67% | DEBOLE | 13,2 | 16,3 |
| +20,00% | 0,08671 $ | 11/40 | +27,50% | -5,00% | 0,06865 $ | 2/11 | +18,18% | -20,83% | DEBOLE | 13,2 | 26,0 |
| +20,00% | 0,08671 $ | 11/40 | +27,50% | -8,00% | 0,06648 $ | 0/11 | 0,00% | -23,33% | DEBOLE | 13,2 | n/d |
| +20,00% | 0,08671 $ | 11/40 | +27,50% | -10,00% | 0,06503 $ | 0/11 | 0,00% | -25,00% | DEBOLE | 13,2 | n/d |
| +20,00% | 0,08671 $ | 11/40 | +27,50% | -15,00% | 0,06142 $ | 0/11 | 0,00% | -29,17% | DEBOLE | 13,2 | n/d |

---
