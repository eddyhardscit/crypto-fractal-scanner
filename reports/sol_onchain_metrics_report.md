# SOL on-chain metrics report

Generato: **2026-09-01 07:32:39 CEST**  
UTC: **2026-09-01 05:32:28 UTC**

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
| TVL 7g | +1,69% | 0 | TVL stabile. |
| DEX volume 7g | -17,97% | -1 | Volume DEX in calo: attività più debole. |
| Fees 7g | -8,41% | 0 | Fee stabili. |
| Stablecoin liquidity 7g | -1,78% | 0 | Stablecoin stabili. |
| Stake ratio | 69,20% | +1 | Quota staked alta: supply liquida più contenuta. |
| Stake delinquent | 0,01% | 0 | Delinquent stake basso. |

## Metriche disponibili

| Metrica | Valore | Lettura |
| --- | --- | --- |
| Prezzo SOL | 103,93 $ | Prezzo spot usato per il report. |
| Market cap | 60,83 mld $ | Grandezza complessiva di mercato. |
| Volume 24h | 2,95 mld $ | Liquidità di trading spot aggregata. |
| TVL Solana | 5,83 mld $ | Capitale in DeFi su Solana. |
| TVL 7g | +1,69% | Crescita/calo DeFi a 7 giorni. |
| DEX volume 24h | 2,46 mld $ | Attività di scambio on-chain. |
| DEX volume 7g | 17,42 mld $ | Volume settimanale DEX. |
| DEX change 7g | -17,97% | Accelerazione o rallentamento DEX. |
| Fees 24h | 13,29 mln $ | Fee generate dalla chain/protocolli monitorati. |
| Fees 7g | 96,17 mln $ | Fee settimanali. |
| Fees change 7g | -8,41% | Uso rete in crescita/calo. |
| Stablecoin su Solana | 16,07 mld $ | Liquidità stabile disponibile su chain. |
| Stablecoin 7g | -1,78% | Entrata/uscita liquidità stabile. |
| Supply totale | 633.267.530 | Supply totale convertita da lamports a SOL. |
| Supply circolante | 585.207.101 | Supply circolante convertita da lamports a SOL. |
| SOL in stake | 438.201.819 | Stake attivo stimato da vote accounts. |
| Stake / supply totale | 69,20% | Quota supply totale in staking. |
| Stake / supply circolante | 74,88% | Quota supply circolante in staking. |
| Stake delinquent | 0,01% | Quota stake su validatori delinquent. |
| Validatori attivi | 680 | Validatori correnti letti da RPC. |
| Validatori delinquent | 14 | Validatori delinquent letti da RPC. |
| Inflazione stimata | 3,67% | Inflation rate da RPC. |

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
| 2026-08-01 | 73,11 $ | 4,74 mld $ | -0,87% | 1,73 mld $ | +12,08% | 16,29 mld $ | 68,50% | 2 | POSITIVA |
| 2026-08-02 | 73,44 $ | 4,73 mld $ | -1,91% | 1,36 mld $ | +29,05% | 16,24 mld $ | 68,50% | 0 | NEUTRALE / MISTA |
| 2026-08-03 | 72,94 $ | 4,74 mld $ | -3,38% | 1,33 mld $ | +10,73% | 16,17 mld $ | 68,51% | 2 | POSITIVA |
| 2026-08-04 | 73,65 $ | 4,76 mld $ | -0,90% | 1,68 mld $ | -8,75% | 16,35 mld $ | 68,51% | 0 | NEUTRALE / MISTA |
| 2026-08-05 | 73,92 $ | 4,80 mld $ | +0,44% | 1,74 mld $ | +0,13% | 16,49 mld $ | 68,78% | 3 | POSITIVA |
| 2026-08-06 | 74,13 $ | 4,78 mld $ | -0,05% | 1,65 mld $ | -15,98% | 16,14 mld $ | 68,78% | -1 | NEUTRALE / MISTA |
| 2026-08-07 | 72,64 $ | 4,70 mld $ | -2,43% | 1,40 mld $ | -11,40% | 16,19 mld $ | 68,83% | 1 | NEUTRALE / MISTA |
| 2026-08-08 | 74,53 $ | 4,75 mld $ | +0,26% | 1,36 mld $ | -19,90% | 16,18 mld $ | 68,83% | 0 | NEUTRALE / MISTA |
| 2026-08-09 | 75,93 $ | 4,80 mld $ | +2,08% | 1,48 mld $ | +13,11% | 16,20 mld $ | 68,69% | 3 | POSITIVA |
| 2026-08-10 | 76,53 $ | 4,85 mld $ | +2,50% | 1,37 mld $ | +1,37% | 16,25 mld $ | 68,69% | 2 | POSITIVA |
| 2026-08-11 | 75,91 $ | 4,83 mld $ | +1,77% | 1,55 mld $ | -9,69% | 16,26 mld $ | 68,82% | 2 | POSITIVA |
| 2026-08-14 | 75,33 $ | 4,83 mld $ | +2,30% | 1,98 mld $ | +43,45% | 16,03 mld $ | 68,76% | 3 | POSITIVA |
| 2026-08-15 | 75,40 $ | 4,82 mld $ | +1,52% | 1,64 mld $ | +20,64% | 15,94 mld $ | 68,88% | 2 | POSITIVA |
| 2026-08-16 | 75,32 $ | 4,81 mld $ | +0,11% | 1,23 mld $ | -16,85% | 15,94 mld $ | 68,88% | -1 | NEUTRALE / MISTA |
| 2026-08-17 | 75,46 $ | 4,80 mld $ | -1,13% | 1,05 mld $ | -21,27% | 15,94 mld $ | 68,89% | -1 | NEUTRALE / MISTA |
| 2026-08-18 | 75,70 $ | 4,84 mld $ | +0,01% | 1,43 mld $ | -9,39% | 15,92 mld $ | 68,89% | 0 | NEUTRALE / MISTA |
| 2026-08-19 | 76,89 $ | 4,90 mld $ | +0,75% | 1,82 mld $ | +10,98% | 15,95 mld $ | 68,89% | 1 | NEUTRALE / MISTA |
| 2026-08-20 | 84,91 $ | 5,20 mld $ | +7,83% | 2,79 mld $ | +62,55% | 16,26 mld $ | 68,81% | 4 | POSITIVA |
| 2026-08-21 | 89,58 $ | 5,34 mld $ | +10,44% | 2,78 mld $ | +43,83% | 16,45 mld $ | 68,81% | 4 | POSITIVA |
| 2026-08-22 | 94,02 $ | 5,62 mld $ | +16,93% | 3,47 mld $ | +115,88% | 16,36 mld $ | 68,52% | 5 | POSITIVA FORTE |
| 2026-08-23 | 93,10 $ | 5,56 mld $ | +15,63% | 3,65 mld $ | +212,06% | 16,31 mld $ | 68,50% | 5 | POSITIVA FORTE |
| 2026-08-24 | 94,09 $ | 5,56 mld $ | +16,32% | 3,12 mld $ | +195,58% | 16,39 mld $ | 68,50% | 5 | POSITIVA FORTE |
| 2026-08-25 | 102,58 $ | 5,79 mld $ | +19,32% | 2,99 mld $ | +102,57% | 16,36 mld $ | 68,75% | 5 | POSITIVA FORTE |
| 2026-08-26 | 96,79 $ | 5,60 mld $ | +14,37% | 2,95 mld $ | +60,42% | 16,25 mld $ | 68,75% | 4 | POSITIVA |
| 2026-08-27 | 100,99 $ | 5,77 mld $ | +10,39% | 2,48 mld $ | -17,56% | 16,22 mld $ | 69,02% | 1 | NEUTRALE / MISTA |
| 2026-08-28 | 106,36 $ | 5,96 mld $ | +11,73% | 3,63 mld $ | +31,27% | 16,32 mld $ | 69,02% | 4 | POSITIVA |
| 2026-08-29 | 104,05 $ | 5,86 mld $ | +5,61% | 2,62 mld $ | -27,38% | 16,28 mld $ | 68,89% | 2 | POSITIVA |
| 2026-08-30 | 105,04 $ | 5,91 mld $ | +6,27% | 1,81 mld $ | -51,42% | 16,23 mld $ | 69,04% | 1 | NEUTRALE / MISTA |
| 2026-08-31 | 102,60 $ | 5,78 mld $ | +3,84% | 1,87 mld $ | -36,38% | 16,06 mld $ | 69,04% | -1 | NEUTRALE / MISTA |
| 2026-09-01 | 103,95 $ | 5,83 mld $ | +1,69% | 2,46 mld $ | -17,97% | 16,07 mld $ | 69,20% | 0 | NEUTRALE / MISTA |

## Come usarlo insieme al frattale SOL/BTC

- **Frattale positivo + score on-chain positivo**: setup più credibile.
- **Frattale positivo + on-chain neutrale**: setup ancora valido, ma non confermato dai fondamentali.
- **Frattale positivo + on-chain negativo**: attenzione, il prezzo può seguire la forma ma avere pressione sotto.
- **Exchange inflow alto**: rischio prese profitto.
- **Stablecoin, TVL, fee e DEX volume in crescita**: attività reale più sana.
- **Stake ratio alto e delinquent basso**: supply liquida più contenuta e rete più stabile.

## Nota importante

Solana non ha un costo di mining come Bitcoin, perché non è Proof-of-Work. Per SOL è più utile guardare staking, attività di rete, liquidità DeFi, stablecoin, DEX volume, fee, MVRV e holder profit/loss.
