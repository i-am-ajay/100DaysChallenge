import turtle
from random import choice
color_list = ['alice blue','AliceBlue','antique white','AntiqueWhite','AntiqueWhite1','AntiqueWhite2','AntiqueWhite3','AntiqueWhite4','aquamarine','aquamarine1','aquamarine2','aquamarine3','aquamarine4','azure','azure1','azure2','azure3','azure4','beige','bisque','bisque1','bisque2','bisque3','bisque4','black','BlanchedAlmond']
s = turtle.Screen()
s.bgcolor("maroon")
s.title("Turtle")
tut = turtle.Turtle()
tut.goto(0, -150)
var = 200


for i in range(40):
    tut.circle(var)
    var -= 5
    tut.color(choice(color_list))
turtle.done()

