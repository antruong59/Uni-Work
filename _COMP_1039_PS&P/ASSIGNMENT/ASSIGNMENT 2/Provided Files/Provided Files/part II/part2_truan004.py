#
# PSP Assignment 2 - Provided file (part2_truan004.py).
# Remove this and place appropriate file comments here.
# File      : part2_truan004.py
# Author    : Ngoc An Truong
# Email Id  : truan004@mymail.unisa.edu.au
# Description: Assignment 2 - Manage character (hero and villain) information
#                           - This Python codes will manage character (heroes and villain) information.
#                           - There are 4 main functions which will be called in the interaction mode:
#                               + read_file(filename, character_list, health_list)
#                               + display_characters(character_list, health_list)
#                               + write_to_file(filename, character_list, health_list)
#                               + do_battle(character_list, health_list, opponent1_pos, opponent2_pos)
#                           - In interaction mode, this Python module will enable user to check for characters
#                           information and create a battle with user's chosen opponents.
#                           - At the end, there will be a text file recording the change of user's choices based on list
# This is my own work as defined by the University's
# Academic Misconduct policy.
# Modify this file to include your code solution.
#
#
# Write your code and function definitions in this file.
# Place your own comments in this file also.
#

import random
import list_function

# Define the character list to store characters
character_list = []

# Define the health list to store health values
health_list = []


# Function read_file() - place your own comments here...  : )
# Function to read the given file and store the information in character list and health list

def read_file(filename, character_list, health_list):
    # Open file for reading.
    infile = open(filename, "r")

    # Read first line of file.
    line = infile.readline()

    # While not end of file reached i.e. empty string not returned from readline method.
    while line != '':
        # Get name - remove new line character
        name = line.strip('\n')

        # Read in next line
        line = infile.readline()

        # Get health - remove new line character and convert to integer
        health = int(line.strip('\n'))

        # Add name to character_list
        character_list.append(name)

        # Add health to health_list
        health_list.append(health)

        # Read next line of file.
        line = infile.readline()

    infile.close()


# Function display_characters() - place your own comments here...  : )
# Function to display and update the list of characters' information

def display_characters(character_list, health_list):
    # This line will eventually be removed - used for development purposes only.
    # print("In function display_characters()")

    # Place your code here
    print('\n')
    print('=' * 36)
    print('-{:^34}-'.format('Character Summary'))
    print('=' * 36)
    print('-  {:<15}'.format('Name'), '{:>14}  -'.format('Health'))
    print('-' * 36)

    # Variable to check for every items in both character list and health list
    index = 0

    while index < len(character_list):
        character = character_list[index]
        health = health_list[index]
        print('-  {:<15}'.format(character), '{:>14}  -'.format(health))
        print('-' * 36)
        index += 1
    print('=' * 36)


# Function write_to_file() - place your own comments here...  : )
# Function to modify characters' information after every changes by user

def write_to_file(filename, character_list, health_list):
    # This line will eventually be removed - used for development purposes only.
    # print("In function write_to_file()")

    # Place your code here

    # Open file for writing
    outfile = open(filename, 'w')

    # Loop to update list of information into new file
    for character in character_list:
        outfile.write(character)
        outfile.write('\n')
        outfile.write(str(health_list[list_function.find(character_list, character)]))
        outfile.write('\n')

    outfile.close()


# Function do_battle() - place your own comments here...  : )
# Function to create a battle between 2 opponents chosen by user
#
# Parameters: character_list - list of characters.
#             health_list    - list of health values.
#             opponent1_pos  - position/index of character in character_list.
#             opponent2_pos  - position/index of character in character_list.

