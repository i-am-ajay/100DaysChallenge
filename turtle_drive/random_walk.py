import random
import turtle
from turtle import Turtle


class RandomWalk:
    def __init__(self):
        turtle.colormode(255)
        self.tut = Turtle()
        self.tut.pensize(7)
        self.tut.speed(70)

    def random_walk(self):
        choose = random.choice([0, 90, 180, 270])
        self.tut.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.tut.forward(15)
        self.tut.setheading(choose)


if __name__ == "__main__":
    obj = RandomWalk()
    for _ in range(3000):
        obj.random_walk()
    turtle.done()

