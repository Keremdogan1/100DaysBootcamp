import random
import turtle as t
import colorgram

turtle = t.Turtle()
t.colormode(255)

turtle_x = -360
turtle_y = -360

turtle.penup()
turtle.hideturtle()
turtle.speed("fastest")
turtle.setpos(turtle_x,turtle_y)

colors = colorgram.extract('image.jpg', 30)
color_tuples_list = []
for i in range(len(colors)):
    rgb_tuple = (colors[i].rgb.r , colors[i].rgb.g , colors[i].rgb.b)
    color_tuples_list.append(rgb_tuple)

color_tuples_list = [(198, 165, 116), (144, 79, 55), (221, 201, 138), (58, 93, 121), (167, 153, 48), (132, 34, 23), (137, 162, 181), (69, 40, 34), (51, 117, 87), (195, 93, 75), (146, 178, 150), (18, 93, 72), (231, 176, 165), (162, 143, 158), (35, 60, 75), (105, 73, 77), (180, 204, 177), (148, 19, 23), (83, 147, 127), (70, 37, 40), (18, 70, 60), (27, 82, 88), (40, 66, 89), (190, 86, 89), (68, 64, 58), (223, 176, 180)]


for _ in range(10):
    for _ in range(10):
        tup = (random.choice(color_tuples_list))
        turtle.dot(25, tup)
        turtle_x += 80
        turtle.setpos(turtle_x, turtle_y)

    turtle_x = -360
    turtle_y += 80
    turtle.setpos(turtle_x, turtle_y)

screen = t.Screen()
screen.exitonclick()
