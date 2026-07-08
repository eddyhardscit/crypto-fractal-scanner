# SOL on-chain metrics report

Generato: **2026-07-08 20:20:50 CEST**  
UTC: **2026-07-08 18:20:38 UTC**

Questo report aggiunge una lettura on-chain/fondamentale di Solana.

Non sostituisce il frattale SOL/BTC. Serve a capire se dietro il movimento ci sono segnali di rete sani oppure pressione/speculazione.

## Sintesi

| Voce | Valore |
| --- | --- |
| Score on-chain | -2 |
| Bias | NEGATIVA |
| Azione coerente | PRUDENZA / POSSIBILE PRESSIONE |
| Metriche importanti mancanti | sol_realized_price_usd, sol_mvrv, sol_holder_profit_pct, sol_exchange_netflow_24h_usd |

## Componenti del punteggio

| Componente | Valore | Punti | Lettura |
| --- | --- | --- | --- |
| TVL 7g | +3,20% | 0 | TVL stabile. |
| DEX volume 7g | +9,31% | 0 | Volume DEX stabile. |
| Fees 7g | -19,04% | -1 | Fee in calo: uso della rete più debole. |
| Stablecoin liquidity 7g | +0,36% | 0 | Stablecoin stabili. |
| Stake ratio | 0,00% | -1 | Quota staked bassa: supply più liquida. |
| Stake delinquent | 0,10% | 0 | Delinquent stake basso. |

## Metriche disponibili

| Metrica | Valore | Lettura |
| --- | --- | --- |
| Prezzo SOL | 77,19 $ | Prezzo spot usato per il report. |
| Market cap | 44,91 mld $ | Grandezza complessiva di mercato. |
| Volume 24h | 2,48 mld $ | Liquidità di trading spot aggregata. |
| TVL Solana | 4,93 mld $ | Capitale in DeFi su Solana. |
| TVL 7g | +3,20% | Crescita/calo DeFi a 7 giorni. |
| DEX volume 24h | 2,56 mld $ | Attività di scambio on-chain. |
| DEX volume 7g | 15,13 mld $ | Volume settimanale DEX. |
| DEX change 7g | +9,31% | Accelerazione o rallentamento DEX. |
| Fees 24h | 8,09 mln $ | Fee generate dalla chain/protocolli monitorati. |
| Fees 7g | 55,73 mln $ | Fee settimanali. |
| Fees change 7g | -19,04% | Uso rete in crescita/calo. |
| Stablecoin su Solana | 15,59 mld $ | Liquidità stabile disponibile su chain. |
| Stablecoin 7g | +0,36% | Entrata/uscita liquidità stabile. |
| Supply totale | 629.974.945.001.625.472 | Supply totale da Solana RPC. |
| Supply circolante | 581.830.719.567.457.664 | Supply circolante da Solana RPC. |
| SOL in stake | 429.413.843 | Stake attivo stimato da vote accounts. |
| Stake / supply totale | 0,00% | Quota supply bloccata in staking. |
| Stake delinquent | 0,10% | Quota stake su validatori delinquent. |
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
| 2026-07-08 | 77,19 $ | 4,93 mld $ | +3,20% | 2,56 mld $ | +9,31% | 15,59 mld $ | 0,00% | -2 | NEGATIVA |

## Come usarlo insieme al frattale SOL/BTC

- **Frattale positivo + score on-chain positivo**: setup più credibile.
- **Frattale positivo + on-chain neutrale**: setup ancora valido, ma non confermato dai fondamentali.
- **Frattale positivo + on-chain negativo**: attenzione, il prezzo può seguire la forma ma avere pressione sotto.
- **Exchange inflow alto**: rischio prese profitto.
- **Stablecoin, TVL, fee e DEX volume in crescita**: attività reale più sana.
- **Stake ratio alto e delinquent basso**: supply liquida più contenuta e rete più stabile.

## Nota importante

Solana non ha un costo di mining come Bitcoin, perché non è Proof-of-Work. Per SOL è più utile guardare staking, attività di rete, liquidità DeFi, stablecoin, DEX volume, fee, MVRV e holder profit/loss.
