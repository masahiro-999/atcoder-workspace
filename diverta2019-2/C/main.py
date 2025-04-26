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


N = II()
A = LII()

if max(A)<0:
    A.sort(reverse=True)
elif min(A)>=0:
    A.sort()
else:
    A.sort()
    if len(A)>2:
        A[1],A[-1] = A[-1],A[1]

dp = [[0]*2  for _ in range(N)]

dp[0][0] = A[0]
dp[0][1] = A[0]

for i in range(1,N):
    a = dp[i-1][0]-A[i]
    b = dp[i-1][1]-A[i]
    dp[i][0] = a if abs(a)>abs(b) else b

    a = A[i] - dp[i-1][0]
    b = A[i] - dp[i-1][1]
    dp[i][1] = a if abs(a)>abs(b) else b

ans = max(dp[N-1])

a = []
val = ans
for i in range(N)[::-1]:
    if dp[i][0] == val:
        y = A[i]
        x = val+y
        a.append((x,y))
        val = x
    else:
        x = A[i]
        y = x-val
        a.append((x,y))
        val = y

print(ans)
for x,y in a[::-1][1:]:    
    print(x,y)