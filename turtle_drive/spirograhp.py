import random
import turtle
from turtle import Turtle


class Spirograph:
    def __init__(self):
        self.tut = Turtle()
        turtle.colormode(255)

    def get_color(self):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return red, green, blue

    def make_spirograph(self, y):
        rgb_color = self.get_color()
        self.tut.pencolor(rgb_color)
        self.tut.setheading(y)
        # self.tut.right(y)
        self.tut.tilt(y)
        self.tut.circle(radius=50)


if __name__ == "__main__":
    sp = Spirograph()
    for angle in range(0, 360, 10):
        sp.make_spirograph(angle)
    turtle.done()
