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

def swap(A,s,K):
    A[s],A[s+1] = A[s+1]+K,A[s]

def solve(A,K):
    ans = []
    for i in range(N-1):
        if i+1 == N-1:
            if A[i] > A[i+1] and A[i] - A[i+1] < K:
                return None
            else:
                while A[i]>A[i+1] or (A[i-1]>A[i] if i > 0 else False):
                    swap(A,i,K)
                    ans.append(i+1)
        elif i+2 == N-1:
            while (A[i]<A[i-1] if i > 0 else False) or abs(A[i+1]-A[i+2])<K:
                swap(A,i,K)
                ans.append(i+1)
        elif i > 0:
            while A[i]<A[i-1]:
                swap(A,i,K)
                ans.append(i+1)
    return ans

ans = solve(A,K)
if ans is None:
    print("No")
else:
    print("Yes")
    print(len(ans))
    print(*ans)

