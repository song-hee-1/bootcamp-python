import turtle as t

# 1. Draw a Squre
tim = t.Turtle()

for _ in range(4):
    tim.forward(100)
    tim.left(90)

# 2. Draw a Dashed Line
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()