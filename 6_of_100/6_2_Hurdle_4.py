# my solution
def jump():
    turn_right()
    move()
    turn_right()
    move()

def turn_right():
    for i in range(3):
        turn_left()

while not at_goal():
    if front_is_clear() and wall_on_right():
        move()
    elif wall_in_front():
        turn_left()
    else:
        jump()


# 100DaysOfCode solution
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
