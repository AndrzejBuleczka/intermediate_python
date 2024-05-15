from turtle import Turtle, Screen
from random import choice, randint

tim = Turtle()
tim.shape("turtle")
tim.pensize(15)
tim.speed(8)
screen = Screen()
screen.colormode(255)

directions = [0, 90, 180, 270]


def move_forwards():
    tim.forward(30)
    tim.setheading(choice(directions))


for x in range(100):
    tim.color(randint(1, 4), randint(0, 255), randint(0, 255))
    move_forwards()


screen.exitonclick()
