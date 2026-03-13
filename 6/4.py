from turtle import *

k = 20
tracer(0)
screensize(2000,2000)
for _ in range(6):
    fd(33*k)
    rt(90)
    fd(20*k)
    rt(90)

up()
fd(3*k)
rt(90)
fd(9*k)
lt(90)
down()
for _ in range(6):
    fd(24*k)
    rt(90)
    fd(25*k)
    rt(90)

up()
for x in range(-30,40):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(4,"red")
update()
done()