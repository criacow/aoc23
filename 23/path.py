#!/usr/bin/python3

import sys
from implementation import *

walls = []
slopes = {}
max_x = 0
cur_y = 0
for line in sys.stdin:
  row = list(line.strip())
  for x in range(len(row)):
    if row[x] == "#":
      walls.append((x, cur_y))
    elif row[x] == ">" or row[x] == "<" or row[x] == "^" or row[x] == "v":
      slopes[(x, cur_y)] = row[x]
  max_x = len(line) - 1
  cur_y += 1
max_y = cur_y

#print(slopes)
#print(walls)
#print(max_x)
#print(max_y)
#sys.exit(0)
#q = SquareGrid(max_x, max_y)
q = GridWithWeights(max_x, max_y)
q.walls = walls

start, goal = (1, 0), (max_x - 2, max_y - 1)
#parents = breadth_first_search(q, start, goal)
#draw_grid(q, point_to=parents, start=start, goal=goal)
came_from, cost_so_far = a_star_search(q, start, goal, slopes)
draw_grid(q, point_to=came_from, path=reconstruct_path(came_from, start, goal), start=start, goal=goal)
print(cost_so_far[goal])
#came_from, cost_so_far = a_star_search(q, start, goal)
#came_from, cost_so_far = dijkstra_search(diagram5, start, goal)
#draw_grid(q)
#, point_to=came_from, start=start, goal=goal)
#draw_grid(diagram5, path=came_from, start=start, goal=goal)
#print()
#draw_grid(diagram5, path=reconstruct_path(came_from, start=start, goal=goal))
#print(diagram5.weights)
#print(came_from)
#print(cost_so_far)
#print(cost_so_far[(max_x - 1,max_y - 1)])
