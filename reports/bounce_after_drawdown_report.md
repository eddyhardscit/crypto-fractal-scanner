# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-08 19:09:07 CEST**  
UTC: **2026-07-08 17:09:07 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 58.976 $ | 68.288 $ | +33,33% | +15,79% | rimbalzo poco frequente | 68.288 $ | 58.976 $ | +26,92% | -13,64% | spike storicamente più resistente |
| SOL | 73,34 $ | 84,92 $ | +11,11% | +15,79% | rimbalzo poco frequente | 84,92 $ | 73,34 $ | +18,75% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06882 $ | 0,07968 $ | +16,67% | +15,79% | rimbalzo poco frequente | 0,07968 $ | 0,06882 $ | +53,85% | -13,64% | attenzione a prendere profitto |

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

- BTC: su 40 casi simili, 21 prima sono scesi a -5,00%. Tra quei 21, 7 poi sono rimbalzati fino a +10,00%. Percentuale: +33,33% (7/21). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- BTC: su 40 casi simili, 26 prima sono saliti a +10,00%. Tra quei 26, 7 poi sono scaricati a -5,00%. Percentuale: +26,92% (7/26). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 58.976 $ | 21/40 | +52,50% | +5,00% | 65.184 $ | 8/21 | +38,10% | +10,53% | BASSA | 12,0 | 12,4 |
| -5,00% | 58.976 $ | 21/40 | +52,50% | +10,00% | 68.288 $ | 7/21 | +33,33% | +15,79% | DEBOLE | 12,0 | 15,0 |
| -5,00% | 58.976 $ | 21/40 | +52,50% | +15,00% | 71.392 $ | 5/21 | +23,81% | +21,05% | DEBOLE | 12,0 | 16,0 |
| -5,00% | 58.976 $ | 21/40 | +52,50% | +20,00% | 74.496 $ | 3/21 | +14,29% | +26,32% | DEBOLE | 12,0 | 16,0 |
| -8,00% | 57.114 $ | 13/40 | +32,50% | +5,00% | 65.184 $ | 4/13 | +30,77% | +14,13% | DEBOLE | 12,9 | 10,2 |
| -8,00% | 57.114 $ | 13/40 | +32,50% | +10,00% | 68.288 $ | 4/13 | +30,77% | +19,57% | DEBOLE | 12,9 | 13,2 |
| -8,00% | 57.114 $ | 13/40 | +32,50% | +15,00% | 71.392 $ | 3/13 | +23,08% | +25,00% | DEBOLE | 12,9 | 17,0 |
| -8,00% | 57.114 $ | 13/40 | +32,50% | +20,00% | 74.496 $ | 2/13 | +15,38% | +30,43% | DEBOLE | 12,9 | 18,5 |
| -10,00% | 55.872 $ | 9/40 | +22,50% | +5,00% | 65.184 $ | 2/9 | +22,22% | +16,67% | DEBOLE | 13,7 | 14,5 |
| -10,00% | 55.872 $ | 9/40 | +22,50% | +10,00% | 68.288 $ | 2/9 | +22,22% | +22,22% | DEBOLE | 13,7 | 20,0 |
| -10,00% | 55.872 $ | 9/40 | +22,50% | +15,00% | 71.392 $ | 2/9 | +22,22% | +27,78% | DEBOLE | 13,7 | 20,5 |
| -10,00% | 55.872 $ | 9/40 | +22,50% | +20,00% | 74.496 $ | 1/9 | +11,11% | +33,33% | DEBOLE | 13,7 | 26,0 |
| -15,00% | 52.768 $ | 7/40 | +17,50% | +5,00% | 65.184 $ | 2/7 | +28,57% | +23,53% | DEBOLE | 12,6 | 14,5 |
| -15,00% | 52.768 $ | 7/40 | +17,50% | +10,00% | 68.288 $ | 2/7 | +28,57% | +29,41% | DEBOLE | 12,6 | 20,0 |
| -15,00% | 52.768 $ | 7/40 | +17,50% | +15,00% | 71.392 $ | 2/7 | +28,57% | +35,29% | DEBOLE | 12,6 | 20,5 |
| -15,00% | 52.768 $ | 7/40 | +17,50% | +20,00% | 74.496 $ | 1/7 | +14,29% | +41,18% | DEBOLE | 12,6 | 26,0 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 65.184 $ | 36/40 | +90,00% | prezzo iniziale | 62.080 $ | 23/36 | +63,89% | -4,76% | MEDIA | 4,4 | 14,0 |
| +5,00% | 65.184 $ | 36/40 | +90,00% | -5,00% | 58.976 $ | 15/36 | +41,67% | -9,52% | BASSA | 4,4 | 16,2 |
| +5,00% | 65.184 $ | 36/40 | +90,00% | -8,00% | 57.114 $ | 10/36 | +27,78% | -12,38% | DEBOLE | 4,4 | 18,0 |
| +5,00% | 65.184 $ | 36/40 | +90,00% | -10,00% | 55.872 $ | 6/36 | +16,67% | -14,29% | DEBOLE | 4,4 | 17,8 |
| +5,00% | 65.184 $ | 36/40 | +90,00% | -15,00% | 52.768 $ | 4/36 | +11,11% | -19,05% | DEBOLE | 4,4 | 17,0 |
| +10,00% | 68.288 $ | 26/40 | +65,00% | prezzo iniziale | 62.080 $ | 11/26 | +42,31% | -9,09% | BASSA | 8,9 | 17,7 |
| +10,00% | 68.288 $ | 26/40 | +65,00% | -5,00% | 58.976 $ | 7/26 | +26,92% | -13,64% | DEBOLE | 8,9 | 17,1 |
| +10,00% | 68.288 $ | 26/40 | +65,00% | -8,00% | 57.114 $ | 5/26 | +19,23% | -16,36% | DEBOLE | 8,9 | 19,4 |
| +10,00% | 68.288 $ | 26/40 | +65,00% | -10,00% | 55.872 $ | 2/26 | +7,69% | -18,18% | DEBOLE | 8,9 | 22,0 |
| +10,00% | 68.288 $ | 26/40 | +65,00% | -15,00% | 52.768 $ | 1/26 | +3,85% | -22,73% | DEBOLE | 8,9 | 24,0 |
| +15,00% | 71.392 $ | 20/40 | +50,00% | prezzo iniziale | 62.080 $ | 6/20 | +30,00% | -13,04% | DEBOLE | 12,2 | 20,7 |
| +15,00% | 71.392 $ | 20/40 | +50,00% | -5,00% | 58.976 $ | 4/20 | +20,00% | -17,39% | DEBOLE | 12,2 | 22,2 |
| +15,00% | 71.392 $ | 20/40 | +50,00% | -8,00% | 57.114 $ | 2/20 | +10,00% | -20,00% | DEBOLE | 12,2 | 20,5 |
| +15,00% | 71.392 $ | 20/40 | +50,00% | -10,00% | 55.872 $ | 1/20 | +5,00% | -21,74% | DEBOLE | 12,2 | 21,0 |
| +15,00% | 71.392 $ | 20/40 | +50,00% | -15,00% | 52.768 $ | 0/20 | 0,00% | -26,09% | DEBOLE | 12,2 | n/d |
| +20,00% | 74.496 $ | 13/40 | +32,50% | prezzo iniziale | 62.080 $ | 1/13 | +7,69% | -16,67% | DEBOLE | 13,1 | 16,0 |
| +20,00% | 74.496 $ | 13/40 | +32,50% | -5,00% | 58.976 $ | 1/13 | +7,69% | -20,83% | DEBOLE | 13,1 | 28,0 |
| +20,00% | 74.496 $ | 13/40 | +32,50% | -8,00% | 57.114 $ | 0/13 | 0,00% | -23,33% | DEBOLE | 13,1 | n/d |
| +20,00% | 74.496 $ | 13/40 | +32,50% | -10,00% | 55.872 $ | 0/13 | 0,00% | -25,00% | DEBOLE | 13,1 | n/d |
| +20,00% | 74.496 $ | 13/40 | +32,50% | -15,00% | 52.768 $ | 0/13 | 0,00% | -29,17% | DEBOLE | 13,1 | n/d |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 27 prima sono scesi a -5,00%. Tra quei 27, 3 poi sono rimbalzati fino a +10,00%. Percentuale: +11,11% (3/27). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- SOL: su 40 casi simili, 16 prima sono saliti a +10,00%. Tra quei 16, 3 poi sono scaricati a -5,00%. Percentuale: +18,75% (3/16). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 73,34 $ | 27/40 | +67,50% | +5,00% | 81,06 $ | 6/27 | +22,22% | +10,53% | DEBOLE | 7,4 | 13,7 |
| -5,00% | 73,34 $ | 27/40 | +67,50% | +10,00% | 84,92 $ | 3/27 | +11,11% | +15,79% | DEBOLE | 7,4 | 11,7 |
| -5,00% | 73,34 $ | 27/40 | +67,50% | +15,00% | 88,78 $ | 2/27 | +7,41% | +21,05% | DEBOLE | 7,4 | 11,5 |
| -5,00% | 73,34 $ | 27/40 | +67,50% | +20,00% | 92,64 $ | 1/27 | +3,70% | +26,32% | DEBOLE | 7,4 | 10,0 |
| -8,00% | 71,02 $ | 24/40 | +60,00% | +5,00% | 81,06 $ | 3/24 | +12,50% | +14,13% | DEBOLE | 10,9 | 19,3 |
| -8,00% | 71,02 $ | 24/40 | +60,00% | +10,00% | 84,92 $ | 2/24 | +8,33% | +19,57% | DEBOLE | 10,9 | 15,0 |
| -8,00% | 71,02 $ | 24/40 | +60,00% | +15,00% | 88,78 $ | 1/24 | +4,17% | +25,00% | DEBOLE | 10,9 | 15,0 |
| -8,00% | 71,02 $ | 24/40 | +60,00% | +20,00% | 92,64 $ | 0/24 | 0,00% | +30,43% | DEBOLE | 10,9 | n/d |
| -10,00% | 69,48 $ | 22/40 | +55,00% | +5,00% | 81,06 $ | 2/22 | +9,09% | +16,67% | DEBOLE | 11,5 | 14,0 |
| -10,00% | 69,48 $ | 22/40 | +55,00% | +10,00% | 84,92 $ | 2/22 | +9,09% | +22,22% | DEBOLE | 11,5 | 15,0 |
| -10,00% | 69,48 $ | 22/40 | +55,00% | +15,00% | 88,78 $ | 1/22 | +4,55% | +27,78% | DEBOLE | 11,5 | 15,0 |
| -10,00% | 69,48 $ | 22/40 | +55,00% | +20,00% | 92,64 $ | 0/22 | 0,00% | +33,33% | DEBOLE | 11,5 | n/d |
| -15,00% | 65,62 $ | 16/40 | +40,00% | +5,00% | 81,06 $ | 2/16 | +12,50% | +23,53% | DEBOLE | 13,2 | 14,0 |
| -15,00% | 65,62 $ | 16/40 | +40,00% | +10,00% | 84,92 $ | 2/16 | +12,50% | +29,41% | DEBOLE | 13,2 | 15,0 |
| -15,00% | 65,62 $ | 16/40 | +40,00% | +15,00% | 88,78 $ | 1/16 | +6,25% | +35,29% | DEBOLE | 13,2 | 15,0 |
| -15,00% | 65,62 $ | 16/40 | +40,00% | +20,00% | 92,64 $ | 0/16 | 0,00% | +41,18% | DEBOLE | 13,2 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 81,06 $ | 26/40 | +65,00% | prezzo iniziale | 77,20 $ | 17/26 | +65,38% | -4,76% | ALTA | 3,9 | 11,7 |
| +5,00% | 81,06 $ | 26/40 | +65,00% | -5,00% | 73,34 $ | 12/26 | +46,15% | -9,52% | BASSA | 3,9 | 12,7 |
| +5,00% | 81,06 $ | 26/40 | +65,00% | -8,00% | 71,02 $ | 12/26 | +46,15% | -12,38% | BASSA | 3,9 | 16,0 |
| +5,00% | 81,06 $ | 26/40 | +65,00% | -10,00% | 69,48 $ | 9/26 | +34,62% | -14,29% | DEBOLE | 3,9 | 14,9 |
| +5,00% | 81,06 $ | 26/40 | +65,00% | -15,00% | 65,62 $ | 5/26 | +19,23% | -19,05% | DEBOLE | 3,9 | 16,2 |
| +10,00% | 84,92 $ | 16/40 | +40,00% | prezzo iniziale | 77,20 $ | 6/16 | +37,50% | -9,09% | BASSA | 6,4 | 16,2 |
| +10,00% | 84,92 $ | 16/40 | +40,00% | -5,00% | 73,34 $ | 3/16 | +18,75% | -13,64% | DEBOLE | 6,4 | 17,0 |
| +10,00% | 84,92 $ | 16/40 | +40,00% | -8,00% | 71,02 $ | 3/16 | +18,75% | -16,36% | DEBOLE | 6,4 | 17,0 |
| +10,00% | 84,92 $ | 16/40 | +40,00% | -10,00% | 69,48 $ | 1/16 | +6,25% | -18,18% | DEBOLE | 6,4 | 14,0 |
| +10,00% | 84,92 $ | 16/40 | +40,00% | -15,00% | 65,62 $ | 1/16 | +6,25% | -22,73% | DEBOLE | 6,4 | 14,0 |
| +15,00% | 88,78 $ | 13/40 | +32,50% | prezzo iniziale | 77,20 $ | 4/13 | +30,77% | -13,04% | DEBOLE | 9,7 | 15,5 |
| +15,00% | 88,78 $ | 13/40 | +32,50% | -5,00% | 73,34 $ | 2/13 | +15,38% | -17,39% | DEBOLE | 9,7 | 18,5 |
| +15,00% | 88,78 $ | 13/40 | +32,50% | -8,00% | 71,02 $ | 2/13 | +15,38% | -20,00% | DEBOLE | 9,7 | 18,5 |
| +15,00% | 88,78 $ | 13/40 | +32,50% | -10,00% | 69,48 $ | 0/13 | 0,00% | -21,74% | DEBOLE | 9,7 | n/d |
| +15,00% | 88,78 $ | 13/40 | +32,50% | -15,00% | 65,62 $ | 0/13 | 0,00% | -26,09% | DEBOLE | 9,7 | n/d |
| +20,00% | 92,64 $ | 9/40 | +22,50% | prezzo iniziale | 77,20 $ | 0/9 | 0,00% | -16,67% | DEBOLE | 12,2 | n/d |
| +20,00% | 92,64 $ | 9/40 | +22,50% | -5,00% | 73,34 $ | 0/9 | 0,00% | -20,83% | DEBOLE | 12,2 | n/d |
| +20,00% | 92,64 $ | 9/40 | +22,50% | -8,00% | 71,02 $ | 0/9 | 0,00% | -23,33% | DEBOLE | 12,2 | n/d |
| +20,00% | 92,64 $ | 9/40 | +22,50% | -10,00% | 69,48 $ | 0/9 | 0,00% | -25,00% | DEBOLE | 12,2 | n/d |
| +20,00% | 92,64 $ | 9/40 | +22,50% | -15,00% | 65,62 $ | 0/9 | 0,00% | -29,17% | DEBOLE | 12,2 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 36 prima sono scesi a -5,00%. Tra quei 36, 6 poi sono rimbalzati fino a +10,00%. Percentuale: +16,67% (6/36). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 13 prima sono saliti a +10,00%. Tra quei 13, 7 poi sono scaricati a -5,00%. Percentuale: +53,85% (7/13). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06882 $ | 36/40 | +90,00% | +5,00% | 0,07606 $ | 9/36 | +25,00% | +10,53% | DEBOLE | 5,3 | 15,2 |
| -5,00% | 0,06882 $ | 36/40 | +90,00% | +10,00% | 0,07968 $ | 6/36 | +16,67% | +15,79% | DEBOLE | 5,3 | 13,7 |
| -5,00% | 0,06882 $ | 36/40 | +90,00% | +15,00% | 0,08331 $ | 6/36 | +16,67% | +21,05% | DEBOLE | 5,3 | 16,0 |
| -5,00% | 0,06882 $ | 36/40 | +90,00% | +20,00% | 0,08693 $ | 6/36 | +16,67% | +26,32% | DEBOLE | 5,3 | 16,8 |
| -8,00% | 0,06664 $ | 34/40 | +85,00% | +5,00% | 0,07606 $ | 7/34 | +20,59% | +14,13% | DEBOLE | 7,5 | 17,4 |
| -8,00% | 0,06664 $ | 34/40 | +85,00% | +10,00% | 0,07968 $ | 4/34 | +11,76% | +19,57% | DEBOLE | 7,5 | 16,2 |
| -8,00% | 0,06664 $ | 34/40 | +85,00% | +15,00% | 0,08331 $ | 4/34 | +11,76% | +25,00% | DEBOLE | 7,5 | 19,2 |
| -8,00% | 0,06664 $ | 34/40 | +85,00% | +20,00% | 0,08693 $ | 4/34 | +11,76% | +30,43% | DEBOLE | 7,5 | 20,0 |
| -10,00% | 0,06520 $ | 32/40 | +80,00% | +5,00% | 0,07606 $ | 5/32 | +15,62% | +16,67% | DEBOLE | 8,1 | 17,6 |
| -10,00% | 0,06520 $ | 32/40 | +80,00% | +10,00% | 0,07968 $ | 2/32 | +6,25% | +22,22% | DEBOLE | 8,1 | 15,0 |
| -10,00% | 0,06520 $ | 32/40 | +80,00% | +15,00% | 0,08331 $ | 2/32 | +6,25% | +27,78% | DEBOLE | 8,1 | 15,5 |
| -10,00% | 0,06520 $ | 32/40 | +80,00% | +20,00% | 0,08693 $ | 2/32 | +6,25% | +33,33% | DEBOLE | 8,1 | 15,5 |
| -15,00% | 0,06157 $ | 30/40 | +75,00% | +5,00% | 0,07606 $ | 4/30 | +13,33% | +23,53% | DEBOLE | 10,8 | 15,8 |
| -15,00% | 0,06157 $ | 30/40 | +75,00% | +10,00% | 0,07968 $ | 2/30 | +6,67% | +29,41% | DEBOLE | 10,8 | 15,0 |
| -15,00% | 0,06157 $ | 30/40 | +75,00% | +15,00% | 0,08331 $ | 2/30 | +6,67% | +35,29% | DEBOLE | 10,8 | 15,5 |
| -15,00% | 0,06157 $ | 30/40 | +75,00% | +20,00% | 0,08693 $ | 2/30 | +6,67% | +41,18% | DEBOLE | 10,8 | 15,5 |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07606 $ | 18/40 | +45,00% | prezzo iniziale | 0,07244 $ | 14/18 | +77,78% | -4,76% | ALTA | 8,6 | 11,9 |
| +5,00% | 0,07606 $ | 18/40 | +45,00% | -5,00% | 0,06882 $ | 12/18 | +66,67% | -9,52% | ALTA | 8,6 | 15,2 |
| +5,00% | 0,07606 $ | 18/40 | +45,00% | -8,00% | 0,06664 $ | 10/18 | +55,56% | -12,38% | MEDIA | 8,6 | 14,6 |
| +5,00% | 0,07606 $ | 18/40 | +45,00% | -10,00% | 0,06520 $ | 9/18 | +50,00% | -14,29% | MEDIA | 8,6 | 15,3 |
| +5,00% | 0,07606 $ | 18/40 | +45,00% | -15,00% | 0,06157 $ | 8/18 | +44,44% | -19,05% | BASSA | 8,6 | 15,0 |
| +10,00% | 0,07968 $ | 13/40 | +32,50% | prezzo iniziale | 0,07244 $ | 7/13 | +53,85% | -9,09% | MEDIA | 10,8 | 12,6 |
| +10,00% | 0,07968 $ | 13/40 | +32,50% | -5,00% | 0,06882 $ | 7/13 | +53,85% | -13,64% | MEDIA | 10,8 | 13,6 |
| +10,00% | 0,07968 $ | 13/40 | +32,50% | -8,00% | 0,06664 $ | 6/13 | +46,15% | -16,36% | BASSA | 10,8 | 13,8 |
| +10,00% | 0,07968 $ | 13/40 | +32,50% | -10,00% | 0,06520 $ | 5/13 | +38,46% | -18,18% | BASSA | 10,8 | 15,0 |
| +10,00% | 0,07968 $ | 13/40 | +32,50% | -15,00% | 0,06157 $ | 5/13 | +38,46% | -22,73% | BASSA | 10,8 | 16,6 |
| +15,00% | 0,08331 $ | 9/40 | +22,50% | prezzo iniziale | 0,07244 $ | 3/9 | +33,33% | -13,04% | DEBOLE | 13,0 | 13,0 |
| +15,00% | 0,08331 $ | 9/40 | +22,50% | -5,00% | 0,06882 $ | 3/9 | +33,33% | -17,39% | DEBOLE | 13,0 | 13,3 |
| +15,00% | 0,08331 $ | 9/40 | +22,50% | -8,00% | 0,06664 $ | 3/9 | +33,33% | -20,00% | DEBOLE | 13,0 | 13,7 |
| +15,00% | 0,08331 $ | 9/40 | +22,50% | -10,00% | 0,06520 $ | 2/9 | +22,22% | -21,74% | DEBOLE | 13,0 | 16,0 |
| +15,00% | 0,08331 $ | 9/40 | +22,50% | -15,00% | 0,06157 $ | 2/9 | +22,22% | -26,09% | DEBOLE | 13,0 | 18,0 |
| +20,00% | 0,08693 $ | 7/40 | +17,50% | prezzo iniziale | 0,07244 $ | 3/7 | +42,86% | -16,67% | BASSA | 17,0 | 19,0 |
| +20,00% | 0,08693 $ | 7/40 | +17,50% | -5,00% | 0,06882 $ | 2/7 | +28,57% | -20,83% | DEBOLE | 17,0 | 15,5 |
| +20,00% | 0,08693 $ | 7/40 | +17,50% | -8,00% | 0,06664 $ | 2/7 | +28,57% | -23,33% | DEBOLE | 17,0 | 16,0 |
| +20,00% | 0,08693 $ | 7/40 | +17,50% | -10,00% | 0,06520 $ | 2/7 | +28,57% | -25,00% | DEBOLE | 17,0 | 16,0 |
| +20,00% | 0,08693 $ | 7/40 | +17,50% | -15,00% | 0,06157 $ | 2/7 | +28,57% | -29,17% | DEBOLE | 17,0 | 18,0 |

---
