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

N,M = LII()
ab = [LII() for _ in range(M)]

g = defaultdict(list)
for a,b in ab:
    g[a].append(b)

def bfs(s):
    q = deque([s])
    d = defaultdict(lambda: inf)
    d[s] = 0
    while q:
        v = q.popleft()
        for u in g[v]:
            if u == 1:
                return d[v] + 1
            if d[u] != inf:
                continue
            d[u] = d[v] + 1
            q.append(u)
    return -1

print(bfs(1))