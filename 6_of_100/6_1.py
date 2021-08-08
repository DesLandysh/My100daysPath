"""
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
"""

#my solution
def turn_right():
    for i in range(3):
        turn_left()


def jump(num):
    for i in range(num):
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()


jump(6)
# 142 intructions 47 sec but more DRY

# so it takes 1 sec for 3 instructions so second loop takes 14 sec!

# 31 sec for true WET code and 74 instructions (with no functions at all)
# While loop takes 105 instructions

# official solution: 99 instructions and 33 sec
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


for i in range(6):
    jump()


# for hurdle 3 random walls
...
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()