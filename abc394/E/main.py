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

C = [I() for _ in range(N)]

D = [x for x in zip(*C)]

ans= [[inf]*N for _ in range(N)]

q = []

for i in range(N):
    for j in range(N):
        if C[i][j] != "-":
            ans[i][j] = 1
            heappush(q,(1,j,i))
    ans[i][i] = 0
    heappush(q,(0,i,i))

def create_table(C):
    ret = []
    for i in range(N):
        x = defaultdict(list)
        for j,c in enumerate(C[i]):
            if c != "-":
                x[c].append(j)
        ret.append(x)
    return ret

table_c = create_table(C)
table_d = create_table(D)

def f(q):
    while q:
        l,s,t = heappop(q)
        c = table_c[s]
        d = table_d[t]
        # print(s,c)
        # print(t,d)
        for k in set(c.keys()) & set(d.keys()):
            for x in c[k]:
                for y in d[k]:
                    # print(k,x,y,l+2)
                    if ans[y][x] == inf:
                        ans[y][x] = l+2
                        q.append((l+2,x,y))
# print(q)
# q = []
# heappush(q,(1,0,3))
f(q)

for i in range(N):
    for j in range(N):
        if ans[i][j] == inf:
            ans[i][j] = -1

for a in ans:
    print(*a)