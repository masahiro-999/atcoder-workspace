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

from atcoder.fenwicktree import FenwickTree


N,M = LII()

N = N*2
ab = []

lookup = [[] for _ in range(N)]
ft = FenwickTree(N)
sm = [0]*N

for i in range(M):
    a,b = LII()
    if a>b:
        a,b = b,a
    a -= 1
    b -= 1
    ab.append((a,b))
    sm[a]=1
    sm[b]=-1

sm = list(accumulate(sm, initial=0))

ab.sort(key=lambda x:x[1], reverse=True)

Q = II()
cd = []

for i in range(Q):
    c,d = LII()
    c -= 1
    d -= 1
    cd.append((i,c,d))
cd.sort(key=lambda x:x[2])
ans = [0]*Q
# print(ab)
# print(cd)
for i,c,d in cd:
    while ab:
        if ab[-1][1] >d:
            break
        a,b = ab.pop()
        ft.add(a,1)
        ft.add(b,-1)

    initial_in = ft.sum(0,c)
    ans[i] = sm[d+1] - sm[c] + initial_in*2

print(*ans, sep="\n")