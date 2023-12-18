#!/usr/bin/python3
import sys, copy

# This solution worked for part one, and given infinite time and space would work for part two.
# But, well, I don't have those. So I had to go learn maths (see diggermath.py)

part = 2

directions = []
for line in sys.stdin:
    directions.append(line)

path = []
cur_x = 0
cur_y = 0
min_x = 0
max_x = 0
min_y = 0
max_y = 0
for i in directions:
    dir, dist, colour = i.split(' ',2)
    print(colour)
    if part == 2:
        hexlength = colour[2:7]
        dist = str(int(hexlength, 16))
        direct = colour[7]
        if direct == 0:
            dir = "R"
        elif direct == 1:
            dir = "D"
        elif direct == 2:
            dir = "L"
        elif direct == 3:
            dir = "U"

    for j in range(int(dist)):
        if dir == "D":
            cur_y += 1
            if cur_y > max_y:
                max_y = cur_y
        elif dir == "U":
            cur_y -= 1
            if cur_y < min_y:
                min_y = cur_y
        elif dir == "R":
            cur_x += 1
            if cur_x > max_x:
                max_x = cur_x
        elif dir == "L":
            cur_x -= 1
            if cur_x < min_x:
                min_x = cur_x
        path.append([cur_x,cur_y])

x_offset = 0
y_offset = 0
if min_x < 0:
  x_offset = abs(min_x)
if min_y < 0:
  y_offset = abs(min_y)

gridmap = []
for y in range(min_y,max_y+1):
  gridline = []
  for x in range(min_x,max_x+1):
    gridline.append(".")
  gridmap.append(gridline)

for i in path:
  x = i[0] + x_offset
  y = i[1] + y_offset
  gridmap[y][x] = "#"

first_x = path[1][0] + x_offset
first_y = path[1][1] + 1 + y_offset
ps = []
ps.append([first_x,first_y])
#ps.append([25,129])
old_p_count = 1
p_count = 1
keep_going = 1
while keep_going:
  newps = []
  print(ps)
  for i in ps:
    x = i[0]
    y = i[1]
    gridmap[y][x] = "P"

    if gridmap[y-1][x] == ".":
      gridmap[y-1][x] = "P"
      newps.append([x,y-1])
      p_count += 1
    if gridmap[y+1][x] == ".":
      gridmap[y+1][x] = "P"
      newps.append([x,y+1])
      p_count += 1
    if gridmap[y][x-1] == ".":
      gridmap[y][x-1] = "P"
      newps.append([x-1,y])
      p_count += 1
    if gridmap[y][x+1] == ".":
      gridmap[y][x+1] = "P"
      newps.append([x+1,y])
      p_count += 1

    if old_p_count == p_count:
      keep_going = 0
    else:
      old_p_count = p_count
  ps = []
  ps = deepcopy(newps)

count = 0
for y in gridmap:
  for x in y:
    if x == "#" or x == "P":
      count += 1

#print(gridmap)
#print(path)
#print(x_offset)
#print(y_offset)
print(count)
