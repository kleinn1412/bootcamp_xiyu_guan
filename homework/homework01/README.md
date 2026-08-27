# Interest Rates and U.S. Stock Market Risk

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement

Long-term individual investors often see news about Federal Reserve interest-rate changes, rising market volatility, or changes in the S&P 500, but may not understand how these indicators have historically moved together. This project will examine the historical relationship among the effective federal funds rate, the VIX volatility index, and the S&P 500.

The project will provide a monthly market-risk summary helps investors understand the current interest-rate and market-volatility environment.

## Stakeholder & User

The primary stakeholder is a long-term individual investor who is responsible for decisions about their own investment portfolio. The user is the investor, or potentially a financial advisor helping that investor understand current market conditions.


## Useful Answer & Decision

This project is primarily descriptive, with a possible simple predictive component in later stages. It will show historical trends and relationships among the effective federal funds rate, VIX, and S&P 500 returns.

The deliverable will be a monthly risk-context summary with charts and plain-language risk notes. It does not recommend buying or selling a specific security.

## Assumptions & Constraints

- The Federal Funds Effective Rate, VIX, and S&P 500 are useful but incomplete indicators of market conditions.
- Historical relationships may not continue in the future.

## Known Unknowns / Risks

- Interest rates, VIX, and the S&P 500 may move together without one directly causing another.
- Inflation, earnings, geopolitical events, and other factors can affect the market but may not be included in the model.

## Lifecycle Mapping

Goal → Stage → Deliverable

## Repo Plan

- `data/`: raw and processed public data
- `src/`: reusable data-cleaning and analysis functions
- `notebooks/`: numbered analysis notebooks
- `docs/`: stakeholder memo, notes, and project documentation
- `README.md`: project scope, lifecycle mapping, and workflow summary