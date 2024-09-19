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

P = []

for i in range(N):
    if S[i:i+3] == "ARC":
        P.append(i)

Q = []
n0 = 0
for p in P:
    i = p
    while i >= 0 and S[i]=="A":
        i -= 1
    n1 = p - i
    i = p +2
    while i < N and S[i]=="C":
        i += 1
    n2 = i - p-2
    n = min(n1,n2)
    # print(n1,n2,n)
    if n == 1:
        n0 +=1
    elif n > 1:
        Q.append(n-1)

Q.sort()
q = 0
# print(Q)

def pop_q():
    global q,Q,n0
    if q == len(Q):
        return False
    Q[q]-=1
    if Q[q]==0:
        q += 1
        n0 += 1
    return True

def stop_current_q():
    global q,Q
    if q == len(Q):
        return False
    q += 1
    return True

ans = 0
while True:
    ans += 1
    if ans % 2 == 1:
        # 奇数回目
        if pop_q():
            pass
        elif n0 > 0:
            n0 -= 1
        else:
            break
    else:
        # 偶数回目
        if n0 > 0:
            n0 -= 1
        elif stop_current_q():
            pass
        else:
            break

print(ans-1)