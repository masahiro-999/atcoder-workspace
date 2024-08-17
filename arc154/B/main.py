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
S = I()
T = I()

cnt_s = Counter(S)
cnt_t = Counter(T)
if cnt_s != cnt_t:
    print(-1)
    exit()

if S == T:
    print(0)
    exit()

t = defaultdict(list)
for i,x in enumerate(T):
    t[x].append(i)

def check(n):
    nn = N-n
    SR = S[-nn:]
    p = -1
    for x in SR:
        i = bisect_right(t[x],p)
        if i == len(t[x]):
            return False
        p = t[x][i]
    return True

l = 0
r = N
while r-l >1:
    mid = (l+r)//2
    if check(mid):
        r = mid
    else:
        l = mid

print(r)

