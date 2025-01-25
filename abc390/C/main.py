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

H,W = LII()
S = [I() for _ in range(H)]

h_min = H
h_max = 0
w_min = W
w_max = 0

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            h_min = min(h_min,i)
            h_max = max(h_max,i)
            w_min = min(w_min,j)
            w_max = max(w_max,j)

ans = "Yes"
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            if h_min <= i <= h_max and w_min <= j <= w_max:
                ans = "No"

print(ans)