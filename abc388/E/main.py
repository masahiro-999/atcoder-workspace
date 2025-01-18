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

N = II()
A = LII()

def f(n):
    j = n
    for i in range(n):
        while j < N and A[j] < A[i]*2:
            j += 1
        if j == N:
            return i
        j += 1
    return n

# for i in range(N+1):
#     print(i,f(i))


l  = 0
r = N+1

while r-l > 2:
    m1 = (2*l+r)//3
    m2 = (l+2*r)//3
    f1 = f(m1)
    f2 = f(m2)
    if f1 < f2:
        l = m1
    else:
        r = m2
    # print(l,r,m1,m2,f1,f2)
ans = max(f(m1),f(m2))
print(ans)