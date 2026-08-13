"""
This module handles the visual representation of the Hangman game.
"""

HANGMAN_STAGES = [
    # Final state: head, torso, both arms, and both legs
    """
       --------
       |      |
       |      O
       |     /|\\
       |     / \\
       |
    """,
    # 5 mistakes: head, torso, both arms, and one leg
    """
       --------
       |      |
       |      O
       |     /|\\
       |     /
       |
    """,
    # 4 mistakes: head, torso, and both arms
    """
       --------
       |      |
       |      O
       |     /|\\
       |
       |
    """,
    # 3 mistakes: head, torso, and one arm
    """
       --------
       |      |
       |      O
       |     /|
       |
       |
    """,
    # 2 mistakes: head and torso
    """
       --------
       |      |
       |      O
       |      |
       |
       |
    """,
    # 1 mistake: head
    """
       --------
       |      |
       |      O
       |
       |
       |
    """,
    # Initial state: empty gallows
    """
       --------
       |      |
       |
       |
       |
       |
    """
]

def get_hangman_stage(remaining_attempts):
    """
    Returns the visual stage based on remaining attempts.
    """
    return HANGMAN_STAGES[remaining_attempts]

def display_game_status(word_completion, remaining_attempts, guessed_letters, category):
    """
    Prints the current status of the game including the category hint.
    """
    print(get_hangman_stage(remaining_attempts))
    print(f"Hint (Category): {category}")
    print(f"Word: {' '.join(word_completion)}")
    print(f"Remaining attempts: {remaining_attempts}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    print("-" * 30)