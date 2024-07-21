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
H,W,Y = LII()
A = [LII() for _ in range(H)]

# g = defaultdict(list)

# for i in range(H):
#     for j in range(W):
#         a  = A[i][j]
#         for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
#             x = i+dx
#             y = j+dy
#             if 0<=x<H and 0<=y<W:
#                 b = A[x][y]
#                 if a >=b:
#                     g[(i,j)].append((x,y))
#                     g[(x,y)].append((i,j))

sl = SortedList()
visited = [[False]*W for _ in range(H)]
added = [[False]*W for _ in range(H)]


q = [ deque() for _ in range(Y+1)]

n = H*W
for i in range(H):
    for j in [0,W-1]:
        a = A[i][j]
        if a <= Y:
            q[a].append((i,j))

for j in range(1,W-1):
    for i in [0,H-1]:
        a = A[i][j]
        if a <= Y:
            q[a].append((i,j))

for i in range(1,Y+1):
    # print(i, sl)
    while q[i]:
        x,y = q[i].popleft()
        if visited[x][y]:
            continue
        n -= 1
        visited[x][y] = True
        for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx = x+dx
            ny = y+dy
            if 0<=nx<H and 0<=ny<W and visited[nx][ny] == False:
                a = A[nx][ny]
                if a <= Y:
                    q[max(i,a)].append((nx,ny))

    print(n)