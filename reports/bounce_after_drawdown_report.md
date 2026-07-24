# Sequenze pratiche: rimbalzo dopo discesa / dump dopo spike

Generato: **2026-07-24 07:13:55 CEST**  
UTC: **2026-07-24 05:13:55 UTC**

Questo report guarda l'ordine degli eventi nei 40 casi storici più simili.

- **Prima scende → poi rimbalza**: utile per capire se una discesa può diventare zona di rimbalzo.
- **Prima sale → poi scarica**: utile per capire se una salita forte può diventare zona da prendere profitto.

## Lettura pratica veloce

| Asset | Se scende a -5% | Target +10% | % casi | Movimento reale | Lettura discesa | Se sale a +10% | Target -5% | % casi | Movimento reale | Lettura spike |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 62.042 $ | 71.838 $ | +48,57% | +15,79% | rimbalzo debole | 71.838 $ | 62.042 $ | +13,04% | -13,64% | spike storicamente più resistente |
| SOL | 71,93 $ | 83,29 $ | +37,93% | +15,79% | rimbalzo debole | 83,29 $ | 71,93 $ | +14,29% | -13,64% | spike storicamente più resistente |
| DOGE | 0,06555 $ | 0,07590 $ | +30,30% | +15,79% | rimbalzo poco frequente | 0,07590 $ | 0,06555 $ | +52,00% | -13,64% | attenzione a prendere profitto |

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

