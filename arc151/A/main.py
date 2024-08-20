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
S = I()
T = I()
X = [0]*N
for i,s,t in zip(count(),S,T):
    if s == "0" and t == "1":
        X[i] = 1
    elif s == "1" and t == "0":
        X[i] = -1

x = sum(X)
# print(x)
# print(X)
if x % 2 == 1:
    ans = -1
else:
    ans = ["0"]*N
    if x != 0:
        if x > 0:
            n = x //2
            p = 1
        else:
            n = -x //2
            p = -1
        for i in range(N)[::-1]:
            if X[i] == p:
                ans[i] = "1"
                n -= 1
                if n == 0:
                    break
                
    ans = "".join(ans)

print(ans)