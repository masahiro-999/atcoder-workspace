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

N,K = LII()
A = [LII() for _ in range(N)]
Q = II()

d = [[0]*2*N for _ in range(2*N)]
for i in range(2*N):
    for j in range(2*N):
        d[i][j]=inf if A[i%N][j%N]==0 else 1

for i in range(N):
    d[i][i] = 0

for k in range(2*N):
    for i in range(2*N):
        for j in range(2*N):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

for _ in range(Q):
    s,t = LII()
    s -= 1
    t -= 1
    n1 = s//N
    n2 = t//N
    if n1 == n2:
        s = s%N
        t = t%N
    else:
        s = s%N
        t = t%N+N
    ans = d[s][t]
    if ans == inf:
        ans = -1
    print(ans)