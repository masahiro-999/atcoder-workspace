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

MOD = 1000000000+7
N = II()

W ="ACGT"

NG={"AGC", "GAC", "ACG"}
NG4={"AAGC","ACGC","AGGC","ATGC","AGAC","AGCC","AGGC","AGTC"}
dp = Counter()
dp[""]=1
for i in range(N):
    ndp = Counter()
    for j in dp.keys():
        for k in W:
            nj = j[-3:]+k
            if nj[-3:] in NG or nj in NG4:
                continue
            ndp[nj] += dp[j]
            ndp[nj] %= MOD
    dp = ndp

ans = sum([x for x in dp.values()])%MOD
print(ans)
