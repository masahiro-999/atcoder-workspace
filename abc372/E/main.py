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

N,Q = LII()

from atcoder.dsu import DSU
dsu = DSU(N)
t = [SortedSet() for _ in range(N)]
for i in range(N):
    t[i].add(i)

for _ in range(Q):
    cmd,u,v = LII()
    if cmd == 1:
        u -= 1
        v -= 1
        if dsu.same(u,v):
            continue
        g = dsu.leader(u)
        h = dsu.leader(v)
        if len(t[g]) < len(t[h]):
            g,h = h,g
        marge = t[g]
        for i in t[h]:
            marge.add(i)
        dsu.merge(u,v)
        g = dsu.leader(u)
        t[g] = marge

    elif cmd == 2:
        k = v
        # 頂点uと連結な頂点の中で、k番目に頂点番号が大きいもの
        u -= 1
        g = dsu.leader(u)
        if len(t[g]) < k:
            print(-1)
        else:
            nn = len(t[g])
            print(t[g][nn-k]+1)


