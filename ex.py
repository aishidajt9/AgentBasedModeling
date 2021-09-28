#%%
print("hello world")

#%%
for i in range(10):
    print(i)

# %%
ex = {(3, 3), (2,1), (1, 2)}
ex = list(ex)
# %%
((3, 2)[0] - (1, 1)[0]) ** 2
# %%
dist = [(e[0] - 1) ** 2 + (e[1] - 1) ** 2 for e in ex]
dist
# %%
import numpy as np
import random
# %%
ex[np.argmin(dist)]
# %%
# np.where(dist == dist.min())
# %%
min_list = [i for i, x in enumerate(dist) if x == min(dist)]
min_list
# %%
random.choice(min_list)
# %%
ex = ["b","b","b"]
all([e=="b" for e in ex])
# %%
