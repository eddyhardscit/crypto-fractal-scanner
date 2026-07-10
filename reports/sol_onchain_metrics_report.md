# SOL on-chain metrics report

Generato: **2026-07-10 03:35:12 CEST**  
UTC: **2026-07-10 01:35:01 UTC**

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
| TVL 7g | -2,02% | 0 | TVL stabile. |
| DEX volume 7g | -23,28% | -1 | Volume DEX in calo: attività più debole. |
| Fees 7g | -8,83% | 0 | Fee stabili. |
| Stablecoin liquidity 7g | -1,53% | 0 | Stablecoin stabili. |
| Stake ratio | 68,16% | +1 | Quota staked alta: supply liquida più contenuta. |
| Stake delinquent | 0,03% | 0 | Delinquent stake basso. |

## Metriche disponibili

| Metrica | Valore | Lettura |
| --- | --- | --- |
| Prezzo SOL | 78,33 $ | Prezzo spot usato per il report. |
| Market cap | 45,58 mld $ | Grandezza complessiva di mercato. |
| Volume 24h | 1,59 mld $ | Liquidità di trading spot aggregata. |
| TVL Solana | 4,94 mld $ | Capitale in DeFi su Solana. |
| TVL 7g | -2,02% | Crescita/calo DeFi a 7 giorni. |
| DEX volume 24h | 1,79 mld $ | Attività di scambio on-chain. |
| DEX volume 7g | 14,50 mld $ | Volume settimanale DEX. |
| DEX change 7g | -23,28% | Accelerazione o rallentamento DEX. |
| Fees 24h | 8,25 mln $ | Fee generate dalla chain/protocolli monitorati. |
| Fees 7g | 49,89 mln $ | Fee settimanali. |
| Fees change 7g | -8,83% | Uso rete in crescita/calo. |
| Stablecoin su Solana | 15,39 mld $ | Liquidità stabile disponibile su chain. |
| Stablecoin 7g | -1,53% | Entrata/uscita liquidità stabile. |
| Supply totale | 629.973.945 | Supply totale convertita da lamports a SOL. |
| Supply circolante | 581.838.209 | Supply circolante convertita da lamports a SOL. |
| SOL in stake | 429.413.833 | Stake attivo stimato da vote accounts. |
| Stake / supply totale | 68,16% | Quota supply totale in staking. |
| Stake / supply circolante | 73,80% | Quota supply circolante in staking. |
| Stake delinquent | 0,03% | Quota stake su validatori delinquent. |
| Validatori attivi | 705 | Validatori correnti letti da RPC. |
| Validatori delinquent | 25 | Validatori delinquent letti da RPC. |
| Inflazione stimata | 3,75% | Inflation rate da RPC. |

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
| 2026-07-10 | 78,33 $ | 4,94 mld $ | -2,02% | 1,79 mld $ | -23,28% | 15,39 mld $ | 68,16% | 0 | NEUTRALE / MISTA |

## Come usarlo insieme al frattale SOL/BTC

- **Frattale positivo + score on-chain positivo**: setup più credibile.
- **Frattale positivo + on-chain neutrale**: setup ancora valido, ma non confermato dai fondamentali.
- **Frattale positivo + on-chain negativo**: attenzione, il prezzo può seguire la forma ma avere pressione sotto.
- **Exchange inflow alto**: rischio prese profitto.
- **Stablecoin, TVL, fee e DEX volume in crescita**: attività reale più sana.
- **Stake ratio alto e delinquent basso**: supply liquida più contenuta e rete più stabile.

## Nota importante

Solana non ha un costo di mining come Bitcoin, perché non è Proof-of-Work. Per SOL è più utile guardare staking, attività di rete, liquidità DeFi, stablecoin, DEX volume, fee, MVRV e holder profit/loss.
