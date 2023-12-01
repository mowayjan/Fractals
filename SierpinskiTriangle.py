# Sierpinski triangle
import turtle as t
from random import randint

t.speed(0)
t.hideturtle()
t.tracer(0, 0)        # Remove to see animation

def drawpoint(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(2)

x1 = 0
y1 = 255
x2 = -300
y2 = -255
x3 = 300
y3 = -255

ver = [(x1, y1), (x2, y2), (x3, y3)]
for p in ver:
    drawpoint(p[0], p[1])

p = (randint(0, 172), randint(0, 172))
drawpoint(p[0], p[1])

for i in range(100000):
    v = ver[randint(0,2)]
    nextp = ((p[0]+v[0])/2, (p[1]+v[1])/2)
    p = nextp
    drawpoint(p[0], p[1])

t.update()              # Remove to see animation
t.done()
