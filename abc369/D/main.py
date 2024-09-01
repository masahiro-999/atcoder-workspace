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
A =LII()
dp = [[-inf]*(2) for _ in range(N+1)]
# dp[i][j] i番目まで見て、j=0それまでに倒したモンスターが偶数の時,j=0それまでに倒したモンスターが偶数の時
# の最小のコスト
dp[0][0] = 0


for i in range(N):
    a = A[i]
    dp[i+1][0] = max(dp[i][0],dp[i][1]+a*2)
    dp[i+1][1] = max(dp[i][1],dp[i][0]+a)
print(max(dp[N]))

# print(dp)