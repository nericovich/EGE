from turtle import *
screensize(2000,2000)
tracer(0)
k = 15
for _ in range(3):
    fd(31 * k)
    lt(90)
    fd(14*k)
    lt(90)

up()
fd(-4*k)
rt(90)
fd(6*k)
lt(90)
down()
for _ in range(3):
    fd(11*k)
    lt(90)
    fd(77*k)
    lt(90)

up()
for x in range(-30,70):
    for y in range(-90,90):
        goto(x*k,y*k)
        dot(4,"red")

update()
done()