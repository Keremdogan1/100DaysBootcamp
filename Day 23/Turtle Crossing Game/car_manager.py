import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10
FINISH_LINE_X = -320
SPAWN_POINTS = [(280, -240), (280, -220), (280, -200), (280, -180), (280, -160), (280, -140), (280, -120), (280, -100), (280, -80), (280, -60), (280, -40), (280, -20), (280, 0), (280, 20), (280, 40), (280, 60), (280, 80), (280, 100), (280, 120), (280, 140), (280, 160), (280, 180), (280, 200), (280, 220), (280, 240)]

cars = []

def move_cars(level):
    for car in cars:
        if car.xcor() > FINISH_LINE_X:
            car.move_distance = level * 10
            car.forward(car.move_distance)

class CarManager(Turtle):
    def __init__(self):
        super().__init__("square")
        self.penup()
        self.goto(random.choice(SPAWN_POINTS))
        self.color(random.choice(COLORS))
        self.move_distance = 0
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        cars.append(self)