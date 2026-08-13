Stock Portfolio Tracker

Project Overview

This project implements a simple command-line stock portfolio tracker in Python. It allows users to input stock names and quantities, calculates the total investment value based on hardcoded stock prices, and can optionally save the summary to a .txt or .csv file. The goal is to demonstrate a professional, modular Python application with clear separation of concerns.

Features

•
User Input: Easily add multiple stocks and their quantities to the portfolio.

•
Hardcoded Prices: Uses a predefined dictionary for stock prices, meeting the simplified scope requirement.

•
Total Investment Calculation: Automatically calculates and displays the total value of the portfolio.

•
File Export: Option to save the portfolio summary to a .txt or .csv file for record-keeping.

•
Modular Design: Structured into distinct modules for data, core logic, and file handling.

Project Structure

The project follows a clean and logical directory structure:

Plain Text


stock_tracker/
├── tracker/
│   ├── __init__.py
│   ├── data.py
│   ├── engine.py
│   └── exporter.py
├──main.py
├── README.md
└── test_tracker.py



•
stock_tracker/: The root directory of the project.

•
tracker/: A Python package containing the core components.

•
__init__.py: Marks the directory as a Python package.

•
data.py: Stores the hardcoded STOCK_PRICES dictionary and provides a get_price function.

•
engine.py: Contains the PortfolioTracker class, which manages adding stocks, calculating values, and maintaining the portfolio state.

•
exporter.py: Provides functions (save_to_txt, save_to_csv) to export the portfolio summary to different file formats.



•
main.py: The main entry point of the application, handling user interaction, displaying available stocks, and orchestrating the portfolio tracking process.

•
README.md: This documentation file.

•
test_tracker.py: A script containing basic unit tests for the PortfolioTracker logic.

How to Run the Application

1.
Navigate to the project directory:

Bash


cd stock_tracker





2.
Run the main script:

Bash


python3 main.py



Follow the on-screen prompts to add stocks to your portfolio. After you are done, you will have the option to save the summary.



Design Choices and Professionalism

•
Modularity: The application is divided into data, engine, and exporter modules. This separation of concerns makes the codebase easy to understand, maintain, and extend.

•
Object-Oriented Programming (OOP): The PortfolioTracker class encapsulates the portfolio's state and behavior, promoting a robust and scalable design.

•
Clear Input/Output: The main.py script provides a user-friendly command-line interface with clear instructions and formatted output.

•
Data Handling: Stock prices are managed in a dedicated data.py module, making it easy to update or expand the list of available stocks.

•
File Handling: The exporter.py module demonstrates how to save data to both .txt and .csv formats, showcasing basic file I/O operations.

•
Error Handling: Basic input validation is implemented to ensure correct quantity input, and messages are provided for invalid stock symbols.

•
Code Comments and Docstrings: Comprehensive docstrings and comments are used throughout the code to explain functionality, arguments, and return values.

•
Testing: A test_tracker.py script is included to verify the core logic of adding stocks and calculating totals, reflecting good development practices.

Requirements

•
Python 3.x

Future Enhancements

•
Dynamic Stock Prices: Integrate with a real-time stock API to fetch live prices.

•
Portfolio Management: Add functionality to remove stocks, update quantities, or track profit/loss.

•
Graphical User Interface (GUI): Develop a GUI using libraries like Tkinter, PyQt, or Streamlit.

•
Database Integration: Store portfolio data in a database instead of relying on file exports.

•
More Reporting Options: Generate more detailed reports or visualizations of portfolio performance.

