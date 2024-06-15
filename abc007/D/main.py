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

A,B = LII()

def count(x):
    S = str(x)
    N = len(S)
    dp = [[[0]*2 for _ in range(2)] for _ in range(N+1)]
    dp[0][0][0]=1
    for i in range(N):
        for j in  range(2):
            for k in range(2):
                for x in range(10 if j else int(S[i])+1):
                    nj = 1 if j or x<int(S[i]) else 0
                    nk = 1 if k or x == 4 or x == 9 else 0
                    dp[i+1][nj][nk] += dp[i][j][k]
    # print(dp)
    return dp[N][0][1]+dp[N][1][1]

ans = count(B)
if A > 0:
    ans -=count(A-1)

print(ans)