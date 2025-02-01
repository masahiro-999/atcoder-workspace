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

N,Q = LII()


hato_su = list(range(1,N+1))
su_hato = defaultdict(set)
for i in range(1,N+1):
    su_hato[i].add(i)

ans  = 0
for _ in range(Q):
    x = LII()
    if x[0] == 1:
        p,h = x[1:]
        before_su = hato_su[p-1]
        hato_su[p-1] = h
        su_hato[before_su].remove(p)
        if len(su_hato[before_su]) == 1:
            ans -= 1
        su_hato[h].add(p)
        if len(su_hato[h]) == 2:
            ans += 1
    else:
        print(ans)




