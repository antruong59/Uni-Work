#
#  PSP Assignment 2 - Provided file (part2_truan004.py).
#  Remove this and place appropriate file comments here.
#
#  Modify this file to include your code solution.
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

def display_characters(character_list, health_list):
    # This line will eventually be removed - used for development purposes only.
    # print("In function display_characters()")

    # Place your code here
    print('=' * 36)
    print('-{:^34}-'.format('Character Summary'))
    print('=' * 36)
    print('-  {:<15}'.format('Name'), '{:>14}  -'.format('Health'))
    print('-' * 36)
    index = 0
    while index < len(character_list):
        character = character_list[index]
        health = health_list[index]
        print('-  {:<15}'.format(character), '{:>14}  -'.format(health))
        print('-' * 36)
        index += 1
    print('=' * 36)


# Function write_to_file() - place your own comments here...  : )

def write_to_file(filename, character_list, health_list):
    # This line will eventually be removed - used for development purposes only.
    # print("In function write_to_file()")

    # Place your code here

    outfile = open(filename, 'w')

    for character in character_list:
        outfile.write(character)
        outfile.write('\n')
        outfile.write(str(health_list[list_function.find(character_list, character)]))
        outfile.write('\n')

    outfile.close()


# Function do_battle() - place your own comments here...  : )
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
    battle_no = input('Please enter number of battle rounds: ')

    # Validate user's input
    while battle_no != '1' and battle_no != '2' and battle_no != '3' and battle_no != '4' and battle_no != '5':
        print('Must be between 1-5 inclusive.')
        battle_no = input('Please enter number of battle rounds: ')

    print('-- Battle --')

    # Confirm user's choices
    if battle_no == '1':
        print(choose_1, 'versus', choose_2, '-', battle_no, 'round')
    else:
        print(choose_1, 'versus', choose_2, '-', battle_no, 'rounds')

    # Variables to randomly damage 2 opponents
    damage_1 = random.randint(0, 50)
    damage_2 = random.randint(0, 50)

    # Players current health
    current_health1 = health_list[opponent1_pos]
    current_health2 = health_list[opponent2_pos]

    # Variable to count each round
    round_no = 1

    # Loop to display battle rounds
    while 0 < round_no <= int(battle_no) and current_health1 > 0 and current_health2 > 0:

        # if current_health1 <= 0:
        #     current_health1 = 0
        #     if current_health2 <= 0:
        #         current_health2 = 0
        #     print('Round:', round_no)
        #     print('>', choose_1, '- Damage:', damage_1, '- Current health:', current_health1)
        #     print('>', choose_2, '- Damage:', damage_2, '- Current health:', current_health2)
        #
        #     # Assign variable to get out of loop
        #     round_no = -2
        #
        # elif current_health2 <= 0:
        #     current_health2 = 0
        #     if current_health1 <= 0:
        #         current_health1 = 0
        #     print('Round:', round_no)
        #     print('>', choose_1, '- Damage:', damage_1, '- Current health:', current_health1)
        #     print('>', choose_2, '- Damage:', damage_2, '- Current health:', current_health2)
        #
        #     # Assign variable to get out of loop
        #     round_no = -2

        # elif current_health1 > 0 and current_health2 > 0:
        damage_1 = random.randint(0, 50)
        damage_2 = random.randint(0, 50)
        current_health1 -= damage_1
        current_health2 -= damage_2

        if current_health1 <= 0:
            current_health1 = 0
        if current_health2 <= 0:
            current_health2 = 0
        print('Round:', round_no)
        print('>', choose_1, '- Damage:', damage_1, '- Current health:', current_health1)
        print('>', choose_2, '- Damage:', damage_2, '- Current health:', current_health2)

        round_no += 1

    health_list[opponent1_pos] = current_health1
    health_list[opponent2_pos] = current_health2

    print('-- End of battle --')
    winner = choose_1
    if current_health2 > current_health1:
        winner = choose_2
    elif current_health2 == current_health1:
        print('Draw!')

    print('**', winner, 'wins!', '**')


### Place your code here...  : )

start = input('Please enter choice \n[list, search, reset, add, remove, battle, quit]: ')

read_file('characters.txt', character_list, health_list)
write_to_file('new_characters.txt', character_list, health_list)

while start != 'quit':
    while start != 'list' and start != 'search' and start != 'reset' and start != 'add' and start != 'remove' and start != 'battle' and start != 'quit':
        print('Not a valid command - please try again.')
        start = input('Please enter choice \n[list, search, reset, add, remove, battle, quit]: ')

    character_list = []
    health_list = []

    read_file('new_characters.txt', character_list, health_list)
    # read_file('characters.txt', character_list, health_list)

    if start == 'list':
        display_characters(character_list, health_list)
        start = input('Please enter choice \n[list, search, reset, add, remove, battle, quit]: ')

    elif start == 'search':
        search = input('Please enter name: ')
        if search not in character_list:
            print(search, 'is not found in character list.')

        else:
            print(search, '\'s current health: ', health_list[list_function.find(character_list, search)], '%')

        start = input('Please enter choice \n[list, search, reset, add, remove, battle, quit]: ')

    elif start == 'reset':
        name = input('Please enter name: ')
        if name in character_list:
            health_list[list_function.find(character_list, name)] = 100
            write_to_file('new_characters.txt', character_list, health_list)
            print('Successfully updated', name, '\'s health to 100')

        else:
            print(name, 'is not found in character list.')

        start = input('Please enter choice \n[list, search, reset, add, remove, battle, quit]: ')
    elif start == 'add':
        add_name = input('Please enter name: ')
        if add_name in character_list:
            print(add_name, 'already exists in character list.')

        else:
            character_list.append(add_name)
            health_list.append(100)
            write_to_file('new_characters.txt', character_list, health_list)
            print('Successfully added', add_name)

        start = input('Please enter choice \n[list, search, reset, add, remove, battle, quit]: ')
    elif start == 'remove':
        remove_name = input('Please enter name: ')
        if remove_name not in character_list:
            print(remove_name, 'is not found in character list.')

        else:
            position = list_function.find(character_list, remove_name)
            character_list = list_function.remove_value(character_list, position)
            health_list = list_function.remove_value(health_list, position)
            write_to_file('new_characters.txt', character_list, health_list)
            print('Successfully removed', remove_name)

        start = input('Please enter choice \n[list, search, reset, add, remove, battle, quit]: ')
    elif start == 'battle':
        choose_1 = input('Please enter opponent one\'s name: ')
        while choose_1 not in character_list:
            print(choose_1, 'is not found in character list - please enter another opponent!')
            choose_1 = input('Please enter opponent one\'s name: ')
        choose_2 = input('Please enter opponent two\'s name: ')
        while choose_2 not in character_list:
            print(choose_2, 'is not found in character list - please enter another opponent!')
            choose_2 = input('Please enter opponent two\'s name: ')
        do_battle(character_list, health_list, list_function.find(character_list, choose_1),
                  list_function.find(character_list, choose_2))
        write_to_file('new_characters.txt', character_list, health_list)
        start = input('Please enter choice \n[list, search, reset, add, remove, battle, quit]: ')

print("\n\n-- Program terminating --\n")


