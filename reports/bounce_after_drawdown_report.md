# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-08-22 07:31:39 CEST**  
UTC: **2026-08-22 05:31:39 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 73.377 $ | 84.963 $ | +39,13% | +15,79% | rimbalzo debole | 84.963 $ | 73.377 $ | +35,71% | -13,64% | scarico possibile |
| SOL | 89,01 $ | 103,07 $ | +29,63% | +15,79% | rimbalzo poco frequente | 103,07 $ | 89,01 $ | +26,09% | -13,64% | spike storicamente più resistente |
| DOGE | 0,08608 $ | 0,09967 $ | +55,17% | +15,79% | rimbalzo possibile | 0,09967 $ | 0,08608 $ | +21,88% | -13,64% | spike storicamente più resistente |

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

- BTC: su 40 casi simili, 23 prima sono scesi a -5,00%. Tra quei 23, 9 poi sono rimbalzati fino a +10,00%. Percentuale: +39,13% (9/23). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 28 prima sono saliti a +10,00%. Tra quei 28, 10 poi sono scaricati a -5,00%. Percentuale: +35,71% (10/28). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: scarico possibile.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 73.377 $ | 23/40 | +57,50% | +5,00% | 81.101 $ | 12/23 | +52,17% | +10,53% | MEDIA | 10,6 | 15,4 |
| -5,00% | 73.377 $ | 23/40 | +57,50% | +10,00% | 84.963 $ | 9/23 | +39,13% | +15,79% | BASSA | 10,6 | 15,3 |
| -5,00% | 73.377 $ | 23/40 | +57,50% | +15,00% | 88.825 $ | 6/23 | +26,09% | +21,05% | DEBOLE | 10,6 | 15,8 |
| -5,00% | 73.377 $ | 23/40 | +57,50% | +20,00% | 92.687 $ | 4/23 | +17,39% | +26,32% | DEBOLE | 10,6 | 20,5 |
| -8,00% | 71.060 $ | 18/40 | +45,00% | +5,00% | 81.101 $ | 8/18 | +44,44% | +14,13% | BASSA | 14,2 | 18,6 |
| -8,00% | 71.060 $ | 18/40 | +45,00% | +10,00% | 84.963 $ | 6/18 | +33,33% | +19,57% | DEBOLE | 14,2 | 19,2 |
| -8,00% | 71.060 $ | 18/40 | +45,00% | +15,00% | 88.825 $ | 5/18 | +27,78% | +25,00% | DEBOLE | 14,2 | 22,8 |
| -8,00% | 71.060 $ | 18/40 | +45,00% | +20,00% | 92.687 $ | 3/18 | +16,67% | +30,43% | DEBOLE | 14,2 | 24,7 |
| -10,00% | 69.515 $ | 18/40 | +45,00% | +5,00% | 81.101 $ | 7/18 | +38,89% | +16,67% | BASSA | 16,6 | 20,9 |
| -10,00% | 69.515 $ | 18/40 | +45,00% | +10,00% | 84.963 $ | 5/18 | +27,78% | +22,22% | DEBOLE | 16,6 | 22,4 |
| -10,00% | 69.515 $ | 18/40 | +45,00% | +15,00% | 88.825 $ | 5/18 | +27,78% | +27,78% | DEBOLE | 16,6 | 22,8 |
| -10,00% | 69.515 $ | 18/40 | +45,00% | +20,00% | 92.687 $ | 3/18 | +16,67% | +33,33% | DEBOLE | 16,6 | 24,7 |
| -15,00% | 65.653 $ | 5/40 | +12,50% | +5,00% | 81.101 $ | 1/5 | +20,00% | +23,53% | DEBOLE | 18,6 | 13,0 |
| -15,00% | 65.653 $ | 5/40 | +12,50% | +10,00% | 84.963 $ | 0/5 | 0,00% | +29,41% | DEBOLE | 18,6 | n/d |
| -15,00% | 65.653 $ | 5/40 | +12,50% | +15,00% | 88.825 $ | 0/5 | 0,00% | +35,29% | DEBOLE | 18,6 | n/d |
| -15,00% | 65.653 $ | 5/40 | +12,50% | +20,00% | 92.687 $ | 0/5 | 0,00% | +41,18% | DEBOLE | 18,6 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 81.101 $ | 35/40 | +87,50% | prezzo iniziale | 77.239 $ | 20/35 | +57,14% | -4,76% | MEDIA | 7,5 | 14,7 |
| +5,00% | 81.101 $ | 35/40 | +87,50% | -5,00% | 73.377 $ | 12/35 | +34,29% | -9,52% | DEBOLE | 7,5 | 16,3 |
| +5,00% | 81.101 $ | 35/40 | +87,50% | -8,00% | 71.060 $ | 11/35 | +31,43% | -12,38% | DEBOLE | 7,5 | 19,0 |
| +5,00% | 81.101 $ | 35/40 | +87,50% | -10,00% | 69.515 $ | 10/35 | +28,57% | -14,29% | DEBOLE | 7,5 | 19,7 |
| +5,00% | 81.101 $ | 35/40 | +87,50% | -15,00% | 65.653 $ | 2/35 | +5,71% | -19,05% | DEBOLE | 7,5 | 25,5 |
| +10,00% | 84.963 $ | 28/40 | +70,00% | prezzo iniziale | 77.239 $ | 16/28 | +57,14% | -9,09% | MEDIA | 7,8 | 14,6 |
| +10,00% | 84.963 $ | 28/40 | +70,00% | -5,00% | 73.377 $ | 10/28 | +35,71% | -13,64% | BASSA | 7,8 | 14,4 |
| +10,00% | 84.963 $ | 28/40 | +70,00% | -8,00% | 71.060 $ | 9/28 | +32,14% | -16,36% | DEBOLE | 7,8 | 17,4 |
| +10,00% | 84.963 $ | 28/40 | +70,00% | -10,00% | 69.515 $ | 9/28 | +32,14% | -18,18% | DEBOLE | 7,8 | 18,7 |
| +10,00% | 84.963 $ | 28/40 | +70,00% | -15,00% | 65.653 $ | 2/28 | +7,14% | -22,73% | DEBOLE | 7,8 | 25,5 |
| +15,00% | 88.825 $ | 23/40 | +57,50% | prezzo iniziale | 77.239 $ | 10/23 | +43,48% | -13,04% | BASSA | 10,0 | 15,6 |
| +15,00% | 88.825 $ | 23/40 | +57,50% | -5,00% | 73.377 $ | 5/23 | +21,74% | -17,39% | DEBOLE | 10,0 | 13,8 |
| +15,00% | 88.825 $ | 23/40 | +57,50% | -8,00% | 71.060 $ | 5/23 | +21,74% | -20,00% | DEBOLE | 10,0 | 16,2 |
| +15,00% | 88.825 $ | 23/40 | +57,50% | -10,00% | 69.515 $ | 5/23 | +21,74% | -21,74% | DEBOLE | 10,0 | 17,6 |
| +15,00% | 88.825 $ | 23/40 | +57,50% | -15,00% | 65.653 $ | 2/23 | +8,70% | -26,09% | DEBOLE | 10,0 | 25,5 |
| +20,00% | 92.687 $ | 16/40 | +40,00% | prezzo iniziale | 77.239 $ | 5/16 | +31,25% | -16,67% | DEBOLE | 11,3 | 15,0 |
| +20,00% | 92.687 $ | 16/40 | +40,00% | -5,00% | 73.377 $ | 3/16 | +18,75% | -20,83% | DEBOLE | 11,3 | 15,0 |
| +20,00% | 92.687 $ | 16/40 | +40,00% | -8,00% | 71.060 $ | 3/16 | +18,75% | -23,33% | DEBOLE | 11,3 | 15,0 |
| +20,00% | 92.687 $ | 16/40 | +40,00% | -10,00% | 69.515 $ | 3/16 | +18,75% | -25,00% | DEBOLE | 11,3 | 16,7 |
| +20,00% | 92.687 $ | 16/40 | +40,00% | -15,00% | 65.653 $ | 1/16 | +6,25% | -29,17% | DEBOLE | 11,3 | 30,0 |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 27 prima sono scesi a -5,00%. Tra quei 27, 8 poi sono rimbalzati fino a +10,00%. Percentuale: +29,63% (8/27). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 23 prima sono saliti a +10,00%. Tra quei 23, 6 poi sono scaricati a -5,00%. Percentuale: +26,09% (6/23). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 89,01 $ | 27/40 | +67,50% | +5,00% | 98,38 $ | 10/27 | +37,04% | +10,53% | BASSA | 11,0 | 13,8 |
| -5,00% | 89,01 $ | 27/40 | +67,50% | +10,00% | 103,07 $ | 8/27 | +29,63% | +15,79% | DEBOLE | 11,0 | 13,2 |
| -5,00% | 89,01 $ | 27/40 | +67,50% | +15,00% | 107,75 $ | 5/27 | +18,52% | +21,05% | DEBOLE | 11,0 | 20,8 |
| -5,00% | 89,01 $ | 27/40 | +67,50% | +20,00% | 112,44 $ | 3/27 | +11,11% | +26,32% | DEBOLE | 11,0 | 17,7 |
| -8,00% | 86,20 $ | 23/40 | +57,50% | +5,00% | 98,38 $ | 6/23 | +26,09% | +14,13% | DEBOLE | 15,9 | 17,0 |
| -8,00% | 86,20 $ | 23/40 | +57,50% | +10,00% | 103,07 $ | 4/23 | +17,39% | +19,57% | DEBOLE | 15,9 | 15,2 |
| -8,00% | 86,20 $ | 23/40 | +57,50% | +15,00% | 107,75 $ | 2/23 | +8,70% | +25,00% | DEBOLE | 15,9 | 27,0 |
| -8,00% | 86,20 $ | 23/40 | +57,50% | +20,00% | 112,44 $ | 1/23 | +4,35% | +30,43% | DEBOLE | 15,9 | 26,0 |
| -10,00% | 84,33 $ | 18/40 | +45,00% | +5,00% | 98,38 $ | 2/18 | +11,11% | +16,67% | DEBOLE | 20,3 | 19,5 |
| -10,00% | 84,33 $ | 18/40 | +45,00% | +10,00% | 103,07 $ | 2/18 | +11,11% | +22,22% | DEBOLE | 20,3 | 21,0 |
| -10,00% | 84,33 $ | 18/40 | +45,00% | +15,00% | 107,75 $ | 2/18 | +11,11% | +27,78% | DEBOLE | 20,3 | 27,0 |
| -10,00% | 84,33 $ | 18/40 | +45,00% | +20,00% | 112,44 $ | 1/18 | +5,56% | +33,33% | DEBOLE | 20,3 | 26,0 |
| -15,00% | 79,64 $ | 2/40 | +5,00% | +5,00% | 98,38 $ | 0/2 | 0,00% | +23,53% | DEBOLE | 13,5 | n/d |
| -15,00% | 79,64 $ | 2/40 | +5,00% | +10,00% | 103,07 $ | 0/2 | 0,00% | +29,41% | DEBOLE | 13,5 | n/d |
| -15,00% | 79,64 $ | 2/40 | +5,00% | +15,00% | 107,75 $ | 0/2 | 0,00% | +35,29% | DEBOLE | 13,5 | n/d |
| -15,00% | 79,64 $ | 2/40 | +5,00% | +20,00% | 112,44 $ | 0/2 | 0,00% | +41,18% | DEBOLE | 13,5 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 98,38 $ | 30/40 | +75,00% | prezzo iniziale | 93,70 $ | 18/30 | +60,00% | -4,76% | MEDIA | 6,7 | 14,6 |
| +5,00% | 98,38 $ | 30/40 | +75,00% | -5,00% | 89,01 $ | 12/30 | +40,00% | -9,52% | BASSA | 6,7 | 16,2 |
| +5,00% | 98,38 $ | 30/40 | +75,00% | -8,00% | 86,20 $ | 9/30 | +30,00% | -12,38% | DEBOLE | 6,7 | 18,4 |
| +5,00% | 98,38 $ | 30/40 | +75,00% | -10,00% | 84,33 $ | 8/30 | +26,67% | -14,29% | DEBOLE | 6,7 | 19,5 |
| +5,00% | 98,38 $ | 30/40 | +75,00% | -15,00% | 79,64 $ | 1/30 | +3,33% | -19,05% | DEBOLE | 6,7 | 12,0 |
| +10,00% | 103,07 $ | 23/40 | +57,50% | prezzo iniziale | 93,70 $ | 10/23 | +43,48% | -9,09% | BASSA | 8,6 | 15,4 |
| +10,00% | 103,07 $ | 23/40 | +57,50% | -5,00% | 89,01 $ | 6/23 | +26,09% | -13,64% | DEBOLE | 8,6 | 15,8 |
| +10,00% | 103,07 $ | 23/40 | +57,50% | -8,00% | 86,20 $ | 5/23 | +21,74% | -16,36% | DEBOLE | 8,6 | 20,4 |
| +10,00% | 103,07 $ | 23/40 | +57,50% | -10,00% | 84,33 $ | 5/23 | +21,74% | -18,18% | DEBOLE | 8,6 | 22,2 |
| +10,00% | 103,07 $ | 23/40 | +57,50% | -15,00% | 79,64 $ | 0/23 | 0,00% | -22,73% | DEBOLE | 8,6 | n/d |
| +15,00% | 107,75 $ | 16/40 | +40,00% | prezzo iniziale | 93,70 $ | 4/16 | +25,00% | -13,04% | DEBOLE | 11,4 | 23,5 |
| +15,00% | 107,75 $ | 16/40 | +40,00% | -5,00% | 89,01 $ | 1/16 | +6,25% | -17,39% | DEBOLE | 11,4 | 21,0 |
| +15,00% | 107,75 $ | 16/40 | +40,00% | -8,00% | 86,20 $ | 1/16 | +6,25% | -20,00% | DEBOLE | 11,4 | 21,0 |
| +15,00% | 107,75 $ | 16/40 | +40,00% | -10,00% | 84,33 $ | 1/16 | +6,25% | -21,74% | DEBOLE | 11,4 | 26,0 |
| +15,00% | 107,75 $ | 16/40 | +40,00% | -15,00% | 79,64 $ | 0/16 | 0,00% | -26,09% | DEBOLE | 11,4 | n/d |
| +20,00% | 112,44 $ | 13/40 | +32,50% | prezzo iniziale | 93,70 $ | 3/13 | +23,08% | -16,67% | DEBOLE | 13,1 | 25,0 |
| +20,00% | 112,44 $ | 13/40 | +32,50% | -5,00% | 89,01 $ | 1/13 | +7,69% | -20,83% | DEBOLE | 13,1 | 21,0 |
| +20,00% | 112,44 $ | 13/40 | +32,50% | -8,00% | 86,20 $ | 1/13 | +7,69% | -23,33% | DEBOLE | 13,1 | 21,0 |
| +20,00% | 112,44 $ | 13/40 | +32,50% | -10,00% | 84,33 $ | 1/13 | +7,69% | -25,00% | DEBOLE | 13,1 | 26,0 |
| +20,00% | 112,44 $ | 13/40 | +32,50% | -15,00% | 79,64 $ | 0/13 | 0,00% | -29,17% | DEBOLE | 13,1 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 29 prima sono scesi a -5,00%. Tra quei 29, 16 poi sono rimbalzati fino a +10,00%. Percentuale: +55,17% (16/29). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo possibile.
- DOGE: su 40 casi simili, 32 prima sono saliti a +10,00%. Tra quei 32, 7 poi sono scaricati a -5,00%. Percentuale: +21,88% (7/32). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,08608 $ | 29/40 | +72,50% | +5,00% | 0,09514 $ | 19/29 | +65,52% | +10,53% | ALTA | 8,0 | 15,7 |
| -5,00% | 0,08608 $ | 29/40 | +72,50% | +10,00% | 0,09967 $ | 16/29 | +55,17% | +15,79% | MEDIA | 8,0 | 16,1 |
| -5,00% | 0,08608 $ | 29/40 | +72,50% | +15,00% | 0,10420 $ | 13/29 | +44,83% | +21,05% | BASSA | 8,0 | 16,5 |
| -5,00% | 0,08608 $ | 29/40 | +72,50% | +20,00% | 0,10873 $ | 6/29 | +20,69% | +26,32% | DEBOLE | 8,0 | 18,5 |
| -8,00% | 0,08336 $ | 21/40 | +52,50% | +5,00% | 0,09514 $ | 9/21 | +42,86% | +14,13% | BASSA | 12,0 | 16,7 |
| -8,00% | 0,08336 $ | 21/40 | +52,50% | +10,00% | 0,09967 $ | 9/21 | +42,86% | +19,57% | BASSA | 12,0 | 17,4 |
| -8,00% | 0,08336 $ | 21/40 | +52,50% | +15,00% | 0,10420 $ | 8/21 | +38,10% | +25,00% | BASSA | 12,0 | 16,9 |
| -8,00% | 0,08336 $ | 21/40 | +52,50% | +20,00% | 0,10873 $ | 3/21 | +14,29% | +30,43% | DEBOLE | 12,0 | 17,3 |
| -10,00% | 0,08155 $ | 17/40 | +42,50% | +5,00% | 0,09514 $ | 4/17 | +23,53% | +16,67% | DEBOLE | 15,4 | 17,0 |
| -10,00% | 0,08155 $ | 17/40 | +42,50% | +10,00% | 0,09967 $ | 4/17 | +23,53% | +22,22% | DEBOLE | 15,4 | 17,5 |
| -10,00% | 0,08155 $ | 17/40 | +42,50% | +15,00% | 0,10420 $ | 3/17 | +17,65% | +27,78% | DEBOLE | 15,4 | 13,7 |
| -10,00% | 0,08155 $ | 17/40 | +42,50% | +20,00% | 0,10873 $ | 1/17 | +5,88% | +33,33% | DEBOLE | 15,4 | 12,0 |
| -15,00% | 0,07702 $ | 11/40 | +27,50% | +5,00% | 0,09514 $ | 1/11 | +9,09% | +23,53% | DEBOLE | 18,4 | 29,0 |
| -15,00% | 0,07702 $ | 11/40 | +27,50% | +10,00% | 0,09967 $ | 1/11 | +9,09% | +29,41% | DEBOLE | 18,4 | 29,0 |
| -15,00% | 0,07702 $ | 11/40 | +27,50% | +15,00% | 0,10420 $ | 0/11 | 0,00% | +35,29% | DEBOLE | 18,4 | n/d |
| -15,00% | 0,07702 $ | 11/40 | +27,50% | +20,00% | 0,10873 $ | 0/11 | 0,00% | +41,18% | DEBOLE | 18,4 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,09514 $ | 33/40 | +82,50% | prezzo iniziale | 0,09061 $ | 17/33 | +51,52% | -4,76% | MEDIA | 7,2 | 13,5 |
| +5,00% | 0,09514 $ | 33/40 | +82,50% | -5,00% | 0,08608 $ | 11/33 | +33,33% | -9,52% | DEBOLE | 7,2 | 15,7 |
| +5,00% | 0,09514 $ | 33/40 | +82,50% | -8,00% | 0,08336 $ | 6/33 | +18,18% | -12,38% | DEBOLE | 7,2 | 22,0 |
| +5,00% | 0,09514 $ | 33/40 | +82,50% | -10,00% | 0,08155 $ | 6/33 | +18,18% | -14,29% | DEBOLE | 7,2 | 24,3 |
| +5,00% | 0,09514 $ | 33/40 | +82,50% | -15,00% | 0,07702 $ | 3/33 | +9,09% | -19,05% | DEBOLE | 7,2 | 26,7 |
| +10,00% | 0,09967 $ | 32/40 | +80,00% | prezzo iniziale | 0,09061 $ | 14/32 | +43,75% | -9,09% | BASSA | 10,7 | 19,9 |
| +10,00% | 0,09967 $ | 32/40 | +80,00% | -5,00% | 0,08608 $ | 7/32 | +21,88% | -13,64% | DEBOLE | 10,7 | 20,3 |
| +10,00% | 0,09967 $ | 32/40 | +80,00% | -8,00% | 0,08336 $ | 5/32 | +15,62% | -16,36% | DEBOLE | 10,7 | 24,2 |
| +10,00% | 0,09967 $ | 32/40 | +80,00% | -10,00% | 0,08155 $ | 5/32 | +15,62% | -18,18% | DEBOLE | 10,7 | 25,0 |
| +10,00% | 0,09967 $ | 32/40 | +80,00% | -15,00% | 0,07702 $ | 2/32 | +6,25% | -22,73% | DEBOLE | 10,7 | 29,0 |
| +15,00% | 0,10420 $ | 28/40 | +70,00% | prezzo iniziale | 0,09061 $ | 11/28 | +39,29% | -13,04% | BASSA | 11,9 | 22,8 |
| +15,00% | 0,10420 $ | 28/40 | +70,00% | -5,00% | 0,08608 $ | 5/28 | +17,86% | -17,39% | DEBOLE | 11,9 | 21,4 |
| +15,00% | 0,10420 $ | 28/40 | +70,00% | -8,00% | 0,08336 $ | 3/28 | +10,71% | -20,00% | DEBOLE | 11,9 | 24,7 |
| +15,00% | 0,10420 $ | 28/40 | +70,00% | -10,00% | 0,08155 $ | 3/28 | +10,71% | -21,74% | DEBOLE | 11,9 | 25,3 |
| +15,00% | 0,10420 $ | 28/40 | +70,00% | -15,00% | 0,07702 $ | 2/28 | +7,14% | -26,09% | DEBOLE | 11,9 | 29,0 |
| +20,00% | 0,10873 $ | 18/40 | +45,00% | prezzo iniziale | 0,09061 $ | 5/18 | +27,78% | -16,67% | DEBOLE | 13,0 | 25,6 |
| +20,00% | 0,10873 $ | 18/40 | +45,00% | -5,00% | 0,08608 $ | 2/18 | +11,11% | -20,83% | DEBOLE | 13,0 | 23,0 |
| +20,00% | 0,10873 $ | 18/40 | +45,00% | -8,00% | 0,08336 $ | 0/18 | 0,00% | -23,33% | DEBOLE | 13,0 | n/d |
| +20,00% | 0,10873 $ | 18/40 | +45,00% | -10,00% | 0,08155 $ | 0/18 | 0,00% | -25,00% | DEBOLE | 13,0 | n/d |
| +20,00% | 0,10873 $ | 18/40 | +45,00% | -15,00% | 0,07702 $ | 0/18 | 0,00% | -29,17% | DEBOLE | 13,0 | n/d |

---
