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
from itertools import product, accumulate,permutations,combinations, count, groupby
input = lambda: sys.stdin.readline().rstrip("\r\n")
I = input
II = lambda: int(I())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
sys.setrecursionlimit(10000000)
inf = float('inf')
debug = False
# debug = True
if debug:
    def dprint(*arg): print(*arg, file=sys.stderr)
else:
    def dprint(*arg): pass

T = II()
for _ in range(T):
    N = II()
    S = I()
    L = []
    for k,g in groupby(S):
        x = len(list(g))
        L.append((int(k),x))

    dp = [[[inf]*2 for _ in range(2)] for _ in range(N+1)]

    M = len(L)
    # print(L)
    dp[0][0][0]=0
    for i in range(M):
        now_k,now_v = L[i]

        if now_k == 1:
            dp[i+1][0][0] = dp[i][0][0] + now_v
        else:
            dp[i+1][0][0] = dp[i][0][0]

        if now_k == 0:
            dp[i+1][1][1] = min(dp[i][1][1], dp[i][0][0]) + now_v
        else:
            dp[i+1][1][1] = min(dp[i][1][1], dp[i][0][0])

        if now_k == 1:
            dp[i+1][1][0] = min(dp[i][1][0],dp[i][1][1]) + now_v
        else:
            dp[i+1][1][0] = min(dp[i][1][0],dp[i][1][1])

    # print(dp)
    ans = min(min(dp[M][1]),min(dp[M][0]))
    print(ans)
