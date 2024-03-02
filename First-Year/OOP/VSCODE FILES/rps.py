#
# File: rps.py
# COMP 1046 Object Oriented Programming
# Practical 1 - Debugging Exercise
#

import random

# Function to get user's choice
def getUserChoice():
    user = input('Rock(1), Paper(2) or Scissors(3)? ')
    while user not in ['1', '2', '3']:
        print('Invalid input - please enter the number 1, 2 or 3.')
        user = input('Rock(1), Paper(2) or Scissors(3)? ')
    return user
    

# Function to ask if play again
def askPlayAgain():
    ans = input('Play again (y|n)? ')
    while ans not in ['Y', 'y', 'N', 'n']:
        print('Invalid input - please enter the number y/n or Y/N')
        ans = input('Play again (y|n)? ')
    return ans

# Function to play the game
def playGame():    
    play = 'y'
    noGames = 0
    selection = ['Rock', 'Paper', 'Scissors']
    role = ['crushes', 'covers', 'cut']

    # Number codes for rock, paper, scissors
    ROCK = 0
    PAPER = 1
    SCISSORS = 2
    
    # build list of all winning combinations
    winningCombos = [[PAPER, ROCK], [SCISSORS, PAPER], [ROCK, SCISSORS]]

    # Repeat while the user wants to play
    while play == 'y':
        # Prompt for and read user's choice
        user = getUserChoice()
        # Display user's choice as text to the screen
        print('You chose', selection[int(user) - 1])
            
        # Randomly generate computer's choice
        comp = random.randint(1, 3)
        # Display computer's "choice" as text to the screen
        print('Computer chose', selection[comp-1])
            
        # Find a winner.
        # build current combination
        currentCombo = [user, comp]
        if comp == int(user):
            print('Draw - no winner!')
        elif currentCombo in winningCombos:
            print('You win -', selection[int(user)-1], role[int(user)-1], selection[comp-1])
        else:
            print('You lose -', selection[comp-1], role[comp-1], selection[int(user)-1])
            
        noGames = noGames + 1
        play = askPlayAgain()
       
    # Show final results
    if play in ['n', 'N']:
        if noGames == 1:
            print("You played", noGames, "game!")
        else:
            print("You played", noGames, "games!")
        print('Thanks for playing!')

    print()

# Main entry of the program
playGame()
