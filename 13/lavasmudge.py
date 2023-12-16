#!/usr/bin/python3

import sys, copy

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

  untouched_val = 0;
  for j in range(y-1):
    mirror = 0
    mirror = process_y(j, j+1, i, x, y)
    if mirror == 1:
      untouched_val = (j + 1) * 100

  for j in range(x-2):
    mirror = 0
    mirror = process_x(j, j+1, i, x, y)
    if mirror == 1:
      untouched_val = j + 1

  mirror = 0
  for q in range(y):
    for r in range(x-1):
      chartcopy = copy.deepcopy(i)
      if chartcopy[q][r] == '.':
        chartcopy[q][r] = "#"
      else:
        chartcopy[q][r] = "."

      for j in range(y-1):
        mirror = process_y(j, j+1, chartcopy, x, y)
        if mirror == 1:
          score = (j + 1) * 100
          if score != untouched_val:
            sum += (j + 1) * 100
            break
          else:
            mirror = 0

      if mirror == 0:
        for j in range(x-2):
          mirror = process_x(j, j+1, chartcopy, x, y)
          if mirror == 1:
            score = j + 1
            if score != untouched_val:
              sum += j + 1
              break
            else:
              mirror = 0
      if mirror == 1:
        break
    if mirror == 1:
      break
print(sum)

sys.exit()

