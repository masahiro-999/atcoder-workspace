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
P = LII()

P = [p-1 for p in P]

R = [0]*N
for i,p in enumerate(P):
    R[p] = i

def check(s,t):
    # print("check",s,t)
    x = s+1
    for i in range(t-1,s-1,-1):
        # print(x,i)
        P[i],P[i+1]=P[i+1],P[i] 
        ans.append(i+1)

s = 0
ans = []
ng = False
while s!=N-1:
    t = R[s]
    if t <= s:
        ng = True
        break
    check(s,t)
    s = t

if not ng:
    for i in range(N):
        if i != P[i]:
            ng = True
if ng:
    print(-1)
else:
    print(*ans, sep='\n')