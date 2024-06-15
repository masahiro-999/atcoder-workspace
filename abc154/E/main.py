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
# input = sys.stdin.readline
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

S = I()
K = II()

N = len(S)

dp = [[[0]*2 for _ in range(K+1)] for _ in range(N+1)]
dp[0][0][0] = 1

for i in range(N):
    for j in range(2):
        for k in range(K+1):
            for x in range(10 if j ==1 else int(S[i])+1):
                nj = j == 1 or x < int(S[i]) 
                nk = k + (x != 0)
                if nk <= K:
                    dp[i+1][nk][nj] += dp[i][k][j]

ans = sum(dp[N][K])
print(ans)