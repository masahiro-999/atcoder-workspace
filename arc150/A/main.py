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


T = II()

for _ in range(T):
    N,K = LII()
    S = I()
    c0 = 0
    c1 = 0
    M = sum([1 for x in S if x == "1"])
    c0 = sum([1 for x in S[:K] if x == "0"])
    c1 = sum([1 for x in S[:K] if x == "1"])
    cnt = 0
    for i in range(N-K+1):
        if c0 == 0 and c1 == M:
            cnt+= 1
        if i == N-K:
            continue
        if S[i]=="0":
            c0 -= 1
        if S[i]=="1":
            c1 -= 1
        if S[i+K]=="0":
            c0 += 1
        if S[i+K]=="1":
            c1 += 1

    if cnt == 1:
        print("Yes")
    else:
        print("No")