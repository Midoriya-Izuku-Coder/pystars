import turtle as t
from random import randint, random
t.speed(0)
t.hideturtle()
def draw_star(size, points, x, y, col):
    angle = 180 - (180 / points)

    t.color(col)
    t.penup()
    t.goto(x,y)
    t.pendown()

    t.begin_fill()


    for i in range (points):
        t.forward(size)
        t.right(angle)
        
    t.end_fill()

t.Screen().bgcolor('black')

while True:
    ranSize = randint(10,50)
    ranPts = randint(2,11) * 2 + 1
    ranX = randint(-500, 500)
    ranY = randint(-400, 400)
    ranColor = (random(), random(), random())
    draw_star(ranSize, ranPts, ranX, ranY, ranColor)
