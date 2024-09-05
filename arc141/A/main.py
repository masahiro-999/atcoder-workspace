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
    n = II()
    str_n = str(n)
    keta = len(str_n)
    ans = int("9" * (keta-1))
    for i in range(1,keta):
        if keta % i != 0:
            continue
        m = str_n[:i]
        mm = int(m * (keta//i))
        if mm <= n:
            ans = max(ans, mm)
        else:
            m = str(int(m) - 1)
            if m == "0":
                continue
            if i == len(m):
                a = int(m * (keta//i))
                ans = max(ans, a)
    print(ans)

