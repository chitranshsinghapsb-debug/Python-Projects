import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########
direction = 0
tim.speed("fastest")

while direction < 360:
    tim.color(random_color())
    tim.setheading(direction)
    tim.circle(100)
    direction+=3

s = t.Screen()
s.exitonclick()