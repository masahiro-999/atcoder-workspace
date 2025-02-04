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
S = LII()

def solv(a1,a2):
    A = [0]*(N+2)
    A[0] = a1
    A[1] = a2
    for i in range(2,N+2):
        A[i] = S[i-2]-A[i-1]-A[i-2]
    return A

# for a1,a2 in((0,0),(1,0),(0,1),(1,1),(0,4)):
#     a = solv(a1,a2)
#     print(a1,a2,a)

B = solv(0,0)
min1 = min(x for i,x in enumerate(B) if i%3==0)
min2 = min(x for i,x in enumerate(B) if i%3==1)
C = solv(-min1,-min2)

if min(C)>=0:
    print("Yes")
    print(*C)
else:
    print("No")