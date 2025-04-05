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

S = [I() for _ in range(H)]
si,sj,ei,ej = LII()
si -= 1
sj -= 1
ei -= 1
ej -= 1

didj = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs():
    dist = [[inf]*W for _ in range(H)]
    q = deque()
    q.append((si,sj,0))
    while q:
        i,j,d = q.popleft()
        if d >= dist[i][j]:
            continue
        dist[i][j]=d
        # print(i,j,d)
        for di,dj in didj:
            ni,nj =i+di,j+dj
            if not (0<=ni<H and 0<=nj<W):
                continue
            if S[ni][nj]==".":
                if dist[ni][nj] == inf:
                    q.appendleft((ni,nj,d))
            else:
                if dist[ni][nj] == inf:
                    q.append((ni,nj,d+1))
                ni,nj =ni+di,nj+dj
                if not (0<=ni<H and 0<=nj<W):
                    continue
                if dist[ni][nj] == inf:
                    q.append((ni,nj,d+1))

    return dist[ei][ej]

print(bfs())

# ..........
# #########.
# #.......#.
# #..####.#.
# ##....#.#.
# #####.#.#.
# .##.#.#.#.
# ###.#.#.#.
# ###.#.#.#.
# #.....#...
# 1 1 7 1