# Drawing the European Union Flag 

import turtle 

# Set up the screen 
screen = turtle.Screen()
screen.bgcolor("white")


# Create a turtle object 
flag = turtle.Turtle() 
flag.speed(1)

# Draw the blue background 
flag.penup()
flag.goto(-170, -100)
flag.pendown()
flag.color("blue")
flag.begin_fill()
for i in range(2):
    flag.forward(350)
    flag.left(90)
    flag.forward(220)
    flag.left(90)
flag.end_fill()


# Draw the 12 yellow stars 
flag.penup()
flag.goto(18, 70)
flag.color("yellow")
for i in range(12):
    flag.begin_fill()
    for j in range(5):
        flag.forward(20)
        flag.right(144)
    flag.end_fill()
    flag.penup()
    flag.right(30)
    flag.forward(30)
    flag.pendown()

flag.penup()
flag.goto(-170, -100)

# Keep the screen open until clicked 
screen.exitonclick()