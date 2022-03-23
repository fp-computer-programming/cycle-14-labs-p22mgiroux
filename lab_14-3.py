# Author: MOG 3/23/22

import turtle

window = turtle.Screen()
window.setup(1000, 1000)
window.title("Lab 3")
window.bgcolor("grey")
toby = turtle.Turtle()
toby.shape("turtle")
toby.pencolor("aquamarine")

for x in range(3):
    toby.left(120)
    toby.forward(200)

window.mainloop()