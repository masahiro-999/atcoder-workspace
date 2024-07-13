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
inf = 1<<60
debug = False
# debug = True
if debug:
    def dprint(*arg): print(*arg, file=sys.stderr)
else:
    def dprint(*arg): pass

N,M = LII()
A = LII()
uvb = [LII() for _ in range(M)]

g = defaultdict(list)
for u,v,b in uvb:
    u -= 1
    v -= 1
    g[u].append((v,b))
    g[v].append((u,b))

# print(g)
def dijkstra():
    q = [(A[0],0)]
    heapify(q)
    cost_table = [inf]*N
    cost_table[0] = A[0]
    while q:
        c,p = heappop(q)
        # print(p,c)
        if cost_table[p] != c:
            continue
        for next_p,next_c in g[p]:
            if cost_table[next_p] <= c+next_c+A[next_p]:
                continue 
            cost_table[next_p] = c+next_c+A[next_p]
            heappush(q,(c+next_c+A[next_p], next_p))
    return cost_table
cost_table = dijkstra()
# print(cost_table)
print(*cost_table[1:])
