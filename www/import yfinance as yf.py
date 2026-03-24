import yfinance as yf
import pandas as pd

# List of stocks you are interested in (e.g., Apple, Tesla, Nvidia)
watch_list = ["AAPL", "TSLA", "NVDA", "AMD", "MSFT"]

def check_opportunity(ticker_symbol):
    # 1. Fetch the last 30 days of stock data
    data = yf.download(ticker_symbol, period="1mo", interval="1d", progress=False)
    
    if data.empty:
        return

    # 2. Calculate a simple 14-day RSI (Relative Strength Index)
    # RSI < 30 means "Oversold" (potential time to sell a Put)
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs)).iloc[-1]

    # 3. Decision Logic
    current_price = data['Close'].iloc[-1]
    
    print(f"Checking {ticker_symbol:5} | Price: ${current_price:>7.2f} | RSI: {rsi:>5.2f}")

    if rsi < 35:
        print(f"  >>> ALERT: {ticker_symbol} is oversold! Good time to check Put options.")
    elif rsi > 65:
        print(f"  >>> ALERT: {ticker_symbol} is overbought! Good time to check Call options.")

# Run the bot
print("--- Starting Market Scanner ---")
for stock in watch_list:
    check_opportunity(stock)
print("--- Scan Complete ---")