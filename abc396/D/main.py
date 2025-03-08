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

## PYRIVAL BOOTSTRAP
# https://github.com/cheran-senthil/PyRival/blob/master/pyrival/misc/bootstrap.py
# This decorator allows for recursion without actually doing recursion
## @bootstrap, yield when getting and returning value in recursive functions, end of functions

# abc276 Eで使用した

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

g = defaultdict(list)

for _ in range(M):
    u,v,w = LII()
    u -= 1
    v -= 1
    g[u].append((v,w))
    g[v].append((u,w))

ans = inf


visited = [False]*N
visited[0] = True
# stack = [(0,0)]

# while stack:
#     p,val = stack.pop()
#     if p == N-1:
#         ans = min(ans,val)
#     else:
#         for n,w in g[p]:
#             if not visited[n]:
#                 visited[n] = True
#                 stack.append((n,val^w))
#                 visited[n] = False

# print(ans)    

@bootstrap
def dfs(p,val):
    # print(p+1,val)
    global ans
    if p == N-1:
        ans = min(ans,val)
        yield
    for n,w in g[p]:
        if not visited[n]:
            visited[n] = True
            yield dfs(n,val^w)
            visited[n] = False
    yield

dfs(0,0)

print(ans)
