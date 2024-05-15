from turtle import Turtle, Screen
from random import choice, randint

tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")
screen = Screen()
screen.colormode(255)


def draw_spirograph(size_of_gap):
    for x in range(int(360 / size_of_gap)):
        tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen.exitonclick()
