# design 17
# Python cool design proram

from turtle import *

t = Turtle()
t.color('purple','pink')
t.speed(0)
x=10
for i in range(20):
    t.circle(x)
    x+=10
t.right(180)
x=10
for i in range(20):
    t.circle(x)
    x+=10
t.right(90)
x=10
for i in range(20):
    t.circle(x)
    x+=10
t.right(-180)
x=10
for i in range(20):
    t.circle(x)
    x+=10
done()
    