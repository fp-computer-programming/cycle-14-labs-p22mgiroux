# Author: MOG 3/23/22

import turtle

window = turtle.Screen()
toby = turtle.Turtle()
toby.color(window.textinput("Color?", "What color would you like?"))
size = int(window.textinput("Size?", "What size would you like the turtle to be (1-5)?"))
if size > 5:
    toby.shapesize(5)
elif size < 1:
    toby.shapesize(1)
else:
    toby.shapesize(size)

toby.begin_fill()
toby.forward(100)
toby.right(90)
toby.forward(100)
toby.right(90)
toby.forward(100)
toby.right(90)
toby.forward(100)
toby.end_fill()

window.listen()
window.mainloop()