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

K,N,M = LII()
A = LII()

C = []
B = []
for a,i in zip(A,count()):
    b = a*M//N

    c0 = abs(a*M-N*b)
    c1 = abs(a*M-N*(b+1))
    if c0 < c1:
        c = c1 - c0, 0, i
    else:
        c = c0 - c1, 1, i
        b = b+1
    C.append(c)
    B.append(b)
d = sum(B) - M
# print(d)
C.sort(key = lambda x: x[0])
# print(B)
# print(C)
if d > 0:
    for _,x,i in C:
        if x == 1:
            B[i] -= 1
            d -= 1
        if d == 0:
            break
elif d < 0:
    for _,x,i in C:
        if x == 0:
            B[i] += 1
            d += 1
        if d == 0:
            break

print(*B)