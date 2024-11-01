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

N = II()

ac = [LI() for _ in range(N*2)]

t = defaultdict(list)

for a,c in ac:
    t[c].append(int(a))

A = t["R"]
B = t["G"]
C = t["B"]

# print(t)

odd_table = []
for x in [A,B,C]:
    x.sort()


if len(A) %2 == 0:
    A,C = C,A

if len(B) %2 == 0:
    B,C = C,B

# print(A)
# print(B)
# print(C)
# C はかならず偶数

def f(A,B):
    ans = inf
    for a in A:
        i = bisect_left(B, a)
        if i == 0:
            x1 = inf
        else:
            x1 = a - B[i-1]
            assert x1 >=0
        if i == len(B):
            x2 = inf
        else:
            x2 = B[i] - a
            assert x2 >=0
        ans = min(ans,x1,x2)
    return ans


# print(odd_table)
if len(A) %2 == 1:
    a1 = f(A,B)
    a2 = f(A,C)+f(C,B)
    ans = min(a1,a2)
else:
    ans = 0

print(ans)

'''
3
2 R
10 R
20 R
30 R
1 G
31 B
'''