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

B,C = LII()


if B > 0:
    L1 = -B-(C-1)//2
    R1 = -B+(C-1)//2
    L2 = B-C//2
    R2 = B+(C-2)//2 if C-2 >=0 else B-(-(C-2))//2
elif B < 0:
    L1 = B-(C)//2
    R1 = B+(C-2)//2
    L2 = -B-(C-1)//2
    R2 = -B+(C-1)//2
else:
    L1 = -(C//2)
    R1 = 0
    L2 = 0
    R2 = (C-1)//2

x = max(0,L2-R1-1)
n = R2-L1+1 -x

# print(L1,R1,L2,R2,n,x)
print(n)