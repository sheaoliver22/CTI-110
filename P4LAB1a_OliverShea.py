# Shea Oliver
# 10/28/2024
# P4LAB1
# Draw turtle graphics with loops

import turtle
win = turtle.Screen()
t = turtle.Turtle()

t.pensize(4)
t.pencolor("orange")
t.shape("arrow")

#for loop to draw 3 sides of triangle
for i in range(3):
    t.forward(100)
    t.left(120)


#While loop to draw 4 sides of square
line = 0
while line <=3:
    line +=1
    t.forward(100)
    t.right(90)


