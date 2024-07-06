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
abc = [LII() for _ in range(N-1)]


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

dist = [-1]*(N+1)

@bootstrap
def dfs(g, start, prev):
    for i,c in g[start]:
        if i == prev:
            continue
        dist[i] = dist[start]+c
        yield dfs(g,i,start)
    yield
# def bfs(g, start):
#     dist = [-1]*(N+1)
#     que = deque([start])
#     dist[start] = 0
#     while que:
#         i = que.popleft()
#         d = dist[i]
#         for j,c in g[i]:
#             if dist[j] != -1:
#                 continue
#             dist[j] = d+c
#             que.append(j)
#     return dist

g = defaultdict(list)
total_c = 0
for a,b,c in abc:
    a -= 1
    b -= 1
    g[a].append((b,c))
    g[b].append((a,c))
    total_c += c

dist[0] = 0
dfs(g,0, -1)
n1 = dist.index(max(dist))
dist[n1] = 0
dfs(g, n1, -1)
ans = total_c*2 - max(dist)
print(ans)
