import turtle
from turtle import Turtle, Screen
from turtledemo import chaos


class PongScreen:
    def __init__(self):
        self.pong_screen = Screen()
        self.pong_screen.title("Pong Beater")
        self.pong_screen.bgcolor("black")
        self.pong_screen.setup(950, 600)

    @staticmethod
    def screen_divider():
        tut_up = Turtle()
        tut_up.pensize(2)
        tut_up.pencolor("white")
        tut_up.hideturtle()
        tut_down = tut_up.clone()
        tut_up.left(90)
        tut_down.right(90)
        for i in range(0, 15):
            PongScreen.draw_line_segment(tut_up)
            PongScreen.draw_line_segment(tut_down)

    @staticmethod
    def draw_line_segment(tut):
        tut.forward(10)
        tut.penup()
        tut.forward(10)
        tut.pendown()


if __name__ == "__main__":
    pong = PongScreen()
    pong.screen_divider()
    turtle.done()
