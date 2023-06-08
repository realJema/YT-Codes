import turtle

# Set screen size
screen = turtle.Screen()
screen.setup(600, 400)

# Set background color
screen.bgcolor("white")

# Create a turtle object
flag = turtle.Turtle()

# Set turtle speed
flag.speed(10)

# Draw the white rectangle
flag.penup()
flag.goto(-300,-200)
flag.pendown()
flag.color("white")
flag.begin_fill()
for i in range(2):
    flag.forward(600)
    flag.left(90)
    flag.forward(400)
    flag.left(90)
flag.end_fill()

# Draw the red circle
flag.penup()
flag.goto(0,-70)
flag.pendown()
flag.color("red")
flag.begin_fill()
flag.circle(70)
flag.end_fill()

# Keep the screen open until clicked
turtle.exitonclick()