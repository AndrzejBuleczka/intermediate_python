from turtle import Screen, Turtle
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

def create_snake():
    tim = Turtle("square")
    tim.color("white")
    tim.penup()
    return tim

for i in range(3):
    tim = create_snake()
    tim.goto(0 - 20 * i, 0 )


screen.exitonclick()
