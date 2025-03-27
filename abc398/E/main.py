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

N = II()

g = defaultdict(list)

flag = [0]*N

uv = set()
for _ in range(N-1):
    u,v = LII()
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)
    if u > v:
        u,v = v,u
    uv.add((u,v))

def set_flag(s,color,parent):
    flag[s] = color
    for next in g[s]:
        if next == parent:
            continue
        set_flag(next, 1-color, s)

set_flag(0,0,None)

ok = set()

for j in range(N):
    for i in range(j):
        if (i,j) in uv:
            continue
        if flag[i] != flag[j]:
            ok.add((i,j))

if len(ok) %2 == 1:
    turn = "First"
else:
    turn = "Second"

used = set()
print(turn, flush=True)
if turn  == "Second":
    u,v = LII()
    u -= 1
    v -= 1
    if u>v:
        u,v = v,u
    used.add((u,v))

for u,v in ok:
    if (u,v) in used:
        continue
    print(u+1,v+1, flush=True)
    u,v = LII()
    u -= 1
    v -= 1
    if (u,v) == (-1,-1):
        exit()
    if u>v:
        u,v = v,u
    used.add((u,v))
