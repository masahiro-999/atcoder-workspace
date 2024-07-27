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
a = LII()
a.sort()
bk = [LII() for _ in range(Q)]

def dist(b,d):
    # bからの距離がdの範囲に何個Aがあるか
    d1 = b+d
    d2 = b-d
    l = bisect_left(a,d2)
    r = bisect_right(a,d1)
    return r-l

# print(dist(0,0))
# print(dist(0,1))
# print(dist(0,2))
# print(dist(0,3))

for b,k in bk:
    if dist(b,0) >= k:
        print(0)
        continue    
    l = 0
    r = 2*10**8+1
    while r-l > 1:
        m = (r+l)//2
        if dist(b,m) >= k:
            r = m
        else:
            l = m
    print(r)

