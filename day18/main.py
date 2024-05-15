from turtle import Turtle, Screen
from random import randint

tim = Turtle()
tim.shape("turtle")
screen = Screen()
screen.colormode(255)

for x in range(3, 11):
    sides = x
    tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
    for _ in range(sides):
        tim.forward(100)
        tim.right(360 / sides)


screen.exitonclick()