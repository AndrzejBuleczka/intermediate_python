import time
from turtle import Screen, Turtle
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


def create_snake():
    snake_part = Turtle("square")
    snake_part.color("white")
    snake_part.penup()
    return snake_part


segments = []


for i in range(3):
    tim = create_snake()
    tim.goto(0 - 20 * i, 0 )
    segments.append(tim)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)


screen.exitonclick()
