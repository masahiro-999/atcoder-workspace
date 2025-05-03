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
inf = 100100100100100100100
debug = False
# debug = True
if debug:
    def dprint(*arg): print(*arg, file=sys.stderr)
else:
    def dprint(*arg): pass

def check(a,b):
    sm = a
    cnt = 0
    for i in range(200):
        n = sm + b
        if (sm > 0) != (n > 0):
            cnt += 1
        print(i*2, cnt, n)
        sm = n
        n = sm + a
        if (sm > 0) != (n > 0):
            cnt += 1
        sm = n
        print(i*2+1, cnt)
    return cnt

t1,t2 = LII()
a1,a2 = LII()
b1,b2 = LII()

if a1 > b1:
    a1,b1 = b1,a1
    a2,b2 = b2,a2

a = t1*(a1-b1)
b = t2*(a2-b2)

if a+b < 0:
    ans = 0
elif a + b == 0:
    ans = "infinity"
else:
    ans = (-a)//(a+b)
    # print(999, ans)
    if (ans)*(a+b) == -a:
        ans = ans *2
    else:
        ans = ans*2+1
    # print(ans*(a+b),a)
    # print(check(a,b))

print(ans)