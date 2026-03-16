from re import L
from turtle import *
tracer(0)
k = 20
for _ in range(2):
    fd(k)
    lt(270)
    fd(16*k)
    rt(90)
up()
back(4*k)
rt(90)
fd(10*k)
lt(90)
down()
for i in range(2):
    fd(17*k)
    rt(90)
    fd(7*k)
    rt(90)

up()
for x in range(-60,40):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(4,"red")
update()
done()