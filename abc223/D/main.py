import sys
import os
from math import ceil, floor, sqrt, pi, factorial, gcd,lcm,sin,cos,tan,asin,acos,atan2,exp,log,log10, isqrt, comb
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cmp_to_key, lru_cache, reduce, cache
from operator import add, iand, ior, itemgetter, mul, xor
from string import ascii_lowercase, ascii_uppercase, ascii_letters
from typing import *
from bisect import bisect, bisect_left, bisect_right
from heapq import heapify, heappop, heappush, heappushpop, nlargest, nsmallest
from sortedcontainers import SortedSet, SortedList, SortedDict
from itertools import product, accumulate,permutations,combinations, count, groupby
input = lambda: sys.stdin.readline().rstrip("\r\n")
I = input
II = lambda: int(I())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
sys.setrecursionlimit(10000000)
inf = float('inf')
N,M = LII()
ab = [LII() for _ in range(M)]


forward = [set() for _ in range(N)]
back = [set() for _ in range(N)]

for a,b in ab:
    a-=1
    b-=1
    forward[a].add(b)
    back[b].add(a)

q = []
for i in range(N):
    if len(back[i])==0:
        heappush(q,i)
ans = []
while q:
    i = heappop(q)
    ans.append(i+1)
    for n in forward[i]:
        back[n].remove(i)
        if len(back[n])==0:
            heappush(q,n)

if not ans or len(ans)!=N:
    print(-1)
else:
    print(*ans)