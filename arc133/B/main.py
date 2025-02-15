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
Q = LII()

back_p = [0]*(N+1)

for i,p in enumerate(P):
    back_p[p] = i

multiple_table = defaultdict(list)

for i in range(1,N+1):
    n = i
    while n <= N:
        multiple_table[n].append(i)
        n += i

from atcoder.lazysegtree import LazySegTree

INF = 1 << 63
ID = INF


def op(ele1, ele2):
    return max(ele1, ele2)


def mapping(func, ele):
    if func == ID:
        return ele
    else:
        return func


def composition(func_upper, func_lower):
    if func_upper == ID:
        return func_lower
    else:
        return func_upper

# TODO (初期リストlst)
seg = LazySegTree(op, 0, mapping, composition, INF, N)

for i in range(N):
    q = Q[i]
    update = []
    for x in multiple_table[q]:
        index = back_p[x]
        current = seg.get(index)
        update.append((index, max(current, seg.prod(0,index)+1)))
    for i,v in update:
        seg.set(i, v)
    # print([seg.get(i) for i in range(N)])
ans = seg.prod(0,N)
print(ans)