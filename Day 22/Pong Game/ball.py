import random
from turtle import Turtle

HEADINGS = (45, 135, 225, 315)
LEFT_HEADINGS = (135, 225)
RIGHT_HEADINGS = (45, 315)

def random_y():
    return random.randint(-23,23) * 10


class Ball(Turtle):

    def __init__(self):
        super().__init__(shape="square")
        self.color("white")
        self.penup()
        self.angle = random.choice(HEADINGS)
        self.goto(0, random_y())
        self.move_forward = 10

    def move(self):
        self.setheading(self.angle)
        self.forward(self.move_forward)
        self.setheading(0)

    def check_bounce(self, left_paddle, right_paddle):
        if self.ycor() <= -240 or self.ycor() >= 250:
            self.angle = abs(360 - self.angle)
        elif (self.distance(left_paddle) < 35 and self.xcor() < -385) or (self.distance(right_paddle) < 35 and self.xcor() > 370):
            self.move_forward += 1
            if self.angle < 180:
                self.angle = abs(180 - self.angle)
            else:
                self.angle = abs(540 - self.angle)

    def check_out(self, left_score , right_score):
        if self.xcor() > 410 or self.xcor() < -420:
            self.move_forward = 10
            if self.xcor() > 400:
                left_score += 1
                self.angle = random.choice(LEFT_HEADINGS)
            else:
                right_score += 1
                self.angle = random.choice(RIGHT_HEADINGS)
            self.goto(0, random_y())
        scores = [left_score, right_score]
        return scores


