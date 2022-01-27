"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def check_play_again():
    while True:
        play_again = input('Do you want to play again? (Yes/No) ')

        if play_again.lower() == 'yes':
            return True
        elif play_again.lower() == 'no':
            return False
        else:
            print('Invalid response. Please say "yes" or "no".')

def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    """
    print('Welcome to the number guessing game!\nBy Renee Louise Brinkman')

    playing = True
    while playing:


        """2. Store a random number as the answer/solution."""
        answer = random.randint(1, 10)

        """3. Continuously prompt the player for a guess."""
        guess_correct = False
        attempts = 0
        while not guess_correct:
            try:
                guess = int(input('Try guessing a number between 1 and 10! '))
            except ValueError:
                print('You did not enter a valid number between 1 and 10. Please try again.')
                continue

            if guess < 1 or guess > 10:
                print('Your number is out of range. It must be between 1 and 10. Please try again.')
                continue

            """a. If the guess greater than the solution, display to the player "It's lower".
            b. If the guess is less than the solution, display to the player "It's higher".
            """
            if guess > answer:
                print("It's lower than that")
            elif guess < answer:
                print("It's higher than that")

            else:
                guess_correct = True

            attempts += 1

        """4. Once the guess is correct, stop looping, inform the user they "Got it"
             and show how many attempts it took them to get the correct number."""
        print(f'Yes! You got it! It took you {attempts} tries to guess correctly.')

        playing = check_play_again()

    """5. Let the player know the game is ending, or something that indicates the game is over."""
    print('The game is over. Thanks for playing!')

    """( You can add more features/enhancements if you'd like to. )
    """



# Kick off the program by calling the start_game function.
start_game()
