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

N,Q = LII()
PV = [LII() for _ in range(Q)]
MOD = 998244353

dir = [0]*Q

for j in range(Q):
    pj = PV[j][0]-1
    vj = PV[j][1]
    for i in range(j):
        pi = PV[i][0]-1
        vi = PV[i][1]
        
        if vj>=vi:
            continue
        if pi == pj:
            print(0)
            exit(0)
        if pi > pj:
            dir_i = -1
            dir_j = 1
        else:
            dir_i = 1
            dir_j = -1
        if (dir[i] == 0 or dir[i] == dir_i) and (dir[j]==0 or dir[j] == dir_j):
            dir[i] = dir_i
            dir[j] = dir_j
            continue
        else:
            print(0)
            exit(0)

cnt = sum(1 for x in dir if x ==0)
ans = 1<<cnt
ans %= MOD
print(ans)


