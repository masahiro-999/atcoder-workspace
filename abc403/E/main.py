from dataclasses import dataclass
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

p = 1<<61-1
b = 975993

def rolling_hash(S):
    h = 0
    for c in S:
        h = (h*b+ord(c))%p
    return h


Q =II()
query = [LI() for _ in range(Q)]

ans = [0]*Q
xq = {}
for q,(t,s) in enumerate(query):
    if t == "1":
        x = rolling_hash(s)
        if x not in xq:
            xq[x] = q

for q,(t,s) in enumerate(query):
    if t == "2":
        ans[q] +=1
        h = 0
        a = inf
        for c in s:
            h = (h*b+ord(c))%p
            if h in xq:
                a = min(a,xq[h])
        if a != inf:
            ans[max(q,a)] -= 1
ans = list(accumulate(ans))
print(*ans, sep="\n")