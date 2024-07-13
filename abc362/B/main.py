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

xy = [LII() for _ in range(3)]

def check(p1,p2,p3):
    # ピタゴラスの定理が成り立つかしらべる
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    a = (x1-x2)**2 + (y1-y2)**2
    b = (x2-x3)**2 + (y2-y3)**2
    c = (x3-x1)**2 + (y3-y1)**2
    return a+b == c or b+c == a or c+a == b

if check(xy[0],xy[1],xy[2]):
    print("Yes")
else:
    print("No")
