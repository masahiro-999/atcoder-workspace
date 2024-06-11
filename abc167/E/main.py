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
input = sys.stdin.readline
# input = lambda: sys.stdin.readline().rstrip("\r\n")
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
N,M,K = LII()
MOD=998244353
# dp=[0]*(K+1)
# dp[0]=M
# for i in range(N-1):
#     ndp = [0]*(K+1)
#     for k in range(K+1):
#         if k == 0:
#             ndp[k] = dp[k]*(M-1) %MOD
#         else:
#             ndp[k] = (dp[k]*(M-1)+dp[k-1])%MOD
#     dp = ndp
#     dprint(dp)

# ans = sum(dp)%MOD

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


def choose(n,a):
    if a == 0:
        return 1
    if n<a or a <0:
        return 0
    return (factorials[n] * (invs[n-a] * invs[a])) % MOD

# print(choose(10,0))

factorials, invs = prepare(N,MOD)

ans = 0
x = M
for i in range(N):
    k = N-1-i
    if k <=K:
        ans += x*choose(N-1,i)
        ans %= MOD
    x =(x*(M-1))%MOD

print(ans)
