#!/usr/bin/python3
import sys,copy

directions = {}
input_section = 1
for line in sys.stdin:
    if line == "\n":
      input_section = 2
    elif input_section == 1:
      dkey,dbl = line.split('{')
      dval,dxx = dbl.split('}')
      directions[dkey]=dval

def get_rule(rule):
  retvals = []
  values = rule.split(",")
  command = values[8]
  if command == "A" or command == "R":
    retvals.append(values)
    return retvals
  checks = directions[command].split(",")
  for k in checks:
    if ':' in k:
      todo,whattodo = k.split(":")
      if '<' in todo:
        checkvar,checkval = todo.split("<")
        offset = 0
        if checkvar == "m":
          offset = 2
        elif checkvar == "a":
          offset = 4
        elif checkvar == "s":
          offset = 6
        if int(values[offset+1]) > int(checkval):
          newvals = copy.deepcopy(values)
          newvals[offset+1] = str(int(checkval)-1)
          newvals[8] = whattodo
          newrules = get_rule(','.join(newvals))
          for nr in newrules:
            retvals.append(nr)
          values[offset] = checkval
      else:
        checkvar,checkval = todo.split(">")
        offset = 0
        if checkvar == "m":
          offset = 2
        elif checkvar == "a":
          offset = 4
        elif checkvar == "s":
          offset = 6
        if int(values[offset]) < int(checkval):
          newvals = copy.deepcopy(values)
          newvals[offset] = str(int(checkval)+1)
          newvals[8] = whattodo
          newrules = get_rule(','.join(newvals))
          for nr in newrules:
            retvals.append(nr)
          values[offset+1] = checkval
    elif k == "A" or k == "R":
      values[8] = k
      retvals.append(values)
    else:
      values[8] = k
      newrules = get_rule(','.join(values))
      for nr in newrules:
        retvals.append(nr)
  return retvals

rule = "1,4000,1,4000,1,4000,1,4000,in"
rulebook = get_rule(rule)

sum = 0
for values in rulebook:
  if values[8] == "A":
    xval = int(values[1]) - int(values[0]) + 1
    mval = int(values[3]) - int(values[2]) + 1
    aval = int(values[5]) - int(values[4]) + 1
    sval = int(values[7]) - int(values[6]) + 1
    sum += xval * mval * aval * sval

print(sum)
