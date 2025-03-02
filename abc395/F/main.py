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
N,X = LII()
ud = [LII() for _ in range(N)]

total = 0
for u,d in ud:
    total += u+d

ud = [(u-1,d-1) for u,d in ud]


def check(n):
    lr = []
    for u,d in ud:
        if u+d<n:
            return False
        l = max(0,n-u)
        r = min(d,n)
        lr.append((l,r))
    
    l,r = lr[0]
    for i in range(1,N):
        l -= X
        r += X
        l1,r1 = lr[i]
        if r<l1 or l > r1:
            return False
        l,r = max(l1,l),min(r1,r)
    return True

ok = 0
ng = 2000000000
while ng-ok >1:
    mid = (ng+ok)//2
    if check(mid):
        ok = mid
    else:
        ng = mid

ans = total - (2+ok)*N
print(ans)