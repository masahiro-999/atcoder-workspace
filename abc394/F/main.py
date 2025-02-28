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
g = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = LII()
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

ans = 0
def dfs(s,parent):
    global ans

    result = []
    for next in g[s]:
        if next == parent:
            continue
        x = dfs(next,s)
        result.append(x)
    result.sort(reverse=True)
    if len(result)>=3:
        ret = sum(result[:3])+1
    else:
        ret = 1
    if len(result)>=4:
        ans = max(ans,sum(result[:4])+1)
    if len(result)>0:
        ans = max(ans,result[0]+1
        )

    del result
    # print(s+1,ret,ans,result)
    return ret

dfs(0,None)
if ans <5:
    ans = -1
print(ans)