- BTC: su 40 casi simili, 35 prima sono scesi a -5,00%. Tra quei 35, 17 poi sono rimbalzati fino a +10,00%. Percentuale: +48,57% (17/35). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- BTC: su 40 casi simili, 23 prima sono saliti a +10,00%. Tra quei 23, 3 poi sono scaricati a -5,00%. Percentuale: +13,04% (3/23). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 62.042 $ | 35/40 | +87,50% | +5,00% | 68.573 $ | 21/35 | +60,00% | +10,53% | MEDIA | 5,3 | 19,3 |
| -5,00% | 62.042 $ | 35/40 | +87,50% | +10,00% | 71.838 $ | 17/35 | +48,57% | +15,79% | BASSA | 5,3 | 21,2 |
| -5,00% | 62.042 $ | 35/40 | +87,50% | +15,00% | 75.104 $ | 14/35 | +40,00% | +21,05% | BASSA | 5,3 | 25,2 |
| -5,00% | 62.042 $ | 35/40 | +87,50% | +20,00% | 78.369 $ | 12/35 | +34,29% | +26,32% | DEBOLE | 5,3 | 26,7 |
| -8,00% | 60.083 $ | 26/40 | +65,00% | +5,00% | 68.573 $ | 13/26 | +50,00% | +14,13% | MEDIA | 8,3 | 21,1 |
| -8,00% | 60.083 $ | 26/40 | +65,00% | +10,00% | 71.838 $ | 10/26 | +38,46% | +19,57% | BASSA | 8,3 | 22,2 |
| -8,00% | 60.083 $ | 26/40 | +65,00% | +15,00% | 75.104 $ | 8/26 | +30,77% | +25,00% | DEBOLE | 8,3 | 25,1 |
| -8,00% | 60.083 $ | 26/40 | +65,00% | +20,00% | 78.369 $ | 7/26 | +26,92% | +30,43% | DEBOLE | 8,3 | 25,9 |
| -10,00% | 58.777 $ | 22/40 | +55,00% | +5,00% | 68.573 $ | 9/22 | +40,91% | +16,67% | BASSA | 10,9 | 21,2 |
| -10,00% | 58.777 $ | 22/40 | +55,00% | +10,00% | 71.838 $ | 7/22 | +31,82% | +22,22% | DEBOLE | 10,9 | 23,0 |
| -10,00% | 58.777 $ | 22/40 | +55,00% | +15,00% | 75.104 $ | 6/22 | +27,27% | +27,78% | DEBOLE | 10,9 | 24,7 |
| -10,00% | 58.777 $ | 22/40 | +55,00% | +20,00% | 78.369 $ | 6/22 | +27,27% | +33,33% | DEBOLE | 10,9 | 25,5 |
| -15,00% | 55.511 $ | 13/40 | +32,50% | +5,00% | 68.573 $ | 1/13 | +7,69% | +23,53% | DEBOLE | 14,9 | 21,0 |
| -15,00% | 55.511 $ | 13/40 | +32,50% | +10,00% | 71.838 $ | 0/13 | 0,00% | +29,41% | DEBOLE | 14,9 | n/d |
| -15,00% | 55.511 $ | 13/40 | +32,50% | +15,00% | 75.104 $ | 0/13 | 0,00% | +35,29% | DEBOLE | 14,9 | n/d |
| -15,00% | 55.511 $ | 13/40 | +32,50% | +20,00% | 78.369 $ | 0/13 | 0,00% | +41,18% | DEBOLE | 14,9 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 68.573 $ | 31/40 | +77,50% | prezzo iniziale | 65.307 $ | 14/31 | +45,16% | -4,76% | BASSA | 14,2 | 13,1 |
| +5,00% | 68.573 $ | 31/40 | +77,50% | -5,00% | 62.042 $ | 11/31 | +35,48% | -9,52% | BASSA | 14,2 | 13,4 |
| +5,00% | 68.573 $ | 31/40 | +77,50% | -8,00% | 60.083 $ | 9/31 | +29,03% | -12,38% | DEBOLE | 14,2 | 14,6 |
| +5,00% | 68.573 $ | 31/40 | +77,50% | -10,00% | 58.777 $ | 7/31 | +22,58% | -14,29% | DEBOLE | 14,2 | 14,6 |
| +5,00% | 68.573 $ | 31/40 | +77,50% | -15,00% | 55.511 $ | 6/31 | +19,35% | -19,05% | DEBOLE | 14,2 | 18,3 |
| +10,00% | 71.838 $ | 23/40 | +57,50% | prezzo iniziale | 65.307 $ | 4/23 | +17,39% | -9,09% | DEBOLE | 18,5 | 18,0 |
| +10,00% | 71.838 $ | 23/40 | +57,50% | -5,00% | 62.042 $ | 3/23 | +13,04% | -13,64% | DEBOLE | 18,5 | 17,0 |
| +10,00% | 71.838 $ | 23/40 | +57,50% | -8,00% | 60.083 $ | 2/23 | +8,70% | -16,36% | DEBOLE | 18,5 | 19,0 |
| +10,00% | 71.838 $ | 23/40 | +57,50% | -10,00% | 58.777 $ | 2/23 | +8,70% | -18,18% | DEBOLE | 18,5 | 19,0 |
| +10,00% | 71.838 $ | 23/40 | +57,50% | -15,00% | 55.511 $ | 2/23 | +8,70% | -22,73% | DEBOLE | 18,5 | 19,5 |
| +15,00% | 75.104 $ | 19/40 | +47,50% | prezzo iniziale | 65.307 $ | 1/19 | +5,26% | -13,04% | DEBOLE | 22,5 | 17,0 |
| +15,00% | 75.104 $ | 19/40 | +47,50% | -5,00% | 62.042 $ | 1/19 | +5,26% | -17,39% | DEBOLE | 22,5 | 17,0 |
| +15,00% | 75.104 $ | 19/40 | +47,50% | -8,00% | 60.083 $ | 1/19 | +5,26% | -20,00% | DEBOLE | 22,5 | 17,0 |
| +15,00% | 75.104 $ | 19/40 | +47,50% | -10,00% | 58.777 $ | 1/19 | +5,26% | -21,74% | DEBOLE | 22,5 | 17,0 |
| +15,00% | 75.104 $ | 19/40 | +47,50% | -15,00% | 55.511 $ | 1/19 | +5,26% | -26,09% | DEBOLE | 22,5 | 18,0 |
| +20,00% | 78.369 $ | 16/40 | +40,00% | prezzo iniziale | 65.307 $ | 1/16 | +6,25% | -16,67% | DEBOLE | 24,2 | 17,0 |
| +20,00% | 78.369 $ | 16/40 | +40,00% | -5,00% | 62.042 $ | 1/16 | +6,25% | -20,83% | DEBOLE | 24,2 | 17,0 |
| +20,00% | 78.369 $ | 16/40 | +40,00% | -8,00% | 60.083 $ | 1/16 | +6,25% | -23,33% | DEBOLE | 24,2 | 17,0 |
| +20,00% | 78.369 $ | 16/40 | +40,00% | -10,00% | 58.777 $ | 1/16 | +6,25% | -25,00% | DEBOLE | 24,2 | 17,0 |
| +20,00% | 78.369 $ | 16/40 | +40,00% | -15,00% | 55.511 $ | 1/16 | +6,25% | -29,17% | DEBOLE | 24,2 | 18,0 |

