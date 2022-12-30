# # design 16
# Python cool design proram

import turtle as s

s.bgcolor('black')
colors=('cyan', 'pink','cyan','pink')
s.speed(0)
for i in range(60):
    s.pencolor(colors[i%4])
    s.width(2)
    s.forward(i)
    s.circle(90,steps=4)
    s.fd(i)
    s.right(45)

s.hideturtle()
s.done()