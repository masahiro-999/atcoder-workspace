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

N,K = LII()
A = LII()
max_a = max(A)
used_a = [0]*(max_a+1)
for a in A:
    used_a[a] += 1

back_a = defaultdict(list)
for i,a in enumerate(A):
    back_a[a].append(i)

ans = [-1]*(max_a+1)
for i in range(1,max_a+1)[::-1]:
    menber = 0
    x_list=[]
    x = i
    while x <=max_a:
        menber += used_a[x]
        x += i
    if menber >= K:
        for j in range(i, max_a+1,i):
            if ans[j] == -1:
                ans[j] = i
for a in A:
    print(ans[a])