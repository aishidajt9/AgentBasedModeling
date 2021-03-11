import turtle
import random

n_turtles = 10
wn = turtle.Screen()

kames = [turtle.Turtle() for i in range(n_turtles - 1)]

for t in kames:
    t.shape('turtle')
    t.color('green')
    t.speed(0)
    t.goto(random.randrange(-100, 100), random.randrange(-100, 100))

def random_walk(ts, steps):
    for steps in range(steps):
        for t in ts:
            t.forward(random.randrange(0, 50))
            t.right(random.randrange(0,180))

random_walk(kames, 100)

wn.exitonclick()