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
inf = 100100100100100100100
debug = False
# debug = True
if debug:
    def dprint(*arg): print(*arg, file=sys.stderr)
else:
    def dprint(*arg): pass

N,K = LII()
A = [LII() for _ in range(N)]


def create_t(limit):
    # limit以下の区画の数
    t = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(N):
            t[i+1][j+1] = t[i+1][j] + (1 if A[i][j]<=limit else 0)
    for j in range(N):
        for i in range(N):
            t[i+1][j+1] += t[i][j+1]    
    return t

def f(limit):
    t = create_t(limit)
    # print(t)
    for i in range(N-K+1):
        for j in range(N-K+1):
            x = t[i+K][j+K]-t[i][j+K]-t[i+K][j]+t[i][j]
            # print(i,j,x)
            if x >= K*K-(K*K//2+1)+1:
                return True
    return False

# print(f(4))
"""
[[0, 0, 0, 0]
 [0, 1, 1, 2]
 [0, 2, 2, 3]
 [0, 2, 3, 5]]

"""
ng = -1
ok = 1000000000
while ok-ng >1:
    mid = (ng+ok)//2
    if f(mid):
        ok = mid
    else:
        ng = mid

print(ok)
