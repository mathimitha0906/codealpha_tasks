"""
This module contains the core engine for the rule-based chatbot.
"""
from .knowledge import get_response

class ChatbotEngine:
    def __init__(self, name="PythonBot"):
        self.name = name
        self.is_active = True

    def process_input(self, user_input):
        """Processes the user input and returns the bot's response."""
        if not user_input.strip():
            return "I can't hear you! Please say something."
            
        # Check for exit commands
        exit_commands = ["exit", "quit", "bye", "goodbye"]
        if any(cmd == user_input.lower().strip() for cmd in exit_commands):
            self.is_active = False
            return get_response("bye")
            
        return get_response(user_input)

    def start_chat(self):
        """Starts the interactive chat loop."""
        print(f"{self.name}: Hello! I'm {self.name}. Type 'quit' or 'exit' to leave.")
        
        while self.is_active:
            try:
                user_input = input("You: ")
                response = self.process_input(user_input)
                print(f"{self.name}: {response}")
            except (KeyboardInterrupt, EOFError):
                print(f"\n{self.name}: {self.process_input('bye')}")
                self.is_active = False

