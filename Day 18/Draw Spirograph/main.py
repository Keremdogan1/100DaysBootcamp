import random
import turtle as t

turtle = t.Turtle()
turtle.speed("fastest")

def draw_spirograph(circle_amount):
    for _ in range(circle_amount):
        tup = (random.random(), random.random(), random.random())
        turtle.pencolor(tup)
        turtle.circle(100)
        turtle.setheading(turtle.heading() + 360/circle_amount)

draw_spirograph(60)

screen = t.Screen()
screen.exitonclick()