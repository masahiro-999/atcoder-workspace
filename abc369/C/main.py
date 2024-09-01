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

N = II()
A = LII()

if N == 1:
    print(1)
    exit()
    
B = [a0-a1 for a0,a1 in zip(A,A[1:])]

# Bを使って、Aの範囲[L,R]が等差数列になるL,Rの組の数を求める
# Bの値が同じ範囲を求める。
# その範囲の数がnなら、その範囲の数はn(n+1)/2

ans = 0
cnt = 1
for b0,b1 in zip(B,B[1:]):
    if b0 == b1:
        cnt += 1
    else:
        ans += cnt*(cnt+1)//2
        cnt = 1
ans += cnt*(cnt+1)//2
ans += N
print(ans)

