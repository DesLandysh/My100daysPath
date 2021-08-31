from turtle import Turtle, Screen
from random import choice

des = Turtle()
des.shape("turtle")
colors = ["red", "blue", "black", "coral", "orange", "violet", "magenta", "cyan", "green", "olive"]
# des.color("coral")
for i in range(3, 16):
    des.color(choice(colors))
    for _ in range(i):
        des.forward(50)
        des.right(360/i)











screen = Screen()
screen.exitonclick()
