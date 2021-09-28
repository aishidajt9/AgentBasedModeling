#%%
import turtle
# https://docs.python.org/ja/3/library/turtle.html

# %%
# screen instance
wn = turtle.Screen()

# %%
# making an instance
t = turtle.Turtle()
print(t)
print(t.position(), t.heading())


#%%
t.shape("turtle")
t.color("green")

# %%
# define Kame class inheriting Turtle class
class Kame(turtle.Turtle):
    def __init__(self, x, y, color):
        super().__init__(shape="turtle")
        
        self.setposition(x, y)
        self.color(color)
        self.pencolor(color)
    
    def dance(self):
        self.right(45)
        self.left(45)
        self.forward(20)
        self.back(20)

# %%
k = Kame(10, 10, "red")

# %%
k.right(45)
k.forward(50)

# %%
for i in range(10):
    k.dance()

# %%
wn.exitonclick()
# %%
