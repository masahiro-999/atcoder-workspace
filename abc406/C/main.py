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

"""
12
11 3 8 9 5 2 10 4 1 6 12 7

3 8 9 5 2 10
"""

N = II()
P = LII()
S = []
POS =[]

prev_pos = 0
if P[0]>P[1]:
    S.append(1)
    POS.append(0)
else:
    S.append(2)
    POS.append(0)
for i in range(1,N-1):
    if P[i-1]>P[i]<P[i+1]:
        S.append(2)
        POS.append(i)
    if P[i-1]<P[i]>P[i+1]:
        S.append(1)
        POS.append(i)

if S[-1] == 2 and POS[-1] != N-1:
    POS.append(N-1)

# print(S)
# print(POS)

ans = 0
M = len(S)
for i in range(M):
    if i-1 >=0 and i+2< M+1 and S[i] == 1:
        ans += (POS[i] - POS[i-1]) * (POS[i+2] - POS[i+1])

print(ans)
