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
X = LII()
A = LII()

if sum(A) != N:
    print(-1)
    exit()

XA = [(x,a) for a,x in zip(A,X)]
XA.sort(reverse=True)

e = N
i = 0
ans = 0
while e > 0 and i < M:
    x,a = XA[i]
    n0 = e - x
    n = min(n0, a)
    n1 = n0 - n 

    ans += n*(n+1)//2+(n0-n)*n
    e -= n
    if a > n:
        e -= 1
    i += 1
    # print(a,n,e,ans)
if e > 0:
    ans = -1

print(ans)