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

N,X = LII()

l = (N-1)//2
r = l+1
rev = False
if l+1 == X:
    X = -1
elif r+1 == X:
    rev = True
    X = -1

A = []
for i in range(1,N+1):
    if i == X:
        continue
    A.append(i)

# print(X)
ans = []
if X !=-1:
    ans.append(X)

l = (len(A)-1)//2
r = l+1
while True:
    if rev:
        if r <len(A):
            ans.append(A[r])
            r += 1
        if l >=0:
            ans.append(A[l])
            l -= 1
    else:
        if l >=0:
            ans.append(A[l])
            l -= 1
        if r <len(A):
            ans.append(A[r])
            r += 1
    if l<0 and r==len(A):
        break

print(*ans)