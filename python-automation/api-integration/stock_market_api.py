#!/usr/bin/env python3
"""
Stock Market Data Integration
Fetch stock market data using Alpha Vantage API.

API: https://www.alphavantage.co/

Dependencies:
    pip install requests

Setup:
    1. Get free API key from: https://www.alphavantage.co/
    2. Replace api_key value with your actual key
"""

import requests

# Alpha Vantage API configuration
API_KEY = "6E20FIQCCZXTA1TU"  # Replace with your actual API key
API_URL = "https://www.alphavantage.co/"

def get_stock_market_data():
    """
    Fetch and display stock market data for a given symbol.
    """
    try:
        symbol = input("Enter the stock symbol (e.g., GOOGL, MSFT, AAPL): ").upper()
        
        if not symbol:
            print("Error: Stock symbol cannot be empty")
            return
        
        # Build query string
        query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
        full_url = API_URL + query
        
        print(f"\nFetching data for {symbol}...\n")
        
        # Make API request
        response = requests.get(full_url)
        response.raise_for_status()  # Raise exception for bad status codes
        
        data = response.json()
        
        # Check for API errors
        if "Error Message" in data:
            print(f"Error: {data['Error Message']}")
            return
        
        if "Note" in data:
            print(f"API Limit: {data['Note']}")
            return
        
        # Display metadata
        if "Meta Data" in data:
            print("=" * 50)
            print("Stock Information:")
            for key, value in data["Meta Data"].items():
                print(f"  {key}: {value}")
            print("=" * 50)
        
        # Display time series data (limited to first 5 entries)
        print("\nLatest Stock Prices (First 5):")
        count = 0
        for date, values in data.get("Time Series (Daily)", {}).items():
            if count >= 5:
                break
            print(f"\n  Date: {date}")
            for key, value in values.items():
                print(f"    {key}: {value}")
            count += 1
    
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to fetch data - {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    get_stock_market_data()
