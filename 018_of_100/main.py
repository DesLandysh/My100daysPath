from turtle import Turtle, Screen

des = Turtle()
des.shape("turtle")
# des.color("coral")
for i in range(50):
    if i % 2 == 0:
        des.penup()
        des.forward(5)
    des.pendown()
    des.forward(5)












screen = Screen()
screen.exitonclick()
