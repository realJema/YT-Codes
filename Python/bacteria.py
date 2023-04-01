# drawing a bacteria using turtle program 

from turtle import Turtle, Screen 

s = Screen()
s.bgcolor("black")
s.title('Bacteria')

sketch_pen = Turtle()
sketch_pen.pencolor("red")
sketch_pen.speed(0)
sketch_pen.pensize(1)


sketch_pen.speed("fastest")

length, angle = 0 , 0
sketch_pen.penup()
sketch_pen.goto(0,100)
sketch_pen.pendown()

while(True): 
    sketch_pen.forward(length)
    sketch_pen.right(angle)
    length+=1
    angle+=0.5

    sketch_pen.hideturtle()
    
    s.exitonclick()

sketch_pen.hideturtle()
s.exitonclick()