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

N,K = LII()
MOD = 998244353

if N == 1:
    print(1)
    exit()

n1 = pow(N,-1,MOD)
n2 = n1*n1%MOD

dp = [[0]*2 for _ in range(K+1)]

dp[0][0] = 1
dp[0][1] = 0

A = ((N-1)**2+1)*n2 % MOD
B = n1*n1*2 %MOD

for i in range(K):
    dp[i+1][0] = (dp[i][0]*A + dp[i][1]*B*(N-1))%MOD
    dp[i+1][1] = (dp[i][0]*B + dp[i][1]*(A+B*(N-2)))%MOD


ans = (dp[K][0]+dp[K][1]*(N+2)*(N-1)//2) %MOD

# n=0
# for i in range(2,N+1):
#     n+=i
# ans = (dp[K][0]+dp[K][1]*n) %MOD


print(ans)