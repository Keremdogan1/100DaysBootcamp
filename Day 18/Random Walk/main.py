import random
import turtle as t

turtle = t.Turtle()
t.colormode(255)
turtle.pensize(5)
turtle.speed(10)


def pick_direction():
    angle = random.randint(0, 3) * 90
    return angle

for i in range(1000):
    direction = pick_direction()
    tup = (random.randint(1,255), random.randint(1,255), random.randint(1,255))
    turtle.pencolor(tup)
    turtle.forward(10)
    turtle.setheading(direction)

