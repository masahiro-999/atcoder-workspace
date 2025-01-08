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
inf = 100100100100100100100100
debug = False
# debug = True
if debug:
    def dprint(*arg): print(*arg, file=sys.stderr)
else:
    def dprint(*arg): pass

N = II()
X = LII()

PX = SortedList([x for x in X if x > 0])
NX = SortedList([x for x in X if x < 0])

mx = -inf
mi = inf

for IX in (PX,NX):
    if not IX:
        continue
    for i in range(len(IX)):
        xi = IX[i]
        IX.discard(xi)
        for JX in (PX,NX):
            if not JX:
                continue
            for j2 in range(2):
                if j2 == 0:
                    xj = JX[0]
                else:
                    xj = JX[-1]
                JX.discard(xj)
                for KX in (PX,NX):
                    if not KX:
                        continue
                    for k2 in range(2):
                        if k2 == 0:
                            xk = KX[0]
                        else:
                            xk = KX[-1]
                        a = (xi+xj+xk)/(xi*xj*xk)
                        mx = max(mx, a)
                        mi = min(mi, a)
                JX.add(xj)
        IX.add(xi)

print(mi)
print(mx)