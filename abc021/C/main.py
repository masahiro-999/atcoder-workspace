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
a,b = LII()
a -= 1
b -= 1
M = II()
MOD = 1000000007

g = defaultdict(list)

for _ in range(M):
    x,y = LII()
    x -= 1
    y -= 1
    g[x].append(y)
    g[y].append(x)

cnt = [0]*N
dist = [-1]*N
path = [-1]*N

def bfs(s):
    q = deque()
    q.append(s)
    dist[s] = 0
    cnt[s] = 1
    while q:
        s = q.popleft()
        d = dist[s]
        for ns in g[s]:
            if dist[ns] == -1:
                dist[ns] = d+1
                path[ns] = s
                cnt[ns]+= 1
                q.append(ns)
            elif dist[ns] == d+1:
                cnt[ns]+=1

bfs(a)

# print(cnt)

ans = 1
p = b
while p !=a:
    ans *= cnt[p]
    ans %= MOD
    p = path[p]
print(ans)