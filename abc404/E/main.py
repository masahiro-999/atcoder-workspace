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

"""
16
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
  1 1 1 2 5 1 1 3 4 1 4 3 1 1 2
  1 0 0 0 1 0 0 1 1 0 0 0 0 0 1
                          1     
                        1
                  2
                3
          4
  5
6   
"""
from atcoder.segtree import SegTree

N = II()

C = [0] + LII()
A = [0] + LII()

def solve(N,C,A):
    st = [inf] * N
    st[0] = 0
    last_a = None
    for i in range(1,N):
        if A[i] > 0:
            last_a = i
        mi = inf
        for j in range(1,C[i]+1):
            l = i-j
            if l < 0:
                break
            mi = min(mi, st[l])
            if A[l] > 0:
                mi = st[l]
                break
        st[i] = mi+1

    return st[last_a]

# def solve2(N, C, A):
#     p = N-1
#     cnt = 0
#     while p:
#         if A[p] == 0:
#             p -= 1
#             continue
#         for i in range(C[p]):
#             if p-1-i == 0 or A[p-1-i] > 0:
#                 A[p-1-i] += A[p]
#                 A[p] = 0
#                 p = p-1-i
#                 break
#         else:
#             A[max(0,p - C[p])] += A[p]
#             A[p] = 0
#             p = p - C[p]
#         cnt += 1
#     return cnt

# import random
# while True:
#     N = 10
#     C = [0]+[random.randrange(1,10,1) for _ in range(N-1)]
#     A = [0]+[0 if random.randrange(5) else 1 for _ in range(N-1)]
#     a1 = solve(N,C,A)
#     a2 = solve2(N,C,A)
#     if a1 != a2:
#         break
# print(N)
# print(C)
# print(A)
# print(a1,a2)

ans = solve(N, C, A)
print(ans)
