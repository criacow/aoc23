#!/usr/bin/python3
import sys

input = ""

for line in sys.stdin:
    input += line.strip()

strs = input.split(",")

sum = 0
for i in strs:
    cur_value = 0
    for j in i:
       cur_value += ord(j)
       cur_value *= 17
       cur_value = cur_value % 256
    sum += cur_value

print(sum)
