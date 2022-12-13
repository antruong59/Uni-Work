#
# PSP Assignment 2 - Provided file (Part I - list_function.py).
# Remove this and place appropriate file comments here.
# File      : list_function.py
# Author    : Ngoc An Truong
# Email Id  : truan004@mymail.unisa.edu.au
# Description: Assignment 2 - Writing a Python Module (list manipulation functions)
#                           - This Python codes include functions that manipulate lists, named as:
#                               + length(my_list)
#                               + to_string(my_list, sep=', ')
#                               + find(my_list, value)
#                               + insert_value(my_list, value, insert_position)
#                               + remove_value(my_list, remove_position)
#                               + get_slice(my_list, start, stop)
#
# This is my own work as defined by the University's
# Academic Misconduct policy.
# Modify this file to include your code solution.
#
#
# Write your function definitions in this file.
# Place your own comments in this file also.
#


# Function length() - place your own comments here...  : )
# Function to count the total items in list

def length(my_list):

    # This line will eventually be removed - used for development purposes only.
    # print("In function length()")

    # Place your code and comments here

    # Variable to count number of items in list
    count = 0

    for item in my_list:
        count += 1
    return count

# Function to_string() - place your own comments here...  : )
# Function to convert a list into a string

def to_string(my_list, sep=', '):

    # This line will eventually be removed - used for development purposes only.
    # print("In function to_string()")

    # Place your code and comments here

    # Variable to store items in list into string
    string = ''

    # Variable to check for every items in list
    index = 0

    # Loop to append every items in list into string (with commas, except for the last one)
    while index < length(my_list) - 1:
        string = string + str(my_list[index]) + sep
        index += 1

    # Append the last one
    if index == length(my_list) - 1:
        string += str(my_list[index])
    return string

# Function find() - place your own comments here...  : )
# Function to find a value in list

def find(my_list, value):
    
    # This line will eventually be removed - used for development purposes only.
    # print("In function find()")

    # Place your code and comments here

    # Variable to return -1 if value not in list
    index = -1

    # Variable to check for every items in list
    i = 0

    while i < length(my_list):
        if my_list[i] == value:
            index = i

            # Variable to check the first position of value in list then get out of loop
            i = length(my_list) + 1

        i += 1
    return index

# Function insert_value() - place your own comments here...  : )
# Function to insert value into list

def insert_value(my_list, value, insert_position):
    
    # This line will eventually be removed - used for development purposes only.
    # print("In function insert_value()")

    # Place your code and comments here

    if insert_position >= length(my_list):
        my_list.append(value)
    elif insert_position <= 0:
        my_list = [value] + my_list
    else:

        # Append one more item into list to expand the list
        my_list.append(None)

        # Variable to check for every items in list from the last item
        index = length(my_list) - 1

        # Loop to insert value into specific position in list
        while index >= insert_position >= - index:
            my_list[index] = my_list[index - 1]
            if insert_position == index:
                my_list[insert_position] = value
            index -= 1

    return my_list

# Function remove_value() - place your own comments here...  : )
# Function to remove value from list

def remove_value(my_list, remove_position):
    
    # This line will eventually be removed - used for development purposes only.
    # print("In function remove_value()")

    # Place your code and comments here

    # Variable to store a copy of list
    new_list = []

    if remove_position >= length(my_list):
        for index in range(length(my_list) - 1):
            new_list.append(my_list[index])
    elif 0 <= remove_position < length(my_list):
        for index in range(remove_position):
            new_list.append(my_list[index])
        for index in range(remove_position + 1, length(my_list)):
            new_list.append(my_list[index])
    else:
        for index in range(1, length(my_list)):
            new_list.append(my_list[index])

    return new_list

# Function get_slice() - place your own comments here...  : )
# Function to slice and get part of the list

def get_slice(my_list, start, stop):

    # This line will eventually be removed - used for development purposes only.
    # print("In function get_slice()")

    # Place your code and comments here

    # Variable to store a copy of list
    new_list = []

    if 0 <= start < stop <= length(my_list) or (start < 0 and stop < 0):
        for index in range(start, stop):
            new_list.append(my_list[index])
    elif 0 <= start < length(my_list) < stop:
        for index in range(start, length(my_list)):
            new_list.append(my_list[index])
    elif start < 0 < stop <= length(my_list):
        for index in range(0, stop):
            new_list.append(my_list[index])
    elif start < 0 < length(my_list) < stop:
        for index in range(0, length(my_list)):
            new_list.append(my_list[index])

    return new_list

