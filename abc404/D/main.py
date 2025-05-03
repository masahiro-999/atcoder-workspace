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

N,M = LII()
C = LII()
T =[[] for _ in range(N)]

for i in range(M):
    a = LII()
    for x in a[1:]:
        x -= 1
        T[x].append(i)

ans = inf
for X in product(range(3), repeat=N):
    cost = 0
    animal = [0]*M
    for i,x in enumerate(X):
        cost += C[i]*x
        if x > 0:
            for ani in T[i]:
                animal[ani] += x
    ok = True
    for n in animal:
        if n <2:
            ok = False
            break
    if ok:
        ans = min(ans, cost)

print(ans)