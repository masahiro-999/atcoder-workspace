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

N = II()
A = LII()

A.sort()

def f(x):
    sm = 0
    for a in A:
        if 2*x < a:
            sm += a-x
        else:
            sm += x
    return sm/N

max_x = A[-1]/2

l = 0
r = max_x
while (r-l) > 0.0000001:
    mid1 = l+(r-l)/3
    mid2 = r-(r-l)/3
    if f(mid1) > f(mid2):
        l = mid1
    else:
        r = mid2
    # print(l,r,r-l)
# d = max_x /100
# ans = inf
# for i in range(100+1):
#     a = f(i*d)
#     ans = min(ans, a)
#     print(a, d*i)

print(f(mid1))