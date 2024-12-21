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

N,M,sx,sy= LII()
xy = [LII() for _ in range(N)]
dc = [LI() for _ in range(M)]


X = defaultdict(list)
Y = defaultdict(list)

X2 = defaultdict(list)
Y2 = defaultdict(list)

for x,y in xy:
    X[x].append(y)
    Y[y].append(x)

for k in X.keys():
    X[k].sort()
    X2[k] = [0]*len(X[k])

for k in Y.keys():
    Y[k].sort()
    Y2[k] = [0]*len(Y[k])

x,y = sx,sy
for d,c in dc:
    c = int(c)
    if d == "U":
        y_next = y + c
        i1 = bisect_left(X[x],y)
        if i1 < len(X[x]):
            X2[x][i1] += 1
            i2 = bisect_right(X[x],y_next)
            if i2 < len(X[x]):
                X2[x][i2] -= 1
        y = y_next
    elif d == "D":
        y_next = y - c
        i1 = bisect_left(X[x],y_next)
        if i1 < len(X[x]):
            X2[x][i1] += 1
            i2 = bisect_right(X[x],y)
            if i2 < len(X[x]):
                X2[x][i2] -= 1
        y = y_next
    elif d == "R":
        x_next = x + c
        i1 = bisect_left(Y[y],x)
        if i1 < len(Y[y]):
            Y2[y][i1] += 1
            i2 = bisect_right(Y[y],x_next)
            if i2 < len(Y[y]):
                Y2[y][i2] -= 1
        x = x_next
    elif d == "L":
        x_next = x - c
        i1 = bisect_left(Y[y],x_next)
        if i1 < len(Y[y]):
            Y2[y][i1] += 1
            i2 = bisect_right(Y[y],x)
            if i2 < len(Y[y]):
                Y2[y][i2] -= 1
        x = x_next
    # print(x,y)

for k in X.keys():
    for i in range(1,len(X[k])):
        X2[k][i] += X2[k][i-1]

for k in Y.keys():
    for i in range(1,len(Y[k])):
        Y2[k][i] += Y2[k][i-1]

s = set()
for xx in X.keys():
    for i in range(len(X[xx])):
        if X2[xx][i] > 0:
            s.add((xx,X[xx][i]))

for yy in Y.keys():
    for i in range(len(Y[yy])):
        if Y2[yy][i] > 0:
            s.add((Y[yy][i],yy))

print(x,y,len(s))

