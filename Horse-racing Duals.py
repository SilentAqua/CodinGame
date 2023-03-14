import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
tab = []
for i in range(n):
    pi = int(input())
    tab.append(pi)

tab.sort()

minDif = tab[1] - tab[0]
for i in range(1, n-1):
    if tab[i+1] - tab[i] < minDif:
        minDif = tab[i+1] - tab[i]


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(minDif)
