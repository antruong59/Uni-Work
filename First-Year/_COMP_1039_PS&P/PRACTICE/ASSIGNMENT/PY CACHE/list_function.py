#
#  PSP Assignment 2 - Provided file (Part I - list_function.py).
#
# File: list_function.py
# Author: Thu Hien Nguyen
# Email Id: nguty317
# Description: - Assugnment 2 - Part I: A Python module (that contains functions
#              that operate on lists)
#                                  
# This is my own work as defined by the University's
# Academic Misconduct policy.
# 
#

# 1. Function length() - function to calculate the length of a list: 
def length(my_list):
    length = 0                      # Variable for list's length.
    
    # Loop to calculate list's length.
    for component in my_list:
        length += 1
        
    return length


# 2. Function to_string() - function to turn a list into a string:
def to_string(my_list, sep=', '):
    my_string = ''                  # A new empty string to store value.
    
    # Loop to convert list into string.
    for index in range(length(my_list)):
        
        # The first items.
        if index < (length(my_list) - 1):
            my_string = my_string + my_list[index] + sep
            
        # The last item.
        else:
            my_string += my_list[length(my_list) - 1]
            
    return my_string


# 3. Function find() - function to find the position of a value in a list:
def find(my_list, value):
    position = 0                    # Variable for position of the value.
    index = 0                       # Variable for loop.
    
    # Loop to find the position of the first value in the list.
    while index < length(my_list) and my_list[index] != value:
        position = -1
        index += 1
        
    # Assign value to the variable position.
    if index < length(my_list) and my_list[index] == value:
        position = index
        
    return position            


# 4. Function insert_value() - function to insert a value in a list:
def insert_value(my_list, value, insert_position):
    new_list = []                   # New empty list to store values.
    index = 0                       # Variable for loop.
    
    # The insert position exceeds the list's length. 
    if insert_position > length(my_list):
        new_list = my_list
        new_list.append(value)
        
    # The insert position is less than 0.
    elif insert_position <= 0:
        new_list = [value] + my_list
        
    else:
        # Loop to insert value into insert position.
        while index < insert_position:
            new_list.append(my_list[index])
            index += 1
        new_list.append(value)
        while index < length(my_list):
            new_list.append(my_list[index])
            index += 1
            
    return new_list
    


# 5. Function remove_value() - function to remove a value in a list:
def remove_value(my_list, remove_position):
    new_list = []                   # New empty list to store values.
    index = 0                       # Variable for loop.
    
    # The remove position exceeds the list's length. 
    if remove_position > length(my_list):
        for index in range(len(my_list)):
            new_list.append(my_list[index])
        del new_list[length(my_list)-1]
        
    # The remove position is less than 0.
    elif remove_position <= 0:
        for index in range(len(my_list)):
            new_list.append(my_list[index])
        del new_list[0]
        
    else:
        # Loop to remove value from remove position.
        while index <= remove_position:
            new_list.append(my_list[index])
            index += 1
        del new_list[remove_position]
        while index < length(my_list):
            new_list.append(my_list[index])
            index += 1
            
    return new_list    
    


# Function reverse() - function to reverse values in a list:
def reverse(my_list, number=-1):
    new_list = []                   # New empty list to store values.
    
    # Number is given in the function call so
    # only the first number of items are reversed.
    if number >= 2 and number < len(my_list):
        index = number
        while index > 0:
            new_list.append(my_list[index - 1])
            index -= 1
        while number < length(my_list):
            new_list.append(my_list[number])
            number += 1
            
    # Number is not given in the function call so
    # the entire list is reversed.
    elif number == -1 or (number >= 2 and number >= len(my_list)):
        index = len(my_list)
        while index > 0:
            new_list.append(my_list[index - 1])
            index -= 1
            
    # Number is less than 2 so no items are reversed.
    else:
        for index in range(len(my_list)):
            new_list.append(my_list[index])
            
    return new_list



