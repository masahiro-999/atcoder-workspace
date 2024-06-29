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
S = I()

p = 0
l = []
for i in range(N):
    if i == N-1 or S[i] == S[i+1]:
        l.append(S[p:i+1])
        p = i+1

ans = 1
for x in l:
    ans *=(len(x)+1)//2
    ans %= 10**9+7

print(ans)
# B BABABA ABABA AAA BA

# ABA ABA ABAB BABA ABA ABA ABAB BAB BAB BAB BAB BAB BAB BAB BAB BAB BAB BAB BAB BAB BABA ABABA ABAB BAB BABAB BABA ABA ABA ABA ABA

