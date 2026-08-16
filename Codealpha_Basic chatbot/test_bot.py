"""
Test script for the Chatbot engine.
"""
from bot.engine import ChatbotEngine

def test_bot_responses():
    bot = ChatbotEngine()
    
    # Test greeting
    response = bot.process_input("hello")
    assert any(greeting in response for greeting in ["Hi", "Hello", "Greetings", "Hey"])
    
    # Test specific keyword
    response = bot.process_input("tell me a joke")
    assert "programmer" in response.lower() or "joke" in response.lower()
    
    # Test default response
    response = bot.process_input("xyzabc123")
    assert "not sure I understand" in response
    
    # Test exit
    response = bot.process_input("quit")
    assert bot.is_active is False
    
    print("All chatbot logic tests passed!")

if __name__ == "__main__":
    test_bot_responses()