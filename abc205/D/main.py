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

N,Q = LII()
A = LII()
A.append(10**18+N+1)
B=[]
C=[]
prev_now = 0
x = 1
for i,now in enumerate(A,start=1):
    can_use = now - prev_now -1
    if can_use > 0:
        B.append(x)
        C.append(prev_now+1)
        x += can_use
    prev_now = now
# print(B)

for _ in range(Q):
    K = II()
    i = bisect_right(B,K)
    if i == 0:
        x,y = 1,1
    else:
        x,y = B[i-1],C[i-1]
    ans = y+(K-x)
    print(ans)