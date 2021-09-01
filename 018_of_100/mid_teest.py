from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
des = Turtle()
# des.shape("turtle")
colors = ["red", "blue", "black", "coral", "orange", "violet", "magenta", "cyan", "green", "olive"]
# angles = [0, 90, 180, 270]
des.pensize(1)
des.speed(0)


def draw(ang):
    for i in range(int(360 / ang)):
        des.color(random.choice(colors))
        des.circle(100)
        des.setheading(des.heading() + ang)


draw(5)







screen.exitonclick()
