"""
This module contains the core game logic for Hangman with hint support.
"""
import random
from .words import WORD_DATA
from .display import display_game_status

class HangmanGame:
    def __init__(self, max_attempts=6):
        selected_entry = random.choice(WORD_DATA)
        self.word = selected_entry["word"].upper()
        self.category = selected_entry["category"]
        self.word_completion = ["_"] * len(self.word)
        self.guessed_letters = set()
        self.remaining_attempts = max_attempts
        self.is_game_over = False

    def play(self):
        print("Welcome to Hangman!")
        print(f"I've picked a word for you from the category: {self.category}")
        
        while not self.is_game_over:
            display_game_status(
                self.word_completion, 
                self.remaining_attempts, 
                self.guessed_letters,
                self.category
            )
            
            guess = input("Please guess a letter: ").upper()
            
            if self._validate_input(guess):
                self._process_guess(guess)
                self._check_game_state()

    def _validate_input(self, guess):
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            return False
        if guess in self.guessed_letters:
            print(f"You already guessed the letter '{guess}'. Try again.")
            return False
        return True

    def _process_guess(self, guess):
        self.guessed_letters.add(guess)
        
        if guess in self.word:
            print(f"Good job! '{guess}' is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_completion[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            self.remaining_attempts -= 1

    def _check_game_state(self):
        if "_" not in self.word_completion:
            display_game_status(
                self.word_completion, 
                self.remaining_attempts, 
                self.guessed_letters,
                self.category
            )
            print("Congratulations! You won!")
            self.is_game_over = True
        elif self.remaining_attempts <= 0:
            display_game_status(
                self.word_completion, 
                self.remaining_attempts, 
                self.guessed_letters,
                self.category
            )
            print(f"Game Over! You ran out of attempts. The word was: {self.word}")
            self.is_game_over = True