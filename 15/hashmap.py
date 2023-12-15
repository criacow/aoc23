#!/usr/bin/python3
import sys
from collections import defaultdict

input = ""

for line in sys.stdin:
    input += line.strip()

strs = input.split(",")

hashmap = defaultdict(list)

for i in strs:
    cur_value = 0
    focal = 0
    type = ""
    label = ""
    for j in i:
       if type == "add":
         focal = j
       elif j == "=":
         type = "add"
       elif j == "-":
         type = "delete"
       else:
         label += j
         cur_value += ord(j)
         cur_value *= 17
         cur_value = cur_value % 256

    if type == "add":
       still_add = 1
       keystr = label + " " + str(focal)
       for i in range(len(hashmap[cur_value])):
         chkval = hashmap[cur_value][i].split(" ")
         if label == chkval[0]:
           hashmap[cur_value][i] = keystr
           still_add = 0

       if still_add == 1:
         hashmap[cur_value].append(keystr)
    elif type == "delete":
       for i in range(len(hashmap[cur_value])):
         chkval = hashmap[cur_value][i].split(" ")
         if label == chkval[0]:
           hashmap[cur_value].remove(hashmap[cur_value][i])
           break

sum = 0
for i in hashmap.items():
    if len(hashmap[i[0]]) > 0:
      for j in range(len(i[1])):
        calcval = hashmap[i[0]][j].split(" ")
        lensval = (i[0] + 1) * (j + 1) * int(calcval[1])
        sum += lensval

print(sum)
