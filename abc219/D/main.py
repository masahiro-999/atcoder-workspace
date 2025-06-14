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
X,Y = LII()
ab=[LII() for _ in range(N)]

dp = [[[inf]*(Y+1) for _ in range(X+1)] for _ in range(N+1)]

dp[0][0][0]=0

for i in range(N):
    a,b = ab[i]
    for j in range(X+1):
        for k in range(Y+1):
            dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
            nj = min(X,j+a)
            nk = min(Y,k+b)
            dp[i+1][nj][nk] = min(dp[i+1][nj][nk], dp[i][j][k]+1)

ans = dp[N][X][Y]
if ans == inf:
    ans = -1
print(ans)