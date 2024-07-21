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
N -= 1

def num_keta(k):
    if k == 1:
        return 10
    if k == 2:
        return 9
    return 9*10**((k+1)//2-1)

assert(num_keta(1) == 10)
assert(num_keta(2) == 9)
assert(num_keta(3) == 90)
assert(num_keta(4) == 90)
assert(num_keta(5) == 900)
assert(num_keta(6) == 900)
assert(num_keta(7) == 9000)
assert(num_keta(8) == 9000)

def solve(k,N):
    # print(k,N)
    n = (k+1)//2
    s = str(10**(n-1)+N)
    if k%2 == 1:
        s = s+s[:-1][::-1]
    else:
        s = s+s[::-1]
    return int(s)

k = 1
while True:
    n = num_keta(k)
    if (N -n)<0:
        break
    N -= n
    k += 1

if k == 1:
    ans = N
elif k == 2:
    ans = 11*N
else:
    ans = solve(k,N)
print(ans)
