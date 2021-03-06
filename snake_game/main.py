import turtle
import time
from turtle import Turtle, Screen
from snake import SnakeGenerator,SnakePart
from food import Food
from score_board import ScoreBoard


class SnakeManager:
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0

    def __init__(self):
        self.screen = Screen()
        self.screen_update(500, 500, "black")
        self.screen.listen()
        self.snake = SnakeGenerator().snake
        self.screen.update()
        self.food = Food()
        self.score_board = ScoreBoard()

    def screen_update(self, width, height, color):
        self.screen.screensize(width, height, color)
        self.screen.tracer(0)

    def snake_forward(self):
        while True:
            self.got_food()
            for index in range(len(self.snake)-1, 0, -1):
                new_x = self.snake[index-1].xcor()
                new_y = self.snake[index-1].ycor()
                self.snake[index].goto(new_x, new_y)
            self.snake[0].forward(20)
            time.sleep(.5)
            self.screen.onkeypress(self.left_turn, "Left")
            self.screen.onkeypress(self.right_turn, "Right")
            self.screen.onkeypress(self.up_turn, "Up")
            self.screen.onkeypress(self.back_turn, "Down")
            self.screen.update()

    def left_turn(self):
        if self.snake[0].heading() != SnakeManager.RIGHT:
            self.snake[0].setheading(SnakeManager.LEFT)

    def right_turn(self):
        if self.snake[0].heading() != SnakeManager.LEFT:
            self.snake[0].setheading(SnakeManager.RIGHT)

    def back_turn(self):
        if self.snake[0].heading() != SnakeManager.UP:
            self.snake[0].setheading(SnakeManager.DOWN)

    def up_turn(self):
        if self.snake[0].heading() != SnakeManager.DOWN:
            self.snake[0].setheading(SnakeManager.UP)

    def got_food(self):
        if self.snake[0].distance(self.food) < 15:
            self.score_board.score.clear()
            self.score_board.update_score(self.score_board.point+10)
            self.food.clear()
            self.food = None
            self.food = Food()
            self.snake.append(SnakePart())


if __name__ == "__main__":
    sm = SnakeManager()
    sm.snake_forward()
    turtle.done()
