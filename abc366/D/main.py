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
A = [[LII() for _ in range(N)] for _ in range(N)]

accA = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            accA[i+1][j+1][k+1] = A[i][j][k]
            if i > 0:
                accA[i+1][j+1][k+1] += accA[i][j+1][k+1]
            if j > 0:
                accA[i+1][j+1][k+1] += accA[i+1][j][k+1]
            if k > 0:
                accA[i+1][j+1][k+1] += accA[i+1][j+1][k]
            if i > 0 and j > 0:
                accA[i+1][j+1][k+1] -= accA[i][j][k+1]
            if i > 0 and k > 0:
                accA[i+1][j+1][k+1] -= accA[i][j+1][k]
            if j > 0 and k > 0:
                accA[i+1][j+1][k+1] -= accA[i+1][j][k]
            if i > 0 and j > 0 and k > 0:
                accA[i+1][j+1][k+1] += accA[i][j][k]

Q = II()
for _ in range(Q):
    Lx,Rx,Ly,Ry,Lz,Rz = LII()
    # AのLx,Rx,Ly,Ry,Lz,Rzの範囲の和を求める
    # 3次元累積和を使う
    ans = accA[Rx][Ry][Rz] - accA[Lx-1][Ry][Rz] - accA[Rx][Ly-1][Rz] - accA[Rx][Ry][Lz-1] + accA[Lx-1][Ly-1][Rz] + accA[Lx-1][Ry][Lz-1] + accA[Rx][Ly-1][Lz-1] - accA[Lx-1][Ly-1][Lz-1]
    print(ans)
    

            
