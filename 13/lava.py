#!/usr/bin/python3

import sys

def process_y(line1, line2, chart, x, y):
  if line1 < 0 or line2 == y:
    return 1
  for l in range(x):
    if chart[line1][l] != chart[line2][l]:
      return 0
  return process_y(line1-1, line2+1, chart, x, y)

def process_x(col1, col2, chart, x, y):
  if col1 < 0 or col2 == x - 1:
    return 1
  for l in range(y):
    if chart[l][col1] != chart[l][col2]:
      return 0
  return process_x(col1-1, col2+1, chart, x, y)

charts = []

curmap = []
for line in sys.stdin:
    if line == "\n":
      charts.append(curmap)
      curmap = []
    else:
      curmap.append(list(line))
charts.append(curmap)

sum = 0
for i in charts:
  y = len(i)
  x = len(i[0])

  for j in range(y-1):
    mirror = process_y(j, j+1, i, x, y)
    if mirror == 1:
      sum += (j + 1) * 100
#    print("line: " + str(j) + "; mirror: " + str(mirror))

  for j in range(x-2):
    mirror = process_x(j, j+1, i, x, y)
    if mirror == 1:
      sum += j + 1
#    print("col : " + str(j) + "; mirror: " + str(mirror))

print(sum)

sys.exit()

