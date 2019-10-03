from turtle import *
hey = Turtle()

bg = Screen()
bg.setup(600,600)
bg.bgcolor("black")

colors = ["magenta", "cyan", "orange", "white", "yellow"]

import random

hey.speed(200)
hey.hideturtle()
hey.up()

def draw_candy(x, y, width, radius):
    hey.goto(x, y)
    hey.down()
    hey.width(width)

    for i in range(125):
        colorchoice = random.choice(colors)
        hey.color(colorchoice)
        hey.forward(radius*2)
        hey.right(181)

    hey.up()

for i in range(30):
    draw_candy(random.randint(-300, 300),
               random.randint(-300, 300),
               73,
               random.randint(50, 100))
