import math
from turtle import*
import colorsys
def hearta(k) :
    return 15 * math.sin(k) ** 3
def heartb(k) :
    return 12 * math.cos(k) - 5 * \
    math.cos(2 * k) - 2 * \
    math.cos(3 * k) - \
    math.cos(4 * k)
speed (500)
bgcolor('black')
tracer (10)
h = 0  # start color
pensize(2)
for i in range(50000):
    goto(hearta(i)*20, heartb(i)*20)

    goto(0,0)

    #rainbow color
    c = colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h += 0.001
    if h > 1:
        h = 0

update()
done()

