import turtle
 # create a turtle object
t = turtle.Turtle()
 # set pen color to blue
t.pencolor("blue")
 # set fill color to blue
t.fillcolor("blue")
 # start filling the shape
t.begin_fill()
 # draw a circle with radius 50
t.circle(50)
 # stop filling the shape
t.end_fill()
 # hide the turtle
t.hideturtle()
 # wait for user to close the window
turtle.done()