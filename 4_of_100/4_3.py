# Tresure map

# U r goin' t write a prog which will mark a spot woth an X.
# map is made of 3 rows of blank squares
""" 1   2   3
1 [' ',' ',' ']
2 [' ',' ',' ']
3 [' ',' ',' ']
"""
# Ur prog should allow you to enter the position of the treasure using a two-digit num.
# 1st digit is the columns
# 2nd digit is the rows
# e.g 23 - where 2 is the columns, and 3 is the row
""" 1   2   3
1 [' ',' ',' ']
2 [' ',' ',' ']
3 [' ','X',' ']
"""

# reserved code
row0 = ["/", "1", "2", "3"]  # adding the instructions
row1 = ["1", " ", " ", " "]  # [0] is for instructions
row2 = ["2", " ", " ", " "]
row3 = ["3", " ", " ", " "]
t_map = [row1, row2, row3]
print(f"{row0}\n{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# Solution
index_x = int(position[0]), int(position[1])
# t_map[index_x[0]-1][index_x[1]-1] = "X"  # if delete all modifies or added rows
t_map[index_x[0]-1][index_x[1]] = "X"
print(f"{row0}\n{row1}\n{row2}\n{row3}")




