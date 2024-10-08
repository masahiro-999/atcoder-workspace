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

H,W,C,Q = LII()

tnc = [LII() for _ in range(Q)]

TH = defaultdict(bool)
TW = defaultdict(bool)

ans = [0]*C
remain_h = H
remain_w = W
for t,n,c in tnc[::-1]:
    if t == 1:
        if TH[n] == False:
            ans[c-1] += remain_w
            remain_h -=1
            TH[n] = True
    else:
        if TW[n] == False:
            ans[c-1] += remain_h
            remain_w -= 1
            TW[n] = True

print(*ans)