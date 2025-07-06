import sys
import os
from math import ceil, floor, sqrt, pi, factorial, gcd,lcm,sin,cos,tan,asin,acos,atan2,exp,log,log10, isqrt, comb
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
inf = float('inf')

T = II()
for _ in range(T):
    N = II()
    A = LII()
    if N == 2:
        print("Yes")
        continue
    cnt = Counter(A)
    if len(cnt) == 1:
        print("Yes")
        continue
    if len(cnt) == 2:
        k_list = list(cnt.keys())
        if k_list[0] == k_list[1]*-1 and abs(cnt[k_list[0]]-cnt[k_list[1]])<2:
            print("Yes")
            continue
    A.sort(key=lambda a: abs(a))
    ans = True
    for i in range(1,N-1):
        if A[i-1]*A[i+1] != A[i]*A[i]:
            ans = False
    print("Yes" if ans else "No")

