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
# debug = False
if debug:
    def dprint(*arg): print(*arg, file=sys.stderr)
else:
    def dprint(*arg): pass

H,W,Q = LII()
RC = [LII() for _ in range(Q)]

HT = [SortedSet(range(W)) for _ in range(H)]
VT = [SortedSet(range(H)) for _ in range(W)]
for r,c in RC:
    r -= 1
    c -= 1
    i = HT[r].bisect_left(c)
    if i < len(HT[r]) and HT[r][i] == c:
        HT[r].remove(c)
    else:
        if i < len(HT[r]):
            a = HT[r][i]
            HT[r].remove(a)
            VT[a].remove(r)
        if i > 0:
            b = HT[r][i-1]
            HT[r].remove(b)
            VT[b].remove(r)
    j = VT[c].bisect_left(r)
    if j < len(VT[c]) and VT[c][j] == r:
        VT[c].remove(r)
    else:
        if j < len(VT[c]):
            a = VT[c][j]
            VT[c].remove(a)
            HT[a].remove(c)
        if j > 0:
            b = VT[c][j-1]
            VT[c].remove(b)
            HT[b].remove(c)
    dprint(r,c)
    dprint(i,j)
    dprint(HT)
    dprint(VT)
# 残っている壁の個数
ans = 0
for i in range(H):
    ans += len(HT[i])
print(ans)