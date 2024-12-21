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
H = LII()

table = defaultdict(set)
for i,h in enumerate(H):
    table[h].add(i)


def f(x,t,interval):
    ret = 1
    while x+interval in t:
        ret += 1
        x += interval
    return ret

# print(table)
# for t in table.values():
#     print(t)
#     for x in t:
#         for y in t:
#             if x == y:
#                 continue
#             if y+(y-x) in t:
#                 print(x,y,y+(y-x))
#                 print("ok")
#                 break
#             if x-(y-x) in t:
#                 print(x,y,x-(y-x))
#                 print("ok")
#                 break


mx = 0
for t in table.values():
    # print(t)
    for interval in range(1,N+1):
        for x in t:
            n = f(x,t,interval)
            # if x == 9 and interval == 8:
                # print(x,interval,n)
            mx = max(mx,n)



print(mx)