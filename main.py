import turtle
import time
from turtle import Turtle, Screen


class SnakeFeeder:
    def __init__(self):
        self.snake = [Turtle(), Turtle(), Turtle()]
        self.screen = Screen()
        self.screen.delay(5)
        self.screen.screensize(500, 500, "black")

        count = 10
        for part in self.snake:
            part.penup()
            part.color("white")
            part.shape("square")
            part.setpos(count, 0)
            count -= 20

    def snake_forward(self):
        while True:
            self.screen.update()
            for part in self.snake:
                part.forward(20)
                time.sleep(1)



if __name__ == "__main__":
    sf = SnakeFeeder()
    sf.snake_forward()
    turtle.done()
