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
A = [deque(LII()) for _ in range(N)]

s1 = set()
q = deque()


for i in range(N):
    a = i
    if not A[i]: continue
    b = A[i].popleft()-1
    if a > b:
        a,b = b,a
    if (a,b) in s1:
        s1.remove((a,b))
        q.append((a,b))
    else:
        s1.add((a,b))

# print(s1)
# print(q)
ans = 0
while q:
    nq = deque()
    while q:
        x = q.popleft()
        for i in x:
            a = i
            if not A[i]: continue
            b = A[i].popleft()-1
            if a > b:
                a,b = b,a
            if (a,b) in s1:
                s1.remove((a,b))
                nq.append((a,b))
            else:
                s1.add((a,b))
    q = nq
    ans += 1
if ans == 0:
    ans = -1
else:
    for i in range(N):
        if A[i]:
            ans = -1
print(ans)