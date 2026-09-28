# SOL on-chain metrics report

Generato: **2026-09-28 07:32:25 CEST**  
UTC: **2026-09-28 05:32:18 UTC**

Questo report aggiunge una lettura on-chain/fondamentale di Solana.

Non sostituisce il frattale SOL/BTC. Serve a capire se dietro il movimento ci sono segnali di rete sani oppure pressione/speculazione.

## Sintesi

| Voce | Valore |
| --- | --- |
| Score on-chain | 3 |
| Bias | POSITIVA |
| Azione coerente | CONFERMA MODERATA / BUONO SE IL FRATTALE REGGE |
| Metriche importanti mancanti | sol_realized_price_usd, sol_mvrv, sol_holder_profit_pct, sol_exchange_netflow_24h_usd |

## Componenti del punteggio

| Componente | Valore | Punti | Lettura |
| --- | --- | --- | --- |
| TVL 7g | +6,72% | +1 | TVL in crescita: rete più forte. |
| DEX volume 7g | -31,97% | -1 | Volume DEX in calo: attività più debole. |
| Fees 7g | +11,95% | +1 | Fee in crescita: uso della rete in miglioramento. |
| Stablecoin liquidity 7g | +5,16% | +1 | Stablecoin su Solana in aumento: liquidità disponibile migliore. |
| Stake ratio | 69,40% | +1 | Quota staked alta: supply liquida più contenuta. |
| Stake delinquent | 0,01% | 0 | Delinquent stake basso. |

## Metriche disponibili

| Metrica | Valore | Lettura |
| --- | --- | --- |
| Prezzo SOL | 119,07 $ | Prezzo spot usato per il report. |
| Market cap | 69,97 mld $ | Grandezza complessiva di mercato. |
| Volume 24h | 4,32 mld $ | Liquidità di trading spot aggregata. |
| TVL Solana | 6,62 mld $ | Capitale in DeFi su Solana. |
| TVL 7g | +6,72% | Crescita/calo DeFi a 7 giorni. |
| DEX volume 24h | 1,90 mld $ | Attività di scambio on-chain. |
| DEX volume 7g | 17,48 mld $ | Volume settimanale DEX. |
| DEX change 7g | -31,97% | Accelerazione o rallentamento DEX. |
| Fees 24h | 15,50 mln $ | Fee generate dalla chain/protocolli monitorati. |
| Fees 7g | 112,88 mln $ | Fee settimanali. |
| Fees change 7g | +11,95% | Uso rete in crescita/calo. |
| Stablecoin su Solana | 16,66 mld $ | Liquidità stabile disponibile su chain. |
| Stablecoin 7g | +5,16% | Entrata/uscita liquidità stabile. |
| Supply totale | 634.841.039 | Supply totale convertita da lamports a SOL. |
| Supply circolante | 587.782.328 | Supply circolante convertita da lamports a SOL. |
| SOL in stake | 440.549.807 | Stake attivo stimato da vote accounts. |
| Stake / supply totale | 69,40% | Quota supply totale in staking. |
| Stake / supply circolante | 74,95% | Quota supply circolante in staking. |
| Stake delinquent | 0,01% | Quota stake su validatori delinquent. |
| Validatori attivi | 676 | Validatori correnti letti da RPC. |
| Validatori delinquent | 7 | Validatori delinquent letti da RPC. |
| Inflazione stimata | 3,63% | Inflation rate da RPC. |

## Metriche opzionali: realized price / MVRV / holder profit / exchange flow

Queste metriche sono molto utili, ma spesso richiedono provider esterni. Il file le supporta tramite variabili d'ambiente.

| Metrica opzionale | Valore | Come interpretarla |
| --- | --- | --- |
| Realized price SOL | n/a | Costo medio stimato degli holder. Richiede provider esterno. |
| MVRV SOL | n/a | Prezzo rispetto al costo medio. Alto = rischio profit taking. |
| Holder in profit | n/a | Troppi holder in profit possono aumentare prese profitto. |
| Holder in loss | n/a | Molti holder in loss possono indicare fase depressa/accumulo. |
| Exchange netflow 24h | n/a | Positivo = SOL entra su exchange, negativo = SOL esce dagli exchange. |

