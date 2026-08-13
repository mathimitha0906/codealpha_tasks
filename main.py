"""
Main entry point for the Hangman Game.
"""
from hangman.engine import HangmanGame

def main():
    try:
        game = HangmanGame()
        game.play()
    except KeyboardInterrupt:
        print("\nGame exited. Goodbye!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
