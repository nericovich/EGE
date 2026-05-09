from turtle import *
tracer(0)
k=10
screensize(2000, 2000)

for _ in range(7):
    fd(78*k)
    rt(90)
    fd(51*k)
    rt(90)
up()
rt(90)
fd(18*k)
rt(90)
fd(6*k)
down()
for _ in range(3):
    rt(90)
    fd(22*k)
    rt(90)
    fd(44*k)
up()
for x in range(-55,100):
    for y in range(-55,100):
        goto(x*k,y*k)
        dot(4,"red")
update()
done()