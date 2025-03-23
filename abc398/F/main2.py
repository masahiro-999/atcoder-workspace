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

S = I()

def solve(S):
    N = len(S)

    if S == S[::-1]:
        return S

    ok = 1
    ng = N
    while ng-ok >1:
        mid = (ng+ok)//2
        if mid % 2 == 0:
            x = mid//2
            t = S[-x:][::-1]
            for i in range(N-x):
                if S[i:i+x]== t:
                    ok = mid
                    break
            else:
                ng = mid
        else:
            x = (mid-1)//2
            t = S[-x-1:-1][::-1]
            for i in range(N-x-1):
                if S[i:i+x]== t:
                    ok = mid
                    break
            else:
                ng = mid

    ans = S[:-ok]+S[-ok:]+S[:-ok][::-1]
    return ans



b = 1000000007
p = 998244353

N = len(S)

from atcoder.string import z_algorithm

z_list = z_algorithm(S[::-1]+S)[N:]

for i in range(N):
    if z_list[i] == N-i:
        ans = S+S[:i][::-1]
        break      

print(ans)
# print(S)
# print(z_list)
