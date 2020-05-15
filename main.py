import numpy as np

import pyglet
import pygame


screen_width = 640
screen_height = 480

# Codes for terrarian type:
# 	"water":	1,
# 	"mountain":	2,
# 	"forest":	3,
# 	"swamp":	4,
# 	"desert":	5


# Hardcoded map pieces, later would add a scanner
map_piece_1 = [1, 1, 1, 1, 3, 3,    4, 4, 1, 5, 3, 3,    4, 4, 5, 5, 5, 3]
map_piece_2 = [5, 3, 3, 3, 3, 3,    4, 4, 3, 5, 5, 5,    4, 2, 2, 2, 2, 5]
map_piece_3 = [4, 4, 3, 3, 3, 1,    4, 4, 3, 2, 1, 1,    2, 2, 2, 2, 1, 1]
map_piece_4 = [5, 5, 2, 2, 2, 2,    5, 5, 2, 1, 1, 1,    5, 5, 5, 3, 3, 3]
map_piece_5 = [4, 4, 4, 2, 2, 2,    4, 5, 5, 1, 2, 2,    5, 5, 1, 1, 1, 1]
map_piece_6 = [5, 5, 4, 4, 4, 3,    2, 2, 4, 4, 3, 3,    2, 1, 1, 1, 1, 3]

# function to combine map correctly from separete pieces
def arrange_map(map_arrangment):
	p1, p2, p3, p4, p5, p6 = map_arrangment
	out = p1[0:6] + p2[0:6] + p1[6:12] + p2[6:12] + p1[12:18] + p2[12:18] + p3[0:6] + p4[0:6] + p3[6:12] + p4[6:12] + p3[12:18] + p4[12:18] + p5[0:6] + p6[0:6] + p5[6:12] + p6[6:12] + p5[12:18] + p6[12:18]
	return 	out

# specification of map, some pieces are upside down, so they are passed backwards
map_arrangment = [	map_piece_4[::-1], map_piece_1[::-1], map_piece_2[::-1],
					map_piece_6[::-1], map_piece_3, map_piece_5[::-1]]

some_map = arrange_map(map_arrangment)


# function to draw a hexagon, x and y are cenral coordinate, k - radius of outer circle.
def hexagon(x, y, k=10):
	t = (3**0.5)/2
	out = [-0.5, t, 0.5, t, 1,0, 0.5,-t, -0.5,-t, -1,0]
	out = [int(k*xy + x) if i%2==0 else int(k*xy + y) for i, xy in enumerate(out)]
	return [(out[x], out[x+1]) for x in range(0, len(out), 2)]


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
done = False

white =		(255)*3
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
			print("Exiting pygame loop")
			done = True


	screen.fill((0, 0, 0))
	mouse_x, mouse_y = pygame.mouse.get_pos()
	# probably window will be scalable, so I left next 2 lines in a loop
	scale_map = 30
	map_size_x, map_size_y = (11*1.5)*scale_map, scale_map*(8*3**0.5+3**0.5/2)


	# a way to find out coordinats for map (9 x 12, overall 108 places)
	coord = [[(i%12), (i//12), (i%2)] for i in range(108)]
	hcoord = [1.5*c[0] for c in coord]
	vcoord = [2 * np.sin(np.radians(60)) * c[1] + c[2]*np.sin(np.radians(60)) for c in coord]
	colors = [color[i-1] for i in some_map]

	# draw all polygons loop
	for x, y, c in zip(hcoord, vcoord, colors):
		x = scale_map*x + screen_width//2 - map_size_x//2
		y = scale_map*y + screen_height//2 - map_size_y//2
		hex_radius = scale_map-3
		distance = ((x-mouse_x)**2 + (y - mouse_y)**2)**.5
		if ((0, 0) != (x, y)) and distance < 3**.5*hex_radius/2:
			c = [255]*3
		pygame.draw.polygon(screen, c, hexagon(x, y, hex_radius))

	pygame.display.flip()
	clock.tick(60)


