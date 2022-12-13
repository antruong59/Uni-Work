
import random

play = 'y'
while play == 'y':
    
    # generate random number 1 - 100 inclusive
    number = random.randint(1,100)

    # prompt for and read user’s guess
    guess = int(input('Please enter your guess: '))
    print('')
    
    # determine whether user guessed correct random number
    while guess == number:
        if guess < number:
            print('Too low - please try again!')
        else:
            print('Too high - please try again!')

        # prompt for and read user’s guess
        guess = int(input('Please enter your guess: '))
        print('')
        
    print('Well done - you guessed it!')
        
    # prompt for and read whether the user would like to play again
    play = input('Would you like to play again (y/n)? ')
    print('')
    

