# Accuratezza moduli / autocalibrazione allargata

Generato: 2026-08-28 08:02 UTC

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

Segnali totali salvati: **147**.

Backfill storico Famiglia statistica: **3 righe totali già completate nel diario**; righe completate in questa esecuzione: **0**. Per le righe retroattive è stato usato soltanto lo Scanner grezzo, senza inventare un bonus Market Regime storico.

Politica snapshot giornaliero: **la prima fotografia per data e asset resta congelata**. Un rerun nello stesso giorno non sovrascrive prezzo, punteggi o azione; può soltanto completare campi realmente mancanti.

## Ultimi segnali salvati

| Data | Asset | Prezzo | Global | Famiglia stat. | Scanner grezzo | Market grezzo | Tecnico | Classic | Frattale | Azione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-28 | BTC | 79.717,91 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-28 | DOGE | 0.08759 | 0 | -1 | -1 | 0 | +1 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-28 | SOL | 106,61 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-08-27 | BTC | 78.624,75 | +7 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-27 | DOGE | 0.08623 | -1 | -1 | -1 | 0 | +1 | 0 | 0 | EVITA LONG / SOLO RIMBALZI VELOCI |
| 2026-08-27 | SOL | 100,81 | +7 | +2 | +2 | 0 | +3 | +1 | 0 | HOLD / ACCUMULO A TRANCHE, NO LEVA AGGRESSIVA |
| 2026-08-26 | BTC | 79.104,96 | +8 | +3 | +3 | 0 | +3 | +1 | 0 | ACCUMULA / LONG PRUDENTE SOLO SU CONFERMA |
| 2026-08-26 | DOGE | 0.08675 | +1 | 0 | 0 | 0 | +2 | 0 | 0 | STAI ALLA FINESTRA |
| 2026-08-26 | SOL | 96,96 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |
| 2026-08-25 | BTC | 80.778,18 | +6 | +2 | +2 | 0 | +3 | +1 | 0 | ACCUMULA A TRANCHE SU PULLBACK / NON INSEGUIRE |
| 2026-08-25 | DOGE | 0.09299 | +5 | +1 | +1 | 0 | +3 | +1 | 0 | SOLO TRANCHE PICCOLE / NO LEVA |
| 2026-08-25 | SOL | 102,40 | +6 | +1 | +1 | 0 | +3 | +1 | 0 | HOLD / TRANCHE PICCOLE, NO LEVA |

## Stato controlli per orizzonte

| Asset | Segnali salvati | 1g | 2g | 3g | 5g | 7g | 10g | 14g | 21g | 30g | 45g | 60g |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 49 | 48 | 47 | 46 | 44 | 42 | 39 | 35 | 30 | 21 | 6 | 0 |
| SOL | 49 | 48 | 47 | 46 | 44 | 42 | 39 | 35 | 30 | 21 | 6 | 0 |
| DOGE | 49 | 48 | 47 | 46 | 44 | 42 | 39 | 35 | 30 | 21 | 6 | 0 |

## Prossimi controlli in arrivo

| Asset | Segnale | Orizzonte | Data target | Quando |
| --- | --- | --- | --- | --- |
| BTC | 2026-07-15 | 45g | 2026-08-29 | domani |
| SOL | 2026-07-15 | 45g | 2026-08-29 | domani |
| DOGE | 2026-07-15 | 45g | 2026-08-29 | domani |

## Lettura rapida Global Confluence

