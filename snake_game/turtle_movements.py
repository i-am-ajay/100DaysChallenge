import turtle
from turtle import Turtle, Screen


class TurtleMovements:
    def __init__(self):
        self.tut = Turtle()
        self.sc = Screen()
        self.sc.bgcolor("black")
        self.sc.listen()

    def show_food(self):
        temp_tut = Turtle()
        temp_tut.penup()
        temp_tut.hideturtle()
        temp_tut.goto(100, 200)
        temp_tut.pendown()
        temp_tut.dot(10, "blue")
        temp_tut.hideturtle()


if __name__ == "__main__":
    tut = TurtleMovements()
    tut.show_food()
    turtle.done()

