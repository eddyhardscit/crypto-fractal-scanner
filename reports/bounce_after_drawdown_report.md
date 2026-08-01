# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-08-01 07:14:01 CEST**  
UTC: **2026-08-01 05:14:01 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 59.912 $ | 69.372 $ | +18,75% | +15,79% | rimbalzo poco frequente | 69.372 $ | 59.912 $ | 0,00% | -13,64% | spike storicamente più resistente |
| SOL | 69,46 $ | 80,43 $ | +14,29% | +15,79% | rimbalzo poco frequente | 80,43 $ | 69,46 $ | 0,00% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06659 $ | 0,07710 $ | +39,29% | +15,79% | rimbalzo debole | 0,07710 $ | 0,06659 $ | +32,14% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 16 prima sono scesi a -5,00%. Tra quei 16, 3 poi sono rimbalzati fino a +10,00%. Percentuale: +18,75% (3/16). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- BTC: su 40 casi simili, 24 prima sono saliti a +10,00%. Tra quei 24, 0 poi sono scaricati a -5,00%. Percentuale: 0,00% (0/24). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 59.912 $ | 16/40 | +40,00% | +5,00% | 66.218 $ | 5/16 | +31,25% | +10,53% | DEBOLE | 7,7 | 19,2 |
| -5,00% | 59.912 $ | 16/40 | +40,00% | +10,00% | 69.372 $ | 3/16 | +18,75% | +15,79% | DEBOLE | 7,7 | 14,7 |
| -5,00% | 59.912 $ | 16/40 | +40,00% | +15,00% | 72.525 $ | 3/16 | +18,75% | +21,05% | DEBOLE | 7,7 | 19,0 |
| -5,00% | 59.912 $ | 16/40 | +40,00% | +20,00% | 75.678 $ | 3/16 | +18,75% | +26,32% | DEBOLE | 7,7 | 22,3 |
| -8,00% | 58.020 $ | 13/40 | +32,50% | +5,00% | 66.218 $ | 3/13 | +23,08% | +14,13% | DEBOLE | 10,0 | 22,7 |
| -8,00% | 58.020 $ | 13/40 | +32,50% | +10,00% | 69.372 $ | 1/13 | +7,69% | +19,57% | DEBOLE | 10,0 | 14,0 |
| -8,00% | 58.020 $ | 13/40 | +32,50% | +15,00% | 72.525 $ | 1/13 | +7,69% | +25,00% | DEBOLE | 10,0 | 25,0 |
| -8,00% | 58.020 $ | 13/40 | +32,50% | +20,00% | 75.678 $ | 1/13 | +7,69% | +30,43% | DEBOLE | 10,0 | 25,0 |
| -10,00% | 56.759 $ | 12/40 | +30,00% | +5,00% | 66.218 $ | 2/12 | +16,67% | +16,67% | DEBOLE | 11,2 | 28,0 |
| -10,00% | 56.759 $ | 12/40 | +30,00% | +10,00% | 69.372 $ | 0/12 | 0,00% | +22,22% | DEBOLE | 11,2 | n/d |
| -10,00% | 56.759 $ | 12/40 | +30,00% | +15,00% | 72.525 $ | 0/12 | 0,00% | +27,78% | DEBOLE | 11,2 | n/d |
| -10,00% | 56.759 $ | 12/40 | +30,00% | +20,00% | 75.678 $ | 0/12 | 0,00% | +33,33% | DEBOLE | 11,2 | n/d |
| -15,00% | 53.605 $ | 6/40 | +15,00% | +5,00% | 66.218 $ | 0/6 | 0,00% | +23,53% | DEBOLE | 12,2 | n/d |
| -15,00% | 53.605 $ | 6/40 | +15,00% | +10,00% | 69.372 $ | 0/6 | 0,00% | +29,41% | DEBOLE | 12,2 | n/d |
| -15,00% | 53.605 $ | 6/40 | +15,00% | +15,00% | 72.525 $ | 0/6 | 0,00% | +35,29% | DEBOLE | 12,2 | n/d |
| -15,00% | 53.605 $ | 6/40 | +15,00% | +20,00% | 75.678 $ | 0/6 | 0,00% | +41,18% | DEBOLE | 12,2 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 66.218 $ | 30/40 | +75,00% | prezzo iniziale | 63.065 $ | 5/30 | +16,67% | -4,76% | DEBOLE | 7,4 | 16,2 |
| +5,00% | 66.218 $ | 30/40 | +75,00% | -5,00% | 59.912 $ | 2/30 | +6,67% | -9,52% | DEBOLE | 7,4 | 15,0 |
| +5,00% | 66.218 $ | 30/40 | +75,00% | -8,00% | 58.020 $ | 2/30 | +6,67% | -12,38% | DEBOLE | 7,4 | 17,0 |
| +5,00% | 66.218 $ | 30/40 | +75,00% | -10,00% | 56.759 $ | 1/30 | +3,33% | -14,29% | DEBOLE | 7,4 | 29,0 |
| +5,00% | 66.218 $ | 30/40 | +75,00% | -15,00% | 53.605 $ | 0/30 | 0,00% | -19,05% | DEBOLE | 7,4 | n/d |
| +10,00% | 69.372 $ | 24/40 | +60,00% | prezzo iniziale | 63.065 $ | 2/24 | +8,33% | -9,09% | DEBOLE | 11,5 | 20,5 |
| +10,00% | 69.372 $ | 24/40 | +60,00% | -5,00% | 59.912 $ | 0/24 | 0,00% | -13,64% | DEBOLE | 11,5 | n/d |
| +10,00% | 69.372 $ | 24/40 | +60,00% | -8,00% | 58.020 $ | 0/24 | 0,00% | -16,36% | DEBOLE | 11,5 | n/d |
| +10,00% | 69.372 $ | 24/40 | +60,00% | -10,00% | 56.759 $ | 0/24 | 0,00% | -18,18% | DEBOLE | 11,5 | n/d |
| +10,00% | 69.372 $ | 24/40 | +60,00% | -15,00% | 53.605 $ | 0/24 | 0,00% | -22,73% | DEBOLE | 11,5 | n/d |
| +15,00% | 72.525 $ | 20/40 | +50,00% | prezzo iniziale | 63.065 $ | 1/20 | +5,00% | -13,04% | DEBOLE | 14,5 | 28,0 |
| +15,00% | 72.525 $ | 20/40 | +50,00% | -5,00% | 59.912 $ | 0/20 | 0,00% | -17,39% | DEBOLE | 14,5 | n/d |
| +15,00% | 72.525 $ | 20/40 | +50,00% | -8,00% | 58.020 $ | 0/20 | 0,00% | -20,00% | DEBOLE | 14,5 | n/d |
| +15,00% | 72.525 $ | 20/40 | +50,00% | -10,00% | 56.759 $ | 0/20 | 0,00% | -21,74% | DEBOLE | 14,5 | n/d |
| +15,00% | 72.525 $ | 20/40 | +50,00% | -15,00% | 53.605 $ | 0/20 | 0,00% | -26,09% | DEBOLE | 14,5 | n/d |
| +20,00% | 75.678 $ | 16/40 | +40,00% | prezzo iniziale | 63.065 $ | 0/16 | 0,00% | -16,67% | DEBOLE | 16,1 | n/d |
| +20,00% | 75.678 $ | 16/40 | +40,00% | -5,00% | 59.912 $ | 0/16 | 0,00% | -20,83% | DEBOLE | 16,1 | n/d |
| +20,00% | 75.678 $ | 16/40 | +40,00% | -8,00% | 58.020 $ | 0/16 | 0,00% | -23,33% | DEBOLE | 16,1 | n/d |
| +20,00% | 75.678 $ | 16/40 | +40,00% | -10,00% | 56.759 $ | 0/16 | 0,00% | -25,00% | DEBOLE | 16,1 | n/d |
| +20,00% | 75.678 $ | 16/40 | +40,00% | -15,00% | 53.605 $ | 0/16 | 0,00% | -29,17% | DEBOLE | 16,1 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 21 prima sono scesi a -5,00%. Tra quei 21, 3 poi sono rimbalzati fino a +10,00%. Percentuale: +14,29% (3/21). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 20 prima sono saliti a +10,00%. Tra quei 20, 0 poi sono scaricati a -5,00%. Percentuale: 0,00% (0/20). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 69,46 $ | 21/40 | +52,50% | +5,00% | 76,78 $ | 6/21 | +28,57% | +10,53% | DEBOLE | 8,5 | 21,2 |
| -5,00% | 69,46 $ | 21/40 | +52,50% | +10,00% | 80,43 $ | 3/21 | +14,29% | +15,79% | DEBOLE | 8,5 | 21,0 |
| -5,00% | 69,46 $ | 21/40 | +52,50% | +15,00% | 84,09 $ | 2/21 | +9,52% | +21,05% | DEBOLE | 8,5 | 22,0 |
| -5,00% | 69,46 $ | 21/40 | +52,50% | +20,00% | 87,74 $ | 2/21 | +9,52% | +26,32% | DEBOLE | 8,5 | 22,0 |
| -8,00% | 67,27 $ | 19/40 | +47,50% | +5,00% | 76,78 $ | 4/19 | +21,05% | +14,13% | DEBOLE | 9,2 | 23,0 |
| -8,00% | 67,27 $ | 19/40 | +47,50% | +10,00% | 80,43 $ | 2/19 | +10,53% | +19,57% | DEBOLE | 9,2 | 22,5 |
| -8,00% | 67,27 $ | 19/40 | +47,50% | +15,00% | 84,09 $ | 1/19 | +5,26% | +25,00% | DEBOLE | 9,2 | 23,0 |
| -8,00% | 67,27 $ | 19/40 | +47,50% | +20,00% | 87,74 $ | 1/19 | +5,26% | +30,43% | DEBOLE | 9,2 | 23,0 |
| -10,00% | 65,81 $ | 18/40 | +45,00% | +5,00% | 76,78 $ | 4/18 | +22,22% | +16,67% | DEBOLE | 10,7 | 23,0 |
| -10,00% | 65,81 $ | 18/40 | +45,00% | +10,00% | 80,43 $ | 2/18 | +11,11% | +22,22% | DEBOLE | 10,7 | 22,5 |
| -10,00% | 65,81 $ | 18/40 | +45,00% | +15,00% | 84,09 $ | 1/18 | +5,56% | +27,78% | DEBOLE | 10,7 | 23,0 |
| -10,00% | 65,81 $ | 18/40 | +45,00% | +20,00% | 87,74 $ | 1/18 | +5,56% | +33,33% | DEBOLE | 10,7 | 23,0 |
| -15,00% | 62,15 $ | 8/40 | +20,00% | +5,00% | 76,78 $ | 0/8 | 0,00% | +23,53% | DEBOLE | 12,8 | n/d |
| -15,00% | 62,15 $ | 8/40 | +20,00% | +10,00% | 80,43 $ | 0/8 | 0,00% | +29,41% | DEBOLE | 12,8 | n/d |
| -15,00% | 62,15 $ | 8/40 | +20,00% | +15,00% | 84,09 $ | 0/8 | 0,00% | +35,29% | DEBOLE | 12,8 | n/d |
| -15,00% | 62,15 $ | 8/40 | +20,00% | +20,00% | 87,74 $ | 0/8 | 0,00% | +41,18% | DEBOLE | 12,8 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 76,78 $ | 29/40 | +72,50% | prezzo iniziale | 73,12 $ | 7/29 | +24,14% | -4,76% | DEBOLE | 8,5 | 10,3 |
| +5,00% | 76,78 $ | 29/40 | +72,50% | -5,00% | 69,46 $ | 6/29 | +20,69% | -9,52% | DEBOLE | 8,5 | 13,3 |
| +5,00% | 76,78 $ | 29/40 | +72,50% | -8,00% | 67,27 $ | 4/29 | +13,79% | -12,38% | DEBOLE | 8,5 | 16,8 |
| +5,00% | 76,78 $ | 29/40 | +72,50% | -10,00% | 65,81 $ | 3/29 | +10,34% | -14,29% | DEBOLE | 8,5 | 18,3 |
| +5,00% | 76,78 $ | 29/40 | +72,50% | -15,00% | 62,15 $ | 0/29 | 0,00% | -19,05% | DEBOLE | 8,5 | n/d |
| +10,00% | 80,43 $ | 20/40 | +50,00% | prezzo iniziale | 73,12 $ | 0/20 | 0,00% | -9,09% | DEBOLE | 10,8 | n/d |
| +10,00% | 80,43 $ | 20/40 | +50,00% | -5,00% | 69,46 $ | 0/20 | 0,00% | -13,64% | DEBOLE | 10,8 | n/d |
| +10,00% | 80,43 $ | 20/40 | +50,00% | -8,00% | 67,27 $ | 0/20 | 0,00% | -16,36% | DEBOLE | 10,8 | n/d |
| +10,00% | 80,43 $ | 20/40 | +50,00% | -10,00% | 65,81 $ | 0/20 | 0,00% | -18,18% | DEBOLE | 10,8 | n/d |
| +10,00% | 80,43 $ | 20/40 | +50,00% | -15,00% | 62,15 $ | 0/20 | 0,00% | -22,73% | DEBOLE | 10,8 | n/d |
| +15,00% | 84,09 $ | 17/40 | +42,50% | prezzo iniziale | 73,12 $ | 0/17 | 0,00% | -13,04% | DEBOLE | 13,4 | n/d |
| +15,00% | 84,09 $ | 17/40 | +42,50% | -5,00% | 69,46 $ | 0/17 | 0,00% | -17,39% | DEBOLE | 13,4 | n/d |
| +15,00% | 84,09 $ | 17/40 | +42,50% | -8,00% | 67,27 $ | 0/17 | 0,00% | -20,00% | DEBOLE | 13,4 | n/d |
| +15,00% | 84,09 $ | 17/40 | +42,50% | -10,00% | 65,81 $ | 0/17 | 0,00% | -21,74% | DEBOLE | 13,4 | n/d |
| +15,00% | 84,09 $ | 17/40 | +42,50% | -15,00% | 62,15 $ | 0/17 | 0,00% | -26,09% | DEBOLE | 13,4 | n/d |
| +20,00% | 87,74 $ | 14/40 | +35,00% | prezzo iniziale | 73,12 $ | 0/14 | 0,00% | -16,67% | DEBOLE | 16,9 | n/d |
| +20,00% | 87,74 $ | 14/40 | +35,00% | -5,00% | 69,46 $ | 0/14 | 0,00% | -20,83% | DEBOLE | 16,9 | n/d |
| +20,00% | 87,74 $ | 14/40 | +35,00% | -8,00% | 67,27 $ | 0/14 | 0,00% | -23,33% | DEBOLE | 16,9 | n/d |
| +20,00% | 87,74 $ | 14/40 | +35,00% | -10,00% | 65,81 $ | 0/14 | 0,00% | -25,00% | DEBOLE | 16,9 | n/d |
| +20,00% | 87,74 $ | 14/40 | +35,00% | -15,00% | 62,15 $ | 0/14 | 0,00% | -29,17% | DEBOLE | 16,9 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 28 prima sono scesi a -5,00%. Tra quei 28, 11 poi sono rimbalzati fino a +10,00%. Percentuale: +39,29% (11/28). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- DOGE: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 9 poi sono scaricati a -5,00%. Percentuale: +32,14% (9/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06659 $ | 28/40 | +70,00% | +5,00% | 0,07359 $ | 14/28 | +50,00% | +10,53% | MEDIA | 7,8 | 22,4 |
| -5,00% | 0,06659 $ | 28/40 | +70,00% | +10,00% | 0,07710 $ | 11/28 | +39,29% | +15,79% | BASSA | 7,8 | 23,4 |
| -5,00% | 0,06659 $ | 28/40 | +70,00% | +15,00% | 0,08060 $ | 8/28 | +28,57% | +21,05% | DEBOLE | 7,8 | 22,8 |
| -5,00% | 0,06659 $ | 28/40 | +70,00% | +20,00% | 0,08411 $ | 2/28 | +7,14% | +26,32% | DEBOLE | 7,8 | 15,5 |
| -8,00% | 0,06448 $ | 25/40 | +62,50% | +5,00% | 0,07359 $ | 12/25 | +48,00% | +14,13% | BASSA | 8,6 | 23,6 |
| -8,00% | 0,06448 $ | 25/40 | +62,50% | +10,00% | 0,07710 $ | 9/25 | +36,00% | +19,57% | BASSA | 8,6 | 24,1 |
| -8,00% | 0,06448 $ | 25/40 | +62,50% | +15,00% | 0,08060 $ | 6/25 | +24,00% | +25,00% | DEBOLE | 8,6 | 23,0 |
| -8,00% | 0,06448 $ | 25/40 | +62,50% | +20,00% | 0,08411 $ | 1/25 | +4,00% | +30,43% | DEBOLE | 8,6 | 15,0 |
| -10,00% | 0,06308 $ | 22/40 | +55,00% | +5,00% | 0,07359 $ | 9/22 | +40,91% | +16,67% | BASSA | 8,9 | 23,4 |
| -10,00% | 0,06308 $ | 22/40 | +55,00% | +10,00% | 0,07710 $ | 6/22 | +27,27% | +22,22% | DEBOLE | 8,9 | 24,0 |
| -10,00% | 0,06308 $ | 22/40 | +55,00% | +15,00% | 0,08060 $ | 5/22 | +22,73% | +27,78% | DEBOLE | 8,9 | 24,8 |
| -10,00% | 0,06308 $ | 22/40 | +55,00% | +20,00% | 0,08411 $ | 0/22 | 0,00% | +33,33% | DEBOLE | 8,9 | n/d |
| -15,00% | 0,05958 $ | 13/40 | +32,50% | +5,00% | 0,07359 $ | 1/13 | +7,69% | +23,53% | DEBOLE | 11,6 | 23,0 |
| -15,00% | 0,05958 $ | 13/40 | +32,50% | +10,00% | 0,07710 $ | 1/13 | +7,69% | +29,41% | DEBOLE | 11,6 | 23,0 |
| -15,00% | 0,05958 $ | 13/40 | +32,50% | +15,00% | 0,08060 $ | 1/13 | +7,69% | +35,29% | DEBOLE | 11,6 | 24,0 |
| -15,00% | 0,05958 $ | 13/40 | +32,50% | +20,00% | 0,08411 $ | 0/13 | 0,00% | +41,18% | DEBOLE | 11,6 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07359 $ | 34/40 | +85,00% | prezzo iniziale | 0,07009 $ | 24/34 | +70,59% | -4,76% | ALTA | 7,3 | 13,8 |
| +5,00% | 0,07359 $ | 34/40 | +85,00% | -5,00% | 0,06659 $ | 16/34 | +47,06% | -9,52% | BASSA | 7,3 | 13,2 |
| +5,00% | 0,07359 $ | 34/40 | +85,00% | -8,00% | 0,06448 $ | 13/34 | +38,24% | -12,38% | BASSA | 7,3 | 12,8 |
| +5,00% | 0,07359 $ | 34/40 | +85,00% | -10,00% | 0,06308 $ | 10/34 | +29,41% | -14,29% | DEBOLE | 7,3 | 12,8 |
| +5,00% | 0,07359 $ | 34/40 | +85,00% | -15,00% | 0,05958 $ | 7/34 | +20,59% | -19,05% | DEBOLE | 7,3 | 14,0 |
| +10,00% | 0,07710 $ | 28/40 | +70,00% | prezzo iniziale | 0,07009 $ | 14/28 | +50,00% | -9,09% | MEDIA | 10,8 | 15,4 |
| +10,00% | 0,07710 $ | 28/40 | +70,00% | -5,00% | 0,06659 $ | 9/28 | +32,14% | -13,64% | DEBOLE | 10,8 | 17,0 |
| +10,00% | 0,07710 $ | 28/40 | +70,00% | -8,00% | 0,06448 $ | 6/28 | +21,43% | -16,36% | DEBOLE | 10,8 | 16,0 |
| +10,00% | 0,07710 $ | 28/40 | +70,00% | -10,00% | 0,06308 $ | 4/28 | +14,29% | -18,18% | DEBOLE | 10,8 | 12,8 |
| +10,00% | 0,07710 $ | 28/40 | +70,00% | -15,00% | 0,05958 $ | 4/28 | +14,29% | -22,73% | DEBOLE | 10,8 | 15,5 |
| +15,00% | 0,08060 $ | 20/40 | +50,00% | prezzo iniziale | 0,07009 $ | 7/20 | +35,00% | -13,04% | BASSA | 13,0 | 20,0 |
| +15,00% | 0,08060 $ | 20/40 | +50,00% | -5,00% | 0,06659 $ | 4/20 | +20,00% | -17,39% | DEBOLE | 13,0 | 21,0 |
| +15,00% | 0,08060 $ | 20/40 | +50,00% | -8,00% | 0,06448 $ | 1/20 | +5,00% | -20,00% | DEBOLE | 13,0 | 23,0 |
| +15,00% | 0,08060 $ | 20/40 | +50,00% | -10,00% | 0,06308 $ | 0/20 | 0,00% | -21,74% | DEBOLE | 13,0 | n/d |
| +15,00% | 0,08060 $ | 20/40 | +50,00% | -15,00% | 0,05958 $ | 0/20 | 0,00% | -26,09% | DEBOLE | 13,0 | n/d |
| +20,00% | 0,08411 $ | 13/40 | +32,50% | prezzo iniziale | 0,07009 $ | 4/13 | +30,77% | -16,67% | DEBOLE | 10,2 | 17,8 |
| +20,00% | 0,08411 $ | 13/40 | +32,50% | -5,00% | 0,06659 $ | 2/13 | +15,38% | -20,83% | DEBOLE | 10,2 | 21,5 |
| +20,00% | 0,08411 $ | 13/40 | +32,50% | -8,00% | 0,06448 $ | 0/13 | 0,00% | -23,33% | DEBOLE | 10,2 | n/d |
| +20,00% | 0,08411 $ | 13/40 | +32,50% | -10,00% | 0,06308 $ | 0/13 | 0,00% | -25,00% | DEBOLE | 10,2 | n/d |
| +20,00% | 0,08411 $ | 13/40 | +32,50% | -15,00% | 0,05958 $ | 0/13 | 0,00% | -29,17% | DEBOLE | 10,2 | n/d |

---
