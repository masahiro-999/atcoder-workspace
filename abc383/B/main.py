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

H,W,D = LII()
S = [I() for _ in range(H)]


def count(i1,j1,D):
    ans = set()
    for i in range(H):
        for j in range(W):
            if S[i][j] == "." and D >= abs(i1-i)+abs(j1-j):
                ans.add((i,j))
    return ans
# print(count(0,0,D)|count(0,4,D))



ans = 0
for i1 in range(H):
    for j1 in range(W):
        if S[i1][j1] == "#":
            continue
        ans1 = count(i1,j1,D)
        for i2 in range(H):
            for j2 in range(W):
                if S[i2][j2] == "#":
                    continue
                ans2 = count(i2,j2,D)
                # print(i1,j1,i2,j2,len(ans1 | ans2))
                ans = max(ans, len(ans1 | ans2))
print(ans)