# Calibrazione pesi Global Confluence

Generato: **2026-07-09 15:03 UTC**

Questo report prepara la calibrazione futura dei pesi del Global Confluence.

Non modifica ancora i pesi dello scanner. Per ora legge l'accuratezza dei moduli e stabilisce quando ci saranno abbastanza dati per fidarsi.

## Regola prudente

- Sotto **30** controlli: solo raccolta dati.
- Da **30** a **59** controlli: osservazione iniziale, non applicare.
- Da **60** a **99** controlli: suggerimento leggero.
- Da **100+** controlli: dati sufficienti per valutare una modifica prudente dei pesi.

Fonte dati letta: **module_accuracy_metrics.csv**

## Sintesi stato calibrazione pesi

| Asset   |   Moduli monitorati |   Controlli max |   Controlli min | Stato generale   |   Moduli con 60+ |   Moduli con 100+ | Lettura                                       |
|:--------|--------------------:|----------------:|----------------:|:-----------------|-----------------:|------------------:|:----------------------------------------------|
| BTC     |                   8 |               0 |               0 | RACCOLTA DATI    |                0 |                 0 | troppi pochi controlli: non modificare i pesi |
| DOGE    |                   8 |               0 |               0 | RACCOLTA DATI    |                0 |                 0 | troppi pochi controlli: non modificare i pesi |
| SOL     |                  10 |               0 |               0 | RACCOLTA DATI    |                0 |                 0 | troppi pochi controlli: non modificare i pesi |

## Dettaglio moduli

| Asset   | Modulo            | Orizzonte   |   Controlli | Accuracy   | Return medio   | Drawdown medio   | Max gain medio   | Stato         | Delta peso   | Suggerimento        |
|:--------|:------------------|:------------|------------:|:-----------|:---------------|:-----------------|:-----------------|:--------------|:-------------|:--------------------|
| BTC     | Global confluence | 30g         |           0 | n/a        | n/a            | n/a              | n/a              | RACCOLTA DATI | 0,00         | nessun suggerimento |
| BTC     | Market regime     | 30g         |           0 | n/a        | n/a            | n/a              | n/a              | RACCOLTA DATI | 0,00         | nessun suggerimento |
| BTC     | Scanner           | 30g         |           0 | n/a        | n/a            | n/a              | n/a              | RACCOLTA DATI | 0,00         | nessun suggerimento |
| BTC     | Tecnico           | 30g         |           0 | n/a        | n/a            | n/a              | n/a              | RACCOLTA DATI | 0,00         | nessun suggerimento |
| BTC     | Global confluence | 60g         |           0 | n/a        | n/a            | n/a              | n/a              | RACCOLTA DATI | 0,00         | nessun suggerimento |
| BTC     | Market regime     | 60g         |           0 | n/a        | n/a            | n/a              | n/a              | RACCOLTA DATI | 0,00         | nessun suggerimento |
| BTC     | Scanner           | 60g         |           0 | n/a        | n/a            | n/a              | n/a              | RACCOLTA DATI | 0,00         | nessun suggerimento |
| BTC     | Tecnico           | 60g         |           0 | n/a        | n/a            | n/a              | n/a              | RACCOLTA DATI | 0,00         | nessun suggerimento |
| SOL     | Frattale SOL      | 30g         |           0 | n/a        | n/a            | n/a              | n/a              | RACCOLTA DATI | 0,00         | nessun suggerimento |
| SOL     | Global confluence | 30g         |           0 | n/a        | n/a            | n/a              | n/a              | RACCOLTA DATI | 0,00         | nessun suggerimento |
| SOL     | Market regime     | 30g         |           0 | n/a        | n/a            | n/a              | n/a              | RACCOLTA DATI | 0,00         | nessun suggerimento |
| SOL     | Scanner           | 30g         |           0 | n/a        | n/a            | n/a              | n/a              | RACCOLTA DATI | 0,00         | nessun suggerimento |
| SOL     | Tecnico           | 30g         |           0 | n/a        | n/a            | n/a              | n/a              | RACCOLTA DATI | 0,00         | nessun suggerimento |
| SOL     | Frattale SOL      | 60g         |           0 | n/a        | n/a            | n/a              | n/a              | RACCOLTA DATI | 0,00         | nessun suggerimento |
| SOL     | Global confluence | 60g         |           0 | n/a        | n/a            | n/a              | n/a              | RACCOLTA DATI | 0,00         | nessun suggerimento |
| SOL     | Market regime     | 60g         |           0 | n/a        | n/a            | n/a              | n/a              | RACCOLTA DATI | 0,00         | nessun suggerimento |
| SOL     | Scanner           | 60g         |           0 | n/a        | n/a            | n/a              | n/a              | RACCOLTA DATI | 0,00         | nessun suggerimento |
| SOL     | Tecnico           | 60g         |           0 | n/a        | n/a            | n/a              | n/a              | RACCOLTA DATI | 0,00         | nessun suggerimento |
| DOGE    | Global confluence | 30g         |           0 | n/a        | n/a            | n/a              | n/a              | RACCOLTA DATI | 0,00         | nessun suggerimento |
| DOGE    | Market regime     | 30g         |           0 | n/a        | n/a            | n/a              | n/a              | RACCOLTA DATI | 0,00         | nessun suggerimento |
| DOGE    | Scanner           | 30g         |           0 | n/a        | n/a            | n/a              | n/a              | RACCOLTA DATI | 0,00         | nessun suggerimento |
| DOGE    | Tecnico           | 30g         |           0 | n/a        | n/a            | n/a              | n/a              | RACCOLTA DATI | 0,00         | nessun suggerimento |
| DOGE    | Global confluence | 60g         |           0 | n/a        | n/a            | n/a              | n/a              | RACCOLTA DATI | 0,00         | nessun suggerimento |
| DOGE    | Market regime     | 60g         |           0 | n/a        | n/a            | n/a              | n/a              | RACCOLTA DATI | 0,00         | nessun suggerimento |
| DOGE    | Scanner           | 60g         |           0 | n/a        | n/a            | n/a              | n/a              | RACCOLTA DATI | 0,00         | nessun suggerimento |
| DOGE    | Tecnico           | 60g         |           0 | n/a        | n/a            | n/a              | n/a              | RACCOLTA DATI | 0,00         | nessun suggerimento |