---

# Solana — SOL

## Lettura semplice

- SOL: su 40 casi simili, 29 prima sono scesi a -5,00%. Tra quei 29, 11 poi sono rimbalzati fino a +10,00%. Percentuale: +37,93% (11/29). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo debole.
- SOL: su 40 casi simili, 21 prima sono saliti a +10,00%. Tra quei 21, 3 poi sono scaricati a -5,00%. Percentuale: +14,29% (3/21). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: spike storicamente più resistente.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 71,93 $ | 29/40 | +72,50% | +5,00% | 79,51 $ | 15/29 | +51,72% | +10,53% | MEDIA | 7,5 | 17,1 |
| -5,00% | 71,93 $ | 29/40 | +72,50% | +10,00% | 83,29 $ | 11/29 | +37,93% | +15,79% | BASSA | 7,5 | 20,6 |
| -5,00% | 71,93 $ | 29/40 | +72,50% | +15,00% | 87,08 $ | 8/29 | +27,59% | +21,05% | DEBOLE | 7,5 | 22,4 |
| -5,00% | 71,93 $ | 29/40 | +72,50% | +20,00% | 90,86 $ | 7/29 | +24,14% | +26,32% | DEBOLE | 7,5 | 23,3 |
| -8,00% | 69,66 $ | 22/40 | +55,00% | +5,00% | 79,51 $ | 9/22 | +40,91% | +14,13% | BASSA | 10,6 | 18,4 |
| -8,00% | 69,66 $ | 22/40 | +55,00% | +10,00% | 83,29 $ | 7/22 | +31,82% | +19,57% | DEBOLE | 10,6 | 21,7 |
| -8,00% | 69,66 $ | 22/40 | +55,00% | +15,00% | 87,08 $ | 5/22 | +22,73% | +25,00% | DEBOLE | 10,6 | 23,8 |
| -8,00% | 69,66 $ | 22/40 | +55,00% | +20,00% | 90,86 $ | 4/22 | +18,18% | +30,43% | DEBOLE | 10,6 | 25,2 |
| -10,00% | 68,15 $ | 15/40 | +37,50% | +5,00% | 79,51 $ | 3/15 | +20,00% | +16,67% | DEBOLE | 14,0 | 23,0 |
| -10,00% | 68,15 $ | 15/40 | +37,50% | +10,00% | 83,29 $ | 2/15 | +13,33% | +22,22% | DEBOLE | 14,0 | 27,5 |
| -10,00% | 68,15 $ | 15/40 | +37,50% | +15,00% | 87,08 $ | 2/15 | +13,33% | +27,78% | DEBOLE | 14,0 | 28,0 |
| -10,00% | 68,15 $ | 15/40 | +37,50% | +20,00% | 90,86 $ | 2/15 | +13,33% | +33,33% | DEBOLE | 14,0 | 28,0 |
| -15,00% | 64,36 $ | 8/40 | +20,00% | +5,00% | 79,51 $ | 1/8 | +12,50% | +23,53% | DEBOLE | 17,5 | 21,0 |
| -15,00% | 64,36 $ | 8/40 | +20,00% | +10,00% | 83,29 $ | 0/8 | 0,00% | +29,41% | DEBOLE | 17,5 | n/d |
| -15,00% | 64,36 $ | 8/40 | +20,00% | +15,00% | 87,08 $ | 0/8 | 0,00% | +35,29% | DEBOLE | 17,5 | n/d |
| -15,00% | 64,36 $ | 8/40 | +20,00% | +20,00% | 90,86 $ | 0/8 | 0,00% | +41,18% | DEBOLE | 17,5 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 79,51 $ | 31/40 | +77,50% | prezzo iniziale | 75,72 $ | 12/31 | +38,71% | -4,76% | BASSA | 13,0 | 15,4 |
| +5,00% | 79,51 $ | 31/40 | +77,50% | -5,00% | 71,93 $ | 8/31 | +25,81% | -9,52% | DEBOLE | 13,0 | 21,1 |
| +5,00% | 79,51 $ | 31/40 | +77,50% | -8,00% | 69,66 $ | 5/31 | +16,13% | -12,38% | DEBOLE | 13,0 | 20,8 |
| +5,00% | 79,51 $ | 31/40 | +77,50% | -10,00% | 68,15 $ | 4/31 | +12,90% | -14,29% | DEBOLE | 13,0 | 23,5 |
| +5,00% | 79,51 $ | 31/40 | +77,50% | -15,00% | 64,36 $ | 3/31 | +9,68% | -19,05% | DEBOLE | 13,0 | 25,0 |
| +10,00% | 83,29 $ | 21/40 | +52,50% | prezzo iniziale | 75,72 $ | 4/21 | +19,05% | -9,09% | DEBOLE | 16,3 | 20,5 |
| +10,00% | 83,29 $ | 21/40 | +52,50% | -5,00% | 71,93 $ | 3/21 | +14,29% | -13,64% | DEBOLE | 16,3 | 27,0 |
| +10,00% | 83,29 $ | 21/40 | +52,50% | -8,00% | 69,66 $ | 1/21 | +4,76% | -16,36% | DEBOLE | 16,3 | 24,0 |
| +10,00% | 83,29 $ | 21/40 | +52,50% | -10,00% | 68,15 $ | 1/21 | +4,76% | -18,18% | DEBOLE | 16,3 | 24,0 |
| +10,00% | 83,29 $ | 21/40 | +52,50% | -15,00% | 64,36 $ | 0/21 | 0,00% | -22,73% | DEBOLE | 16,3 | n/d |
| +15,00% | 87,08 $ | 18/40 | +45,00% | prezzo iniziale | 75,72 $ | 2/18 | +11,11% | -13,04% | DEBOLE | 18,6 | 22,0 |
| +15,00% | 87,08 $ | 18/40 | +45,00% | -5,00% | 71,93 $ | 2/18 | +11,11% | -17,39% | DEBOLE | 18,6 | 25,5 |
| +15,00% | 87,08 $ | 18/40 | +45,00% | -8,00% | 69,66 $ | 1/18 | +5,56% | -20,00% | DEBOLE | 18,6 | 24,0 |
| +15,00% | 87,08 $ | 18/40 | +45,00% | -10,00% | 68,15 $ | 1/18 | +5,56% | -21,74% | DEBOLE | 18,6 | 24,0 |
| +15,00% | 87,08 $ | 18/40 | +45,00% | -15,00% | 64,36 $ | 0/18 | 0,00% | -26,09% | DEBOLE | 18,6 | n/d |
| +20,00% | 90,86 $ | 13/40 | +32,50% | prezzo iniziale | 75,72 $ | 1/13 | +7,69% | -16,67% | DEBOLE | 17,7 | 19,0 |
| +20,00% | 90,86 $ | 13/40 | +32,50% | -5,00% | 71,93 $ | 1/13 | +7,69% | -20,83% | DEBOLE | 17,7 | 23,0 |
| +20,00% | 90,86 $ | 13/40 | +32,50% | -8,00% | 69,66 $ | 1/13 | +7,69% | -23,33% | DEBOLE | 17,7 | 24,0 |
| +20,00% | 90,86 $ | 13/40 | +32,50% | -10,00% | 68,15 $ | 1/13 | +7,69% | -25,00% | DEBOLE | 17,7 | 24,0 |
| +20,00% | 90,86 $ | 13/40 | +32,50% | -15,00% | 64,36 $ | 0/13 | 0,00% | -29,17% | DEBOLE | 17,7 | n/d |

