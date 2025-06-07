import sys
import os
from math import ceil, floor, sqrt, pi, factorial, gcd,lcm,sin,cos,tan,asin,acos,atan2,exp,log,log10, isqrt, comb
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cmp_to_key, lru_cache, reduce, cache
from operator import add, iand, ior, itemgetter, mul, xor
from string import ascii_lowercase, ascii_uppercase, ascii_letters
from typing import *
from bisect import bisect, bisect_left, bisect_right
from heapq import heapify, heappop, heappush, heappushpop, nlargest, nsmallest
from sortedcontainers import SortedSet, SortedList, SortedDict
from itertools import product, accumulate,permutations,combinations, count, groupby
input = lambda: sys.stdin.readline().rstrip("\r\n")
I = input
II = lambda: int(I())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
sys.setrecursionlimit(10000000)
inf = float('inf')

N,L = LII()
d = LII()

if L % 3 != 0:
    print(0)
    exit()
L3 = L//3
D = []

p = 0
D.append(p)
for x in d:
    p += x
    p %=L
    D.append(p)

cnt = Counter(D)

pos = list(cnt.keys())

pos2 = pos[:]

for i in range(len(pos2)):
    pos2[i] %= L3

cnt_pos2 = Counter(pos2)

ans = 0
for k,v in cnt_pos2.items():
    if v == 3:
        a = 1
        for i in range(3):
            a *= cnt[k+i*L3]
    
        ans += a
print(ans)