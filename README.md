# Crypto Price Tracker (Python)

A Python script that automatically collects live market data for the 10 largest cryptocurrencies from the CoinMarketCap API, saves each run to a CSV file to build up a price history, and compares how each coin's price has changed over the last hour, day and week.

## What it does
1. **Collects the data:** calls the CoinMarketCap `listings/latest` endpoint for the top 10 coins by market cap, priced in USD.
2. **Cleans and stores it:** flattens the nested JSON response into a table with `pandas.json_normalize`, adds a timestamp and appends each run to `CoinPriceHistory.csv`. The file is created with headers on the first run.
3. **Automates the runs:** a loop calls the API repeatedly and pauses between calls, so the history grows over time without manual work.
4. **Analyses the history:** averages the 1-hour, 24-hour and 7-day percentage price change for each coin and reshapes the result (`groupby`, `stack`, `reset_index`) into `CoinPriceHistoryNEW.csv`.
5. **Visualises the result:** plots the average changes for every coin side by side with Seaborn, so it's easy to see which coins are rising or falling.

## Example result
From the sample data in this repository (collected on 28 April 2024):
- **Ethereum and BNB were the strongest**, both up about 5% over 7 days.
- **Toncoin fell the most**, down about 11% over 7 days, after rising about 4% in the previous 24 hours.
- **Stablecoins (Tether USDt and USDC) stayed flat**, as expected, which is a useful check that the data is correct.

## How to run
1. Get a free API key from [coinmarketcap.com/api](https://coinmarketcap.com/api/).
2. Save it as an environment variable called `CMC_API_KEY`. The key is read from the environment so it never appears in the code.
3. Install the libraries: `pip install requests pandas seaborn matplotlib`
4. Update the CSV file paths in `Code.py` to a folder on your computer. They currently point to a local Windows folder.
5. Run `Code.py`. It was developed as a Jupyter notebook, so it also works well cell by cell.

## Files
| File | Description |
|---|---|
| `Code.py` | API call, data storage, automation, analysis and plotting |
| `CoinPriceHistory.csv` | Sample raw history collected from the API (10 coins × several runs) |
| `CoinPriceHistoryNEW.csv` | Average percentage changes per coin, used for the chart |

## Tools
Python, requests, pandas, Seaborn, Matplotlib, CoinMarketCap API
