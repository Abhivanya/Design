# design 15
# Python cool design proram

#  *************************** Python Logo  **********************

from turtle import *

def gt(x,y):
    penup()
    goto(x,y)
    pendown()

def c3():
    for i in range(90):
        right(1)
        forward(1)

def c1():
    circle(58,90)

def c2(x=80):
    c1()
    forward(x)
    c1()

def h():
    begin_fill()
    forward(50)
    c1()
    fd(90)
    c2()
    fd(40)
    left(90)
    fd(80)
    right(90)
    fd(10)
    right(90)
    fd(120)
    c2(90)
    fd(30)
    left(90)
    fd(50)
    c3()
    forward(40)
    seth(180)
    end_fill()

def dots(x,y):
    pu()
    goto(x,y)
    dot(35)

color('#306998')
h()
gt(19.79,-11.21)
color('#FFD43D')
h()
color('white')
dots(-50,150)
dots(70,-160)
done()
