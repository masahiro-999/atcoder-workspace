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

N,A,B = LII()
S = I()

SS = [1 if s =="(" else -1 for s in S]
dprint(SS)
cnt = Counter(SS)

n1 = cnt[1]
n2 = cnt[-1]
d = n1  - n2
dprint(d)
n = abs(d)//2
y = abs(d)//2
if d < 0:
    for i in range(2*N):
        if SS[i] == -1:
            SS[i] = 1
            n -= 1
        if n == 0:
            break
elif d > 0:
    for i in range(2*N)[::-1]:
        if SS[i] == 1:
            SS[i] = -1
            n -= 1
        if n == 0:
            break
dprint(SS)
dprint(list(accumulate(SS)))
x = min(accumulate(SS))
x = max(0, -x)
x = (x+1) //2
ans = y*B +x*min(A,2*B)
dprint(d,x,y,ans)

print(ans)

