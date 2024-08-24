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

N,K = LII()
AB = [LII() for _ in range(N-1)]

V = LII()

v_set = set(V)


g = defaultdict(list)

for a,b in AB:
    g[a].append(b)
    g[b].append(a)

visited  = [False]*(N+1)
vlist = [False]*(N+1)
for v in V:
    vlist[v] = True

@bootstrap
def dfs(s):
    # sからたどっていき、v_setに含まれるものが無いパスは無視する。無視しないパスにある頂点の数を返す
    visited[s] = True
    ret = 0
    for nxt in g[s]:
        if visited[nxt]:
            continue
        ret += yield dfs(nxt)
    
    if vlist[s] or ret > 0:
        ret += 1
    # print(s,ret,find)
    yield ret

    
ans = dfs(V[0])
print(ans)
