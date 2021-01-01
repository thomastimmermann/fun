#!/usr/bin/env python3

import turtle

silly = turtle.Turtle()


k = 0


def koch(n, size):
    if n == 0:
        global k
        print(k)
        k = k + 1
        silly.forward(size)
        return
    size = size / 3
    koch(n - 1, size)
    silly.left(60)
    koch(n - 1, size)
    silly.right(120)
    koch(n - 1, size)
    silly.left(60)
    koch(n - 1, size)


def sierpinski(n, size):
    for i in range(3):
        if n == 0:
            silly.forward(size)
        else:
            sierpinski(n - 1, size / 2)
            silly.penup()
            silly.forward(size)
            silly.pendown()
        silly.left(120)


colors = ["green", "yellow", "blue", "red"]
silly.speed(0)


def fun():
    for i in range(200):
        step = (i % 7) * 7 + 1
        print(i)
        silly.pencolor(colors[i % len(colors)])
        silly.forward(step)
        silly.left(333)
        silly.forward(step)
        silly.right(111)
        silly.forward(step)
        silly.left(333)
        silly.backward


sierpinski(6, 400)
