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

N,Q = LII()
lrc = [LII() for _ in range(Q)]

from atcoder.dsu import DSU
dsu = DSU(N+Q)
used = [False] * N

ss = SortedSet()
for i in range(N):
    ss.add(i)

def merge(l,r):
    # ssは、区間の始まりをもっている。[l:r]があたえられたら、その区間に含まれる区間の数を返し、ssからその区間とかぶる区間を一つの区間にまとめる
    l = ss.bisect_right(l)-1
    r = ss.bisect_right(r)-1
    # print(l,r)
    if r == N:
        r = N-1
    for i in range(r,l,-1):
        del ss[i]
    return r-l+1

# ss = SortedSet([0,3,9,11])
# n = merge(6,8)
# print(n,ss)
# exit()

lrc.sort(key=lambda x: x[2])
ans = 0
for l,r,c in lrc:
    l -= 1
    r -= 1
    n = merge(l,r)
    # print(ss)
    ans += c*n

if len(ss)>1:
    ans = -1

print(ans)