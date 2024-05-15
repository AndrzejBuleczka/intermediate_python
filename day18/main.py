from turtle import Turtle, Screen
from random import choice, randint

tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")
screen = Screen()
screen.colormode(255)


for x in range(120):
    tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
    tim.circle(100)
    tim.setheading(tim.heading() + 3)


screen.exitonclick()
