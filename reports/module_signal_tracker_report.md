# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-08-08 05:19 UTC

Questo report salva ogni giorno i segnali dei moduli e controlla ogni giorno quali orizzonti sono maturati.

La calibrazione ora controlla questi orizzonti:

- **1g / 2g / 3g** = feedback rapidissimo
- **5g / 7g / 10g** = feedback settimanale
- **14g / 21g** = feedback swing
- **30g / 45g / 60g** = feedback più serio

Moduli controllati:

- Global Confluence = benchmark dell'aggregato finale
- **Famiglia statistica Scanner + Market Regime = modulo calibrabile reale**
- Scanner grezzo = diagnostico, già incluso nella famiglia statistica
- Market Regime grezzo = diagnostico, già incluso nella famiglia statistica
- Struttura tecnica
- Classic technical confirmation
- Microstruttura exchange, OI/funding/taker flow/order book
- Frattale SOL/BTC, solo per SOL

Regola anti-doppio-conteggio: **Scanner e Market Regime continuano a essere misurati separatamente solo per diagnosi, ma non devono ricevere due modifiche di peso autonome**. La calibrazione dei pesi deve agire sulla Famiglia statistica.

Nota: i controlli vengono aggiornati **ogni giorno**, ma i pesi del Global non devono cambiare automaticamente sotto 30 controlli. Prima si osserva, poi si calibra.

