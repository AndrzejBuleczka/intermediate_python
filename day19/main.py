from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
if user_bet:
    is_race_on = True


def create_turtle():
    for i in range(1, 8):
        tim = Turtle("turtle")
        tim.color(colors[i - 1])
        tim.penup()
        tim.goto(x=-230, y=-190 + (i * 50))


create_turtle()


while is_race_on:
    for turtle in screen.turtles():
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
