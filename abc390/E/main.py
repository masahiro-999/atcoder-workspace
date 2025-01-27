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
inf = 100100100100100100
debug = False
# debug = True
if debug:
    def dprint(*arg): print(*arg, file=sys.stderr)
else:
    def dprint(*arg): pass

N,X = LII()
vac =[LII() for _ in range(N)]

ac1 = [(a,c) for v,a,c in vac if v ==1]
ac2 = [(a,c) for v,a,c in vac if v ==2]
ac3 = [(a,c) for v,a,c in vac if v ==3]

max_a = 200000*5000+1


def f(ac):
    dp = [0]*(X+1)
    dp[0] = 0
    N = len(ac)
    for i in range(N):
        a,c = ac[i]
        for j in range(X+1)[::-1]:
            if j+c <=X:
                dp[j+c] = max(dp[j+c], dp[j]+a)
    return dp

table = [f(ac) for ac in (ac1, ac2, ac3)]

def ff(target_a):
    sm = 0
    for t in table:
        i = bisect_left(t,target_a)
        if i == len(t):
            return False
        sm += i
    return sm <= X

# print(ff(3))
# exit()
ok = 0
ng = max_a+1
while ng-ok >1:
    mid = (ok+ng)//2
    if ff(mid):
        ok = mid
    else:
        ng = mid

print(ok)