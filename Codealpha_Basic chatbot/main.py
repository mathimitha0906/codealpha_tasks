"""
Main entry point for the Basic Chatbot project.
"""
from bot.engine import ChatbotEngine

def main():
    try:
        # Initialize and start the chatbot
        bot = ChatbotEngine()
        bot.start_chat()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
