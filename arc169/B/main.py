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

N,S = LII()
A = LII()

dp = [0]*(N+1)
dp[N] == 0

accA = list(accumulate(A, initial=0))
pj=[]
for i in range(N):
    t = accA[i]+S
    j = bisect_right(accA,t)
    pj.append(j-1)

# print(pj)

for i in range(N-1,-1,-1):
    dp[i] = N-(i+1)+1 +dp[pj[i]]

# print(dp)
ans = sum(dp)

# for i in range(N):
#     ans += dp[i]

print(ans)