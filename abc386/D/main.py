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
inf = 100100100100100100
debug = False
# debug = True
if debug:
    def dprint(*arg): print(*arg, file=sys.stderr)
else:
    def dprint(*arg): pass

N,M = LII()
xyc = [LI() for _ in range(M)]

X = list(set([int(x) for x,y,c in xyc]))
X.sort()
Y = list(set([int(y) for x,y,c in xyc]))
Y.sort()

tate_b = defaultdict(lambda: 0)
tate_w = defaultdict(lambda: inf)
yoko_b = defaultdict(lambda: 0)
yoko_w = defaultdict(lambda: inf)

for x,y,c in xyc:
    x = int(x)
    y = int(y)
    if c == "B":
        tate_b[y] = max(tate_b[y],x)
        yoko_b[x] = max(yoko_b[x],y)
    else:
        tate_w[y] = min(tate_w[y],x)
        yoko_w[x] = min(yoko_w[x],y)



bound = inf
for y in Y:
    bound = min(bound,tate_w[y])
    if bound <= tate_b[y]:
        print("No")
        exit()

bound = inf 
for x in X:
    bound = min(bound,yoko_w[x])
    if bound <= yoko_b[x]:
        print("No")
        exit()

print("Yes")
