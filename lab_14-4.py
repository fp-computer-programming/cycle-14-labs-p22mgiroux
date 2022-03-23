# Author: MOG 3/23/22

import turtle

window = turtle.Screen()
window.setup()
window.title("Lab 4")
toby = turtle.Turtle()
toby.speed(3)
toby.color("red")
toby.fillcolor("maroon")

toby.stamp()
toby.penup()
toby.begin_fill()
toby.setposition(100,100)
toby.pendown()
toby.forward(100)
toby.right(90)
toby.forward(100)
toby.right(90)
toby.forward(100)
toby.right(90)
toby.forward(100)
toby.end_fill()

window.mainloop()