## Variabili opzionali supportate

| Variabile | Significato |
| --- | --- |
| SOL_REALIZED_PRICE_USD | Realized price stimato di SOL. |
| SOL_MVRV | MVRV di SOL. |
| SOL_HOLDER_PROFIT_PCT | % holder/supply in profit. |
| SOL_HOLDER_LOSS_PCT | % holder/supply in loss. |
| SOL_EXCHANGE_NETFLOW_24H_USD | Netflow exchange 24h in USD. Positivo = entra su exchange; negativo = esce. |
| SOLANA_RPC_URL | RPC Solana custom, se non vuoi usare quello pubblico. |
| SOL_ONCHAIN_DISABLE_RPC=1 | Disattiva letture Solana RPC. |

## Storico ultimi 30 salvataggi

| Data | Prezzo | TVL | TVL 7g | DEX 24h | DEX 7g | Stablecoin | Stake ratio | Score | Bias |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08-26 | 96,79 $ | 5,60 mld $ | +14,37% | 2,95 mld $ | +60,42% | 16,25 mld $ | 68,75% | 4 | POSITIVA |
| 2026-08-27 | 100,99 $ | 5,77 mld $ | +10,39% | 2,48 mld $ | -17,56% | 16,22 mld $ | 69,02% | 1 | NEUTRALE / MISTA |
| 2026-08-28 | 106,36 $ | 5,96 mld $ | +11,73% | 3,63 mld $ | +31,27% | 16,32 mld $ | 69,02% | 4 | POSITIVA |
| 2026-08-29 | 104,05 $ | 5,86 mld $ | +5,61% | 2,62 mld $ | -27,38% | 16,28 mld $ | 68,89% | 2 | POSITIVA |
| 2026-08-30 | 105,04 $ | 5,91 mld $ | +6,27% | 1,81 mld $ | -51,42% | 16,23 mld $ | 69,04% | 1 | NEUTRALE / MISTA |
| 2026-08-31 | 102,60 $ | 5,78 mld $ | +3,84% | 1,87 mld $ | -36,38% | 16,06 mld $ | 69,04% | -1 | NEUTRALE / MISTA |
| 2026-09-01 | 103,95 $ | 5,83 mld $ | +1,69% | 2,46 mld $ | -17,97% | 16,07 mld $ | 69,20% | 0 | NEUTRALE / MISTA |
| 2026-09-02 | 100,25 $ | 5,69 mld $ | +1,54% | 2,25 mld $ | -23,45% | 15,79 mld $ | 69,20% | 0 | NEUTRALE / MISTA |
| 2026-09-03 | 99,91 $ | 5,73 mld $ | -0,81% | 2,33 mld $ | -1,05% | 16,03 mld $ | 69,22% | 0 | NEUTRALE / MISTA |
| 2026-09-04 | 103,69 $ | 5,91 mld $ | -1,70% | 2,37 mld $ | -35,85% | 16,58 mld $ | 68,97% | 0 | NEUTRALE / MISTA |
| 2026-09-05 | 102,31 $ | 5,85 mld $ | -0,31% | 1,85 mld $ | -28,69% | 16,54 mld $ | 68,97% | 0 | NEUTRALE / MISTA |
| 2026-09-06 | 106,09 $ | 5,92 mld $ | +0,23% | 1,96 mld $ | +17,35% | 16,62 mld $ | 69,33% | 3 | POSITIVA |
| 2026-09-07 | 105,58 $ | 5,92 mld $ | +0,23% | 1,96 mld $ | +17,35% | 16,67 mld $ | 69,36% | 3 | POSITIVA |
| 2026-09-08 | 103,30 $ | 5,90 mld $ | -1,43% | 2,87 mld $ | +14,81% | 16,63 mld $ | 69,36% | 4 | POSITIVA |
| 2026-09-09 | 104,39 $ | 5,94 mld $ | +5,28% | 2,58 mld $ | +18,71% | 16,56 mld $ | 69,22% | 5 | POSITIVA FORTE |
| 2026-09-10 | 102,04 $ | 5,86 mld $ | +2,37% | 2,56 mld $ | +11,68% | 16,51 mld $ | 69,22% | 4 | POSITIVA |
| 2026-09-11 | 99,61 $ | 5,78 mld $ | -2,55% | 2,95 mld $ | +19,88% | 16,29 mld $ | 69,29% | 3 | POSITIVA |
| 2026-09-12 | 101,45 $ | 5,89 mld $ | +0,30% | 3,25 mld $ | +72,60% | 16,49 mld $ | 68,91% | 3 | POSITIVA |
| 2026-09-13 | 101,84 $ | 5,91 mld $ | -0,09% | 2,47 mld $ | +32,64% | 16,46 mld $ | 68,91% | 3 | POSITIVA |
| 2026-09-14 | 101,00 $ | 5,86 mld $ | -2,20% | 1,64 mld $ | -43,64% | 16,29 mld $ | 69,20% | -1 | NEUTRALE / MISTA |
| 2026-09-15 | 100,89 $ | 5,89 mld $ | -0,56% | 2,21 mld $ | -20,62% | 16,33 mld $ | 69,27% | -1 | NEUTRALE / MISTA |
| 2026-09-16 | 97,09 $ | 5,73 mld $ | -3,72% | 2,50 mld $ | -10,15% | 15,90 mld $ | 69,27% | -2 | NEGATIVA |
| 2026-09-17 | 99,61 $ | 5,80 mld $ | -0,98% | 2,73 mld $ | -11,14% | 15,70 mld $ | 69,34% | -2 | NEGATIVA |
| 2026-09-22 | 115,84 $ | 6,47 mld $ | +9,26% | 3,37 mld $ | +33,20% | 17,11 mld $ | 69,32% | 5 | POSITIVA FORTE |
| 2026-09-23 | 117,37 $ | 6,55 mld $ | +14,39% | 3,45 mld $ | +27,58% | 16,82 mld $ | 69,32% | 5 | POSITIVA FORTE |
| 2026-09-24 | 115,46 $ | 6,40 mld $ | +10,70% | 2,68 mld $ | -4,17% | 16,37 mld $ | 69,33% | 4 | POSITIVA |
| 2026-09-25 | 122,10 $ | 6,61 mld $ | +12,13% | 2,45 mld $ | -5,48% | 17,63 mld $ | 69,43% | 4 | POSITIVA |
| 2026-09-26 | 120,37 $ | 6,61 mld $ | +4,87% | 2,80 mld $ | -20,84% | 16,93 mld $ | 68,93% | 0 | NEUTRALE / MISTA |
| 2026-09-27 | 120,68 $ | 6,62 mld $ | +7,26% | 2,35 mld $ | -18,28% | 16,74 mld $ | 68,93% | 3 | POSITIVA |
| 2026-09-28 | 119,05 $ | 6,62 mld $ | +6,72% | 1,90 mld $ | -31,97% | 16,66 mld $ | 69,40% | 3 | POSITIVA |

## Come usarlo insieme al frattale SOL/BTC

- **Frattale positivo + score on-chain positivo**: setup più credibile.
- **Frattale positivo + on-chain neutrale**: setup ancora valido, ma non confermato dai fondamentali.
- **Frattale positivo + on-chain negativo**: attenzione, il prezzo può seguire la forma ma avere pressione sotto.
- **Exchange inflow alto**: rischio prese profitto.
- **Stablecoin, TVL, fee e DEX volume in crescita**: attività reale più sana.
- **Stake ratio alto e delinquent basso**: supply liquida più contenuta e rete più stabile.

## Nota importante

Solana non ha un costo di mining come Bitcoin, perché non è Proof-of-Work. Per SOL è più utile guardare staking, attività di rete, liquidità DeFi, stablecoin, DEX volume, fee, MVRV e holder profit/loss.
