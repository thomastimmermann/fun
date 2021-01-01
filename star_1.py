"""Tests."""
import turtle

silly = turtle.Turtle()

silly.speed(0)
turtle.clearscreen()

for i in range(200):
    print(i)
    silly.forward(i * 2)
    silly.right(90)
    silly.forward(i * 1)
    silly.left(145)
    silly.forward(i * 1)
