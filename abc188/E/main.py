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

N,M = LII()
A = LII()
XY = [LII() for _ in range(M)]

mx = A[:]
mi = A[:]

f = defaultdict(set)
f2 = defaultdict(set)
b = defaultdict(set)
b2 = defaultdict(set)

leaf_f = []
leaf_b = []

for x,y in XY:
    x -= 1
    y -= 1
    f[x].add(y)
    f2[x].add(y)
    b[y].add(x)
    b2[y].add(x)

for i in range(N):
    if len(b[i]) ==0:
        leaf_f.append(i)
    if len(f[i]) ==0:
        leaf_b.append(i)

dprint(leaf_f)

for i in leaf_f:
    mx[i] = -inf

for i in leaf_b:
    mi[i] = inf

def find_mi(f,b,leaf_f,mi,min):
    while leaf_f:
        i = leaf_f.pop()
        a = mi[i]
        dprint(i,a)
        for ni in f[i]:
            b[ni].remove(i)
            mi[ni] = min(a,mi[ni])
            if len(b[ni])==0:
                leaf_f.append(ni)                

find_mi(f,b2,leaf_f,mi,min)
find_mi(b,f,leaf_b,mx,max)

dprint(A)
dprint(mi)
dprint(mx)

ans = -inf
for i in range(N):
    if len(f2[i])>0:
        a = mx[i]-mi[i]
        ans = max(a,ans)

print(ans)