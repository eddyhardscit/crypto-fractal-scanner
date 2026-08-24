# SOL on-chain metrics report

Generato: **2026-08-24 07:32:20 CEST**  
UTC: **2026-08-24 05:32:05 UTC**

Questo report aggiunge una lettura on-chain/fondamentale di Solana.

Non sostituisce il frattale SOL/BTC. Serve a capire se dietro il movimento ci sono segnali di rete sani oppure pressione/speculazione.

## Sintesi

| Voce | Valore |
| --- | --- |
| Score on-chain | 5 |
| Bias | POSITIVA FORTE |
| Azione coerente | ON-CHAIN SANO / RAFFORZA IL FRATTALE |
| Metriche importanti mancanti | sol_realized_price_usd, sol_mvrv, sol_holder_profit_pct, sol_exchange_netflow_24h_usd |

## Componenti del punteggio

| Componente | Valore | Punti | Lettura |
| --- | --- | --- | --- |
| TVL 7g | +16,32% | +1 | TVL in crescita: rete più forte. |
| DEX volume 7g | +195,58% | +1 | Volume DEX in aumento: attività reale più forte. |
| Fees 7g | +82,95% | +1 | Fee in crescita: uso della rete in miglioramento. |
| Stablecoin liquidity 7g | +2,85% | +1 | Stablecoin su Solana in aumento: liquidità disponibile migliore. |
| Stake ratio | 68,50% | +1 | Quota staked alta: supply liquida più contenuta. |
| Stake delinquent | 0,04% | 0 | Delinquent stake basso. |

## Metriche disponibili

| Metrica | Valore | Lettura |
| --- | --- | --- |
| Prezzo SOL | 94,05 $ | Prezzo spot usato per il report. |
| Market cap | 54,89 mld $ | Grandezza complessiva di mercato. |
| Volume 24h | 3,46 mld $ | Liquidità di trading spot aggregata. |
| TVL Solana | 5,56 mld $ | Capitale in DeFi su Solana. |
| TVL 7g | +16,32% | Crescita/calo DeFi a 7 giorni. |
| DEX volume 24h | 3,12 mld $ | Attività di scambio on-chain. |
| DEX volume 7g | 18,98 mld $ | Volume settimanale DEX. |
| DEX change 7g | +195,58% | Accelerazione o rallentamento DEX. |
| Fees 24h | 12,45 mln $ | Fee generate dalla chain/protocolli monitorati. |
| Fees 7g | 82,00 mln $ | Fee settimanali. |
| Fees change 7g | +82,95% | Uso rete in crescita/calo. |
| Stablecoin su Solana | 16,39 mld $ | Liquidità stabile disponibile su chain. |
| Stablecoin 7g | +2,85% | Entrata/uscita liquidità stabile. |
| Supply totale | 632.749.502 | Supply totale convertita da lamports a SOL. |
| Supply circolante | 583.276.393 | Supply circolante convertita da lamports a SOL. |
| SOL in stake | 433.436.313 | Stake attivo stimato da vote accounts. |
| Stake / supply totale | 68,50% | Quota supply totale in staking. |
| Stake / supply circolante | 74,31% | Quota supply circolante in staking. |
| Stake delinquent | 0,04% | Quota stake su validatori delinquent. |
| Validatori attivi | 685 | Validatori correnti letti da RPC. |
| Validatori delinquent | 10 | Validatori delinquent letti da RPC. |
| Inflazione stimata | 3,68% | Inflation rate da RPC. |

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
| 2026-08-19 | 76,89 $ | 4,90 mld $ | +0,75% | 1,82 mld $ | +10,98% | 15,95 mld $ | 68,89% | 1 | NEUTRALE / MISTA |
| 2026-08-20 | 84,91 $ | 5,20 mld $ | +7,83% | 2,79 mld $ | +62,55% | 16,26 mld $ | 68,81% | 4 | POSITIVA |
| 2026-08-21 | 89,58 $ | 5,34 mld $ | +10,44% | 2,78 mld $ | +43,83% | 16,45 mld $ | 68,81% | 4 | POSITIVA |
| 2026-08-22 | 94,02 $ | 5,62 mld $ | +16,93% | 3,47 mld $ | +115,88% | 16,36 mld $ | 68,52% | 5 | POSITIVA FORTE |
| 2026-08-23 | 93,10 $ | 5,56 mld $ | +15,63% | 3,65 mld $ | +212,06% | 16,31 mld $ | 68,50% | 5 | POSITIVA FORTE |
| 2026-08-24 | 94,09 $ | 5,56 mld $ | +16,32% | 3,12 mld $ | +195,58% | 16,39 mld $ | 68,50% | 5 | POSITIVA FORTE |

## Come usarlo insieme al frattale SOL/BTC

- **Frattale positivo + score on-chain positivo**: setup più credibile.
- **Frattale positivo + on-chain neutrale**: setup ancora valido, ma non confermato dai fondamentali.
- **Frattale positivo + on-chain negativo**: attenzione, il prezzo può seguire la forma ma avere pressione sotto.
- **Exchange inflow alto**: rischio prese profitto.
- **Stablecoin, TVL, fee e DEX volume in crescita**: attività reale più sana.
- **Stake ratio alto e delinquent basso**: supply liquida più contenuta e rete più stabile.

## Nota importante

Solana non ha un costo di mining come Bitcoin, perché non è Proof-of-Work. Per SOL è più utile guardare staking, attività di rete, liquidità DeFi, stablecoin, DEX volume, fee, MVRV e holder profit/loss.
