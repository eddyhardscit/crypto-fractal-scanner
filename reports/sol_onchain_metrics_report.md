# SOL on-chain metrics report

Generato: **2026-07-20 07:14:28 CEST**  
UTC: **2026-07-20 05:14:22 UTC**

Questo report aggiunge una lettura on-chain/fondamentale di Solana.

Non sostituisce il frattale SOL/BTC. Serve a capire se dietro il movimento ci sono segnali di rete sani oppure pressione/speculazione.

## Sintesi

| Voce | Valore |
| --- | --- |
| Score on-chain | 0 |
| Bias | NEUTRALE / MISTA |
| Azione coerente | NESSUNA CONFERMA FORTE / LEGGERE INSIEME AL FRATTALE |
| Metriche importanti mancanti | sol_realized_price_usd, sol_mvrv, sol_holder_profit_pct, sol_exchange_netflow_24h_usd |

## Componenti del punteggio

| Componente | Valore | Punti | Lettura |
| --- | --- | --- | --- |
| TVL 7g | +1,19% | 0 | TVL stabile. |
| DEX volume 7g | +3,62% | 0 | Volume DEX stabile. |
| Fees 7g | -15,16% | -1 | Fee in calo: uso della rete più debole. |
| Stablecoin liquidity 7g | +0,97% | 0 | Stablecoin stabili. |
| Stake ratio | 67,76% | +1 | Quota staked alta: supply liquida più contenuta. |
| Stake delinquent | 0,16% | 0 | Delinquent stake basso. |

## Metriche disponibili

| Metrica | Valore | Lettura |
| --- | --- | --- |
| Prezzo SOL | 75,92 $ | Prezzo spot usato per il report. |
| Market cap | 44,38 mld $ | Grandezza complessiva di mercato. |
| Volume 24h | 1,39 mld $ | Liquidità di trading spot aggregata. |
| TVL Solana | 4,90 mld $ | Capitale in DeFi su Solana. |
| TVL 7g | +1,19% | Crescita/calo DeFi a 7 giorni. |
| DEX volume 24h | 1,25 mld $ | Attività di scambio on-chain. |
| DEX volume 7g | 10,64 mld $ | Volume settimanale DEX. |
| DEX change 7g | +3,62% | Accelerazione o rallentamento DEX. |
| Fees 24h | 4,82 mln $ | Fee generate dalla chain/protocolli monitorati. |
| Fees 7g | 41,44 mln $ | Fee settimanali. |
| Fees change 7g | -15,16% | Uso rete in crescita/calo. |
| Stablecoin su Solana | 15,71 mld $ | Liquidità stabile disponibile su chain. |
| Stablecoin 7g | +0,97% | Entrata/uscita liquidità stabile. |
| Supply totale | 630.612.704 | Supply totale convertita da lamports a SOL. |
| Supply circolante | 582.632.471 | Supply circolante convertita da lamports a SOL. |
| SOL in stake | 427.304.217 | Stake attivo stimato da vote accounts. |
| Stake / supply totale | 67,76% | Quota supply totale in staking. |
| Stake / supply circolante | 73,34% | Quota supply circolante in staking. |
| Stake delinquent | 0,16% | Quota stake su validatori delinquent. |
| Validatori attivi | 698 | Validatori correnti letti da RPC. |
| Validatori delinquent | 16 | Validatori delinquent letti da RPC. |
| Inflazione stimata | 3,74% | Inflation rate da RPC. |

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
| 2026-07-08 | 77,46 $ | 4,93 mld $ | +3,25% | 2,55 mld $ | +8,81% | 15,59 mld $ | 68,16% | 0 | NEUTRALE / MISTA |
| 2026-07-09 | 77,98 $ | 4,95 mld $ | +0,89% | 2,44 mld $ | +4,56% | 15,39 mld $ | 68,16% | 2 | POSITIVA |
| 2026-07-10 | 78,03 $ | 4,92 mld $ | -2,31% | 1,79 mld $ | -23,19% | 15,36 mld $ | 67,94% | -2 | NEGATIVA |
| 2026-07-11 | 78,01 $ | 4,94 mld $ | -3,52% | 1,59 mld $ | -10,93% | 15,43 mld $ | 67,94% | 0 | NEUTRALE / MISTA |
| 2026-07-12 | 76,47 $ | 4,87 mld $ | -4,77% | 1,13 mld $ | -47,34% | 15,47 mld $ | 67,94% | -1 | NEUTRALE / MISTA |
| 2026-07-13 | 76,31 $ | 4,86 mld $ | -4,87% | 1,14 mld $ | -39,96% | 15,56 mld $ | 68,07% | 0 | NEUTRALE / MISTA |
| 2026-07-14 | 77,19 $ | 4,89 mld $ | -4,85% | 1,77 mld $ | -19,15% | 15,15 mld $ | 67,58% | -2 | NEGATIVA |
| 2026-07-15 | 77,75 $ | 4,92 mld $ | -1,56% | 1,90 mld $ | -25,44% | 15,05 mld $ | 67,58% | -1 | NEUTRALE / MISTA |
| 2026-07-16 | 76,30 $ | 4,86 mld $ | -1,50% | 1,62 mld $ | -33,52% | 14,89 mld $ | 67,58% | -2 | NEGATIVA |
| 2026-07-17 | 74,47 $ | 4,82 mld $ | -2,76% | 1,56 mld $ | -12,83% | 15,33 mld $ | 67,59% | 1 | NEUTRALE / MISTA |
| 2026-07-18 | 74,98 $ | 4,82 mld $ | -2,21% | 1,43 mld $ | -11,89% | 15,63 mld $ | 67,59% | -1 | NEUTRALE / MISTA |
| 2026-07-19 | 75,98 $ | 4,87 mld $ | +0,51% | 1,29 mld $ | +21,21% | 15,69 mld $ | 67,76% | 3 | POSITIVA |
| 2026-07-20 | 76,17 $ | 4,90 mld $ | +1,19% | 1,25 mld $ | +3,62% | 15,71 mld $ | 67,76% | 0 | NEUTRALE / MISTA |

## Come usarlo insieme al frattale SOL/BTC

- **Frattale positivo + score on-chain positivo**: setup più credibile.
- **Frattale positivo + on-chain neutrale**: setup ancora valido, ma non confermato dai fondamentali.
- **Frattale positivo + on-chain negativo**: attenzione, il prezzo può seguire la forma ma avere pressione sotto.
- **Exchange inflow alto**: rischio prese profitto.
- **Stablecoin, TVL, fee e DEX volume in crescita**: attività reale più sana.
- **Stake ratio alto e delinquent basso**: supply liquida più contenuta e rete più stabile.

## Nota importante

Solana non ha un costo di mining come Bitcoin, perché non è Proof-of-Work. Per SOL è più utile guardare staking, attività di rete, liquidità DeFi, stablecoin, DEX volume, fee, MVRV e holder profit/loss.
