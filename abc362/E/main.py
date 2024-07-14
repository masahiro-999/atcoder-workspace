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

from types import GeneratorType

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

N = II()
A = LII()
MOD = 998244353
dp = [[[0]*(N+1) for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(i):
        dp[i][j][2]+=1
        for k in range(2,N):
            for x in range(i+1,N):
                d = A[i]-A[j]
                if d == A[x]-A[i]:
                    dp[x][i][k+1] += dp[i][j][k]
                    dp[x][i][k+1] %= MOD

ans = [0]*(N+1)
for k in range(2,N+1):
    for i in range(N):
        for j in range(i):
            ans[k] += dp[i][j][k]
            ans[k] %= MOD
ans [1] = N
print(*ans[1:])
