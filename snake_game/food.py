from turtle import Turtle
import turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        random_x = (random.randint(-280, 280) // 10) * 10
        random_y = (random.randint(-280, 280) // 10) * 10
        self.goto(random_x, random_y)
        self.pendown()
        self.dot(10, "blue")
        self.hideturtle()

    def food_coordinates(self):
        return self.position()


if __name__ == "__main__":
    tut = Food()
    print(tut.food_coordinates())
    turtle.done()


