import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import numpy as np

import pyglet
import pygame


screen_width = 640
screen_height = 480


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




def arrange_map(map_arrangment):
	p1, p2, p3, p4, p5, p6 = map_arrangment
	out = p1[0:6] + p2[0:6] + p1[6:12] + p2[6:12] + p1[12:18] + p2[12:18] + p3[0:6] + p4[0:6] + p3[6:12] + p4[6:12] + p3[12:18] + p4[12:18] + p5[0:6] + p6[0:6] + p5[6:12] + p6[6:12] + p5[12:18] + p6[12:18]
	return 	out

map_arrangment = [	map_piece_4[::-1], map_piece_1[::-1], map_piece_2[::-1],
					map_piece_6[::-1], map_piece_3, map_piece_5[::-1]]

some_map = arrange_map(map_arrangment)





def hexagon(x, y, k=10):
	t = (3**0.5)/2
	out = [-0.5, t, 0.5, t, 1,0, 0.5,-t, -0.5,-t, -1,0]
	out = [int(k*xy + x) if i%2==0 else int(k*xy + y) for i, xy in enumerate(out)]
	return [(out[x], out[x+1]) for x in range(0, len(out), 2)]


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
done = False

white = 	(255)*3
black = 	[0]*3
green = 	[0, 255, 0]
blue = 		[0, 0, 255]
yellow = 	[255, 255, 0]
gray = 		[211, 211, 211]
violet = 	[238, 130, 238]

color = [blue, gray, green, violet, yellow]

clock = pygame.time.Clock()
 
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("Exiting...")
			done = True

        
	screen.fill((0, 0, 0))


	# coord = [[(i%12), 2*(i//12), (i%2==0)] for i in range(108)]
	coord = [[(i%12), (i//12), (i%2)] for i in range(108)]

	# hcoord = [c[0] for c in coord]
	hcoord = [1.5*c[0] for c in coord]
	# vcoord = [2 * np.sin(np.radians(60)) * (c[1] - c[2]) /3 for c in coord]
	vcoord = [2 * np.sin(np.radians(60)) * c[1] + c[2]*np.sin(np.radians(60)) for c in coord]
	colors = [color[i-1] for i in some_map]


	for x, y, c in zip(hcoord, vcoord, colors):
		scale_map = 30
		map_size_x, map_size_y = (11*1.5)*scale_map, scale_map*(8*3**0.5+3**0.5/2)
		x = scale_map*x + screen_width//2 - map_size_x//2
		y = scale_map*y + screen_height//2 - map_size_y//2
		pygame.draw.polygon(screen, c, hexagon(x, y, scale_map))

	pygame.display.flip()
	clock.tick(60)



# window = pyglet.window.Window()


# def hexagon(x, y, k=10):
# 	t = (3**0.5)/2
# 	out = [-0.5, t, 0.5, t, 1,0, -0.5,t, 1,0, 0.5,-t, -0.5,t, 0.5,-t, -0.5,-t, -0.5,t, -0.5,-t, -1,0]
# 	out = [int(k*xy + x) if i%2==0 else int(k*xy + y) for i, xy in enumerate(out)]
# 	return out

# white = 	[255]*4
# black = 	[0]*3 + [255]
# green = 	[0, 255, 0, 255]
# blue = 		[0, 0, 255, 255]
# yellow = 	[255, 255, 0, 255]
# gray = 		[211, 211, 211, 255]
# violet = 	[238, 130, 238, 255]

# color = [blue, gray, green, violet, yellow]

# coord = [[(i%12), -2*(i//12), (i%2)] for i in range(108)]

# hcoord = [c[0] for c in coord]
# vcoord = [2. * np.sin(np.radians(60)) * (c[1] - c[2]) /3. for c in coord]
# colors = [color[i-1] for i in some_map]

# batch = pyglet.graphics.Batch()


# for x, y, c in zip(hcoord, vcoord, colors):
# 	batch.add(12, pyglet.gl.GL_TRIANGLES, None, ('v2i', hexagon(20*x + window.width//2, 20*y + window.height//2, 10)), ('c4B', c*12))
# 	# print(hexagon(20*x + window.width//2, 20*y + window.height//2, 20))

# # batch.add(12, pyglet.gl.GL_TRIANGLES, None, ('v2i', [290, 277, 310,277, 320,260,  290,277, 320,260, 310,242,   290,277, 310,242, 290,242,   290,277, 290,242, 280,260]), ('c4B', blue*12))
# # batch.add(6, pyglet.gl.GL_TRIANGLES, None, ('v2i', [330, 237,	350, 237,  360, 220,   350, 202,   330, 202,   320, 220]), ('c4B', gray*6))

# @window.event
# def on_draw():
#     window.clear()
#     batch.draw()


# pyglet.app.run()












# Looked it up here https://stackoverflow.com/questions/46525981/how-to-plot-
# x-y-z-coordinates-in-the-shape-of-a-hexagonal-grid
# Just for testing the map

# fig, ax = plt.subplots(1)
# ax.set_aspect('equal')
# coord = [[(i%12), -2*(i//12), (i%2)] for i in range(108)]
# # print(coord)
# # Horizontal cartesian coords
# hcoord = [c[0] for c in coord]
# # Vertical cartersian coords
# vcoord = [2. * np.sin(np.radians(60)) * (c[1] - c[2]) /3. for c in coord]
# colors = [color[i-1] for i in some_map]
# for x, y, c in zip(hcoord, vcoord, colors):
#     color = c[0]
#     hexa = RegularPolygon((x, y), numVertices=6, radius=2. / 3., 
#                          orientation=np.radians(30), 
#                          facecolor=color, alpha=0.2, edgecolor='k')
#     ax.add_patch(hexa)

# ax.scatter(hcoord, vcoord, c=['white' for c in colors],  alpha=0.5)
# plt.axis('off')
# plt.show()