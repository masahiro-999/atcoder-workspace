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

N,M = LII()
X = LII()
X = list(set(X))
X.sort()
N = len(X)

if N<=M:
    ans = 0
else:
    d = []
    for a,b in zip(X,X[1:]):
        d.append(b-a)
    d.sort(reverse=True)
    ans = sum(d[M-1:])

# def check(x):
#     print("chek",x)
#     p = 0
#     m = M
#     while m>0 and p<N:
#         p = bisect_right(X,X[p]+x)
#         m -= 1
#     return  p >=N

# if N<=M:
#     ans = 0
# else:
#     ng = 0
#     ok = max(X)
#     while ok-ng >1:
#         mid = (ok+ng)//2
#         if check(mid):
#             ok = mid
#         else:
#             ng = mid

#     ans = ok

print(ans)