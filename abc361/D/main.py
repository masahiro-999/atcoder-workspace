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
N+=2
S = S+".."
T = T+".."

def bfs(s):
    d = defaultdict(lambda : -1)
    q = deque()
    q.append((s,len(s)-2))
    d[s] = 0
    while q:
        s, free_i = q.popleft()
        for i in range(N-1):
            if s[i] == "." or s[i+1] == ".":
                continue
            tmp = s[:free_i]+s[i:i+2]+s[free_i+2:]
            ns = tmp[:i]+".."+tmp[i+2:]
            if d[ns] != -1:
                continue
            d[ns] = d[s]+1
            q.append((ns,i))
    return d

d = bfs(S)

print(d[T])