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

n,m,d = LII()

def solv(n,m,d):
    sm = 0
    for X in product(range(n), repeat=m):    
        for x1,x2 in zip(X,X[1:]):
            sm += 1 if abs(x1-x2)==d else 0
    return sm/n**m

def solv2(n,m,d):
    ans = 2*(n-d)*(m-1)/n/n
    return ans

# for n in [2,4,6]:
#     for d in range(n):
#         for m in [2,3,4]:
#             ans1 = solv(4,6,2)
#             ans2 = solv2(4,6,2)
#             if ans1 != ans2:
#                 print(ans1)
#                 print(ans2)

ans = solv2(n,m,d)
if d == 0:
    ans /= 2
print(ans)