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

N,a,b = LII()
A = LII()

A.sort()

def check(x):
    na = 0
    nb = 0
    for i in range(N):
        if A[i]<x:
            na += ((x-A[i])+a-1)//a
        else:
            break
    for i in range(N)[::-1]:
        if A[i] > x:
            nb += (A[i]-x)//b
        else:
            break
    return na <= nb

l = A[0]
r = A[-1]
while r -l >1:
    mid = (l+r)//2
    if check(mid):
        l = mid
    else:
        r = mid

print(l)