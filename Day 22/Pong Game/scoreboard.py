from turtle import Turtle

line = Turtle()

def draw_line():
    line.penup()
    line.hideturtle()
    line.pensize(10)
    line.pencolor("white")

    line.setheading(270)
    line.goto(0, 245)

    for _ in range(10):
        line.pendown()
        line.forward(25)
        line.penup()
        line.forward(25)

class Scoreboard(Turtle):
    def __init__(self):
        draw_line()

        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()

        self.left_score = 0
        self.right_score = 0

        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-50, 230)
        self.write(f"{self.left_score}", align="center", font=("Courier", 20, "bold"))

        self.goto(50, 230)
        self.write(f"{self.right_score}", align="center", font=("Courier", 20, "bold"))

    def is_game_finished(self):
        if self.left_score == 3 or self.right_score == 3:
            if self.left_score == 3:
                line.goto(0, 0)
                line.clear()
                line.write("Left win!", align="center", font=("Courier", 30, "bold"))
            else:
                line.goto(0, 0)
                line.clear()
                line.write("Right win!", align="center", font=("Courier", 30, "bold"))

            return True
        else:
            return False
