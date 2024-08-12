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

N,D = LII()
xy = [LII() for _ in range(N)]
M = 2000000
X = [x+M for x,y in xy]
Y = [y+M for x,y in xy]

X.sort()
Y.sort()

def create_t(X):
    ret = []
    p = 0
    left = 0
    right = N
    n = sum(X)
    for i in range(2*M+1):
        ret.append(n)
        while p < N and i ==X[p]:
            p += 1
            left += 1
            right -= 1
        n += left-right
    return ret

t_x = create_t(X)
t_y = create_t(Y)

t_y.sort()
ans = 0
for d_x in t_x:
    d = D - d_x
    i = bisect_right(t_y, d)
    ans += i

print(ans)