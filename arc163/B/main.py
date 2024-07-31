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
A = LII()

a0 = A[0]
a1 = A[1]
n = a1-a0+1

A = A[2:]
A.sort()
N = len(A)

def check(x):
    n0 =bisect_left(A,a0-x)
    n1 =bisect_left(A,a0)
    # print(x,n0,n1)
    for i in range(n0,min(N,n1+1)):
        if i+M-1 >=N:
            continue
        b = A[i+M-1]
        xx = max(0,a0-A[i])
        if b <= a1+(x-xx):
            return True
    return False

# print(check(0))
# print(check(1))
# print(check(2))
# print(check(3))
# print(check(4))
# print(check(34))
# print(check(35))
# print(check(36))



l = -1
r = 10**9*2
while r-l>1:
    mid = (l+r)//2
    if check(mid):
        r = mid
    else:
        l = mid
print(r)