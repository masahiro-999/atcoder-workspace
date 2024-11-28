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
import random
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

# S = ''.join(random.choice("111222/") for _ in range(10000))
# print(S)
# S='222///222121222/12//2//1/22/12//21/1/2211//111/222'

pos1 = []
pos2 = []
posx = []
for i,s in enumerate(S):
    if s == "1":
        pos1.append(i+1)
    elif s == "2":
        pos2.append(i+1)
    else:
        posx.append(i+1)

def get_next(pos, start, x):
    if x == 0:
        return start
    i = bisect_left(pos, start)
    i += x-1
    if i < len(pos):
        return pos[i]+1
    return inf

def check(x,l,r):
    l = get_next(pos1,l,x)
    l = get_next(posx,l,1)
    l = get_next(pos2,l,x)
    return l <= r+1

# print(pos1)
# print(pos2)
# print(posx)
# print(get_next(pos1,1,2))
# print(get_next(posx,3,1))
# print(get_next(pos2,5,2))

# print(check(1,1,7))
# print(check(2,1,7))
# print(check(3,1,7))
# print(check(4,1,7))

for _ in range(Q):
    l, r = LII()
    if check(0,l,r) is False:
        print(0)
    else:
        ok = 0
        ng = (r-l+1)
        while ng - ok > 1:
            mid = (ng+ok)//2
            if check(mid,l,r):
                ok = mid
            else:
                ng = mid
        print(ok*2+1)
