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
S = [I() for _ in range(N)]
T = [I() for _ in range(N)]

def rot(A):
    return list(zip(*A))[::-1]

def find_area(A):
    i_min,j_min = inf,inf
    i_max,j_max = -inf,-inf
    for i in range(N):
        for j in range(N):
            if A[i][j] == "#":
                i_min = min(i_min,i)
                j_min = min(j_min,j)
                i_max = max(i_max,i)
                j_max = max(j_max,j)
    return i_min, j_min, i_max - i_min + 1, j_max - j_min +1

ti,tj,ti_size,tj_size = find_area(T)

ans = "No"
for i in range(4):
    si,sj,si_size,sj_size = find_area(S)

    if ti_size ==si_size and tj_size==sj_size:
        ok = True
        for i in range(ti_size):
            for j in range(tj_size):
                if S[si+i][sj+j] != T[ti+i][tj+j]:
                    ok = False
        if ok:
            ans = "Yes"
            break
    S = rot(S)

print(ans)