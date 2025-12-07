from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.level = 1

    def player_move(self):
        self.forward(10)
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.level += 1