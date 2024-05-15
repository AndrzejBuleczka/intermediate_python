from turtle import Turtle, Screen
from random import randint

tim = Turtle()
tim.shape("turtle")
screen = Screen()
screen.colormode(255)
def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)

for x in range(3, 11):
    sides = x
    tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
    draw_shape(sides)


screen.exitonclick()