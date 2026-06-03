# import colorgram

# rgb_colors = []
# colors = colorgram.extract('day_18_project/image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
import turtle as t
import random

tim = t.Turtle()
s = t.Screen()
t.colormode(255)
# colors = [
#     (202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), 
#     (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), 
#     (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), 
#     (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), 
#     (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), 
#     (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), 
#     (176, 192, 208), (168, 99, 102)
# ]
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
tim.speed("fastest")
tim.teleport(-275,-275)

def next_coloumn():
    y = tim.ycor()
    y += 60
    tim.teleport(-275,y)

for _ in range(10):   
    for i in range(10):
        tim.dot(20,random_color())
        tim.penup()
        tim.forward(60)
        tim.pendown
    next_coloumn()


s.exitonclick()