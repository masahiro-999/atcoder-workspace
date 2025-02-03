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

def ask(u,v):
    if v>2:
        print("?", u, v, flush = True)
        return II()
    else:
        return 0

d1 = [ask(1,i) for i in range(N+1)]
d2 = [ask(2,i) for i in range(N+1)]
d3 = [i for i in range(3,N+1) if d1[i]+d2[i] ==3]


d = [1 for i in range(3,N+1) if abs(d1[i]-d2[i]) !=1]
if len(d3)==2:
    if ask(d3[0],d3[1]) == 1:
        ans = 3
    else:
        ans = 1
else:
    ans = min(d1[i]+d2[i] for i in range(3,N+1))

print("!",ans)
