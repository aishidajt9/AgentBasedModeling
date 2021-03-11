from turtle import *

shape('turtle')
speed(0)
color('red', 'green')

def square():
    for i in range(4):
        forward(100)
        right(90)

for i in range(60):
    right(5)
    square()

done()

# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()