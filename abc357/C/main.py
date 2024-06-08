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
input = sys.stdin.readline
# input = lambda: sys.stdin.readline().rstrip("\r\n")
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

def create(n):
    def cp(ret, n, x, y, a):
        for i in range(n):
            for j in range(n):
                ret[i+n*x][j+n*y] = a[i][j]

    if n == 0:
        return [[1]]
    ret = [[0]*3**n for _ in range(3**n)]
    a = create(n-1)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            cp(ret,3**(n-1),i,j,a)
    return ret

a = create(N)
for i in range(3**N):
    ans = []
    for j in range(3**N):
        ans.append("#" if a[i][j] == 1 else ".")
    print("".join(ans))