Segnali totali salvati: **93**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-08 | BTC | 64.965,57 | +8 | +4 | +3 | +3 | +3 | 0 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-08 | DOGE | 0.07012 | +3 | +3 | +2 | +3 | -1 | 0 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-08 | SOL | 74,51 | +3 | +4 | +3 | +3 | -2 | 0 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-07 | BTC | 64.173,65 | +6 | +4 | +3 | +3 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-07 | DOGE | 0.06903 | +1 | +2 | +1 | +2 | -1 | -1 | 0 | STAI ALLA FINESTRA |
| 2026-08-07 | SOL | 72,63 | +1 | +4 | +3 | +3 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-06 | BTC | 64.856,39 | +6 | +4 | +3 | +3 | +2 | 0 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-06 | DOGE | 0.06999 | +2 | +2 | +1 | +2 | 0 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-06 | SOL | 74,14 | +2 | +4 | +3 | +2 | -2 | 0 | 0 | HOLD LEGGERO / ATTESA CONFERME |
| 2026-08-05 | BTC | 64.252,74 | +2 | +4 | +3 | +3 | -1 | 0 | 0 | HOLD / ATTESA CONFERME |
| 2026-08-05 | DOGE | 0.06992 | 0 | +2 | +1 | +2 | -2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-05 | SOL | 73,88 | +1 | +4 | +3 | +2 | -2 | -1 | 0 | HOLD LEGGERO / ATTESA CONFERME |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 31 | 30 | 29 | 28 | 26 | 24 | 21 | 17 | 10 | 1 | 0 | 0 |
| SOL | 31 | 30 | 29 | 28 | 26 | 24 | 21 | 17 | 10 | 1 | 0 | 0 |
| DOGE | 31 | 30 | 29 | 28 | 26 | 24 | 21 | 17 | 10 | 1 | 0 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-10 | 30g | 2026-08-09 | domani |
| SOL | 2026-07-10 | 30g | 2026-08-09 | domani |
| DOGE | 2026-07-10 | 30g | 2026-08-09 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 28 | 50,00% | +0,08% | +0,03% | FEEDBACK RAPIDO |
| BTC | 2g | 27 | 44,44% | +0,16% | -0,01% | FEEDBACK RAPIDO |
| BTC | 3g | 26 | 42,31% | +0,09% | -0,18% | FEEDBACK RAPIDO |
| BTC | 5g | 24 | 29,17% | +0,29% | -0,24% | FEEDBACK RAPIDO |
| BTC | 7g | 22 | 40,91% | +0,32% | -0,17% | FEEDBACK RAPIDO |
| BTC | 10g | 19 | 36,84% | +0,54% | +0,06% | FEEDBACK RAPIDO |
| BTC | 14g | 15 | 53,33% | +0,19% | +0,06% | FEEDBACK RAPIDO |
| BTC | 21g | 9 | 33,33% | +0,37% | -0,10% | FEEDBACK RAPIDO |
| BTC | 30g | 1 | 100,00% | +2,74% | +2,74% | FEEDBACK RAPIDO |
| BTC | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 23 | 52,17% | -0,05% | -0,32% | FEEDBACK RAPIDO |
| SOL | 2g | 22 | 40,91% | -0,30% | -0,62% | FEEDBACK RAPIDO |
| SOL | 3g | 21 | 42,86% | -0,26% | -0,69% | FEEDBACK RAPIDO |
| SOL | 5g | 20 | 45,00% | -0,59% | -0,87% | FEEDBACK RAPIDO |
| SOL | 7g | 18 | 50,00% | -0,96% | -0,67% | FEEDBACK RAPIDO |
| SOL | 10g | 15 | 40,00% | -1,87% | -0,45% | FEEDBACK RAPIDO |
| SOL | 14g | 14 | 57,14% | -3,18% | +0,21% | FEEDBACK RAPIDO |
| SOL | 21g | 9 | 66,67% | -3,68% | -0,01% | FEEDBACK RAPIDO |
| SOL | 30g | 1 | 0,00% | -4,50% | -4,50% | FEEDBACK RAPIDO |
| SOL | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 28 | 42,86% | -0,03% | -0,05% | FEEDBACK RAPIDO |
| DOGE | 2g | 27 | 44,44% | -0,20% | -0,20% | FEEDBACK RAPIDO |
| DOGE | 3g | 26 | 42,31% | -0,43% | +0,00% | FEEDBACK RAPIDO |
| DOGE | 5g | 25 | 56,00% | -0,75% | +0,25% | FEEDBACK RAPIDO |
| DOGE | 7g | 23 | 60,87% | -1,16% | +0,76% | FEEDBACK RAPIDO |
| DOGE | 10g | 20 | 55,00% | -1,87% | +1,19% | FEEDBACK RAPIDO |
| DOGE | 14g | 17 | 76,47% | -2,70% | +2,70% | FEEDBACK RAPIDO |
| DOGE | 21g | 10 | 100,00% | -4,14% | +4,14% | FEEDBACK RAPIDO |
| DOGE | 30g | 1 | 100,00% | -3,75% | +3,75% | FEEDBACK RAPIDO |
| DOGE | 45g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 28 | 50,00% | +0,08% | +0,03% | -0,26% | +0,63% | FEEDBACK RAPIDO |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 30 | 53,33% | +0,06% | +0,06% | -0,28% | +0,58% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 30 | 53,33% | +0,06% | +0,06% | -0,28% | +0,58% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 26 | 53,85% | +0,02% | +0,02% | -0,33% | +0,49% | FEEDBACK RAPIDO |
| BTC | 1g | Tecnico | CALIBRABILE | 25 | 36,00% | +0,26% | -0,37% | -0,10% | +0,78% | FEEDBACK RAPIDO |
| BTC | 1g | Classic technical | CALIBRABILE | 4 | 0,00% | +0,76% | -0,76% | +0,03% | +1,12% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +2,00% | +2,00% | +1,48% | +2,25% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 27 | 44,44% | +0,16% | -0,01% | -0,35% | +0,85% | FEEDBACK RAPIDO |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 29 | 48,28% | +0,12% | +0,12% | -0,37% | +0,81% | FEEDBACK RAPIDO |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 29 | 48,28% | +0,12% | +0,12% | -0,37% | +0,81% | FEEDBACK RAPIDO |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 25 | 48,00% | +0,03% | +0,03% | -0,47% | +0,71% | FEEDBACK RAPIDO |
| BTC | 2g | Tecnico | CALIBRABILE | 24 | 45,83% | +0,37% | -0,31% | -0,11% | +1,06% | FEEDBACK RAPIDO |
| BTC | 2g | Classic technical | CALIBRABILE | 4 | 25,00% | +0,86% | -0,86% | +0,50% | +1,73% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +3,18% | +3,18% | +3,05% | +3,89% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 26 | 42,31% | +0,09% | -0,18% | -1,36% | +1,79% | FEEDBACK RAPIDO |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 28 | 57,14% | +0,17% | +0,17% | -1,32% | +1,76% | FEEDBACK RAPIDO |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 28 | 57,14% | +0,17% | +0,17% | -1,32% | +1,76% | FEEDBACK RAPIDO |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 24 | 58,33% | +0,17% | +0,17% | -1,35% | +1,67% | FEEDBACK RAPIDO |
| BTC | 3g | Tecnico | CALIBRABILE | 23 | 39,13% | +0,64% | -0,28% | -1,01% | +2,14% | FEEDBACK RAPIDO |
| BTC | 3g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,18% | -1,18% | -0,41% | +2,46% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,88% | +1,88% | +1,44% | +4,24% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 24 | 29,17% | +0,29% | -0,24% | -2,17% | +2,37% | FEEDBACK RAPIDO |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 26 | 42,31% | +0,28% | +0,28% | -2,12% | +2,39% | FEEDBACK RAPIDO |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 26 | 42,31% | +0,28% | +0,28% | -2,12% | +2,39% | FEEDBACK RAPIDO |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 22 | 45,45% | +0,43% | +0,43% | -2,11% | +2,39% | FEEDBACK RAPIDO |
| BTC | 5g | Tecnico | CALIBRABILE | 21 | 47,62% | +0,61% | -0,45% | -1,80% | +2,78% | FEEDBACK RAPIDO |
| BTC | 5g | Classic technical | CALIBRABILE | 4 | 25,00% | +1,14% | -1,14% | -1,16% | +2,94% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,16% | -0,16% | -0,37% | +4,24% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 22 | 40,91% | +0,32% | -0,17% | -2,49% | +2,70% | FEEDBACK RAPIDO |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 24 | 54,17% | +0,25% | +0,25% | -2,46% | +2,69% | FEEDBACK RAPIDO |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 24 | 54,17% | +0,25% | +0,25% | -2,46% | +2,69% | FEEDBACK RAPIDO |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 20 | 60,00% | +0,56% | +0,56% | -2,44% | +2,75% | FEEDBACK RAPIDO |
| BTC | 7g | Tecnico | CALIBRABILE | 19 | 36,84% | +0,90% | -0,45% | -2,10% | +3,11% | FEEDBACK RAPIDO |
| BTC | 7g | Classic technical | CALIBRABILE | 3 | 0,00% | +1,41% | -1,41% | -1,92% | +2,79% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 19 | 36,84% | +0,54% | +0,06% | -2,77% | +3,14% | FEEDBACK RAPIDO |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 21 | 47,62% | +0,27% | +0,27% | -2,79% | +3,10% | FEEDBACK RAPIDO |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 21 | 47,62% | +0,27% | +0,27% | -2,79% | +3,10% | FEEDBACK RAPIDO |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 17 | 58,82% | +0,81% | +0,81% | -2,64% | +3,26% | FEEDBACK RAPIDO |
| BTC | 10g | Tecnico | CALIBRABILE | 17 | 41,18% | +0,72% | -0,05% | -2,41% | +3,56% | FEEDBACK RAPIDO |
| BTC | 10g | Classic technical | CALIBRABILE | 2 | 0,00% | +1,45% | -1,45% | -2,23% | +2,64% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 15 | 53,33% | +0,19% | +0,06% | -3,05% | +3,96% | FEEDBACK RAPIDO |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 17 | 47,06% | -0,01% | -0,01% | -3,08% | +3,80% | FEEDBACK RAPIDO |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 17 | 47,06% | -0,01% | -0,01% | -3,08% | +3,80% | FEEDBACK RAPIDO |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 13 | 61,54% | +0,74% | +0,74% | -2,67% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Tecnico | CALIBRABILE | 14 | 50,00% | +0,22% | +0,07% | -2,72% | +4,14% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 9 | 33,33% | +0,37% | -0,10% | -2,48% | +5,20% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 10 | 60,00% | +0,50% | +0,50% | -2,49% | +5,16% | FEEDBACK RAPIDO |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 10 | 60,00% | +0,50% | +0,50% | -2,49% | +5,16% | FEEDBACK RAPIDO |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 10 | 60,00% | +0,50% | +0,50% | -2,49% | +5,16% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 9 | 11,11% | +0,47% | -0,72% | -2,41% | +5,20% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 1 | 100,00% | +2,74% | +2,74% | -2,32% | +5,81% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 1 | 100,00% | +2,74% | +2,74% | -2,32% | +5,81% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 1 | 100,00% | +2,74% | +2,74% | -2,32% | +5,81% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 1 | 100,00% | +2,74% | +2,74% | -2,32% | +5,81% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 1 | 0,00% | +2,74% | -2,74% | -2,32% | +5,81% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 28 | 42,86% | -0,03% | -0,05% | -0,50% | +0,62% | FEEDBACK RAPIDO |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 30 | 56,67% | -0,16% | +0,24% | -0,64% | +0,47% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 30 | 56,67% | -0,16% | +0,24% | -0,64% | +0,47% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 28 | 57,14% | -0,04% | +0,12% | -0,53% | +0,61% | FEEDBACK RAPIDO |
| DOGE | 1g | Tecnico | CALIBRABILE | 29 | 48,28% | -0,12% | +0,12% | -0,61% | +0,51% | FEEDBACK RAPIDO |
| DOGE | 1g | Classic technical | CALIBRABILE | 21 | 38,10% | +0,20% | -0,20% | -0,32% | +0,77% | FEEDBACK RAPIDO |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +2,65% | +1,60% | +1,48% | +2,77% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 27 | 44,44% | -0,20% | -0,20% | -0,83% | +0,75% | FEEDBACK RAPIDO |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 29 | 48,28% | -0,33% | -0,01% | -0,96% | +0,58% | FEEDBACK RAPIDO |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 29 | 48,28% | -0,33% | -0,01% | -0,96% | +0,58% | FEEDBACK RAPIDO |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 27 | 48,15% | -0,45% | +0,08% | -1,02% | +0,53% | FEEDBACK RAPIDO |
| DOGE | 2g | Tecnico | CALIBRABILE | 28 | 60,71% | -0,35% | +0,35% | -0,97% | +0,59% | FEEDBACK RAPIDO |
| DOGE | 2g | Classic technical | CALIBRABILE | 20 | 50,00% | +0,13% | -0,13% | -0,57% | +1,24% | FEEDBACK RAPIDO |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +5,65% | +5,65% | +4,05% | +5,83% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 26 | 42,31% | -0,43% | +0,00% | -2,02% | +1,82% | FEEDBACK RAPIDO |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 28 | 50,00% | -0,55% | -0,10% | -2,13% | +1,63% | FEEDBACK RAPIDO |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 28 | 50,00% | -0,55% | -0,10% | -2,13% | +1,63% | FEEDBACK RAPIDO |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 26 | 53,85% | -0,87% | +0,17% | -2,09% | +1,46% | FEEDBACK RAPIDO |
| DOGE | 3g | Tecnico | CALIBRABILE | 28 | 50,00% | -0,55% | +0,55% | -2,13% | +1,63% | FEEDBACK RAPIDO |
| DOGE | 3g | Classic technical | CALIBRABILE | 20 | 40,00% | -0,14% | +0,14% | -1,99% | +2,22% | FEEDBACK RAPIDO |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +3,13% | +3,13% | +0,09% | +6,33% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 25 | 56,00% | -0,75% | +0,25% | -2,99% | +2,16% | FEEDBACK RAPIDO |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 26 | 53,85% | -0,87% | +0,12% | -3,08% | +1,99% | FEEDBACK RAPIDO |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 26 | 53,85% | -0,87% | +0,12% | -3,08% | +1,99% | FEEDBACK RAPIDO |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 24 | 54,17% | -0,90% | +0,09% | -3,12% | +1,78% | FEEDBACK RAPIDO |
| DOGE | 5g | Tecnico | CALIBRABILE | 26 | 61,54% | -0,87% | +0,87% | -3,08% | +1,99% | FEEDBACK RAPIDO |
| DOGE | 5g | Classic technical | CALIBRABILE | 20 | 55,00% | -0,45% | +0,45% | -2,87% | +2,58% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,26% | +1,26% | +0,02% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 23 | 60,87% | -1,16% | +0,76% | -3,59% | +2,38% | FEEDBACK RAPIDO |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 24 | 62,50% | -1,28% | +0,50% | -3,72% | +2,19% | FEEDBACK RAPIDO |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 24 | 62,50% | -1,28% | +0,50% | -3,72% | +2,19% | FEEDBACK RAPIDO |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 22 | 63,64% | -1,30% | +0,45% | -3,81% | +1,97% | FEEDBACK RAPIDO |
| DOGE | 7g | Tecnico | CALIBRABILE | 24 | 62,50% | -1,28% | +1,28% | -3,72% | +2,19% | FEEDBACK RAPIDO |
| DOGE | 7g | Classic technical | CALIBRABILE | 20 | 55,00% | -1,01% | +1,01% | -3,42% | +2,68% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,19% | +1,19% | -0,23% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 20 | 55,00% | -1,87% | +1,19% | -4,52% | +2,48% | FEEDBACK RAPIDO |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 21 | 57,14% | -1,97% | +1,04% | -4,62% | +2,25% | FEEDBACK RAPIDO |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 21 | 57,14% | -1,97% | +1,04% | -4,62% | +2,25% | FEEDBACK RAPIDO |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 19 | 57,89% | -2,09% | +1,06% | -4,74% | +2,01% | FEEDBACK RAPIDO |
| DOGE | 10g | Tecnico | CALIBRABILE | 21 | 71,43% | -1,97% | +1,97% | -4,62% | +2,25% | FEEDBACK RAPIDO |
| DOGE | 10g | Classic technical | CALIBRABILE | 17 | 64,71% | -1,53% | +1,53% | -4,24% | +2,85% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +1,09% | +1,09% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 17 | 76,47% | -2,70% | +2,70% | -5,47% | +2,78% | FEEDBACK RAPIDO |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 17 | 82,35% | -2,70% | +2,81% | -5,47% | +2,78% | FEEDBACK RAPIDO |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 17 | 82,35% | -2,70% | +2,81% | -5,47% | +2,78% | FEEDBACK RAPIDO |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 15 | 86,67% | -2,85% | +2,97% | -5,70% | +2,55% | FEEDBACK RAPIDO |
| DOGE | 14g | Tecnico | CALIBRABILE | 17 | 76,47% | -2,70% | +2,70% | -5,47% | +2,78% | FEEDBACK RAPIDO |
| DOGE | 14g | Classic technical | CALIBRABILE | 16 | 75,00% | -2,59% | +2,59% | -5,33% | +2,92% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +0,46% | +0,46% | -1,85% | +6,57% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 10 | 100,00% | -4,14% | +4,14% | -6,62% | +2,51% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 10 | 100,00% | -4,14% | +4,14% | -6,62% | +2,51% | FEEDBACK RAPIDO |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 10 | 100,00% | -4,14% | +4,14% | -6,62% | +2,51% | FEEDBACK RAPIDO |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 10 | 100,00% | -4,14% | +4,14% | -6,62% | +2,51% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 10 | 100,00% | -4,14% | +4,14% | -6,62% | +2,51% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 9 | 100,00% | -4,00% | +4,00% | -6,45% | +2,73% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 1 | 100,00% | -3,75% | +3,75% | -6,69% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 1 | 100,00% | -3,75% | +3,75% | -6,69% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 1 | 100,00% | -3,75% | +3,75% | -6,69% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 1 | 100,00% | -3,75% | +3,75% | -6,69% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 1 | 100,00% | -3,75% | +3,75% | -6,69% | +3,59% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 1 | 100,00% | -3,75% | +3,75% | -6,69% | +3,59% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 23 | 52,17% | -0,05% | -0,32% | -0,59% | +0,65% | FEEDBACK RAPIDO |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 26 | 61,54% | -0,39% | -0,06% | -0,87% | +0,26% | FEEDBACK RAPIDO |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 29 | 58,62% | -0,23% | -0,16% | -0,75% | +0,42% | FEEDBACK RAPIDO |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 24 | 54,17% | -0,19% | -0,02% | -0,82% | +0,43% | FEEDBACK RAPIDO |
| SOL | 1g | Tecnico | CALIBRABILE | 30 | 50,00% | -0,13% | +0,01% | -0,65% | +0,51% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 21 | 47,62% | +0,04% | -0,04% | -0,54% | +0,59% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,51% | -0,51% | -0,47% | +0,31% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 22 | 40,91% | -0,30% | -0,62% | -0,96% | +0,65% | FEEDBACK RAPIDO |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 25 | 48,00% | -0,57% | -0,38% | -1,30% | +0,19% | FEEDBACK RAPIDO |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 28 | 46,43% | -0,47% | -0,38% | -1,16% | +0,47% | FEEDBACK RAPIDO |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 23 | 43,48% | -0,51% | -0,46% | -1,23% | +0,45% | FEEDBACK RAPIDO |
| SOL | 2g | Tecnico | CALIBRABILE | 29 | 41,38% | -0,37% | -0,02% | -1,04% | +0,56% | FEEDBACK RAPIDO |
| SOL | 2g | Classic technical | CALIBRABILE | 20 | 50,00% | -0,20% | +0,20% | -0,76% | +0,30% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -1,38% | -1,38% | -1,57% | +0,62% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 21 | 42,86% | -0,26% | -0,69% | -2,18% | +1,80% | FEEDBACK RAPIDO |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 24 | 41,67% | -0,75% | -0,43% | -2,55% | +1,41% | FEEDBACK RAPIDO |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 27 | 40,74% | -0,63% | -0,41% | -2,40% | +1,63% | FEEDBACK RAPIDO |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 22 | 40,91% | -0,64% | -0,73% | -2,38% | +1,62% | FEEDBACK RAPIDO |
| SOL | 3g | Tecnico | CALIBRABILE | 28 | 46,43% | -0,55% | +0,13% | -2,27% | +1,70% | FEEDBACK RAPIDO |
| SOL | 3g | Classic technical | CALIBRABILE | 20 | 45,00% | -0,13% | +0,13% | -2,07% | +1,62% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,20% | -3,20% | -3,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 20 | 45,00% | -0,59% | -0,87% | -3,08% | +2,35% | FEEDBACK RAPIDO |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 22 | 45,45% | -1,01% | -0,68% | -3,46% | +1,94% | FEEDBACK RAPIDO |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 25 | 44,00% | -0,80% | -0,69% | -3,28% | +2,18% | FEEDBACK RAPIDO |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 20 | 40,00% | -1,21% | -0,84% | -3,34% | +2,06% | FEEDBACK RAPIDO |
| SOL | 5g | Tecnico | CALIBRABILE | 26 | 53,85% | -0,86% | +0,23% | -3,27% | +2,23% | FEEDBACK RAPIDO |
| SOL | 5g | Classic technical | CALIBRABILE | 18 | 61,11% | -0,43% | +0,43% | -2,88% | +2,29% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,99% | -3,99% | -6,07% | +0,62% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 18 | 50,00% | -0,96% | -0,67% | -3,89% | +2,59% | FEEDBACK RAPIDO |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 20 | 55,00% | -1,53% | -0,38% | -4,27% | +2,14% | FEEDBACK RAPIDO |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 23 | 56,52% | -1,34% | -0,32% | -4,07% | +2,37% | FEEDBACK RAPIDO |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 18 | 44,44% | -1,28% | -1,17% | -4,17% | +2,24% | FEEDBACK RAPIDO |
| SOL | 7g | Tecnico | CALIBRABILE | 24 | 45,83% | -1,27% | +0,42% | -4,04% | +2,42% | FEEDBACK RAPIDO |
| SOL | 7g | Classic technical | CALIBRABILE | 16 | 56,25% | -1,13% | +1,13% | -3,80% | +2,49% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -6,33% | -6,33% | -6,71% | +0,62% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 15 | 40,00% | -1,87% | -0,45% | -4,59% | +2,76% | FEEDBACK RAPIDO |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 17 | 35,29% | -1,99% | -0,71% | -5,16% | +2,21% | FEEDBACK RAPIDO |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 20 | 35,00% | -1,72% | -0,58% | -4,90% | +2,47% | FEEDBACK RAPIDO |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 15 | 20,00% | -1,56% | -1,92% | -5,05% | +2,34% | FEEDBACK RAPIDO |
| SOL | 10g | Tecnico | CALIBRABILE | 21 | 71,43% | -1,80% | +1,57% | -4,90% | +2,52% | FEEDBACK RAPIDO |
| SOL | 10g | Classic technical | CALIBRABILE | 13 | 84,62% | -2,13% | +2,13% | -4,84% | +2,64% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,36% | -5,36% | -7,47% | +0,62% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 14 | 57,14% | -3,18% | +0,21% | -5,68% | +2,77% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 13 | 61,54% | -2,87% | +0,01% | -5,98% | +2,43% | FEEDBACK RAPIDO |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 16 | 68,75% | -2,91% | +0,59% | -5,59% | +2,71% | FEEDBACK RAPIDO |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 11 | 18,18% | -2,80% | -2,47% | -5,53% | +2,64% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 17 | 64,71% | -2,98% | +1,79% | -5,67% | +2,76% | FEEDBACK RAPIDO |
| SOL | 14g | Classic technical | CALIBRABILE | 9 | 88,89% | -3,03% | +3,03% | -5,90% | +3,13% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -5,80% | -5,80% | -9,62% | +0,62% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 9 | 66,67% | -3,68% | -0,01% | -6,74% | +3,33% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 7 | 85,71% | -4,23% | +2,87% | -7,04% | +2,83% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 10 | 90,00% | -3,78% | +2,83% | -6,75% | +3,15% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 7 | 28,57% | -3,91% | -1,48% | -6,83% | +3,09% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 10 | 60,00% | -3,78% | -0,34% | -6,75% | +3,15% | FEEDBACK RAPIDO |
| SOL | 21g | Classic technical | CALIBRABILE | 3 | 100,00% | -2,10% | +2,10% | -6,17% | +4,49% | FEEDBACK RAPIDO |
| SOL | 21g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -5,86% | -5,86% | -7,23% | +1,96% | FEEDBACK RAPIDO |
| SOL | 30g | Global confluence | BENCHMARK | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | FEEDBACK RAPIDO |
| SOL | 30g | Famiglia statistica | CALIBRABILE | 1 | 100,00% | -4,50% | +4,50% | -9,39% | +1,96% | FEEDBACK RAPIDO |
| SOL | 30g | Scanner grezzo | DIAGNOSTICO | 1 | 100,00% | -4,50% | +4,50% | -9,39% | +1,96% | FEEDBACK RAPIDO |
| SOL | 30g | Market regime grezzo | DIAGNOSTICO | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | FEEDBACK RAPIDO |
| SOL | 30g | Tecnico | CALIBRABILE | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | FEEDBACK RAPIDO |
| SOL | 30g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -4,50% | -4,50% | -9,39% | +1,96% | FEEDBACK RAPIDO |

