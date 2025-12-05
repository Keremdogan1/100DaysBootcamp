import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

LEFT_POS = (-400, 0)
RIGHT_POS = (390, 0)

screen = Screen()
screen.setup(width=858, height=525)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

ball = Ball()
left_paddle = Paddle(LEFT_POS)
right_paddle = Paddle(RIGHT_POS)

scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(right_paddle.paddle_up, "Up")
screen.onkeypress(right_paddle.paddle_down, "Down")
screen.onkeypress(left_paddle.paddle_up, "w")
screen.onkeypress(left_paddle.paddle_down, "s")

is_game_on = True

while is_game_on:
    time.sleep(0.05)
    ball.move()
    ball.check_bounce(left_paddle, right_paddle)
    updated_scores = ball.check_out(scoreboard.left_score, scoreboard.right_score)

    scoreboard.left_score = updated_scores[0]
    scoreboard.right_score = updated_scores[1]

    scoreboard.update_score()
    if scoreboard.is_game_finished():
        ball.hideturtle()
        left_paddle.hideturtle()
        right_paddle.hideturtle()

        is_game_on = False

    screen.update()

screen.exitonclick()