import time
from turtle import Screen
from player import Player
from car_manager import CarManager, move_cars, cars
from scoreboard import Scoreboard

DELAY = 1

game_time = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()

screen.onkeypress(player.player_move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(DELAY / 10)
    game_time += DELAY

    if game_time % 6 == 0:
        new_car = CarManager()
    move_cars(player.level)

    scoreboard.update_level(player.level)
    for car in cars:
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()


    screen.update()

screen.exitonclick()
