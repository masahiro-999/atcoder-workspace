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
N,Q = LII()
A = LII()
B = LII()
from random import randint
t = {}
from atcoder.fenwicktree import FenwickTree

BIT_A = FenwickTree(N)
BIT_B = FenwickTree(N)

for i,a in enumerate(A):
    if a not in t:
        t[a] = randint(0,1000000000)
    BIT_A.add(i,t[a])

for i,a in enumerate(B):
    if a not in t:
        t[a] = randint(0,1000000000)
    BIT_B.add(i,t[a])

for _ in range(Q):
    L1,R1,L2,R2 = LII()
    if BIT_A.sum(L1-1,R1) == BIT_B.sum(L2-1,R2):
        print("Yes")
    else:
        print("No")