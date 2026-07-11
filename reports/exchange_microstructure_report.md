# Dati exchange, liquidità e leva

Generato: 2026-07-11 03:03 UTC

Questo modulo legge Binance Futures, Bybit e KuCoin Futures per aggiungere microstruttura, leva e flussi reali allo scanner.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** gli exchange non pubblicano la mappa completa dei prezzi di liquidazione di tutti gli utenti. Le liquidazioni qui sotto sono eventi realmente osservati in un campione pubblico di circa 15 secondi; le zone future di liquidazione restano stime di pressione, non dati certi delle singole posizioni.

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding | OI 24h | Taker B/S 4h | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 64.152 $ | 1 | 0 | 0 | LEGGERMENTE NEGATIVA / NON PESATA | BASSA | 29% | -0,0010% | +1,72% | 0,06 | +2,84% | 0 $ | 0 $ |
| SOL | 77,77 $ | 1 | 0 | 0 | LEGGERMENTE NEGATIVA / NON PESATA | BASSA | 29% | +0,0073% | +17,81% | 0,41 | -9,72% | 0 $ | 0 $ |
| DOGE | 0.07422 $ | 1 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 29% | +0,0024% | -7,68% | 1,14 | +4,98% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding | Open interest | Taker B/S | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Binance | MANCANTE | n/a | n/a | n/a | +0,00% |
| BTC | Bybit | MANCANTE | n/a | n/a | n/a | +0,00% |
| BTC | Kucoin | OK | -0,0010% | 1,86 mld $ | 0,06 | +2,84% |
| SOL | Binance | MANCANTE | n/a | n/a | n/a | +0,00% |
| SOL | Bybit | MANCANTE | n/a | n/a | n/a | +0,00% |
| SOL | Kucoin | OK | +0,0073% | 341,84 mln $ | 0,41 | -9,72% |
| DOGE | Binance | MANCANTE | n/a | n/a | n/a | +0,00% |
| DOGE | Bybit | MANCANTE | n/a | n/a | n/a | +0,00% |
| DOGE | Kucoin | OK | +0,0024% | 97,18 mln $ | 1,14 | +4,98% |

KuCoin contribuisce a funding, open interest, trade aggressivi e order book. Non viene inventato un long/short ratio pubblico né un feed pubblico completo delle liquidazioni quando l'API non li espone.

## Conferme per indicatori tecnici

### BTC

- Score grezzo exchange: **-1,50**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 0, accuratezza n/a.
- Fonti disponibili: Binance **NO**, Bybit **NO**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 0, divergenze 0.
- Flusso taker/order book: **-1,00**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni nel campione: **0 eventi**, long 0 $, short 0 $.
- **Wyckoff:** Possibile accumulazione non confermata: il flusso aggressivo resta venditore.
- **Fibonacci:** Fibonacci tenuto; nessuna conferma exchange netta.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Resistenza vicina ma long affollati/flusso debole: rischio di falso breakout o squeeze breve.
- **Mappa liquidità attuale:** muro bid kucoin @ 63.366 (-1,22%, 3,16 mln $, 1649.1x mediana); muro ask kucoin @ 64.925 (+1,20%, 3,24 mln $, 1739.3x mediana)

### SOL

- Score grezzo exchange: **-3,00**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 0, accuratezza n/a.
- Fonti disponibili: Binance **NO**, Bybit **NO**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 0, divergenze 0.
- Flusso taker/order book: **-2,00**.
- OI/funding/basis: **-1,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni nel campione: **0 eventi**, long 0 $, short 0 $.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Livello Fibonacci soltanto testato: order book e taker flow non bastano ancora per dichiararlo tenuto o perso. Confluenza tecnica dichiarata: neckline rialzista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid kucoin @ 76,88 (-1,14%, 1,02 mln $, 573.8x mediana); muro ask kucoin @ 78,61 (+1,08%, 1,98 mln $, 2178.3x mediana)

### DOGE

- Score grezzo exchange: **+1,38**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 0, accuratezza n/a.
- Fonti disponibili: Binance **NO**, Bybit **NO**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 0, divergenze 0.
- Flusso taker/order book: **+1,00**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni nel campione: **0 eventi**, long 0 $, short 0 $.
- **Wyckoff:** Possibile accumulazione/spring sostenuto da pressione compratrice o assorbimento.
- **Fibonacci:** Fibonacci non_attivo; nessuna conferma exchange netta. Confluenza tecnica dichiarata: resistenza tecnica, invalidazione ribassista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid kucoin @ 0.07286 (-1,85%, 1,55 mln $, 584.1x mediana); muro ask kucoin @ 0.07555 (+1,78%, 832,2 mila $, 164.5x mediana)

## Overlay sulle previsioni a 30 giorni

La previsione storica grezza dello scanner resta intatta. L'overlay exchange può correggerla solo dopo almeno 30 controlli maturati a 30 giorni e solo se il modulo dimostra accuratezza direzionale almeno del 55%.

| Asset | Prob. grezza salita | Return p50 grezzo | Controlli 30g | Accuratezza exchange | Stato overlay | Peso | Prob. corretta | Return corretto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | +77,50% | +9,01% | 0 | n/a | RACCOLTA DATI | 0,00 | +77,50% | +9,01% |
| SOL | +40,00% | -1,70% | 0 | n/a | RACCOLTA DATI | 0,00 | +40,00% | -1,70% |
| DOGE | +15,00% | -22,37% | 0 | n/a | RACCOLTA DATI | 0,00 | +15,00% | -22,37% |

## Dati salvati

- `exchange_market_data_snapshot.json`: fotografia raw/derivata Binance + Bybit + KuCoin.
- `exchange_market_data_intraday.csv`: memoria operativa mobile degli ultimi 180 giorni, ripristinata da due copie ridondanti su GitHub Releases.
- `exchange_intraday_YYYY-MM.csv.gz`: archivio mensile permanente dei dati intraday, creato dopo la chiusura del mese.
- `exchange_microstructure_metrics.csv`: score e conferme correnti lette dal Global.
- `exchange_microstructure_history.csv`: prima fotografia giornaliera congelata, usata per valutare le previsioni.
- `exchange_signal_tracker_metrics.csv`: accuratezza a 1/3/7/14/30 giorni.
- `exchange_prediction_overlay.csv`: confronto scanner grezzo vs overlay calibrato.

## Regole di prudenza

- Un muro dell'order book può essere cancellato: non è un supporto garantito.
- Funding e long/short ratio misurano affollamento, non direzione certa.
- OI in aumento conta soltanto insieme alla direzione del prezzo e al taker flow.
- Le liquidazioni del campione breve sono diagnostiche e hanno peso ridotto.
- Prima dei 30 controlli a 7g il modulo non pesa nel Global; prima dei 30 controlli a 30g l'overlay non altera le previsioni.

Salute fonti: **WARN** — coppie exchange/asset disponibili: 3/9.
Storage persistente: **OK** — ultimo asset: exchange_state_A.tar.gz.
