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

from atcoder.lazysegtree import LazySegTree

N = II()
A = LII()


e = inf
id_ = 0

def mapping(func, ele):
    return func + ele


def composition(func_upper, func_lower):
    return func_upper + func_lower

seg = LazySegTree(min, e, mapping, composition, id_, A)

ans = [0]*N

nokori = N
for i in range(N):
    nokori -= 1
    x = seg.get(i)
    move = min(x,nokori)
    a = x - move
    # print(i,x,move,a)
    seg.apply(i+1,i+move+1,1)
    # for i in range(N):
    #     print(seg.get(i),end=" ")
    # print()
    ans[i] = a

print(*ans)