from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Roboto", 16, "normal")


def create_scoreboard(player_score):
    score = Turtle()
    score.penup()
    score.color("white")
    score.goto(0, 270)
    score.write(f"Score: {player_score}", align=ALIGNMENT, font=FONT)
    return score
