# Scanner + Telegram Upgrade V2

Questa versione aggiunge:

- dashboard stabile `reports/paper_trading_live.md` pubblicata automaticamente sul branch `paper-trading-live`;
- avvisi Telegram per aperture, chiusure, spostamenti del trailing stop e blocchi di rischio;
- riepilogo paper trading ogni 4 ore;
- invio automatico del nuovo report giornaliero dello scanner una sola volta per aggiornamento;
- allegato Telegram con `reports/latest_report.md`;
- nessun messaggio nei cicli senza eventi, salvo il riepilogo programmato;
- nessuna modifica agli ordini reali: resta tutto in paper trading.

## Secret richiesti nel repository

- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`

Il workflow intraday esistente legge già questi due secret.
