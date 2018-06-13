__author__ = 'Chirag'

import turtle

def draw_art():
    window = turtle.Screen()
    print(type(window))
    window.bgcolor("red")

    brian = turtle.Turtle()
    print(type(brian))
    brian.shape("classic")
    brian.color("white")
    brian.speed(100)

    for n in range(1,46):
        brian.circle(100)
        brian.right(8)

    window.exitonclick()

draw_art()
