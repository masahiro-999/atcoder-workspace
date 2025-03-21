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
from itertools import product, accumulate,permutations,combinations, count, groupby
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

N,K = LII()
S = I()

run_len = []
first_zero = None

ad = 0

cnt = 0
for k,g in groupby(S):
    x = len(list(g))
    run_len.append((k,x))
    if k == "1":
        cnt += 1
        if cnt == K:
            ad = x    
# print(run_len)
# print(ad)
cnt = 0
A = []
for k,l in run_len:
    if k == "1":
        cnt += 1
        if cnt == K-1:
            l += ad
        if cnt == K:
            l = 0
    A.append(k*l)

print("".join(A))
