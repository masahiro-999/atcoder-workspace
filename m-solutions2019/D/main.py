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
ab = [LII() for _ in range(N-1)]
C = LII()

C.sort(reverse=True)

g = defaultdict(set)

for a,b in ab:
    a -= 1
    b -= 1
    g[a].add(b)
    g[b].add(a)

leaf=[]
ans = [-1]*N

for i in range(N):
    if len(g[i])==1:
        leaf.append(i)

while leaf:
    q = []
    for n in leaf:
        ans[n] = C.pop()
        # print(n,ans[n])
        if g[n]:
            prev = g[n].pop()
            g[prev].discard(n)
            g[n].discard(prev)
            if len(g[prev])==1:
                q.append(prev)
    leaf = q

sm = 0
for a,b in ab:
    a -= 1
    b -= 1
    sm += min(ans[a],ans[b])    

print(sm)
print(*ans)
