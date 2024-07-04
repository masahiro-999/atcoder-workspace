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
A = LII()

max_A = max(K,max(A))

L = f'{K:0{max_A.bit_length()}b}'
LL = len(L)

# print(max_A,L,LL)
dp = [[-1]*2 for _ in range(LL+1)]
dp[0][0] = 0

def f(bit,x):
    ret = 0
    for a in A:
        ret +=  ((a >> bit &1)^x)<<bit
    return ret

for i in range(LL):
    x = int(L[i])
    for j in range(2):
        for k in range(2 if j==1 else x+1):
            nj = j
            if j == 0:
                if k == x:
                    nj = j
                elif k < x:
                    nj = 1
            if dp[i][j] == -1:
                continue
            dp[i+1][nj] = max(dp[i+1][nj], dp[i][j]+f(LL-1-i,k))
            # print(i,j,k,dp[i][j])
ans = max(dp[LL])
print(ans)
