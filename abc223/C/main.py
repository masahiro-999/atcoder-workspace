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
N=II()
ab=[LII() for _ in range(N)]

ans = 0
q = deque(ab)
while q and len(q)>1:
    la,lb = q[0]
    ra,rb = q[-1]
    lt = la/lb
    rt = ra/rb
    if lt > rt:
        x= lb*rt
        q[0]=la-x,lb
        ans += lb*rt
        q.pop()
    elif lt < rt:
        x= rb*lt
        q[-1]=ra-x,rb
        ans += lb*lt
        q.popleft()
    else:
        x= lb*lt
        ans += x
        q.popleft()
        q.pop()
    # print(q, ans)
    
if q:
    la,lb = q[0]
    lt = la/lb
    x= lb*lt/2
    ans += x

print(ans)