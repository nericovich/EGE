from turtle import *
tracer(0)
 #speed 10
k = 15

screensize(3500, 2500)
right(315)
for _ in range(7):
    fd(72 *k) # forward(x)
    rt(45) #right(x)
    fd(43*k)
    rt(135)

up() # down()

for x in range(-30, 100):
    for y in range(-30, 100):
        goto(x * k, y * k)
        dot(4, 'red')

update()
done()