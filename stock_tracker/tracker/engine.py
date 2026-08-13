"""
This module contains the core logic for the Stock Portfolio Tracker.
"""
from .data import get_price

class PortfolioTracker:
    def __init__(self):
        self.portfolio = {}
        self.total_value = 0.0

    def add_stock(self, symbol, quantity):
        """Adds a stock to the portfolio and calculates its value."""
        price = get_price(symbol)
        if price is None:
            return False, f"Stock symbol '{symbol}' not found in our database."
        
        if symbol.upper() in self.portfolio:
            self.portfolio[symbol.upper()]["quantity"] += quantity
        else:
            self.portfolio[symbol.upper()] = {
                "quantity": quantity,
                "price": price
            }
        
        self._calculate_totals()
        return True, f"Successfully added {quantity} shares of {symbol.upper()}."

    def _calculate_totals(self):
        """Calculates subtotals for each stock and the overall total value."""
        self.total_value = 0.0
        for symbol, data in self.portfolio.items():
            subtotal = data["quantity"] * data["price"]
            self.portfolio[symbol]["subtotal"] = subtotal
            self.total_value += subtotal

    def get_summary(self):
        """Returns the current portfolio and total value."""
        return self.portfolio, self.total_value
