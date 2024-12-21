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

H,W,X,Y = LII()
S = [I() for _ in range(H)]
T = I()

X -= 1
Y -= 1

s = set()
for t in T:
    if t == "U":
        if X > 0 and S[X-1][Y] != "#":
            X -= 1
    elif t == "D":
        if X < H-1 and S[X+1][Y] != "#":
            X += 1
    elif t == "L":
        if Y > 0 and S[X][Y-1] != "#":
            Y -= 1
    elif t == "R":
        if Y < W-1 and S[X][Y+1] != "#":
            Y += 1
    if S[X][Y] == "@":
        s.add((X,Y))
    # print(X,Y)
print(X+1,Y+1,len(s))