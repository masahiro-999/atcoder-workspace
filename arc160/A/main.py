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
AI = [(a,i) for i,a in enumerate(A)]
AI.sort()
# print(AI)
def solve_up(n,L=0):
    # print(n,L)
    if L == N-1:
        return (-1,-1)
    # dprint(f'{AI=}')
    a1 = A[L]
    c = n
    for a,i in AI:
        if i <L:
            continue
        if a < a1:
            c -= 1
        if c == 0:
            return(L,i)

    return solve_up(c,L+1)

def solve_down(n,L=0):
    # print(n,L)
    if L == N-1:
        return (-1,-1)
    # dprint(f'{AI=}')
    a1 = A[L]
    c = n
    for i in range(N-1,-1,-1):
        if AI[i][1] <L:
            continue
        if AI[i][0] > a1:
            c -= 1
        if c == 0:
            return(L,AI[i][1])

    return solve_down(c,L+1)

def solve(n):
    a = solve_up(n)
    b = solve_down(N*(N+1)//2-n+1)
    if a ==(-1,-1) and b == (-1,-1):
        return(0,0)
    if a ==(-1,-1):
        return b
    else:
        return a

# for i in range(1,N+1):
#     L,R = solve(i)
#     print(f'{i=}',L,R)

L,R = solve(K)
ans = A[:L]+A[L:R+1][::-1]+A[R+1:]
print(*ans)

# def solve2():
#     a = []
#     for R in range(N):
#         for L in range(R+1):
#             x = A[:L]+A[L:R+1][::-1]+A[R+1:]
#             a.append((x,(L,R)))
#     a.sort()
#     return a

# a = solve2()
# for k in range(1,N*(N+1)//2+1):
#     L,R = solve(k)
#     if  (L,R) != a[k-1][1]:
#         print(k,a[k-1][1], "NG",L,R)
#     else:
#         print(k,a[k-1][1])
