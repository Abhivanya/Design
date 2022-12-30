# design 11
# Python cool design proram

from turtle import *

def r(x,y):
    rt(x)
    fd(y)

tracer(4)
fd(100)
bgcolor('black')
color('yellow')
width(3)

for i in range(2000):
    fd(i)
    r(90,i)
    r(90,i)
    r(270,i)
    r(90,i)
    circle(90,100)

done()