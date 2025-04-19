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
inf = 100100100100100100100
debug = False
# debug = True
if debug:
    def dprint(*arg): print(*arg, file=sys.stderr)
else:
    def dprint(*arg): pass

from atcoder.dsu import DSU


N,M = LII()
uv = [LII() for _ in range(M)]

dsu = DSU(N)
s = set()
g = defaultdict(list)

for i in range(M):
    u,v = uv[i]
    u -= 1
    v -= 1
    if u<v:
        u,v = v,u
    uv[i] = u,v

uv.sort()

for u,v in uv:
    g[u].append(v)
    g[v].append(u)

for j in g[0]:
    if j > 0:
        s.add(j)

added = [False]*N

q = deque(uv)
for i in range(N):
    for j in g[i]:
        if j > i:
            s.add(j)
        else:
            dsu.merge(i,j)
    s.discard(i)
    if dsu.size(i) == i+1:
        print(len(s))
    else:
        print(-1)

