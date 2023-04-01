'''
name: Nigerian_flag.py
author: realjema
date: 02/2023
description: Drawing the nigerian flag in python :)
'''

import turtle 

turtle.Screen().colormode(255)
turtle.Screen().bgcolor(135,206,235)

def draw_bands():
    #set up turtle 
    turtle.penup()
    turtle.goto(-300, 150)
    turtle.pendown()
    turtle.speed(10)

    # Draw green band 
    turtle.color(5, 133, 76)
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

    # Draw white band 
    turtle.color("white")
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

     # Draw green band 
    turtle.color(5, 133, 76)
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

    turtle.exitonclick()

draw_bands()