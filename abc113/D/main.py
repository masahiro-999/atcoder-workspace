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

H,W,K = LII()

dp = [[0]*(W) for _ in range(H+1)]
dp[0][0] = 1
MOD = 1000000007 

if W == 1:
    print(1)
    exit()

valid_w =[]
for i in range(1<<(W-1)):
    ok = True
    for j in range(W-2):
        if i>>j&1 == 1 and i>>(j+1)&1 == 1:
            ok = False
            break
    if ok:
        valid_w.append(i)
# print(*[bin(x) for x in valid_w], sep="\n")
for i in range(H):
    for j in range(W):
        for k in range(-1,2):
            nj = j+k
            if nj<0 or nj>=W:
                continue
            if k == 1:
                n = len([1 for x in valid_w if x>>j&1 == 1])
            elif k == -1:
                n = len([1 for x in valid_w if x>>(j-1)&1 == 1])
            else:
                n = len([1 for x in valid_w if (j==W-1 or x>>j&1 == 0) and (j==0 or x>>(j-1)&1 == 0)])
            dp[i+1][nj] += dp[i][j]*n 
            dp[i+1][nj] %= MOD
ans = dp[H][K-1]
print(ans)
