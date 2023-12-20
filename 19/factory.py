#!/usr/bin/python3
import sys

directions = {}
parts = []
input_section = 1
for line in sys.stdin:
    if line == "\n":
      input_section = 2
    elif input_section == 1:
      dkey,dbl = line.split('{')
      dval,dxx = dbl.split('}')
      directions[dkey]=dval
    else:
      lxx,lbl = line.split('{')
      lval,lxx = lbl.split('}')
      parts.append(lval)

sum = 0
for i in parts:
    part = {}
    partvals = i.split(',')
    for j in partvals:
       pkey, pval = j.split('=')
       part[pkey] = pval
    command = "in"
    result = ""
    while result == "":
      checks = directions[command].split(",")
      for k in checks:
        do_thing = 0
        if ':' in k:
          todo,whattodo = k.split(":")
          if '<' in todo:
            checkvar,checkval = todo.split("<")
            if int(part[checkvar]) < int(checkval):
              do_thing = 1
          else:
            checkvar,checkval = todo.split(">")
            if int(part[checkvar]) > int(checkval):
              do_thing = 1
          if do_thing == 1:
            if whattodo == "A" or whattodo == "R":
              result = whattodo
              break
            else:
              command = whattodo
              break
        else:
          if k == "A" or k == "R":
            result = k
            break
          else:
            command = k
            break

    if result == "A":
      for j in part.values():
        sum += int(j)

print(sum)
