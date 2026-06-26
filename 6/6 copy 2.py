from email.contentmanager import raw_data_manager
from turtle import *
tracer(0)
k=10
screensize(2000, 2000)

for _ in range(9):
    fd(7*k)
    rt(90)
    fd(42*k)
    rt(90)
up()
back(10*k)
lt(90)
back(16*k)
down()
for _ in range(9):
    fd(42*k)
    rt(90)
    fd(16*k)
    rt(90)

up()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x*k,y*k)
        dot(4,"red")
update()
done()