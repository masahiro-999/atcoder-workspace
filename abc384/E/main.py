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

H,W,X = LII()
P,Q = LII()
P-= 1
Q-= 1
S = [LII() for _ in range(H)]

ans = 1
po = S[P][Q]
visited = [[False]*W for _ in range(H)]
visited[P][Q] = True

def add_4dir(i,j):
    for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
        ni = i+di
        nj = j+dj
        if 0 <= ni < H and 0 <= nj < W and visited[ni][nj] == False:
           heappush(q,(S[ni][nj],ni,nj))
 
q=[]
heapify(q)
add_4dir(P,Q)
while q:
    _,i,j = heappop(q)
    if visited[i][j]:
        continue
    if S[i][j]*X < po:
        ans += 1
        po += S[i][j]
        visited[i][j] = True
        # print(i+1,j+1,S[i][j],po)
        add_4dir(i,j)
    else:
        break

print(po)


# 388 130 971 202 487 924 247 286 237 316
# 117 166 918 106 336 928 493 391 235 398
# 124 280 425 955 212 988 227 222 307 226
# 336 302 478 246 950 368 291 236 170 101
# 370 200 204 141 287 410 388 314 205 460
# 291 104 348 337 404 399 416 263 415 339
# 105 420 302 334 231 481 466 366 401 452
# 119 432 292 403 371 417 351 231 482 184