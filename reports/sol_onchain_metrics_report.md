# SOL on-chain metrics report

Generato: **2026-08-18 07:32:26 CEST**  
UTC: **2026-08-18 05:32:08 UTC**

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
| TVL 7g | +0,01% | 0 | TVL stabile. |
| DEX volume 7g | -9,39% | 0 | Volume DEX stabile. |
| Fees 7g | +2,60% | 0 | Fee stabili. |
| Stablecoin liquidity 7g | -2,13% | -1 | Stablecoin su Solana in calo: liquidità in uscita. |
| Stake ratio | 68,89% | +1 | Quota staked alta: supply liquida più contenuta. |
| Stake delinquent | 0,01% | 0 | Delinquent stake basso. |

## Metriche disponibili

| Metrica | Valore | Lettura |
| --- | --- | --- |
| Prezzo SOL | 75,70 $ | Prezzo spot usato per il report. |
| Market cap | 44,13 mld $ | Grandezza complessiva di mercato. |
| Volume 24h | 1,31 mld $ | Liquidità di trading spot aggregata. |
| TVL Solana | 4,84 mld $ | Capitale in DeFi su Solana. |
| TVL 7g | +0,01% | Crescita/calo DeFi a 7 giorni. |
| DEX volume 24h | 1,43 mld $ | Attività di scambio on-chain. |
| DEX volume 7g | 10,47 mld $ | Volume settimanale DEX. |
| DEX change 7g | -9,39% | Accelerazione o rallentamento DEX. |
| Fees 24h | 10,77 mln $ | Fee generate dalla chain/protocolli monitorati. |
| Fees 7g | 61,82 mln $ | Fee settimanali. |
| Fees change 7g | +2,60% | Uso rete in crescita/calo. |
| Stablecoin su Solana | 15,92 mld $ | Liquidità stabile disponibile su chain. |
| Stablecoin 7g | -2,13% | Entrata/uscita liquidità stabile. |
| Supply totale | 632.387.909 | Supply totale convertita da lamports a SOL. |
| Supply circolante | 582.895.649 | Supply circolante convertita da lamports a SOL. |
| SOL in stake | 435.676.796 | Stake attivo stimato da vote accounts. |
| Stake / supply totale | 68,89% | Quota supply totale in staking. |
| Stake / supply circolante | 74,74% | Quota supply circolante in staking. |
| Stake delinquent | 0,01% | Quota stake su validatori delinquent. |
| Validatori attivi | 689 | Validatori correnti letti da RPC. |
| Validatori delinquent | 6 | Validatori delinquent letti da RPC. |
| Inflazione stimata | 3,69% | Inflation rate da RPC. |

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
| 2026-07-18 | 74,98 $ | 4,82 mld $ | -2,21% | 1,43 mld $ | -11,89% | 15,63 mld $ | 67,59% | -1 | NEUTRALE / MISTA |
| 2026-07-19 | 75,98 $ | 4,87 mld $ | +0,51% | 1,29 mld $ | +21,21% | 15,69 mld $ | 67,76% | 3 | POSITIVA |
| 2026-07-20 | 76,17 $ | 4,90 mld $ | +1,19% | 1,25 mld $ | +3,62% | 15,71 mld $ | 67,76% | 0 | NEUTRALE / MISTA |
| 2026-07-21 | 78,17 $ | 4,97 mld $ | +3,45% | 1,83 mld $ | +3,43% | 15,71 mld $ | 67,60% | 3 | POSITIVA |
| 2026-07-22 | 77,84 $ | 4,98 mld $ | +1,50% | 1,50 mld $ | -21,47% | 15,86 mld $ | 67,60% | 0 | NEUTRALE / MISTA |
| 2026-07-23 | 77,11 $ | 4,99 mld $ | +1,47% | 1,72 mld $ | +6,24% | 16,97 mld $ | 67,81% | 3 | POSITIVA |
| 2026-07-24 | 75,70 $ | 4,90 mld $ | +1,24% | 1,47 mld $ | -5,15% | 17,02 mld $ | 67,81% | 2 | POSITIVA |
| 2026-07-25 | 74,19 $ | 4,80 mld $ | -0,25% | 1,54 mld $ | +7,86% | 17,03 mld $ | 67,96% | 3 | POSITIVA |
| 2026-07-26 | 75,02 $ | 4,83 mld $ | -0,55% | 1,14 mld $ | -6,23% | 16,96 mld $ | 67,96% | 2 | POSITIVA |
| 2026-07-27 | 76,33 $ | 4,90 mld $ | +0,77% | 1,18 mld $ | -9,41% | 16,87 mld $ | 67,93% | 3 | POSITIVA |
| 2026-07-28 | 73,28 $ | 4,78 mld $ | -3,65% | 1,77 mld $ | -5,26% | 17,20 mld $ | 67,93% | 3 | POSITIVA |
| 2026-07-29 | 73,45 $ | 4,77 mld $ | -4,29% | 1,75 mld $ | +16,98% | 16,12 mld $ | 67,93% | 3 | POSITIVA |
| 2026-07-30 | 73,45 $ | 4,79 mld $ | -3,21% | 1,94 mld $ | +12,40% | 16,29 mld $ | 67,86% | 1 | NEUTRALE / MISTA |
| 2026-07-31 | 74,03 $ | 4,80 mld $ | -2,18% | 1,60 mld $ | +7,95% | 16,30 mld $ | 67,86% | 0 | NEUTRALE / MISTA |
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

## Come usarlo insieme al frattale SOL/BTC

- **Frattale positivo + score on-chain positivo**: setup più credibile.
- **Frattale positivo + on-chain neutrale**: setup ancora valido, ma non confermato dai fondamentali.
- **Frattale positivo + on-chain negativo**: attenzione, il prezzo può seguire la forma ma avere pressione sotto.
- **Exchange inflow alto**: rischio prese profitto.
- **Stablecoin, TVL, fee e DEX volume in crescita**: attività reale più sana.
- **Stake ratio alto e delinquent basso**: supply liquida più contenuta e rete più stabile.

## Nota importante

Solana non ha un costo di mining come Bitcoin, perché non è Proof-of-Work. Per SOL è più utile guardare staking, attività di rete, liquidità DeFi, stablecoin, DEX volume, fee, MVRV e holder profit/loss.
