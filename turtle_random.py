import turtle
import random

n_turtles = 10
wn = turtle.Screen()

kames = [turtle.Turtle() for i in range(n_turtles)]
colours=["red","blue","yellow","brown","black","purple","green"]

for i, t in enumerate(kames):
    t.shape('turtle')
    t.color(colours[i%7])
    t.speed(0)
    t.goto(random.randrange(-100, 100), random.randrange(-100, 100))

def random_walk(ts, steps):
    for steps in range(steps):
        for t in ts:
            t.forward(random.randrange(0, 50))
            t.right(random.randrange(0,180))

random_walk(kames, 100)

wn.exitonclick()