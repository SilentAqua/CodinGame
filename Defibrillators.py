import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = float(input().replace(",", "."))
lat = float(input().replace(",", "."))

n = int(input())

distances = []

answer = "answer"
for i in range(n):
    defib = input()
    elements = defib.split(";")
    lon_D = float(elements[4].replace(",", "."))
    lat_D = float(elements[5].replace(",", "."))

    x = (lon_D - lon) * math.cos((lat + lat_D)/2)
    y = lat_D - lat
    d = math.sqrt(x*x + y*y) * 6371

    distances += [(elements[1], d)]

minimum = -1
name = ""
for el in distances:
    if minimum == -1 or el[1] < minimum:
        minimum = el[1]
        name = el[0]

print(name)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
