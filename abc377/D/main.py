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

N,M = LII()
LR = [LII() for _ in range(N)]

LR.sort(key=lambda x: x[1])
# print(LR)

table = Counter()
for l,r in LR:
    table[r] = max(table[r],l)

ans = 0

p = 1
for r in range(1,M+1):
    if r in table:
        p = max(p,table[r]+1)
    d = r - p + 1
    if d > 0:
        ans += d
    # print(r,p,d,ans)

print(ans)

# ans = 0
# for l in range(1,M+1):
#     for r in range(l,M+1):
#         for ll,rr in LR:
#             if l <= ll and rr <= r:
#                 break
#         else:
#             ans += 1

# print(ans)