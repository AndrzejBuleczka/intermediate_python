from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Roboto", 16, "normal")

def create_scoreboard():
    score = Turtle()
    score.penup()
    score.color("white")
    score.goto(0, 270)
    score.write("Score: 0", align=ALIGNMENT, font=FONT)
    return score