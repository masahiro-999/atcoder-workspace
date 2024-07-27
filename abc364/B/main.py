import sys
import os
from math import ceil, floor, sqrt, pi, factorial, gcd,lcm,sin,cos,tan,asin,acos,atan2,exp,log,log10, isqrt
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cmp_to_key, lru_cache, reduce, cache
from operator import add, iand, ior, itemgetter, mul, xor
from string import ascii_lowercase, ascii_uppercase, ascii_letters
from typing import *
from bisect import bisect, bisect_left, bisect_right
from heapq import heapify, heappop, heappush, heappushpop, nlargest, nsmallest
from sortedcontainers import SortedSet, SortedList, SortedDict
from itertools import product, accumulate,permutations,combinations, count
input = lambda: sys.stdin.readline().rstrip("\r\n")
I = input
II = lambda: int(I())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
sys.setrecursionlimit(10000000)
inf = 100100100100
debug = False
# debug = True
if debug:
    def dprint(*arg): print(*arg, file=sys.stderr)
else:
    def dprint(*arg): pass

H,W = LII()
Si, Sj = LII()
C = [I() for _ in range(H)]
X = I()

x,y = Si-1,Sj-1

for c in X:
    if c == "U":
        if x-1 >= 0 and C[x-1][y] == ".":
            x -= 1
    elif c == "D":
        if x+1 < H and C[x+1][y] == ".":
            x += 1
    elif c == "L":
        if y-1 >= 0 and C[x][y-1] == ".":
            y -= 1
    elif c == "R":
        if y+1 < W and C[x][y+1] == ".":
            y += 1

print(x+1,y+1)