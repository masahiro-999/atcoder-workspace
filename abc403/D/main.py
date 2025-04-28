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

NN,D = LII()
AA =LII()

cnt = Counter(AA)

if D == 0:
    ans = NN - len(cnt)
    print(ans)
    exit()


A = list(cnt.keys())
N = len(A)


# import random
# N=100000
# D =random.randrange(1000000)
# A =[random.randrange(1000000) for _ in range(N)]

A.sort()

g = [-1]*N
b = [-1]*N

for i in range(N):
    n = A[i]+D
    j = bisect_left(A,n)
    if j<N and A[j] == n:
        g[i] = j
        b[j] = i

dp = [[0]*2 for _ in range(N)]
ans = 0
for i in range(N):
    if b[i] == -1:
        dp[i][0] = 0
        dp[i][1] = cnt[A[i]]
    else:
        prev_i = b[i]
        dp[i][0] = dp[prev_i][1]
        dp[i][1] = min(dp[prev_i])+cnt[A[i]]
    if g[i] == -1:
        ans += min(dp[i])

print(ans)
