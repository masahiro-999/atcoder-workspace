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

N = II()
X = LII()
P = LII()
Q = II()

lr= [LII() for _ in range(Q)]

A = set(X)
for l,r in lr:
    A.add(l)
    A.add(r)

TMP = { x: i for i,x in enumerate(sorted(A))}

ft = FenwickTree(len(TMP))

X = [TMP[x] for x in X]

for x,p in zip(X,P):
    ft.add(x,p)

for l,r in lr:
    l = TMP[l]
    r = TMP[r]
    print(ft.sum(l,r+1))
