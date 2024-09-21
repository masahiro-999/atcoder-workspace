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
S = I()
S = [s for s in S]

n = 0
# "ABC"の数
for i in range(N-2):
    if S[i] == "A" and S[i+1] == "B" and S[i+2] == "C":
        n += 1

def is_abc(i):
    if i+2<N and S[i] == "A" and S[i+1] == "B" and S[i+2] == "C":
        return True
    if i-1>=0 and i+1 <N and S[i-1] == "A" and S[i] == "B" and S[i+1] == "C":
        return True
    if i-2>=0 and S[i-2] == "A" and S[i-1] == "B" and S[i] == "C":
        return True
    return False

for _ in range(Q):
    X,C = LI()
    X = int(X)-1

    if is_abc(X):
        n -= 1
    S[X] = C
    if is_abc(X):
        n += 1
    print(n)