# design 12
# Python cool design proram

from turtle import *

def r(x,y):
    rt(x)
    fd(y)

tracer(4)
fd(100)
bgcolor('black')
color('white')
width(3)

for i in range(150):
    fd(i)
    r(270,i)
    r(90,i)
    r(90,i)
    r(90,i)
    circle(90,100)

done()