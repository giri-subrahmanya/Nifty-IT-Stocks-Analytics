import yfinance as yf

# From March 1, 2023 to June 15, 2025
start_date = '2023-03-01'
end_date = '2025-06-16'

# tickers
tickers = {
    'hcl': 'HCLTECH.NS',
    'infosys': 'INFY.NS',
    'tcs': 'TCS.NS',
    'techM': 'TECHM.NS',
    'wipro': 'WIPRO.NS',
    'nifty_it': '^CNXIT',
    'nifty_50': '^NSEI',
}

# collection
symbols = list(tickers.values())
df = yf.download(
    symbols, 
    start=start_date, 
    end=end_date, 
    auto_adjust=False,
    group_by='ticker'
)

# to_csv() loop
for t in tickers:
    df[tickers[t]].to_csv(f'datasets/{t}.csv')