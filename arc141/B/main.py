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

mod = 998244353
N,M = LII()

if N > 60:
    print(0)
    exit()

cnt = [0]*61

for i in range(M.bit_length()):
    cnt[i+1] = 1<<i
cnt[M.bit_length()]=M - (1<<(M.bit_length()-1))+1


# for i in range(1,M+1):
#     k = i.bit_length()
#     cnt[k]+=1
# print(cnt)

dp = [[0]*61 for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    sm = 0
    for j in range(60+1):
        dp[i+1][j] = (sm * cnt[j]) % mod
        sm += dp[i][j]
        sm %= mod
ans = 0
for k in range(60+1):
    ans += dp[N][k]
    ans %= mod
print(ans)

