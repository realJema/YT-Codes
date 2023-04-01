'''
name: Graphics.py
author: realjema
date: 01/2023
'''

import random 
import turtle 

colors = ['red', 'cyan', 'pink', 'yellow', 'green', 'orange']
t = turtle.Turtle()
t.speed(50)
turtle.bgcolor("black")
length=100
angle=50
size=5

for i in range(length):
    color=random.choice(colors) # chooses a random color from the array
    t.pencolor(color)
    t.fillcolor(color)
    t.penup()
    t.forward(i+50)
    t.pendown()
    t.left(angle)
    t.begin_fill()
    t.circle(size)
    t.end_fill()

turtle.exitonclick()
turtle.bgcolor("black")
