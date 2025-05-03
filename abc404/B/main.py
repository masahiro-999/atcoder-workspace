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

N = II()
S = [I() for _ in range(N)]
T = [I() for _ in range(N)]

def rotate(S):
    ret = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ret[i][N-1-j] = S[j][i]
    return ret

def count_diff(A,B):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if A[i][j] != B[i][j]:
                cnt += 1
    
    return cnt

A = S

ans = inf
for i in range(4):
    a = count_diff(A,T)+i
    ans = min(ans,a)
    A = rotate(A)

print(ans)