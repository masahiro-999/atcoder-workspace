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

Sx,Sy  = LII()
Tx,Ty = LII()

if Sx > Tx:
    Sx, Tx = Tx, Sx
    Sy, Ty = Ty, Sy

if Ty < Sy:
    Ty *= -1
    Sy *= -1


# print(Sx, Sy, Tx, Ty)
if Sy % 2 == 0:
    if Sx %2 == 0:
        Sx += 1
else:
    if Sx %2 == 1:
        Sx += 1

if Ty % 2 == 0:
    if Tx %2 == 1:
        Tx -= 1
else:
    if Tx %2 == 0:
        Tx -= 1

dy = Ty - Sy

dx = Tx -Sx
# print(dx, dy)
if dx <= dy:
    ans = dy
else:
    dx -= dy
    ans = dy + (dx-1)//2+1

print(ans)
