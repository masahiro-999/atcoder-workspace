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
C = [LII() for _ in range(N)]
TC = [x for x in zip(*C)]

def get_sub(c):
    sub = []
    for a,b in zip(c,c[1:]):
        sub.append(b-a)
    return sub

def check(C):
    sub = get_sub(C[0])
    for i in range(1,N):
        if get_sub(C[i]) != sub:
            return False
    return True
   

if check(C) and check(TC):
    if N == 1:
        A = [0]
        B = [C[0][0]]
    else:
        sub = get_sub(C[0])
        acc_sub = list(accumulate(sub))
        mi = min(0, min(acc_sub))
        B=[-mi]
        for s in sub:
            B.append(s+B[-1])
        A=[0]*N
        for i in range(N):
            A[i] = C[i][0] -B[0]
    print("Yes")
    print(*A)
    print(*B)
else:
    print("No")