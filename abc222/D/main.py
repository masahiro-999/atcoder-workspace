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
mod = 998244353
N = II()
A = LII()
B = LII()

M=3000
dp = [1]*(M+1)
for i in range(N):
    ndp = [0]*(M+1)
    a,b = A[i],B[i]
    for j in range(a,M+1):
        if j <=b:
            ndp[j] = (ndp[j-1]+dp[j])%mod
        else:
            ndp[j] = (ndp[j-1])%mod


    # print(dp,ndp)
    dp = ndp

ans=dp[-1]
print(ans)