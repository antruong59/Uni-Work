#
#  PSP Assignment 2 (Part I) - Test File
#  Study Period 5, 2020
#
#  DO NOT MODIFY THIS FILE!
#

import list_function

print("\nStart Testing!")

str_list1 = ['r', 'i', 'n', 'g', 'i', 'n', 'g']
str_list2 = ['r', 'e', 'd']
empty = []

print("\nlength Test")
print("List length:", list_function.length(str_list1))
print("List length:", list_function.length(empty))

print("\nto_string Test")
string = list_function.to_string(str_list1)
print("List is:", string)
string = list_function.to_string(str_list1, sep='-')
print("List is:", string)
print("List is:", list_function.to_string(empty))

print("\nfind Test")
print(list_function.find(str_list1, 'g'))
print(list_function.find(str_list1, 'z'))

print("\ninsert_value Test")
str_list6 = ['one','three','four', 'five']
new_list = list_function.insert_value(str_list6, 'two', 1)
print(new_list)
str_list7 = ['i', 't']
str_list7 = list_function.insert_value(str_list7, 'p', 0)
print(str_list7)
str_list7 = list_function.insert_value(str_list7, 's', -1)
print(str_list7)
str_list7 = list_function.insert_value(str_list7, 's', 7)
print(str_list7)

print("\nremove_value Test")
str_list8 = ['r','i','n','g']
new_list = list_function.remove_value(str_list8, 2)
print(new_list)
new_list = list_function.remove_value(str_list8, -1)
print(new_list)
new_list = list_function.remove_value(str_list8, 10)
print(new_list)

print("\nget_slice Test")
print(str_list1)
my_slice = list_function.get_slice(str_list1, 4, 100)
print('Slice is:', my_slice)
my_slice = list_function.get_slice(str_list1, 6, 1)
print('Slice is:', my_slice)
my_slice = list_function.get_slice(str_list1, -1, 4)
print('Slice is:', my_slice)
my_slice = list_function.get_slice(str_list1, 2, 5)
print('Slice is:', my_slice)

print("\nEnd Testing!\n")


