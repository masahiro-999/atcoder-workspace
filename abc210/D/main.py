import sys
import os
from math import ceil, floor, sqrt, pi, factorial, gcd,lcm,sin,cos,tan,asin,acos,atan2,exp,log,log10, isqrt, comb
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cmp_to_key, lru_cache, reduce, cache
from operator import add, iand, ior, itemgetter, mul, xor
from string import ascii_lowercase, ascii_uppercase, ascii_letters
from typing import *
from bisect import bisect, bisect_left, bisect_right
from heapq import heapify, heappop, heappush, heappushpop, nlargest, nsmallest
from sortedcontainers import SortedSet, SortedList, SortedDict
from itertools import product, accumulate,permutations,combinations, count, groupby
input = lambda: sys.stdin.readline().rstrip("\r\n")
I = input
II = lambda: int(I())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
sys.setrecursionlimit(10000000)
inf = float('inf')
inf = 100000000000000000000
H,W,C = LII()

A = [LII() for _ in range(H)]

def solv(A):
    t0 = [[inf]*(W+1) for _ in range(H+1)]

    ans = inf
    for i in range(H)[::-1]:
        for j in range(W)[::-1]:
            mi = min(t0[i+1][j], t0[i][j+1])
            val = A[i][j]+mi-C*(i+j)
            ans = min(ans,val)
            t0[i][j] = min(mi, A[i][j]+C*(i+j))
    return ans

ans = min(solv(A), solv(A[::-1]))
print(ans)  