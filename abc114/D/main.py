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

def get_prime_list(num_max):
    prime_table=[1]*(num_max+1)
    prime_table[0] = 0
    prime_table[1] = 0
    for i in range(2, num_max+1):
        k = i*2
        while k <= num_max:
            prime_table[k] = 0
            k += i
    return [i for i in range(2,num_max+1) if prime_table[i]]


N = II()

prime_list = get_prime_list(N)
dprint(prime_list)

factor=Counter()
for i in range(2,N+1):
    for p in prime_list:
        if i%p==0:
            while i%p==0:
                i //=p
                factor[p]+=1
        if i<p:
            break

f = list(factor.values())
N = len(f)
M = 75

dp = [[0]*(M+1) for _ in range(N+1)]

dp[0][1]=1

for i in range(N):
    for j in range(1,M+1):
        for k in range(1,f[i]+1+1):
            if j*k <=M:
                dp[i+1][j*k] += dp[i][j]

ans = dp[N][M]
print(ans)
