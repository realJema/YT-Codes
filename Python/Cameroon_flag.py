'''
name: Cameroon_flag.py
author: realjema
date: 01/2023
description: Drawing the cameroonian flag in python :)
'''

import turtle 

def draw_bands():
    # set up turtle 
    turtle.penup()
    turtle.goto(-300, 150)
    turtle.pendown()
    turtle.speed(10)

    # Draw green band 
    turtle.color("green")
    turtle.begin_fill()
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(300)
    turtle.end_fill()
    turtle.right(90)
    turtle.forward(200)

    # Draw red band 
    turtle.color("red")
    turtle.begin_fill()
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(300)
    turtle.end_fill()
    turtle.right(90)
    turtle.forward(200)

    # Draw yellow band 
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(300)
    turtle.end_fill()
    turtle.right(90)
    turtle.forward(200)

    # Draw the yellow star
    turtle.penup()
    turtle.goto(-40, 15)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("yellow")
    for i in range(5):
        turtle.forward(90)
        turtle.right(144)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-300, 150)
    turtle.pendown()


    turtle.exitonclick()

draw_bands()