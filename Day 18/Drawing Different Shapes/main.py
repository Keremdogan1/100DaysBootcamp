import random
from turtle import Turtle, Screen

turtle = Turtle()

for i in range(3,11):
    tup = (random.random(), random.random(), random.random())
    turtle.pencolor(tup)
    for _ in range(i):
        turtle.forward(100)
        turtle.right(360/i)

screen = Screen()
screen.exitonclick()
