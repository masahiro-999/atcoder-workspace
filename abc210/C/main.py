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

N,K = LII()
C = LII()

cnt = Counter(C[:K])

ans=[]
n = len(cnt)
ans.append(n)
for i in range(1,N-K+1):
    # print(i)
    cnt[C[i-1]] -= 1
    if cnt[C[i-1]] == 0:
        n -= 1
    cnt[C[i+K-1]] += 1
    if cnt[C[i+K-1]] == 1:
        n += 1
    ans.append(n)

print(max(ans))