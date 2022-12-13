import character
import random
import list_function
# Function read_file() - create a list of character objects:
def read_file(filename):

    # List to store information on heroes and villains
    character_list = []
    
    infile = open(filename, "r")

    index = 0

    # Read first line of file.
    line = infile.readline()

    # While not end of file reached i.e. empty string not returned from readline method.
    while line != '':

        # Get name
        name = line.strip('\n')

        # Read in next line
        line = infile.readline()
        
        # Get secret_identity
        secret_id = line.strip('\n')

        # Read in next line
        line = infile.readline()
        
        # Split line into no battles, no won, no lost, etc.
        info_list = line.split()
        is_hero = info_list[0]
        if is_hero == 'h':
            is_hero = True
        else:
            is_hero = False
        no_battles = int(info_list[1])
        no_won = int(info_list[2])
        no_lost = int(info_list[3])
        no_drawn = int(info_list[4])
        health = int(info_list[5])        
        
        # Create new Character object with character (hero and villain) info
        new_character = character.Character(name, secret_id, is_hero, no_battles, no_won,
                                              no_lost, no_drawn, health)
        
        # Add new character to character_list
        character_list.append(new_character)
        
        # Read next line of file.
        line = infile.readline()
    
    return character_list


# Function display_characters() - print characters and their information to the screen:
def display_characters(character_list, display_type):
    print('='*51)
    print(format('-', '<6s'), end = '')
    print(format('Character (heroes and villains) Summary', '^39s'), end = '')
    print(format('-', '>6s'))
    print('='*51)
    print(format('-', '<3s'), end = '')
    print(format('', '<25s'), end = '')
    print(format('P', '>3s'), end = '')
    print(format('W', '>3s'), end = '')
    print(format('L', '>3s'), end = '')
    print(format('D', '>3s'), end = '')
    print(format('Health', '>8s'), end = '')
    print(format('-', '>3s'))

    if display_type == 0:
        for new_character in character_list:
            print('-'*51)
            print(format('-', '<3s'), end = '')
            print(new_character, end = '')
            print(format('-', '>3s'))
            
    elif display_type == 1:
        for new_character in character_list:
            if new_character.get_is_hero() :
                print('-'*51)
                print(format('-', '<3s'), end = '')
                print(new_character, end = '')
                print(format('-', '>3s'))
    
    else:
        for new_character in character_list:
            if new_character.get_is_hero() == False:
                print('-'*51)
                print(format('-', '<3s'), end = '')
                print(new_character, end = '')
                print(format('-', '>3s'))
                    
    print('-'*51)
    print('='*51)
    print()


            
# Function write_to_file() - write output to a new text file:
def write_to_file(filename, character_list):
    outfile = open(filename, "w")
    for new_character in character_list:
        outfile.write(new_character)
    outfile.close()
    

# Function find_character() - find the index of the character in the list:
def find_character(character_list, name):
    print()
    name_list = []
    for new_character in character_list:
        name_list.append(new_character.get_name())
    index = list_function.find(name_list, name)
    
    return index

# Function add_character() - place your own comments here...  : )
def add_character(character_list, name, secret_id, is_hero):
    index = find_character(character_list, name)
    if index != -1:
        print(name, 'already exists in character list.')
    else:
        if is_hero == 'h':
            is_hero == True
        else:
            is_hero == False
            
        new_character = character.Character(name, secret_id, is_hero, no_battles = 0, no_won = 0,
                                              no_lost = 0, no_drawn = 0, health = 100)
        character_list.append(new_character)
        print('Successfully added', name, 'to character list.')
    print()
    print()
    return character_list
# Function remove_character() - place your own comments here...  : )
def remove_character(character_list, name):
    index = find_character(character_list, name)
    if index == -1:
        print(name, 'is not found in characters.')
    else:
        del character_list[index]
        print('Successfully removed', name, 'from character list.')
    print()
    print()
    return character_list

character_list = []


### Place your code here...  : )
character_list = read_file("characters.txt")

choices = ['list', 'heroes', 'villains', 'search', 'reset', 'add', 'remove', 'battle', 'quit']
choice_string = list_function.to_string(choices, sep = ', ')
print("Please enter choice")
choice = input('[' + choice_string + ']' + ' ')

while choice not in choices:
    print()
    print("Not a valid command - please try again.")
    print()
    print()
    print("Please enter choice")
    choice = input('[' + choice_string + ']:' + ' ')
    
while choice in ['list', 'heroes', 'villains', 'search', 'reset', 'add', 'remove', 'battle']:
    if choice == 'list':
        display_characters(character_list, 0)
        
        
    elif choice == 'heroes':
        display_characters(character_list, 1)
        
                
    elif choice == 'villains':
        display_characters(character_list, 2)
        
        
    elif choice == 'search':
        name = input("Please enter name: ")
        index = find_character(character_list, name)
        if index == -1:
            print(name, 'is not found in character (heroes and villains) list.')
        else:
            is_hero = character_list[index].get_is_hero()
            if is_hero:
                is_hero = 'HERO'
            else:
                is_hero = 'VILLAIN'
            print()
            print('All about', name, '-->', is_hero)
            print()
            print('Secret identity: ', character_list[index].get_secret_identity())
            print()
            print('Battles fought:', character_list[index].get_no_battles())
            print('  > No won:', format(character_list[index].get_no_won(), '>3d'))
            print('  > No lost:', format(character_list[index].get_no_lost(), '>2d'))
            print('  > No drawn:', format(character_list[index].get_no_drawn(), '>1d'))
            print()
            print('Current health:', str(character_list[index].get_health()) + '%')
            print()
            print()   

    elif choice == 'reset':
        print()
        name = input("Please enter name: ")

        name_list = []
        for new_character in character_list:
            name_list.append(new_character.get_name())
        index = list_function.find(name_list, name)
    
        if index == -1:
            print(name, 'is not found in character (heroes and villains) list.')
        else:
            character_list[index].set_health(health = 100)
            print('Successfully updated', name + "'s health to 100")
        print()
        print()

           
    elif choice == 'add':
        name = input('Please enter name: ')
        secret_identity = input('Please enter secret_identity: ')
        is_hero = input('Is this character a hero or a villain [h|v]? ')
        character_list = add_character(character_list, name, secret_identity, is_hero)
        
        
    elif choice == 'remove':
        name = input("Please enter name: ")
        character_list = remove_character(character_list, name)
        
    print("Please enter choice")
    choice = input('[' + choice_string + ']' + ' ')
    
if choice == 'quit':
    print("\n\n-- Program terminating --\n")