---

# Dogecoin — DOGE

## Lettura semplice

- DOGE: su 40 casi simili, 33 prima sono scesi a -5,00%. Tra quei 33, 10 poi sono rimbalzati fino a +10,00%. Percentuale: +30,30% (10/33). Dal livello -5,00% al target +10,00% il movimento reale sarebbe circa +15,79%. Lettura: rimbalzo poco frequente.
- DOGE: su 40 casi simili, 25 prima sono saliti a +10,00%. Tra quei 25, 13 poi sono scaricati a -5,00%. Percentuale: +52,00% (13/25). Dal livello +10,00% al target -5,00% il movimento reale sarebbe circa -13,64%. Lettura: attenzione a prendere profitto.

## Tabella rimbalzo dopo discesa

| Prima scende | Prezzo | Casi scesi | % casi scesi | Poi rimbalza a | Prezzo target | Casi riusciti | % riusciti | Movimento reale | Forza | Giorni discesa | Giorni target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -5,00% | 0,06555 $ | 33/40 | +82,50% | +5,00% | 0,07245 $ | 16/33 | +48,48% | +10,53% | BASSA | 7,3 | 16,6 |
| -5,00% | 0,06555 $ | 33/40 | +82,50% | +10,00% | 0,07590 $ | 10/33 | +30,30% | +15,79% | DEBOLE | 7,3 | 18,4 |
| -5,00% | 0,06555 $ | 33/40 | +82,50% | +15,00% | 0,07935 $ | 5/33 | +15,15% | +21,05% | DEBOLE | 7,3 | 20,0 |
| -5,00% | 0,06555 $ | 33/40 | +82,50% | +20,00% | 0,08280 $ | 3/33 | +9,09% | +26,32% | DEBOLE | 7,3 | 27,0 |
| -8,00% | 0,06348 $ | 26/40 | +65,00% | +5,00% | 0,07245 $ | 7/26 | +26,92% | +14,13% | DEBOLE | 10,4 | 16,4 |
| -8,00% | 0,06348 $ | 26/40 | +65,00% | +10,00% | 0,07590 $ | 4/26 | +15,38% | +19,57% | DEBOLE | 10,4 | 17,8 |
| -8,00% | 0,06348 $ | 26/40 | +65,00% | +15,00% | 0,07935 $ | 2/26 | +7,69% | +25,00% | DEBOLE | 10,4 | 17,5 |
| -8,00% | 0,06348 $ | 26/40 | +65,00% | +20,00% | 0,08280 $ | 1/26 | +3,85% | +30,43% | DEBOLE | 10,4 | 30,0 |
| -10,00% | 0,06210 $ | 24/40 | +60,00% | +5,00% | 0,07245 $ | 7/24 | +29,17% | +16,67% | DEBOLE | 10,5 | 16,4 |
| -10,00% | 0,06210 $ | 24/40 | +60,00% | +10,00% | 0,07590 $ | 4/24 | +16,67% | +22,22% | DEBOLE | 10,5 | 17,8 |
| -10,00% | 0,06210 $ | 24/40 | +60,00% | +15,00% | 0,07935 $ | 2/24 | +8,33% | +27,78% | DEBOLE | 10,5 | 17,5 |
| -10,00% | 0,06210 $ | 24/40 | +60,00% | +20,00% | 0,08280 $ | 1/24 | +4,17% | +33,33% | DEBOLE | 10,5 | 30,0 |
| -15,00% | 0,05865 $ | 17/40 | +42,50% | +5,00% | 0,07245 $ | 4/17 | +23,53% | +23,53% | DEBOLE | 10,4 | 14,8 |
| -15,00% | 0,05865 $ | 17/40 | +42,50% | +10,00% | 0,07590 $ | 3/17 | +17,65% | +29,41% | DEBOLE | 10,4 | 16,0 |
| -15,00% | 0,05865 $ | 17/40 | +42,50% | +15,00% | 0,07935 $ | 1/17 | +5,88% | +35,29% | DEBOLE | 10,4 | 10,0 |
| -15,00% | 0,05865 $ | 17/40 | +42,50% | +20,00% | 0,08280 $ | 0/17 | 0,00% | +41,18% | DEBOLE | 10,4 | n/d |

