"""
This module handles exporting portfolio results to files.
"""
import csv

def save_to_txt(portfolio, total_value, filename="portfolio_summary.txt"):
    """Saves the portfolio summary to a text file."""
    try:
        with open(filename, "w") as f:
            f.write("Stock Portfolio Summary\n")
            f.write("=" * 25 + "\n")
            for symbol, data in portfolio.items():
                f.write(f"{symbol}: {data['quantity']} shares @ ${data['price']:.2f} = ${data['subtotal']:.2f}\n")
            f.write("-" * 25 + "\n")
            f.write(f"Total Investment Value: ${total_value:.2f}\n")
        return True
    except Exception as e:
        print(f"Error saving to TXT: {e}")
        return False

def save_to_csv(portfolio, total_value, filename="portfolio_summary.csv"):
    """Saves the portfolio summary to a CSV file."""
    try:
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Symbol", "Quantity", "Price", "Subtotal"])
            for symbol, data in portfolio.items():
                writer.writerow([symbol, data["quantity"], f"{data['price']:.2f}", f"{data['subtotal']:.2f}"])
            writer.writerow([])
            writer.writerow(["Total Value", "", "", f"{total_value:.2f}"])
        return True
    except Exception as e:
        print(f"Error saving to CSV: {e}")
        return False