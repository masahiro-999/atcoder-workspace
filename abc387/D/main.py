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

S1 = [[x for x in X] for X in S]
S2 = [[x for x in X] for X in S]

for i in range(H):
    for j in range(W):
        if S[i][j] == "S":
            si,sj = i,j
        if S[i][j] == "G":
            gi,gj = i,j

# dir 0: up,down
# dir 1: left,right

# def bfs(s,t):
#     q = deque()
#     dist = [[-1]*W for _ in range(H)]
#     q.append(s)
#     dist[s[0]][s[1]] = 0
#     while q:
#         i,j = q.popleft()
#         X = [(i+dx,j+dy) for dx,dy in dxdy1]
#         for ni,nj in chain(X, g[A[i][j]]):
#             if ni<0 or nj<0 or ni>=H or nj>=W:
#                 continue
#             if A[ni][nj] == "#":
#                 continue
#             if dist[ni][nj]!=-1:
#                 continue
#             dist[ni][nj] = dist[i][j]+1
#             q.append((ni,nj))
#         if "a" <=A[i][j] <="z":
#             g[A[i][j]] = []
#     return(dist[t[0]][t[1]])

def bfs(i,j,initial_dir):
    dist = [[-1]*W for _ in range(H)]    
    q = deque()
    q.append((i,j,initial_dir))
    dist[i][j] = 0
    while q:
        i,j,dir = q.popleft()
        # print(i+1,j+1,dir,dist[i][j])
        d = dist[i][j]
        if dir:
            didj = [(0,1),(0,-1)]
        else:
            didj = [(1,0),(-1,0)]
        for di,dj in didj:
            ni,nj = i+di,j+dj
            if ni<0 or nj<0 or ni>=H or nj>=W:
                continue
            if S[ni][nj] == "#":
                continue
            if dist[ni][nj] != -1:
                continue
            dist[ni][nj] = d+1
            if S[ni][nj] == "G":
                return dist[ni][nj]
            q.append((ni,nj,1-dir))
    return dist[gi][gj]

ans1 = bfs(si,sj,0)
ans2 = bfs(si,sj,1)

# print(ans1,ans2)
if ans1 != -1 and ans2 != -1:
    print(min(ans1,ans2))
else:
    if ans1 == -1:
        print(ans2)
    else:
        print(ans1)

