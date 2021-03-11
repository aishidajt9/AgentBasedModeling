import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import numpy as np

class Agent2:
    """random walking angent
    who avoids other's personal space"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.search_neighbour()
        self.xtjct = [x]
        self.ytjct = [y]

    def search_neighbour(self) -> set:
        """Neumann neighborhood"""
        self.neighbor = {(i, j) for i in [self.x - 1, self.x, self.x + 1] for j in [self.y - 1, self.y, self.y + 1]}

    def search_other_neighbor(self, other_agents):
        """search other agents' neighbors"""
        temp = set()
        for other in other_agents:
            temp = temp.union(other.neighbor)
        self.other_neighbor = temp

    def walk(self):
        """walking with avoiding other agents"""
        temp_x = self.x + random.choice([-1, 0, 1])
        temp_y = self.y + random.choice([-1, 0, 1])
        if (temp_x, temp_y) not in self.other_neighbor:
            self.x, self.y = temp_x, temp_y

    def next_move(self, other_agents):
        self.search_other_neighbor(other_agents)
        self.walk()
        self.search_neighbour()
        self.xtjct.append(self.x)
        self.ytjct.append(self.y)

agents = [Agent2(random.randrange(-10, 10), random.randrange(-10, 10)) for i in range(10)]

fig = plt.figure()
ims = []

colormap = plt.cm.gist_ncar #nipy_spectral, Set1,Paired  
colorst = [colormap(i) for i in np.linspace(0, 0.9,len(agents))]       

for t in range(100):
    # plt.cla()
    for i in range(len(agents)):
        agents[i].next_move(agents[0:i] + agents[(i + 1):len(agents)])

    x = [agents[i].x for i in range(len(agents))]
    y = [agents[i].y for i in range(len(agents))]
    im = plt.scatter(x, y, marker= ".", c = colorst)# c=list(range(len(agents)))
    ims.append([im]) 

ani = animation.ArtistAnimation(fig, ims)
plt.show()

