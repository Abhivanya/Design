# design 4
# Python cool design proram

import turtle

wn = turtle.Screen()
wn.bgcolor('#ffdd9a')

t=turtle.Pen()
t.speed(0)
t.color('#0e1e52')
t.width(3)

for i in range(18):
    t.left(20)
    for j in range(50,60,2):
        t.circle(j*2)

turtle.mainloop()
t.done()
