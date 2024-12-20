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

Q = II()

s = 0
t = 0
table_t = [0]*Q
table_n = [0]*Q
sm = 0
for _ in range(Q):
    cmd = LII()
    if cmd[0] == 1:
        table_n[s] += 1
    if cmd[0] == 2:
        table_t[s] = cmd[1]
        sm += cmd[1]
        s += 1
    if cmd[0] == 3:
        H = cmd[1]
        ans = 0
        while sm >= H and t < s:
            ans += table_n[t]
            sm -= table_t[t]
            t += 1
        print(ans)