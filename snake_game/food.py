from turtle import Turtle
import turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        random_x = random.randint(-280,280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.pendown()
        self.dot(10, "blue")
        self.hideturtle()


if __name__ == "__main__":
    tut = Food()
    turtle.done()

