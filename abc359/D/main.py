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

MOD = 998244353
N,K = LII()
S = I()
dp = [Counter() for _ in range(N+1)]
dp[0][""] = 1
Kh = K//2

for i in range(N):
    s = S[i]
    if s == "?":
        x = "AB"
    else:
        x = s
    for j in dp[i].keys():
        for k in x:
            nj = (j+k)[-K:]
            if len(nj)==K:
                if nj[:Kh]!=nj[-Kh:][::-1]:
                    dp[i+1][nj] += dp[i][j]
                    dp[i+1][nj] %= MOD
            else:
                dp[i+1][nj] += dp[i][j]
                dp[i+1][nj] %= MOD

ans = 0
for k,v in dp[N].items():
    if k[:Kh]!=k[-Kh:][::-1]:
        ans += v
        ans %= MOD

print(ans)