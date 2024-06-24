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
# input = sys.stdin.readline
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

S = I()
T = I()

d = defaultdict(list)
for i,s in enumerate(S):
    d[s].append(i)

loop = 0
p = -1
for t in T:
    if not d[t]:
        loop = -1
        break
    i = bisect_left(d[t],p+1)
    if i == len(d[t]):
        p =d[t][0]
        loop+=1
    else:
        p = d[t][i]
#     print(t,p,loop)
# print(p)
# print(loop)
if loop == -1:
    ans = -1
else:
    ans = loop*len(S)+p+1

print(ans)