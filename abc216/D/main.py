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

A = []
for _ in range(M):
    k = II()
    A.append(LII())

color_pos = [-1]*N

pos=[0]*M

q = []
for i in range(M):
    q.append(i)

while q:
    i = q.pop()
    c = A[i][pos[i]]-1
    same_m = color_pos[c]
    if same_m == -1:
        color_pos[c]=i
    else:
        pos[i]+=1
        if pos[i]<len(A[i]):
            q.append(i)
        pos[same_m]+=1
        if pos[same_m]<len(A[same_m]):
            q.append(same_m)

ans = "Yes"
for i in range(M):
    if pos[i] < len(A[i]):
        ans = "No"

print(ans)