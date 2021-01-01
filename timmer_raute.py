#!/usr/bin/env python3

import turtle
import math


def raute(size, winkel):
    turtle.right(winkel / 2.0)
    for w in [winkel, 180 - winkel, winkel, 180 - winkel / 2.0]:
        turtle.forward(size)
        turtle.left(w)


def timmer_raute(n, size, winkel):
    for i in range(n):
        raute(size, winkel)
        turtle.right(winkel / 2.0)
        turtle.forward(size)
        turtle.left((180 + winkel) / 2.0)
        size *= math.tan(math.pi / 360 * winkel)


turtle.speed(0)
timmer_raute(40, 200, 87)

turtle.done()
