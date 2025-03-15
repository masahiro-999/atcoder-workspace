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

N = II()

# def find(n):
#     ok = 1
#     ng = N
#     while ng-ok>1:
#         x = (ok+ng)//2
#         if n**3+3*n*n*x+3*n*x*x <= N:
#             ok = x
#         else:
#             ng = x
#     return ok

# print(find(26))

N3 = int((N+1)**(1/3))

for n in range(1,N3):
    x = 0
    if n**3+3*n*n*x+3*n*x*x > N:
        break
    ok = 0
    ng = isqrt(N)
    while ng-ok>1:
        x = (ok+ng)//2
        if n**3+3*n*n*x+3*n*x*x <= N:
            ok = x
        else:
            ng = x
    x = ok
    if N == n**3+3*n*n*x+3*n*x*x:
        print(x+n,x)
        exit()

print(-1)
