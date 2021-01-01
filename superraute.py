import turtle
import math


colors = ["green", "purple", "blue"]


def raute(size, winkel):
    global colors
    turtle.right(winkel / 2.0)
    for w in [winkel, 180 - winkel, winkel, 180 - winkel / 2.0]:
        turtle.pencolor(colors[0])
        colors = colors[1:] + [colors[0]]
        turtle.forward(size)
        turtle.left(w)


def timmer_raute(n, size, winkel):
    for i in range(n):
        raute(size, winkel)
        turtle.right(winkel / 2.0)
        turtle.forward(size)
        turtle.left((180 + winkel) / 2.0)
        size *= math.tan(math.pi / 360 * winkel)


def unter_raute(n, size, winkel):
    turtle.right(winkel / 2.0)
    turtle.forward(size)
    turtle.left(winkel / 2.0)
    turtle.left(90)
    super_raute(n - 1, size * math.tan(math.pi / 360 * winkel), winkel)
    turtle.right(90)
    turtle.right(winkel / 2.0)
    turtle.backward(size)
    turtle.left(winkel / 2.0)


def super_raute(n, size, winkel):
    raute(size, winkel)
    if n > 0:
        size /= 2
        unter_raute(n, size, winkel)
        turtle.right(winkel / 2.0)
        turtle.forward(size)
        turtle.left(winkel / 2.0)
        unter_raute(n, size, winkel)
        raute(size, winkel)
        turtle.left(winkel / 2.0)
        turtle.forward(size)
        turtle.right(winkel / 2.0)
        unter_raute(n, size, winkel)
        raute(size, winkel)
        turtle.right(winkel / 2.0)
        turtle.backward(size)
        turtle.left(winkel / 2.0)
        unter_raute(n, size, winkel)
        raute(size, winkel)
        turtle.left(winkel / 2.0)
        turtle.backward(size)
        turtle.right(winkel / 2.0)


turtle.speed(0)
super_raute(3, 200, 75)
