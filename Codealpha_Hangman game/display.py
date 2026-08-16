"""
This module handles the visual representation of the Hangman game.
"""

HANGMAN_STAGES = [
    # 0 mistakes: base scaffolding only
    """
       --------

       |      |
       |      
       |     
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
    # 2 mistakes: head and torso
    """
       --------

       |      |
       |      O

       |      |
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
    # 4 mistakes: head, torso, and both arms
    """
       --------

       |      |
       |      O

       |     /|\\
       |     
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
    # 6 mistakes: final state (dead man)
    """
       --------

       |      |
       |      O

       |     /|\\
       |     / \\
       |
    """
]

def display_game_status(word_completion, remaining_attempts, guessed_letters, category):
    # Calculate index based on mistakes made
    mistakes = 6 - remaining_attempts
    print(HANGMAN_STAGES[mistakes])
    print(f"Category: {category}")
    print("Word: " + " ".join(word_completion))
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    print(f"Attempts left: {remaining_attempts}")
    print("-" * 30)
