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

mod = 998244353
N = II()
A = LII()

A.sort()

B = [0]
r = 1
for i in range(N):
    B.append((B[i]+A[i]*r) % mod)
    r *= 2
    r %= mod

# print(B)
ans = 0
inv2 = pow(2,-1,mod)
r = inv2
for i in range(1,N+1):
    ans += A[i-1]*A[i-1]
    ans += (B[N]-B[i])*A[i-1]*r
    ans %= mod
    r = (r*inv2)%mod

print(ans)