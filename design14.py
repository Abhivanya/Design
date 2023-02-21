# design 14
# Python cool design proram

from turtle import *

def r(x,y):
    rt(x)
    fd(y)

tracer(4)
fd(10)
bgcolor('black')
color('pink')
width(5)

for i in range(150):
    fd(i)
    r(90,i)
    r(90,i)
    r(90,i)
    r(90,i)
    circle(90,100)

done()