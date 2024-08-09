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

N = II()
xy = [LII() for _ in range(N)]
# from atcoder.dsu import DSU

# g = defaultdict(list)

# for i in range(N):
#     x1,y1 = xy[i]
#     for j in range(i):
#         x2,y2 = xy[j]
#         dx,dy = x1-x2, y1-y2
#         if dx == 0:
#             dy = 1
#         elif dy == 0:
#             dx = 1
#         else:
#             gcdxy = gcd(dx,dy)
#             dx //= gcdxy
#             dy //= gcdxy
#             if dx <0:
#                 dx *= -1
#                 dy *= -1
#         if i > j:
#             i,j = j,i
#         g[(dx,dy)].append((i,j))

# mx = 0
# for k in g:
#     dsu = DSU(N)
#     for i,j in g[k]:
#         dsu.merge(i,j)
#     gr = dsu.groups()
#     mx = max(mx, max([len(g) for g in gr]))

mx = 0
for i in range(N):
    x1,y1 = xy[i]
    for j in range(i):
        x2,y2 = xy[j]
        cnt = 2
        for k in range(N):
            if k == i or k == j:
                continue
            x3,y3 = xy[k]
            dx1,dy1 = x1-x2,y1-y2
            dx2,dy2 = x2-x3,y2-y3
            if dx1*dy2 == dx2*dy1:
                cnt += 1
        mx = max(mx,cnt)
        
a = N - mx

ans = N//3
ans = min(ans,a)

print(ans)