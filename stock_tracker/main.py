"""
Main entry point for the Stock Portfolio Tracker.
"""
from tracker.engine import PortfolioTracker
from tracker.exporter import save_to_txt, save_to_csv
from tracker.data import STOCK_PRICES

def display_available_stocks():
    print("\nAvailable Stocks and Prices:")
    print("-" * 30)
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol}: ${price:.2f}")
    print("-" * 30)

def main():
    tracker = PortfolioTracker()
    print("Welcome to the Professional Stock Portfolio Tracker!")
    
    display_available_stocks()

    while True:
        symbol = input("\nEnter stock symbol (or 'done' to finish): ").strip().upper()
        if symbol == 'DONE':
            break
        
        try:
            quantity = float(input(f"Enter quantity for {symbol}: "))
            if quantity <= 0:
                print("Quantity must be positive.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number for quantity.")
            continue

        success, message = tracker.add_stock(symbol, quantity)
        print(message)

    portfolio, total_value = tracker.get_summary()
    
    if not portfolio:
        print("\nPortfolio is empty. Goodbye!")
        return

    print("\n" + "=" * 40)
    print("FINAL PORTFOLIO SUMMARY")
    print("=" * 40)
    for symbol, data in portfolio.items():
        print(f"{symbol:6} | {data['quantity']:8.2f} shares | Subtotal: ${data['subtotal']:10.2f}")
    print("-" * 40)
    print(f"TOTAL INVESTMENT VALUE: ${total_value:10.2f}")
    print("=" * 40)

    save_choice = input("\nWould you like to save this summary? (txt/csv/both/none): ").lower()
    if save_choice in ['txt', 'both']:
        if save_to_txt(portfolio, total_value):
            print("Successfully saved to portfolio_summary.txt")
    if save_choice in ['csv', 'both']:
        if save_to_csv(portfolio, total_value):
            print("Successfully saved to portfolio_summary.csv")

    print("\nThank you for using the Stock Portfolio Tracker!")

if __name__ == "__main__":
    main()
