from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
des = Turtle()
# des.shape("turtle")
colors = ["red", "blue", "black", "coral", "orange", "violet", "magenta", "cyan", "green", "olive"]
angles = [0, 90, 180, 270]
des.pensize(10)
des.speed(10)

def rgb():
    r = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return r

def r_dir(ang):
    des.setheading(ang)
    des.forward(40)

for i in range(100):
    des.pencolor(rgb())
    r_dir(random.choice(angles))










screen.exitonclick()
