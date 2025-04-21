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

N,M = LII()
A = []
for _ in range(M):
    ka = LII()
    a = ka[1:]
    A.append(a)

B = LII()

back_b =[0]*N
for i,b in enumerate(B):
    back_b[b-1] = i+1

last_day = [0]*M

for i in range(M):
    a = A[i]
    mx = -1
    for x in a:
        mx = max(mx,back_b[x-1])
    last_day[i] = mx

last_day.sort()
# print(last_day)
q = deque(last_day)
ans = 0
for i in range(1,N+1):
    while q and q[0]<=i:
        q.popleft()
        ans += 1
    print(ans)
