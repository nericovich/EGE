from turtle import *
tracer(0)
k=20
for i in range(2):
    fd(25*k)
    lt(270)
    fd(17*k)
    rt(90)
up()
fd(12*k)
rt(90)
fd(9*k)
lt(90)
down()
for _ in range(2):
    fd(19*k)
    rt(90)
    fd(11*k)
    rt(90)

up()
for x in range(-30,40):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(4,"red")
update()
done()