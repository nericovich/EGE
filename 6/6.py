from turtle import *
tracer(0)
k=20
screensize(2000, 2000)
rt(315)
for _ in range(7):
    fd(7*k)
    rt(45)
    fd(8*k)
    rt(135)


up()
for x in range(-30,40):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(4,"red")
update()
done()