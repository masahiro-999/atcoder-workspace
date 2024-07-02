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
inf = 100100100100100100
debug = False
# debug = True
if debug:
    def dprint(*arg): print(*arg, file=sys.stderr)
else:
    def dprint(*arg): pass

N,K = LII()
V = LII()

ans = -inf
for i in range(0,min(K,N)+1):
    x = K - i
    for j in range(0,x+1):
        if i+j>N or i+j>K:
            break
        if j > 0:
            v = V[:i]+V[-j:]
        else:
            v = V[:i]
        v.sort()
        neg = [x for x in v if x <0]
        k = K - i -j
        a = sum(v) - sum(neg[:k])
        # if a > ans:
        #     print(i,j,k,v,neg,a)
        ans = max(ans, a)

print(ans)