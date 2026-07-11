# Dati exchange, liquidità e leva

Generato: 2026-07-11 04:13 UTC

Questo modulo legge Binance Futures, Bybit e KuCoin Futures per aggiungere microstruttura, leva e flussi reali allo scanner.
Non modifica la formula matematica di RSI, Fibonacci o Wyckoff: controlla se quei segnali sono sostenuti da acquisti, vendite, OI, funding e liquidità.

**Limite importante:** gli exchange non pubblicano la mappa completa dei prezzi di liquidazione di tutti gli utenti. Le liquidazioni qui sotto sono eventi realmente osservati in un campione pubblico di circa 20 secondi; le zone future di liquidazione restano stime di pressione, non dati certi delle singole posizioni.

Diagnostica completa: [exchange_source_diagnostics.md](exchange_source_diagnostics.md)

## Sintesi

| Asset | Prezzo | Exchange | Segnale candidato | Peso Global | Bias exchange | Confidenza | Copertura | Funding | OI 24h | Taker flow (campione/4h) | Book 0,5% | Liq long campione | Liq short campione |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BTC | 64.090 $ | 1 | 0 | 0 | LEGGERMENTE NEGATIVA / NON PESATA | BASSA | 29% | -0,0036% | +2,04% | 0,06 | +4,28% | 0 $ | 0 $ |
| SOL | 77,63 $ | 1 | 0 | 0 | LEGGERMENTE NEGATIVA / NON PESATA | BASSA | 29% | +0,0058% | +17,79% | 0,76 | +5,04% | 0 $ | 0 $ |
| DOGE | 0.07425 $ | 1 | 0 | 0 | LEGGERMENTE POSITIVA / NON PESATA | BASSA | 29% | +0,0011% | -7,64% | 3,47 | +8,81% | 0 $ | 0 $ |

Il segnale candidato è limitato a **±1**, ma il peso nel Global resta **0** finché il tracker a 7 giorni non raggiunge 30 controlli, almeno 55% di accuratezza e return corretto direzione positivo. Un singolo muro o funding non basta.

La colonna taker usa un campione recente nel primo run. Dopo almeno 3 fotografie nelle ultime 4 ore viene sostituita automaticamente dalla media intraday 4h.

## Dati separati per exchange

| Asset | Exchange | Stato | Funding | Open interest | Taker flow | Book 0,5% |
| --- | --- | --- | --- | --- | --- | --- |
| BTC | Binance | DISABILITATO | n/a | n/a | n/a | +0,00% |
| BTC | Bybit | DISABILITATO | n/a | n/a | n/a | +0,00% |
| BTC | Kucoin | OK | -0,0036% | 1,86 mld $ | 0,06 | +4,28% |
| SOL | Binance | DISABILITATO | n/a | n/a | n/a | +0,00% |
| SOL | Bybit | DISABILITATO | n/a | n/a | n/a | +0,00% |
| SOL | Kucoin | OK | +0,0058% | 342,35 mln $ | 0,76 | +5,04% |
| DOGE | Binance | DISABILITATO | n/a | n/a | n/a | +0,00% |
| DOGE | Bybit | DISABILITATO | n/a | n/a | n/a | +0,00% |
| DOGE | Kucoin | OK | +0,0011% | 96,94 mln $ | 3,47 | +8,81% |

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
- **Mappa liquidità attuale:** muro bid kucoin @ 63.280 (-1,26%, 3,16 mln $, 1702.2x mediana); muro ask kucoin @ 64.882 (+1,23%, 3,24 mln $, 1739.8x mediana)

### SOL

- Score grezzo exchange: **-2,00**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 0, accuratezza n/a.
- Fonti disponibili: Binance **NO**, Bybit **NO**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 0, divergenze 0.
- Flusso taker/order book: **-1,00**.
- OI/funding/basis: **-1,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni nel campione: **0 eventi**, long 0 $, short 0 $.
- **Wyckoff:** Fase Wyckoff non abbastanza chiara per una conferma exchange.
- **Fibonacci:** Livello Fibonacci soltanto testato: order book e taker flow non bastano ancora per dichiararlo tenuto o perso. Confluenza tecnica dichiarata: neckline rialzista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid kucoin @ 76,77 (-1,11%, 1,02 mln $, 819.5x mediana); muro ask kucoin @ 78,51 (+1,13%, 1,05 mln $, 612.0x mediana)

### DOGE

- Score grezzo exchange: **+2,38**; candidato: **0**; peso Global: **0**.
- Attivazione Global: **LOCKED / RACCOLTA 7G** — controlli 7g 0, accuratezza n/a.
- Fonti disponibili: Binance **NO**, Bybit **NO**, KuCoin **SI**.
- Consenso multi-exchange: bull 0, bear 0, divergenze 0.
- Flusso taker/order book: **+2,00**.
- OI/funding/basis: **+0,00**.
- Affollamento long/short: **+0,00**.
- Liquidazioni nel campione: **0 eventi**, long 0 $, short 0 $.
- **Wyckoff:** Possibile accumulazione/spring sostenuto da pressione compratrice o assorbimento.
- **Fibonacci:** Fibonacci non_attivo; nessuna conferma exchange netta. Confluenza tecnica dichiarata: resistenza tecnica, invalidazione ribassista.
- **RSI:** RSI in zona non estrema o flusso exchange non abbastanza netto.
- **Pattern:** I pattern candidati restano non operativi: i dati exchange possono solo preparare la conferma.
- **Breakout/breakdown:** Prezzo non abbastanza vicino a un livello chiave o flusso non netto.
- **Mappa liquidità attuale:** muro bid kucoin @ 0.07288 (-1,85%, 802,5 mila $, 158.7x mediana); muro ask kucoin @ 0.07559 (+1,80%, 832,4 mila $, 163.2x mediana)

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

Salute fonti: **WARN** — coppie exchange/asset disponibili: 3/9. Binance DISABILITATO; Bybit DISABILITATO; KuCoin OK.
Storage persistente: **OK** — ultimo asset: exchange_state_B.tar.gz.
