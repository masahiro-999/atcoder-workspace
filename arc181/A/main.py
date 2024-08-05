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
    N = II()
    P = LII()

    can_1 = False
    can_0 = True
    max_p = -1
    for i in range(N):
        max_p = max(max_p,P[i])
        if max_p <= i+1 and P[i] == i+1:
                can_1 = True
        if P[i] != i+1:
            can_0 = False


    if can_0:
        ans = 0
    elif can_1:
        ans = 1
    else:
        if P[0]==N and P[-1]== 1:
            ans = 3
        else:
            ans = 2
    print(ans)
