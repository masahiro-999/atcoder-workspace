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
from itertools import product, accumulate,permutations,combinations, count, groupby
input = lambda: sys.stdin.readline().rstrip("\r\n")
I = input
II = lambda: int(I())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
sys.setrecursionlimit(10000000)
inf = float('inf')

N,M = LII()
ab = [LII() for _ in range(M)]

from atcoder.dsu import DSU
dsu = DSU(N)
g = [set() for _ in range(N)]

for a,b in ab:
    a -= 1
    b -= 1
    g[a].add(b)
    g[b].add(a)

def check(p):
    us = 0
    ad = 0
    for i,j in zip(p,list(p[1:])+[p[0]]):
        if j in g[i]:
            us += 1
        else:
            ad += 1
    return (us-ad)

ans = inf
for p in permutations(range(N)):
    us = check(p)
    a = M-us
    ans = min(ans,a)
    if N>5:
        us = check(p[:3])
        us += check(p[3:])
        a = M-us
        ans = min(ans,a)
    if N==8:
        us = check(p[:4])
        us += check(p[4:])
        a = M-us
        ans = min(ans,a)

print(ans)

"""

1 4
4 5
1 5
2 3
2 6
3 4
3 6
4 6

"""