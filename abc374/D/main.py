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
N,S,T = LII()
abcd = [LII() for _ in range(N)]

dt = []
for i in range(N):
    a,b,c,d = abcd[i]
    dt.append(sqrt((a-c)**2+(b-d)**2))

# for i in dt:
#     print(i*T)

ans = inf
for p in permutations(range(N), N):
# for p in [[1,0,2]]:
    for i in range(1<<N):
    # for i in [5]:
        x,y = 0,0
        a1 = 0
        for j in range(N):
            a,b,c,d = abcd[p[j]]
            if i>>j&1:
                a,b,c,d = c,d,a,b
            d1 = sqrt((a-x)**2+(b-y)**2)
            a1 += d1/S
            d2 = dt[p[j]]
            a1 += d2/T
            x,y = c,d
            # print(a,b,c,d, d1,d2,a1)
            # print(d1*S,d2*T)
        ans = min(ans,a1)
print(ans)

