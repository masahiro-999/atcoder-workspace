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

N,X,Y = LII()
ab = [LII() for _ in range(N)]

dp = [[inf]*(N+1) for _ in range(X+1)]

dp[0][0] = 0

ans = 0
for i in range(N):
    a,b = ab[i]
    for x in range(X)[::-1]:
        for n in range(N)[::-1]:
            if dp[x][n] == inf:
                continue
            if X < x+a:
                continue
            dp[x+a][n+1] = min(dp[x+a][n+1], dp[x][n]+b)
            if dp[x+a][n+1] <= Y:
                ans = max(ans,n+1)

if ans < N:
    ans += 1
print(ans)