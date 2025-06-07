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

mod = 1000000007
T = "chokudai"
M = len(T)

S = I()
N = len(S)

dp = [[1]+[0]*M for _ in range(N+1)]

for i in range(N):
    for j in range(1,M+1):
        t = T[j-1]
        if S[i] == t:
            dp[i+1][j] = dp[i][j] + dp[i][j-1]
        else:
            dp[i+1][j] = dp[i][j]
        dp[i+1][j] %= mod
ans = dp[N][M]

print(ans)