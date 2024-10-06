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
inf = 100100100100100100100
debug = False
# debug = True
if debug:
    def dprint(*arg): print(*arg, file=sys.stderr)
else:
    def dprint(*arg): pass

N,X = LII()
apbq = [LII() for _ in range(N)]

# # dp[i][j] i番目で、処理能力の最小がjの時の最小コスト
# dp = [[inf]*101 for _ in range(N+1)]
# dp_min = [[inf]*101 for _ in range(N+1)]

# dp[0][0] = 0

# for i in range(N):
#     a,b,p,q = apbq[i]
#     prev = inf
#     for j in range(101)[::-1]:
#         if j <= a:
#             dp[i+1][j] = min(dp[i+1][j],dp_min[i][j]+p)
#         if j <= b:
#             dp[i+1][j] = min(dp[i+1][j],dp_min[i][j]+q)
#         dp_min[i+1][j] = min(prev,dp_min[i+1][j])
#         prev = dp[i+1][j]

def check_sub(a,b,p,q, w):
    x = inf
    for na in range(b+1):
        nb = max(0,(w - a*na+b-1)//b)

        x = min(x,  na*p + nb*q)
    for nb in range(a+1):
        na = max(0, (w - b*nb+a-1)//a)
        x = min(x,  na*p + nb*q)
    return x

def check(w):
    x = 0
    for a,p,b,q in apbq:
        x += check_sub(a,b,p,q,w)
    return x <= X

# print(check(2))
# print(check(3))
# print(check(4))
# print(check(5))
ok = 0
ng = 10**18
while ng-ok>1:
    mid = (ok+ng)//2
    if check(mid) :
        ok = mid
    else:
        ng = mid
print(ok)


