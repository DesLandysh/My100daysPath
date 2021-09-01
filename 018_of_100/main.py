import colorgram
from random import choice
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)

colors = colorgram.extract('hirst.jpg', 25)
color = []

for i in range(25):
    extra = colors[i]
    rgb = extra.rgb
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    col = [r, g, b]
    color.append(col)


dot = Turtle()
dot.speed(0)
x = -600
y = 500
dot.penup()
dot.goto(x, y)

for row in range(11):
    for line in range(9):
        dot.pendown()
        dot.dot(50, choice(color))
        dot.penup()
        dot.forward(150)
    y -= 100
    dot.goto(x, y)


screen.exitonclick()
