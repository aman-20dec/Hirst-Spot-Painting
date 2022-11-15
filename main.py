#########To extract the colors from a painting##############
# import colorgram
# hirst_colors = colorgram.extract("hirst_painting.jpg", 30)
# colors = []
# for color in hirst_colors:
#     colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
#############################################################

from turtle import Turtle, Screen, screensize
import random

screen = Screen()
ninja = Turtle()

x = -230
y = -230
grid_size = 10


hirst_colors = [  (198, 159, 116), (70, 92, 129), (147, 85, 53), (218, 210, 116), (138, 160, 191), (178, 160, 38), (184, 146, 164), (28, 32, 46), (58, 34, 23), (120, 70, 93), (139, 175, 154), (77, 115, 79), (143, 25, 16), (186, 97, 82), (61, 31, 42), (121, 27, 41), (45, 58, 94), (177, 96, 114), (102, 119, 170), (34, 52, 45), (100, 160, 85), (214, 175, 192), (216, 181, 173), (160, 209, 191), (67, 86, 23), (219, 206, 8)]



def init_turtle():
    screen.colormode(255)
    ninja.hideturtle()
    ninja.penup()
    ninja.speed("fastest")
    

init_turtle()
ninja.setpos(x,y)

for _ in range(grid_size):
    for _ in range(grid_size):        
        ninja.dot(25, random.choice(hirst_colors))       
        ninja.forward(50)

    y += 50
    ninja.setpos(x,y)



screen.exitonclick()







