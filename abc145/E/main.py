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

N,T = LII()

AB = [LII() for _ in range(N)]


def solve(AB):
    dp = [-1]*(T+1)
    dp[0] = 0
    for a,b in AB:
        for i in range(T-1,-1,-1):
            if dp[i]==-1:
                continue
            if i+a < T:
                dp[i+a] = max(dp[i+a],dp[i]+b)
            else:
                dp[T] = max(dp[T], dp[i]+b)

    dprint(dp)
    ans = max(dp)
    return ans

AB1 = sorted(AB)
# AB2 = sorted(AB, key=lambda x: x[1])
# ans = max(solve(AB1), solve(AB2))
ans = solve(AB1)
print(ans)
