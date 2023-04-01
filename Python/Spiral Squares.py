# Drawing a spiral of squares with turtle program 

import turtle 
import random 

size=1
turtle.speed(200)

#creating hex codes for color change 
paletteMaker = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
color = []
turtle.bgcolor('black')
while len(color) < 24:
    if (col := ''.join(['#', *random.choices(paletteMaker, k = 6)])) not in color:
        color.append(col) 

while(True):
    turtle.forward(size)
    turtle.right(91)
    turtle.color(color[random.randint(0,23)], color[random.randint(0,23)])
    size = size +1