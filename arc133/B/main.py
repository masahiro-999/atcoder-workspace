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
P = LII()
Q = LII()

back_p = [0]*(N+1)

for i,p in enumerate(P):
    back_p[p] = i

multiple_table = defaultdict(list)

for i in range(1,N+1):
    n = i
    while n <= N:
        multiple_table[n].append(i)
        n += i

ij = []
for i in range(N):
    q = Q[i]
    update = []
    for x in multiple_table[q]:
        index = back_p[x]
        ij.append((index, -i))

ij.sort()
j_list = [-j for _,j in ij]

lis = [inf]*N
for j in j_list:
    i = bisect_left(lis,j)
    lis[i] = j

# print(*lis)
ans = sum([1 for x in lis if x!= inf])

print(ans)
