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

mod = 1000000007

ab = [LII() for _ in range(M)]

g = [[] for _ in range(N)]

for a,b in [(a-1,b-1) for a,b in ab]:
    g[a].append(b)
    g[b].append(a)

def bfs(s):
    q = deque()
    q.append((s,0))
    num_path = [0]*N
    dist = [-1]*N
    dist[s] = 0
    num_path[s] = 1
    while q:
        s,d = q.popleft()
        for nxt in g[s]:
            if dist[nxt] != -1:
                if dist[nxt] == d+1:
                    num_path[nxt]+=num_path[s]
                    num_path[nxt] %= mod
                continue
            dist[nxt] = d+1
            num_path[nxt]+=num_path[s]
            num_path[nxt] %= mod
            q.append((nxt,d+1))
    return num_path[N-1]

ans = bfs(0)

print(ans)