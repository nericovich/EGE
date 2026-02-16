from turtle import * 
tracer(0)
k = 20
rt(90)
for _ in range(3):
    fd(15*k)
    rt(90)
    fd(20*k)
    rt(90)
up()
fd(7*k)
rt(90)
fd(13*k)
lt(90)
down()
for _ in range(2):
    fd(10*k)
    lt(90)
    fd(17*k)
    lt(90)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*k, y*k)
        dot(4, 'red')

update()
done()