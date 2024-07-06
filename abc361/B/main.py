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

x1,y1,z1,x2,y2,z2 = LII()

x3,y3,z3,x4,y4,z4 = LII()

def cmp(x1,x2,x3,x4):
    if max(x1,x2) <= min(x3,x4) or max(x3,x4) <= min(x1,x2):
        return False
    return True 


def cmp2d(x1,y1,x2,y2,x3,y3,x4,y4):
    return cmp(x1,x2,x3,x4) and cmp(y1,y2,y3,y4)

def cmp3d(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4):
    return cmp2d(x1,y1,x2,y2,x3,y3,x4,y4) and cmp(z1,z2,z3,z4)

if cmp3d(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4):
    print("Yes")
else:
    print("No")

