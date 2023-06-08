''' 
import turtle as t 
import colorsys as cs 

t.setup(640, 640)
t.bgcolor('black')
t.pencolor('white')
t.tracer(50) 

t.up()
t.rt(90)
t.fd(150)
t.lt(180)
t.down()

def tree(b1,b2,c):
    if c<0:
        return 
    t.color(cs.hls_to_rgb(c/11,0.6,1))
    t.pensize(c+1)
    t.fd(c*8)
    p=t.pos()
    h=t.heading()
    t.lt(b1)
    tree(b1,b2,c-1)
    t.up()
    t.goto(p)
    t.seth(h)
    t.rt(b2)
    t.down()
    tree(b1,b2,c-1)

tree(19,19,10)
t.done()

from turtle import * 
import colorsys 

tracer(100)
bgcolor('black')
pensize(4)
h=0

for i in range(400):
    c=colorsys.hsv_to_rgb(h,1,1)
    h +=0.005
    color('black')
    fillcolor(c)
    begin_fill()
    rt(46.5)
    fd(i)
    circle(20,180)
    end_fill()
    circle(i,21)
done()

from turtle import * 

speed(0)
bgcolor('black')
color('cyan')
pensize(2)

for i in range(160):
    for j in range(4):
        fd(i)
        rt(20)
        rt(60)
    rt(120)

done()

'''

from turtle import * 
import colorsys

speed(0)
bgcolor('black')
h=0.6
pensize(2)

for i in range(300):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.005
    for j in range(2):
        fd(i*j*2)
        lt(91)

done()