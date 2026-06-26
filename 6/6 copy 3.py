from turtle import *
tracer(0)
k=10
screensize(2000, 2000)

for _ in range(5):
    fd(29*k)
    rt(90)
    fd(27*k)
    rt(90)
up()
fd(3*k)
rt(90)
fd(9*k)
lt(90)
down()
for _ in range(5):
    fd(72*k)
    rt(90)
    fd(95*k)
    rt(90)
up()
for x in range(-55,100):
    for y in range(-55,100):
        goto(x*k,y*k)
        dot(4,"red")
update()
done()