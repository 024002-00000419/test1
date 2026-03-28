a = [[],[]]
for s in open("text"):
    x,y = [float(i) for i in s.split()]
    if y>0: a[0].append([x,y])
    else: a[1].append([x,y])
from turtle import *
tracer(0)
up()
for x,y in a[0]:
    goto(x*20,y*20)
    dot(5,"blue")
for x,y in a[0]:
    goto(x*20,y*20)
    dot(5)
done()
