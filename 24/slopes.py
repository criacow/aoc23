#!/usr/bin/python3
import sys

range_start = 200000000000000
range_end = 400000000000000

lines = []

id = 0
for line in sys.stdin:
    coords,velocity = line.strip().split(' @ ')
    x1,y1,z1 = coords.split(', ')
    vx,vy,vz = velocity.split(', ')
    x1 = int(x1)
    y1 = int(y1)
    vx = int(vx)
    vy = int(vy)
    x2 = x1 + vx
    y2 = y1 + vy
    m = (y2 - y1) / (x2 - x1)
    b = y1 - (m * x1)
    lines.append([id, x1, y1, m, b, vx])
    id += 1

count = 0
for i in range(len(lines)):
  for j in range(lines[i][0] + 1, len(lines)):
    if lines[i][3] != lines[j][3]:
      # y = mx + b, y = mx + b
      # m1x + b1 = m2x + b2
      # m1x - m2x = b2 - b1
      # (m1-m2)x = b2 - b1
      # x = (b2 - b1) / (m1 - m2)
      # y = mx + b
      x = (lines[j][4] - lines[i][4]) / (lines[i][3] - lines[j][3])
      y = (lines[i][3] * x) + lines[i][4]
      if x > range_start and x < range_end and y > range_start and y < range_end:
        if (lines[i][5] > 0 and lines[i][1] < x) or (lines[i][5] < 0 and lines[i][1] > x):
          if (lines[j][5] > 0 and lines[j][1] < x) or (lines[j][5] < 0 and lines[j][1] > x):
#            print(lines[i][0],lines[j][0], lines[i][1],lines[j][1], lines[i][5],lines[j][5], x, y)
            count += 1

print(count)
