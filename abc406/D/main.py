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

H,W,N = LII()
xy = [LII() for _ in range(N)]
Q = II()


h_sum = [0]*H
w_sum = [0]*W

hh = [[] for _ in range(H)]
ww = [[] for _ in range(W)]

for x,y in xy:
    x -= 1
    y -= 1
    h_sum[x]+= 1
    w_sum[y]+= 1
    hh[x].append(y)
    ww[y].append(x)

del_h = set()
del_w = set()

q = [LII() for _ in range(Q)]

# print(h_sum, w_sum)

for cmd,val in q:
    val -= 1
    if cmd == 1:
        print(h_sum[val])
        if val not in del_h:
            h_sum[val] = 0
            del_h.add(val)
            for i in hh[val]:
                if i not in del_w:
                    w_sum[i] -= 1
    else:
        print(w_sum[val])
        if val not in del_w:
            w_sum[val] = 0
            del_w.add(val)
            for i in ww[val]:
                if i not in del_h:
                    h_sum[i] -= 1
    # print(h_sum, w_sum)
