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
ab = [LII() for _ in range(N)]
cd = [LII() for _ in range(N)]

def d2(x1,y1,x2,y2):
    return((x1-x2)**2+(y1-y2)**2)

def create_d(base,e1,data):
    x0,y0=base
    x,y=e1
    x1 = x-x0
    y1 = y-y0
    ret = []
    for x,y in data:
        x2 = x-x0
        y2 = y-y0
        ret.append((x1*x2+y1*y2,x1*y2-x2*y1))
    ret.sort()
    return ret

if N == 1:
    ans = True
elif N == 2:
    ans =  d2(*ab[0],*ab[1]) == d2(*cd[0],*cd[1])
else:
    base = ab[0]
    e1=ab[1]
    result_ab = create_d(base,e1,ab[2:])
    ans = False
    for j in range(N):
        for i in range(N):
            if i == j:
                continue
            if d2(*base,*e1) != d2(*cd[i],*cd[j]) :
                continue
            # print("ok")
            n,m = i,j
            if n > m:
                n,m = m,n
            result_cd = create_d(cd[i],cd[j],cd[:n]+cd[n+1:m]+cd[m+1:])
            if result_ab == result_cd:
                ans = True

if ans:
    print("Yes")
else:
    print("No")