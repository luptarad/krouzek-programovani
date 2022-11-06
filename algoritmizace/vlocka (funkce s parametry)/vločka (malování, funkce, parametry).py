from turtle import *
color("blue")
shape("turtle")
speed(100)
pencolor("white")
pensize(6)

Screen().bgcolor("turquoise")


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


def vlocka():
    for x in range(0,6):
        ramenoVlocky()
        right(60)

def vlockaHusta():
    for x in range(0,18):
        ramenoVlocky()
        right(20)


#vlocka()

#barvy: https://cs111.wellesley.edu/labs/lab02/colors
import random
colours = ["blue", "purple", "cyan", "white", "yellow", "green", "orange"]



def vlockaBarevna():
    for x in range(0,6):
        color(random.choice(colours))
        ramenoVlocky()
        right(60)

#vlockaBarevna()


def vTvarSParametrem(velikost):
    right(25)
    forward(velikost)
    backward(velikost)
    left(50)
    forward(velikost)
    backward(velikost)
    right(25)

def ramenoVlockySParametrem(velikost):
    for x in range(0,4):
        forward(velikost)
        vTvarSParametrem(velikost)
    backward(velikost*4)


def vlockaSParametrem(velikost):
    for x in range(0,6):
        color(random.choice(colours))
        ramenoVlockySParametrem(velikost)
        right(60)


#vlockaSParametrem(20)


#hlavni program
pensize(3)
for i in range(0,10):
    velikost = random.randint(5,30)
    x = random.randint(-400,400)
    y = random.randint(-400,400)
    penup()
    goto(x,y)
    pendown()
    vlockaSParametrem(velikost)

