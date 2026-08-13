"""
This module contains the hardcoded stock price data.
"""

STOCK_PRICES = {
    "AAPL": 180.50,
    "TSLA": 250.75,
    "GOOGL": 140.20,
    "AMZN": 175.10,
    "MSFT": 410.30,
    "NVDA": 720.45,
    "META": 485.15,
    "NFLX": 590.60
}

def get_price(symbol):
    """Returns the price of a stock symbol or None if not found."""
    return STOCK_PRICES.get(symbol.upper())
