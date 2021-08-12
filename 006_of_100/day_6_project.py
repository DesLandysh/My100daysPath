# maze resolve

# my solution
def turn_right():
    for i in range(3):
        turn_left()

while not at_goal():
    while right_is_clear():
        turn_right()
        move()
    while wall_on_right():
        while wall_in_front():
            turn_left()
        move()


# 100 days solution
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
