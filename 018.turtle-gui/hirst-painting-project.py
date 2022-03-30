# import colorgram
import turtle as t
import random

# rgb_color_list = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color_list.append(new_color)

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

rgb_color_list = [(250, 246, 243), (248, 245, 246), (212, 154, 97), (239, 246, 243), (52, 108, 132), (178, 78, 33),
                  (198, 143, 34),
                  (123, 80, 97), (235, 240, 244), (116, 155, 171), (124, 175, 158), (228, 197, 129), (194, 85, 105),
                  (54, 38, 20),
                  (12, 51, 65), (189, 123, 142), (54, 120, 115), (41, 169, 126), (167, 21, 31), (225, 94, 78),
                  (4, 30, 28), (39, 32,
                                34), (243, 163, 159), (81, 148, 168), (164, 27, 22), (239, 163, 167), (104, 123, 159),
                  (164, 209, 193), (21, 81,
                                    93), (29, 85, 81)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

num_of_dots = 100

for do_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(rgb_color_list))
    tim.forward(50)

    if do_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
