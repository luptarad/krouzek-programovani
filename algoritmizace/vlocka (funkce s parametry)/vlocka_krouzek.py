from turtle import *
color("blue")
shape("turtle")
speed(100)
pencolor("white")
pensize(6)

Screen().bgcolor("orange")


def vTvar():
    right(25)
    forward(50)
    backward(50)
    left(50)
    forward(50)
    backward(50)
    right(25)

def ramenoVlocky():
    for x in range(0,4):
        forward(30)
        vTvar()
    backward(120)

import random
colours = ["blue", "purple", "cyan", "white", "yellow"]

def vlocka():
    for x in range(0,6):
        color(random.choice(colours))
        ramenoVlocky()
        right(60)

vlocka()

