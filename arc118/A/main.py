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

t, N = LII()

Nn = N // t
Nr = N % t

if t == 1:
    ans = N*101-1
else:
    if Nn > 0:
        Nn -= 1
        Nr += t
    i = Nn*100
    prev_x = None
    cnt = 0
    while cnt < Nr:
        i += 1
        x = (100+t)*i//100
        if prev_x is None:
            prev_x = x
            continue
        if x-prev_x == 2:
            cnt += 1
            ans = prev_x+1
        prev_x = x

print(ans)

# sm = 0
# for i in range(1,t+1):
#     sm += (100+i-1)//t
#     print(i,sm, (100+t)*sm//100)
