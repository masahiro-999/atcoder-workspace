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

n1 =[0]*N
n2 =[0]*N

n = 0
for i in range(N)[::-1]:
    s = S[i]
    # 連続する2の数
    if s == "2":
        n += 1
    elif s == "1":
        n =0
    elif s == "/":
        n1[i] = n
        n = 0

        n = 0
for i in range(N):
    s = S[i]
    # 連続する1の数
    if s == "1":
        n += 1
    elif s == "2":
        n =0
    elif s == "/":
        n2[i] = n
        n = 0

ans = 0
for i in range(N):
    ans = max(ans, min(n1[i], n2[i]))

print(ans*2+1)