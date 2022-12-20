# design 2
# Python cool design proram

from turtle import *
t = Turtle()
t.speed(-1000)
def draw(x):
    t.right(10)
    for i in range(4):
        t.forward(x)
        t.right(90)
        t.forward(x)


x = 100
for j in range(10):
    for i in range(36):
        draw(x)
    x -=10
done()