## Tabella dump dopo spike

| Prima sale | Prezzo spike | Casi spike | % casi spike | Poi scarica a | Prezzo target | Casi scarico | % scarico | Movimento reale | Forza | Giorni spike | Giorni dump |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +5,00% | 0,07245 $ | 31/40 | +77,50% | prezzo iniziale | 0,06900 $ | 23/31 | +74,19% | -4,76% | ALTA | 7,0 | 12,7 |
| +5,00% | 0,07245 $ | 31/40 | +77,50% | -5,00% | 0,06555 $ | 20/31 | +64,52% | -9,52% | MEDIA | 7,0 | 16,5 |
| +5,00% | 0,07245 $ | 31/40 | +77,50% | -8,00% | 0,06348 $ | 14/31 | +45,16% | -12,38% | BASSA | 7,0 | 19,2 |
| +5,00% | 0,07245 $ | 31/40 | +77,50% | -10,00% | 0,06210 $ | 12/31 | +38,71% | -14,29% | BASSA | 7,0 | 19,8 |
| +5,00% | 0,07245 $ | 31/40 | +77,50% | -15,00% | 0,05865 $ | 4/31 | +12,90% | -19,05% | DEBOLE | 7,0 | 18,8 |
| +10,00% | 0,07590 $ | 25/40 | +62,50% | prezzo iniziale | 0,06900 $ | 15/25 | +60,00% | -9,09% | MEDIA | 8,5 | 13,7 |
| +10,00% | 0,07590 $ | 25/40 | +62,50% | -5,00% | 0,06555 $ | 13/25 | +52,00% | -13,64% | MEDIA | 8,5 | 19,2 |
| +10,00% | 0,07590 $ | 25/40 | +62,50% | -8,00% | 0,06348 $ | 8/25 | +32,00% | -16,36% | DEBOLE | 8,5 | 18,6 |
| +10,00% | 0,07590 $ | 25/40 | +62,50% | -10,00% | 0,06210 $ | 6/25 | +24,00% | -18,18% | DEBOLE | 8,5 | 18,7 |
| +10,00% | 0,07590 $ | 25/40 | +62,50% | -15,00% | 0,05865 $ | 2/25 | +8,00% | -22,73% | DEBOLE | 8,5 | 17,5 |
| +15,00% | 0,07935 $ | 18/40 | +45,00% | prezzo iniziale | 0,06900 $ | 9/18 | +50,00% | -13,04% | MEDIA | 9,5 | 13,6 |
| +15,00% | 0,07935 $ | 18/40 | +45,00% | -5,00% | 0,06555 $ | 7/18 | +38,89% | -17,39% | BASSA | 9,5 | 20,1 |
| +15,00% | 0,07935 $ | 18/40 | +45,00% | -8,00% | 0,06348 $ | 4/18 | +22,22% | -20,00% | DEBOLE | 9,5 | 16,0 |
| +15,00% | 0,07935 $ | 18/40 | +45,00% | -10,00% | 0,06210 $ | 3/18 | +16,67% | -21,74% | DEBOLE | 9,5 | 17,0 |
| +15,00% | 0,07935 $ | 18/40 | +45,00% | -15,00% | 0,05865 $ | 1/18 | +5,56% | -26,09% | DEBOLE | 9,5 | 14,0 |
| +20,00% | 0,08280 $ | 11/40 | +27,50% | prezzo iniziale | 0,06900 $ | 3/11 | +27,27% | -16,67% | DEBOLE | 13,2 | 16,3 |
| +20,00% | 0,08280 $ | 11/40 | +27,50% | -5,00% | 0,06555 $ | 2/11 | +18,18% | -20,83% | DEBOLE | 13,2 | 26,0 |
| +20,00% | 0,08280 $ | 11/40 | +27,50% | -8,00% | 0,06348 $ | 0/11 | 0,00% | -23,33% | DEBOLE | 13,2 | n/d |
| +20,00% | 0,08280 $ | 11/40 | +27,50% | -10,00% | 0,06210 $ | 0/11 | 0,00% | -25,00% | DEBOLE | 13,2 | n/d |
| +20,00% | 0,08280 $ | 11/40 | +27,50% | -15,00% | 0,05865 $ | 0/11 | 0,00% | -29,17% | DEBOLE | 13,2 | n/d |

---
