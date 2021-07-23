from turtle import Turtle
import turtle
import random


class SnakePart(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.speed(9)
        self.penup()


class SnakeGenerator:
    def __init__(self):
        self.snake = [SnakePart(), SnakePart(), SnakePart()]
        self.create_snake()

    def create_snake(self):
        count = 0
        for part in self.snake:
            part.setpos(count, 0)
            count -= 20

