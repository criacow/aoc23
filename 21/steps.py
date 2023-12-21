#!/usr/bin/python3
import sys

num_steps = 64
cur_steps = []
cur_map = []
max_x = 0
max_y = 0
cur_y = 0

for line in sys.stdin:
    r = list(line.strip())
    cur_map.append(r)
    max_x = len(r)
    for x in range(len(line)):
      if line[x] == "S":
        cur_steps.append((x, cur_y))
    cur_y += 1
max_y = len(cur_map)

for y in range(len(cur_map)):
  for x in range(len(cur_map[y])):
    if cur_map[y][x] == "S":
        cur_map[y][x] = "."

for i in range(num_steps):
  new_steps = []
  for s in cur_steps:
    x = s[0]
    y = s[1]
    if x > 0:
      if cur_map[y][x-1] == ".":
        new_steps.append((x-1,y))
        cur_map[y][x-1] = "S"
    if x < max_x:
      if cur_map[y][x+1] == ".":
        new_steps.append((x+1,y))
        cur_map[y][x+1] = "S"
    if y > 0:
      if cur_map[y-1][x] == ".":
        new_steps.append((x,y-1))
        cur_map[y-1][x] = "S"
    if y < max_x:
      if cur_map[y+1][x] == ".":
        new_steps.append((x,y+1))
        cur_map[y+1][x] = "S"
    cur_map[y][x] = "."
  cur_steps = new_steps
print(len(cur_steps))
