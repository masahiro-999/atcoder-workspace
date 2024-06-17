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

N,u,v = LII()
u -=1
v -=1

g = defaultdict(list)

for _ in range(N-1):
    a,b = LII()
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

dist = [-1]*N
maxd = [0]*N

@bootstrap
def dfs(s,d):
    dist[s] = d
    mx = d
    for ns in g[s]:
        if dist[ns]!=-1:
            continue
        xx = yield dfs(ns, d+1)
        mx = max(mx, xx)
    maxd[s] = mx
    yield mx

dfs(v,0)

dprint(dist)
dprint(maxd)

ans = 0
half = (dist[u]-1)//2
dprint(half)
p = u
for _ in range(half):
    for np in g[p]:
        if dist[np] < dist[p]:
            p = np
            break

dprint(p)

n1 = 0+half
n2 = dist[p]

dprint(n1,n2)
ans = half + (maxd[p]-dist[p]) + (n2-n1)//2

print(ans)