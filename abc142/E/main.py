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

N,M = LII()

ac = []
for _ in range(M):
    a,b = LII()
    c = LII()
    x = 0
    for i in c:
        x |= 1<<(i-1)
    ac.append((a,x))


N2 = 1<<N

dp = [[inf]*N2 for _ in range(M+1)]
dp[0][0]=0

for i,(a,x) in enumerate(ac):
    for j in range(N2):
        if dp[i][j] ==-1:
            continue
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        dp[i+1][j|x] = min(dp[i+1][j|x], dp[i][j]+a)

# print(dp)
ans = dp[M][N2-1]
if ans == inf:
    ans = -1
print(ans)
