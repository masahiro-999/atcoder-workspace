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
inf = 100100100100100100
debug = False
# debug = True
if debug:
    def dprint(*arg): print(*arg, file=sys.stderr)
else:
    def dprint(*arg): pass
Q,A,B = LII()

tab = [LII() for _ in range(Q)]

s = SortedSet([A-B, A+B])

for t,a,b in tab:
    if t == 1:
        s.add(a+b)
        s.add(a-b)
    else:
        i = s.bisect_left(a)
        j = s.bisect_right(b)
        if i <= j-1:
            ans = 0
        else:
            if i > 0:
                ans = a - s[i-1]
            else:
                ans = inf
            if j < len(s):
                ans = min(ans, s[j]-b)
        print(ans)