## Come leggerlo

- **CALIBRABILE** = modulo reale sul quale, con dati maturi, si può valutare una modifica di peso.
- **DIAGNOSTICO** = resta misurato, ma è già incluso in una famiglia e il suo peso separato deve restare 0.
- **BENCHMARK** = risultato complessivo del Global; serve per confrontare l'aggregato, non è un peso interno.
- **Controlli** = segnali non neutrali già verificati su quell'orizzonte.
- **Accuratezza direzione** = quante volte un segnale positivo ha avuto return positivo o un segnale negativo ha avuto return negativo.
- **Return medio** = rendimento reale medio dell'asset su quell'orizzonte.
- **Return corretto direzione** = return visto dal lato del modulo: se il modulo era ribassista, un calo conta positivo.
- **Drawdown medio** = peggior discesa media durante l'orizzonte.
- **Max gain medio** = massimo rialzo medio durante l'orizzonte.

Regole operative:

- Sotto **30 controlli**: solo osservazione, nessuna modifica ai pesi.
- Da **30 controlli**: possibile calibrazione leggera.
- Da **60 controlli**: lettura più utile.
- Da **100+ controlli**: possibile revisione più seria dei pesi.

Questo report non cambia ancora automaticamente i pesi del Global Confluence. Produce però i metadati `calibratable` e `calibration_role`, così il report di calibrazione può escludere Scanner e Market dalle proposte di peso separate.

Nota tecnica: le colonne data sono forzate come testo, quindi non deve più apparire l'errore `Invalid value 'YYYY-MM-DD' for dtype 'float64'`.
