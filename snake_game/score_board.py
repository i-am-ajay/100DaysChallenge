import turtle
from turtle import Turtle, Screen


class ScoreBoard:
    def __init__(self, point=0):
        self.point = point
        self.score = Turtle()
        self.score.penup()
        self.score.pencolor("white")
        self.score.goto(0, 270)
        self.score.hideturtle()
        self.update_score(point)

    def update_score(self, point):
        self.point = point
        self.score.write(f"Score : {self.point}", align="center", font=("Arial", 10, "normal"))


if __name__ == "__main__":
    tut = ScoreBoard()
    turtle.done()

