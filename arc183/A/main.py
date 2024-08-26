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

N,K = LII()

cnt = Counter()
for i in range(1,N+1):
    cnt[i] = K

def create_ans(cnt):
    ans = []
    for k,v in cnt.items():
        for i in range(v):
            ans.append(k)
    ans.sort(reverse=True)
    return ans


if N % 2 == 0:
    h = N//2
    cnt[h] -= 1
    ans = [h]+create_ans(cnt)
else:
    h = (N+1)//2
    cnt[h] = 0
    if h-1 in cnt:
        cnt[h-1] -= 1
        ans = [h]*K + [h-1] + create_ans(cnt)
    else:
        ans = [h]*K + create_ans(cnt)

print(*ans)