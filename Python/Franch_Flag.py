# Drawing the French Flag using Turtle Python 

import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
t = turtle.Turtle()
t.speed(1)

# Define some constants
WIDTH = 20
HEIGHT = 10

# Draw the blue stripe
t.penup()
t.goto(-190, 90)
t.pendown()
t.color("blue", "blue")
t.begin_fill()
for i in range(2):
    t.forward(WIDTH * 6.33)
    t.right(90)
    t.forward(HEIGHT * 25)
    t.right(90)
t.end_fill()

# Draw the white stripe
t.penup()
t.goto(-190 + WIDTH * 6.33, 90)
t.pendown()
t.color("white", "white")
t.begin_fill()
for i in range(2):
    t.forward(WIDTH * 6.33)
    t.right(90)
    t.forward(HEIGHT * 25)
    t.right(90)
t.end_fill()

# Draw the red stripe
t.penup()
t.goto(-190 + WIDTH * 12.66, 90)
t.pendown()
t.color("red", "red")
t.begin_fill()
for i in range(2):
    t.forward(WIDTH * 6.33)
    t.right(90)
    t.forward(HEIGHT * 25)
    t.right(90)
t.end_fill()

# Hide the turtle and keep the screen open
# drawing the french flag end
t.hideturtle()
screen.mainloop()
