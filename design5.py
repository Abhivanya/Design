# design 5
# Python cool design proram

from turtle import *

speed(0)
pensize(4)
fillcolor('cyan')
begin_fill()
for i in range(20):
    for j in range(28):
        forward(25)
        left(360/28)
    left(360/20)

end_fill()
mainloop()
done()