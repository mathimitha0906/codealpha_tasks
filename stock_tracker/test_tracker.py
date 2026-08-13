"""
Test script for the Stock Portfolio Tracker.
"""
from tracker.engine import PortfolioTracker

def test_add_stock():
    tracker = PortfolioTracker()
    # Test adding a valid stock
    success, msg = tracker.add_stock("AAPL", 10)
    assert success is True
    assert tracker.total_value == 180.50 * 10
    
    # Test adding another valid stock
    success, msg = tracker.add_stock("TSLA", 5)
    assert success is True
    expected_total = (180.50 * 10) + (250.75 * 5)
    assert tracker.total_value == expected_total
    
    # Test invalid stock
    success, msg = tracker.add_stock("INVALID", 1)
    assert success is False
    print("All logic tests passed!")

if __name__ == "__main__":
    test_add_stock()
