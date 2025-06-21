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

N = II()
xy = [LII() for _ in range(N)]

ans = 0
for i in range(N):
    x0,y0 = xy[i]
    for j in range(i):
        x1,y1 = xy[j]
        x1 -= x0
        y1 -= y0
        for k in range(j):
            x2,y2=xy[k]
            x2-=x0
            y2-=y0

            # print(i,j,k,x1*y2-x2*y1)
            if x1*y2-x2*y1!=0:
                ans += 1
print(ans)