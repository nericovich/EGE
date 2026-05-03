from turtle import *
tracer(0)
k=20

rt(30)
for i in range(3):
    rt(45)
    fd(4*k)
    rt(45)
rt(315)
fd(4*k)
for _ in range(2):
    rt(90)
    fd(4*k)

up()
for x in range(-30,40):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(4
            ,"red")
update()
done()