def do_battle(character_list, health_list, opponent1_pos, opponent2_pos):
    # This line will eventually be removed - used for development purposes only.
    # print("In function do_battle()")

    # Refer to algorithm in assignment handout for this function...

    # Place your code here

    # Variable to prompt user for battle number
    battle_no = input('\nPlease enter number of battle rounds: ')

    # Validate user input
    while battle_no != '1' and battle_no != '2' and battle_no != '3' and battle_no != '4' and battle_no != '5':
        print('\nMust be between 1-5 inclusive.\n')
        battle_no = input('\nPlease enter number of battle rounds: ')

    print('\n\n-- Battle --\n')

    # Confirm user choices
    if battle_no == '1':
        print(opponent1, 'versus', opponent2, '-', battle_no, 'round')
    else:
        print(opponent1, 'versus', opponent2, '-', battle_no, 'rounds')

    # Opponents current health
    current_health1 = health_list[opponent1_pos]
    current_health2 = health_list[opponent2_pos]

    # Variable to count each round
    round_no = 1

    # Loop to display battle rounds
    while 0 < round_no <= int(battle_no) and current_health1 > 0 and current_health2 > 0:

        # Variable to randomly create damage during battle
        damage_1 = random.randint(0, 50)
        damage_2 = random.randint(0, 50)

        current_health1 -= damage_1
        current_health2 -= damage_2

        if current_health1 <= 0:
            current_health1 = 0
        if current_health2 <= 0:
            current_health2 = 0

        print('\nRound:', round_no)
        print('  >', opponent1, '- Damage:', damage_1, '- Current health:', current_health1)
        print('  >', opponent2, '- Damage:', damage_2, '- Current health:', current_health2)

        round_no += 1

    # Update current health to health list
    health_list[opponent1_pos] = current_health1
    health_list[opponent2_pos] = current_health2

    print('\n-- End of battle --')

    # Display the final result of the battle
    if current_health2 == current_health1:
        if current_health2 == current_health1 == 0:
            print('\nBoth 2 opponents died!')
        print('\nDraw!')
    else:
        winner = opponent1
        if current_health2 > current_health1:
            winner = opponent2
        if current_health1 == 0:
            print('\n--', opponent1, 'has died!  :(')
        elif current_health2 == 0:
            print('\n--', opponent2, 'has died!  :(')



        print('\n**', winner, 'wins!', '**')


### Place your code here...  : )

# Display information
print('''File      : part2_truan004.py
Author    : Ngoc An Truong
Email Id  : truan004@mymail.unisa.edu.au
This is my own work as defined by the University's
Academic Misconduct policy.\n''')

# Prompt for user choices
start = input('Please enter choice \n[list, search, reset, add, remove, battle, quit]: ')

# Copy information from given file to new file
read_file('characters.txt', character_list, health_list)
write_to_file('new_characters.txt', character_list, health_list)

