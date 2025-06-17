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
N,M = LII()
c={"G":0,"C":1,"P":2}

A = [[c[val] for val in I()] for _ in range(2*N)]

win=[(0,-i) for i in range(2*N)]

def judge(a,b):
    if a == b:
        return 0
    return 1 if (a+1)%3 == b else -1

for i in range(M):
    t = list(range(2*N))
    t.sort(key=lambda x: win[x], reverse=True)
    for j in range(N):
        a,ia = win[t[2*j]]
        b,ib = win[t[2*j+1]]
        assert -ia == t[2*j]
        assert -ib == t[2*j+1]
        result = judge(A[-ia][i],A[-ib][i])
        if result == 1:
            win[t[2*j]] = (a+1,ia)
        elif result == -1:
            win[t[2*j+1]] = (b+1,ib)
    # print(win)
t = list(range(2*N))
t.sort(key=lambda x: win[x],reverse=True)

for i in range(2*N):
    print(t[i]+1)