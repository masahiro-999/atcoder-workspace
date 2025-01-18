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

R = II()

R = R*2

def f(x,y):
    return x**2+y**2<=R**2

def find_x(n):
    ok = 0
    ng = 10**7
    while ng-ok > 1:
        mid = (ok+ng)//2
        if f(n,mid):
            ok = mid
        else:
            ng = mid
    return ok

ans = 0
for i in range(1,R,2):
    max_x = find_x(i)
    if max_x % 2 == 0:
        max_x -= 1
    # print(i,max_x)
    if i !=1:
        max_x *= 2
    ans += max_x

print(ans)