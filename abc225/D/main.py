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

N,Q = LII()

fw = [None]*N
ba = [None]*N


for _ in range(Q):
    q = LII()
    if q[0]==1:
        x,y = q[1:]
        x -=1
        y -=1
        assert fw[x] is None
        assert ba[y] is None
        fw[x]=y
        ba[y]=x
    elif q[0]==2:
        x,y = q[1:]
        x -=1
        y -=1
        assert fw[x]==y
        assert ba[y]==x
        fw[x]=None
        ba[y]=None
    else:
        x = q[1]
        x -=1
        ans1 = []
        p = x
        while True:
            p = ba[p]
            if p is None:
                break
            # print(f"b {p=}")
            ans1.append(p+1)
        ans2 = []
        p = x
        while True:
            p = fw[p]
            if p is None:
                break
            # print(f"f {p=}")
            ans2.append(p+1)
        M = len(ans1)+len(ans2)+1
        # print(fw)
        print(M,*ans1[::-1],x+1,*ans2)
