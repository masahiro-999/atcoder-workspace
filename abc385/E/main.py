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
uv = [LII() for _ in range(N-1)]

g = defaultdict(list)
for u,v in uv:
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

ans = 0

def get_y(s,y,parent):
    global ans
    mi = inf
    y_list = []
    for next in g[s]:
        if next == parent:
            continue
        yy = get_y(next,len(g[s])-1,s)
        y_list.append(yy)
        mi = min(mi,yy)
    if y !=inf:
        y_list.append(y)
    cnt = Counter(y_list)
    aa = 0
    sm = 0
    for k in sorted(cnt.keys(), reverse=True):
        sm += cnt[k]
        a = (k+1)*sm+1
        aa = max(aa,a)

    # print(s+1,y,aa,y_list)

    ans = max(ans,aa)
    ret = len(g[s])
    if y != inf:
        ret -= 1
    return ret

get_y(0,inf,None)

print(N-ans)