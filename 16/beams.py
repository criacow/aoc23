#!/usr/bin/python3

import sys

def move(beam, max_x, max_y):
  curbeam = beam.split(",")
  x = int(curbeam[0])
  y = int(curbeam[1])
  dir = curbeam[2]
  if dir == "N":
    y -= 1
    if y < 0:
      dir = "X"
  if dir == "E":
    x += 1
    if x >= max_x:
      dir = "X"
  if dir == "S":
    y += 1
    if y >= max_x:
      dir = "X"
  if dir == "W":
    x -= 1
    if x < 0:
      dir = "X"
  newcoords = str(x) + "," + str(y) + "," + dir
  return newcoords

beams = ["-1,0,E"]
beammap = []
max_x = 0
for line in sys.stdin:
    beammap.append(list(line))
    max_x = len(line) - 1
max_y = len(beammap)
print("max_x: " + str(max_x) + ", max_y: " + str(max_y))
energized = ["0,0"]

while len(beams) > 0:
  newbeams = []

  for i in range(len(beams)):
    beams[i] = move(beams[i], max_x, max_y)
    curbeam = beams[i].split(",")
    if curbeam[2] != "X":
      x = int(curbeam[0])
      y = int(curbeam[1])
      newdir = curbeam[2]
      coords = curbeam[0] + "," + curbeam[1]
      if coords not in energized:
        energized.append(coords)
      if beammap[y][x] == "|" and (curbeam[2] == "E" or curbeam[2] == "W"):
        newdir = "N"
        newbeam = str(x) + "," + str(y) + ",S"
        newbeams.append(newbeam)
      elif beammap[y][x] == "-" and (curbeam[2] == "S" or curbeam[2] == "N"):
        newdir = "W"
        newbeam = str(x) + "," + str(y) + ",E"
        newbeams.append(newbeam)
      elif beammap[y][x] == "/" and curbeam[2] == "N":
        newdir = "E"
      elif beammap[y][x] == "/" and curbeam[2] == "S":
        newdir = "W"
      elif beammap[y][x] == "/" and curbeam[2] == "W":
        newdir = "S"
      elif beammap[y][x] == "/" and curbeam[2] == "E":
        newdir = "N"
      elif beammap[y][x] == "\\" and curbeam[2] == "W":
        newdir = "N"
      elif beammap[y][x] == "\\" and curbeam[2] == "E":
        newdir = "S"
      elif beammap[y][x] == "\\" and curbeam[2] == "S":
        newdir = "E"
      elif beammap[y][x] == "\\" and curbeam[2] == "N":
        newdir = "W"
      updbeam = str(x) + "," + str(y) + "," + newdir
      beams[i] = updbeam

  for i in range(len(beams)-1, -1, -1):
    z = beams[i].split(",")
    if z[2] == "X":
      beams.pop(i)

  beams += newbeams

  beams = list ( dict.fromkeys(beams) )

  print("beams: " + str(len(beams)) + ", energized: " + str(len(energized)))
