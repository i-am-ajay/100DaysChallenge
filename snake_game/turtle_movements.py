import turtle
from turtle import Turtle, Screen


class TurtleMovements:
    def __init__(self):
        self.tut = Turtle()
        self.sc = Screen()

    def left_turn(self):
        print("left pressed")
        self.tut.setheading(90)

    def right_turn(self):
        print("right pressed")
        self.tut.setheading(270)

    def back_turn(self):
        print("back pressed")
        self.tut.setheading(180)

    def move_turtle(self):
        self.sc.onkeypress(self.left_turn, "Left")
        self.sc.onkeypress(self.right_turn, "Right")
        self.sc.onkeypress(self.back_turn, "Down")


if __name__ == "__main__":
    tut = TurtleMovements()
    tut.move_turtle()
    turtle.done()

