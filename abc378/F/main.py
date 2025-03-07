import sys
import os
from math import ceil, floor, sqrt, pi, factorial, gcd,lcm,sin,cos,tan,asin,acos,atan2,exp,log,log10, isqrt, comb
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

N = II()
uv = [LII() for _ in range(N-1)]

dsu = DSU(N)

g = defaultdict(list)
for u,v in uv:
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

for u,v in uv:
    u -= 1
    v -= 1
    if len(g[u])==3 and len(g[v])==3:
        dsu.merge(u,v)

ans = 0
for group in dsu.groups():
    cnt = 0
    for u in group:
        if len(g[u])!=3:
            continue
        for v in g[u]:
            if len(g[v])==2:
                cnt += 1
    ans += comb(cnt,2)

print(ans)