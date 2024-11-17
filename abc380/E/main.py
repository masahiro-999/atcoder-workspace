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

from atcoder.lazysegtree import LazySegTree


N, Q = LII()

group = [i for i in range(N)]
color = [i for i in range(N)]
left = [i for i in range(N)]
right = [i for i in range(N)]
num_color = [1 for i in range(N)]

def marge(i,j):
    if right[i]-left[i] > right[j]-left[j]:
        i,j = j,i
    # i -> j
    to_g = j
    from_g = i
    # print(i,j,from_g,to_g)
    for x in range(left[from_g], right[from_g]+1):
        group[x] = to_g
        # print("change", x,to_g)
    left[to_g] = min(left[from_g], left[to_g])
    right[to_g] = max(right[from_g], right[to_g])
for _ in range(Q):
    q = LII()
    if q[0] == 1:
        x,c = q[1:]
        x -= 1
        c -= 1
        change_n = right[group[x]]-left[group[x]]+1
        prev_c = color[group[x]]
        num_color[prev_c] -= change_n
        color[group[x]] = c
        num_color[c] += change_n
        l = left[group[x]]
        r = right[group[x]]
        if l > 0 and color[group[l-1]] == color[group[l]]:
            marge(group[l-1],group[l])
        if r+1 <N and color[group[r]] == color[group[r+1]]:
            marge(group[r],group[r+1])
        # print(group,color,left,right,num_color)
    else:
        print(num_color[q[1]-1])
