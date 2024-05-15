import turtle
from turtle import Turtle, Screen
from random import choice
# import colorgram
#
#
# colors = colorgram.extract('hirst.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(236, 243, 250), (236, 226, 85), (211, 159, 109), (115, 176, 211), (202, 5, 69), (231, 53, 126), (195, 77, 20), (215, 133, 176), (194, 163, 14), (33, 106, 169), (10, 20, 65), (30, 189, 116), (232, 224, 4), (18, 28, 172), (234, 165, 197), (121, 187, 159), (203, 31, 130), (12, 186, 212), (10, 46, 25), (143, 216, 200), (43, 17, 11), (39, 132, 71), (107, 92, 210), (182, 15, 8), (127, 219, 233), (233, 71, 40), (169, 178, 229)]
turtle.colormode(255)
dot = Turtle()
dot.hideturtle()
dot.speed("fastest")
dot.pensize(20)
dot.setheading(225)
dot.penup()
dot.forward(350)
dot.setheading(0)
dot.pendown()


def draw_dots_row():
    for x in range(10):
        dot.dot(20, choice(color_list))
        dot.penup()
        dot.forward(50)


for y in range(10):
    draw_dots_row()
    dot.setheading(90)
    dot.forward(50)
    dot.setheading(180)
    dot.forward(500)
    dot.setheading(0)


screen = Screen()
screen.exitonclick()
