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
S = [I() for _ in range(N)]

A = [int(s,2).bit_count() %2 for s in S]

cnt = Counter(A)

ans = cnt[0] * cnt[1]

# ans = 0
# for j in range(N):
#     for i in range(j):
#         x = t[i].bit_count() - t[j].bit_count()
#         if x %2 == 1:
#             ans += 1

print(ans)
# t = defaultdict(int)
# for s in S:
#     n = sum(int(x) for x in s)
#     t[n]+= 1

# print(t)
# cnt = 0
# for v in t.values():
#     cnt += comb(v,2)

# ans = comb(N,2)-cnt

# print(ans)