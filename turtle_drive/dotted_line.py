from turtle import Turtle, Screen
import turtle

tut = Turtle()
tut.penup()
tut.goto(x=-250, y=0)
for _ in range(50):
    tut.pendown()
    tut.forward(3)
    tut.penup()
    tut.forward(2)

turtle.done()