| Asset | Orizzonte | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | 45 | 53,33% | +0,54% | +0,51% | PRIMA CALIBRAZIONE |
| BTC | 2g | 44 | 54,55% | +0,93% | +0,82% | PRIMA CALIBRAZIONE |
| BTC | 3g | 43 | 51,16% | +1,20% | +1,03% | PRIMA CALIBRAZIONE |
| BTC | 5g | 41 | 43,90% | +2,40% | +2,09% | PRIMA CALIBRAZIONE |
| BTC | 7g | 39 | 51,28% | +3,23% | +2,95% | PRIMA CALIBRAZIONE |
| BTC | 10g | 36 | 50,00% | +3,62% | +3,37% | PRIMA CALIBRAZIONE |
| BTC | 14g | 33 | 57,58% | +4,04% | +3,93% | PRIMA CALIBRAZIONE |
| BTC | 21g | 28 | 50,00% | +6,28% | +6,04% | FEEDBACK RAPIDO |
| BTC | 30g | 19 | 84,21% | +8,15% | +5,88% | FEEDBACK RAPIDO |
| BTC | 45g | 6 | 100,00% | +23,99% | +23,99% | FEEDBACK RAPIDO |
| BTC | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| SOL | 1g | 41 | 58,54% | +0,89% | +0,74% | PRIMA CALIBRAZIONE |
| SOL | 2g | 40 | 55,00% | +1,67% | +1,50% | PRIMA CALIBRAZIONE |
| SOL | 3g | 39 | 58,97% | +2,49% | +2,26% | PRIMA CALIBRAZIONE |
| SOL | 5g | 37 | 62,16% | +4,08% | +3,94% | PRIMA CALIBRAZIONE |
| SOL | 7g | 35 | 65,71% | +5,39% | +5,54% | PRIMA CALIBRAZIONE |
| SOL | 10g | 32 | 65,62% | +6,02% | +6,26% | PRIMA CALIBRAZIONE |
| SOL | 14g | 28 | 71,43% | +5,80% | +7,10% | FEEDBACK RAPIDO |
| SOL | 21g | 23 | 65,22% | +8,57% | +7,02% | FEEDBACK RAPIDO |
| SOL | 30g | 15 | 46,67% | +4,92% | +2,85% | FEEDBACK RAPIDO |
| SOL | 45g | 5 | 40,00% | +30,39% | -10,04% | FEEDBACK RAPIDO |
| SOL | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |
| DOGE | 1g | 46 | 47,83% | +0,50% | +0,42% | PRIMA CALIBRAZIONE |
| DOGE | 2g | 45 | 51,11% | +0,98% | +0,97% | PRIMA CALIBRAZIONE |
| DOGE | 3g | 44 | 47,73% | +1,43% | +1,68% | PRIMA CALIBRAZIONE |
| DOGE | 5g | 42 | 57,14% | +2,82% | +3,42% | PRIMA CALIBRAZIONE |
| DOGE | 7g | 40 | 67,50% | +4,02% | +5,12% | PRIMA CALIBRAZIONE |
| DOGE | 10g | 37 | 62,16% | +3,36% | +5,04% | PRIMA CALIBRAZIONE |
| DOGE | 14g | 33 | 66,67% | +3,68% | +6,50% | PRIMA CALIBRAZIONE |
| DOGE | 21g | 28 | 71,43% | +4,71% | +3,30% | FEEDBACK RAPIDO |
| DOGE | 30g | 20 | 75,00% | +6,44% | +0,95% | FEEDBACK RAPIDO |
| DOGE | 45g | 6 | 0,00% | +22,35% | -22,35% | FEEDBACK RAPIDO |
| DOGE | 60g | 0 | n/a | n/a | n/a | RACCOLTA DATI |

## Accuratezza direzionale per modulo