## Pesi / score attuali letti dal Global Confluence

Questa tabella mostra gli score attuali. La calibrazione qui sotto non li modifica ancora.

| Asset   | Modulo        | Score attuale   |
|:--------|:--------------|:----------------|
| BTC     | Daily change  | +1,00           |
| BTC     | Fractal path  | 0,00            |
| BTC     | Frattale SOL  | 0,00            |
| BTC     | Futures       | 0,00            |
| BTC     | Lifecycle EMA | 0,00            |
| BTC     | Market regime | +3,00           |
| BTC     | RSI top-cycle | 0,00            |
| BTC     | Scanner       | +3,00           |
| BTC     | Scanner path  | 0,00            |
| SOL     | Daily change  | 0,00            |
| SOL     | Fractal path  | 0,00            |
| SOL     | Frattale SOL  | +2,00           |
| SOL     | Futures       | 0,00            |
| SOL     | Lifecycle EMA | +1,00           |
| SOL     | Market regime | +2,00           |
| SOL     | RSI top-cycle | +1,00           |
| SOL     | Scanner       | -1,00           |
| SOL     | Scanner path  | 0,00            |
| DOGE    | Daily change  | 0,00            |
| DOGE    | Fractal path  | 0,00            |
| DOGE    | Frattale SOL  | 0,00            |
| DOGE    | Futures       | 0,00            |
| DOGE    | Lifecycle EMA | 0,00            |
| DOGE    | Market regime | -3,00           |
| DOGE    | RSI top-cycle | 0,00            |
| DOGE    | Scanner       | -3,00           |
| DOGE    | Scanner path  | 0,00            |

## Lettura operativa

- Stato attuale: **RACCOLTA DATI**.
- Nessun modulo ha ancora abbastanza controlli per suggerire modifiche ai pesi.
- Il Global Confluence deve continuare a usare i pesi attuali.

## Regola anti-autoinganno

- Non aumentare il peso di un modulo solo perché ha funzionato per pochi giorni.
- Non ridurre il peso di un modulo solo per una piccola serie negativa.
- La modifica dei pesi deve partire solo quando ci sono abbastanza controlli e quando 30g e 60g non si contraddicono troppo.
- Questo report serve a evitare che il modello si auto-saboti con pochi dati.

