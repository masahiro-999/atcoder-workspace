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
input = sys.stdin.readline
# input = lambda: sys.stdin.readline().rstrip("\r\n")
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

ab = [LII() for _ in range(N)]
cd = [LII() for _ in range(Q)]

b_list = defaultdict(SortedList)

sl = SortedList()

group = [0]*(N+1)
a_list = [0]*(N+1)
b_list_max = [0]*(2*10**5+1)

def add(a,b):
    if b_list[b]:
        mx = b_list_max[b]
    else:
        mx = None
    b_list[b].add(a)
    b_list_max[b] = max(b_list_max[b], a)
    if mx is None or mx <=a:
        # aは新しい最大
        sl.add(a)
        if mx is not None:
            sl.discard(mx)

def remove(a,b):
    assert b_list[b] 
    mx = b_list_max[b]
    b_list[b].remove(a)
    if mx ==a:
        # aは最大でなくなる
        sl.discard(a)
        if b_list[b]:
            b_list_max[b] = b_list[b][-1]
            sl.add(b_list_max[b])
        else:
            b_list_max[b] = 0

for i,(a,b) in enumerate(ab):
    group[i] = b
    a_list[i] = a
    add(a,b)

dprint("---")
dprint(b_list)
dprint(a_list)
dprint(sl)

for c,d in cd:
    c -= 1
    b = group[c]
    a = a_list[c]
    remove(a,b)
    add(a,d)
    group[c]=d
    ans = sl[0]
    dprint("---")
    dprint(b_list)
    dprint(a_list)
    dprint(sl)


    print(ans)



# 6 3
# 1 8 1
# 2 6 2
# 3 9 3
# 4 1 1
# 5 2 2
# 6 1 3


# 4 3
# 2 1
# 1 2
