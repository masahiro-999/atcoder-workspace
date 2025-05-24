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

H,W = LII()

S = [[0]*W for _ in range(H)]
T = [[0]*W for _ in range(H)]

for i in range(H):
    a = LII()
    for j in range(W):
        S[i][j] = a[j]
        T[i][j] = a[j]

ans = 0
def dfs(i,j,result):
    global ans
    if i == H and j == 0:
        ans = max(ans, result)
        return
    x = S[i][j]
    nj = j+1
    ni = i
    if nj == W:
        nj = 0
        ni = i+1 
    # print(i,j)
    if x == -1:
        dfs(ni,nj, result)
    if x != -1:
        dfs(ni,nj, result ^ x)
        S[i][j] = -1
        if i < H-1 and S[i+1][j] != -1:
            S[i+1][j] = -1
            dfs(ni,nj, result)
            S[i+1][j] = T[i+1][j]
        if j < W-1 and S[i][j+1] != -1:
            S[i][j+1] = -1
            dfs(ni,nj, result)
            S[i][j+1] = T[i][j+1]
        S[i][j] = T[i][j]

dfs(0,0,0)

print(ans)