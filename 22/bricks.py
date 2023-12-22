#!/usr/bin/python3
import sys, copy

# Assumes an input list sorted from the ground up. See sort-inputs.pl.
part = 1

bricks = []

cur_y = 0
for line in sys.stdin:
    data = line.strip().replace('~', ',').split(",")
    brick = [ cur_y, int(data[0]), int(data[1]), int(data[2]), int(data[3]), int(data[4]), int(data[5]) ]
    bricks.append(brick)
    cur_y += 1

only_supports_one = [ ]

for brick in bricks:
  resting = 0
  while resting == 0:
    if brick[3] == 1:
      resting = 1
      break
    supported_by = [ ]
    for chkbrick in bricks:
      if chkbrick[6] == brick[3] - 1:
        for y in range(brick[2], brick[5]+1):
          for x in range(brick[1], brick[4]+1):
            if y >= chkbrick[2] and y <= chkbrick[5] and x >= chkbrick[1] and x <= chkbrick[4]:
              supported_by.append(chkbrick[0])
    supported_by = list(dict.fromkeys(supported_by))
    if len(supported_by) == 1:
      only_supports_one.append(supported_by[0])
    if len(supported_by) > 0:
      resting = 1
    else:
      brick[3] -= 1
      brick[6] -= 1

only_supports_one = list(dict.fromkeys(only_supports_one))
if part == 1:
  print(len(bricks) - len(only_supports_one))
else:
  sum = 0
  for brick in only_supports_one:
    without_me = copy.deepcopy(bricks)
    del without_me[brick]
    fell = []
    for brick in without_me:
      resting = 0
      while resting == 0:
        if brick[3] == 1:
          resting = 1
          break
        supported_by = [ ]
        for chkbrick in without_me:
          if chkbrick[6] == brick[3] - 1:
            for y in range(brick[2], brick[5]+1):
              for x in range(brick[1], brick[4]+1):
                if y >= chkbrick[2] and y <= chkbrick[5] and x >= chkbrick[1] and x <= chkbrick[4]:
                  supported_by.append(chkbrick[0])
        supported_by = list(dict.fromkeys(supported_by))
        if len(supported_by) > 0:
          resting = 1
        else:
          brick[3] -= 1
          brick[6] -= 1
          fell.append(brick[0])

    fell = list(dict.fromkeys(fell))
    sum += len(fell)
  print(sum)
