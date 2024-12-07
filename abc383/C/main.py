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

H,W,D = LII()
S = [I() for _ in range(H)]

visited = [[False]*W for _ in range(H)]


set_p = set()

for i in range(H):
    for j in range(W):
        if S[i][j] == "H":
            set_p.add((i,j))
            visited[i][j] = True    

while set_p and D > 0:
    next_set_p = set()
    for i,j in set_p:
        for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni,nj = i+di,j+dj
            if 0<=ni<H and 0<=nj<W and S[ni][nj] != "#" and not visited[ni][nj]:
                visited[ni][nj] = True
                next_set_p.add((ni,nj))
    set_p = next_set_p
    D -= 1


ans = 0
for i in range(H):
    for j in range(W):
        if visited[i][j]:
            ans += 1
print(ans)