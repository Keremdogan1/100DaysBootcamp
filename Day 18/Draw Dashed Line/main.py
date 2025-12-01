from turtle import Turtle, Screen

turtle = Turtle()

for _ in range(15):
    turtle.down()
    turtle.forward(10)
    turtle.up()
    turtle.forward(10)

screen = Screen()
screen.exitonclick()