# Drawing the American Flag with Turtle Python 

import turtle 

# Set up the screen 
screen = turtle.Screen()
screen.bgcolor("white")

# create a turtle object 
t = turtle.Turtle()
t.speed(10)

# Define some constants 
WIDTH = 20
HEIGHT = 10 
STAR_SIZE = 10 

# Draw the red and white stripes 
for i in range(13): 
    t.penup()
    t.goto(-190, 90 - i * HEIGHT * 1.5)
    t.pendown()
    if i % 2 == 0: 
        t.color("red", "red")
    else: 
        t.color("white", "white")
    t.begin_fill()
    for j in range(2):
        t.forward(WIDTH * 19)
        t.right(90)
        t.forward(HEIGHT * 1.5)
        t.right(90)
    t.end_fill()

# Draw the blue rectangle 
t.penup()
t.goto(-190, 90)
t.pendown()
t.color("blue", "blue")
t.begin_fill()
for i in range(2):
    t.forward(WIDTH * 6.9)
    t.right(90)
    t.forward(HEIGHT * 10.4)
    t.right(90)
t.end_fill()

# Draw the stars 
t.penup()
t.goto(-177, 80)
t.color("white", "white")
for i in range(9):
    if i % 2 == 0: 
        for j in range(6): 
            t.penup()
            t.goto(-177 + j * WIDTH, 80 - i * HEIGHT)
            t.pendown()
            t.begin_fill()
            for k in range(5):
                t.forward(STAR_SIZE)
                t.right(144)
            t.end_fill()
    else: 
        for j in range(5):
            t.penup()
            t.goto(-167 + j * WIDTH, 80 - i * HEIGHT)
            t.pendown()
            t.begin_fill()
            for k in range(5):
                t.forward(STAR_SIZE)
                t.right(144)
            t.end_fill()

# Hide the turtle and keep the screen open 
t.hideturtle()
screen.mainloop()