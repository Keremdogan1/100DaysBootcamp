from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, paddle_position):
        super().__init__(shape="square")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color("white")
        self.penup()
        self.goto(paddle_position)

    def paddle_up(self):
        if self.ycor() < 230:
            self.forward(20)

    def paddle_down(self):
        if self.ycor() > -220:
            self.backward(20)