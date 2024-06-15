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

K = II()
C = LII()

MOD = 998244353

def prepare(n, MOD):
    f = 1
    factorials = [1]
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
 
    return factorials, invs

factorials, invs = prepare(1000000+1,MOD)

def choose(n,a):
    if a == 0:
        return 1
    if n<a or a <0:
        return 0
    return (factorials[n] * (invs[n-a] * invs[a])) % MOD


dp = [[0]*(K+1) for _ in range(26+1)]
dp[0][0]=1

for i in range(26):
    for j in range(K+1):
        for k in range(min(j+1,C[i]+1)):
            dp[i+1][j] += choose(j,k)*dp[i][j-k]
            dp[i+1][j] %= MOD

# print(dp)
ans = sum(dp[26][1:])%MOD
print(ans)