| Asset | Orizzonte | Modulo | Ruolo | Controlli | Accuratezza direzione | Return medio | Return corretto direzione | Drawdown medio | Max gain medio | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 1g | Global confluence | BENCHMARK | 45 | 53,33% | +0,54% | +0,51% | +0,09% | +1,14% | PRIMA CALIBRAZIONE |
| BTC | 1g | Famiglia statistica | CALIBRABILE | 48 | 56,25% | +0,50% | +0,50% | +0,07% | +1,09% | PRIMA CALIBRAZIONE |
| BTC | 1g | Scanner grezzo | DIAGNOSTICO | 48 | 56,25% | +0,50% | +0,50% | +0,07% | +1,09% | PRIMA CALIBRAZIONE |
| BTC | 1g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,25% | +0,25% | -0,10% | +0,70% | PRIMA CALIBRAZIONE |
| BTC | 1g | Tecnico | CALIBRABILE | 43 | 39,53% | +0,67% | +0,19% | +0,21% | +1,26% | PRIMA CALIBRAZIONE |
| BTC | 1g | Classic technical | CALIBRABILE | 16 | 37,50% | +1,21% | +0,55% | +0,46% | +1,86% | FEEDBACK RAPIDO |
| BTC | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +0,27% | +0,27% | -0,26% | +0,74% | FEEDBACK RAPIDO |
| BTC | 2g | Global confluence | BENCHMARK | 44 | 54,55% | +0,93% | +0,82% | +0,34% | +1,67% | PRIMA CALIBRAZIONE |
| BTC | 2g | Famiglia statistica | CALIBRABILE | 47 | 57,45% | +1,03% | +1,03% | +0,45% | +1,76% | PRIMA CALIBRAZIONE |
| BTC | 2g | Scanner grezzo | DIAGNOSTICO | 47 | 57,45% | +1,03% | +1,03% | +0,45% | +1,76% | PRIMA CALIBRAZIONE |
| BTC | 2g | Market regime grezzo | DIAGNOSTICO | 35 | 54,29% | +0,52% | +0,52% | -0,02% | +1,18% | PRIMA CALIBRAZIONE |
| BTC | 2g | Tecnico | CALIBRABILE | 42 | 45,24% | +1,28% | +0,29% | +0,69% | +2,01% | PRIMA CALIBRAZIONE |
| BTC | 2g | Classic technical | CALIBRABILE | 15 | 40,00% | +1,78% | +0,76% | +1,19% | +2,61% | FEEDBACK RAPIDO |
| BTC | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +2,14% | +2,14% | +1,22% | +2,65% | FEEDBACK RAPIDO |
| BTC | 3g | Global confluence | BENCHMARK | 43 | 51,16% | +1,20% | +1,03% | -0,82% | +2,89% | PRIMA CALIBRAZIONE |
| BTC | 3g | Famiglia statistica | CALIBRABILE | 46 | 60,87% | +1,54% | +1,54% | -0,81% | +3,15% | PRIMA CALIBRAZIONE |
| BTC | 3g | Scanner grezzo | DIAGNOSTICO | 46 | 60,87% | +1,54% | +1,54% | -0,81% | +3,15% | PRIMA CALIBRAZIONE |
| BTC | 3g | Market regime grezzo | DIAGNOSTICO | 35 | 57,14% | +0,91% | +0,91% | -1,00% | +2,36% | PRIMA CALIBRAZIONE |
| BTC | 3g | Tecnico | CALIBRABILE | 41 | 39,02% | +1,97% | -0,08% | -0,57% | +3,53% | PRIMA CALIBRAZIONE |
| BTC | 3g | Classic technical | CALIBRABILE | 14 | 42,86% | +2,91% | +0,16% | +0,06% | +4,37% | FEEDBACK RAPIDO |
| BTC | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +1,42% | +1,42% | -0,64% | +3,18% | FEEDBACK RAPIDO |
| BTC | 5g | Global confluence | BENCHMARK | 41 | 43,90% | +2,40% | +2,09% | -1,38% | +4,43% | PRIMA CALIBRAZIONE |
| BTC | 5g | Famiglia statistica | CALIBRABILE | 44 | 52,27% | +2,67% | +2,67% | -1,35% | +4,79% | PRIMA CALIBRAZIONE |
| BTC | 5g | Scanner grezzo | DIAGNOSTICO | 44 | 52,27% | +2,67% | +2,67% | -1,35% | +4,79% | PRIMA CALIBRAZIONE |
| BTC | 5g | Market regime grezzo | DIAGNOSTICO | 35 | 48,57% | +2,08% | +2,08% | -1,57% | +4,07% | PRIMA CALIBRAZIONE |
| BTC | 5g | Tecnico | CALIBRABILE | 39 | 41,03% | +3,15% | -1,19% | -1,08% | +5,31% | PRIMA CALIBRAZIONE |
| BTC | 5g | Classic technical | CALIBRABILE | 12 | 41,67% | +7,17% | -2,51% | -0,07% | +8,71% | FEEDBACK RAPIDO |
| BTC | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +2,17% | +2,17% | +0,08% | +5,37% | FEEDBACK RAPIDO |
| BTC | 7g | Global confluence | BENCHMARK | 39 | 51,28% | +3,23% | +2,95% | -1,62% | +5,68% | PRIMA CALIBRAZIONE |
| BTC | 7g | Famiglia statistica | CALIBRABILE | 42 | 59,52% | +3,59% | +3,59% | -1,61% | +6,02% | PRIMA CALIBRAZIONE |
| BTC | 7g | Scanner grezzo | DIAGNOSTICO | 42 | 59,52% | +3,59% | +3,59% | -1,61% | +6,02% | PRIMA CALIBRAZIONE |
| BTC | 7g | Market regime grezzo | DIAGNOSTICO | 35 | 60,00% | +3,17% | +3,17% | -1,80% | +5,49% | PRIMA CALIBRAZIONE |
| BTC | 7g | Tecnico | CALIBRABILE | 37 | 35,14% | +4,38% | -2,51% | -1,31% | +6,69% | PRIMA CALIBRAZIONE |
| BTC | 7g | Classic technical | CALIBRABILE | 10 | 20,00% | +11,13% | -7,29% | +0,03% | +13,42% | FEEDBACK RAPIDO |
| BTC | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,77% | +1,77% | -0,79% | +4,24% | FEEDBACK RAPIDO |
| BTC | 10g | Global confluence | BENCHMARK | 36 | 50,00% | +3,62% | +3,37% | -2,38% | +6,08% | PRIMA CALIBRAZIONE |
| BTC | 10g | Famiglia statistica | CALIBRABILE | 39 | 56,41% | +3,84% | +3,84% | -2,35% | +6,44% | PRIMA CALIBRAZIONE |
| BTC | 10g | Scanner grezzo | DIAGNOSTICO | 39 | 56,41% | +3,84% | +3,84% | -2,35% | +6,44% | PRIMA CALIBRAZIONE |
| BTC | 10g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +3,94% | +3,94% | -2,29% | +6,32% | PRIMA CALIBRAZIONE |
| BTC | 10g | Tecnico | CALIBRABILE | 34 | 29,41% | +4,58% | -3,24% | -2,08% | +7,20% | PRIMA CALIBRAZIONE |
| BTC | 10g | Classic technical | CALIBRABILE | 8 | 0,00% | +13,19% | -13,19% | -0,77% | +15,42% | FEEDBACK RAPIDO |
| BTC | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -0,43% | -0,43% | -2,30% | +4,24% | FEEDBACK RAPIDO |
| BTC | 14g | Global confluence | BENCHMARK | 33 | 57,58% | +4,04% | +3,93% | -2,80% | +7,09% | PRIMA CALIBRAZIONE |
| BTC | 14g | Famiglia statistica | CALIBRABILE | 35 | 57,14% | +3,72% | +3,72% | -2,83% | +6,84% | PRIMA CALIBRAZIONE |
| BTC | 14g | Scanner grezzo | DIAGNOSTICO | 35 | 57,14% | +3,72% | +3,72% | -2,83% | +6,84% | PRIMA CALIBRAZIONE |
| BTC | 14g | Market regime grezzo | DIAGNOSTICO | 31 | 64,52% | +4,52% | +4,52% | -2,62% | +7,41% | PRIMA CALIBRAZIONE |
| BTC | 14g | Tecnico | CALIBRABILE | 30 | 63,33% | +4,55% | +2,70% | -2,56% | +7,70% | PRIMA CALIBRAZIONE |
| BTC | 14g | Classic technical | CALIBRABILE | 5 | 40,00% | +5,63% | -5,63% | -1,27% | +8,59% | FEEDBACK RAPIDO |
| BTC | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -2,25% | -2,25% | -3,05% | +4,24% | FEEDBACK RAPIDO |
| BTC | 21g | Global confluence | BENCHMARK | 28 | 50,00% | +6,28% | +6,04% | -2,90% | +9,77% | FEEDBACK RAPIDO |
| BTC | 21g | Famiglia statistica | CALIBRABILE | 30 | 60,00% | +5,78% | +5,78% | -2,95% | +9,30% | PRIMA CALIBRAZIONE |
| BTC | 21g | Scanner grezzo | DIAGNOSTICO | 30 | 60,00% | +5,78% | +5,78% | -2,95% | +9,30% | PRIMA CALIBRAZIONE |
| BTC | 21g | Market regime grezzo | DIAGNOSTICO | 26 | 65,38% | +6,89% | +6,89% | -2,72% | +10,36% | FEEDBACK RAPIDO |
| BTC | 21g | Tecnico | CALIBRABILE | 25 | 28,00% | +6,63% | -1,13% | -2,65% | +10,19% | FEEDBACK RAPIDO |
| BTC | 21g | Classic technical | CALIBRABILE | 4 | 0,00% | +11,68% | -11,68% | -1,55% | +14,27% | FEEDBACK RAPIDO |
| BTC | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +1,21% | +1,21% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 30g | Global confluence | BENCHMARK | 19 | 84,21% | +8,15% | +5,88% | -3,20% | +11,73% | FEEDBACK RAPIDO |
| BTC | 30g | Famiglia statistica | CALIBRABILE | 21 | 76,19% | +8,14% | +8,14% | -3,24% | +11,87% | FEEDBACK RAPIDO |
| BTC | 30g | Scanner grezzo | DIAGNOSTICO | 21 | 76,19% | +8,14% | +8,14% | -3,24% | +11,87% | FEEDBACK RAPIDO |
| BTC | 30g | Market regime grezzo | DIAGNOSTICO | 17 | 76,47% | +8,94% | +8,94% | -2,95% | +13,00% | FEEDBACK RAPIDO |
| BTC | 30g | Tecnico | CALIBRABILE | 17 | 35,29% | +7,58% | -4,90% | -2,88% | +11,85% | FEEDBACK RAPIDO |
| BTC | 30g | Classic technical | CALIBRABILE | 2 | 0,00% | +24,39% | -24,39% | -2,23% | +27,64% | FEEDBACK RAPIDO |
| BTC | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 100,00% | +0,16% | +0,16% | -3,06% | +4,24% | FEEDBACK RAPIDO |
| BTC | 45g | Global confluence | BENCHMARK | 6 | 100,00% | +23,99% | +23,99% | -2,29% | +26,87% | FEEDBACK RAPIDO |
| BTC | 45g | Famiglia statistica | CALIBRABILE | 6 | 100,00% | +23,99% | +23,99% | -2,29% | +26,87% | FEEDBACK RAPIDO |
| BTC | 45g | Scanner grezzo | DIAGNOSTICO | 6 | 100,00% | +23,99% | +23,99% | -2,29% | +26,87% | FEEDBACK RAPIDO |
| BTC | 45g | Market regime grezzo | DIAGNOSTICO | 6 | 100,00% | +23,99% | +23,99% | -2,29% | +26,87% | FEEDBACK RAPIDO |
| BTC | 45g | Tecnico | CALIBRABILE | 5 | 40,00% | +24,69% | -5,00% | -2,09% | +27,36% | FEEDBACK RAPIDO |
| DOGE | 1g | Global confluence | BENCHMARK | 46 | 47,83% | +0,50% | +0,42% | -0,08% | +1,58% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Famiglia statistica | CALIBRABILE | 47 | 57,45% | +0,42% | +0,61% | -0,18% | +1,46% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Scanner grezzo | DIAGNOSTICO | 47 | 57,45% | +0,42% | +0,61% | -0,18% | +1,46% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,15% | +0,26% | -0,32% | +0,87% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Tecnico | CALIBRABILE | 41 | 56,10% | +0,32% | +0,52% | -0,31% | +1,35% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Classic technical | CALIBRABILE | 31 | 41,94% | +0,27% | -0,51% | -0,38% | +0,97% | PRIMA CALIBRAZIONE |
| DOGE | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 71,43% | +2,86% | +2,41% | +1,15% | +3,54% | FEEDBACK RAPIDO |
| DOGE | 2g | Global confluence | BENCHMARK | 45 | 51,11% | +0,98% | +0,97% | +0,22% | +2,36% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Famiglia statistica | CALIBRABILE | 46 | 52,17% | +0,84% | +1,04% | +0,11% | +2,15% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Scanner grezzo | DIAGNOSTICO | 46 | 52,17% | +0,84% | +1,04% | +0,11% | +2,15% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Market regime grezzo | DIAGNOSTICO | 38 | 50,00% | +0,36% | +0,74% | -0,26% | +1,41% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Tecnico | CALIBRABILE | 40 | 62,50% | +0,35% | +0,81% | -0,35% | +1,66% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Classic technical | CALIBRABILE | 31 | 45,16% | +0,67% | -1,20% | -0,10% | +1,65% | PRIMA CALIBRAZIONE |
| DOGE | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +4,25% | +3,88% | +3,39% | +6,58% | FEEDBACK RAPIDO |
| DOGE | 3g | Global confluence | BENCHMARK | 44 | 47,73% | +1,43% | +1,68% | -1,44% | +4,33% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Famiglia statistica | CALIBRABILE | 46 | 52,17% | +1,28% | +1,55% | -1,53% | +4,11% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Scanner grezzo | DIAGNOSTICO | 46 | 52,17% | +1,28% | +1,55% | -1,53% | +4,11% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +0,84% | +1,55% | -1,48% | +3,36% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Tecnico | CALIBRABILE | 39 | 48,72% | +0,28% | +0,71% | -1,84% | +2,91% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Classic technical | CALIBRABILE | 31 | 32,26% | +1,30% | -2,13% | -1,89% | +4,20% | PRIMA CALIBRAZIONE |
| DOGE | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 7 | 57,14% | +3,59% | +3,29% | -0,23% | +7,51% | FEEDBACK RAPIDO |
| DOGE | 5g | Global confluence | BENCHMARK | 42 | 57,14% | +2,82% | +3,42% | -1,94% | +6,91% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Famiglia statistica | CALIBRABILE | 44 | 54,55% | +2,60% | +3,18% | -2,02% | +6,59% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Scanner grezzo | DIAGNOSTICO | 44 | 54,55% | +2,60% | +3,18% | -2,02% | +6,59% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Market regime grezzo | DIAGNOSTICO | 38 | 55,26% | +2,45% | +3,08% | -2,17% | +5,74% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Tecnico | CALIBRABILE | 37 | 62,16% | +1,44% | +1,09% | -2,43% | +5,30% | PRIMA CALIBRAZIONE |
| DOGE | 5g | Classic technical | CALIBRABILE | 29 | 41,38% | +3,19% | -3,72% | -2,28% | +7,24% | FEEDBACK RAPIDO |
| DOGE | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 6 | 50,00% | +3,80% | +3,53% | +0,14% | +10,26% | FEEDBACK RAPIDO |
| DOGE | 7g | Global confluence | BENCHMARK | 40 | 67,50% | +4,02% | +5,12% | -2,08% | +9,15% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Famiglia statistica | CALIBRABILE | 42 | 64,29% | +3,71% | +4,73% | -2,20% | +8,76% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Scanner grezzo | DIAGNOSTICO | 42 | 64,29% | +3,71% | +4,73% | -2,20% | +8,76% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Market regime grezzo | DIAGNOSTICO | 38 | 63,16% | +3,59% | +4,60% | -2,54% | +8,00% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Tecnico | CALIBRABILE | 35 | 65,71% | +2,27% | +2,31% | -2,67% | +7,03% | PRIMA CALIBRAZIONE |
| DOGE | 7g | Classic technical | CALIBRABILE | 27 | 44,44% | +4,34% | -4,34% | -2,39% | +9,14% | FEEDBACK RAPIDO |
| DOGE | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +3,64% | +3,43% | +1,17% | +11,40% | FEEDBACK RAPIDO |
| DOGE | 10g | Global confluence | BENCHMARK | 37 | 62,16% | +3,36% | +5,04% | -3,11% | +8,88% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Famiglia statistica | CALIBRABILE | 39 | 61,54% | +3,09% | +4,71% | -3,18% | +8,48% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Scanner grezzo | DIAGNOSTICO | 39 | 61,54% | +3,09% | +4,71% | -3,18% | +8,48% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Market regime grezzo | DIAGNOSTICO | 37 | 62,16% | +3,30% | +4,92% | -3,16% | +8,69% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Tecnico | CALIBRABILE | 33 | 66,67% | +1,15% | +2,31% | -3,59% | +6,29% | PRIMA CALIBRAZIONE |
| DOGE | 10g | Classic technical | CALIBRABILE | 26 | 50,00% | +3,10% | -3,10% | -3,17% | +9,15% | FEEDBACK RAPIDO |
| DOGE | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +0,93% | +0,18% | -1,31% | +5,72% | FEEDBACK RAPIDO |
| DOGE | 14g | Global confluence | BENCHMARK | 33 | 66,67% | +3,68% | +6,50% | -3,93% | +9,47% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Famiglia statistica | CALIBRABILE | 35 | 71,43% | +3,35% | +6,03% | -3,96% | +8,99% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Scanner grezzo | DIAGNOSTICO | 35 | 71,43% | +3,35% | +6,03% | -3,96% | +8,99% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Market regime grezzo | DIAGNOSTICO | 33 | 72,73% | +3,65% | +6,30% | -3,97% | +9,26% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Tecnico | CALIBRABILE | 30 | 66,67% | -0,31% | +0,31% | -4,43% | +4,70% | PRIMA CALIBRAZIONE |
| DOGE | 14g | Classic technical | CALIBRABILE | 23 | 60,87% | +1,45% | -1,45% | -4,25% | +6,95% | FEEDBACK RAPIDO |
| DOGE | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 75,00% | +12,47% | +2,65% | -1,31% | +16,91% | FEEDBACK RAPIDO |
| DOGE | 21g | Global confluence | BENCHMARK | 28 | 71,43% | +4,71% | +3,30% | -4,71% | +11,83% | FEEDBACK RAPIDO |
| DOGE | 21g | Famiglia statistica | CALIBRABILE | 30 | 83,33% | +5,07% | +9,02% | -4,70% | +12,47% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Scanner grezzo | DIAGNOSTICO | 30 | 83,33% | +5,07% | +9,02% | -4,70% | +12,47% | PRIMA CALIBRAZIONE |
| DOGE | 21g | Market regime grezzo | DIAGNOSTICO | 28 | 85,71% | +5,52% | +9,57% | -4,77% | +13,04% | FEEDBACK RAPIDO |
| DOGE | 21g | Tecnico | CALIBRABILE | 29 | 65,52% | +4,45% | -4,45% | -4,81% | +11,42% | FEEDBACK RAPIDO |
| DOGE | 21g | Classic technical | CALIBRABILE | 21 | 71,43% | +1,31% | -1,31% | -4,94% | +7,86% | FEEDBACK RAPIDO |
| DOGE | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 66,67% | +9,47% | -8,45% | -1,27% | +19,32% | FEEDBACK RAPIDO |
| DOGE | 30g | Global confluence | BENCHMARK | 20 | 75,00% | +6,44% | +0,95% | -5,84% | +14,30% | FEEDBACK RAPIDO |
| DOGE | 30g | Famiglia statistica | CALIBRABILE | 21 | 80,95% | +7,04% | +4,86% | -5,88% | +15,39% | FEEDBACK RAPIDO |
| DOGE | 30g | Scanner grezzo | DIAGNOSTICO | 21 | 80,95% | +7,04% | +4,86% | -5,88% | +15,39% | FEEDBACK RAPIDO |
| DOGE | 30g | Market regime grezzo | DIAGNOSTICO | 19 | 89,47% | +4,84% | +8,32% | -6,11% | +13,09% | FEEDBACK RAPIDO |
| DOGE | 30g | Tecnico | CALIBRABILE | 21 | 57,14% | +7,04% | -7,04% | -5,88% | +15,39% | FEEDBACK RAPIDO |
| DOGE | 30g | Classic technical | CALIBRABILE | 17 | 64,71% | +4,96% | -4,96% | -5,74% | +12,22% | FEEDBACK RAPIDO |
| DOGE | 30g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 100,00% | +31,53% | +31,53% | -1,85% | +40,20% | FEEDBACK RAPIDO |
| DOGE | 45g | Global confluence | BENCHMARK | 6 | 0,00% | +22,35% | -22,35% | -6,84% | +35,71% | FEEDBACK RAPIDO |
| DOGE | 45g | Famiglia statistica | CALIBRABILE | 6 | 0,00% | +22,35% | -22,35% | -6,84% | +35,71% | FEEDBACK RAPIDO |
| DOGE | 45g | Scanner grezzo | DIAGNOSTICO | 6 | 0,00% | +22,35% | -22,35% | -6,84% | +35,71% | FEEDBACK RAPIDO |
| DOGE | 45g | Market regime grezzo | DIAGNOSTICO | 6 | 0,00% | +22,35% | -22,35% | -6,84% | +35,71% | FEEDBACK RAPIDO |
| DOGE | 45g | Tecnico | CALIBRABILE | 6 | 0,00% | +22,35% | -22,35% | -6,84% | +35,71% | FEEDBACK RAPIDO |
| DOGE | 45g | Classic technical | CALIBRABILE | 6 | 0,00% | +22,35% | -22,35% | -6,84% | +35,71% | FEEDBACK RAPIDO |
| SOL | 1g | Global confluence | BENCHMARK | 41 | 58,54% | +0,89% | +0,74% | +0,24% | +1,90% | PRIMA CALIBRAZIONE |
| SOL | 1g | Famiglia statistica | CALIBRABILE | 43 | 60,47% | +0,51% | +0,49% | -0,06% | +1,48% | PRIMA CALIBRAZIONE |
| SOL | 1g | Scanner grezzo | DIAGNOSTICO | 46 | 58,70% | +0,55% | +0,39% | -0,04% | +1,51% | PRIMA CALIBRAZIONE |
| SOL | 1g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +0,27% | +0,39% | -0,30% | +0,87% | PRIMA CALIBRAZIONE |
| SOL | 1g | Tecnico | CALIBRABILE | 45 | 53,33% | +0,50% | +0,47% | -0,12% | +1,42% | PRIMA CALIBRAZIONE |
| SOL | 1g | Classic technical | CALIBRABILE | 29 | 55,17% | +0,85% | +0,79% | +0,08% | +1,93% | FEEDBACK RAPIDO |
| SOL | 1g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 60,00% | +0,64% | +0,64% | +0,16% | +3,12% | FEEDBACK RAPIDO |
| SOL | 1g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,10% | -0,10% | -0,21% | +0,02% | FEEDBACK RAPIDO |
| SOL | 2g | Global confluence | BENCHMARK | 40 | 55,00% | +1,67% | +1,50% | +0,74% | +2,87% | PRIMA CALIBRAZIONE |
| SOL | 2g | Famiglia statistica | CALIBRABILE | 42 | 50,00% | +1,17% | +0,60% | +0,23% | +2,04% | PRIMA CALIBRAZIONE |
| SOL | 2g | Scanner grezzo | DIAGNOSTICO | 45 | 48,89% | +1,12% | +0,54% | +0,21% | +2,09% | PRIMA CALIBRAZIONE |
| SOL | 2g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +0,76% | +0,78% | -0,00% | +1,60% | PRIMA CALIBRAZIONE |
| SOL | 2g | Tecnico | CALIBRABILE | 44 | 45,45% | +1,04% | +0,34% | +0,18% | +2,23% | PRIMA CALIBRAZIONE |
| SOL | 2g | Classic technical | CALIBRABILE | 28 | 57,14% | +1,31% | +1,27% | +0,42% | +2,40% | FEEDBACK RAPIDO |
| SOL | 2g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 5 | 40,00% | +2,12% | +2,12% | +0,59% | +4,38% | FEEDBACK RAPIDO |
| SOL | 2g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -0,28% | -0,28% | -0,31% | +0,05% | FEEDBACK RAPIDO |
| SOL | 3g | Global confluence | BENCHMARK | 39 | 58,97% | +2,49% | +2,26% | -1,15% | +4,66% | PRIMA CALIBRAZIONE |
| SOL | 3g | Famiglia statistica | CALIBRABILE | 41 | 48,78% | +1,83% | +1,11% | -1,55% | +4,00% | PRIMA CALIBRAZIONE |
| SOL | 3g | Scanner grezzo | DIAGNOSTICO | 44 | 47,73% | +1,73% | +1,02% | -1,52% | +3,96% | PRIMA CALIBRAZIONE |
| SOL | 3g | Market regime grezzo | DIAGNOSTICO | 34 | 50,00% | +1,43% | +1,38% | -1,48% | +3,53% | PRIMA CALIBRAZIONE |
| SOL | 3g | Tecnico | CALIBRABILE | 43 | 48,84% | +1,55% | +0,02% | -1,61% | +3,63% | PRIMA CALIBRAZIONE |
| SOL | 3g | Classic technical | CALIBRABILE | 27 | 55,56% | +1,57% | +1,37% | -1,52% | +3,62% | FEEDBACK RAPIDO |
| SOL | 3g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 4 | 50,00% | +1,27% | +1,27% | -2,62% | +5,77% | FEEDBACK RAPIDO |
| SOL | 3g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,97% | -1,97% | -2,74% | +1,96% | FEEDBACK RAPIDO |
| SOL | 5g | Global confluence | BENCHMARK | 37 | 62,16% | +4,08% | +3,94% | -1,63% | +7,09% | PRIMA CALIBRAZIONE |
| SOL | 5g | Famiglia statistica | CALIBRABILE | 39 | 53,85% | +3,16% | +1,77% | -2,05% | +6,18% | PRIMA CALIBRAZIONE |
| SOL | 5g | Scanner grezzo | DIAGNOSTICO | 42 | 52,38% | +2,99% | +1,59% | -2,05% | +6,02% | PRIMA CALIBRAZIONE |
| SOL | 5g | Market regime grezzo | DIAGNOSTICO | 34 | 55,88% | +2,66% | +2,88% | -2,09% | +5,82% | PRIMA CALIBRAZIONE |
| SOL | 5g | Tecnico | CALIBRABILE | 41 | 46,34% | +2,99% | -0,89% | -2,24% | +5,88% | PRIMA CALIBRAZIONE |
| SOL | 5g | Classic technical | CALIBRABILE | 25 | 60,00% | +2,17% | +1,94% | -2,03% | +4,70% | FEEDBACK RAPIDO |
| SOL | 5g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +1,18% | +1,18% | -1,95% | +5,20% | FEEDBACK RAPIDO |
| SOL | 5g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -3,96% | -3,96% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 7g | Global confluence | BENCHMARK | 35 | 65,71% | +5,39% | +5,54% | -2,03% | +8,81% | PRIMA CALIBRAZIONE |
| SOL | 7g | Famiglia statistica | CALIBRABILE | 37 | 64,86% | +4,30% | +3,90% | -2,48% | +7,81% | PRIMA CALIBRAZIONE |
| SOL | 7g | Scanner grezzo | DIAGNOSTICO | 40 | 65,00% | +3,97% | +3,61% | -2,50% | +7,52% | PRIMA CALIBRAZIONE |
| SOL | 7g | Market regime grezzo | DIAGNOSTICO | 34 | 61,76% | +4,35% | +4,41% | -2,45% | +7,76% | PRIMA CALIBRAZIONE |
| SOL | 7g | Tecnico | CALIBRABILE | 39 | 35,90% | +3,92% | -2,51% | -2,71% | +7,43% | PRIMA CALIBRAZIONE |
| SOL | 7g | Classic technical | CALIBRABILE | 23 | 47,83% | +1,60% | +1,68% | -2,66% | +4,77% | FEEDBACK RAPIDO |
| SOL | 7g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 3 | 33,33% | +3,96% | +3,96% | -2,17% | +8,29% | FEEDBACK RAPIDO |
| SOL | 7g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,59% | -2,59% | -4,95% | +1,96% | FEEDBACK RAPIDO |
| SOL | 10g | Global confluence | BENCHMARK | 32 | 65,62% | +6,02% | +6,26% | -3,00% | +9,59% | PRIMA CALIBRAZIONE |
| SOL | 10g | Famiglia statistica | CALIBRABILE | 35 | 68,57% | +5,41% | +6,03% | -3,34% | +8,82% | PRIMA CALIBRAZIONE |
| SOL | 10g | Scanner grezzo | DIAGNOSTICO | 38 | 65,79% | +4,96% | +5,57% | -3,34% | +8,43% | PRIMA CALIBRAZIONE |
| SOL | 10g | Market regime grezzo | DIAGNOSTICO | 33 | 63,64% | +6,05% | +5,88% | -3,17% | +9,27% | PRIMA CALIBRAZIONE |
| SOL | 10g | Tecnico | CALIBRABILE | 37 | 40,54% | +4,48% | -4,61% | -3,45% | +8,21% | PRIMA CALIBRAZIONE |
| SOL | 10g | Classic technical | CALIBRABILE | 21 | 52,38% | -0,08% | +0,08% | -3,74% | +3,68% | FEEDBACK RAPIDO |
| SOL | 10g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | -2,05% | -2,05% | -4,86% | +1,05% | FEEDBACK RAPIDO |
| SOL | 10g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -2,54% | -2,54% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 14g | Global confluence | BENCHMARK | 28 | 71,43% | +5,80% | +7,10% | -3,87% | +10,55% | FEEDBACK RAPIDO |
| SOL | 14g | Famiglia statistica | CALIBRABILE | 31 | 83,87% | +5,69% | +6,90% | -4,05% | +9,76% | PRIMA CALIBRAZIONE |
| SOL | 14g | Scanner grezzo | DIAGNOSTICO | 34 | 85,29% | +4,92% | +6,56% | -4,04% | +9,25% | PRIMA CALIBRAZIONE |
| SOL | 14g | Market regime grezzo | DIAGNOSTICO | 29 | 68,97% | +6,31% | +6,43% | -3,75% | +10,35% | FEEDBACK RAPIDO |
| SOL | 14g | Tecnico | CALIBRABILE | 33 | 33,33% | +3,19% | -3,81% | -4,24% | +7,75% | PRIMA CALIBRAZIONE |
| SOL | 14g | Classic technical | CALIBRABILE | 21 | 38,10% | +1,19% | -1,19% | -4,25% | +5,07% | FEEDBACK RAPIDO |
| SOL | 14g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 2 | 50,00% | +8,38% | +8,38% | -5,94% | +13,89% | FEEDBACK RAPIDO |
| SOL | 14g | Frattale SOL | CALIBRABILE | 1 | 0,00% | -1,13% | -1,13% | -5,92% | +1,96% | FEEDBACK RAPIDO |
| SOL | 21g | Global confluence | BENCHMARK | 23 | 65,22% | +8,57% | +7,02% | -5,27% | +13,95% | FEEDBACK RAPIDO |
| SOL | 21g | Famiglia statistica | CALIBRABILE | 26 | 80,77% | +9,37% | +11,52% | -5,12% | +13,98% | FEEDBACK RAPIDO |
| SOL | 21g | Scanner grezzo | DIAGNOSTICO | 29 | 82,76% | +8,12% | +10,61% | -5,22% | +12,94% | FEEDBACK RAPIDO |
| SOL | 21g | Market regime grezzo | DIAGNOSTICO | 24 | 62,50% | +10,37% | +11,08% | -4,81% | +15,04% | FEEDBACK RAPIDO |
| SOL | 21g | Tecnico | CALIBRABILE | 30 | 40,00% | +7,87% | -9,24% | -5,28% | +12,62% | PRIMA CALIBRAZIONE |
| SOL | 21g | Classic technical | CALIBRABILE | 21 | 38,10% | +11,18% | -11,18% | -4,64% | +15,32% | FEEDBACK RAPIDO |
| SOL | 21g | Microstruttura exchange | CALIBRABILE / NON PESATO FINO AL GATE | 1 | 0,00% | -3,18% | -3,18% | -9,62% | +0,62% | FEEDBACK RAPIDO |

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
