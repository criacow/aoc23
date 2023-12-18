#!/usr/bin/python3
import sys, copy

part = 2

directions = []
for line in sys.stdin:
    directions.append(line)

path = []
path.append([0,0])
cur_x = 0
cur_y = 0
trench_len = 0
for i in directions:
    dir, dist, colour = i.split(' ',2)
    if part == 2:
        hexlength = colour[2:7]
        dist = int(hexlength, 16)
        direct = colour[7]
        if direct == "0":
            dir = "R"
        elif direct == "1":
            dir = "D"
        elif direct == "2":
            dir = "L"
        elif direct == "3":
            dir = "U"
    else:
        dist = int(dist)

    if dir == "D":
        cur_y += dist
    elif dir == "U":
        cur_y -= dist
    elif dir == "R":
        cur_x += dist
    elif dir == "L":
        cur_x -= dist
    trench_len += dist
    path.append([cur_x,cur_y])

# maths! https://www.themathdoctors.org/polygon-coordinates-and-areas/
area = 0
for i in range(1,len(path)):
  product = 0
  product += path[i-1][0] * path[i][1]
  product -= path[i][0] * path[i-1][1]
  area += product

area = abs(area)
area = ((area + trench_len) / 2) + 1

print(int(area))
