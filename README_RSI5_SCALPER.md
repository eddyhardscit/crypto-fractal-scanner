# Installazione — RSI 5m Fixed TP Scalper

Questi file aggiungono una strategia completamente separata dal paper trading già presente nel repository. Non modificano né fermano gli altri conti.

## Strategia installata

Quattro conti paper indipendenti, ognuno con capitale iniziale di **3.800 USDT**:

| Conto | Trigger | Leva |
| --- | ---: | ---: |
| RSI5_RSI20_10X | RSI 14 scende da sopra 20 a 20 o meno | 10× |
| RSI5_RSI20_20X | RSI 14 scende da sopra 20 a 20 o meno | 20× |
| RSI5_RSI25_10X | RSI 14 scende da sopra 25 a 25 o meno | 10× |
| RSI5_RSI25_20X | RSI 14 scende da sopra 25 a 25 o meno | 20× |

Regole comuni:

- timeframe 5 minuti;
- segnale valido solo alla chiusura della candela;
- long soltanto;
- take profit fisso a **+0,50%** dal prezzo di esecuzione simulato;
- stop loss fisso a **−0,25%**;
- una sola posizione aperta per conto;
- tutto il saldo disponibile del conto è usato come margine simulato;
- dopo qualunque chiusura, lo stesso asset deve recuperare RSI 35 prima di poter essere riutilizzato;
- dopo uno stop o una liquidazione simulata, lo stesso asset resta inoltre bloccato per almeno **24 candele, cioè 2 ore**;
- se stop e target vengono toccati nella stessa candela, il backtest sceglie lo stop per prudenza;
- commissioni taker simulate: 0,06% per lato;
- slippage simulato: 0,02% per lato;
- nessuna chiave KuCoin e nessun ordine reale.

Pool iniziale: DOGE, SOL, XRP, ADA, AVAX, LINK, SUI, HYPE, ETH e BTC. Gli asset senza contratto KuCoin USDT o con turnover inferiore a 10 milioni USDT nelle 24 ore vengono ignorati automaticamente.

## File da caricare

Carica nella **radice** del repository:

1. `paper_rsi5_scalper.py`
2. `paper_rsi5_scalper_storage.py`
3. `paper_rsi5_scalper_config.json`
4. `requirements-rsi5-scalper.txt`
5. `README_RSI5_SCALPER.md`

Carica invece questo file nel percorso esatto:

```text
.github/workflows/paper_rsi5_scalper.yml
```

Il file ZIP fornito conserva già questa struttura.

## Telegram

Il workflow usa prima questi secret dedicati, se presenti:

```text
RSI5_TELEGRAM_BOT_TOKEN
RSI5_TELEGRAM_CHAT_ID
```

Se non esistono, usa automaticamente i secret già impiegati dal paper trading principale:

```text
TELEGRAM_BOT_TOKEN
TELEGRAM_CHAT_ID
```

I messaggi hanno intestazioni specifiche `RSI 5M SCALPER`, quindi restano riconoscibili anche usando lo stesso bot e la stessa chat.

## Attivazione

1. Apri **Settings → Actions → General** nel repository.
2. Verifica che i workflow abbiano permesso **Read and write permissions**.
3. Apri **Actions → RSI 5m Paper Scalper**.
4. Premi **Run workflow** una volta.
5. Controlla che il run finisca in verde.
6. Dovresti ricevere su Telegram il messaggio `RSI 5M SCALPER PAPER ATTIVATO`.

Dopo l’avvio, GitHub prova a eseguire il controllo ogni 5 minuti. Le esecuzioni pianificate possono subire qualche minuto di ritardo; il programma recupera tutte le candele chiuse mancanti disponibili nell’ultima finestra KuCoin.

## Persistenza separata

Lo stato viene salvato in una GitHub Release dedicata:

```text
paper-rsi5-scalper-v1
```

Asset persistente:

```text
paper-rsi5-scalper-state.zip
```

Non usa né sovrascrive la Release `paper-trading-v1` del paper trading principale.

## Report prodotti

Il workflow salva nello stato persistente e negli artifact:

```text
reports/paper_rsi5_scalper_state.json
reports/paper_rsi5_scalper_trades.csv
reports/paper_rsi5_scalper_signals.csv
reports/paper_rsi5_scalper_latest.md
reports/paper_rsi5_scalper_latest.json
reports/paper_rsi5_scalper_storage_status.json
```

## Ordine di selezione degli asset

Se più criptovalute generano il segnale nello stesso intervallo, ogni conto sceglie quella con l’RSI più basso. A parità di RSI viene preferito l’asset con maggiore turnover KuCoin. Gli altri segnali vengono comunque registrati nel file `paper_rsi5_scalper_signals.csv`.

## Impatto indicativo di un singolo trade iniziale

Con commissioni e slippage configurati, partendo da 3.800 USDT e usando tutto il conto come margine:

| Leva | Notional iniziale | TP netto indicativo | Stop netto indicativo |
| ---: | ---: | ---: | ---: |
| 10× | 38.000 USDT | circa **+137 USDT**, +3,6% sul conto | circa **−148 USDT**, −3,9% |
| 20× | 76.000 USDT | circa **+273 USDT**, +7,2% sul conto | circa **−296 USDT**, −7,8% |

I valori effettivi cambiano leggermente perché la commissione d’uscita viene calcolata sul notional al prezzo reale di uscita simulato. Un gap può produrre una perdita maggiore dello stop previsto. Per questo la configurazione deve restare esclusivamente paper finché non esiste un campione ampio di operazioni.

## Modifiche rapide

Tutti i parametri principali sono in `paper_rsi5_scalper_config.json`. Per esempio:

```json
"take_profit_pct": 0.005,
"stop_loss_pct": 0.0025,
"cooldown_after_stop_bars": 24,
"rearm_rsi": 35.0
```

Le percentuali sono espresse in forma decimale: `0.005` significa 0,50% e `0.0025` significa 0,25%.
