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

from types import GeneratorType

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

M = II()
N = 9
uv = [LII() for _ in range(M)]
P = LII()

p = tuple([x-1 for x in P])


def find_free_i(p):
    free = [1]*N
    for i in p:
        free[i]=0
    for i in range(N):
        if free[i]==1:
            return i

g = [set() for _ in range(N)]

for u,v in uv:
    u -= 1
    v -= 1
    g[u].add(v)
    g[v].add(u)

visited = set()

gole = tuple(range(8))

def bfs(p):
    q = deque()
    free_i = find_free_i(p)
    q.append((p,free_i,0))
    visited.add(p)
    while q:
        p,free_i,cnt = q.popleft()
        if p == gole:
            return cnt
        for i,v in enumerate(p):
            if free_i in g[v]:
                np = list(p)
                np[i] = free_i
                tuple_np = tuple(np)
                if tuple_np in visited:
                    continue
                visited.add(tuple_np)
                q.append((tuple_np,v,cnt+1))
    return -1

ans = bfs(p)
print(ans)