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

N,M = LII()
S = [int(x) for x in I()]

last_ok = -1

dprint(S)
p = N
ans = []
while p>0:
    p_bak = p
    for _ in range(M):
        p -=1
        if S[p]==0:
            last_ok = p
        if p == 0:
            break
    dprint(p_bak, p, last_ok)
    if last_ok == -1 or p_bak == last_ok:
        print(-1)
        exit()
    ans.append(p_bak - last_ok)
    p = last_ok

ans = ans[::-1]
print(*ans)