# Treasure map
# Make it funnier - let's do the search treasure game!!!
import random


# reserved code
row0 = ["/", "1", "2", "3"]  # adding the instructions
row1 = ["1", " ", " ", " "]  # [0] is for instructions
row2 = ["2", " ", " ", " "]
row3 = ["3", " ", " ", " "]
t_map = [row0, row1, row2, row3]
print(f"{row0}\n{row1}\n{row2}\n{row3}")

# solution
tries = 5
treasure_place = random.randint(1, 3), random.randint(1, 3)

while tries > 0:
    position = input(f"Find the treasure in {tries} try/tries, type 2 digit number: ")
    index_x = int(position[0]), int(position[1])
    if index_x == treasure_place:
        t_map[index_x[0]][index_x[1]] = "X"
        print("Yo-ho-ho! You found the treasure!")
        print(f"{row0}\n{row1}\n{row2}\n{row3}")
        break
    tries -= 1

quit()
