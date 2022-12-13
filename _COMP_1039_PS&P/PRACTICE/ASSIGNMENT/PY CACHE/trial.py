import character
import random
import list_function



# Function that displays my details to the screen.
def display_details():
    print("File     : nguty317_poker.py")
    print("Author   : Thu Hien Nguyen")
    print("Stud ID  : 110270736")
    print("Email ID : nguty317")
    print("This is my own work as defined by the")
    print("University's Academic Misconduct Policy.")
    
# Function read_file() - place your own comments here...  : )
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


# Function display_characters() - place your own comments here...  : )
def display_characters(character_list, display_type):

    # This line will eventually be removed - used for development purposes only.
    print("In function display_characters()")

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
    
    character_list = read_file("characters.txt")
    
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
def find_character(character_list, name):
    name_list = []
    for new_character in character_list:
        name_list.append(new_character.get_name())
    index = list_function.find(name_list, name)
    
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
character_list = read_file("characters.txt")
display_characters(character_list, 1)
name = input("Please enter name: ")
find_character(character_list, name)
