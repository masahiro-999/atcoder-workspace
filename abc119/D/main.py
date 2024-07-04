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


A,B,Q = LII()
S = [II() for _ in range(A)]
T = [II() for _ in range(B)]
X = [II() for _ in range(Q)]

def find_near(a,x):
    i = bisect_left(a,x)
    if i == 0:
        return [a[0]]
    if i == len(a):
        return [a[i-1]]
    d1 = x- a[i-1]
    d2 = a[i] - x
    if d1 < d2:
        return [a[i-1],a[i]]
    else:
        return [a[i],a[i-1]]

for x in X:
    ans = inf
    for s,t in [(S,T),(T,S)]:
        x_list = find_near(s,x)
        for x0 in x_list:
            x1 = find_near(t,x0)[0]
            d = abs(x-x0)+abs(x0-x1)
            ans = min(ans,d)
    print(ans)