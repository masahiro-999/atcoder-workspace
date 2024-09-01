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
uvt = [LII() for _ in range(M)]
dist = [[inf]*N for _ in range(N)]

for u,v,t in uvt:
    u -= 1
    v -= 1
    dist[u][v] = min(dist[u][v],t)
    dist[v][u] = min(dist[v][u],t)

for i in range(N):
    dist[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
        
Q = II()
for _ in range(Q):
    ans = inf
    K = II()
    B = LII()
    for path in permutations(B,K):
        for mask in range(1<<K):
            p = 0
            ret = 0
            for i, x in enumerate(path):
                u,v,t = uvt[x-1]
                u -= 1
                v -= 1
                if mask >> i & 1:
                    u,v = v,u
                # print(u,v,t, dist[p][u])
                ret += dist[p][u] + t
                p = v
            ret += dist[p][N-1]
            ans = min(ans,ret)
    print(ans)