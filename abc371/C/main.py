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

N = II()
MG = II()
uv = [LII() for _ in range(MG)]
uv = set([(u-1,v-1) for (u,v) in uv])
MH = II()
ab = [LII() for _ in range(MH)]
ab = set([(a-1,b-1) for a,b in ab])
A = [[0]*(N) for _ in range(N)]

for i in range(N-1):
    for j,x in enumerate(LII()):
        A[i][i+j+1] = x

# print(uv)
# print(ab)
# print(A)


def f(uv):
    ans = 0
    # uvにあって、abにないものを探す
    for u,v in uv:
        if (u,v) in ab:
            continue
        if (v,u) in ab:
            continue
        if u > v:
            u,v = v,u
        # print(0,u,v)
        ans += A[u][v]

    # abにあって、uvにないものを探す
    for a,b in ab:
        if (a,b) in uv:
            continue
        if (b,a) in uv:
            continue
        if a > b:
            a,b = b,a
        # print(1,a,b)
        ans += A[a][b]
    return ans

# uv1 = [[0,3],[0,1],[1,4],[4,2]]
# x = f(uv1)
# print(x)
ans = inf
for p in permutations(range(N),N):
    uv1 = [(p[u],p[v]) for u,v in uv]
    x = f(uv1)
    ans = min(ans, x)

print(ans)