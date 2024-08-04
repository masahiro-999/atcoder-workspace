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
S = I()

win = [1,2,0]
t = {"R":0,"P":1,"S":2}
S = [t[s] for s in S]

dp = [[0]*3 for _ in range(N+1)]
# j = 0: 引き分け, j = 1: 勝つ
dp[0][0] = 0
dp[0][1] = 0
dp[0][2] = 0

for i in range(1,N+1):
    ao = S[i-1]
    for j in range(3):
        if win[j] == ao:
            dp[i][j] = 0
            continue
        if j == ao:
            for k in range(3):
                if k == j:
                    continue
                dp[i][j] = max(dp[i][j],dp[i-1][k])
        else:
            for k in range(3):
                if k == j:
                    continue
                dp[i][j] = max(dp[i][j],dp[i-1][k]+1)

ans = max(dp[N])
print(ans)
