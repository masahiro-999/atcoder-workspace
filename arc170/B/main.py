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
A = LII()

t = [[] for _ in range(11)]

for i,a in enumerate(A):
    t[a].append(i)

for i in range(11):
    t[i].sort()

lr = []
for i,a in enumerate(A):
    for a_l in range(1,11):
        d = a - a_l
        a_r = a + d
        if a_r <1 or a_r > 10:
            continue
        x = bisect_left(t[a_l],i)
        if x == 0:
            continue
        l = t[a_l][x-1]
        x = bisect_right(t[a_r],i)
        if x == len(t[a_r]):
            continue
        r = t[a_r][x]
        lr.append((l,r))

lr.sort(key = lambda x: x[1])

ans = 0
prev = -1
for l,r in lr:
    if l <= prev:
        continue
    ans += (l-prev)*(N-r)
    prev = l

print(ans)