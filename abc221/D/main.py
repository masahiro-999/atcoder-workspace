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

N = II()
ab = [LII() for _ in range(N)]

A = [a for a,b in ab]
B = [a+b for a,b in ab]

points = list(sorted(set(A+B)))
back = {v:i for i,v in enumerate(points)}

table = [0]*len(points)

for a,b in ab:
    point_a = back[a]
    point_b = back[a+b]
    table[point_a]+=1
    table[point_b]-=1

sm = 0
ans = [0]*(N+1)
for i in range(len(points)-1):
    sm += table[i]
    ans[sm] += points[i+1]-points[i]

print(*ans[1:])