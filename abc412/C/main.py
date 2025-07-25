import sys
import os
from math import ceil, floor, sqrt, pi, factorial, gcd,lcm,sin,cos,tan,asin,acos,atan2,exp,log,log10, isqrt, comb
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cmp_to_key, lru_cache, reduce, cache
from operator import add, iand, ior, itemgetter, mul, xor
from string import ascii_lowercase, ascii_uppercase, ascii_letters
from typing import *
from bisect import bisect, bisect_left, bisect_right
from heapq import heapify, heappop, heappush, heappushpop, nlargest, nsmallest
from sortedcontainers import SortedSet, SortedList, SortedDict
from itertools import product, accumulate,permutations,combinations, count, groupby
input = lambda: sys.stdin.readline().rstrip("\r\n")
I = input
II = lambda: int(I())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
sys.setrecursionlimit(10000000)
inf = float('inf')
T = II()
for _ in range(T):
    N = II()
    S = LII()
    SS = S[1:-1]
    SS.sort()
    s = S[0]
    e = S[-1]
    ans = 2
    while True:
        if 2*s >= e:
            break
        i = bisect_right(SS,2*s)
        if i == 0:
            ans = -1
            break
        ns = SS[i-1]
        if ns == s:
            ans = -1
            break
        s = ns
        ans += 1
    print(ans)