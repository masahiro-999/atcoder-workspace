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

N,M = LII()


g = [[] for _ in range(N)]

for _ in range(M):
    u,v,w = LII()
    u -= 1
    v -= 1
    g[u].append((v,w))
    g[v].append((u,w))


@bootstrap
def dfs(s,val,visited):
    visited[s] = True
    for n,w in g[s]:
        if visited[n]:
            continue
        if val != val|w:
            continue
        if n == N-1:
            yield True
        visited[n] = True
        ret = yield dfs(n,val,visited)
        visited[n] = False
        if ret:
            yield True
    yield False

def bfs(s,val,visited):
    q = []
    q.append(s)
    while q:
        s = q.pop()
        visited[s] = True
        for n,w in g[s]:
            if visited[n]:
                continue
            if val != val|w:
                continue
            if n == N-1:
                return True
            q.append(n)



ans = 2**30-1
for i in range(30)[::-1]:
    x = ans-(1<<i)
    visited = [False]*N
    ret = bfs(0, x,visited)
    # print(i,x,ret)
    if ret:
        ans =ans-(1<<i)

print(ans)

