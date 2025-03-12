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
xyz = [LII() for _ in range(M)]

A = [0]*N
        
g = [[] for _ in range(N)]
for x,y,z in xyz:
    x -= 1
    y -= 1
    g[x].append((y,z))
    g[y].append((x,z))

val = [-1]*N

@bootstrap
def dfs(q, s, v, parent=None):
    val[s] = v
    q.append(s)
    for next,xor in g[s]:
        if next == parent:
            continue
        if val[next] == -1:
            yield dfs(q, next, v ^ xor, s)
        else:
            if val[next] != v ^ xor:
                print(-1)
                exit()
    yield

A = [0]*N

for i in range(N):
    if val[i] != -1:
        continue
    q = []
    dfs(q,i,0)

    for bit in range(30):
        cnt = Counter()
        for i in q:
            cnt[val[i] >> bit & 1] += 1
        less_bit = 1 if cnt[1] < cnt[0] else 0
        for i in q:
            if (val[i]>>bit&1) == less_bit:
                A[i] += 1<<bit

print(*A)