# while user not quit
while start != 'quit':

    # Validate user input
    if start != 'list' and start != 'search' and start != 'reset' and start != 'add' and start != 'remove' and start != 'battle':
        print('\nNot a valid command - please try again.')
        start = input('\nPlease enter choice \n[list, search, reset, add, remove, battle, quit]: ')

    # Reset character list and health list
    character_list = []
    health_list = []

    # Read new file
    read_file('new_characters.txt', character_list, health_list)

    # List command
    if start == 'list':

        # Check if list is empty
        if character_list == [] or health_list == []:
            print('\nThere\'s no character in list!')

        else:
            display_characters(character_list, health_list)
        start = input('\nPlease enter choice \n[list, search, reset, add, remove, battle, quit]: ')

    # Search command
    elif start == 'search':

        # Check if list is empty
        if character_list == [] or health_list == []:
            print('\nThere\'s no character to choose!')

        else:

            # Prompt for user searching
            search = input('\nPlease enter name: ')

            if list_function.find(character_list, search) == -1:
                print('\n', search, ' is not found in character list.', sep='')

            else:
                print('\n', search, '\'s current health: ', health_list[list_function.find(character_list, search)], '%', sep='')

        start = input('\nPlease enter choice \n[list, search, reset, add, remove, battle, quit]: ')

    # Reset command
    elif start == 'reset':

        # Check if list is empty
        if character_list == [] or health_list == []:
            print('\nThere\'s no character to choose!')

        else:

            # Prompt for user resetting
            name = input('\nPlease enter name: ')

            if list_function.find(character_list, name) != -1:
                health_list[list_function.find(character_list, name)] = 100
                write_to_file('new_characters.txt', character_list, health_list)
                print('\nSuccessfully updated', name, '\'s health to 100')

            else:
                print('\n', name, ' is not found in character list.', sep='')

        start = input('\nPlease enter choice \n[list, search, reset, add, remove, battle, quit]: ')

    # Add command
    elif start == 'add':

        # Prompt for user adding
        add_name = input('\nPlease enter name: ')

        # Check if name is empty
        while add_name == '':
            print('\nPlease re-enter name!')
            add_name = input('\nPlease enter name: ')

        if list_function.find(character_list, add_name) != -1:
            print('\n', add_name, ' already exists in character list.', sep='')

        else:
            character_list.append(add_name)
            health_list.append(100)
            write_to_file('new_characters.txt', character_list, health_list)
            print('\nSuccessfully added', add_name)

        start = input('\nPlease enter choice \n[list, search, reset, add, remove, battle, quit]: ')

    # Remove command
    elif start == 'remove':

        # Check if list is empty
        if character_list == [] or health_list == []:
            print('\nThere\'s no character to choose!')

        else:

            # Prompt for user removing
            remove_name = input('\nPlease enter name: ')

            # Remove all from list
            if remove_name == 'remove all':
                character_list = []
                health_list = []
                write_to_file('new_characters.txt', character_list, health_list)
                print('\nSuccessfully removed all!')

            elif list_function.find(character_list, remove_name) == -1:
                print('\n', remove_name, ' is not found in character list.', sep='')

            else:
                position = list_function.find(character_list, remove_name)
                character_list = list_function.remove_value(character_list, position)
                health_list = list_function.remove_value(health_list, position)
                write_to_file('new_characters.txt', character_list, health_list)
                print('\nSuccessfully removed', remove_name)

        start = input('\nPlease enter choice \n[list, search, reset, add, remove, battle, quit]: ')

    # Battle command
    elif start == 'battle':

        # Check if enough characters with health greater than 0
        new_list = []
        for value in health_list:
            if value != 0:
                new_list.append(value)

        # Check if list is empty
        if character_list == [] and health_list == []:
            print('\nThere\'s no character to choose!')

        # Check if opponent is available to play
        elif list_function.length(character_list) >= 2 and list_function.length(new_list) <= 1:
            print('\nCan\'t do battle!')

        # Check if enough opponents to play
        elif list_function.length(character_list) < 2:
            print('\nNot enough characters to do battle! Please add more characters to play.')

        else:

            # Prompt for opponent 1
            opponent1 = input('\nPlease enter opponent one\'s name: ')
            while list_function.find(character_list, opponent1) == -1 or health_list[list_function.find(character_list, opponent1)] == 0:
                if list_function.find(character_list, opponent1) == -1:
                    print('\n', opponent1, ' is not found in character list - please enter another opponent!', sep='')

                # Check if opponent is available to play
                elif health_list[list_function.find(character_list, opponent1)] == 0:
                    print('\nCan\'t do battle!', opponent1, ' has already died :( Please choose another one!')

                opponent1 = input('\nPlease enter opponent one\'s name: ')

            # Prompt for opponent 2
            opponent2 = input('\nPlease enter opponent two\'s name: ')
            while list_function.find(character_list, opponent2) == -1 or opponent2 == opponent1 or health_list[list_function.find(character_list, opponent2)] == 0:
                if list_function.find(character_list, opponent2) == -1:
                    print('\n', opponent2, ' is not found in character list - please enter another opponent!', sep='')

                # Check if chose same opponent
                elif opponent2 == opponent1:
                    print('\n', opponent1, ' has already been chosen! Please choose another one!', sep='')

                # Check if opponent is available to play
                elif health_list[list_function.find(character_list, opponent2)] == 0:
                    print('\nCan\'t do battle!', opponent2, 'has already died :( Please choose another one!')

                opponent2 = input('\nPlease enter opponent two\'s name: ')

            # Do battle
            do_battle(character_list, health_list, list_function.find(character_list, opponent1), list_function.find(character_list, opponent2))

            # Update information into new file
            write_to_file('new_characters.txt', character_list, health_list)

        start = input('\nPlease enter choice \n[list, search, reset, add, remove, battle, quit]: ')


print("\n\n-- Program terminating --\n")


