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

T = II()
for _ in range(T):
    N = II()
    A = LII()
    s = set()
    ng = set()
    ans = 0
    for a1,a2 in zip(A,A[1:]):
        if a1==a2:
            ng.add(a1)
    b1 = None
    b2 = None
    for a1,a2 in zip(A,A[1:]):
        if a1 > a2:
            a1,a2 = a2,a1

        if (a1,a2) in s:
            if a1 not in ng and a2 not in ng:
                ans += 1
        s.add((b1,b2))
        b1 = a1
        b2 = a2
    print(ans)        
