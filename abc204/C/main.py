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

N,M = LII()
ab = [LII() for _ in range(M)]

g = defaultdict(list)
for a,b in ab:
    a -= 1
    b -= 1
    g[a].append(b)

cnt = 0

def dfs(x,visited):
    # print(x)
    global cnt
    cnt += 1
    visited[x] = 1
    for n in g[x]:
        if not visited[n]:
            dfs(n,visited)

ans = 0
for i in range(N):
    visited = [0]*N
    cnt = 0
    # print(i,"start")
    dfs(i,visited)
    ans += cnt

print(ans)