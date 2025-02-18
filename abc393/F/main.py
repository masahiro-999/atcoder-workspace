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
inf = 100100100100100100100
debug = False
# debug = True
if debug:
    def dprint(*arg): print(*arg, file=sys.stderr)
else:
    def dprint(*arg): pass

N,Q = LII()
A = LII()
rx = [LII() for _ in range(Q)]

xi = defaultdict(list)

for i,(r,x) in enumerate(rx):
    xi[r-1].append((x,i))

ans = [0]*Q

lis = [inf]*N
for i,j in enumerate(A):
    k = bisect_left(lis,j)
    lis[k] = j
    for x,q_i in xi[i]:

        k = bisect_right(lis,x)
        ans[q_i] = k
        # print(q_i,x,k,lis)
print(*ans, sep="\n")