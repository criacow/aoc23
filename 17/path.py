#!/usr/bin/python3

import sys
from implementation import *

pathmap = []
max_x = 0
for line in sys.stdin:
    pathmap.append(list(line))
    max_x = len(line) - 1
max_y = len(pathmap)

diagram5 = GridWithWeights(max_x, max_y)

for y in range(max_y):
  for x in range(max_x):
#     print(str(y) + " " + str(x) + " " + str(max_y) + " " + str(max_x))
     diagram5.weights[(x, y)] = int(pathmap[y][x])

start, goal = (0, 0), (max_x - 1, max_y - 1)
came_from, cost_so_far = a_star_search(diagram5, start, goal)
#came_from, cost_so_far = dijkstra_search(diagram5, start, goal)
draw_grid(diagram5, point_to=came_from, start=start, goal=goal)
#draw_grid(diagram5, path=came_from, start=start, goal=goal)
print()
#draw_grid(diagram5, path=reconstruct_path(came_from, start=start, goal=goal))
#print(diagram5.weights)
print(came_from)
print(cost_so_far)
print(cost_so_far[(max_x - 1,max_y - 1,"S")])
print(cost_so_far[(max_x - 1,max_y - 1,"E")])
#print(cost_so_far[(max_x - 1,max_y - 1)])
