from turtle import Turtle
import turtle
import random


class SnakePart(Turtle):
    def __init__(self):
        super().__init__()


class SnakeGenerator:
    def __init__(self):
        self.snake = [SnakePart(), SnakePart(), SnakePart()]
        self.create_snake()

    def create_snake(self):
        count = 0
        for part in self.snake:
            part.penup()
            part.color("white")
            part.shape("square")
            part.setpos(count, 0)
            count -= 20

