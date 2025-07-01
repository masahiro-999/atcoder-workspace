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

S = I()
K = II()
N = len(S)

def check(n):
    b = 0
    l = 0
    for i in range(N):
        if S[i]==".":
            b+=1
        if i-n>=0:
            if S[i-n]==".":
                b-=1
        if i >=n-1 and b <=K:
                return True
    return False

ok = 0
ng = N+1
while ng-ok>1:
    mid = (ng+ok)//2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)