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

N = II()
X = LII()
uvw = [LII() for _ in range(N-1)]

g = [set() for _ in range(N)]

for u,v,w in uvw:
    u -= 1
    v -= 1
    g[u].add((v,w))
    g[v].add((u,w))

def move(i,j,w):
    global ans
    ans += abs(X[i])*w
    X[j] += X[i]
    X[i] =0 
    g[j].remove((i,w))
    g[i].remove((j,w))

q = []
for i in range(N):
    if len(g[i]) == 1:
        q.append(i)

ans = 0

while q:
    i = q.pop()
    if len(g[i]) == 0:
        continue
    v,w = list(g[i])[0]
    move(i,v,w)
    if len(g[v])== 1:
        q.append(v)

print(ans)
