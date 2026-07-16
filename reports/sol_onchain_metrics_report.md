# SOL on-chain metrics report

Generato: **2026-07-16 12:53:34 CEST**  
UTC: **2026-07-16 10:53:26 UTC**

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
| TVL 7g | -1,30% | 0 | TVL stabile. |
| DEX volume 7g | -32,19% | -1 | Volume DEX in calo: attività più debole. |
| Fees 7g | -25,84% | -1 | Fee in calo: uso della rete più debole. |
| Stablecoin liquidity 7g | -3,19% | -1 | Stablecoin su Solana in calo: liquidità in uscita. |
| Stake ratio | 67,58% | +1 | Quota staked alta: supply liquida più contenuta. |
| Stake delinquent | 0,08% | 0 | Delinquent stake basso. |

## Metriche disponibili

| Metrica | Valore | Lettura |
| --- | --- | --- |
| Prezzo SOL | 76,10 $ | Prezzo spot usato per il report. |
| Market cap | 44,33 mld $ | Grandezza complessiva di mercato. |
| Volume 24h | 2,00 mld $ | Liquidità di trading spot aggregata. |
| TVL Solana | 4,87 mld $ | Capitale in DeFi su Solana. |
| TVL 7g | -1,30% | Crescita/calo DeFi a 7 giorni. |
| DEX volume 24h | 1,66 mld $ | Attività di scambio on-chain. |
| DEX volume 7g | 10,79 mld $ | Volume settimanale DEX. |
| DEX change 7g | -32,19% | Accelerazione o rallentamento DEX. |
| Fees 24h | 6,12 mln $ | Fee generate dalla chain/protocolli monitorati. |
| Fees 7g | 43,08 mln $ | Fee settimanali. |
| Fees change 7g | -25,84% | Uso rete in crescita/calo. |
| Stablecoin su Solana | 14,89 mld $ | Liquidità stabile disponibile su chain. |
| Stablecoin 7g | -3,19% | Entrata/uscita liquidità stabile. |
| Supply totale | 630.357.197 | Supply totale convertita da lamports a SOL. |
| Supply circolante | 582.409.363 | Supply circolante convertita da lamports a SOL. |
| SOL in stake | 425.977.801 | Stake attivo stimato da vote accounts. |
| Stake / supply totale | 67,58% | Quota supply totale in staking. |
| Stake / supply circolante | 73,14% | Quota supply circolante in staking. |
| Stake delinquent | 0,08% | Quota stake su validatori delinquent. |
| Validatori attivi | 702 | Validatori correnti letti da RPC. |
| Validatori delinquent | 12 | Validatori delinquent letti da RPC. |
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
| 2026-07-16 | 76,11 $ | 4,87 mld $ | -1,30% | 1,66 mld $ | -32,19% | 14,89 mld $ | 67,58% | -2 | NEGATIVA |

## Come usarlo insieme al frattale SOL/BTC

- **Frattale positivo + score on-chain positivo**: setup più credibile.
- **Frattale positivo + on-chain neutrale**: setup ancora valido, ma non confermato dai fondamentali.
- **Frattale positivo + on-chain negativo**: attenzione, il prezzo può seguire la forma ma avere pressione sotto.
- **Exchange inflow alto**: rischio prese profitto.
- **Stablecoin, TVL, fee e DEX volume in crescita**: attività reale più sana.
- **Stake ratio alto e delinquent basso**: supply liquida più contenuta e rete più stabile.

## Nota importante

Solana non ha un costo di mining come Bitcoin, perché non è Proof-of-Work. Per SOL è più utile guardare staking, attività di rete, liquidità DeFi, stablecoin, DEX volume, fee, MVRV e holder profit/loss.
