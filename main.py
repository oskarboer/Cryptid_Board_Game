import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import numpy as np

number2type_of_terrarian = {
	"water":	1,
	"mountain":	2,
	"forest":	3,
	"swamp":	4,
	"desert":	5
	}

# color = ["blue", "green", "green", "green", "green"]
color = ["blue", "white", "green", "magenta", "yellow"]


map_piece_1 = [1, 1, 1, 1, 3, 3,    4, 4, 1, 5, 3, 3,    4, 4, 5, 5, 5, 3]

map_piece_2 = [5, 3, 3, 3, 3, 3,    4, 4, 3, 5, 5, 5,    4, 2, 2, 2, 2, 5]

map_piece_3 = [4, 4, 3, 3, 3, 1,    4, 4, 3, 2, 1, 1,    2, 2, 2, 2, 1, 1]

map_piece_4 = [5, 5, 2, 2, 2, 2,    5, 5, 2, 1, 1, 1,    5, 5, 5, 3, 3, 3]

map_piece_5 = [4, 4, 4, 2, 2, 2,    4, 5, 5, 1, 2, 2,    5, 5, 1, 1, 1, 1]

map_piece_6 = [5, 5, 4, 4, 4, 3,    2, 2, 4, 4, 3, 3,    2, 1, 1, 1, 1, 3]


map_arrangment = []


# Looked it up here https://stackoverflow.com/questions/46525981/how-to-plot-
# x-y-z-coordinates-in-the-shape-of-a-hexagonal-grid

fig, ax = plt.subplots(1)
ax.set_aspect('equal')
coord = [[(i%6), -2*(i//6), (i%2)] for i in range(18)]
# print(coord)
# Horizontal cartesian coords
hcoord = [c[0] for c in coord]
# Vertical cartersian coords
vcoord = [2. * np.sin(np.radians(60)) * (c[1] - c[2]) /3. for c in coord]
colors = [color[i-1] for i in map_piece_3]
for x, y, c in zip(hcoord, vcoord, colors):
    color = c[0]
    hexa = RegularPolygon((x, y), numVertices=6, radius=2. / 3., 
                         orientation=np.radians(30), 
                         facecolor=color, alpha=0.2, edgecolor='k')
    ax.add_patch(hexa)

ax.scatter(hcoord, vcoord, c=['white' for c in colors],  alpha=0.5)
plt.axis('off')
plt.show()