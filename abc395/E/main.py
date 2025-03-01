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

N,M,X = LII()

g = defaultdict(list)
for _ in range(M):
    u,v = LII()
    u -= 1
    v -= 1
    g[u].append((1,v))
    g[v+N].append((1,u+N))

for i in range(N):
    g[i].append((X,i+N))
    g[i+N].append((X,i))


def dijkstra():
    q = [(0,0)]
    heapify(q)
    cost_table = [inf]*N*2
    cost_table[0] = 0
    while q:
        c,p = heappop(q)
        # print(p,c)
        if cost_table[p] != c:
            continue
        for next_c,next_p in g[p]:
            if cost_table[next_p] <= c+next_c:
                continue 
            cost_table[next_p] = c+next_c
            heappush(q,(c+next_c, next_p))
    return cost_table

cost_table = dijkstra()

ans = min(cost_table[N-1],cost_table[N*2-1])

print(ans)