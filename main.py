import turtle
import time
from turtle import Turtle, Screen


class SnakeFeeder:
    def __init__(self):
        self.snake = [Turtle(), Turtle(), Turtle()]
        self.screen = Screen()
        self.screen_update(500, 500, "black")

        count = 0
        for part in self.snake:
            part.penup()
            part.color("white")
            part.shape("square")
            part.setpos(count, 0)
            count -= 20

    def screen_update(self, width, height, color):
        self.screen.screensize(width, height, color)
        self.screen.tracer(0)

    def snake_forward(self):
        while True:
            for part in self.snake:
                part.forward(20)
            time.sleep(.5)
            self.screen.update()

    def turn_snake(self, angle):
        count = 0
        for part in self.snake:
            part.forward(count)
            part.setheading(angle)


if __name__ == "__main__":
    sf = SnakeFeeder()

    sf.snake_forward()
    turtle.done()
