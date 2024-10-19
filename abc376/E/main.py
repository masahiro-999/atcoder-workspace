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

T = II()
for _ in range(T):
    N,K = LII()
    A = LII()
    B = LII()
    C = [(a,b) for a,b in zip(A,B)]
    C.sort()
    # print("C",C)
    ss = SortedList()
    for i,(a,b) in enumerate(C):
        if i < K:
            ss.add(b)
            if i == K -1:
                sm = sum(ss)
                ans = sm * a
                # print("start",sm,ss,ans)
            continue
        if b < ss[K-1]:
            sm = sm - ss[K-1] + b
        ss.add(b)
        # print(i,a,b,sm,ss)
        ans = min(ans, sm * a)
    print(ans)