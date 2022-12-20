# design 1
# Python cool design proram

import turtle as tu
import colorsys

tu.Screen().bgcolor('black')
t = tu.Turtle()
h = 0.3

def fun(len, ang=0, cl="#000000",c='black'):
    # if you want to increase the speed of brush then uncomment the line
    #t.speed(8)
    
    t.seth(ang)
    t.fillcolor(cl)
    t.begin_fill()
    t.forward(len)
    t.seth(60+ang)
    t.forward((73/200)*len)
    t.seth(150+ang)
    t.forward((73/200)*len)
    t.seth(210+ang)
    t.forward(len)
    t.end_fill()

    t.fillcolor(c)
    t.begin_fill()
    t.seth(ang+0.01)
    t.forward(len/2)
    t.circle((13/200)*len,180)
    t.seth(30+ang)
    t.circle((14/200)*len,180)
    t.forward(len/2)
    t.end_fill()

for i in range(12):
    c = colorsys.hsv_to_rgb(h,1,1)
    cl = colorsys.hsv_to_rgb(h+0.5,1,1)
    t.pencolor(c)
    fun(280,i*30,c,cl)
    h += 0.15

# tu.done() comment out if you want to make output screen to wait after execution