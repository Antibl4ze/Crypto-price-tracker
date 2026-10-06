# Crypto Price Tracker (Python)

A Python script that pulls live data for the top 10 cryptocurrencies from the CoinMarketCap API, stores it over time and compares price changes.

## What it does
- Calls the CoinMarketCap API and flattens the JSON response with pandas
- Adds a timestamp and appends each run to a CSV file
- Calculates the average 1-hour, 24-hour and 7-day percentage change per coin
- Plots the changes with Seaborn and Matplotlib

## How to run
1. Get a free API key from coinmarketcap.com
2. Set it as an environment variable: `CMC_API_KEY=your_key`
3. Run `Code.py`

## Tools
Python, pandas, requests, Seaborn, Matplotlib
