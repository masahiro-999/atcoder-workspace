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
inf = 100100100100100100
debug = False
# debug = True
if debug:
    def dprint(*arg): print(*arg, file=sys.stderr)
else:
    def dprint(*arg): pass

N = II()
ab = [LII() for _ in range(N)]

A = [a for a,b in ab]
B = [b for a,b in ab]

sum_b = sum(B)

if sum_b % 3 != 0:
    print(-1)
    exit()

M = sum_b // 3

dp = [[[inf]*(M+1) for _ in range(M+1)] for _ in range(N+1)]

dp[0][0][0] = 0

for i in range(N):
    for x in range(M+1):
        for y in range(M+1):
            for j in range(1,4):
                d = 0 if A[i]==j else 1
                dx = 0
                dy = 0
                if j == 1:
                    dx = B[i]
                elif j == 2:
                    dy = B[i]
                if x + dx > M or y + dy > M:
                    continue
                dp[i+1][x+dx][y+dy] = min(dp[i+1][x+dx][y+dy], dp[i][x][y] + d)

if dp[N][M][M] == inf:
    print(-1)
else:
    print(dp[N][M][M])
