#!/usr/bin/python3
import sys

input = "#70c710"

hexlength = input[1:6]
length = int(hexlength, 16)
dire = input[6]
print(str(length) + "," + dire)
