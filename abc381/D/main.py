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

def solv(A):
    pos = [-1]*(N+1)
    B = []
    for i in range(len(A)//2):
        if A[i*2] != A[i*2+1]:
            B.append(-1)
        else:
            B.append(A[i*2])
    s = 0
    ans = 0
    used = set()
    for i in range(len(B)):
        a = B[i]
        if a == -1:
            s = i+1
            used = set()
            continue
        while a in used:
            x = B[s]
            if x in used:
                used.remove(x)
            s += 1
        used.add(a)
        ans = max(ans, i-s+1)
    return ans

a1 = solv(A)
a2 = solv(A[1:])
ans = max(a1, a2)*2
print(ans)