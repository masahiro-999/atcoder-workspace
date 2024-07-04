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

N,*t = LII()

L = [II() for _ in range(N)]
t.sort()

# print(t)
ans = inf
for x in product(range(4), repeat=N):
    a = [0]*3
    b = [0]*3
    for i,sel in enumerate(x):
        if sel == 3:
            continue
        a[sel] += L[i]
        b[sel] += 1
    
    ab = [(x,y) for x,y in zip(a,b)]
    ab.sort()
    mp = 0
    for i in range(3):
        a,b = ab[i]
        if b == 0:
            mp = inf
            break
        mp += (b-1)*10+abs(t[i]-a)
    # print(ab,mp)
    ans = min(ans, mp)
print(ans)