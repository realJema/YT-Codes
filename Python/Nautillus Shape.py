# Drawing the Nautillus shape with python turtle 

import turtle 

size=1
turtle.speed(200)
turtle.bgcolor('black')
turtle.pencolor('white')

while(True):
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
        size=size + 1
    turtle.right(10)