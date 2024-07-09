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

from atcoder.fenwicktree import FenwickTree


N,M,Q = LII()
ft = FenwickTree(N+1)
lr = [LII() for _ in range(M)]
pq = [LII() for _ in range(Q)]

pq = [(i,p,q) for i,(p,q) in enumerate(pq)]

lr.sort(key= lambda x: x[0])
pq.sort(key= lambda x: x[1])

for l,r in lr:
    ft.add(r,1)

ans = [0]*Q

s = 0
for i in range(Q):
    j,p,q = pq[i]
    # pよりも小さいlを消す
    while s <M:
        l,r = lr[s]
        if l >= p:
            break
        ft.add(r, -1)
        s += 1

    ans[j] = ft.sum(p,q+1)
print(*ans, sep="\n")