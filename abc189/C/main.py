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
from itertools import product, accumulate,permutations,combinations, count, groupby
input = lambda: sys.stdin.readline().rstrip("\r\n")
I = input
II = lambda: int(I())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
sys.setrecursionlimit(10000000)
inf = 100100100100100100100
debug = False
# debug = True
if debug:
    def dprint(*arg): print(*arg, file=sys.stderr)
else:
    def dprint(*arg): pass

N = II()
A = LII()

from atcoder.dsu import DSU
dsu = DSU(N)

table = defaultdict(list)
for i,a in enumerate(A):
    table[a].append(i)

ans = 0
for k in sorted(table.keys(), reverse=True):
    for v in table[k]:
        if (v+1 <N and A[v] <= A[v+1]):
            dsu.merge(v,v+1)
        if (v-1 >=0 and A[v] <= A[v-1]):
            dsu.merge(v,v-1)
        ans = max(ans,k*dsu.size(v))

print(ans)
