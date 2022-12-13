import enum
import random
def display_map(columns, rows):
    room = ''
    l1 = ['+---- ----+', '|         |', '           ', '|         |', '+---- ----+']
    oy = columns
    for ox in range(rows):
        for index in range(len(l1)):
            room += (l1[index] + '  ') * oy + '\n'


    print(room)


# use either 'from enum import IntEnum' or 'name(enum.IntEnum)'
class direction(enum.Enum):
    North = 1
    South = 2
    East = 3
    West = 4



# user_columns = int(input('Please enter number of columns: '))
# user_rows = int(input('Please enter number of rows: '))
# display_map(user_columns, user_rows)
