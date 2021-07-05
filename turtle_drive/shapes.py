import turtle
from turtle import Turtle


class MyTurtle:
    def __init__(self):
        self.tut = Turtle()
        self.tut.penup()
        self.tut.goto(0, 50)
        self.tut.pendown()
        self.tut.pensize(1.5)

    def draw_shape(self, num_sides, color):
        self.tut.pencolor(color)
        angle = 360 / num_sides
        for _ in range(num_sides):
            self.tut.right(angle)
            self.tut.forward(50)


if __name__ == '__main__':
    myTurtle = MyTurtle()
    # draw triangle
    for sides in range(3,11):
        myTurtle.draw_shape(sides, "red")
    turtle.done()

