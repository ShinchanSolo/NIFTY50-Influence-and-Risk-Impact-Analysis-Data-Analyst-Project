import yfinance as yf
import pandas as pd
from datetime import datetime
import os

def fetch_stock_data(ticker, period="10y", interval="1d", prefix="raw", save_dir="data"):
    """
    Fetch stock/index data from Yahoo Finance and save it as CSV.

    Parameters:
        ticker (str): Yahoo Finance ticker symbol (e.g., 'TCS.NS', '^NSEI')
        period (str): Data period (default "10y") e.g., "1y", "6mo", "max"
        interval (str): Data interval (default "1d") e.g., "1d", "1h", "5m"
        prefix (str): File prefix (default "raw")
        save_dir (str): Directory where CSVs will be saved

    Returns:
        pd.DataFrame: Stock data
    """
    os.makedirs(save_dir, exist_ok=True) 
    data = yf.download(ticker, period=period, interval=interval)

    if data.empty:
        print(f"No data fetched for ticker {ticker}")
        return pd.DataFrame()

    data.reset_index(inplace=True)
    file_name = f"{prefix}_{ticker.replace('^', '').replace('.', '-')}_{datetime.today().date()}.csv"
    file_path = os.path.join(save_dir, file_name)
    data.to_csv(file_path, index=False)
    print(f"Data saved: {file_path}")
    return data


if __name__ == "__main__":
    # Full list of Nifty50 stock tickers (Yahoo Finance format)
    nifty50_symbols = [
        "RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS",
        "HINDUNILVR.NS", "KOTAKBANK.NS", "ITC.NS", "LT.NS", "SBIN.NS",
        "AXISBANK.NS", "BAJFINANCE.NS", "BHARTIARTL.NS", "ASIANPAINT.NS", "MARUTI.NS",
        "SUNPHARMA.NS", "WIPRO.NS", "ULTRACEMCO.NS", "TITAN.NS", "HCLTECH.NS",
        "BAJAJFINSV.NS", "NTPC.NS", "ONGC.NS", "POWERGRID.NS", "JSWSTEEL.NS",
        "GRASIM.NS", "ADANIENT.NS", "ADANIPORTS.NS", "TECHM.NS", "NESTLEIND.NS",
        "M&M.NS", "DRREDDY.NS", "CIPLA.NS", "BRITANNIA.NS", "COALINDIA.NS",
        "BPCL.NS", "HEROMOTOCO.NS", "HINDALCO.NS", "INDUSINDBK.NS", "BAJAJ-AUTO.NS",
        "DIVISLAB.NS", "APOLLOHOSP.NS", "EICHERMOT.NS", "SHREECEM.NS", "UPL.NS",
        "TATASTEEL.NS", "SBILIFE.NS", "HDFCLIFE.NS", "IOC.NS", "VEDL.NS"
    ]

    # Add Nifty50 Index itself
    all_symbols = nifty50_symbols + ["^NSEI"]

    # Fetch and save data for each symbol
    for symbol in all_symbols:
        fetch_stock_data(symbol, period="10y", interval="1d", prefix="raw", save_dir="data")
