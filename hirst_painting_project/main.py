# import colorgram

# color_palette = []
# colors = colorgram.extract('image.jpg', 10)

# for color in colors:
#   r = color.rgb.r
#   g = color.rgb.g
#   b = color.rgb.b

#   new_color = (r,g,b)
#   color_palette.append(new_color)

# print(color_palette)
import random
from turtle import Turtle,Screen
import turtle

tim = Turtle()


turtle.colormode(255)
color_list = [(245, 239, 230), (251, 226, 233), (46, 92, 144), (243, 250, 245), (170, 13, 26), (34, 44, 62), (141, 80, 44), (228, 154, 7), (161, 57, 88), (211, 162, 101)]

tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
  tim.dot(20,random.choice(color_list))
  tim.forward(50)

  if dot_count % 10 == 0:
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)




screen = Screen()
screen.exitonclick()