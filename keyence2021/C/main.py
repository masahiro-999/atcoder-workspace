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

mod = 998244353

H,W,K = LII()

cnt =[[0]*W for _ in range(H)]
S =[[" "]*W for _ in range(H)]

for _ in range(K):
    h,w,c = LI()
    h = int(h)-1
    w = int(w)-1
    S[h][w] = c

cnt[0][0] = 1

r = 2*pow(3,-1,mod)
for i in range(H):
    for j in range(W):
        if j+1 < W:
            if S[i][j] in {"X","R"}:
                cnt[i][j+1]+= cnt[i][j]
                cnt[i][j+1]%= mod
            if S[i][j] == " ":
                cnt[i][j+1]+= cnt[i][j]*r
                cnt[i][j+1]%= mod
        if i+1<H:
            if S[i][j] in {"X","D"}:
                cnt[i+1][j]+= cnt[i][j]
                cnt[i+1][j]%= mod
            if S[i][j] == " ":
                cnt[i+1][j]+= cnt[i][j]*r
                cnt[i+1][j]%= mod

# print(cnt)
ans = cnt[H-1][W-1]
ans *= pow(3,H*W-K,mod)
ans %= mod

print(ans)