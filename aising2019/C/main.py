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

H,W = LII()
S = [I() for _ in range(H)]

from atcoder.dsu import DSU

dsu = DSU(H*W)

for i in range(H):
    for j in range(W):
        if i+1<H and S[i][j]!=S[i+1][j]:
            dsu.merge(i*W+j,i*W+j+W)
        if j+1<W and S[i][j]!=S[i][j+1]:
            dsu.merge(i*W+j,i*W+j+1)

ans = 0
for X in dsu.groups():
    cnt = Counter()
    for x in X:
        i,j = divmod(x,W)
        cnt[S[i][j]] += 1
    ans += cnt["."]*cnt["#"]

print(ans)    
