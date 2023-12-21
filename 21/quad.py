#!/usr/bin/python

# Values determined by hand. See Excel screenshot lol.

a = 122800.0 / 137288.0
b = (92330.0 - (102704.0 * a)) / 262.0
c = 3885.0 - 4225.0 * a - 65.0 * b

x = 26501365

print((a * x * x) + (b * x) + c)

