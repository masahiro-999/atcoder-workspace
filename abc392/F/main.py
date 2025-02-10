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

N = II()
P = LII()

BASE = 500000

from atcoder.fenwicktree import FenwickTree

ft = FenwickTree(N)

def find_nth(n):
    ok = N
    ng = -1
    while ok-ng > 1:
        mid = (ok+ng)//2
        if mid - ft.sum(0,mid+1) >=n:
            ok = mid
        else:
            ng = mid
    return ok

# ft.add(0,1)
# print(find_nth(0))
# print(find_nth(1))
# print(find_nth(2))
# exit()
ans = [0]*N
for i in range(N)[::-1]:
    p = P[i]-1
    x = find_nth(p)
    ans[x] = i+1
    ft.add(x,1)
    # print(i,p,x,ans)
print(*ans)