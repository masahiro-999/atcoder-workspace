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

S = I()
N = len(S)
t = {}

def pos_list(S,c):
    ret = [0]*(N+1)
    cnt = 0
    for i in range(N)[::-1]:
        if S[i] == c:
            cnt += 1
        ret[i] = cnt
    return ret

for c in ascii_lowercase:
    t[c] = pos_list(S, c)

lr = []
prev = S[0]
r = -1
l = 0
for i in range(1,N):
    if S[i]==prev:
        r = i
    else:
        if l<r:
            lr.append((l,r))
        prev = S[i]
        l = i
        r = -1
    prev = S[i]

ans = 0
prev_l = N
prev_c = None
for l,r in lr[::-1]:
    c = S[r]
    x = t[c][r+1] - t[c][prev_l]
    ans += prev_l - (r+1) - x
    if c != prev_c:
        ans += N-prev_l
    prev_l = l
    prev_c = c

print(ans)