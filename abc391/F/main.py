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

N,K = LII()
A = LII()
B = LII()
C = LII()

def solve(A,B,C):
    A.sort()
    B.sort()
    C.sort()

    q = []
    x = A[-1]*B[-1]+B[-1]*C[-1]+C[-1]*A[-1]
    heappush(q,(-x,N-1,N-1,N-1))
    used = {(N-1,N-1,N-1)}
    cnt = K
    while q:
        x,i,j,k = heappop(q)
        # print(x,i,j,k)
        cnt -= 1
        if cnt == 0:
            ans = -x
            break
        for di,dj,dk in ((1,0,0),(0,1,0),(0,0,1)):
            ni = i-di
            nj = j-dj
            nk = k-dk
            if ni ==-1 or nj ==-1 or nk == -1:
                continue
            if (ni,nj,nk) not in used:
                used.add((ni,nj,nk))
                x = A[ni]*B[nj]+B[nj]*C[nk]+C[nk]*A[ni]
                heappush(q,(-x,ni,nj,nk))
    return ans
ans1 = solve(A,B,C)
print(ans1)